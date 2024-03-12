from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from habits.models import Habit
from users.models import User

import datetime


'''HABITS TESTS'''


class HabitTestCase(APITestCase):
    '''Тест модели Habit'''

    def setUp(self) -> None:
        '''Создается тестовый пользователь'''
        self.user = User.objects.create_user(
            username='test',
            password='test123'

        )
        '''Аутентификация пользователя'''
        self.client.force_authenticate(user=self.user)

        '''Создается тестовая привычка'''
        self.habit = Habit.objects.create(
            user=self.user,
            place='В кафе',
            time=datetime.time(minute=20).strftime("%Y-%m-%d %H:%M"),
            action='Пить кофе',
            is_nice_habit=True,
            periodicity=1,
            time_to_complete=10,
            is_public=True
        )

    def test_create_habit(self):
        '''Тест CREATE habit'''

        data = {
            'place': 'Дом',
            'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            'action': 'Пить чай',
            'is_nice_habit': False,
            'periodicity': 2,
            'time_to_complete': 120
        }

        habit_create_url = reverse('habits:habit_create')
        response = self.client.post(habit_create_url, data=data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED,
        )
        print(response.json())

        self.assertEqual(
            response.json().get('action'),
            data.get('action')
        )

        self.assertTrue(
            Habit.objects.get(pk=self.habit.pk).action,
            data.get('action')
        )

    def test_list_habit(self):
        '''Тест READ LIST habit'''

        habit_list_url = reverse('habits:habit_list')

        response = self.client.get(habit_list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        print(response.json())

        self.assertEqual(
            Habit.objects.get(pk=self.habit.pk).action,
            response.json().get('results')[0].get('action'))

    def test_list_habit_public(self):
        '''Тест READ LIST Public habit'''
        public_habit_url = reverse('habits:habit_public')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(public_habit_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_habit(self):
        '''Тест READ ONE habit'''

        habit_one_url = reverse('habits:habit_one', args=[self.habit.pk])

        response = self.client.get(habit_one_url)
        print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )

        response = response.json()

        self.assertEqual(response.get('user'), self.user.pk)
        self.assertEqual(response.get('place'), 'В парке')
        # self.assertEqual(response.get('time'), datetime.time(minute=20).strftime("%Y-%m-%d %H:%M"))
        self.assertEqual(response.get('action'), 'Слушать музыку')

    def test_update_habit(self):
        '''Тест UPDATE habit'''

        data = {
            'place': 'updated place',
            'action': 'updated action',
        }

        habit_update_url = reverse('habits:habit_update', args=[self.habit.pk])

        response = self.client.patch(habit_update_url, data)

        print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        response = response.json()

        self.assertEqual(response.get('place'), 'updated place')
        self.assertEqual(response.get('action'), 'updated action')

    def test_delete_habit(self):
        '''Тест DELETE habit'''

        habit_delete_url = reverse('habits:habit_delete', args=[self.habit.pk])

        response = self.client.delete(habit_delete_url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Habit.objects.all().exists(),
        )
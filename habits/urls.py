from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView
from habits.views import PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    # HABITS
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_one'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    # HABITS PUBLIC
    path('public/', PublicHabitListAPIView.as_view(), name='habit_public'),

]
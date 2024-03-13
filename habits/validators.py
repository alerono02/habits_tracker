from rest_framework.serializers import ValidationError


class GoodHabitValidator:
    '''Cвязанная привычка, приятная привычка и награда.'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habit_is_good = dict(value).get('is_good_habit')  # приятная привычка
        habit_is_linked = dict(value).get('associated_habit')  # связанная привычка
        habit_reward = dict(value).get('reward')  # награда

        if habit_is_good and habit_reward is not None:
            raise ValidationError('У приятной привычки нет награды!')

        if habit_is_good and habit_is_linked is not None:
            raise ValidationError('Нельзя выбрать приятную и связанную привычки одновременно!')

        if habit_is_linked and habit_reward is None:
            raise ValidationError('Можно выбрать связанную привычку и награду одновременно!')


class IsGoodHabitValidator:
    '''Связанная привычка - привычка с признаком приятной привычки.'''

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        good_habit = dict(value).get(self.fields)
        if good_habit:
            if not good_habit.is_good_habit:
                raise ValidationError('Связанная привычка может быть только с признаком приятной привычки!')


class TimeHabitValidator:
    '''Время выполнения привычки не должно быть больше 120 секунд'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        lead_time = dict(value).get(self.field)
        if lead_time > 120:
            raise ValidationError('Время выполнения не должно превышать 120 сек!')


class PeriodicHabitValidator:
    '''Нельзя выполнять привычку реже, чем 1 раз в 7 дней.'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    '''Пагинация, 5 элементов на 1 странице, максимальное кол-во страниц - 100'''
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
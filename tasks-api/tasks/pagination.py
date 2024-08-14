from rest_framework.pagination import PageNumberPagination


class TaskPageNumberPagination(PageNumberPagination):
    page_size = 10

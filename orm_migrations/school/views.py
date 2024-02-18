from django.views.generic import ListView
from .models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'school/students_list.html'
    context_object_name = 'object_list'
    ordering = 'group'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('teachers')
        return queryset
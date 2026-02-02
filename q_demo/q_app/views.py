from django.views.generic import ListView
from django.db.models import Q
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"

    def get_queryset(self):
        query = self.request.GET.get("q")
        students = Student.objects.all()

        if query:
            students = students.filter(
                Q(name__icontains=query) | Q(city__icontains=query)
            )

        return students

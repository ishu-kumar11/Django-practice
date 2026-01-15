from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    # class Meta:
    #     db_table = "student_info"   # custom table name
    #     ordering = ["name"]        # auto order by name
    #     verbose_name = "Student"
    #     verbose_name_plural = "Students"

    def __str__(self):
        return self.name

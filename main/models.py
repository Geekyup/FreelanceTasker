from django.db import models

class Project(models.Model):
    title = models.CharField("Название проекта", max_length=200)
    description = models.TextField("Описание")
    deadline = models.DateField("Дедлайн")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title

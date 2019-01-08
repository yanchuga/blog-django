from django.db import models
from django.utils import timezone

#get post class
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    active = models.BooleanField()
    dep = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#get department class
class Department(models.Model):
    Dep1 = 'HR'
    Dep2 = 'TECH'
    Dep3 = 'FINANCE'
    DEP_CHOICES = (
        (Dep1, 'Human Resources'),
        (Dep2, 'Technical'),
        (Dep3, 'Finance'),
    )
    deps = models.CharField(max_length=2,
                                      choices=DEP_CHOICES,
                                      default=Dep1)
    def is_upperclass(self):
        return self.deps in (self.Dep1, self.Dep2)
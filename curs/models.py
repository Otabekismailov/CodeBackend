from django.db import models
from django.utils.text import slugify


class BaseCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name.upper():
            self.slug = slugify(self.name.lower())
        return super().save(force_insert, force_update, using, update_fields)


class Category(models.Model):
    name = models.CharField(max_length=250, null=False, unique=False)
    slug = models.SlugField(max_length=255, blank=True, null=False)
    basecategory = models.ForeignKey(BaseCategory, on_delete=models.CASCADE, related_name='basecategory', )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name.upper():
            self.slug = slugify(self.name.lower())
        return super().save(force_insert, force_update, using, update_fields)


class Courses(models.Model):
    title = models.CharField(max_length=250, null=False, unique=True)
    paragraph = models.TextField()
    images = models.ImageField(upload_to='images/')
    description = models.TextField()
    Duration = models.CharField(max_length=250, null=True)
    teacher = models.CharField(max_length=250, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return self.title


class LessonTopic(models.Model):
    name = models.CharField(max_length=250, null=False)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lessons(models.Model):
    name = models.CharField(max_length=255)

    Duration = models.CharField(max_length=250, null=True)
    topic = models.ForeignKey(LessonTopic, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Upload avartar
class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/%Y/%m', null=True)

class ItemBase(models.Model):
    class Meta:
        abstract = True

    subject = models.CharField(max_length=100, null=False) #not null
    create_date = models.DateTimeField(auto_now_add=True) #chỉ cập nhật thời gian thực khi tạo, lần đầu được tạo ra
    update_date = models.DateTimeField(auto_now=True) #cập nhật thời gian thực khi tạo hoặc đã có sẵn
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='course/%Y/%m', null=True)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Course(ItemBase):
    objects = None

    class Meta:
        unique_together = ('subject', 'category')
    description = models.TextField(null=True, blank=True) #null, blank có thể để trống trong form
    # Khóa ngoại
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subject
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True) #umique : chỉ định giá trị duy nhất trong bảng

    def __str__(self):
        return self.name

class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')
    content = RichTextField()
    #Khóa ngoại
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson')
    #khóa ngoại manytomany
    tags = models.ManyToManyField(Tag, blank=True,null=True)


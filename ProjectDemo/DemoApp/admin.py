from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag
# import 2 thư viện này để sử dụng bộ công cụ nhập liệu
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

#Tạo form nhập liệu, bộ công cụ nhập liệu
class LessonForms(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        # Model cung cắp
        models = Lesson
        # Các trường tương tác
        fields = '__all__'
class LessonAdmin(admin.ModelAdmin):
    # Gán fomr bằng lesonForms ở trên
    form = LessonForms
    list_display = ['id', 'subject', 'create_date', 'course', 'avatar'] #Tùy chỉnh hiển thị các object
    list_filter = ['subject', 'create_date'] #Tạo bộ lọc danh sách
    search_fields = ['subject', 'create_date', 'course__subject'] #tìm kiếm lesson theo tên và ngày tạo
    readonly_fields = ['avatar']

    def avatar(self, lesson):
        return mark_safe("<img src='/static/{url}' width='100px' alt='image lessons'/>".format(url=lesson.image.name, alt = lesson.subject))

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'create_date', 'avatar']
    readonly_fields = ['avatar']

    def avatar(self, course):
        return mark_safe("<img src='/static/{url}' width='120px' alt='image lessons'/>".format(url=course.image.name, alt = course.subject))

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)

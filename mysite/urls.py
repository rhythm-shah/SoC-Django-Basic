from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', views.EmployeeList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
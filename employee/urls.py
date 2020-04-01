from django.urls import path

from . import views
urlpatterns = [
    # /employee/
    path('', views.index, name='index'),
    # /employee/1/
    path('<int:employee_id>/', views.detail, name='detail'),

]
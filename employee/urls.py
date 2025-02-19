
from django.urls import path # type: ignore
from .views import get_employees, create_employee, update_employee, delete_employee, home

urlpatterns = [
    path('employees/', get_employees, name='get_employees'),                                    #get
    path('employees/create/', create_employee, name='create_employee'),                         #post
    path('employees/<int:pk>/update/', update_employee, name='update_employee'),                #put
    path('employees/<int:pk>/delete/', delete_employee, name='delete_employee'),                #delete
    path('', home, name="home")                                                                 #home
]


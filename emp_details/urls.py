
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from emp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees/',views.EmployeeList.as_view())
]

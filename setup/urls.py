from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_cep/', include("via_cep_project.urls"))

]

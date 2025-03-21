# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('bunch01/', include('bunch01.urls'))
]

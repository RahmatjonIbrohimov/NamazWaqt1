from django.contrib import admin
from django.urls import path, include

import WaqtApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WaqtApp.urls'))
]

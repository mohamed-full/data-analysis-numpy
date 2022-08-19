
from django.contrib import admin
from django.urls import path
import appA.allviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appA.allviews.views.index),
    path('excel/', appA.allviews.views.excel),
    path('excel/num', appA.allviews.views.indnum),
    path('excel/numpy', appA.allviews.views.numpy),
]

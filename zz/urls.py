from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BookList.as_view(), name="booklist"),
    path('my/', views.MyList.as_view(), name="mylist"),
    path('form/', views.rps_new, name="rps_new"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
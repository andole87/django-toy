from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BookList.as_view(), name="booklist")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
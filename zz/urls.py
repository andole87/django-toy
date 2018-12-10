from django.urls import include,path

urlpatterns = [
    path('/<int:pk>/', views.booklist, name="booklist")
]

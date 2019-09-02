from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('articles/', views.article_list_create_api_view, name='articles_list'),
    path('articles/<int:pk>/', views.article_detail_api_view, name='articles_detail'),
    path('tourpack/', views.tourpack_list_create_api_view, name='articles_list'),
    path('tourpack/<int:pk>/', views.tourpack_detail_api_view,
         name='articles_detail'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

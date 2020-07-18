from django.urls import path
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from english_learning.views import *

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category_list_url'),
    path('levels/', LevelList.as_view(), name='level_list_url'),
    path('themes/', ThemeList.as_view(), name='theme_list_url'),
    path('themes/<int:pk>/', ThemeDetail.as_view(), name='theme_detail_url'),
    path('words/<int:pk>/', WordDetail.as_view(), name='word_detail_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

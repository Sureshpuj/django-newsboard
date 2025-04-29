
# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', NewsListView.as_view(), name='news_list'),
#     path('news/create/', NewsCreateView.as_view(), name='news_create'),
#     path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
#     path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
#     path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
# ]
from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]

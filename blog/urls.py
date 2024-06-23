from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogUpdateView, BlogDeleteView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path("create/", BlogCreateView.as_view(), name='blog_create'),    #на страницу создания нового блога
    path("", BlogListView.as_view(), name='blog_list'),  # на страницу просмотра всех блогов
    path("view/<int:pk>/", BlogDetailView.as_view(), name='blog_detail'),  # на страницу просмотра блога с переданным id
    path("update/<int:pk>/", BlogUpdateView.as_view(), name='blog_update'),    #на страницу редактирования блога с переданным id
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name='blog_delete'),    #на страницу удаления блога с переданным id
]
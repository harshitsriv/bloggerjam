from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('add_blog/', AddBlogView.as_view(), name= 'add_blog'),
    path('blog/edit/<int:pk>', UpdateBlogView.as_view(), name='edit_blog'),
    path('blog/delete/<int:pk>', DeleteBlogView.as_view(), name='delete_blog'),
    path('category/', CategoryView ,name='category'),
    path('category/<str:cats>', BlogByCategoryView ,name='category_blogs'),
    path('like/<int:pk>', LikeView, name="like_post" )
]
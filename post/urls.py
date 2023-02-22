from django.urls import path
from .views import PostCreate, PostUpdate, SignUpView, HomeView, Post_Details, DraftPost, PostListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostListView.as_view(),name ='index'),
    path('home/', HomeView.as_view(),name ='home'),
    path('create/', PostCreate.as_view(),name ='create'),
    path('update/<int:pk>/', PostUpdate.as_view(),name ='update'),
    path('signup/', SignUpView.as_view(),name ='signup'),
    path('login/', auth_views.LoginView.as_view(template_name ='post/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'index'),name ='logout'),
    path('post_detail/<int:pk>/', Post_Details.as_view(),name ='post_detail'),
    path('draft/', DraftPost.as_view(),name ='draft'),
]
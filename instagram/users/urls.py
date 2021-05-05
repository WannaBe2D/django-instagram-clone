from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.page_profile, name='profile'),
    path('follower/', views.page_follower, name='follower'),
    path('following/', views.page_following, name='following'),
    path('edit_user/', views.EditUser.as_view(), name='edit_user'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('<int:user_id>/user_profile/', views.profile_follower, name='profile_follower'),
    path('<int:user_id>/user_follower/', views.follower, name='user_follower'),
    path('<int:follow_id>/add_following/', views.following_in_user, name='add_following'),
    path('<int:follow_id>/unfollow/', views.unfollow, name='unfollow'),
    path('<int:post_id>/view_post/', views.view_post, name='view_post'),
    path('<int:post_id>/like/', views.like, name='like'),
    path('<int:post_id>/unlike/', views.unlike, name='unlike'),
    path('time_line/', views.time_line, name='time_line'),
    path('activity/', views.activity, name='activity'),
    path('create_post/', views.test_create_post, name='create_post'),
    path('<int:pk>/delete_post/', views.DeletePost.as_view(), name='delete_post'),
    path('search/', views.search, name='search'),
    path('search_profile/', views.SearchProfile.as_view(), name='search_profile'),
    path('<int:post_id>/comments/', views.create_comment, name='comment'),

]

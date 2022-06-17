
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('readblog/<int:id>',views.readblog,name='read'),
    path('sign',views.sign_up,name='sign'),
    path('login/',views.loginuser,name='log'),
    path('profile/',views.userprofile,name='pro'),
    path('logout',views.logoutuser,name='out'),
    path('addpost',views.add_post,name='add'),
    path('contactpage',views.contact,name='con'),
    path('update/<int:id>',views.edit_post,name='edit'),
    path('delete/<int:id>',views.delete_post,name='delete'),
    path('password/',views.changepass,name='changepass'),
    path('aboutpage',views.about,name='about'),
    path('search',views.search,name='search'),
    path('category/<str:cats>',views.category,name='category'),
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('',include('django.contrib.auth.urls')),
    path('readblog/postComment', views.postComment, name="postComment"),
    path('editprofile',views.EditProfile.as_view(), name="editpro"),
    
    # path('profile/<int:pk>',views.Usershowprofile.as_view(), name="userpro"),

]


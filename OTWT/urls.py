from django.contrib import admin
from django.urls import path
from main.views import homepage,share_view,signup,view_login,home, accounts, contacts, aboutus, logout
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # path('', homepage, name="homepage"),
    path('', view_login, name="login"),
    path('homepage/', homepage, name="homepage"),
    path('login/', view_login, name = 'login'),
    path('signup/', signup, name="signup"),
    path('share/', share_view, name='share'),
    path('locate/', home, name='locate'),
    path('accounts/', accounts, name='accounts'),
    path('contacts/', contacts, name = 'contacts'),
    path('about/', aboutus, name = 'aboutus'),
    path('logout/', logout, name='logout'),
 

    path('admin/', admin.site.urls),
]

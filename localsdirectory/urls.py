from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="localsdirectory/index.html"), name="home" ),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('blog/', login_required(TemplateView.as_view(template_name="localsdirectory/blog.html")), name="blog" ),
    path('contact/', TemplateView.as_view(template_name="localsdirectory/contact.html"), name="contact" ),
]

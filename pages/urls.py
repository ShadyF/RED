from django.conf.urls import url
from .views import HomePage

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
]
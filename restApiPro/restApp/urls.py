from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets,
                base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    url(r'hello-views/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]

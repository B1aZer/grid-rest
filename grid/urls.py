from django.conf.urls import patterns, url, include
from rest_framework import routers
from grid import views
from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.SimpleRouter()
#router.register(r'products', views.ProductList)
router.register(r'shops', views.ShopViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.rootview, name='home'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductChange.as_view()),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)



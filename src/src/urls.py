from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from default_post.views import post_view


schema_view = get_swagger_view(
    title='Default Project'
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', schema_view),

    path('', post_view, name='main-page')
]

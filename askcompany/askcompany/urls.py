from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('blog/', include('blog.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/',include(debug_toolbar.urls)),
#
#     ]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]


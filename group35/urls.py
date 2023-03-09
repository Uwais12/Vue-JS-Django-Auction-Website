from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import group35.settings as settings
from authentication.views import health

# static is used to correctly display the static files into the website
static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns = static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+[

    # admin page
    path('admin/', admin.site.urls),
    path('health/', health),

    # path to main app
    path('', include('authentication.urls'))
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/account/", include("apps.account.urls")),
    path("api/v1/product/", include("apps.product.urls")),
    path("api/v1/category/", include("apps.category.urls")),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
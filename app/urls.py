from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register('Trees', views.TreeViewSet)
router.register('Nodes', views.NodeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', views.IndexView.as_view(), name = 'Index'),
    path('Detail/<int:id>', views.TreeDetail.as_view(), name = 'Detail'),
    
    # path('API/', views.api_root),
    path('API/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


from rest_framework import routers
from .api import ProyectoViewSet


router = routers.DefaultRouter()
router.register('api/proyectos', ProyectoViewSet, 'Proyecto' )

urlpatterns = router.urls




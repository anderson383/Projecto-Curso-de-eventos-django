from django.urls import path
from . import views
from django.conf import settings


#Rutas
urlpatterns = [
    path("",views.IndexView.as_view(), name="index"),
    path("panel/",views.PanelView.as_view(), name="panel"),
    path("panel/evento/nuevo",views.CrearEventView.as_view(), name="panel_nuevo"),
    path("panel/evento/<int:pk>/",views.DetalleEventView.as_view(), name="detalle_evento"),
    path("panel/evento/editar/<int:pk>/",views.EditarEventView.as_view(), name="editar_evento"),
    path("panel/evento/eliminar/<int:pk>/",views.EliminarEventView.as_view(), name="eliminar_evento"),

]



#Configuracion de imagenes
if(settings.DEBUG):
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('servicio/nosotros',views.nosotros,name='nosotros'),
    path('servicio/listaServivo',views.listaServicio,name='listaServicio'),
    path('<int:id>/',views.crear_editar,name='crear_editar'),
    path('servicio/eliminar/<int:id>',views.eliminar,name='eliminar'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('pago_servicio/listapago_servicio',views.listapago_servicio,name='listapago_servicio'),
    path('pago_servicio/<int:idpago_servicio/', views.crear_editar_pago_servicio, name='crear_editar_pago_servicio'),
    path('eliminarpago_servicio/<int:idpago_servicio>/',views.eliminapago_servicio,name='eliminapago_servicio'),  

    
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
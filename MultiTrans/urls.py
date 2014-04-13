from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# from Trabajos.views import

# from index import Mostrar
# from Trabajos.views import mostrarTrabajos

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MultiTrans.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index.Mostrar'),
    url(r'^trabajos/$', 'Trabajos.views.mostrarTrabajos'),
    url(r'^proyectos/$', 'Trabajos.views.mostrarProyectos'),
    url(r'^usuarios/$', 'Usuarios.views.mostrarUsuarios'),
    url(r'^trabajos/(?P<titulo>[^/]+)/$', 'Trabajos.views.mostrarTrabajo'),
    url(r'^usuarios/(?P<nombre>[^/]+)/$', 'Usuarios.views.mostrarUsuario'),
)

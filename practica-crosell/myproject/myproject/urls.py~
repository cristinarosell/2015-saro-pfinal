
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from pcrosell.feeds import EventoFeed, TodasFeed, PrinFeed


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC2_URL}),
    url(r'^login$', 'pcrosell.views.login'),
    url(r'^$', 'pcrosell.views.pprincipal'),
    url(r'^todas(?P<path>.*)/rss$', TodasFeed()),
    url(r'^principal(?P<path>.*)/rss$', PrinFeed()),
    url(r'^(?P<nombre>.*)/rss$', EventoFeed()),
    url(r'^ranking$', 'pcrosell.views.ranking'),
    url(r'^listausuarios$', 'pcrosell.views.listausuarios'),
    url(r'^seguir/(.*)$', 'pcrosell.views.seguir'),
    url(r'^dejardeseguir/(.*)$', 'pcrosell.views.dejardeseguir'),
    url(r'^eliminar/(.*)$', 'pcrosell.views.eliminaract'),
    url(r'^votar/(.*)$', 'pcrosell.views.votar'),
    url(r'^comentarios/(.*)$', 'pcrosell.views.vercoment'),
    url(r'^todas$', 'pcrosell.views.todas'),
    url(r'^logout', 'pcrosell.views.milogout'),
    url(r'^actividad/(.*)$', 'pcrosell.views.actividad'),
    url(r'^ayuda$', 'pcrosell.views.ayuda'),
    url(r'^actualizar$', 'pcrosell.views.actualizar'),
    url(r'^elegiract/(.*)$', 'pcrosell.views.elegiract'),
    url(r'^(.*)$', 'pcrosell.views.usuario')
)

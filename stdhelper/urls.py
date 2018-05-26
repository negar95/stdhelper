from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include(('student.urls', 'porsesh'), namespace='porsesh')),
    url(r'^teacher/', include(('teacher.urls', 'pasokh'), namespace='pasokh'))
)

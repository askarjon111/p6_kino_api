from django.contrib import admin
from apps.movies.models import *


admin.site.register(Movie)
admin.site.register(MovieSubtitle)
admin.site.register(MovieAudio)
admin.site.register(MovieFile)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Country)

from django.contrib import admin
from .models import PointsOfInterest
from .models import Streets
from leaflet.admin import LeafletGeoAdmin

class PointsOfInterestAdmin(LeafletGeoAdmin):

   list_display = ('name', 'location')

admin.site.register(PointsOfInterest, PointsOfInterestAdmin)


class StreetsAdmin(LeafletGeoAdmin):

   list_display = ('name', 'location')

admin.site.register(Streets, StreetsAdmin)

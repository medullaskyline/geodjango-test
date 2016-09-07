from django.contrib.gis import forms


class PointForm(forms.Form):
    point = forms.PointField(widget=
        forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))


class WorldBorderForm(forms.Form):
    world = forms.MultiPolygonField(widget =
        forms.OSMWidget(attrs={'map_width': 1024, 'map_height': 600}))
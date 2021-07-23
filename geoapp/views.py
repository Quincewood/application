from django.shortcuts import render, redirect
import os
import folium


def home(request):
    crd_dir = os.path.join(os.getcwd(), 'media', 'crd')
    m = folium.Map(location=[-6.161184, 35.745426], height=2000)

    folium.GeoJson(os.path.join(crd_dir, 'dealers.geojson'), name='dealers', popup=folium.GeoJsonPopup(fields=["Name of respondent"] + ["Region"] + ["Ward"])).add_to(m)


    m = m._repr_html_()
    context = {'my_map': m}
    return render(request, 'geoapp/home.html', context)




import os
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from django.views.generic.edit import FormView
from .forms import WeatherForm

# Create your views here.
class WeatherMainView(FormView):
    template_name = 'weatherform.html'
    form_class = WeatherForm

    def post(self, request, *args, **kwargs):

        city = request.POST.get('city')
        api_key = os.environ.get('API_KEY')
        
        response = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={city}')
        weather_data = response.json()
        current = weather_data.get('current')
        temperature = current.get('temperature')
        description = current.get('weather_descriptions')[0]
        icons = current.get('weather_icons')
        humidity = current.get('humidity')
        uv_index = current.get('uv_index')
        visibility = current.get('visibility')
        country = weather_data.get('location').get('country')
        observation_time = current.get('observation_time')
        wind_speed = current.get('wind_speed')
        precip = current.get('precip')
        wind_dir = current.get('wind_dir')
        form = self.form_class()
        #get the forecast to 5 days
        
        context = {
            'title': 'Weather Main Page',
            'city': city,
            'country': country,
            'temperature': temperature,
            'description': description,
            'icons': icons,
            'humidity': humidity,
            'uv_index': uv_index,
            'visibility': visibility,
            'observation_time': observation_time,
            'wind_speed': wind_speed,
            'form': form,
            'precip': precip,
            'wind_dir': wind_dir,
        }
        
        return render(request, 'weatherform.html', context)
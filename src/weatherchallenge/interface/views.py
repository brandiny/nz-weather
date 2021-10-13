from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from . import services
from .forms import CityForm



# Main view for the page
def interface_view(request):
    default_city = "wellington"

    # If selecting a city, sanitise it. Otherwise - use default
    if request.method == "GET":
        form = CityForm(request.GET)
        if form.is_valid():
            city_name = form.cleaned_data["city"]
        else:
            city_name = default_city

    # Create data to be passed to template
    context = {}
    context["city_name"]        = city_name.title()
    context["city_form"]        = CityForm({"city": city_name})

    weather_data = services.get_weather_data(city_name)
    weather_data = {} if weather_data is None else weather_data

    context["date"]             = "-" if "dt" not in weather_data else services.utc_to_datestring(weather_data["dt"])
    context["temp"]             = "n/a" if "main" not in weather_data else int(round(weather_data["main"]["temp"], 0))
    context["description"]      = "n/a" if "main" not in weather_data else weather_data["weather"][0]["description"].title()
    context["temp_feels_like"]  = "-" if "main" not in weather_data else int(round(weather_data["main"]["feels_like"], 0))
    context["temp_min"]         = "-" if "main" not in weather_data else round(weather_data["main"]["temp_min"], 1)
    context["temp_max"]         = "-" if "main" not in weather_data else round(weather_data["main"]["temp_max"], 1)
    context["pressure"]         = "-" if "main" not in weather_data else round(weather_data["main"]["pressure"], 0)
    context["humidity"]         = "- " if "main" not in weather_data else round(weather_data["main"]["humidity"], 0)
    context["wind_speed"]       = "-" if "wind" not in weather_data else round(weather_data["wind"]["speed"], 0)
    context["wind_gust"]        = "-" if "wind" not in weather_data else round(weather_data["wind"]["gust"], 0)
    context["wind_angle"]       = "-" if "wind" not in weather_data else round(weather_data["wind"]["deg"], 0)
    context["precipitation"]    = "-" if "rain" not in weather_data else round(weather_data["rain"]["1h"], 0)
    context["clouds"]           = "-" if "clouds" not in weather_data else round(weather_data["clouds"]["all"], 0)
    
    context["weather_status"] = "rain"
    if weather_data is not None:
        # In reverse order of importance
        # clouds --> rain --> nighttime
        if context["clouds"] != "-" and context["clouds"] <= 30:
            context["weather_status"] = "fine"

        else:
            context["weather_status"] = "rain"

        if context["precipitation"] != "-" and context["precipitation"] > 10:
            context["weather_status"] = "rain"

        if datetime.now().hour > 18:
            context["weather_status"] = "night"

        
        
        
        
    return render(request, "interface.html", context)


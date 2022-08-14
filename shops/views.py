from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import IceCream

def get_ice_cream(request, ice_cream_id):
    try:
        getIceCream = IceCream.objects.get(id=ice_cream_id)
    except IceCream.DoesNotExist:
        raise Http404("Ice Cream does not exists")
    else:
        context = {
            "IceCream": {
                "name": getIceCream.name,
                "shop": getIceCream.shop.name,
                "stock": getIceCream.stock,
            }
        }
        return render(request, 'ice_cream_detail.html', context)

def get_all_ice_creams(request):
    ice_creams = IceCream.objects.all()
    context = {
        "ice_creams": ice_creams
    }
    return render(request, "ice_cream_list.html", context)
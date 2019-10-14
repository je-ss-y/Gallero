from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Category,Location


# Create your views here.



def pictures_of_day(request):

    pictures = Image.objects.all()
    return render(request, 'all-posts/pictures-today.html', {"pictures":pictures})






def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def onepic(request,pic_id):
    try:
        picture = Image.objects.get(id = pic_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-posts/onepic.html", {"picture":picture})



# def filter_by_location(request, id):
#         location = Location.objects.all()
#         pictures = Image.objects.filter(location__id=id)
#         return render(request, "location.html",{'pictures':pictures,'location':location})


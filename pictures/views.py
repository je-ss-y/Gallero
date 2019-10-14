from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Category,Location


# Create your views here.



def pictures_of_day(request):
    date = dt.date.today()
    pictures = Image.objects.all()
    return render(request, 'all-posts/pictures-today.html', {"date": date,"pictures":pictures})




def past_days_pictures(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-posts/past-pictures.html', {"date": date})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



# def filter_by_location(request, id):
#         location = Location.objects.all()
#         pictures = Image.objects.filter(location__id=id)
#         return render(request, "location.html",{'pictures':pictures,'location':location})


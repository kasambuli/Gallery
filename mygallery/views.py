from django.shortcuts import render
from .models import Image,Category,Location
# Create your views here.
def search_results(request):

    if 'image_category' in request.GET and request.GET["image_category"]:
        searched_category = request.GET.get("image_category")
        images = Image.search_by_category(searched_category)
        message = f"{searched_category}"

        return render(request, 'search.html',{"message":message,"images":images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image_list(request):
    images = Image.image_list()
    return render(request,'index.html',{"images":images})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image, id: image_id})

def location(request):
    location = Image.Nairobi()
    return render(request,"nairobi.html",{"location":location})

def location1(request):
    location = Image.Mombasa()
    return render(request,"mombasa.html",{"location":location})

def location2(request):
    location = Image.Dubai()
    return render(request,"dubai.html",{"location":location})


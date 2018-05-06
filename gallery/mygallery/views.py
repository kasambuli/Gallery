from django.shortcuts import render
from .models import Image
# Create your views here.
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        searched_category = request.GET.get("image")
        searched_images = Image.search_by_category(searched_category)
        message = f"{searched_category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image_list(request):
    images = Image.image_list()
    return render(request,'index.html',{"images":images})

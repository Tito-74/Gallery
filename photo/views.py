from django.shortcuts import render
from django.http import HttpResponse
from photo.models import Category,Location, Post


# Create your views here.
def index(request):
    post=Post.objects.all()
    location = Location.get_locations()

    return render(request,'home.html',{'post':post,'location':location})


def post_location(request):
    post=Post.objects.all()
    location = Location.get_locations()
    # location=Location.get_locations()
    
    return render(request, 'location.html',{'post':post,"location":location})


def post_properties(request,post_id):
    location=Location.get_locations()
    image = Post.get_post_by_id(post_id)
    return render(request, {"image" : image,"location":location})


def search_category(request):
    location=Location.get_locations()
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        search = Post.search_category(category)
        message = f"{category}"
        return render(request, 'search.html',{"message":message,"category": search,"location":location})
    else:
        return render(request, 'search.html')



# def search_results(request):
#     location = Location.get_location()

    
#     if 'category' in request.GET and request.GET["category"]:
#         term = request.GET.get("category")
#         searched = Post.search_results(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',{"message":message,"post": searched,'location':location})

#     else:
#         message = "You haven't searched for any category"
#         return render(request, 'search.html',{"message":message})

#     return render(request,'search.html')
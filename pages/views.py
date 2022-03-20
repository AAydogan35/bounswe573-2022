from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # Control parameters in cmd
    print(args, kwargs)
    print(request)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {}) # "home.html" template name, {} context

# Contect is any data type that you return to the template to be displated at view - data from the BACKEND! cool..

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    my_context = {
        "my_text" : "This is my context",
        "my_number" : 54667,
        "my_list" : [1,234,454]
    }
    return render(request, "contact.html", my_context)
from django.shortcuts import render

# Create your views here.
# render takes a request and then render (put together) our template (MVC -> view, html) 'blog/post_list.html'
def post_list(request):
    return render(request, 'blog/post_list.html', {})
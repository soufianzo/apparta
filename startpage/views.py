from django.shortcuts import render

def post_list(request):
    return render(request, 'startpage/post_list.html', {})
from django.shortcuts import render

from default_post.models import DefaultPost


def post_view(request):
    response_date = {
        'posts': DefaultPost.objects.all()
    }
    return render(request, 'templates/default_index.html', response_date)

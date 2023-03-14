from django.shortcuts import render, redirect


def index_page_view(request):

    context = {}
    return render(request, 'users/index.html', context)
from django.shortcuts import render
from .models import Dictionary


# Create your views here.
def index(request):
    word = request.GET.get('word', ' ')
    if word and word != '':
        # result = Dictionary.objects.filter().all()
        result = Dictionary.objects.filter(english__contains=word).all() or Dictionary.objects.filter(
            uzbek__contains=word).all()
    else:
        result = ''
    return render(request, 'index.html', {'word': word, 'result': result})


def add(request):
    if request.method == 'POST':
        english = request.POST.get('english')
        uzbek = request.POST.get('uzbek')
        Dictionary.objects.create(english=english, uzbek=uzbek)
    return render(request, 'add.html', )


def about(request):
    return render(request, 'about.html')

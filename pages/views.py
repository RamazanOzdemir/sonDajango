from django.shortcuts import render
from .models import Slide,ImageCard
def home(request):
    slides = Slide.objects.all()
    cards = ImageCard.objects.all()

    print('dkdaspşa')
    for slide in slides:
        print(slide.slideImage)
    context = {'slides': slides,'cards':cards}
    return render(request, 'pages/home.html', context)

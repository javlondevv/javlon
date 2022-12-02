from django.shortcuts import render

from self_clothes.models import self_clothes


def main_page(request):
    clothes = self_clothes.objects.all()
    context = {
        'self_clothes': clothes
    }
    return render(request, 'self_clothes/index.html', context)


def product_detail(request, slug):
    cloth = self_clothes.objects.filter(slug=slug).first()
    context = {
        'cloth': cloth
    }
    return render(request, 'self_clothes/detail.html', context)

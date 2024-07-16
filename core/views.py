from django.shortcuts import get_object_or_404, render
from .models import SiteSettings, StaticPage
from content.models import Content
import random


def index(request):
    all_content = Content.objects.all()

    
    trending_contents = all_content.filter(tags__name="Trending")[:7]
    f_con = Content.objects.all().order_by('?').first()
    ff_con = Content.objects.all().order_by('?')[:3]
    fff_con = Content.objects.all().order_by('?')[:3]
    # ffff_con = Content.objects.all().order_by('?')[:6]
    f_con2 = Content.objects.filter(category__name="Fan Fic").order_by('?').first()
    f_con3 = Content.objects.filter(category__name="Fan Fic").order_by('?').first()
    f_con4 = Content.objects.filter(category__name="Fan Fic").order_by('?').first()
    f_con5 = Content.objects.filter(category__name="Fan Fic").order_by('?').first()
    f_con6 = Content.objects.filter(category__name="Fan Fic").order_by('?')[:6]

    cat_1 = Content.objects.all().order_by('?')[:1]
    cat_2 = Content.objects.all().order_by('?')[:1]
    cat_3 = Content.objects.filter(category__name="Fan Fic").order_by('?')[:1]
    # Randomly select 5 items
    random_content = random.sample(list(all_content), min(len(all_content), 5))
    context = {
        'random_content': random_content,
        'trending_contents': trending_contents,
        'f_con': f_con,
        'ff_con': ff_con,
        'fff_con': fff_con,
        # 'ffff_con': ffff_con,
        'f_con2': f_con2,
        'f_con3': f_con3,
        'f_con4': f_con4,
        'f_con5': f_con5,
        'f_con6': f_con6,
        'cat_1':cat_1,
        'cat_2':cat_2,
        'cat_3':cat_3,
    }
    return render(request, 'core/index.html', context)


def static_page_view(request, slug):
    page = get_object_or_404(StaticPage, slug=slug)
    context = {
        'page': page,
        
    }
    return render(request, 'core/static_page.html', context)

def contact_view(request):
    context = {
        
    }
    return render(request, 'core/contact.html', context)

def about_view(request):
    context = {
        
    }
    return render(request, 'core/about.html', context)


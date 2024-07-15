from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Content, Category
from .forms import ContentForm

def content_list(request, category_slug=None, tag_slug=None):
    category = None
    categories = Category.objects.all()
    contents = Content.objects.all().order_by('?')
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        contents = contents.filter(category=category).order_by('?')

    # Fetch tagged contents
    popular_contents = contents.filter(tags__name="Popular").order_by('?')[:7]
    trending_contents = contents.filter(tags__name="Trending").order_by('?')[:7]
    latest_contents = contents.filter(tags__name="Latest").order_by('?')[:7]

    context = {
        'category': category,
        'categories': categories,
        'contents': contents,
        'popular_contents': popular_contents,
        'trending_contents': trending_contents,
        'latest_contents': latest_contents,
    }

    return render(request, 'content/content_list.html', context)

def content_detail(request, slug, category_slug=None, tag_slug=None):
    content = get_object_or_404(Content, slug=slug)
    contents = Content.objects.all()
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        contents = contents.filter(category=category)

    # Fetch tagged contents
    popular_contents = contents.filter(tags__name="Popular").order_by('?')[:7]
    trending_contents = contents.filter(tags__name="Trending").order_by('?')[:7]
    latest_contents = contents.filter(tags__name="Latest").order_by('?')[:7]
    context = {
        'content': content,
        'popular_contents': popular_contents,
        'trending_contents': trending_contents,
        'latest_contents': latest_contents,
        'categories': categories,
    }

    return render(request, 'content/single-post.html', context)

@login_required
def content_create(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.author = request.user
            general_category = Category.objects.get(name='General')
            content.category = general_category
            content.save()
            return redirect('content_detail', slug=content.slug)
    else:
        form = ContentForm()
    return render(request, 'content/content_form.html', {'form': form})

@login_required
def like_content(request, slug):
    content = get_object_or_404(Content, slug=slug)
    if content.likes.filter(id=request.user.id).exists():
        content.likes.remove(request.user)
    else:
        content.likes.add(request.user)
    return redirect('content_detail', slug=slug)

@login_required
def dislike_content(request, slug):
    content = get_object_or_404(Content, slug=slug)
    if content.dislikes.filter(id=request.user.id).exists():
        content.dislikes.remove(request.user)
    else:
        content.dislikes.add(request.user)
    return redirect('content_detail', slug=slug)
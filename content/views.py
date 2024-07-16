from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from content.forms import CommentForm

# from .forms import CommentForm
from .models import Content, Category, Comment

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
    comments = Comment.objects.filter(content=content, parent__isnull=True)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.content = content
            new_comment.save()
            return redirect('content_detail', slug=content.slug)
    else:
        comment_form = CommentForm()

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
        'content': content,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'content/single-post.html', context)


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
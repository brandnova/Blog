from datetime import timedelta
from django.utils import timezone
from io import BytesIO
from django.db.models import Q
# from gtts import gTTS # type: ignore
# from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from content.forms import CommentForm
from .models import Content, Category, Comment
from accounts.utils import assign_badges
from ads.models import Ad
# from accounts.models import Badge


# def text_to_speech(request, slug):
#     content = get_object_or_404(Content, slug=slug)
#     text_content = content.content

#     tts = gTTS(text_content)
#     audio = BytesIO()
#     tts.write_to_fp(audio)
#     audio.seek(0)

#     response = HttpResponse(audio, content_type='audio/mpeg')
#     response['Content-Disposition'] = f'attachment; filename="{content.slug}.mp3"'
#     return response


def content_list(request, category_slug=None, tag_slug=None):
    category = None
    categories = Category.objects.all()
    contents = Content.objects.all().order_by('?')
    ads_base = Ad.objects.filter(placement__name="Base", active=True).first()
    
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
        'ads_base': ads_base,
    }

    return render(request, 'content/content_list.html', context)


def content_detail(request, slug, category_slug=None, tag_slug=None):
    ads = Ad.objects.filter(placement__name="Side Contents", active=True).order_by('?')
    ads_details_top = Ad.objects.filter(placement__name="Top Content", active=True).first()
    content = get_object_or_404(Content, slug=slug)
    contents = Content.objects.all()
    category = None
    categories = Category.objects.all()
    comments = Comment.objects.filter(content=content, parent__isnull=True)
    ads_base = Ad.objects.filter(placement__name="Base", active=True).first()
    
    target_user = content.author
    if request.user.is_authenticated:
        assign_badges(request.user)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.content = content
            new_comment.save()
            assign_badges(request.user)
            return redirect('content_detail', slug=content.slug)
    else:
        comment_form = CommentForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        contents = contents.filter(category=category)

    popular_contents = contents.filter(tags__name="Popular").order_by('?')[:7]
    trending_contents = contents.filter(tags__name="Trending").order_by('?')[:7]
    latest_contents = contents.filter(tags__name="Latest").order_by('?')[:7]

    context = {
        'content': content,
        'popular_contents': popular_contents,
        'trending_contents': trending_contents,
        'latest_contents': latest_contents,
        'categories': categories,
        'comments': comments,
        'comment_form': comment_form,
        'target_user': target_user,
        'ads': ads,
        'ads_details_top': ads_details_top,
        'ads_base': ads_base,
    }

    return render(request, 'content/single-post.html', context)

def search_results(request):
    query = request.GET.get('q')
    content_results = Content.objects.filter(title__icontains=query) | Content.objects.filter(content__icontains=query) | Content.objects.filter(highlight__icontains=query)
    category_results = Category.objects.filter(name__icontains=query)
    ads_base = Ad.objects.filter(placement__name="Base", active=True).first()

    context = {
        'query': query,
        'content_results': content_results,
        'category_results': category_results,
        'ads_base': ads_base,
    }
    return render(request, 'search_results.html', context)


@login_required
def like_content(request, slug):
    content = get_object_or_404(Content, slug=slug)
    if content.likes.filter(id=request.user.id).exists():
        content.likes.remove(request.user)
    else:
        content.likes.add(request.user)
        content.dislikes.remove(request.user)
    return redirect('content_detail', slug=slug)

@login_required
def dislike_content(request, slug):
    content = get_object_or_404(Content, slug=slug)
    if content.dislikes.filter(id=request.user.id).exists():
        content.dislikes.remove(request.user)
    else:
        content.dislikes.add(request.user)
        content.likes.remove(request.user)
    return redirect('content_detail', slug=slug)
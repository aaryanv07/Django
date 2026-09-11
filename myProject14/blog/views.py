from django.shortcuts import render
from django.db.models import Q
from .models import Post

def post_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    # If no category is selected, show no posts
    if not category:
        posts = Post.objects.none()

    else:
        posts = Post.objects.filter(
            category__iexact=category
        ).order_by('-id')

        # Search within selected category
        if query:
            posts = posts.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )

    return render(
        request,
        'blog/post_list.html',
        {
            'posts': posts,
            'query': query,
            'category': category
        }
    )
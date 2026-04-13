from django.shortcuts import render

from products.models import Product, Tag, Category

def product_list(request):
    
    category_id = request.GET.get('category')
    
    tag_ids = request.GET.getlist('tag')
    search_query = request.GET.get('search')
    products = Product.objects.all()

    if search_query:
        products = products.filter(description__icontains=search_query)

    if category_id:
        products = products.filter(category__id=category_id)

    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'tags': tags,
    })
    
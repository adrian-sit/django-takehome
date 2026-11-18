from django.shortcuts import render
from .models import Product, Category, Tag

"""
Product catalog views

Handles category and tag boolean product filtering, 
combined with description search

The initial file structure and view scaffold were AI-generated
Database queries, search logic, and filtering logic are implemented manually
"""

def product_list(request):
    search_query = request.GET.get("q", "").strip()
    selected_categories = request.GET.getlist("categories")
    selected_tags = request.GET.getlist("tags")
    # logic returns "or"(match any) or "and"(match all) with default "or"(match any)
    tag_logic = request.GET.get("tag_logic", "or")
    group_logic = request.GET.get("group_logic", "or")

    # Retrieve all products, categories and tags
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Display all initially, no selection assumes no filter applied
    
    # Categories are 1-to-many relationship with assumed "or" logic
    if selected_categories:
        category_products = products.filter(category_id__in=selected_categories)

    # Filter tags based on "or"/"and" logic
    if selected_tags:
        if tag_logic == "or":
            tag_products = products.filter(tags__id__in=selected_tags)
        else:
            tag_products = products
            for tag_id in selected_tags:
                tag_products = tag_products.filter(tags__id=tag_id)

    # Filter groups based on "or"/"and" logic
    if selected_tags and selected_categories:
        if group_logic == "or":
            products = category_products | tag_products
        else:
            products = category_products & tag_products
    elif selected_categories:
        products = category_products
    elif selected_tags:
        products = tag_products
    # Else no filter returns all objects

    # Remove duplicates
    products = products.distinct()

    # Apply search query
    if search_query:
        products = products.filter(description__icontains=search_query)

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "search_query": search_query,
        "selected_categories": selected_categories,
        "selected_tags": selected_tags,
        "context_key": "value",
        "tag_logic": tag_logic,
        "group_logic": group_logic,
    }

    return render(request, "catalog/product_list.html", context)
def categories(request):
    from mainapp.models import Category
    return {'categories': Category.objects.all()}
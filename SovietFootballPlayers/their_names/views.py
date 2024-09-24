from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Players


def index(request):
    players = Players.objects.all().order_by('-time_create')
    paginate_by = request.GET.get('paginate_by', 3)
    paginator = Paginator(players, paginate_by) # Получаем количество постов на странице. По умолчанию 3.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'paginate_by': paginate_by
    }
    return render(request, 'index.html', context)


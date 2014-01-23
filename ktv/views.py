from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from ktv.models import Article, Category


class IndexView(generic.ListView):
    template_name = 'ktv/index.html'
    context_object_name = 'latest_article_list'
    paginate_by = 25

    def get_queryset(self):
        return Article.objects.order_by('pub_date')

        
class DetailView(generic.DetailView):
    model = Article
    template_name = 'ktv/offcanvas.html'
        

def detail_page(request):
    latest_ktv_list = Article.objects.order_by('pub_date')[:5]
    template = loader.get_template('ktv/index.html')
    context = RequestContext(request, {
        'latest_ktv_list': latest_ktv_list,
    })
    return HttpResponse(template.render(context))


def detail(request, ktv_id):
    ktv = Article.objects.get(pk=ktv_id)
    return render(request, 'ktv/detail.html', {'ktv': ktv})
    
# Create your views here.



















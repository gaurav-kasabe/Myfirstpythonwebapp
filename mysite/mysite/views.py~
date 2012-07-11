# Create your views here.
#from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
def home(request):
    #return HttpResponseRedirect(reverse("poll_results", args=(p.id,)))
    return render_to_response("mysite/index.html")


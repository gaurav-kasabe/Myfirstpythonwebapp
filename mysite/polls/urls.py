from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
  url(r"^$",ListView.as_view(
    queryset=Poll.objects.order_by("-pub_date")[:5],
    context_object_name="latest_poll_list",
    template_name="polls/index.html")),
    
  url(r"^(?P<pk>\d+)/$",DetailView.as_view(
    model=Poll,
    template_name="polls/details.html")),
    
  url(r"^(?P<pk>\d+)/results/$",DetailView.as_view(
    model=Poll,
    template_name="polls/results.html"),
    name="poll_results"),
    
  url(r"^(?P<poll_id>\d+)/vote/$", "polls.views.vote"),
)



#urlpatterns = patterns("polls.views",
    ## Examples:
    ##url(r"^$", "mysite.views.home", name="home"),
    ##url(r"^mysite/", include("mysite.foo.urls")),

    ## Uncomment the admin/doc line below to enable admin documentation:
    ##url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
    #url(r"^$", "index"),
    #url(r"^(?P<poll_id>\d+)/$", "detail"),
    #url(r"^(?P<poll_id>\d+)/results/$", "results"),
    #url(r"^(?P<poll_id>\d+)/vote/$", "vote"),
#)

#urlpatterns += patterns("",
   ## Uncomment the next line to enable the admin:
  #url(r"^admin/", include(admin.site.urls)),
#)

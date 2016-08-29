from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', view.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', view.snippet_detail),
]

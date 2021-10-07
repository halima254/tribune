from django.conf import settings
#import project settings from django.conf module and a static functiom

from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    #when creating new articles, we make changes in the url by deleting welcome route and view
    # url('^$', views.welcome,name='welcome'),
    url(r'^$', views.news_today,name='newsToday'),
    #creating a regex pattern
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name= 'pastNews'),
    url(r'^search/',views.search_results, name = 'search_results'),
    url(r'^article/(\d+)',views.article,name ='article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    #add to url patterns a new static route that references the location to the uploaded files

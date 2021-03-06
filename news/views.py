import datetime as dt
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Article

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def news_today(request):
    #changed later from news_of_today
    date = dt.date.today()
    news = Article.todays_news()
    
    #adding function to convert date object to find exact dayafter creatinga new function covert_dates below
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1> { day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    # 
    return render(request, 'all-news/today-news.html', {"date":date,"news":news})    
    
def convert_dates(dates):
    #function that gets the weekday number for the date
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    #returning the actual day of the week
    day = days[day_number]
    return day   

def past_days_news(request,past_date):
    try:
        
    #converts data from the string Url

         date = dt.datetime.strftime(past_date,'%Y-%m-%d').date()
    except ValueError:
        #raise 404 error when ValueError is thrown
        raise Http404()
        
    day = convert_dates(date) 
    # html= f'''
    #     <html>
    #     <body>
    #     <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
    #     </body>
    #     </html>
    #     '''
    return HttpResponse(html)    

#View function to present news from past days
def past_days_news(request,past_date):
    
    try:
        # converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
        
    except ValueError:
        #Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
        
    if date == dt.date.today():
        return redirect(news_today)
    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date,"news":news})    
        
    #creating a search results view function    
def search_results(request):
    #checking if article query exists in our request.GET
    if 'article' in request.GET and request.GET["article"]:
        #getting our search-term using get method request.GET object
        search_term = request.GET.get("article")
        #call the search_by_title class method and pass user input
        searched_articles=Article.search_by_title(search_term)
        message=f"{search_term}"
        #rendering our html template and pass in the list of articles found and the search term
        return render(request,'all-news/search.html',{"message":message,"articles":searched_articles}) 
    
    else:
        message = "you haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})      
    
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html",{"article":article})     
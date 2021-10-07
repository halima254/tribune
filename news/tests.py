from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt
# Create your tests here.

#creating a test class for the editor model
#it inherits from the testcase class
class EditorTestClass(TestCase):
    #setUp method that allows us to create an instance of the editor class before every test
    #setup method that allows us to define a new editor and a tag instance
    def setUp(self):
        self.james=Editor(first_name='James',last_name='Muriuki',email='james@moringaschool.com')
        
    #testing instance
    def test_instance(self):
        #create test_instance test to confirm that the object is being instantiated correctly
        self.assertTrue(isinstance(self.james,Editor))    
        
    #testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0 )
        
      #create test class  
class ArticleTestClass(TestCase):
    
    def setUp(self):
        #create new editor and saving it
        self.james=Editor(first_name='James',last_name='Muriuki', email='james@moringaschool.com')
        self.james.save_editor()
        #create anew tag and saving it
        self.new_tag=tags(name='testing')
        self.new_tag.save()
        #creating new article and saving it
        self.new_article=Article(title='Test Article',post='A random test post', editor=self.james)
        self.new_article.save()
        self.new_article.tags.add(self.new_tag)
        
    def tearDown(self):
        #this method allow us to delete all instances of our models from the db after each test
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
            ###article and tags share a many to many relationship
            #i.e, for us to create more a join table where we need the id property of both models instances
            #ediror and article ahsre a one to many relationship, we have to save the editor instances first then equate it to the editor field in the article model
            
            #frot the many to many relationship, we create a join table with the id of both model instances. we first save both tags and article instance to thedb then use the add function on the many to many fields to add a new tag.
            
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)   
        
    def test_get_news_by_date(self):
        test_date='2020-10-06'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()  
        news_by_date= Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)       
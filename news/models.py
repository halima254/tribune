from django.db import models
import datetime as dt

# Create your models here.
#first model; editor model, this contains details of the editor of the article
class Editor(models.Model):
    #edito class inherits from tje modules.Model class
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.first_name
    #save_editor defines the method to be tested
    def save_editor(self):
        self.save()
    class Meta:
        ordering = ['first_name']
    #above are three class variables that represent different columns in our database
    # we use field objects to define what sort of data the database will store
    #charfiels is sql equivalent to varchar in stringfiels, for small to large sized strings
    #max_lenth requirement passed by Charfield.
    #Emailfiels is a charfields that checks that the valuei is a valid email adress.
    
class tags(models.Model):
    #creating a tag model
    name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.name 
    
#creating article model
class Article(models.Model):
    #title will contain the title
    title = models.CharField(max_length=60)
    #post will contain the post
    post = models.TextField()
    #we create models.foreign key. this will create a foreign key column that will store the id of the editor from the editor table
    editor = models.ForeignKey('Editor',on_delete=models.CASCADE) 
    #we create many to many field named tags. This many to many fields tells django to create a separate join table.
    #This new table handles mapping between articles to tags
    #the table handles mapping between articles to tags
    tags = models.ManyToManyField(tags)
    #adding time-stamp    
    pub_date = models.DateTimeField(auto_now_add= True)  
    #datetime stores exact date and time the article is posted.
    #auto_now_Add = true; automatically saves exact time and date to the db as we save the model
    article_image = models.ImageField(upload_to ='articles/', null=True)
    #image field takes in the upload_to article which defines where the image will be stored in the file system
    
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news=cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date=date)
        return news  
    @classmethod
    #the def method allows us to filter all the articles in our db and return ones matching our search query
    def search_by_title(cls,search_term):
        #__i contains query filter checks if any word in the titlr field of our article matches the search_term
        news=cls.objects.filter(title__icontains=search_term)
        return news
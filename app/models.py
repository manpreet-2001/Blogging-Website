
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return   str(self.name)




class blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return   str(self.id)  + ' | ' +  self.title + ' | ' + str(self.author)
         
    title = models.CharField(max_length=250)
    desc = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="postimages")
    head0 = models.CharField(max_length=400)
    shead0 = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50)


   
    
class contact(models.Model):
    name = models.CharField(max_length=150)
    email= models.EmailField(max_length=254) 
    desc = models.CharField(max_length=400)

    def __str__(self):
        return  str (self.desc)

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(blog, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    post_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username




  
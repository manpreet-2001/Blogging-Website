
from .models import contact,blog,category
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User
from django import forms



class signupform(UserCreationForm):
     class Meta:
        model=User
        fields =['username','first_name','last_name','email','password1','password2']
        labels={'email': 'Email','password1': 'Password', 'password2': 'Confirm Password'}
    
choices= category.objects.all().values_list('name','name')

choices_list=[]

for item in choices:
    choices_list.append(item)



class Blogform(forms.ModelForm):
    class Meta:
        model=blog
        fields=[ 'author','title','desc','photo','head0','shead0','author','category']
        labels={ 'author':'Author','title':'Title', 'desc':'Description','head0':'Sub-title','shead0':'Sub-description' ,'photo':'Images','category':'Category'}
        widgets={'desc':forms.Textarea(),'shead0':forms.Textarea(),'category':forms.Select(choices=choices)}

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email','desc']
        labels={'name':'Name', 'email':'Email','desc':'Message'}
        widgets={
            'name':forms.TextInput(attrs={'class':'input','placeholder':'Your Name', 'label_suffix' :'- '}),
            'email':forms.EmailInput(attrs={'class':'input','placeholder':'you@gmail.com'}),
            'desc':forms.Textarea(attrs={'class':'textarea','rows':6,'placeholder':'Your message'})    
        }
    

class EditUserform(UserChangeForm):

    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',}))
    first_name =forms.CharField(max_length=100 ,widget=forms.TextInput (attrs={'class':'form-control'}))
    last_name =forms.CharField(max_length=100 ,widget=forms.TextInput (attrs={'class':'form-control'}))
    username =forms.CharField(max_length=100 ,widget=forms.TextInput (attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields =['username','first_name','last_name','email','password' ]
        labels={'email': 'Email','password': 'Password', 'username':'Username','first_name':'First Name'}
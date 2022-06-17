
from django.shortcuts import  get_object_or_404, render,HttpResponseRedirect
from .models import blog ,category as cat ,BlogComment
from .forms import signupform,Blogform,contactform,EditUserform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash 
from django.contrib.auth.models import User
from . templatetags import extras
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy

# HOME
def home(request):
    # posts=blog.objects.all()
    posts = blog.objects.order_by('-id')
    cate = cat.objects.all()
    return render(request,'home.html',{'posts':posts,'cate':cate})


# BLOG CONTINUE
def readblog(request ,id):
        post=blog.objects.all()
        cate = cat.objects.all()

        post =blog.objects.get(pk=id)
        comments= BlogComment.objects.filter(post=post ,parent=None)
        replies= BlogComment.objects.filter(post=post).exclude(parent=None)
        replyDict={}
        for reply in replies:
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno] = [reply]
            else:
                replyDict[reply.parent.sno].append[reply]
    
        cate = cat.objects.all()
        
    
        return render(request,'blogcontinue.html',{'post':post ,'cate':cate,'comments':comments ,'replyDict':replyDict})   


# SIGNUP
def sign_up(request):
    if request.method=="POST":
        fm = signupform(request.POST)
        if fm.is_valid(): 
         fm.save()      
         messages.success(request,'Your Account has been Created Succesfully !!')  
         return HttpResponseRedirect('/log/')

    else:
        
     fm= signupform() 
    return render(request,'signup.html',{"form":fm})


# LOGIN

def loginuser(request):
    if not request.user.is_authenticated:  
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
             uname=fm.cleaned_data['username']
             upass=fm.cleaned_data['password']
             user=authenticate(username=uname,password=upass)
             if user is not None:
                login(request,user)

                messages.success(request,'You Logged in Successfully!!')
                return HttpResponseRedirect('/profile/')             
        else:
          fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/') 



 # USER_PROFILE

def userprofile(request):
    
    if request.user.is_authenticated:  
        
        posts= blog.objects.all()


        return render (request,'dashboard.html',{'name':request.user, 'posts':posts})
    else:
     return HttpResponseRedirect('/login/')       


# LOGOUT 

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')

# ADD POST

def add_post(request):
    cate=cat.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
         form = Blogform(request.POST, request.FILES)
         if form.is_valid:
             form.save()
             messages.success(request,'Your Blog Post has been Added !!')
             return HttpResponseRedirect('/profile/')

        else:
          form = Blogform()         

        return render(request,'add.html',{'form':form ,'cate':cate})
    else:
     return HttpResponseRedirect('login')    

# CONTACT PAGE

def contact(request):
     
    
        if request.method == 'POST':
         form = contactform(request.POST)
        
        
         if form.is_valid: 
             form.save()
             form= contactform()
             messages.success(request,'Your Message has been Shared !!')

        else:
             form = contactform()         
             
        return render(request,'contact.html',{'form':form})

# EDIT POST

def edit_post(request , id):

    if request.user.is_authenticated:
        if request.method == 'POST':
            pi =blog.objects.get(pk=id)
            form=Blogform(request.POST, request.FILES, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,'Your Blog Post has been Updated !!')
                return HttpResponseRedirect('/')
        else:
            pi=blog.objects.get(pk=id)
            form=Blogform(instance=pi)        
        
        return render(request,'update.html',{'form':form})
    else:
     return HttpResponseRedirect('login')        

# DELETE POST

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=blog.objects.get(pk=id)
            pi.delete()
            
        return HttpResponseRedirect('/profile/')
    else:
     return HttpResponseRedirect('login')

# CHANGE PASSWORD with old pass

def changepass(request):
    if  request.user.is_authenticated: 
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user) 
                messages.success(request,"Your Password has been changed!!")
                return HttpResponseRedirect('/profile/')
        else:        
         fm=PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form':fm})    
    else:
        return HttpResponseRedirect('login')    

# ABOUT PAGE

def about(request):
    
    return render(request,'about.html')       

# SEARCH

def search(request):
    query=request.GET['query']
    if len(query)>78:
        posts=blog.objects.none()
    else:
        poststitle= blog.objects.filter(title__icontains=query)
        postsdesc =blog.objects.filter(desc__icontains=query)
        category=blog.objects.filter(category__icontains=query)
        posts=  poststitle.union(postsdesc).union(category)
    if posts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'posts': posts,'query':query}
    return render(request,'search.html',params)


# CATEGORY
def category(request,cats):
    category_post=blog.objects.filter(category=cats)
    cate = cat.objects.all()
    return render(request,'category.html',{'cats':cats,'category_post':category_post,'cate':cate})

# COMMENTS
def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postId =request.POST.get('postId')
        blo= blog.objects.get(id = postId)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=blo)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=blo , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        # comment=BlogComment(comment= comment, user=user, post=blo)
        # comment.save()
        
    return  HttpResponseRedirect('/')


 # EDIT PROFILE
class EditProfile(generic.UpdateView):
    form_class= EditUserform
    template_name= 'Edit_profile.html'
    success_url = reverse_lazy('home')
    
    
    def get_object(self):
     return self.request.user









# class Usershowprofile(DetailView):      
#     model= Profile
#     template_name='Userprofile.html'

#     def get_context_data(self,*args ,**kwargs):
#         user=Profile.objects.all()
#         context= super(Usershowprofile,self).get_context_data(*args ,**kwargs)
#         page_user = get_object_or_404(Profile, id=self.Kwargs['pk'])

#         context['page_user']= page_user
#         return context


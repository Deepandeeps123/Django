from django.shortcuts import render,redirect
from django.http import HttpResponse


def first(request):
    return render(request,'first.html')



def password_validation(password):
    u_count=0
    l_count=0
    n_count=0
    s_count=0
    if len(password)>=8:
        for i in password:
            if i.isupper():
                u_count+=1
            elif i.islower():
                l_count+=1
            elif i.isdigit():
                n_count+=1
            else:
                s_count+=1
        if u_count>0 and l_count>0 and n_count>0 and s_count>0:
            return True
        else:
            return False
    else:
        return False
    
    
from demo.models import customers

def signup(request):
    return redirect(request,'signup.html')
    # return redirect('/')


def submit(request):
    # return HttpResponse("Scuccess")
    name=request.POST.get('name')
    phone=request.POST.get('phno')
    password=request.POST.get('pass')
    i=request.FILES['image']
    f=request.FILES['file']
    # return HttpResponse("Success")
    
    if password_validation(password) and len(phone)==10:
        details=customers(
            name=name,
            phone=phone,
            password=password,
            image=i,
            resume=f
            
        )
        details.save()
        return render(request,'first.html')
    else:
        return HttpResponse("Password Validation Wrong")
    
    
    
    
    
    
    
    
    
    
    
    
def login(request):
    return render(request,'login.html')

def verify(request):
    user_name=request.POST.get('name')
    password=request.POST.get('pass')
    
    validate=customers.objects.all()
    for i in validate:
        if i.name==user_name:
            check=customers.objects.filter(name=user_name)
            for i in check:
                if i.password==password:
                    # return HttpResponse("Hello")
                    # ! 
                    # return render(request,'homepage.html',{'d':validate})
                    
                    # !
                    return render(request,'homepage.html')
            else:
                # return HttpResponse("Wrong Password")
                return render(request,'login.html',{'error':'username or password is wrong'})
            
            
            
    # !
    # else:
    #     return render(request,'signup.html') 
    
    # !
    
    
def home(request):
    return render(request,'home.html')    
    
    
    
def about(request):
    return render(request,'about.html')



def document(request):
    return render(request,'document.html')







def signup_regdirect(request):
    return render(request,'signup.html')

# login page
# photo and resume view



# ! photo



def photo(request):
    a=customers.objects.all()
    return render(request,'photo.html',{'res':a})



    
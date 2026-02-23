from django.shortcuts import render,redirect
from app.models import Student,department,employee
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        p=req.POST.get('password')
        cp=req.POST.get('cpassword')
        user=Student.objects.filter(Email=e)
        if user:
           msg="Email is Already Existd"
           return render(req,'register.html',{'msg':msg})
        else:
            if p==cp:
              Student.objects.create(
                Name=n,
                Email=e,
                Password=p,
                Cpassword=cp,
              )
              return redirect('login')
            else:
                user={'name':n,'email':e}
                msg="Password & Confirm Password not matched"
                return render(req,'register.html',{'userdata':user,'pmsg':msg})   
    else:    
     return render(req,'register.html')
    




def login(req):
    if req.method=='POST':
        e=req.POST.get('email')
        p=req.POST.get('password')
        user=Student.objects.filter(Email=e)

        if e=='admin@gmail.com' and p=='admin':
            a_data={
                'id':1,
                'name':'Admin',
                'email':'admin@gmail.com',
                'password':'admin',
                'image':'images/img.jpg',
            }
            req.session['a_data']=a_data
            return redirect('admindashboard')

        else:
            # user=Student.objects.filter(Email=e)
            # if not user:
            #    msg="Register First"
            #    return redirect('registation')
            # else:
            #    userdata=Student.objects.get(Email=e)
            #    if p==userdata.Password:
            #       req.session['user_id']=userdata.id
            #       return redirect('userdashboard')
            #    else:
            #       msg="Email & Password not matched"
            #       return render(req,'login.html',{'x':msg})

            employee=employee.objects.filter(eemail=e)
            if employee:
                emp_data=employee.objects.get(eemail=e)
                if p==emp_data.ecode:
                    req.session['emp_id']=emp_data.id
                    return redirect('empdashboard')   # ✅ RETURN ADDED
                else:
                    messages.warning(req,'Email and pass not match')
                return redirect('login')   
            else:
                messages.warning(req,'Employee does not exist ')
            return redirect('login')

    # ✅ YE LINE MISSING THI (GET REQUEST FIX)
    return render(req,'login.html')
           

def userdashboard(req):
    if 'user_id' in req.session:
        x=req.session.get('user_id')
        userdata=Student.objects.get(id=x)
        return render(req,'userdashboard.html',{'data':userdata})
    return redirect('login')

def logout(req):
    if 'user_id' in req.session:
        req.session.flush()
        return redirect('login')

    return redirect('login')

def admindashboard(req):
   if 'a_data' in req.session:
      a_data=req.session.get('a_data')
      return render(req,'admindashboard.html',{'data':a_data})
   else:
      return redirect('login')
   

def login1(req):
   return render(req,'login1.html')


def add_dept(req):
    if 'a_data' in req.session:
      a_data=req.session.get('a_data')
      return render(req,'admindashboard.html',{'data':a_data,'add_dept':True})
    else:
      return redirect('login')
    
def save_dept(req):
    if 'a_data' in req.session:
      if req.method=='POST':
         dn=req.POST.get('deptname')
         dd=req.POST.get('deptdes')
         dh=req.POST.get('depthead')
         dept=department.objects.filter(dname=dn)
         if dept:
            messages.warning(req,'Department already exist')
            a_data=req.session.get('a_data')
            return render(req,'admindashboard.html',{'data':a_data,'add_dept':True})
         else:
            department.objects.create(dname=dn,ddes=dd,dhead=dh)
            messages.success(req,'Department Created')
            a_data=req.session.get('a_data')
            return render(req,'admindashboard.html',{'data':a_data,'add_dept':True})
      return redirect('add_dept')
    else:
        return redirect('login')
    

def show_dept(req):
   if 'a_data' in req.session:
      a_data=req.session.get('a_data')
      #Department model
      all_dept=department.objects.all()
      return render(req,'admindashboard.html',{'data':a_data,'show_dept':True,'all_dept':all_dept})
   else:
      return redirect('login')
   
def add_emp(req):
    if 'a_data' in req.session:
      a_data=req.session.get('a_data')
      all_dept=department.objects.all()
      return render(req,'admindashboard.html',{'data':a_data,'add_emp':True,'all_dept':all_dept})
    else:
      return redirect('login')

def show_emp(req):
   if 'a_data' in req.session:
      a_data=req.session.get('a_data')
      #Department model
      all_dept=employee.objects.all()
      return render(req,'admindashboard.html',{'data':a_data,'show_emp':True,'all_dept':all_dept})
   else:
      return redirect('login')

def save_emp(req):
    if 'a_data' in req.session:
      if req.method=='POST':
         en=req.POST.get('name')
         ec=req.POST.get('contact')
         ee=req.POST.get('email')
         ed=req.POST.get('dept')
         ec=req.POST.get('code')
         ep=req.FILES.get('file')
         emp=employee.objects.filter(eemail=ee)
         if emp:
            messages.warning(req,'Employee already exist')
            a_data=req.session.get('a_data')
            all_dept=department.objects.all()
            return render(req,'admindashboard.html',{'data':a_data,'add_emp':True,'all_dept':all_dept})
         else:
            employee.objects.create(ename=en,econtact=ec,eemail=ee,edep=ed,ecode=ec,eprofile=ep,)
            messages.success(req,'Employee Created')
            send_mail(
               'You are now an employee',
               f'Confirmation name:{en},email:{ee},contact:{ec},dept:{ed},deptcode:{ec},image:{ep}',
               'govindpatel4823@gmail.com',[ee],
               fail_silently=False
            )
            a_data=req.session.get('a_data')
            all_dept=department.objects.all()
            return render(req,'admindashboard.html',{'data':a_data,'add_emp':True,'all_dept':all_dept})
      return redirect('add_dept')
    else:
        return redirect('login')
     
def empdashboard(req):
   if 'emp_id' in req.session:
      pass
   else:
      return redirect('login')
   
def empdashboard(req):
   return render(req,'empdashboard.html')
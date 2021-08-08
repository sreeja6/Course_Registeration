from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import Course,Student,Enrolldetails
def main_page(request):
    return render(request,"main_page.html")


def admin_login(request):
    return render(request,"admin_login.html")
def admin_sucess_login(request):
    us = request.POST.get("a1")
    ps = request.POST.get("a2")
    print(us,ps)
    if us == 'admin' and ps == 'admin':
        return render(request, "admin_page.html")
    else:
        messages.error(request, "invalid username or password")
        return redirect('main')
def schedule_class(request):
    return render(request,"schedule_class.html")
def schedule_sucessfully(request):
    N = request.POST.get("s1")
    Fa = request.POST.get("s2")
    Da = request.POST.get("s3")
    T = request.POST.get("s4")
    Fe = request.POST.get("s5")
    Du = request.POST.get("s6")
    Course(Name=N,Faculty=F,Date=Da,Time=T,Fee=F,Duration=Du).save()
    return redirect('schedule_class')
def view_all_schedule_classes(request):
    return render(request,"view_all_schedule_classes.html",{"view":Course.objects.all()})
def student_page(request):
    return render(request,"student_page.html")
def student_registeration(request):
    return render(request,"student_registeration.html")

def student_register_sucessfully(request):
    na = request.POST.get("sr1")
    ct = request.POST.get("sr2")
    em = request.POST.get("sr3")
    pas = request.POST.get("sr4")

    Student(Name=na,Contact=ct,Email=em,Password=pas).save()
    return redirect('student_registeration')
def student_login(request):
    return render(request,"student_login.html")
def student_login_check(request):
    u = request.POST.get('l1')
    p = request.POST.get('l2')
    try:
      res = Student.objects.get(Name=u,Password=p)
      request.session['user'] = res.Contact
      return render(request,"student_sucessfully_login.html",{"data":res})
    except Student.DoesNotExist:
        messages.error(request,"invalid username or password")
        return redirect('student_login')
def enroll_the_course(request):
    return render(request,"enroll_the_course.html",{"data": Course.objects.all()})
def student_enroll_sucess(request):
    cn = request.POST.get("s1")
    cname = request.POST.get("s2")
    Enrolldetails(Student_contact=cn,Course_name=cname).save()

    return redirect('enroll_the_course')
def view_all_enrolled_courses(request):
    i = request.GET.get("no")
    result = Student.objects.get(No=i)
    ct = result.Contact
    print(ct)
    enroll = Enrolldetails.objects.filter(Student_contact=ct)
    return render(request, "view_respective_enroll.html", {"enr": enroll})













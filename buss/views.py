import datetime
import json

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here.



def login(request):
    return render(request,'index.html')


def login_btn(request):
    print(request.POST)
    try:
        uname=request.POST['Username']
        passwd=request.POST['Password']
        ob=login_table.objects.get(username=uname,password=passwd)
        request.session['lid']=ob.id
        if ob.type == 'admin':
            return HttpResponse('''<script>alert('Welcome');window.location='/adminhome'</script>''')

        elif ob.type == 'bus_owner':
            print('gggggggggggggggggg')
            return HttpResponse('''<script>alert('Welcome');window.location='/busowner_homepage'</script>''')

        else:
            return HttpResponse('''<script>alert('invaild login request');window.location='/'</script>''')

    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert('Invalid username or password');window.location='/'</script>''')

def add_notification(request):
    return render(request, 'admin/add notification.html')

def add_notification_post(request):
    notification=request.POST['textfield2']
    details=request.POST['textfield']

    noti = notification_table()
    noti.notification = notification
    noti.details = details
    noti.date = datetime.datetime.now().date()
    noti.save()
    return HttpResponse('''<script>alert('notification added successfully ');window.location='/admin_view_notification'</script>''')


def admin_view_notification(request):
    ob=notification_table.objects.all()
    return  render(request,'admin/Notification.html',{"data":ob})





def add_route(request):
    return render(request, 'admin/add_route.html')
def add_route_post(request):
    from_rout = request.POST['from']
    to_rout = request.POST['to']

    addingroute = route_table()
    addingroute.from_rout = from_rout
    addingroute.to_rout = to_rout

    addingroute.save()
    return HttpResponse('''<script>alert('Bus stop added successfully ');window.location='/manage_bus_route';</script>''')

def adminhome(request):
    return render(request, 'admin/adminindex.html')

def busownerreg(request):
    return render(request, 'admin/busowner_registration.html')




def busownerreg_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    username = request.POST['textfield7']
    password =request.POST['textfield8']

    login = login_table()
    login.username = username
    login.password = password
    login.type = 'bus_owner'
    login.save()

    profile = busowner_table()
    profile.login = login
    profile.name = name
    profile.phone = phone
    profile.email = email
    profile.place = place
    profile.post = post
    profile.pin = pin

    profile.save()
    return HttpResponse('''<script>alert('Bus owner added successfully ');window.location='/adminhome'</script>''')


def view_bussowner(request):
    ob=busowner_table.objects.all()
    return render(request,'admin/VIEW BUS OWNER.html',{'val':ob})





def manage_bus_route(request):
    ob=route_table.objects.all()
    return render(request,'admin/manage_bus_route.html',{'val':ob})


def manage_bus_route_delete(request,id):
    ob=route_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/manage_bus_route"</script>''')


def view_bussowner_delete(request,lid):
    ob=busowner_table.objects.get(login=lid)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/view_bussowner"</script>''')


def sendreply(request,id):
    com=complaint_table.objects.get(id=id)
    return render(request,'admin/Send_reply.html',{'data':com})

def sendreply_post(request):
    sendreply=request.POST['textfield']
    data=request.POST['data']
    reply_data=complaint_table.objects.get(id=data)
    reply_data.reply=sendreply
    reply_data.save()
    return HttpResponse('''<script>alert("reply send successfully");window.location='/viewcomplaints'</script>''')




def stopadd(request):
    ob=route_table.objects.all()
    return render(request,'admin/stop_add.html',{"rout":ob})


def stopadd_post(request):

    route = request.POST['select']
    stopname = request.POST['textfield2']
    fair = request.POST['textfield3']
    stage = request.POST['textfield4']
    latitude = request.POST['textfield42']
    longitude= request.POST['textfield43']

    addstop = stop_table()
    addstop.route_id=route
    addstop.stopname=stopname
    addstop.fair=fair
    addstop.stage=stage
    addstop.latitude=latitude
    addstop.longitude=longitude
    addstop.save()
    return HttpResponse ('''<script>alert('Bus route added successfully ');window.location='/stopmangmnt'</script>''')



def stopmangmnt(request):
    ob=stop_table.objects.all()
    return render(request,'admin/stop_managment.html',{"rout":ob})

def userinformtion (request):
    ob=user_table.objects.all()
    return render(request,'admin/user_information.html',{"val":ob})

def accept_owner(request,id):
    ob=login_table.objects.get(id=id)
    ob.type="bus_owner"
    ob.save()
    return HttpResponse ('''<script>alert('Accepted successfully ');window.location='/verifybusowner'</script>''')



def reject_owner(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = "Rejected"
    ob.save()
    return HttpResponse('''<script>alert('Accepted successfully ');window.location='/verifybusowner'</script>''')


def vrfyroute(request):
    return render(request,'admin/verify route request.html')

def verifybusowner(request):
    ob=busowner_table.objects.filter(login__type='pending')
    return render(request,'admin/verifybusowner.html' , {"val":ob})

def delete_new_owner(request,id):
    ob=busowner_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("trip deleted");window.location="/verifybusowner"</script>''')


def new_owner_reg(request):
    return render(request,'admin/newbusower.html')

def new_owner_reg_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    username = request.POST['textfield7']
    password =request.POST['textfield8']

    login = login_table()
    login.username = username
    login.password = password
    login.type = 'pending'
    login.save()

    profile = busowner_table()
    profile.login = login
    profile.name = name
    profile.phone = phone
    profile.email = email
    profile.place = place
    profile.post = post
    profile.pin = pin

    profile.save()
    return HttpResponse('''<script>alert('request send successfully ');window.location='/'</script>''')


def viewinformation(request):
    return render(render,'admin/view information.html')

def viewtiming(request):
    return render(request,'admin/view timing.html')

def viewcomplaints(request):
    ob=complaint_table.objects.all()
    return render(request,'admin/view_complaints.html',{"com":ob})

def viewfeedback(request):
    kk=bus_table.objects.all()
    ob=feedback_table.objects.all()
    return render(request,'admin/View_feedback.html',{"val":ob,"bus":kk})

def viewfeedbacksearch(request):
    kk = bus_table.objects.all()
    bus=request.POST['bus']
    ob=feedback_table.objects.filter(bus__id=bus)
    return render(request,'admin/View_feedback.html',{"val":ob,"bus":kk})

def search_bus_stops(request):
    stop=request.POST['select']
    ob=stop_table.objects.filter(route__id=stop)
    return render(request,'admin/stop_managment.html',{'rout':ob,'stop':stop})


# def searchstopmangmnt(request):
#     route=request.POST['select']
#     ob=stop_table.objects.filter(route__icontains=route)
#     return render(request,'admin/stop_managment.html',{"rout":ob})

def add_bus_to_route(request):
    ob=route_table.objects.all()
    ob1=bus_table.objects.filter(bus_owner__login_id=request.session['lid'])
    ob2=trip_table.objects.all()
    return render(request,'owner/add bus to route.html',{'rout':ob,'bus':ob1,'trip':ob2})

def add_buss_post(request):
    print(request.POST,'jjjjjjjjjjj')
    name=request.POST['textfield']
    regno=request.POST['textfield2']
    fitness=request.POST['textfield3']
    insurance=request.POST['textfield4']
    rcbook=request.FILES['file2']

    photo=request.FILES['file']



    fs = FileSystemStorage()
    fp = fs.save(photo.name, photo)
    df = fs.save(rcbook.name, rcbook)

    obb=bus_table()
    obb.bus_owner = busowner_table.objects.get(login__id=request.session['lid'])
    obb.name = name
    obb.regno = regno
    obb.fitness = fitness
    obb.insurance= insurance
    obb.rcbook= df
    obb.image=fp
    obb.save()
    return HttpResponse('''<script>alert("bus added sucessfully");window.location='/managebus';</script>''')


def add_bus(request):
    return render(request,'owner/add  bus.html')

def addemploye(request):
    return render(request,'owner/add employye.html')



def addemploye_post(request):
    name=request.POST['textfield']
    dob=request.POST['textfield2']
    phoneno=request.POST['textfield3']
    email=request.POST['textfield4']
    place=request.POST['textfield5']
    post=request.POST['textfield6']
    pin=request.POST['textfield7']
    image=request.FILES['file']
    license=request.POST['textfield10']
    username=request.POST['textfield8']
    password=request.POST['textfield9']

    fs=FileSystemStorage()
    fp=fs.save(image.name,image)


    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type="employee"
    ob.save()

    obb=employee_table()
    obb.name=name
    obb.dob=dob
    obb.phoneno=phoneno
    obb.email=email
    obb.place=place
    obb.post=post
    obb.license=license
    obb.pin=pin
    obb.image=fp
    obb.owner=busowner_table.objects.get(login__id=request.session['lid'])
    obb.login=ob
    obb.save()
    return HttpResponse('''<script>alert("employee added sucessfully");window.location='/manageemploye';</script>''')








def addtime(request):
    ob=stop_table.objects.all()
    return render(request,'owner/add time.html' , {'val':ob})


def assignemployee(request,id):
    request.session['eid']=id
    bus=bus_table.objects.filter(bus_owner__login_id=request.session['lid'])
    return render(request,'owner/assign employee.html',{'bus':bus})
#
def add_assignemployee_post(request):
    bus=request.POST['select']
    emp=request.session['eid']
    status='pending'
    date=datetime.datetime.today()

    ob=assign_table()
    ob.bus_id=bus
    ob.employe_id=emp
    ob.status=status
    ob.date=date
    ob.save()
    return HttpResponse('''<script>alert("employee assigned sucessfully");window.location='/manageemploye';</script>''')

def view_assignedemp(request):
    ob = assign_table.objects.all()
    return render(request,'owner/assigned employee.html',{"val":ob})

def delete_assignedemp(request,id):
    ob=assign_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/view_assignedemp"</script>''')


def busowner_homepage(request):
    return render(request,'owner/index.html')

def managebus(request):
    ob=bus_table.objects.all()
    return render(request,'owner/manage bus.html',{'val':ob})

def manageemploye(request):
    ob=employee_table.objects.filter(owner__login_id=request.session['lid'])
    return render(request,'owner/manage employe.html',{"val":ob})

def trip(request):
    ob = trip_table.objects.all()
    return render(request, 'owner/trip.html', {"data": ob})





def view_collection(request):
    ob=collection_table.objects.all()
    return render(request,'owner/view collction details.html',{'val':ob})

def view_notification(request):
    ob=notification_table.objects.all()
    return render(request,'owner/view notification.html',{'data':ob})

def notification_delete(request,id):
    a=notification_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert("deleted successfully");window.location='/admin_view_notification'</script>''')

def delete_stopmanagment(request,id):
    a=stop_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert("deleted successfully");window.location='/stopmangmnt'</script>''')

def edit_notification(request,id):
    b=notification_table.objects.get(id=id)
    return render(request,'admin/edit notification.html',{'data':b})


def edit_notification_post(request):
    id = request.POST['data']
    notification = request.POST['textfield2']
    details = request.POST['textfield']

    noti = notification_table.objects.get(id=id)
    noti.notification = notification
    noti.details = details
    noti.date = datetime.datetime.now().date()
    noti.save()
    return HttpResponse(
        '''<script>alert('notification updated successfully ');window.location='/admin_view_notification'</script>''')


def viewtime(request,id):
    request.session['bid']=id
    ob=timing_table.objects.filter(trip__id=request.session['bid'])
    return render(request,'owner/view time.html',{'val':ob})

def add_viewtime(request):
        stop=request.POST['select']
        timee=request.POST['textfield']

        ss = timing_table()
        ss.stop = stop_table.objects.get(id=stop)
        ss.time = timee
        ss.trip = trip_table.objects.get(id=request.session['bid'])
        ss.save()
        return HttpResponse('''<script>alert('time added successfully ');window.location='/viewtime/'''+str(request.session['bid'])+''''</script>''')

def delete_viewtime(request,id):
    ob=timing_table .objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("trip deleted");window.location='/viewtime/'''+str(request.session['bid'])+''''</script>''')

def edit_viewtime(request,id):
    ob=timing_table.objects.get(id=id)
    request.session["bbid"]=id
    kk=stop_table.objects.all()
    return render(request,'owner/edit_time.html' , {'i':ob,"val":kk})


def edit_viewtime_post(request):
    stop = request.POST['select']
    timee = request.POST['textfield']

    editbuss=timing_table.objects.get(id=request.session["bbid"])
    editbuss.stop=stop_table.objects.get(id=stop)
    editbuss.time=timee
    editbuss.save()
    return HttpResponse(
        '''<script>alert('bus time edited  successfully ');window.location='/trip'</script>''')






def edit_stopadd(request,id):
    request.session['aid']=id
    ob=stop_table.objects.get(id=id)
    obr=route_table.objects.all()
    return render(request, 'admin/stop_add.html', {"rout": obr,"i":ob})

def edit_stopadd_post(request):
    route = request.POST['select']
    stopname = request.POST['textfield2']
    fair = request.POST['textfield3']
    stage = request.POST['textfield4']
    latitude = request.POST['textfield42']
    longitude= request.POST['textfield43']

    addstop = stop_table.objects.get(id=request.session['aid'])
    addstop.route_id=route
    addstop.stopname=stopname
    addstop.fair=fair
    addstop.stage=stage
    addstop.latitude=latitude
    addstop.longitude=longitude
    addstop.save()
    return HttpResponse ('''<script>alert('Bus route edited  successfully ');window.location='/stopmangmnt'</script>''')

def edit_busowner(request,id):
    request.session['aid']=id
    ob = busowner_table.objects.get(id=id)
    return render(request, 'admin/edit_Busownerr.html', {'val': ob})

def edit_busowner_post(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    phone=request.POST['textfield5']
    email=request.POST['textfield6']

    addowner=busowner_table.objects.get(id=request.session['aid'])
    addowner.name=name
    addowner.place=place
    addowner.post=post
    addowner.pin=pin
    addowner.phone=phone
    addowner.email=email
    addowner.save()
    return HttpResponse ('''<script>alert('bus owner edited  successfully ');window.location='/view_bussowner'</script>''')


def edit_bus_route(request,id):
    request.session["bid"]=id
    ob=route_table.objects.get(id=id)
    return render(request,'admin/add_route.html',{'val':ob})

def edit_busroute_post(request):
    from_rout=request.POST['from']
    to_rout=request.POST['to']

    editbuss=route_table.objects.get(id=request.session["bid"])
    editbuss.from_rout=from_rout
    editbuss.to_rout=to_rout
    editbuss.save()
    return HttpResponse('''<script>alert('bus route edited  successfully ');window.location='/manage_bus_route';</script>''')


def edit_manageemploye(request,id):
    request.session["aid"]=id
    ob=employee_table.objects.get(id=id)
    return render(request,'owner/edit_employe.html' , {'i':ob})

def edit_manageemployee_post(request):
    name=request.POST['textfield']
    dob=request.POST['textfield2']
    Phone=request.POST['textfield3']
    Email=request.POST['textfield4']
    Place=request.POST['textfield5']
    Post=request.POST['textfield6']
    pin=request.POST['textfield7']

    mange_emp = employee_table.objects.get(id=request.session["aid"])
    mange_emp.name=name
    mange_emp.dob=dob
    mange_emp.phoneno=Phone
    mange_emp.email=Email
    mange_emp.place=Place
    mange_emp.post=Post
    mange_emp.pin=pin
    mange_emp.save()
    return HttpResponse('''<script>alert('employe edited  successfully ');window.location='/manageemploye';</script>''')

def delete_employee(request,id):
    ob=employee_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/manageemploye"</script>''')

def delete_bus(request,id):
    ob=bus_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/managebus"</script>''')

def edit_bus(request,id):
    ob=bus_table.objects.get(id=id)
    request.session["bid"]=id
    return render(request,'owner/edit  bus.html' , {'i':ob})

def edit_bus_post(request):
    busname=request.POST['textfield']
    reg=request.POST['textfield2']
    photo=request.POST['file']
    fitness=request.POST['textfield3']
    insurance=request.POST['textfield4']
    rcbook=request.POST['file2']

    mange_bus = bus_table.objects.get(id=request.session["bid"])
    mange_bus.name=busname
    mange_bus.regno=reg
    mange_bus.photo=photo
    mange_bus.fitness=fitness
    mange_bus.insurance=insurance
    mange_bus.rcbook=rcbook

    mange_bus.save()
    return HttpResponse('''<script>alert('bus edited  successfully ');window.location='/managebus';</script>''')

def add_bus_to_route_post(request):
    print(request.POST,'jjjjjjjjjjj')
    route = request.POST['select']
    bus = request.POST['select1']
    trip = request.POST['textfield']

    add_rout = trip_table()
    add_rout.route=route_table.objects.get(id=route)
    add_rout.bus=bus_table.objects.get(id=bus)
    add_rout.tripname=trip
    add_rout.status='pending'
    add_rout.save()
    return HttpResponse('''<script>alert('trip added successfully ');window.location='/trip';</script>''')


def delete_trip(request,id):
    ob=trip_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("trip deleted");window.location="/trip"</script>''')


#----------------------------------------------------------------------------------------------------------------------



def logincode(request):
    print(request.POST)
    un = request.POST['username']
    pwd = request.POST['password']
    print(un, pwd,"hello")
    try:
        ob = login_table.objects.get(username=un, password=pwd)

        if ob is None:
            data = {"task": "invalid"}
        else:
            print("in user function")
            data = {"task": "valid", "lid": ob.id,"type":ob.type}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)



# def user_view_profile(request):
#     lid=request.POST["lid"]
#     i=employee_table.objects.get(login__id=lid)
#     print(i,"HHHHHHHHHHHHHHH")
#
#     return JsonResponse({"status":"ok",'name':i.name,'dob':i.dob,'phone':i.phoneno,
#             'email':i.email,
#             'place':i.place,
#             'post':i.post,
#             'pin':i.pin,
#             'img':i.image,
#             'lisence':i.license,
#             'id':i.id})

def user_view_profile(request):
    lid = request.POST.get("lid")  # Use .get() for better handling of missing keys
    if not lid:
        return JsonResponse({"status": "error", "message": "lid parameter is missing."})

    try:
        i = employee_table.objects.get(login__id=lid)
        return JsonResponse({
            "status": "ok",
            "name": i.name,
            "dob": str(i.dob),  # Ensure the date is properly formatted as a string
            "phone": str(i.phoneno),
            "email": i.email,
            "place": i.place,
            "post": i.post,
            "pin": str(i.pin),
            "img": str(i.image.url)[1:],  # Ensure the image URL is correct
            "license": i.license,
            "id": i.id
        })

    except employee_table.DoesNotExist:
        return JsonResponse({"status": "error", "message": f"Employee with login ID {lid} not found."})

def view_assinged_bus_flutter(request):
        lid=request.POST["lid"]
        p=employee_table.objects.get(login_id=lid)
        ob=assign_table.objects.filter(employe_id=p.id)
        list=[]
        for i in ob:
            list.append({'id':i.bus.id,'bus':i.bus.name,'date':i.date})
        return JsonResponse({'status':'ok','data':list})

def view_bus_route_flutter(request):
    bus_id=request.POST['bid']
    print(request.POST)
    ob=trip_table.objects.filter(bus_id=bus_id)

    list=[]
    for i in ob:

        list.append({'id': i.bus.id,
                     'bus':i.bus.name,
                     'route_from': i.route.from_rout,
                     'route_to':i.route.to_rout})
        print(list)
    return JsonResponse({'status': 'ok', 'data': list})

def view_bus_shudule(request):
    print(request.POST, ";;;;;;;;;;;;;;;;;")
    trip_id=request.POST["bid"]

    ob=timing_table.objects.filter(trip=trip_id)
    list = []
    for i in ob:
        list.append({'trip': i.trip.tripname,
                     'stop': i.stop.stopname,
                     'time': i.time,})
    return JsonResponse({'status': 'ok', 'data': list})

def collection_details_flutter(request):
    lid=request.POST['lid']
    ob=collection_table.objects.get(login_id=lid)
    list=[]
    for i in ob:
        list.append({'id': i.id,'trip':i.trip, 'date': i.trip,'amount':i.amount})
    return JsonResponse({'status': 'ok', 'data': list})



def viewpayment(request):
    ob=booking_table.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    list=[]
    for i in ob:
        list.append({'user':i.user.name,
              'trip':i.trip.tripname,
              'date':i.date,
              'from_booking':i.from_booking,
              'to_booking':i.to_booking,
              'id':i.id,
              'status':i.status})

    return JsonResponse({"status":"ok","data":list})


def viewpaymentuser(request):
    ob=booking_table.objects.all()
    list = []
    for i in ob:
        list.append({'user': i.user.name,
                     'id':i.id,
                     'date': i.date,
                     'from_booking': i.from_booking,
                     'to_booking': i.to_booking,
                     'amount':i.amount,
                     'id': i.id,
                     'status': i.status})

    return JsonResponse({"status": "ok", "data": list})


def viewtrip(request):
    ob=trip_table.objects.all()
    list = []
    for i in ob: list.append({
        'id':i.id,
        'tripname': i.tripname,


    })
    return JsonResponse({"status": "ok", "data": list})



def updateamount(request):
    bid=request.POST['bid']
    amnt=request.POST['amount']
    ob=booking_table.objects.get(id=bid)
    ob.amount=amnt
    ob.save()

    return JsonResponse({"status":"ok"}, status=200)


def acc_bk(request):
    bid=request.POST['bid']
    ob=booking_table.objects.get(id=bid)
    ob.status="booked"
    ob.save()

    return JsonResponse({"status":"ok"}, status=200)


def rj_bk(request):
    bid=request.POST['bid']
    ob=booking_table.objects.get(id=bid)
    ob.status="rejected"
    ob.save()

    return JsonResponse({"status":"ok"}, status=200)



def book(request):
    lid=request.POST['lid']
    sid=request.POST['sid']
    user = booking_table.get(LOGIN_id=lid)
    print(user,"hello")

    schedule = booking_table.objects.get(id=sid)
    existing_booking = booking_table.objects.filter(SCHEDULE_id=schedule,USER_id=user).exists()

    if existing_booking:
        return JsonResponse({"status": "error", "message": "You have already booked this schedule"}, status=400)

    count1 = booking_table.objects.filter(SCHEDULE_id=sid, status="booked").count()
    total_count = 1
    avail = count1 >= total_count

    if avail :
        return JsonResponse({"status": "error", "message": "booking full"}, status=410)
































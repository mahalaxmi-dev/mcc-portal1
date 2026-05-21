# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import check_password
# from .models import Officer, LoginLog
# from complaints.models import Complaint


# def officer_login(request):

#     if request.method == "POST":

#         username = request.POST['username']
#         password = request.POST['password']

#         try:
#             officer = Officer.objects.get(username=username)

#             # CHECK HASHED PASSWORD
#             if check_password(password, officer.password):

#                 # SAVE LOGIN LOG
#                 LoginLog.objects.create(
#                     officer_name=officer.name,
#                     department=officer.department
#                 )

#                 # STORE SESSION
#                 request.session['officer_id'] = officer.id
#                 request.session['officer_name'] = officer.name
#                 request.session['department'] = officer.department

#                 return redirect('officer_dashboard')

#             else:
#                 return render(request, 'officer_login.html', {
#                     'error': 'Invalid username or password'
#                 })

#         except Officer.DoesNotExist:

#             return render(request, 'officer_login.html', {
#                 'error': 'Invalid username or password'
#             })

#     return render(request, 'officer_login.html')


# def officer_dashboard(request):

#     if 'officer_id' not in request.session:
#         return redirect('officer_login')

#     department = request.session['department']

#     complaints = Complaint.objects.filter(
#         department=department
#     ).order_by('-date_submitted')

#     return render(request, 'officer_dashboard.html', {
#         'complaints': complaints,
#         'officer_name': request.session['officer_name']
#     })
# def officer_complaint_detail(request, complaint_id):

#     if 'officer_id' not in request.session:
#         return redirect('officer_login')

#     complaint = Complaint.objects.get(complaint_id=complaint_id)

#     if request.method == "POST":
#         complaint.status = request.POST.get('status', complaint.status)
#         complaint.officer_remark = request.POST.get('remark', '')
#         complaint.save()
#         return redirect('officer_complaint_detail', complaint_id=complaint_id)

#     return render(request, 'officer_complaint_detail.html', {
#         'complaint': complaint
#     })

# def officer_complaint_detail(request, complaint_id):

#     if 'officer_id' not in request.session:
#         return redirect('officer_login')

#     complaint = Complaint.objects.get(complaint_id=complaint_id)


#     return render(request, 'officer_complaint_detail.html', {
#         'complaint': complaint
#     })


# def officer_logout(request):

#     request.session.flush()

#     return redirect('officer_login')


from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Officer, LoginLog
from complaints.models import Complaint

def officer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            officer = Officer.objects.get(username=username)
            if check_password(password, officer.password):
                LoginLog.objects.create(
                    officer_name=officer.name,
                    department=officer.department
                )
                request.session['officer_id'] = officer.id
                request.session['officer_name'] = officer.name
                request.session['department'] = officer.department
                return redirect('officer_dashboard')
            else:
                return render(request, 'officer_login.html', {
                    'error': 'Invalid username or password'
                })
        except Officer.DoesNotExist:
            return render(request, 'officer_login.html', {
                'error': 'Invalid username or password'
            })
    return render(request, 'officer_login.html')

def officer_dashboard(request):
    if 'officer_id' not in request.session:
        return redirect('officer_login')
    department = request.session['department']
    complaints = Complaint.objects.filter(
        department=department
    ).order_by('-date_submitted')
    return render(request, 'officer_dashboard.html', {
        'complaints': complaints,
        'officer_name': request.session['officer_name']
    })

def officer_complaint_detail(request, complaint_id):
    if 'officer_id' not in request.session:
        return redirect('officer_login')
    complaint = Complaint.objects.get(complaint_id=complaint_id)
    if request.method == "POST":
        complaint.status = request.POST.get('status', complaint.status)
        complaint.officer_remark = request.POST.get('remark', '')
        complaint.save()
        return redirect('officer_complaint_detail', complaint_id=complaint_id)
    return render(request, 'officer_complaint_detail.html', {
        'complaint': complaint
    })

def officer_logout(request):
    request.session.flush()
    return redirect('officer_login')
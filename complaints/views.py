# from django.shortcuts import render, redirect
# from .models import Complaint
# from users.models import Citizen

# def terms(request):
#     if 'citizen_id' not in request.session:
#         return redirect('login')
#     if request.method == "POST":
#         return redirect('file_complaint')
#     return render(request, 'terms.html')

# def file_complaint(request):

#     if 'citizen_id' not in request.session:
#         return redirect('login')

#     error = None

#     if request.method == "POST":

#         citizen = Citizen.objects.get(id=request.session['citizen_id'])

#         uploaded_file = request.FILES.get('attachment')

#         # FILE VALIDATION
#         if uploaded_file:

#             allowed_types = ['image/jpeg', 'image/png']

#             if uploaded_file.content_type not in allowed_types:
#                 error = "Only JPG and PNG images are allowed."

#             elif uploaded_file.size > 3 * 1024 * 1024:
#                 error = "Image size must be below 3 MB."

#         else:
#             error = "Please upload an image."

#         if error:
#             return render(request, 'file_complaint.html', {
#                 'error': error
#             })

#         complaint = Complaint(
#             citizen=citizen,
#             department=request.POST['department'],
#             title=request.POST['title'],
#             address=request.POST['address'],
#             description=request.POST['description'],
#             map_location=request.POST.get('map_location', ''),
#             attachment=uploaded_file,
#         )

#         complaint.save()

#         return redirect(
#             'complaint_success',
#             complaint_id=complaint.complaint_id
#         )

#     return render(request, 'file_complaint.html')

# def complaint_success(request, complaint_id):
#     return render(request, 'complaint_success.html', {'complaint_id': complaint_id})

# def dashboard(request):
#     if 'citizen_id' not in request.session:
#         return redirect('login')
#     citizen = Citizen.objects.get(id=request.session['citizen_id'])
#     complaints = Complaint.objects.filter(citizen=citizen).order_by('status', '-date_submitted')
#     return render(request, 'dashboard.html', {
#         'citizen': citizen,
#         'complaints': complaints
#     })

# def complaint_detail(request, complaint_id):
#     if 'citizen_id' not in request.session:
#         return redirect('login')
#     complaint = Complaint.objects.get(complaint_id=complaint_id)
#     return render(request, 'complaint_detail.html', {'complaint': complaint})

# def track_complaint(request):
#     complaint = None
#     error = None
#     if request.method == "POST":
#         complaint_id = request.POST['complaint_id']
#         try:
#             complaint = Complaint.objects.get(complaint_id=complaint_id)
#         except Complaint.DoesNotExist:
#             error = "No complaint found with this ID."
#     return render(request, 'track_complaint.html', {
#         'complaint': complaint,
#         'error': error
#     })


from django.shortcuts import render, redirect
from .models import Complaint
from users.models import Citizen

def terms(request):
    if 'citizen_id' not in request.session:
        return redirect('login')
    if request.method == "POST":
        return redirect('file_complaint')
    return render(request, 'terms.html')

def file_complaint(request):
    if 'citizen_id' not in request.session:
        return redirect('login')

    error = None

    if request.method == "POST":
        citizen = Citizen.objects.get(id=request.session['citizen_id'])
        uploaded_file = request.FILES.get('attachment')

        if uploaded_file:
            allowed_types = ['image/jpeg', 'image/png']
            if uploaded_file.content_type not in allowed_types:
                error = "Only JPG and PNG images are allowed."
            elif uploaded_file.size > 3 * 1024 * 1024:
                error = "Image size must be below 3 MB."
        else:
            error = "Please upload an image."

        if error:
            return render(request, 'file_complaint.html', {'error': error})

        complaint = Complaint(
            citizen=citizen,
            department=request.POST['department'],
            title=request.POST['title'],
            address=request.POST['address'],
            description=request.POST['description'],
            map_location=request.POST.get('map_location', ''),
            attachment=uploaded_file,
        )
        complaint.save()

        return redirect('complaint_success', complaint_id=complaint.complaint_id)

    return render(request, 'file_complaint.html')

def complaint_success(request, complaint_id):
    return render(request, 'complaint_success.html', {'complaint_id': complaint_id})

def dashboard(request):
    if 'citizen_id' not in request.session:
        return redirect('login')
    citizen = Citizen.objects.get(id=request.session['citizen_id'])
    complaints = Complaint.objects.filter(citizen=citizen).order_by('status', '-date_submitted')
    return render(request, 'dashboard.html', {
        'citizen': citizen,
        'complaints': complaints
    })

def complaint_detail(request, complaint_id):
    if 'citizen_id' not in request.session:
        return redirect('login')
    complaint = Complaint.objects.get(complaint_id=complaint_id)
    return render(request, 'complaint_detail.html', {'complaint': complaint})

def track_complaint(request):
    complaint = None
    error = None
    if request.method == "POST":
        complaint_id = request.POST.get('complaint_id', '').strip()
        if not complaint_id:
            error = "Please enter a Complaint ID."
        else:
            try:
                complaint = Complaint.objects.get(complaint_id=complaint_id)
            except Complaint.DoesNotExist:
                error = "No complaint found with this ID. Please check and try again."
    return render(request, 'track_complaint.html', {
        'complaint': complaint,
        'error': error
    })
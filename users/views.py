# # # import re
# # # from django.shortcuts import render, redirect
# # # from django.contrib.auth.hashers import make_password, check_password
# # # from .models import Citizen
# # # from officers.models import Officer

# # # def home(request):
# # #     return render(request, 'home.html')

# # # def register(request):
# # #     if request.method == "POST":
# # #         name = request.POST['name']
# # #         email = request.POST['email']
# # #         phone = "+91" + request.POST['phone']
# # #         username = request.POST['username']
# # #         password = request.POST['password']

# # #         # ---------------- USERNAME VALIDATION ----------------
# # #         # 3-20 characters
# # #         if len(username) < 3 or len(username) > 20:
# # #             return render(request, 'register.html', {
# # #                 'error': "Username must be between 3 and 20 characters."
# # #             })

# # #         # Only letters, numbers and underscore
# # #         if not re.match(r'^[A-Za-z0-9_]+$', username):
# # #             return render(request, 'register.html', {
# # #                 'error': "Username can contain only letters, numbers and underscore (_)."
# # #             })

# # #         # ---------------- PASSWORD VALIDATION ----------------
# # #         # Minimum 8 characters
# # #         if len(password) < 8:
# # #             return render(request, 'register.html', {
# # #                 'error': "Password must be at least 8 characters."
# # #             })

# # #         # ---------------- EXISTING CHECKS ----------------
# # #         email_exists = Citizen.objects.filter(email=email).exists()
# # #         phone_exists = Citizen.objects.filter(phone=phone).exists()
# # #         username_exists = Citizen.objects.filter(username=username).exists()

# # #         if email_exists and phone_exists:
# # #             return render(request, 'register.html', {
# # #                 'error': "Phone number and Email ID already registered."
# # #             })

# # #         elif email_exists:
# # #             return render(request, 'register.html', {
# # #                 'error': "Email ID already registered."
# # #             })

# # #         elif phone_exists:
# # #             return render(request, 'register.html', {
# # #                 'error': "Phone number already registered."
# # #             })

# # #         elif username_exists:
# # #             return render(request, 'register.html', {
# # #                 'error': "Username already taken. Please choose another."
# # #             })

# # #         # ---------------- SAVE USER ----------------
# # #         citizen = Citizen(
# # #             name=name,
# # #             email=email,
# # #             phone=phone,
# # #             username=username,
# # #             password=make_password(password)
# # #         )

# # #         citizen.save()

# # #         return redirect(reverse('login') + '?registered=true')

# # #     return render(request, 'register.html')

# # # def register_success(request):
# # #     return render(request, 'success.html')

# # # def login(request):
# # #     if request.method == "POST":
# # #         username = request.POST['username']
# # #         password = request.POST['password']

# # #         try:
# # #             citizen = Citizen.objects.get(username=username)
# # #         except Citizen.DoesNotExist:
# # #             return render(request, 'login.html', {'error': "Invalid username or password."})

# # #         if check_password(password, citizen.password):
# # #             request.session['citizen_id'] = citizen.id
# # #             request.session['citizen_name'] = citizen.name
# # #             return redirect('dashboard')
# # #         else:
# # #             return render(request, 'login.html', {'error': "Invalid username or password."})

# # #     success = request.GET.get('registered') == 'true'
# # #     return render(request, 'login.html', {'success': success})

# # # def logout_view(request):
# # #     request.session.flush()
# # #     return redirect('home')

# # # def forgot_username(request):
# # #     if request.method == "POST":
# # #         email = request.POST['email']
# # #         try:
# # #             citizen = Citizen.objects.get(email=email)
# # #             return render(request, 'forgot_username.html', {'found_username': citizen.username})
# # #         except Citizen.DoesNotExist:
# # #             return render(request, 'forgot_username.html', {'error': "No account found with this email."})

# # #     return render(request, 'forgot_username.html')

# # # def forgot_password(request):
# # #     if request.method == "POST":
# # #         username = request.POST['username']
# # #         email = request.POST['email']
# # #         new_password = request.POST['new_password']
# # #         confirm_password = request.POST['confirm_password']

# # #         if new_password != confirm_password:
# # #             return render(request, 'forgot_password.html', {'error': "Passwords do not match."})

# # #         try:
# # #             citizen = Citizen.objects.get(username=username, email=email)
# # #             citizen.password = make_password(new_password)
# # #             citizen.save()
# # #             return render(request, 'forgot_password.html', {'success': True})
# # #         except Citizen.DoesNotExist:
# # #             return render(request, 'forgot_password.html', {'error': "Username and email do not match."})

# # #     return render(request, 'forgot_password.html')

# # # def about(request):
# # #     return render(request, 'about.html')

# # # def faqs(request):
# # #     return render(request, 'faqs.html')

# # # def officers_directory(request):
# # #     officers = Officer.objects.all().order_by('department')
# # #     return render(request, 'officers_directory.html', {'officers': officers})
# # #     return render(request, 'officers_directory.html', {'officers': officers})

# # from django.shortcuts import render, redirect
# # from django.urls import reverse                          # ✅ fixes NameError
# # from django.contrib.auth.hashers import make_password, check_password
# # from .models import Citizen


# # def register(request):
# #     if request.method == "POST":
# #         name     = request.POST.get('name', '').strip()
# #         email    = request.POST.get('email', '').strip()
# #         phone    = request.POST.get('phone', '').strip()
# #         username = request.POST.get('username', '').strip()
# #         password = request.POST.get('password', '')

# #         # ── Validation ──────────────────────────────────────────
# #         if not name:
# #             return render(request, 'register.html', {'error': 'Full name is required.'})

# #         if not email:
# #             return render(request, 'register.html', {'error': 'Email address is required.'})

# #         if not phone or not phone.isdigit() or len(phone) != 10 or phone[0] not in '6789':
# #             return render(request, 'register.html', {'error': 'Enter a valid 10-digit Indian mobile number starting with 6, 7, 8 or 9.'})

# #         if len(username) < 3 or len(username) > 20:
# #             return render(request, 'register.html', {'error': 'Username must be between 3 and 20 characters.'})

# #         # ✅ FIXED: minimum 8 characters (was wrongly checking for exactly 10)
# #         if len(password) < 8:
# #             return render(request, 'register.html', {'error': 'Password must be at least 8 characters long.'})

# #         if Citizen.objects.filter(username=username).exists():
# #             return render(request, 'register.html', {'error': 'That username is already taken. Please choose another.'})

# #         if Citizen.objects.filter(email=email).exists():
# #             return render(request, 'register.html', {'error': 'An account with this email already exists.'})

# #         # ── Create user ─────────────────────────────────────────
# #         Citizen.objects.create(
# #             name=name,
# #             email=email,
# #             phone=phone,
# #             username=username,
# #             password=make_password(password),
# #         )

# #         # ✅ Show success banner on the same page
# #         return render(request, 'register.html', {'success': True})

# #     return render(request, 'register.html')


# # def login_view(request):
# #     if request.method == "POST":
# #         username = request.POST.get('username', '').strip()
# #         password = request.POST.get('password', '')

# #         try:
# #             citizen = Citizen.objects.get(username=username)
# #         except Citizen.DoesNotExist:
# #             return render(request, 'login.html', {'error': 'Invalid username or password.'})

# #         if not check_password(password, citizen.password):
# #             return render(request, 'login.html', {'error': 'Invalid username or password.'})

# #         request.session['citizen_id'] = citizen.id
# #         request.session['citizen_name'] = citizen.name
# #         return redirect('dashboard')

# #     return render(request, 'login.html')


# # def logout_view(request):
# #     request.session.flush()
# #     return redirect('login')

# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password, check_password
# from .models import Citizen


# # ─────────────────────────────────────────
# #  PUBLIC PAGES  (no login required)
# # ─────────────────────────────────────────

# def home(request):
#     return render(request, 'home.html')


# def about(request):
#     return render(request, 'about.html')


# def faqs(request):
#     return render(request, 'faqs.html')


# def officers_directory(request):
#     return render(request, 'officers_directory.html')


# # ─────────────────────────────────────────
# #  AUTH  — register / login / logout
# # ─────────────────────────────────────────

# def register(request):
#     if request.method == "POST":
#         name     = request.POST.get('name', '').strip()
#         email    = request.POST.get('email', '').strip()
#         phone    = request.POST.get('phone', '').strip()
#         username = request.POST.get('username', '').strip()
#         password = request.POST.get('password', '')

#         # ── Validation ──────────────────────────────────────
#         if not name:
#             return render(request, 'register.html', {'error': 'Full name is required.'})

#         if not email:
#             return render(request, 'register.html', {'error': 'Email address is required.'})

#         if not phone or not phone.isdigit() or len(phone) != 10 or phone[0] not in '6789':
#             return render(request, 'register.html', {
#                 'error': 'Enter a valid 10-digit Indian mobile number starting with 6, 7, 8 or 9.'
#             })

#         if len(username) < 3 or len(username) > 20:
#             return render(request, 'register.html', {
#                 'error': 'Username must be between 3 and 20 characters.'
#             })

#         # FIXED: minimum 8 chars (was wrongly checking exactly 10)
#         if len(password) < 8:
#             return render(request, 'register.html', {
#                 'error': 'Password must be at least 8 characters long.'
#             })

#         if Citizen.objects.filter(username=username).exists():
#             return render(request, 'register.html', {
#                 'error': 'That username is already taken. Please choose another.'
#             })

#         if Citizen.objects.filter(email=email).exists():
#             return render(request, 'register.html', {
#                 'error': 'An account with this email already exists.'
#             })

#         # ── Create citizen ───────────────────────────────────
#         Citizen.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             username=username,
#             password=make_password(password),
#         )

#         # Show success banner — no redirect, no reverse needed
#         return render(request, 'register.html', {'success': True})

#     return render(request, 'register.html')


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username', '').strip()
#         password = request.POST.get('password', '')

#         try:
#             citizen = Citizen.objects.get(username=username)
#         except Citizen.DoesNotExist:
#             return render(request, 'login.html', {'error': 'Invalid username or password.'})

#         if not check_password(password, citizen.password):
#             return render(request, 'login.html', {'error': 'Invalid username or password.'})

#         request.session['citizen_id']   = citizen.id
#         request.session['citizen_name'] = citizen.name
#         return redirect('dashboard')

#     return render(request, 'login.html')


# def logout_view(request):
#     request.session.flush()
#     return redirect('login')



import re
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Citizen
from officers.models import Officer


# ─────────────────────────────────────────
#  PUBLIC PAGES
# ─────────────────────────────────────────

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def faqs(request):
    return render(request, 'faqs.html')


def officers_directory(request):
    officers = Officer.objects.all().order_by('department')
    return render(request, 'officers_directory.html', {'officers': officers})


# ─────────────────────────────────────────
#  REGISTER
# ─────────────────────────────────────────

def register(request):
    if request.method == "POST":
        name     = request.POST.get('name', '').strip()
        email    = request.POST.get('email', '').strip()
        phone    = request.POST.get('phone', '').strip()
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Validation
        if not name:
            return render(request, 'register.html', {'error': 'Full name is required.'})

        if not email:
            return render(request, 'register.html', {'error': 'Email address is required.'})

        if not phone or not phone.isdigit() or len(phone) != 10 or phone[0] not in '6789':
            return render(request, 'register.html', {
                'error': 'Enter a valid 10-digit mobile number starting with 6, 7, 8 or 9.'
            })

        if len(username) < 3 or len(username) > 20:
            return render(request, 'register.html', {
                'error': 'Username must be between 3 and 20 characters.'
            })

        if not re.match(r'^[A-Za-z0-9_]+$', username):
            return render(request, 'register.html', {
                'error': 'Username can only contain letters, numbers and underscore (_).'
            })

        # FIXED: minimum 8 characters
        if len(password) < 8:
            return render(request, 'register.html', {
                'error': 'Password must be at least 8 characters long.'
            })

        phone_full = "+91" + phone

        if Citizen.objects.filter(email=email).exists() and Citizen.objects.filter(phone=phone_full).exists():
            return render(request, 'register.html', {'error': 'Phone number and Email ID already registered.'})
        elif Citizen.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email ID already registered.'})
        elif Citizen.objects.filter(phone=phone_full).exists():
            return render(request, 'register.html', {'error': 'Phone number already registered.'})
        elif Citizen.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken. Please choose another.'})

        # Save citizen
        Citizen.objects.create(
            name=name,
            email=email,
            phone=phone_full,
            username=username,
            password=make_password(password),
        )

        # Show success banner on the same page (no reverse/redirect needed)
        return render(request, 'register.html', {'success': True})

    return render(request, 'register.html')


def register_success(request):
    """Kept for url routing — redirects to register with success shown."""
    return render(request, 'success.html')


# ─────────────────────────────────────────
#  LOGIN / LOGOUT
# ─────────────────────────────────────────

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        try:
            citizen = Citizen.objects.get(username=username)
        except Citizen.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

        if not check_password(password, citizen.password):
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

        request.session['citizen_id']   = citizen.id
        request.session['citizen_name'] = citizen.name
        return redirect('dashboard')

    # Support ?registered=true query param (legacy)
    success = request.GET.get('registered') == 'true'
    return render(request, 'login.html', {'success': success})


def logout_view(request):
    request.session.flush()
    return redirect('home')


# ─────────────────────────────────────────
#  FORGOT USERNAME / PASSWORD
# ─────────────────────────────────────────

def forgot_username(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        try:
            citizen = Citizen.objects.get(email=email)
            return render(request, 'forgot_username.html', {'found_username': citizen.username})
        except Citizen.DoesNotExist:
            return render(request, 'forgot_username.html', {'error': 'No account found with this email.'})

    return render(request, 'forgot_username.html')


def forgot_password(request):
    if request.method == "POST":
        username         = request.POST.get('username', '').strip()
        email            = request.POST.get('email', '').strip()
        new_password     = request.POST.get('new_password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if new_password != confirm_password:
            return render(request, 'forgot_password.html', {'error': 'Passwords do not match.'})

        if len(new_password) < 8:
            return render(request, 'forgot_password.html', {'error': 'Password must be at least 8 characters long.'})

        try:
            citizen = Citizen.objects.get(username=username, email=email)
            citizen.password = make_password(new_password)
            citizen.save()
            return render(request, 'forgot_password.html', {'success': True})
        except Citizen.DoesNotExist:
            return render(request, 'forgot_password.html', {'error': 'Username and email do not match.'})

    return render(request, 'forgot_password.html')
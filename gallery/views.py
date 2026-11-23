from django.shortcuts import render, redirect, get_object_or_404
from .models import ArtPiece, Appointment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# 1. Тот самый новый приветственный экран выбора роли
def welcome(request):
    return render(request, 'welcome.html')


# 2. Страница каталога и записи для клиента (переехала по адресу /catalog/)
def index(request):
    search_result = None
    phone_searched = None

    if request.method == 'POST':
        if 'check_phone' in request.POST:
            phone_searched = request.POST.get('check_phone')
            search_result = Appointment.objects.filter(phone=phone_searched).order_by('-created_at').first()

        else:
            hour = request.POST.get('time_hour', '15')
            minute = request.POST.get('time_minute', '00')
            full_time = f"{hour}:{minute}"

            Appointment.objects.create(
                client_name=request.POST.get('client_name'),
                phone=request.POST.get('phone'),
                date=request.POST.get('date'),
                time=full_time,
                custom_image=request.FILES.get('custom_image'),
                custom_style=request.POST.get('custom_style'),
                custom_size=request.POST.get('custom_size'),
                comment=request.POST.get('comment', '')
            )
            return redirect('index')

    artworks = ArtPiece.objects.filter(is_approved=True)
    return render(request, 'index.html', {
        'artworks': artworks,
        'search_result': search_result,
        'phone_searched': phone_searched
    })


# 3. НАША ЗАЩИТА: Магическая строчка @login_required требует пароль для входа в CRM!
@login_required(login_url='/django-admin/login/')
def admin_dashboard(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        action = request.POST.get('action')
        appointment = get_object_or_404(Appointment, id=appointment_id)

        if action == 'approve':
            appointment.status = 'Одобрено'
        elif action == 'reject':
            appointment.status = 'Отменено'

        appointment.save()
        return redirect('admin_dashboard')

    users = User.objects.all()
    appointments = Appointment.objects.all().order_by('-created_at')

    return render(request, 'admin_dashboard.html', {
        'users': users,
        'appointments': appointments
    })

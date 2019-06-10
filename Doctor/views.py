from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import Schedule, History
# Create your views here.

def index(request):
    return render(request, 'index.html')

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "doctor/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register_def.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/doctor/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def get_users(request):
    users = User.objects.all()

    return render(request,'users.html', {'users': users})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctor/register/login')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'register.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'page-blog.html')

def timetable(request):
    schedule = Schedule.objects.all()
    return render(request, 'page-time-table.html', context={'schedule' : schedule})

def our_doctors(request):
    return render(request, 'page-our-doctors.html')

def department(request):

    return render(request, 'page-department-detail.html')

def history(request):
    history = History.objects.all()
    args = {'user': request.user}
    return render(request, 'history.html', context={'history': history, 'args' : args})
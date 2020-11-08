from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import *
from django.contrib.auth import get_user_model
from .forms import *
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
class ONViewMixin(object):
    title = None
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def get_initials(self):
        return {
            'instance': self.request.user.instance
        }

    def get_success_url(self):
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url


def login_user(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Core:index')
        else:
            error = 'برجاء إدخال اسم المستخدم وكلمة السر'
            context.update({'error': error})
            return render(request, 'Auth/login.html', context)
    return render(request, 'Auth/login.html', context)


class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # self.mail_notify(request)
                return redirect('Core:index')
            else:
                error = 'تم إيقاف الحساب الخاص بك'
                return render(request, 'Auth/login.html', context={'error': error})
        else:
            error = 'برجاء التأكد من اسم المستخدم وكلمة السر'
            return render(request, 'Auth/login.html', context={'error': error})

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('Core:index')
        return render(request, 'Auth/login.html')

    def mail_notify(self, request):
        send_mail(
            'Subject here',
            'Here is the message.',
            'noreply@daftre.com',
            ['ahmed.elkhayyat@onlink4it.com'],
            fail_silently=False,
        )


class Logout(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('Core:login')


def permissions(request, pk):
    user = User.objects.get(id=pk)
    form = PermissionsForm(request.POST or None, instance=user)
    title = 'تعديل صلاحيات الموظف ' + user.__str__()
    action_url = reverse_lazy('Core:permissions', kwargs={'pk': user.id})
    if form.is_valid():
        obj = form.save()
        return redirect('Core:index')
    context = {
        'form': form,
        'title': title,
        'action_url': action_url,
    }
    return render(request, 'Core/form_template.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'تم تغيير كلمة المرور بنجاح!')
            return redirect('Core:index')
        else:
            messages.error(request, 'برجاء إصلاح الأخطاء الاتية')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Core/form_template.html', {
        'form': form,
        'title': 'تغيير كلمة المرور',
        'action_url': reverse_lazy('Core:change_password'),
    })


def login_as(request, pk):
    user = User.objects.get(id=pk)
    login(request, user)
    return redirect('Core:index')


class PasswordReset(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = User
    form_class = PasswordResetForm
    template_name = 'Core/form_template.html'
    success_url = reverse_lazy('HR:EmployeeList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إعادة ضبط كلمة المرور للمستخدم: ' + str(self.object)
        context['action_url'] = reverse_lazy('Core:PasswordReset', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        return redirect('HR:EmployeeList')


class UserLogin(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request.POST.get('url'))
            else:
                error = 'تم إيقاف الحساب الخاص بك'
                return render(request, 'Auth/login.html', context={'error': error})
        else:
            error = 'برجاء التأكد من اسم المستخدم وكلمة السر'
            return render(request, 'Core/form_template.html', context={'error': error})

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('Website:HomePage')
        return render(request, 'Auth/website_login.html', self.get_context_data())


class RegisterUser(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'Core/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "تسجيل حساب جديد"
        return context


class UserLogout(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('Website:HomePage')


@login_required(login_url='Core:login')
def index(request):
    return render(request, 'Core/index.html')


class UserList(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'Core.list_users'
    paginate_by = 10

    def get_queryset(self):
        queryset = User.objects.filter(instance=self.request.user.instance)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'عرض المستخدمين'
        return context


class UserCreate(PermissionRequiredMixin, CreateView):
    model = User
    permission_required = 'Core.add_user'
    form_class = RegisterForm
    success_url = reverse_lazy('Core:UserList')
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة مستخدم'
        context['action_url'] = reverse_lazy('Core:UserCreate')
        return context

    def get_success_url(self):
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url


class UserUpdate(PermissionRequiredMixin, UpdateView):
    model = User
    permission_required = 'Core.edit_user'
    form_class = RegisterForm
    success_url = reverse_lazy('Core:UserList')
    template_name = 'forms/form_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل مستخدم'
        context['action_url'] = reverse_lazy('Core:UserUpdate', kwargs={'pk': self.object.id})
        return context

    def get_success_url(self):
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url

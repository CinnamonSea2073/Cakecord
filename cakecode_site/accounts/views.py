from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from . forms import UserCreateForm, LoginForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from .models import UserData

#indexページ
class Index(TemplateView):
    template_name = 'accounts/index.html'

index = Index.as_view()

""" ユーザ限定クラス """
class UserOnlyMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserDeleteView(UserOnlyMixin, generic.DeleteView):
    template_name = "accounts/delete.html"
    success_url = reverse_lazy("accounts:login")
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

#アカウント作成
class Create_Account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            #フォームに入力された'username', 'password1'が一致する会員をDBから探し，userに代入
            user = authenticate(username=username, password=password)
            login(request, user)
            UserData.objects.create(user=user, user_name=username, user_profile="")
            return redirect('/memevo_app/')
        return render(request, 'accounts/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'accounts/create.html', {'form': form,})

create_account = Create_Account.as_view()

#ログイン
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/memevo_app/')
        return render(request, 'accounts/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'accounts/login.html', {'form': form,})

account_login = Account_login.as_view()

#ログアウト
class Account_logout(LogoutView):
    template_name = 'accounts/index.html'
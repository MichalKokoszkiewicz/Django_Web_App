"""ALTBHP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeDoneView
from django.urls import include, path
from order.views import Register, szkolenie_wstepne_view, szkolenie_okresowe_view, szkolenie_pp_view, szkolenie_opp_view, szkolenie_inst_opp_view, audyt_view, ocena_ryzyka_view

import order.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', order.views.index),
    path('kontakt/', order.views.kontakt),
    path('szkolenia/', order.views.szkolenia),
    path('ocena/', order.views.ocena),
    path('pomoc/', order.views.pomoc),
    path('wypadek/', order.views.wypadek),
    path('doradztwo/', order.views.doradztwo),
    path('zamowienie/', order.views.orderserv),
    path('zamowienie/szkolenie_wstepne/', szkolenie_wstepne_view.as_view()),
    path('zamowienie/szkolenie_okresowe/', szkolenie_okresowe_view.as_view()),
    path('zamowienie/szkolenie_pp/', szkolenie_pp_view.as_view()),
    path('zamowienie/szkolenie_opp/', szkolenie_opp_view.as_view()),
    path('zamowienie/instrukcja_opp/', szkolenie_inst_opp_view.as_view()),
    path('zamowienie/audyt/', audyt_view.as_view()),
    path('zamowienie/ocena_ryzyka/', ocena_ryzyka_view.as_view()),
    path('zamowienie/koniec', order.views.success_order),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/profile/', order.views.profile),
    path('accounts/profile/order/1', order.views.profile_wstepne),
    path('accounts/profile/order/2', order.views.profile_okresowe),
    path('accounts/profile/order/3', order.views.profile_pp),
    path('accounts/profile/order/4', order.views.profile_opp),
    path('accounts/profile/order/5', order.views.profile_inst_opp),
    path('accounts/profile/order/6', order.views.profile_audyt),
    path('accounts/profile/order/7', order.views.profile_ocena_ryzyka),
    path('register/', Register.as_view()),
    path('register/success/', order.views.success_reg),
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(),
         {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),
         {'template_name': 'registration/password_change_done.html'}, name="password_change_done", ),
]

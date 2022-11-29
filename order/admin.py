from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, szkolenie_wstepne, szkolenie_okresowe, szkolenie_pp, szkolenie_opp, szkolenie_inst_opp, \
    audyt, ocena_ryzyka


class WstepneAdmin(admin.ModelAdmin):
    model = szkolenie_wstepne
    list_display = ('imie', 'nazwisko', 'email', 'nazwa_firmy', 'numer_nip', 'numer_telefonu', 'liczba_osob', 'kierownicze_czy_nie',
                    'niebezpiecznie_czy_nie', 'data')
    search_fields = ['nazwisko']

    def get_nazwisko(self, obj):
        return obj.szkolenie_wstepne.nazwisko


class OkresoweAdmin(admin.ModelAdmin):
    model = szkolenie_okresowe
    list_display = ('imie', 'nazwisko', 'rodzaj_szkolenia', 'email', 'nazwa_firmy', 'numer_nip', 'numer_telefonu', 'liczba_osob',
                    'niebezpiecznie_czy_nie', 'data')
    search_fields = ['nazwisko']

    def get_nazwisko(self, obj):
        return obj.szkolenie_okresowe.nazwisko


class PpAdmin(admin.ModelAdmin):
    model = szkolenie_pp
    list_display = ('imie', 'nazwisko', 'email', 'nazwa_firmy', 'numer_nip', 'numer_telefonu', 'liczba_osob', 'data')
    search_fields = ['nazwisko']

    def get_nazwisko(self, obj):
        return obj.szkolenie_pp.nazwisko


class OppAdmin(admin.ModelAdmin):
    model = szkolenie_opp
    list_display = ('imie', 'nazwisko', 'email', 'nazwa_firmy', 'numer_nip', 'numer_telefonu', 'liczba_osob', 'data')
    search_fields = ['nazwisko']

    def get_nazwisko(self, obj):
        return obj.szkolenie_opp.nazwisko


class InstAdmin(admin.ModelAdmin):
    model = szkolenie_inst_opp
    list_display = ('imie', 'nazwisko', 'email', 'nazwa_firmy', 'numer_nip', 'numer_telefonu', 'data')
    search_fields = ['nazwisko']

    def get_nazwisko(self, obj):
        return obj.szkolenie_inst_opp.nazwisko


class AudytAdmin(admin.ModelAdmin):
    model = audyt
    list_display = ('imie', 'nazwisko', 'rodzaj_audytu', 'email', 'nazwa_firmy', 'numer_nip', 'numer_telefonu', 'data')
    search_fields = ['nazwisko']

    def get_nazwisko(self, obj):
        return obj.audyt.nazwisko


class OcenaAdmin(admin.ModelAdmin):
    model = ocena_ryzyka
    list_display = ('imie', 'nazwisko', 'wybor_stanowiska', 'kod_zawodu', 'email', 'nazwa_firmy', 'numer_nip', 'numer_telefonu', 'data')
    search_fields = ['nazwisko']

    def get_nazwisko(self, obj):
        return obj.ocena_ryzyka.nazwisko


admin.site.register(CustomUser, UserAdmin)
admin.site.register(szkolenie_wstepne, WstepneAdmin)
admin.site.register(szkolenie_okresowe, OkresoweAdmin)
admin.site.register(szkolenie_pp, PpAdmin)
admin.site.register(szkolenie_opp, OppAdmin)
admin.site.register(szkolenie_inst_opp, InstAdmin)
admin.site.register(audyt, AudytAdmin)
admin.site.register(ocena_ryzyka, OcenaAdmin)

from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, szkolenie_wstepne, szkolenie_okresowe, szkolenie_pp, szkolenie_opp, szkolenie_inst_opp, \
    audyt, ocena_ryzyka


class form_szkolenie_wstepne(forms.ModelForm):
    imie = forms.CharField(
        label='Imię:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    nazwisko = forms.CharField(
        label='Nazwisko:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    nazwa_firmy = forms.CharField(
        label='Nazwa firmy:',
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa firmy'})
    )
    numer_nip = forms.CharField(
        label='NIP:',
        min_length=10,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'NIP'})
    )
    numer_telefonu = forms.CharField(
        label='Numer telefonu:',
        min_length=9,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'Numer telefonu'})
    )
    liczba_osob = forms.IntegerField(
        label="Ilość osób:"
    )
    kierownicze_czy_nie = forms.ChoiceField(
        label='Szkolenie na stanowiska kierownicze?',
        choices=[('Tak', 'Tak'), ('Nie', 'Nie')],

    )
    niebezpiecznie_czy_nie = forms.ChoiceField(
        label='Szkolenie na stanowiska niebezpieczne?',
        choices=[('Tak', 'Tak'), ('Nie', 'Nie')],
    )

    email = forms.EmailField(
        label='E-mail:',
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                                   message="Napisz poprawny e-mail: xxx@xx.xx")],
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )

    class Meta:
        model = szkolenie_wstepne
        exclude = ["creator", "data"]


class form_szkolenia_okresowe(forms.ModelForm):
    imie = forms.CharField(
        label='Imię:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )

    nazwisko = forms.CharField(
        label='Nazwisko:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )

    nazwa_firmy = forms.CharField(
        label='Nazwa firmy:',
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa firmy'})
    )

    numer_nip = forms.CharField(
        label='NIP:',
        min_length=10,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'NIP'})
    )

    numer_telefonu = forms.CharField(
        label='Numer telefonu:',
        min_length=9,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'Numer telefonu'})
    )

    liczba_osob = forms.IntegerField(
        label="Ilość osób:"
    )

    niebezpiecznie_czy_nie = forms.ChoiceField(
        label='Szkolenie na stanowiska niebezpieczne?',
        choices=[('Tak', 'Tak'), ('Nie', 'Nie')],
    )

    rodzaj_szkolenia = forms.ChoiceField(
        label='Rodzaj szkolenia:',
        choices=[('Pracodawcy i stanowiska kierownicze', 'Pracodawcy i stanowiska kierownicze'),
                 ('Stanowiska robotnicze', 'Stanowiska robotnicze'),
                 ('Stanowiska administracyjno-biurowe', 'Stanowiska administracyjno-biurowe'),
                 ('Stanowiska inżynieryjno-techniczne', 'Stanowiska inżynieryjno-techniczne'),
                 ('Stanowiska osób pełniących służbę BHP', 'Stanowiska osób pełniących służbę BHP')]
    )

    email = forms.EmailField(
        label='E-mail:',
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                                   message="Napisz poprawny e-mail: xxx@xx.xx")],
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )

    class Meta:
        model = szkolenie_okresowe
        exclude = ["creator", "data"]


class form_szkolenie_pp(forms.ModelForm):
    imie = forms.CharField(
        label='Imię:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    nazwisko = forms.CharField(
        label='Nazwisko:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    nazwa_firmy = forms.CharField(
        label='Nazwa firmy:',
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa firmy'})
    )
    numer_nip = forms.CharField(
        label='NIP:',
        min_length=10,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'NIP'})
    )
    numer_telefonu = forms.CharField(
        label='Numer telefonu:',
        min_length=9,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'Numer telefonu'})
    )
    liczba_osob = forms.IntegerField(
        label="Ilość osób:"
    )

    email = forms.EmailField(
        label='E-mail:',
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                                   message="Napisz poprawny e-mail: xxx@xx.xx")],
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )

    class Meta:
        model = szkolenie_pp
        exclude = ["creator", "data"]


class form_szkolenie_opp(forms.ModelForm):
    imie = forms.CharField(
        label='Imię:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    nazwisko = forms.CharField(
        label='Nazwisko:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    nazwa_firmy = forms.CharField(
        label='Nazwa firmy:',
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa firmy'})
    )
    numer_nip = forms.CharField(
        label='NIP:',
        min_length=10,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'NIP'})
    )
    numer_telefonu = forms.CharField(
        label='Numer telefonu:',
        min_length=9,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'Numer telefonu'})
    )
    liczba_osob = forms.IntegerField(
        label="Ilość osób:"
    )

    email = forms.EmailField(
        label='E-mail:',
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                                   message="Napisz poprawny e-mail: xxx@xx.xx")],
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )

    class Meta:
        model = szkolenie_opp
        exclude = ["creator", "data"]


class form_szkolenie_inst_opp(forms.ModelForm):
    imie = forms.CharField(
        label='Imię:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    nazwisko = forms.CharField(
        label='Nazwisko:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    nazwa_firmy = forms.CharField(
        label='Nazwa firmy:',
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa firmy'})
    )
    numer_nip = forms.CharField(
        label='NIP:',
        min_length=10,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'NIP'})
    )
    numer_telefonu = forms.CharField(
        label='Numer telefonu:',
        min_length=9,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'Numer telefonu'})
    )

    email = forms.EmailField(
        label='E-mail:',
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                                   message="Napisz poprawny e-mail: xxx@xx.xx")],
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )

    class Meta:
        model = szkolenie_inst_opp
        exclude = ["creator", "data"]


class form_audyt(forms.ModelForm):
    imie = forms.CharField(
        label='Imię:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    nazwisko = forms.CharField(
        label='Nazwisko:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    nazwa_firmy = forms.CharField(
        label='Nazwa firmy:',
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa firmy'})
    )
    numer_nip = forms.CharField(
        label='NIP:',
        min_length=10,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'NIP'})
    )
    numer_telefonu = forms.CharField(
        label='Numer telefonu:',
        min_length=9,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'Numer telefonu'})
    )

    rodzaj_audytu = forms.ChoiceField(
        label='Rodzaj audytu:',
        choices=[('BHP', 'BHP'), ('Przeciwpożarowy', 'Przeciwpożarowy')]
    )

    email = forms.EmailField(
        label='E-mail:',
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                                   message="Napisz poprawny e-mail: xxx@xx.xx")],
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )

    class Meta:
        model = audyt
        exclude = ["creator", "data"]


class form_ocena_ryzyka(forms.ModelForm):

    imie = forms.CharField(
        label='Imię:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    nazwisko = forms.CharField(
        label='Nazwisko:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    nazwa_firmy = forms.CharField(
        label='Nazwa firmy:',
        min_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa firmy'})
    )
    numer_nip = forms.CharField(
        label='NIP:',
        min_length=10,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'NIP'})
    )
    numer_telefonu = forms.CharField(
        label='Numer telefonu:',
        min_length=9,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'Numer telefonu'})
    )

    wybor_stanowiska = forms.CharField(
        label='Wybór stanowiska:',
        min_length=2,
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
        widget=forms.TextInput(attrs={'placeholder': 'Stanowisko'})
    )

    kod_zawodu = forms.CharField(
        label='Kod zawodu: ',
        min_length=6,
        validators=[RegexValidator(regex=r"^[0-9]*$", message="Tylko cyfry!")],
        widget=forms.TextInput(attrs={'placeholder': 'Kod zawodu'})
    )

    email = forms.EmailField(
        label='E-mail:',
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                                   message="Napisz poprawny e-mail: xxx@xx.xx")],
        widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )

    class Meta:
        model = ocena_ryzyka
        exclude = ["creator", "data"]


class RegisterForm1(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        label="Nazwa użytkownika",
        help_text="Tylko litery, cyfry i @/./+/-/_.",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nazwa użytkownika"
            }
        )
    )

    password1 = forms.CharField(
        label="Hasło:",
        help_text="Twoje hasło musi zawierać co najmniej 8 znaków. <br> Twoje hasło nie może być całkowicie numeryczne.",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Hasło"
            }
        )
    )

    password2 = forms.CharField(
        label="Powtórz hasło:",
        help_text="Wprowadź to samo hasło co poprzednio, w celu weryfikacji.",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Powtórz hasło"
            }
        )
    )

    first_name = forms.CharField(
        label="Imię",
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
    )

    last_name = forms.CharField(
        label="Nazwisko",
        validators=[RegexValidator(regex=r"^[a-zA-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃÀ-ÿ\s]*$", message="Tylko litery!")],
    )

    email = forms.EmailField(
        label="E-mail",
        validators=[RegexValidator(regex=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                                   message="Napisz poprawny e-mail: xxx@xx.xx")],
    )

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")

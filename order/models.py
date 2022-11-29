from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = "Użytkownicy"


class szkolenie_wstepne(models.Model):
    choices = [('Tak', 'Tak'), ('Nie', 'Nie')]
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nazwa_firmy = models.CharField(max_length=100)
    numer_nip = models.CharField(max_length=10)
    numer_telefonu = models.CharField(max_length=11)
    liczba_osob = models.IntegerField()
    kierownicze_czy_nie = models.CharField(max_length=3, choices=choices)
    niebezpiecznie_czy_nie = models.CharField(max_length=3, choices=choices)
    data = models.DateField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

    class Meta:
        verbose_name_plural = "Szkolenia wstępne"


class szkolenie_okresowe(models.Model):
    choices1 = [('Tak', 'Tak'), ('Nie', 'Nie')]
    choices2 = [('Pracodawcy i stanowiska kierownicze', 'Pracodawcy i stanowiska kierownicze'),
                ('Stanowiska robotnicze', 'Stanowiska robotnicze'),
                ('Stanowiska administracyjno-biurowe', 'Stanowiska administracyjno-biurowe'),
                ('Stanowiska inżynieryjno-techniczne', 'Stanowiska inżynieryjno-techniczne'),
                ('Stanowiska osób pełniących służbę BHP', 'Stanowiska osób pełniących służbę BHP')]
    rodzaj_szkolenia = models.CharField(max_length=50, choices=choices2)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nazwa_firmy = models.CharField(max_length=100)
    numer_nip = models.CharField(max_length=10)
    numer_telefonu = models.CharField(max_length=11)
    liczba_osob = models.IntegerField()
    niebezpiecznie_czy_nie = models.CharField(max_length=3, choices=choices1)
    data = models.DateField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

    class Meta:
        verbose_name_plural = "Szkolenia okresowe"


class szkolenie_pp(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nazwa_firmy = models.CharField(max_length=100)
    numer_nip = models.CharField(max_length=10)
    numer_telefonu = models.CharField(max_length=11)
    liczba_osob = models.IntegerField()
    data = models.DateField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

    class Meta:
        verbose_name_plural = "Szkolenia Pierwsza Pomoc"


class szkolenie_opp(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nazwa_firmy = models.CharField(max_length=100)
    numer_nip = models.CharField(max_length=10)
    numer_telefonu = models.CharField(max_length=11)
    liczba_osob = models.IntegerField()
    data = models.DateField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

    class Meta:
        verbose_name_plural = "Szkolenia Ochrony Przeciwpożarowej"


class szkolenie_inst_opp(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nazwa_firmy = models.CharField(max_length=100)
    numer_nip = models.CharField(max_length=10)
    numer_telefonu = models.CharField(max_length=11)
    data = models.DateField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

    class Meta:
        verbose_name_plural = "Instrukcja Ochrony Przeciwpożarowej"


class audyt(models.Model):
    choices = [('Przeciwpożarowy', 'Przeciwpożarowy'), ('BHP', 'BHP')]
    rodzaj_audytu = models.CharField(max_length=50, choices=choices)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nazwa_firmy = models.CharField(max_length=100)
    numer_nip = models.CharField(max_length=10)
    numer_telefonu = models.CharField(max_length=11)
    data = models.DateField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

    class Meta:
        verbose_name_plural = "Audyty"


class ocena_ryzyka(models.Model):
    wybor_stanowiska = models.CharField(max_length=50)
    kod_zawodu = models.CharField(max_length=6)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField()
    nazwa_firmy = models.CharField(max_length=100)
    numer_nip = models.CharField(max_length=10)
    numer_telefonu = models.CharField(max_length=11)
    data = models.DateField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

    class Meta:
        verbose_name_plural = "Oceny ryzyka"

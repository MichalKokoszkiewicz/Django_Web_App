from django.test import TestCase
from order.models import szkolenie_wstepne, CustomUser, szkolenie_okresowe, szkolenie_pp, szkolenie_opp, \
    szkolenie_inst_opp, audyt, ocena_ryzyka


class TestWstepneModel(TestCase):
    def setUp(self):
        self.customuser = CustomUser.objects.create(username='test', password='admintestalt')
        self.szkolenie = szkolenie_wstepne.objects.create(imie='Testaąeę', nazwisko='Testaąeę',
                                                          email='test00@test.com',
                                                          nazwa_firmy='ALT', numer_nip='1234567890',
                                                          numer_telefonu='123456789',
                                                          liczba_osob='5', kierownicze_czy_nie='Tak',
                                                          niebezpiecznie_czy_nie='Tak',
                                                          data='2022-11-14', creator=self.customuser)

    def test_create_szkolenie_wstepne(self):
        self.assertIsInstance(self.szkolenie, szkolenie_wstepne)

    def test_str_representation(self):
        self.assertEquals(str(self.szkolenie), "Testaąeę Testaąeę")


class TestOkresoweModel(TestCase):
    def setUp(self):
        self.customuser = CustomUser.objects.create(username='test', password='admintestalt')
        self.szkolenie = szkolenie_okresowe.objects.create(rodzaj_szkolenia='Stanowiska robotnicze', imie='Testaąeę',
                                                           nazwisko='Testaąeę',
                                                           email='test00@test.com',
                                                           nazwa_firmy='ALT', numer_nip='1234567890',
                                                           numer_telefonu='123456789',
                                                           liczba_osob='5',
                                                           niebezpiecznie_czy_nie='Tak',
                                                           data='2022-11-14', creator=self.customuser)

    def test_create_szkolenie_okresowe(self):
        self.assertIsInstance(self.szkolenie, szkolenie_okresowe)

    def test_str_representation(self):
        self.assertEquals(str(self.szkolenie), "Testaąeę Testaąeę")


class TestPpModel(TestCase):
    def setUp(self):
        self.customuser = CustomUser.objects.create(username='test', password='admintestalt')
        self.szkolenie = szkolenie_pp.objects.create(imie='Testaąeę',
                                                     nazwisko='Testaąeę',
                                                     email='test00@test.com',
                                                     nazwa_firmy='ALT', numer_nip='1234567890',
                                                     numer_telefonu='123456789',
                                                     liczba_osob='5',
                                                     data='2022-11-14', creator=self.customuser)

    def test_create_szkolenie_pp(self):
        self.assertIsInstance(self.szkolenie, szkolenie_pp)

    def test_str_representation(self):
        self.assertEquals(str(self.szkolenie), "Testaąeę Testaąeę")


class TestOppModel(TestCase):
    def setUp(self):
        self.customuser = CustomUser.objects.create(username='test', password='admintestalt')
        self.szkolenie = szkolenie_opp.objects.create(imie='Testaąeę',
                                                      nazwisko='Testaąeę',
                                                      email='test00@test.com',
                                                      nazwa_firmy='ALT', numer_nip='1234567890',
                                                      numer_telefonu='123456789',
                                                      liczba_osob='5',
                                                      data='2022-11-14', creator=self.customuser)

    def test_create_szkolenie_pp(self):
        self.assertIsInstance(self.szkolenie, szkolenie_opp)

    def test_str_representation(self):
        self.assertEquals(str(self.szkolenie), "Testaąeę Testaąeę")


class TestInstOppModel(TestCase):
    def setUp(self):
        self.customuser = CustomUser.objects.create(username='test', password='admintestalt')
        self.szkolenie = szkolenie_inst_opp.objects.create(imie='Testaąeę',
                                                           nazwisko='Testaąeę',
                                                           email='test00@test.com',
                                                           nazwa_firmy='ALT', numer_nip='1234567890',
                                                           numer_telefonu='123456789',
                                                           data='2022-11-14', creator=self.customuser)

    def test_create_szkolenie_pp(self):
        self.assertIsInstance(self.szkolenie, szkolenie_inst_opp)

    def test_str_representation(self):
        self.assertEquals(str(self.szkolenie), "Testaąeę Testaąeę")


class TestAudytModel(TestCase):
    def setUp(self):
        self.customuser = CustomUser.objects.create(username='test', password='admintestalt')
        self.szkolenie = audyt.objects.create(rodzaj_audytu='BHP',
                                              imie='Testaąeę',
                                              nazwisko='Testaąeę',
                                              email='test00@test.com',
                                              nazwa_firmy='ALT', numer_nip='1234567890',
                                              numer_telefonu='123456789',
                                              data='2022-11-14', creator=self.customuser)

    def test_create_szkolenie_pp(self):
        self.assertIsInstance(self.szkolenie, audyt)

    def test_str_representation(self):
        self.assertEquals(str(self.szkolenie), "Testaąeę Testaąeę")


class TestOcenaRyzykaModel(TestCase):
    def setUp(self):
        self.customuser = CustomUser.objects.create(username='test', password='admintestalt')
        self.szkolenie = ocena_ryzyka.objects.create(wybor_stanowiska='Test',
                                                     kod_zawodu='123456',
                                                     imie='Testaąeę',
                                                     nazwisko='Testaąeę',
                                                     email='test00@test.com',
                                                     nazwa_firmy='ALT', numer_nip='1234567890',
                                                     numer_telefonu='123456789',
                                                     data='2022-11-14', creator=self.customuser)

    def test_create_szkolenie_pp(self):
        self.assertIsInstance(self.szkolenie, ocena_ryzyka)

    def test_str_representation(self):
        self.assertEquals(str(self.szkolenie), "Testaąeę Testaąeę")

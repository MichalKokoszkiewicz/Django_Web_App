from django.test import TestCase
from order.forms import form_szkolenie_pp, form_szkolenie_wstepne, form_szkolenia_okresowe, form_szkolenie_opp, \
    form_szkolenie_inst_opp, form_audyt, form_ocena_ryzyka, RegisterForm1


class TestWstepneForm(TestCase):
    def test_valid(self):
        form_data = {
            'imie': 'Testaąeę',
            'nazwisko': 'Testaąeę',
            'nazwa_firmy': 'ALT',
            'numer_nip': '1234567890',
            'numer_telefonu': '123456789',
            'liczba_osob': 5,
            'kierownicze_czy_nie': 'Tak',
            'niebezpiecznie_czy_nie': 'Tak',
            'email': 'test00@test.com',
        }
        form = form_szkolenie_wstepne(data=form_data)
        self.assertTrue(form.is_valid())

    def test_not_valid(self):
        form_data = {
            'imie': '12345',
            'nazwisko': '12345',
            'nazwa_firmy': 'A',
            'numer_nip': '123456789a',
            'numer_telefonu': '12345678a',
            'liczba_osob': 'a',
            'niebezpiecznie_czy_nie': 'TAK',
            'kierownicze_czy_nie': 'TAK',
            'email': 'test',
        }
        form = form_szkolenie_wstepne(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 9)

    def test_no_data(self):
        form = form_szkolenie_wstepne(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 9)


class TestOkresoweForm(TestCase):
    def test_valid(self):
        form_data = {
            'imie': 'Testaąeę',
            'nazwisko': 'Testaąeę',
            'nazwa_firmy': 'ALT',
            'numer_nip': '1234567890',
            'numer_telefonu': '123456789',
            'liczba_osob': 5,
            'niebezpiecznie_czy_nie': 'Tak',
            'rodzaj_szkolenia': 'Stanowiska robotnicze',
            'email': 'test00@test.com',
        }
        form = form_szkolenia_okresowe(data=form_data)
        self.assertTrue(form.is_valid())

    def test_not_valid(self):
        form_data = {
            'imie': '12345',
            'nazwisko': '12345',
            'nazwa_firmy': 'A',
            'numer_nip': '123456789a',
            'numer_telefonu': '12345678a',
            'liczba_osob': 'a',
            'niebezpiecznie_czy_nie': 'TAK',
            'rodzaj_szkolenia': 'Robotnicze',
            'email': 'test',
        }
        form = form_szkolenia_okresowe(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 9)

    def test_no_data(self):
        form = form_szkolenia_okresowe(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 9)


class TestPpForm(TestCase):
    def test_valid(self):
        form_data = {
            'imie': 'Testaąeę',
            'nazwisko': 'Testaąeę',
            'nazwa_firmy': 'ALT',
            'numer_nip': '1234567890',
            'numer_telefonu': '123456789',
            'liczba_osob': 5,
            'email': 'test00@test.com',
        }
        form = form_szkolenie_pp(data=form_data)
        self.assertTrue(form.is_valid())

    def test_not_valid(self):
        form_data = {
            'imie': '12345',
            'nazwisko': '12345',
            'nazwa_firmy': 'A',
            'numer_nip': '123456789a',
            'numer_telefonu': '12345678a',
            'liczba_osob': 'a',
            'email': 'test',
        }
        form = form_szkolenie_pp(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)

    def test_no_data(self):
        form = form_szkolenie_pp(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)


class TestOppForm(TestCase):
    def test_valid(self):
        form_data = {
            'imie': 'Testaąeę',
            'nazwisko': 'Testaąeę',
            'nazwa_firmy': 'ALT',
            'numer_nip': '1234567890',
            'numer_telefonu': '123456789',
            'liczba_osob': 5,
            'email': 'test00@test.com',
        }
        form = form_szkolenie_opp(data=form_data)
        self.assertTrue(form.is_valid())

    def test_not_valid(self):
        form_data = {
            'imie': '12345',
            'nazwisko': '12345',
            'nazwa_firmy': 'A',
            'numer_nip': '123456789a',
            'numer_telefonu': '12345678a',
            'liczba_osob': 'a',
            'email': 'test',
        }
        form = form_szkolenie_opp(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)

    def test_no_data(self):
        form = form_szkolenie_opp(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)


class TestInstOppForm(TestCase):
    def test_valid(self):
        form_data = {
            'imie': 'Testaąeę',
            'nazwisko': 'Testaąeę',
            'nazwa_firmy': 'ALT',
            'numer_nip': '1234567890',
            'numer_telefonu': '123456789',
            'email': 'test00@test.com',
        }
        form = form_szkolenie_inst_opp(data=form_data)
        self.assertTrue(form.is_valid())

    def test_not_valid(self):
        form_data = {
            'imie': '12345',
            'nazwisko': '12345',
            'nazwa_firmy': 'A',
            'numer_nip': '123456789a',
            'numer_telefonu': '12345678a',
            'email': 'test',
        }
        form = form_szkolenie_inst_opp(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_no_data(self):
        form = form_szkolenie_inst_opp(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)


class TestAudytForm(TestCase):
    def test_valid(self):
        form_data = {
            'imie': 'Testaąeę',
            'nazwisko': 'Testaąeę',
            'nazwa_firmy': 'ALT',
            'numer_nip': '1234567890',
            'numer_telefonu': '123456789',
            'rodzaj_audytu': 'BHP',
            'email': 'test00@test.com',
        }
        form = form_audyt(data=form_data)
        self.assertTrue(form.is_valid())

    def test_not_valid(self):
        form_data = {
            'imie': '12345',
            'nazwisko': '12345',
            'nazwa_firmy': 'A',
            'numer_nip': '123456789a',
            'numer_telefonu': '12345678a',
            'rodzaj_audytu': 'bhp',
            'email': 'test',
        }
        form = form_audyt(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)

    def test_no_data(self):
        form = form_audyt(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)


class TestOcenaRyzykaForm(TestCase):
    def test_valid(self):
        form_data = {
            'imie': 'Testaąeę',
            'nazwisko': 'Testaąeę',
            'nazwa_firmy': 'ALT',
            'numer_nip': '1234567890',
            'numer_telefonu': '123456789',
            'wybor_stanowiska': 'Kucharz',
            'kod_zawodu': '123456',
            'email': 'test00@test.com',
        }
        form = form_ocena_ryzyka(data=form_data)
        self.assertTrue(form.is_valid())

    def test_not_valid(self):
        form_data = {
            'imie': '12345',
            'nazwisko': '12345',
            'nazwa_firmy': 'A',
            'numer_nip': '123456789a',
            'numer_telefonu': '12345678a',
            'wybor_stanowiska': '12345',
            'kod_zawodu': 'abc',
            'email': 'test',
        }
        form = form_ocena_ryzyka(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)

    def test_no_data(self):
        form = form_ocena_ryzyka(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)


class TestRegisterForm(TestCase):
    def test_valid(self):
        form_data = {
            'username': 'testuser',
            'password1': 'admintestalt',
            'password2': 'admintestalt',
            'first_name': 'testimie',
            'last_name': 'testnazwisko',
            'email': 'test@test.com',
        }
        form = RegisterForm1(data=form_data)
        self.assertTrue(form.is_valid())

    def test_no_data(self):
        form = RegisterForm1(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_not_same_passwords(self):
        form_data = {
            'username': 'testuser',
            'password1': 'admintestalt',
            'password2': 'admintestalta',
            'first_name': 'testimie',
            'last_name': 'testnazwisko',
            'email': 'test@test.com',
        }
        form = RegisterForm1(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_same_password_and_username(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testuser',
            'password2': 'testuser',
            'first_name': 'testimie',
            'last_name': 'testnazwisko',
            'email': 'test@test.com',
        }
        form = RegisterForm1(data=form_data)
        self.assertFalse(form.is_valid())

    def test_not_valid_email_and_password(self):
        form_data = {
            'username': 'testuser',
            'password1': '123456789',
            'password2': '123456789',
            'first_name': 'testimie',
            'last_name': 'testnazwisko',
            'email': 'test',
        }
        form = RegisterForm1(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


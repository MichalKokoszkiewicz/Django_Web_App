from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from order.views import index, profile, kontakt, szkolenia, ocena, pomoc, wypadek, doradztwo, orderserv, \
    profile_wstepne, profile_okresowe, profile_pp, profile_opp, profile_inst_opp, profile_audyt, profile_ocena_ryzyka, \
    success_order, szkolenie_pp_view, szkolenie_wstepne_view, szkolenie_okresowe_view, szkolenie_opp_view, \
    szkolenie_inst_opp_view, audyt_view, ocena_ryzyka_view, success_reg, Register
from order.models import CustomUser, szkolenie_pp, szkolenie_wstepne, szkolenie_okresowe, szkolenie_opp, \
    szkolenie_inst_opp, audyt, ocena_ryzyka


class TestIndexView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/index')
        response = index(request)
        self.assertEquals(response.status_code, 200)


class TestKontaktView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/kontakt')
        response = kontakt(request)
        self.assertEquals(response.status_code, 200)


class TestSzkoleniaView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/szkolenia')
        response = szkolenia(request)
        self.assertEquals(response.status_code, 200)


class TestOcenaView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/ocena')
        response = ocena(request)
        self.assertEquals(response.status_code, 200)


class TestPomocView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/pomoc')
        response = pomoc(request)
        self.assertEquals(response.status_code, 200)


class TestWypadekView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/wypadek')
        response = wypadek(request)
        self.assertEquals(response.status_code, 200)


class TestDoradztwoView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/doradztwo')
        response = doradztwo(request)
        self.assertEquals(response.status_code, 200)


class TestZamowieniaView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/zamowienie')
        response = orderserv(request)
        self.assertEquals(response.status_code, 200)


class TestSukcesView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/register/success')
        response = success_reg(request)
        self.assertEquals(response.status_code, 200)


class TestProfileView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/accounts/profile')
        request.user = AnonymousUser()
        response = profile(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/accounts/profile')
        request.user = self.test_user
        response = profile(request)
        self.assertEquals(response.status_code, 200)


class TestProfileWstepneView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/accounts/profile/order/1')
        request.user = AnonymousUser()
        response = profile_wstepne(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/accounts/profile/order/1')
        request.user = self.test_user
        response = profile_wstepne(request)
        self.assertEquals(response.status_code, 200)


class TestProfileOkresoweView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/accounts/profile/order/2')
        request.user = AnonymousUser()
        response = profile_okresowe(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/accounts/profile/order/2')
        request.user = self.test_user
        response = profile_okresowe(request)
        self.assertEquals(response.status_code, 200)


class TestProfilePPView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/accounts/profile/order/3')
        request.user = AnonymousUser()
        response = profile_pp(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/accounts/profile/order/3')
        request.user = self.test_user
        response = profile_pp(request)
        self.assertEquals(response.status_code, 200)


class TestProfileOppView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/accounts/profile/order/4')
        request.user = AnonymousUser()
        response = profile_opp(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/accounts/profile/order/4')
        request.user = self.test_user
        response = profile_opp(request)
        self.assertEquals(response.status_code, 200)


class TestProfileInstOppView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/accounts/profile/order/5')
        request.user = AnonymousUser()
        response = profile_inst_opp(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/accounts/profile/order/5')
        request.user = self.test_user
        response = profile_inst_opp(request)
        self.assertEquals(response.status_code, 200)


class TestProfileAudytView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/accounts/profile/order/6')
        request.user = AnonymousUser()
        response = profile_audyt(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/accounts/profile/order/6')
        request.user = self.test_user
        response = profile_audyt(request)
        self.assertEquals(response.status_code, 200)


class TestProfileOcenaRyzykaView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/accounts/profile/order/7')
        request.user = AnonymousUser()
        response = profile_ocena_ryzyka(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/accounts/profile/order/7')
        request.user = self.test_user
        response = profile_ocena_ryzyka(request)
        self.assertEquals(response.status_code, 200)


class TestSuccessOrderView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/zamowienie/koniec')
        request.user = AnonymousUser()
        response = success_order(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/zamowienie/koniec')
        request.user = self.test_user
        response = success_order(request)
        self.assertEquals(response.status_code, 200)


class TestCreateSzkolenieWstepneView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/zamowienie/szkolenie_wstepne')
        request.user = AnonymousUser()
        response = szkolenie_wstepne_view.as_view()(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/zamowienie/szkolenie_wstepne')
        request.user = self.test_user
        response = szkolenie_wstepne_view.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_saves_valid_form(self):
        szkolenie_wstepne_count = szkolenie_wstepne.objects.count()
        request = self.factory.post(
            "/zamowienie/szkolenie_wstepne", {
                'imie': 'Michał',
                'nazwisko': 'Kokoszkiewicz',
                'nazwa_firmy': 'ALT',
                'numer_nip': '1234567890',
                'numer_telefonu': '123456789',
                'liczba_osob': 5,
                'email': 'michal.kokoszkiewicz0@gmail.com',
                'kierownicze_czy_nie': 'Tak',
                'niebezpiecznie_czy_nie': 'Tak',
                'creator': self.test_user,
                'data': '2022-11-14',
            })
        request.user = self.test_user
        response = szkolenie_wstepne_view.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(szkolenie_wstepne.objects.count(), szkolenie_wstepne_count + 1)


class TestCreateSzkolenieOkresoweView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/zamowienie/szkolenie_okresowe')
        request.user = AnonymousUser()
        response = szkolenie_okresowe_view.as_view()(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/zamowienie/szkolenie_okresowe')
        request.user = self.test_user
        response = szkolenie_okresowe_view.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_saves_valid_form(self):
        szkolenie_okresowe_count = szkolenie_okresowe.objects.count()
        request = self.factory.post(
            "/zamowienie/szkolenie_okresowe", {
                'imie': 'Michał',
                'nazwisko': 'Kokoszkiewicz',
                'nazwa_firmy': 'ALT',
                'numer_nip': '1234567890',
                'numer_telefonu': '123456789',
                'liczba_osob': 5,
                'email': 'michal.kokoszkiewicz0@gmail.com',
                'niebezpiecznie_czy_nie': 'Tak',
                'rodzaj_szkolenia': 'Stanowiska robotnicze',
                'creator': self.test_user,
                'data': '2022-11-14',
            })
        request.user = self.test_user
        response = szkolenie_okresowe_view.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(szkolenie_okresowe.objects.count(), szkolenie_okresowe_count + 1)


class TestCreateSzkoleniePpView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/zamowienie/szkolenie_pp')
        request.user = AnonymousUser()
        response = szkolenie_pp_view.as_view()(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/zamowienie/szkolenie_pp')
        request.user = self.test_user
        response = szkolenie_pp_view.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_saves_valid_form(self):
        szkoleniepp_count = szkolenie_pp.objects.count()
        request = self.factory.post(
            "/zamowienie/szkolenie_pp/", {
                'imie': 'Michał',
                'nazwisko': 'Kokoszkiewicz',
                'nazwa_firmy': 'ALT',
                'numer_nip': '1234567890',
                'numer_telefonu': '123456789',
                'liczba_osob': 5,
                'email': 'michal.kokoszkiewicz0@gmail.com',
                'creator': self.test_user,
                'data': '2022-11-14',
            })
        request.user = self.test_user
        response = szkolenie_pp_view.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(szkolenie_pp.objects.count(), szkoleniepp_count + 1)


class TestCreateSzkolenieOppView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/zamowienie/szkolenie_opp')
        request.user = AnonymousUser()
        response = szkolenie_opp_view.as_view()(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/zamowienie/szkolenie_opp')
        request.user = self.test_user
        response = szkolenie_opp_view.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_saves_valid_form(self):
        szkolenieopp_count = szkolenie_opp.objects.count()
        request = self.factory.post(
            "/zamowienie/szkolenie_opp", {
                'imie': 'Michał',
                'nazwisko': 'Kokoszkiewicz',
                'nazwa_firmy': 'ALT',
                'numer_nip': '1234567890',
                'numer_telefonu': '123456789',
                'liczba_osob': 5,
                'email': 'michal.kokoszkiewicz0@gmail.com',
                'creator': self.test_user,
                'data': '2022-11-14',
            })
        request.user = self.test_user
        response = szkolenie_opp_view.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(szkolenie_opp.objects.count(), szkolenieopp_count + 1)


class TestCreateSzkolenieInstOppView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/zamowienie/instrukcja_opp')
        request.user = AnonymousUser()
        response = szkolenie_inst_opp_view.as_view()(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/zamowienie/instrukcja_opp')
        request.user = self.test_user
        response = szkolenie_inst_opp_view.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_saves_valid_form(self):
        szkolenieinstpp_count = szkolenie_inst_opp.objects.count()
        request = self.factory.post(
            "/zamowienie/instrukcja_opp", {
                'imie': 'Michał',
                'nazwisko': 'Kokoszkiewicz',
                'nazwa_firmy': 'ALT',
                'numer_nip': '1234567890',
                'numer_telefonu': '123456789',
                'email': 'michal.kokoszkiewicz0@gmail.com',
                'creator': self.test_user,
                'data': '2022-11-14',
            })
        request.user = self.test_user
        response = szkolenie_inst_opp_view.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(szkolenie_inst_opp.objects.count(), szkolenieinstpp_count + 1)


class TestCreateAudytView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/zamowienie/audyt')
        request.user = AnonymousUser()
        response = audyt_view.as_view()(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/zamowienie/audyt')
        request.user = self.test_user
        response = audyt_view.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_saves_valid_form(self):
        audyt_count = audyt.objects.count()
        request = self.factory.post(
            "/zamowienie/audyt", {
                'imie': 'Michał',
                'nazwisko': 'Kokoszkiewicz',
                'nazwa_firmy': 'ALT',
                'numer_nip': '1234567890',
                'numer_telefonu': '123456789',
                'rodzaj_audytu': 'BHP',
                'email': 'michal.kokoszkiewicz0@gmail.com',
                'creator': self.test_user,
                'data': '2022-11-14',
            })
        request.user = self.test_user
        response = audyt_view.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(audyt.objects.count(), audyt_count + 1)


class TestCreateOcenaRyzykaView(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='testuser', password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_not_authenticated(self):
        request = self.factory.get('/zamowienie/ocena_ryzyka')
        request.user = AnonymousUser()
        response = ocena_ryzyka_view.as_view()(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/zamowienie/ocena_ryzyka')
        request.user = self.test_user
        response = ocena_ryzyka_view.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_saves_valid_form(self):
        ocena_ryzyka_count = ocena_ryzyka.objects.count()
        request = self.factory.post(
            "/zamowienie/ocena_ryzyka", {
                'imie': 'Michał',
                'nazwisko': 'Kokoszkiewicz',
                'nazwa_firmy': 'ALT',
                'numer_nip': '1234567890',
                'numer_telefonu': '123456789',
                'wybor_stanowiska': 'Kucharz',
                'kod_zawodu': '123456',
                'email': 'michal.kokoszkiewicz0@gmail.com',
                'creator': self.test_user,
                'data': '2022-11-14',
            })
        request.user = self.test_user
        response = ocena_ryzyka_view.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ocena_ryzyka.objects.count(), ocena_ryzyka_count + 1)


class TestCreateRegisterView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test(self):
        request = self.factory.get('/register')
        response = Register.as_view()(request)
        self.assertEquals(response.status_code, 200)

    # def test_saves_valid_form(self):
    #     user_count = CustomUser.objects.count()
    #     request = self.factory.post(
    #         "/register", {
    #             'username': 'testuser',
    #             'password1': 'admintestalt',
    #             'password2': 'admintestalt',
    #             'first_name': 'testimie',
    #             'last_name': 'testnazwisko',
    #             'email': 'test@test.com',
    #         })
    #
    #     response = Register.as_view()(request)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(CustomUser.objects.count(), user_count + 1)

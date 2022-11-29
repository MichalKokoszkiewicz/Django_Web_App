from django import template
from order.models import szkolenie_wstepne

register = template.Library()


@register.inclusion_tag('order_list_wstepne.html')
def order_list(id):
    """Renderowanie listy książek przeczytanych przez użytkownika.

    :param: str username Nazwa użytkownika, którego książki należy pobrać

    :return: słownik książek przeczytanych przez użytkownika
    """
    order = szkolenie_wstepne.objects.filter(creator__id__contains=id)
    order_list_wstepne = [szkolenie_wstepne.__class__.objects.values('imie') for szkolenie_wstepne in order]
    # order_list_wstepne1 = [szkolenie_wstepne.imie for szkolenie_wstepne in order]
    return {'order_list_wstepne': order_list_wstepne}

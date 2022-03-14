from cart.models import cart, cartitem
from cart.views import _cart_id


def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            c=cart.objects.filter(cart_id=_cart_id(request))
            ci=cartitem.objects.all().filter(c=c[:1])
            for i in ci:
                item_count+=i.qty
        except cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)
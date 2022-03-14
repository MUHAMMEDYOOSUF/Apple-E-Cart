from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from cart.models import cart, cartitem
from cartapp.models import product
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):
    c=request.session.session_key
    if not c:
        c=request.session.create()

    return c

def add_cart(request,product_id):
    pro=product.objects.get(id=product_id)
    try:
        ca=cart.objects.get(cart_id=_cart_id(request))
    except cart.DoesNotExist:
        ca=cart.objects.create(cart_id=_cart_id(request))
        ca.save()
    try:
        ci=cartitem.objects.get(products=pro,c=ca)
        if ci.qty<ci.products.stock:
            ci.qty +=1
        ci.save()
    except cartitem.DoesNotExist:
        ci=cartitem.objects.create(products=pro,qty=1,c=ca)
        ci.save()

    return redirect('cart:cart_detail')

def cart_detail(request,total=0,counter=0,ci=None):
    try:
        ca=cart.objects.get(cart_id=_cart_id(request))
        ci=cartitem.objects.filter(c=ca,active=True)
        for i in ci:
            total+=(i.products.price*i.qty)
            counter+=i.qty
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(ci=ci,total=total,counter=counter))

def cart_remove(request,product_id):
    c=cart.objects.get(cart_id=_cart_id(request))
    pro=get_object_or_404(product,id=product_id)
    ci=cartitem.objects.get(products=pro,c=c)
    if ci.qty > 1:
        ci.qty-=1
        ci.save()
    else:
        ci.delete()
    return redirect('cart:cart_detail')

def full_remove(request,product_id):
    c = cart.objects.get(cart_id=_cart_id(request))
    pro = get_object_or_404(product, id=product_id)
    ci = cartitem.objects.get(products=pro, c=c)
    ci.delete()
    return redirect('cart:cart_detail')

from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    # print(product, cart)
    for val in keys:
        if int(val) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    # print(product, cart)
    for val in keys:
        if int(val) == product.id:
            return cart.get(val)
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name='cart_total')
def cart_total(products, cart):
    Sum=0
    for p in products:
        Sum += price_total(p, cart)
    return Sum

TAX_RATE = 0.08   # 8% sales tax


def item_total(price, quantity):
    """Cost of one line on the receipt."""
    return price * quantity


def add_tax(amount):
    """Add sales tax and round to cents."""
    return round(amount * (1 + TAX_RATE), 2)


def checkout(cart):
    """cart is a list of (price, quantity) tuples. Returns the final total."""
    subtotal = 0
    for price, quantity in cart:
        subtotal += item_total(price, quantity)
    return add_tax(subtotal)

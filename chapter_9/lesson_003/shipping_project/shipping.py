def shipping_cost(weight_kg):
    """Return the shipping cost in dollars for a package.

    Rules:
      - up to and including 1 kg ........ $5.00
      - over 1 kg, up to and including 5 kg ... $8.50
      - over 5 kg ....................... $12.00
    Raises TypeError if weight_kg is not a number.
    Raises ValueError if weight_kg is zero or negative.
    """
    if isinstance(weight_kg, bool) or not isinstance(weight_kg, (int, float)):
        raise TypeError("weight must be a number")
    if weight_kg <= 0:
        raise ValueError("weight must be greater than 0")

    if weight_kg <= 1:
        return 5.00
    elif weight_kg <= 5:
        return 8.50
    else:
        return 12.00

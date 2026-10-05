from shop import item_total, add_tax, checkout

# --- Unit tests: check ONE small piece by itself ---
assert item_total(2.50, 2) == 5.00
assert item_total(1.00, 0) == 0
assert add_tax(10.00) == 10.80
assert add_tax(0) == 0

# --- Integration test: check that the pieces work TOGETHER ---
cart = [(2.50, 2), (1.00, 3)]     # subtotal is 5.00 + 3.00 = 8.00
assert checkout(cart) == 8.64     # 8.00 plus 8% tax

print("Unit tests and integration test passed!")

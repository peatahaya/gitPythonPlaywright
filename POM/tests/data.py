from randomuser import RandomUser
# Data for login

# Valid user
username = 'standard_user'
password = 'secret_sauce'

# Invalid user
usernameInvalid = 'user'

# Urls
main_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
item_url = 'https://www.saucedemo.com/inventory-item.html?id=0'
cart_url = 'https://www.saucedemo.com/cart.html'
checkout_step_one_url = 'https://www.saucedemo.com/checkout-step-one.html'
checkout_step_two_url = 'https://www.saucedemo.com/checkout-step-two.html'
checkout_complete_url = 'https://www.saucedemo.com/checkout-complete.html'

# Item
item_name = "Sauce Labs Bike Light"
item_desc = ("A red light isn't the desired state in "
             "testing but it sure helps when riding your bike at night. "
             "Water-resistant with 3 lighting modes, 1 AAA battery included.")
item_price = "9.99"

# User information
user = RandomUser()
first_name = user.get_first_name()
last_name = user.get_last_name()
postal_code = str(user.get_postcode())
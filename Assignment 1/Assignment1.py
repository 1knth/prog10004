"""

Name: Kenneth Yang
Student #: 991873745
Date: September 28
Task: Create a program for a retailer that creates an invoice after a dialog with a customer. 

"""
# data objects
class Customer:
    def __init__(self):
        self.name: str = ""
        self.phone_number: str = ""
        self.postal_code: str = ""
        self.cart: list[dict] = []

class Payment_Summary:
    def __init__(self):
        self.subtotal_1: float = 0
        self.subtotal_2: float = 0
        self.hst: float = 0
        self.total: float = 0

# What: Obtains customer information
# How: Let user input name, phone number, and postal code and then save and return it in a new Customer object
def get_customer_info(customer) -> Customer:
    print("Hello, welcome to Terminal Convenience!")
    print("Please tell us your name, phone number, and postal code")
    customer.name = input("Enter your name: ")
    customer.phone_number = input("Enter your phone number: ")

    while len(customer.postal_code) > 7 or len(customer.postal_code) < 6:
        customer.postal_code = input("Enter your postal code: ")
    return customer

# What: Asks user for input on how much of each item they want to order
# How: Loops through and displays the name and price of the products dictionary, input gets saved into the Customer() object
def order(customer, products):
    for product, price in products.items():
        msg = "\n" + product + "'s are $" + format(price,'.2f') + "\nHow many would you like: "
        quantity = -1
        while quantity < 0:
            try:
                quantity = int(input(msg))
            except:
                print("Must be 0 or above")

        if quantity > 0:
            customer.cart.append({
                "quantity": quantity, 
                "name": product, 
                "unit_price": price,
                "total": quantity * price
            })

def draw_border(symbol):
    if symbol == "=":
        for i in range(63):
            print(symbol, end="")
    elif symbol == "-":
        for i in range(50):
            print(symbol, end="")
        print("|", end="")
        for i in range(12):
            print(symbol, end="")

    print("")

# What: Calculates the payments given a customer's cart and the given discount
# How: Performs operations on the Customer's cart and returns it in a new Payment_Summary() object
def payment_summary(cart,discount) -> Payment_Summary:
    payment = Payment_Summary()

    for item in cart:
        payment.subtotal_1 += item["total"]
    payment.hst = payment.subtotal_1 * 0.13
    payment.subtotal_2 = payment.subtotal_1 + payment.hst
    payment.total = payment.subtotal_2 - payment.subtotal_2 * discount * 0.01
    
    return payment 

# What: Prints out receipt in the terminal
# How: takes in customer object, discount, and payments then prints the values using format to structure the receipt
def generate_receipt(customer, discount, payment):
    draw_border("=")

    # print  header
    print(format("Terminal Convenience", ">22s"), "Customer:" + format(customer.name, ">29s"), sep=" | ") 
    print(format("www.samsfruitstand.com", ">22s"), format(customer.phone_number, ">38s"), sep=" | ") 
    print(format("", ">22s"), format(customer.postal_code, ">38s"), sep=" | ") 
    
    draw_border("=")

    # print products
    print(format("PRODUCT", ">25s"), format("QUANTITY", "8s"), format("UNIT PRICE", "10s"), format("TOTAL PRICE", "11s"), sep=" | ")
    for item in customer.cart: 
        print(
          format(item["name"], ">25s"), 
          format(item["quantity"], "8d"),
          format(item["unit_price"], "10.2f"),
          format(item["total"], "11.2f"),
          sep=" | "
        )

    draw_border("-")

    # print payment summary
    print(format("Sub Total 1", ">49s"), format(payment.subtotal_1, ">11.2f"), sep=" | ") 
    print(format("H.S.T", ">49s"), format(payment.hst, ">11.2f"), sep=" | ") 
    print(format("Sub Total 2", ">49s"), format(payment.subtotal_2, ">11.2f"), sep=" | ") 
    print(format("Discount" + " ("+ str(discount) +"%)", ">49s"), format(payment.subtotal_2 * discount * 0.01, ">11.2f"), sep=" | ") 
    print(format("Amount Due", ">49s"), format(payment.total, ">11.2f"), sep=" | ") 

    draw_border("=")

# main program
def main():
    discount = 0
    products = {
        "lighter": 1.50, 
        "chocolate bar": 2.00,
        "chips": 3.00, 
        "coke": 2.50,
        "coffee": 2.00 
    }

    customer = Customer()
    customer = get_customer_info(customer)

    # print("\nList of products:")
    # for product, price in products.items():
    #     print(product + ", $" + format(price, ".2f"))

    order(customer, products)
    discount = int(input("Enter your discount (0-100%): ")) # assume perfect input
    payment = payment_summary(customer.cart, discount)
    generate_receipt(customer, discount, payment)

main()


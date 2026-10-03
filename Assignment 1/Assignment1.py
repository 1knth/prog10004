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

class PaymentSummary:
    def __init__(self):
        self.subtotal_1: float = 0
        self.subtotal_2: float = 0
        self.hst: float = 0
        self.total: float = 0

# What: Obtains customer information
# How: Let user input name, phone number, and postal code and then save and return it in a new Customer object
def get_customer_info(customer) -> Customer:
    name = ""
    phone_number = ""
    postal_code = ""

    name = input("Enter your name: ")
    names = name.split()
    name = ""
    for noun in names:
        name += noun.capitalize() + " "
    name = name.strip()

    while len(phone_number) != 10 or not phone_number.isdigit():
        phone_number = input("Enter your phone number: ")
        phone_number = phone_number.strip().replace(" ", "").replace("-", "")

    phone_number = phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]

    while True:
        postal_code = input("Enter your postal code: ")
        postal_code = postal_code.upper().strip().replace(" ", "").replace("-","")

        if len(postal_code) != 6:
            print("only 6 characters allowed")
            continue

        # hard rules
        if (
            postal_code[0].isalpha() and 
            postal_code[1].isdigit() and 
            postal_code[2].isalpha() and  
            postal_code[3].isdigit() and 
            postal_code[4].isalpha() and 
            postal_code[5].isdigit() 
        ):
            break
    postal_code = postal_code[:3] + " " + postal_code[3:]

    customer.name = name
    customer.phone_number = phone_number
    customer.postal_code = postal_code

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
    print("|", end="")
    if symbol == "=":
        for i in range(64):
            print(symbol, end="")
    elif symbol == "-":
        for i in range(51):
            print(symbol, end="")
        print("|", end="")
        for i in range(12):
            print(symbol, end="")

    print("|")

# What: Calculates the payments given a customer's cart and the given discount
# How: Performs operations on the Customer's cart and returns it in a new PaymentSummary() object
def payment_summary(cart,discount) -> PaymentSummary:
    hst = 0.13
    subtotal_1 = 0
    subtotal_2 = 0
    payment_hst = 0
    total = 0

    payment = PaymentSummary()

    for item in cart:
        subtotal_1 += item["total"]
    payment_hst = subtotal_1 * hst
    subtotal_2 = subtotal_1 + payment_hst
    total = subtotal_2 - subtotal_2 * discount * 0.01

    payment.subtotal_1 = subtotal_1
    payment.subtotal_2 = subtotal_2
    payment.hst = payment_hst
    payment.total = total
    
    return payment 

# What: Prints out receipt in the terminal
# How: takes in customer object, discount, and payments then prints the values using format to structure the receipt
def generate_receipt(customer, discount, payment):
    store_name = "Terminal Convenience"
    # used the original website string to match Assignment1.docx output formatting
    website_address ="www.samsfruitstand.com" 
    draw_border("=")

    # print header
    print("|" + format(store_name, ">23s"), "Customer:" + format(customer.name, ">28s") + " ", sep=" | ", end="|\n")
    print("|" + format(website_address, ">23s"), format(customer.phone_number, ">37s") + " ", sep=" | ", end="|\n")
    print("|" + format("", ">23s"), format(customer.postal_code, ">37s") + " ", sep=" | ", end="|\n")
    
    draw_border("=")

    # print products
    print("|" + format("PRODUCT", ">26s"), format("QUANTITY", "8s"), format("UNIT PRICE", "10s"), format("TOTAL PRICE", "11s"), sep=" | ", end="|\n")
    for item in customer.cart: 
        print(
          "|" + format(item["name"], ">26s"), 
          format(item["quantity"], "8d"),
          format(item["unit_price"], "10.2f"),
          format(item["total"], "10.2f") + " ",
          sep=" | ",
          end="|\n"
        )

    draw_border("-")

    # print payment summary
    print("|" + format("Sub Total 1", ">50s"), format(payment.subtotal_1, ">10.2f") + " ", sep=" | ", end="|\n")
    print("|" + format("H.S.T", ">50s"), format(payment.hst, ">10.2f") + " ", sep=" | ", end="|\n")
    print("|" + format("Sub Total 2", ">50s"), format(payment.subtotal_2, ">10.2f") + " ", sep=" | ", end="|\n")
    print("|" + format("Discount" + " ("+ str(discount) +"%)", ">50s"), format(payment.subtotal_2 * discount * 0.01, ">10.2f") + " ", sep=" | ", end="|\n")
    print("|" + format("Amount Due", ">50s"), format(payment.total, ">10.2f") + " ", sep=" | ", end="|\n")

    draw_border("=")

# Main program
# I created a seperate function for main in order to declare these variables here instead of globally for clearer code
def main():
    # initialize data
    discount = 0
    products = {
        "lighter": 1.50, 
        "chocolate bar": 2.00,
        "chips": 3.00, 
        "coke": 2.50,
        "coffee": 2.00 
    }

    customer = Customer()

    # input
    print("Hello, welcome to Terminal Convenience!")
    print("Please tell us your name, phone number, and postal code")
    customer = get_customer_info(customer)
    
    order(customer, products)
    discount = int(input("Enter your discount (0-100%): ")) # assume perfect input
    
    # processing
    payment = payment_summary(customer.cart, discount)

    # output
    generate_receipt(customer, discount, payment)

if __name__ == "__main__":
    main()

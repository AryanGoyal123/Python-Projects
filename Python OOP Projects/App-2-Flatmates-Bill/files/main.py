from receipt import Receipt
from flatmate import Flatmate
from pdfreport import PdfReport


def main():
    print("Welcome to the receipt split calculator!")

    name1 = input("Please enter your name: ").strip()
    days_in_house_1 = int(input("How many days were you in the house?: ").strip())

    # Create Flat Mate 1 object
    flatmate1 = Flatmate(name=name1, days_in_house=days_in_house_1)

    name2 = input("Please enter your name: ").strip()
    days_in_house_2 = int(input("How many days were you in the house?: ").strip())

    # Create Flat Mate 2 object
    flatmate2 = Flatmate(name=name2, days_in_house=days_in_house_2)

    amount = int(input("Enter the receipt amount: ").strip())
    period = input("Enter the period: ").strip()

    # Create the Receipt Object
    receipt = Receipt(amount=amount, period=period)

    flatmate1_amount = flatmate1.pays(receipt, flatmate2)
    flatmate2_amount = flatmate2.pays(receipt, flatmate1)

    print(flatmate1_amount)
    print(flatmate2_amount)


if __name__ == '__main__':
    main()

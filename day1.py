import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"

def generate_phone_numbers(name: str) -> str:
    """Generates phone numbers by their name"""
    decoder = {"abc": "2", "def": "3", "ghi": "4",  "jkl": "5", "mno": "6",  "pqrs": "7", "tuv": "8","wxyz":  "9"}

    number = ""
    for letter in name:
        for decode in decoder.keys():
            if letter in decode:
                number += decoder[decode]
    return number

if __name__ == "__main__":
    customers =

    for customer in customers:
        last_name = customer["name"].split(' ')[1]
        if len(last_name) == 10 and "0" not in customer["phone"] and "1" not in customer["phone"]:
            number = generate_phone_numbers(last_name.lower())
            phone = ''.join(customer["phone"].split('-'))
            if number == phone:
                print(customer)

"""Day1: f you wanted a phone number that was easy-to-remember, you could get a number that spelled
something using the letters printed on the phone buttons: like 2 has “ABC”, and 3 “DEF”, etc. And I
guess this person had done that, so if you dialed the numbers corresponding to the letters in their name,
it would call their phone number!"""

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


def find_suspect(customers: pd.DataFrame):
    """Finds the suspect"""

    customer

if __name__ == "__main__":
    customers = pd.read_csv(CUSTOMER_DATA)

    for customer in customers:
        last_name = customer["name"].split(' ')[1]
        if len(last_name) == 10 and "0" not in customer["phone"] and "1" not in customer["phone"]:
            number = generate_phone_numbers(last_name.lower())
            phone = ''.join(customer["phone"].split('-'))
            if number == phone:
                print(customer)

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
    print(number)
    num = number[0:3] + "-" + number[3:6] + "-" + number[6:]
    print(num)
    return num


def find_suspect(customers: pd.DataFrame):
    """Finds the suspect"""

    # transform the name column into a separate lastname column
    customers["lastname"] = customers["name"].apply(lambda x: x.split(' ')[-1])

    # 1 and 0 are not letters on a phone keyboard
    customers = customers[customers["phone"].apply(lambda x: "0" not in x and "1" not in x)]

    # last name is length of phone number
    customers = customers[customers["lastname"].apply(lambda x: len(x) == 10)]

    customers = customers[customers["phone"] == customers["lastname"].apply(generate_phone_numbers)]

    print(customers)

if __name__ == "__main__":
    customers = pd.read_csv(CUSTOMER_DATA)

    find_suspect(customers)

    # for customer in customers:
    #     last_name = customer["name"].split(' ')[1]
    #     if len(last_name) == 10 and "0" not in customer["phone"] and "1" not in customer["phone"]:
    #         number = generate_phone_numbers(last_name.lower())
    #         phone = ''.join(customer["phone"].split('-'))
    #         if number == phone:
    #             print(customer)

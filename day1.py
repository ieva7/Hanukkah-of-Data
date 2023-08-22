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
    for letter in name.lower():
        for decode in decoder.keys():
            if letter in decode:
                number += decoder[decode]
    num = number[0:3] + "-" + number[3:6] + "-" + number[6:]
    return num


def find_suspect(customers: pd.DataFrame):
    """Finds the suspect"""

    # transform the name column into a separate lastname column
    customers["lastname"] = customers["name"].apply(lambda x: x.split(' ')[-1])

    # 1 and 0 are not letters on a phone keyboard
    customers = customers[customers["phone"].apply(lambda x: "0" not in x and "1" not in x)]

    # last name is length of phone number
    customers = customers[customers["lastname"].apply(lambda x: len(x) == 10)]

    # applying the function
    customers = customers[customers["phone"] == customers["lastname"].apply(generate_phone_numbers)]

    # printing the final suspect(s)
    print(customers)
    # 2187   3188  Sam Guttenberg  221 Banker St  Brooklyn, NY 11222  1998-05-30  488-836-2374  Guttenberg


if __name__ == "__main__":
    customers = pd.read_csv(CUSTOMER_DATA)

    find_suspect(customers)


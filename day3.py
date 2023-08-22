"""so I gave it to this guy who lived in my neighborhood. He said that he was
naturally assertive because he was a Aries born in the year of the Dog, so maybe
he was able to clean it. I don’t remember his name. Last time I saw him, he was
leaving the subway and carrying a bag from Noah’s."""
import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
# "HOM8601","Rug Cleaner",3.51


def filter_birthdate(birthdate: str) -> bool:
    """Filter for Aries and born in Dog Year. Returns True if Dog and Aries"""
    # Plausible years
    dog_years = [1994, 1982, 1970, 1958, 1946, 1934, 1922]
    # aries: 0320 0420

    birthdate = birthdate.split('-')
    mnthd = int(birthdate[1] + birthdate[2])
    if int(birthdate[0]) in dog_years and mnthd >= 320 and mnthd <= 420:
        return True
    return False


def find_orders(o_data: list, suspects: list, o_i_data: list):
    narrowed_suspects = []
    for person in suspects:
        for row in o_data:
            if person["customerid"] == row["customerid"]:
                order_id = row["orderid"]
                break
        for row in o_i_data:
            if row["orderid"] == order_id:
                if row["sku"] == "HOM8601":
                    print(order_id)
                    narrowed_suspects.append(person)
    return narrowed_suspects


if __name__ == "__main__":
    customers = pd.read_csv(CUSTOMER_DATA)

    # filter birthdates
    customers = customers[customers["birthdate"].apply(filter_birthdate)]

    # filter for his neighbourhood
    customers = customers[customers["citystatezip"].str.contains("South Ozone Park")]

    print(customers)
    # 1273        2274  Brent Nguyen  109-19 110th St  South Ozone Park, NY 11420  1958-03-25  516-636-7397
    # an alternative is to look for rug cleaner!

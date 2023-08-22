"""Day2: As they’re right across the street from Noah’s, they usually talked about the
project over coffee and bagels at Noah’s before handing off the item to be cleaned. The
contractors would pick up the tab and expense it, along with their cleaning supplies.
The claim ticket said ‘2017 spec JD’. ‘2017’ is the year the item was brought in, and ‘JD’
is the initials of the contractor."""
import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
# fun fact: they only sell one type of coffee at Noah's
COFFEE_ID = '"DLI1464","Coffee, Drip",6.21'


def is_J_D_name(name: str) -> bool:
    """Returns True if name has JD initials"""

    name = name.split(' ')
    if name[0] == 'J' and name[-1] == 'D':
        return True
    return False


def find_suspects(o_data: list, suspects: list, o_i_data: list):

    narrowed_suspects = []
    for person in suspects:
        for row in o_data:
            if person["customerid"] == row["customerid"]:
                order_id = row["orderid"]
                break
        for row in o_i_data:
            if row["orderid"] == order_id:
                if row["sku"] == "DLI1464":
                    narrowed_suspects.append(person)
    return narrowed_suspects


if __name__ == "__main__":

    customers = pd.read_csv(CUSTOMER_DATA)
    orders = pd.read_csv(ORDER_DATA)
    order_details = pd.read_csv(ORDER_ITEMS_DATA)

    # only customers with JD initials can stay
    customers = customers[customers["name"].apply(is_J_D_name)]

    # combining three datasets to find their order items
    customers = customers.merge(orders, how="left", on="customerid")["orderid"]

    print(customers)
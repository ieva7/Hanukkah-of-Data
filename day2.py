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
    if name[0][0] == 'J' and name[-1][0] == 'D':
        return True
    return False


if __name__ == "__main__":

    customers = pd.read_csv(CUSTOMER_DATA)
    orders = pd.read_csv(ORDER_DATA)
    order_details = pd.read_csv(ORDER_ITEMS_DATA)

    # only customers with JD initials can stay
    customers = customers[customers["name"].apply(is_J_D_name)]

    # combining three datasets to find their order items
    customers = customers.merge(orders, how="left", on="customerid")[["name", "phone", "orderid", "ordered", "shipped"]]

    # only keeping in-store orders
    customers = customers[customers["ordered"] == customers["shipped"]].drop(columns="shipped")

    # merging for order details
    customers = customers.merge(order_details, how="left", on="orderid")

    # finalising suspects who ordered Drip coffee
    customers = customers[customers["sku"] == "DLI1464"]

    print(customers)
    # 335  Jeremy Davis  212-771-8924   7409.0  2017-04-05 12:49:41  DLI1464    1        7.73
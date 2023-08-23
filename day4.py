"""Thankfully, this woman I met on Tinder came over at 5am with her bike chain
repair kit and some pastries from Noah’s. Apparently she liked to get up before
dawn and claim the first pastries that came out of the oven."""
import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_DETAIL_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"


def find_by_time_of_purchase(orders: pd.DataFrame):
    """Find in-store orders between 3-5am, after buying carpet cleaner but before 'years ago'"""

    orders["ordered"] = pd.to_datetime(orders["ordered"])
    orders.index = orders["ordered"]
    # Store is in Manhattan, Tapestry man is in Queens, South Ozone Park. Most time it would take to get from
    # Manhattan to his is 1.5hrs according to Google
    orders = orders.between_time("03:00", "05:00")
    orders = orders[orders['ordered'].between("2017-02-18", "2018-12-31")]

    # transaction in-person
    orders = orders[orders["ordered"] == orders["shipped"]]

    return orders


def find_items(orderid: str, order_details: pd.DataFrame, products: pd.DataFrame) -> list:
    """Finds the item names by sku"""

    items = list(order_details[order_details["orderid"] == orderid]["sku"])

    items = [products[products["sku"] == item]["desc"] for item in items]
    return items


if __name__ == "__main__":
    customers = pd.read_csv(CUSTOMER_DATA)
    orders = pd.read_csv(ORDER_DATA)
    order_details = pd.read_csv(ORDER_DETAIL_DATA)
    products = pd.read_csv(PRODUCTS_DATA)

    orders = find_by_time_of_purchase(orders)

    # under 40 dollars
    orders = orders[orders["total"] <= 40]

    # customers of legal age
    customers = customers[customers["birthdate"] <= "2000-12-31"]

    customers = customers.merge(orders, how="inner", on="customerid")[["name", "phone", "ordered", "orderid"]]


    customers["items"] = customers["orderid"].apply(lambda x: find_items(x, order_details, products))

    print(customers)
    # frequent buyer of baked goods
    #  Christina Booker  718-649-9036 2018-08-27 04:14:45    58193      [[Caraway Bagel]]



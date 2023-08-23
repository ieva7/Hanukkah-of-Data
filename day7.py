"""Day7: He said ‘I got almost exactly the same thing!’ We laughed about
it and wound up swapping items because he had wanted the color I got. We
had a moment when our eyes met and my heart stopped for a second. I asked
him to get some food with me and we spent the rest of the day together."""
import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"


def find_emilys_purchases(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Search for only Emily's purchases"""

    data = customers[customers["name"] == "Emily Randolph"]
    orders = orders[orders["ordered"] == orders["shipped"]]

    data = data.merge(orders, how="inner", on="customerid")[["customerid", "orderid", "ordered"]]
    return data


def filter_items(orders: pd.DataFrame, order_details: pd.DataFrame, products: \
                           pd.DataFrame):
    """Find purchases with variation"""
    # Find item descriptions
    orders = orders.merge(order_details, how="left", on="orderid")
    orders = orders.merge(products, how="left", on="sku")[["customerid", "ordered", "desc", "sku"]]

    orders["ordered"] = pd.to_datetime(orders["ordered"])

    # find items with colour variation
    orders = orders[orders["desc"].str.contains("\(")]

    return orders


if __name__ == "__main__":
    customers = pd.read_csv(CUSTOMER_DATA)
    orders = pd.read_csv(ORDER_DATA)
    order_details = pd.read_csv(ORDER_ITEMS_DATA)
    products = pd.read_csv(PRODUCTS_DATA)

    emily_orders = find_emilys_purchases(customers, orders)
    emily_orders = filter_items(emily_orders, order_details, products)

    suspect_orders = filter_items(orders, order_details, products)

    #same day purchases as Emily
    suspect_orders = suspect_orders[suspect_orders["ordered"].dt.date.isin(emily_orders["ordered"].dt.date)]

    # re-formatting sku
    suspect_orders["sku"] = suspect_orders["sku"].str[:3]
    emily_orders["sku"] = emily_orders["sku"].str[:3]

    # merging the datasets
    merged_orders = emily_orders.merge(suspect_orders, how = "inner", on="sku")
    merged_orders = merged_orders[merged_orders["customerid_x"] != merged_orders["customerid_y"]]

    # refiltering for items to match
    merged_orders["desc_x"] = merged_orders["desc_x"].str.extract('(.*)(?=\s+\()')
    merged_orders["desc_y"] = merged_orders["desc_y"].str.extract('(.*)(?=\s+\()')
    merged_orders = merged_orders[merged_orders["desc_x"] == merged_orders["desc_y"]]

    print(merged_orders)
    # by manually cross-refrencing, only one suspect:
    # 8835,"Jonathan Adams","644 Targee St","Staten Island, NY 10304","1975-08-26","315-618-5263"

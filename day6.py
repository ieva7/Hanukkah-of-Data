"""Day6: She’s always been very frugal, and she clips every coupon and shops every
sale at Noah’s Market. In fact I like to tease her that Noah actually loses money
whenever she comes in the store. I think she’s been taking it too far lately though.
Once the subway fare increased, she stopped coming to visit me. And she’s really slow to
respond to my texts."""
import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"


def find_sales(order_details: pd.DataFrame, products: \
                                        pd.DataFrame) -> pd.DataFrame:
    """Finding all the sales items"""

    sales_items = order_details.merge(products, how="left", on="sku")

    # sold for less than wholesale purchase
    sales_items = sales_items[sales_items["wholesale_cost"] >= sales_items["unit_price"]]
    return sales_items


def find_by_frequency(orders: pd.DataFrame, merged_sales_data: pd.DataFrame, customers: pd.DataFrame):
    """Find top sales shoppers"""

    orders = orders[orders["ordered"] == orders["shipped"]]

    order_data = merged_sales_data.merge(orders, how="inner", on="orderid")

    merge_with_people = order_data.merge(customers, how="left", on="customerid")[["orderid", "desc", "name", "total"]]

    frequency = merge_with_people["name"].value_counts().head()
    print(frequency)
    # Emily Randolph  14, ahead by 9 purchases in first place

if __name__ == "__main__":
    customers = pd.read_csv(CUSTOMER_DATA)
    orders = pd.read_csv(ORDER_DATA)
    order_details = pd.read_csv(ORDER_ITEMS_DATA)
    products = pd.read_csv(PRODUCTS_DATA)

    find_by_frequency(orders, find_sales(order_details, products), customers)
    # 8342,"Emily Randolph","1055A E 3rd St","Brooklyn, NY 11230","1988-10-30","914-868-0316"


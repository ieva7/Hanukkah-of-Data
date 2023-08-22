import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"

people_data = pd.read_csv(CUSTOMER_DATA)
order_data = pd.read_csv(ORDER_DATA)
o_i_data = pd.read_csv(ORDER_ITEMS_DATA)
product_data = pd.read_csv(PRODUCTS_DATA)


def merge_items_and_order_items_to_find_sales(o_i_data, product_data):

    sales_items = o_i_data.merge(product_data, how="left", on="sku")
    sales_items = sales_items[sales_items["wholesale_cost"] >= sales_items["unit_price"]]
    return sales_items

def find_by_time_of_purchase(o_data: pd.DataFrame, merged_sales_data, people_data):

    o_data = o_data[o_data["ordered"] == o_data["shipped"]]

    order_data = merged_sales_data.merge(o_data, how="inner", on="orderid")
    order_data = order_data.drop(columns=["shipped", "items", "qty", "sku", "wholesale_cost", "unit_price"])

    merge_with_people = order_data.merge(people_data, how="left", on="customerid")

    frequency = merge_with_people["name"].value_counts()
    print(frequency)
    # is emily our suspect? YES
    # 8342,"Emily Randolph","1055A E 3rd St","Brooklyn, NY 11230","1988-10-30","914-868-0316"


sales_items = merge_items_and_order_items_to_find_sales(o_i_data, product_data)

find_by_time_of_purchase(order_data, sales_items, people_data)


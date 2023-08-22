import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"

people_data = pd.read_csv(CUSTOMER_DATA)
order_data = pd.read_csv(ORDER_DATA)
o_i_data = pd.read_csv(ORDER_ITEMS_DATA)
product_data = pd.read_csv(PRODUCTS_DATA)

def find_by_time_of_purchase(o_data: pd.DataFrame, people_data, o_i_data, product_data):
    # lives in queens village
    people_data = people_data[people_data["citystatezip"].str.contains("Queens Village")]

    # bought cat food after the tapestry was given away to tinder bestie
    o_data["ordered"] = pd.to_datetime(o_data["ordered"])
    o_data.index = o_data["ordered"]
    o_data = o_data[o_data['ordered'].between("2022-07-15", "2023-12-31")]

    suspects = people_data[people_data["customerid"].isin(o_data["customerid"])]
    print(suspects)
    # this was it LMAO

suspects = find_by_time_of_purchase(order_data, people_data, o_i_data, product_data)

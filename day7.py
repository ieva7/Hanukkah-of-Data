import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"

people_data = pd.read_csv(CUSTOMER_DATA)
order_data = pd.read_csv(ORDER_DATA)
o_i_data = pd.read_csv(ORDER_ITEMS_DATA)
product_data = pd.read_csv(PRODUCTS_DATA)


def find_emilys_purchases_after_rug(people_data, o_data):

    data = people_data[people_data["name"] == "Emily Randolph"]
    o_data = o_data[o_data["ordered"] == o_data["shipped"]]

    # purchases after getting rug I am confused as to when this handoff happened
    o_data["ordered"] = pd.to_datetime(o_data["ordered"])
    o_data.index = o_data["ordered"]
    o_data = o_data[o_data['ordered'].between("2017-01-15", "2023-12-31")]

    data = data.merge(o_data, how="inner", on="customerid")
    data = data.drop(columns=["items", "birthdate", "citystatezip", "phone", "address", "shipped"])
    return data


def merge_emily_with_items(emily_orders, o_i_data, product_data):
    emily_orders = emily_orders.merge(o_i_data, how="left", on="orderid")
    emily_orders = emily_orders.merge(product_data, how="left", on="sku")

    # find items with colour variation
    emily_orders = emily_orders[emily_orders["desc"].str.contains("\(")]
    print(emily_orders)
    return emily_orders


def filter_for_purchases_and_date(o_i_data, order_data, product_data, emily_orders):

    merged = order_data.merge(o_i_data, "left", on="orderid")
    merged = merged.merge(product_data, "left", on="sku")

    merged = merged[merged["ordered"] == merged["shipped"]]

    # purchases after getting rug
    merged["ordered"] = pd.to_datetime(merged["ordered"])
    # purchases with colour options
    merged = merged[merged["desc"].str.contains("\(")]
    #same day purchases as Emily
    merged = merged[merged["ordered"].dt.date.isin(emily_orders["ordered"].dt.date)]

    # gonna hand-change values because idk how else to do this
    merged = merged[merged["desc"].str.contains("Electric Machine")]

    print(merged)
    # two hours apart
    #4236,"Melvin Rodriguez III","228A E 115th St","Manhattan, NY 10029","1970-11-22","914-698-1257"
    # same time!!!!!
    # 8835,"Jonathan Adams","644 Targee St","Staten Island, NY 10304","1975-08-26","315-618-5263"


emily_orders = find_emilys_purchases_after_rug(people_data, order_data)

emily_orders = merge_emily_with_items(emily_orders, o_i_data, product_data)

filter_for_purchases_and_date(o_i_data, order_data, product_data, emily_orders)
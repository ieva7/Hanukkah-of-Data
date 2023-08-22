import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"

people_data = pd.read_csv(CUSTOMER_DATA)
order_data = pd.read_csv(ORDER_DATA)
o_i_data = pd.read_csv(ORDER_ITEMS_DATA)
product_data = pd.read_csv(PRODUCTS_DATA)

# new date: 2019-06-01

def filter_by_noahs_collectibles(o_i_data, order_data, product_data):

    order_data = o_i_data.merge(order_data, how="inner", on="orderid")
    order_data = order_data.drop(columns=["shipped", "items"])

    merge_with_products = order_data.merge(product_data, how="left", on="sku")
    merge_with_products = merge_with_products.drop(columns=["unit_price", "total", "wholesale_cost"])

    # collectibles will probs have "Noah's" in the name
    merge_with_products = merge_with_products[merge_with_products["desc"].str.contains("Noah's")]

    # which show up most frequently?
    individuals = merge_with_products["customerid"].value_counts().reset_index().sort_values(by="count")

    print(individuals)
    # Three times as much purchases of "Noah's" as the second top
    #4308,"Travis Bartlett","2527B Adam Clayton Powell Jr Blvd","Manhattan, NY 10039","1942-07-22","929-906-5980"

filter_by_noahs_collectibles(o_i_data, order_data, product_data)
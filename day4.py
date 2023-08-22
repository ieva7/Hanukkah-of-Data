import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"


people_data = pd.read_csv(CUSTOMER_DATA)
o_data = pd.read_csv(ORDER_DATA)
o_i_data = pd.read_csv(ORDER_ITEMS_DATA)
p_data = pd.read_csv(PRODUCTS_DATA)



def find_by_time_of_purchase(o_data: pd.DataFrame, people_data, items, products):
    """Find orders before 5am and between 2017 and 2018"""
    o_data["ordered"] = pd.to_datetime(o_data["ordered"])
    o_data.index = o_data["ordered"]
    o_data = o_data.between_time("00:00", "05:00")
    o_data = o_data[o_data['ordered'].between("2017-04-17", "2023-12-31")]
    # transaction in-person
    o_data = o_data[o_data["ordered"] == o_data["shipped"]]
    # under 40 dollars
    o_data = o_data[o_data["total"] <= 40]

    suspects = people_data[people_data["customerid"].isin(o_data["customerid"])]
    # of legal age
    suspects = suspects[suspects["birthdate"] <= "2000-12-31"]

    big_marge = suspects.merge(o_data, how="left", on="customerid")
    big_marge = big_marge.drop(columns=["total", "ordered", "items"])
    big_marge = big_marge.merge(items, how="left", on="orderid")
    big_marge = big_marge.drop(columns=["address"])
    big_marge = big_marge.merge(products, how="left", on="sku")
    big_marge = big_marge.drop(columns=["orderid", "sku"])

    big_marge = big_marge[big_marge["desc"].str.contains("Twist")]



    print(big_marge)
    return big_marge


suspects = find_by_time_of_purchase(o_data, people_data, o_i_data, p_data)

# 204        5375  Christina Booker      Bronx, NY 10474  1981-01-08  718-649-9036  2022-07-15 04:38:38    2        7.25  Caraway Twist            6.15


"""a woman in Queens Village came to pick it up. She was wearing a ‘Noah’s Market’ sweatshirt,
and it was just covered in cat hair. When I suggested that a clowder of cats might ruin such a
fine tapestry, she looked at me funny and said she only had ten or eleven cats and they were
getting quite old and had cataracts now so they probably wouldn’t notice some old rug anyway."""
import pandas as pd

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"


def find_by_time_of_purchase(orders: pd.DataFrame, customers: pd.DataFrame):
    # lives in queens village
    customers = customers[customers["citystatezip"].str.contains("Queens Village")]

    # bought cat food after the tapestry was given away to tinder woman
    orders["ordered"] = pd.to_datetime(orders["ordered"])
    orders.index = orders["ordered"]
    orders = orders[orders['ordered'].between("2022-07-15", "2023-12-31")]

    return customers[customers["customerid"].isin(orders["customerid"])]


if __name__ == "__main__":
    customers = pd.read_csv(CUSTOMER_DATA)
    orders = pd.read_csv(ORDER_DATA)
    order_details = pd.read_csv(ORDER_ITEMS_DATA)
    products = pd.read_csv(PRODUCTS_DATA)

    suspects = find_by_time_of_purchase(orders, customers)
    print(suspects)
    # this was it :)
    # 6674         7675       Anita Koch     106-51 214th St  Queens Village, NY 11429  1955-11-14  315-492-7411


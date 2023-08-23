"""Day8: she gave it to an acquaintance of hers who collects all sorts of junk. Apparently he owns
an entire set of Noah’s collectibles! He probably still has the rug, even."""
import pandas as pd

ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"
# new date: 2019-06-01

def filter_by_noahs_collectibles(order_details, orders, products):
    """Find the collectibles and sales counts, find the collector"""

    orders = order_details.merge(orders, how="inner", on="orderid")
    merge_with_products = orders.merge(products, how="left", on="sku")

    # collectibles will probs have "Noah's" in the name
    merge_with_products = merge_with_products[merge_with_products["desc"].str.contains("Noah's")]

    # which show up most frequently?
    individuals = merge_with_products["customerid"].value_counts().reset_index().sort_values(by="count").tail()

    print(individuals)
    # One individual has three times as much of "Noah's" purchases as the second top
    #4308,"Travis Bartlett","2527B Adam Clayton Powell Jr Blvd","Manhattan, NY 10039","1942-07-22","929-906-5980"


if __name__ == "__main__":
    orders = pd.read_csv(ORDER_DATA)
    order_details = pd.read_csv(ORDER_ITEMS_DATA)
    products = pd.read_csv(PRODUCTS_DATA)

    filter_by_noahs_collectibles(order_details, orders, products)

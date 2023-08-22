from day1 import read_csv

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
PRODUCTS_DATA = "./noahs-csv/noahs-products.csv"
# "HOM8601","Rug Cleaner",3.51

def filter_birthdate(data: list) -> list:
    """Filter for Aries and born in Dog Year"""
    dog_years = [1994, 1982, 1970, 1958, 1946, 1934, 1922]
    # aries: 0320 0420
    suspects = []
    for person in data:
        birthdate = person['birthdate'].split('-')
        mnthd = int(birthdate[1] + birthdate[2])
        if int(birthdate[0]) in dog_years and mnthd >= 320 and mnthd <= 420:
            suspects.append(person)
    return suspects


def find_orders(o_data: list, suspects: list, o_i_data: list):
    narrowed_suspects = []
    for person in suspects:
        for row in o_data:
            if person["customerid"] == row["customerid"]:
                order_id = row["orderid"]
                break
        for row in o_i_data:
            if row["orderid"] == order_id:
                if row["sku"] == "HOM8601":
                    print(order_id)
                    narrowed_suspects.append(person)
    return narrowed_suspects


people_data = read_csv(CUSTOMER_DATA)
o_data = read_csv(ORDER_DATA)
o_i_data = read_csv(ORDER_ITEMS_DATA)

suspects = filter_birthdate(people_data)
n_suspects = find_orders(o_data, suspects, o_i_data)
print(n_suspects)

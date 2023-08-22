from day1 import read_csv

CUSTOMER_DATA = "./noahs-csv/noahs-customers.csv"
ORDER_DATA = "./noahs-csv/noahs-orders.csv"
ORDER_ITEMS_DATA = "./noahs-csv/noahs-orders_items.csv"
COFFEE_ID = '"DLI1464","Coffee, Drip",6.21'


def find_J_D_names(data: list) -> list:
    suspect = []
    for person in data:
        name = person["name"].split(' ')
        if name[0][0] == 'J' and name[1][0] == 'D':
            suspect.append(person)
    return suspect


def find_orders(o_data: list, suspects: list, o_i_data: list):
    narrowed_suspects = []
    for person in suspects:
        for row in o_data:
            if person["customerid"] == row["customerid"]:
                order_id = row["orderid"]
                break
        for row in o_i_data:
            if row["orderid"] == order_id:
                if row["sku"] == "DLI1464":
                    narrowed_suspects.append(person)
    return narrowed_suspects

c_data = read_csv(CUSTOMER_DATA)
o_data = read_csv(ORDER_DATA)
o_i_data = read_csv(ORDER_ITEMS_DATA)
suspects = find_J_D_names(c_data)
n_suspects = find_orders(o_data, suspects, o_i_data)
print(n_suspects)

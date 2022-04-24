import json


def write_order_json(item, quantity, price, buyer, date):
    orders_data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json', 'r', encoding='utf-8') as f_out:
        objs = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as f_in:
        order_list = objs['orders']
        order_list.append(orders_data)
        json.dump(orders_data, f_in, indent=4, ensure_ascii=False)


write_order_json('computer', '1', '1000 rub', 'user', '21.04.2022')
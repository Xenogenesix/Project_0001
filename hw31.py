
import requests
URL = "https://dummyjson.com/carts"
params = {
    "limit": 5000,
    "skip": 0
}
response = requests.get(url=URL, params=params)
carts = response.json()["carts"]

#отримати вартість всіх замовлень користувачів з id <= 25

total_price_of_all_orders_of_users_with_id_l_or_e_25 = 0

for cart in carts:

    print(cart.keys())
    print(cart["userId"])
    print(cart["total"])
    if cart["userId"] <= 25:
        total_price_of_all_orders_of_users_with_id_l_or_e_25 += cart["total"]

print(f"Price:", {total_price_of_all_orders_of_users_with_id_l_or_e_25})
print("@Bubbly cat.")

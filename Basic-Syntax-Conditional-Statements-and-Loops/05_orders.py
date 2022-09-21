number_of_orders = int(input())
total_cost = 0

for order in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100 or days < 1 or days > 31 or capsules_needed_per_day < 1 \
            or capsules_needed_per_day > 2000:
        continue
    order_value = (capsules_needed_per_day * days) * capsule_price
    total_cost += order_value
    print(f"The price for the coffee is: ${order_value:.2f}")
print(f"Total: ${total_cost:.2f}")
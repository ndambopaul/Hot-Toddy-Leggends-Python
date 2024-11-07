# Calculate the area of a circle

def calculate_circle_area(radius, pie):
    return pie * (radius * radius)


pie = 3.14
radius = 10
area = calculate_circle_area(radius, pie)
print(area)


# Placing an order
def calculate_order_total(quantity, price):
    total = quantity * price
    return total

order_1 = calculate_order_total(5, 10)
print(order_1)

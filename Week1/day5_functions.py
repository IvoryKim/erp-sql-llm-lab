def greet(name):
    print(f"{name}님, 안녕하세요!")

greet("김철수")
greet("이영희")

def calculate_total(price, qty, discount):
    total = price * qty
    total = total * (1 - discount)
    return total
#    print (total)

result = calculate_total(1200, 5, 0.1)
print(result)

def check_stock(stock):
    if stock == 0:
        return "품절"
    elif stock < 10:
        return "재고 부족"
    else:
        return "재고 충분"

products = [
    {"name": "노트북", "stock": 15},
    {"name": "마우스", "stock": 3}
]

for p in products:
    status = check_stock(p["stock"])
    print(p["name"], status)
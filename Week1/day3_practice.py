product1 = {"name" : "노트북", "price" : 1200000, "stock" : 5}
product2 = {"name" : "마우스", "price" : 100000, "stock" : 50}
product3 = {"name" : "키보드", "price" : 80000, "stock" : 30}

product = [product1, product2, product3]

total = 0

for p in product:
    total += p["price"]
    print(p["name"], ":", p["price"], "원")


print(total)

for p in product:
    if p["stock"] < 10:
        print(p["name"])








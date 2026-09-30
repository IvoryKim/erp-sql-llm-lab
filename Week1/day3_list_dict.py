# 리스트: 순서가 있는 여러 값의 묶음
fruits = ["사과", "바나나", "딸기"]
print(fruits[0])
print(fruits[-1])

fruits.append("포도")
print(fruits)

for fruit in fruits:
    print(fruit)

# 딕셔너리: 키-값 쌍으로 값을 저장
product = {"name": "노트북", "price": 1200000, "stock": 5}
print(product["name"])
print(product["price"])

product["stock"] = 14
print(product)

for key, value in product.items():
    print(key, ":", value)

print(fruits[1])
product["category"] = "전자기기"

print(product)

products = [product, {"name":"마우스", "price":30000, "stock":100}]

for p in products:
    print(p["name"])
product1 = {"name" : "노트북", "price" : 1200000}
product2 = {"name" : "마우스", "price" : 100000}
product3 = {"name" : "키보드", "price" : 80000}
product4 = {"name" : "모니터", "price" : 3000000}
product5 = {"name" : "스피커", "price" : 1500000}

products = [product1, product2, product3, product4, product5]

for p in products:
    if p["price"] > 1000000:
        print(p["name"], "- 고가")
    else:
        print(p["name"], "- 저가")

# 1부터 10까지의 수 중에서 짝수만 출력하는 반복문을 작성해보세요.
i = 1

while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# 리스트에서 가장 고가의 제품을 출력하세요.
ExpItem = "고가제품"
ExpPrice = 0

for p in products:
    if p["price"] > ExpPrice:
        ExpItem = p["name"]

print(ExpItem)
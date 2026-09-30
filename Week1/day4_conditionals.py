# 조건문: if / elif / else
stock = 8

if stock == 0:
    print("품절")
elif stock < 10:
    print("재고 부족")
else:
    print("재고 충분")

# 여러 조건 묶기: and, or
price = 1200000
category = "전자기기"

if price >= 1000000 and category == "전자기기":
    print("고가 전자제품")

# 반복문 : while
"""
count = 3
while count > 0:
    print(count)
    count = count - 1
print("발사!")
"""
count = 5
while count > 0:
    count -= 1
    print(5-count)


# 반복문 안에서 조건문 함께 쓰기
products = [
    {"name" : "노트북", "stock" : 15},
    {"name" : "마우스", "stock" : 3},
    {"name" : "키보드", "stock" : 0}
]

for p in products:
    if p["stock"] == 0:
        print(p["name"], "- 품절")
    elif p["stock"] < 10:
        print(p["name"], "- 재고 부족")
    else:
        print(p["name"], "- 재고 충분")

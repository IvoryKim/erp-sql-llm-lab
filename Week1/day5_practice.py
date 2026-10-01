
#1. is_expensive(price)라는 함수를 만드세요. 가격이 100만 원 이상이면 True, 아니면 False를 return하세요.
def is_expensive(price):
    if price >= 1000000:
        return "true"
    else:
        return "false"

#2. 제품 리스트(딕셔너리들)를 만들고, 반복문 안에서 is_expensive를 호출해서 결과에 따라 다른 메시지를 출력하세요.
products = [
    {"name": "노트북", "price": 1700000},
    {"name": "마우스", "price": 100000},
    {"name": "키보드", "price": 80000},
    {"name": "모니터", "price": 1200000}
]

for p in products:
    result = is_expensive(p["price"])
    print(p["name"], ":", result)


#3. average(numbers)라는 함수를 만드세요. 
# 숫자로 된 리스트를 받아서 평균을 return하세요. 
# (힌트: 합계는 sum(리스트), 개수는 len(리스트)로 구할 수 있어요. 둘 다 Python에 이미 있는 함수예요.)

def average(numbers):
    avg = sum(numbers)/len(numbers)
    return avg

#4. 3번 함수를 이용해서, 제품들의 price 평균을 구해 출력하세요.

#print(average([p["price"] for p in products]))

price = []

for p in products:
    price.append(p["price"])

print(average(price))
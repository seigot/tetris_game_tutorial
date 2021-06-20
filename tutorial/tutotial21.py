# FizzBuzz
# このコードの出典は以下です
# https://qiita.com/Sekky0905/items/7e2b13f2a001384c7fc4

print("FizzBuzz")

for i in range(1, 101):
    if i % 15 == 0:
        print("Fizz Buzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)

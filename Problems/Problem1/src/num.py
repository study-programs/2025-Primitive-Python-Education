import random

target_number = random.randint(1, 100)

attempts = 0

print("1부터 100 사이의 숫자를 맞혀보세요!")

while True:
    try:
        guess = int(input("숫자를 입력하세요: "))
        attempts += 1

        if guess < target_number:
            print("더 큰 수를 입력하세요.")
            print()
        elif guess > target_number:
            print("더 작은 수를 입력하세요.")
            print()
        else:
            print(f"정답입니다! {attempts}번 만에 맞히셨습니다.")
            break
    except ValueError:
        print("유효한 숫자를 입력하세요.")

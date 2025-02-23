n = int(input("숫자를 입력하세요: "))

match n:
    case 1:
        print("Case 1")
    case 2:
        print("Case 2")
    case _:
        print("Case Deafult")
from functions import BankingSystem, Transaction

def main():
    bank = Transaction()
    bank.open_file()

    while True:
        print("1. 계좌 생성, 2. 입금, 3. 출금, 4. 송금, 5. 잔액 조회, 6. 종료")
        choice = int(input("작업을 선택해주세요: "))

        if choice == 1:
            name = input("이름을 입력하세요: ")
            bank.create_account(name)

        elif choice == 2:
            account_number = input("계좌번호를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            amount = int(input("입금할 금액을 입력하세요: "))
            bank.deposit(account_number, password, amount)

        elif choice == 3:
            account_number = input("계좌번호를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            amount = int(input("출금할 금액을 입력하세요: "))
            bank.withdraw(account_number, password, amount)

        elif choice == 4:
            from_account = input("송금할 계좌번호를 입력하세요: ")
            from_password = input("송금할 계좌의 비밀번호를 입력하세요: ")
            to_account = input("받을 계좌번호를 입력하세요: ")
            amount = int(input("송금할 금액을 입력하세요: "))
            bank.transfer(from_account, from_password, to_account, amount)

        elif choice == 5:
            account_number = input("계좌번호를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            bank.check_balance(account_number, password)

        elif choice == 6:
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
import random
from file import FileHandler

class BankingSystem(FileHandler):
    def __init__(self):
        super().__init__()

    def create_account(self, name):
        while True:
            password = input("비밀번호를 4자리 숫자로 입력하세요: ")
            if not password.isdigit() or len(password) != 4:
                print("비밀번호는 4자리 숫자여야 합니다.")
            else:
                break

        account_number = "-".join(["".join(str(random.randint(0, 9)) for _ in range(4)) for _ in range(3)])

        if account_number in self.data:
            print("계좌 생성 실패: 다시 시도하세요.")
            return

        self.data[account_number] = {"name": name, "balance": 0, "password": password}
        self.save_file()
        print(f"계좌가 생성되었습니다. 계좌번호: {account_number}, 사용자: {name}")

    def authenticate(self, account_number, password):
        if account_number in self.data and self.data[account_number]["password"] == password:
            return True
        print("계좌번호 또는 비밀번호가 일치하지 않습니다.")
        return False

class Transaction(BankingSystem):
    def __init__(self):
        super().__init__()

    def deposit(self, account_number, password, amount):
        if not self.authenticate(account_number, password):
            return
        if amount <= 0:
            print("입금 금액은 0보다 커야 합니다.")
            return
        self.data[account_number]["balance"] += amount
        self.save_file()
        print(f"{account_number} 계좌에 {amount}원이 입금되었습니다.")

    def withdraw(self, account_number, password, amount):
        if not self.authenticate(account_number, password):
            return
        if amount <= 0:
            print("출금 금액은 0보다 커야 합니다.")
            return
        if self.data[account_number]["balance"] < amount:
            print("잔액이 부족합니다.")
            return
        self.data[account_number]["balance"] -= amount
        self.save_file()
        print(f"{account_number} 계좌에서 {amount}원이 출금되었습니다.")

    def transfer(self, from_account, from_password, to_account, amount):
        if not self.authenticate(from_account, from_password):
            return
        if amount <= 0:
            print("송금 금액은 0보다 커야 합니다.")
            return
        if self.data[from_account]["balance"] < amount:
            print("잔액이 부족합니다.")
            return
        if to_account not in self.data:
            print("받는 계좌가 존재하지 않습니다.")
            return

        self.data[from_account]["balance"] -= amount
        self.data[to_account]["balance"] += amount
        self.save_file()
        print(f"{from_account} 계좌에서 {amount}원이 송금되었습니다.")

    def check_balance(self, account_number, password):
        if not self.authenticate(account_number, password):
            return
        balance = self.data[account_number]["balance"]
        print(f"{account_number} 계좌의 잔액은 {balance}원입니다.")

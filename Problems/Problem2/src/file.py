import json
import os

class FileHandler:
    def __init__(self, file_path="users.txt"):
        self.file_path = file_path
        self.data = {}
        self.open_file()

    def open_file(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    account_data = json.load(f)
                    self.data = {
                        user["Account_Number"]: {
                            "name": user["name"],
                            "balance": user["Balance"],
                            "password": user["Password"],
                        }
                        for user in account_data
                    }
                    print("파일 열기 성공")
            except Exception as e:
                print(f"파일 열기 실패: {e}")

    def save_file(self):
        try:
            account_data = [
                {
                    "name": user["name"],
                    "Account_Number": account,
                    "Password": user["password"],
                    "Balance": user["balance"],
                }
                for account, user in self.data.items()
            ]
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(account_data, f, indent=4, ensure_ascii=False)
            print("데이터 저장 성공")
        except Exception as e:
            print(f"데이터 저장 실패: {e}")

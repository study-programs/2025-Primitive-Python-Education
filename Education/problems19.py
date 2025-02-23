class Example:
    def __init__(self, value):
        self.value = value

    def modify_value(self, new_value):
        self.value = new_value

obj = Example(10)
print(obj.value)

obj.modify_value(20)
print(obj.value)
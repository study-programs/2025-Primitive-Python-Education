def outer_function():
    y = 5

    def inner_function():
        nonlocal y
        y = 10

    inner_function()
    print(y)

outer_function()
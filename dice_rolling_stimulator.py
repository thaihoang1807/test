import random
while True:
    no = random.randint(1, 6)
    if no == 1:
        # In biểu diễn xúc xắc
        print("[-----]")
        print("[    ]")
        print("[  0  ]")
        print("[    ]")
        print("[-----]")
    elif no == 2:
        # In biểu diễn xúc xắc
        print("[-----]")
        print("[ 0   ]")
        print("[    ]")
        print("[   0 ]")
        print("[-----]")
    elif no == 3:
        # In biểu diễn xúc xắc
        print("[-----]")
        print("[    ]")
        print("[0 0 0]")
        print("[    ]")
        print("[-----]")
    elif no == 4:
        # In biểu diễn xúc xắc
        print("[-----]")
        print("[0   0]")
        print("[    ]")
        print("[0   0]")
        print("[-----]")
    elif no == 5:
        # In biểu diễn xúc xắc
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif no == 6:
        # In biểu diễn xúc xắc
        print("[-----]")
        print("[0 0 0]")
        print("[    ]")
        print("[0 0 0]")
        print("[-----]")

    # Yêu cầu người dùng nhập liệu
    x = input("Press y to roll again and n to exit: ")
    print("\n")
    # Kiểm tra nếu người dùng không chọn "y" thì thoát khỏi vòng lặp
    if x != "y":
        break

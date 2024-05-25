code = []
combination1 = int(input("Type your 4-digit code "))

code.append(combination1)
print(code)

for d1 in range(10):
    for d2 in range(10):
        for d3 in range(10):
            for d4 in range(10):
                    combination = f"{d1}{d2}{d3}{d4}"
                    if combination == combination1:
                        print("Its unlocked")



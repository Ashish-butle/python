# For Loop
"""
Planet = "Pluto"
for i in Planet:
    print("value of i is now", i)

print("Rest of the code")

# For loop for tuple

VACCINES = ("A", "B", "C", "D", "E")
for VAC in VACCINES:
    print(f"{VAC} it is available")


# For loop for List

VACCINES = ["A", "B", "C", "D", "E"]
for VAC in VACCINES:
    print(f"{VAC} it is available")

# While Loop

X = 0
while X <= 10:
    print("value of x is:", X)
    print("Loping")
    X+=1
print("Rest of the code:")


VACCINES = ["ABC", "BGX", "CAD", "DXCV", "ENM"]
for VAC in VACCINES:
    print("")
    print(f"I would like to print one by one charercter here it is {VAC} ")
    for i in VAC:
        print(i)
"""
import time
X = 2
while True:
    print("value of X is ", X)
    print("Loping")
    X*=5
    time.sleep(1)

"""
def add (arg1, arg2):
    Total = arg1 + arg2
    print(Total)
add (10, 20)
print(add(2,2))



def sum(arg):
    x = 0
    for i in arg:
        x = x + i
    return x
out = sum([10,20,30])
print(out)


def greetings(MESG="Morning"):
    print(f"good {MESG}")
greetings()
greetings("Evening")

# variable Lenght Arguments (Non keywords Arguments)
def order_food(Min_order, *args):
    print(f"You have ordered {Min_order}")
    for item in args:
        print(f"You have ordered {item}")
    print("it will take 30 mints to reach there")
order_food("salad", "poli")

"""

import random
# variable Lenght Arguments **kwargs (keywords Arguments)
def time_activity (*args, **Kwargs):
    #print(args)
    #print(Kwargs)
    min = sum(args) + random.randint(0,20)
    #print(min)
    choice = random.choice(list(Kwargs.keys()))
   # print(choice)
    print(f"you have spend {min} Minutes for {Kwargs[choice]}")
time_activity(10,20,30, hobby="Build home labs", Sport="Gym", Fun="Driving")

"""
# Break Statement
#i = "DevOps"
for i in "DevOps":
    print(i)
    if i == "O":
        print("Found My data")
        break
       
print("out of look")

# Continue Statement "It Skip the Match"
for i in "Ashish":
    if i == "i":
        print("Found my data")
        continue
    print(f"value of i is {i}")
print("Out of loop")

import random
DevOps = ["Linux", "vagrant", "Bash", "AWS", "jenkins", "python", "Ansible"]

random.shuffle(DevOps)
print(DevOps)

Skill = random.choice(DevOps)
print(Skill)

for test in DevOps:
    print(f"***Skill is Testing {test}")
    if test ==  Skill:
        print(f"{test} Skill is found")
        continue
    print("Test failed")

"""  
import random
DevOps = ["Linux", "vagrant", "Bash", "AWS", "jenkins", "python", "Ansible"]

random.shuffle(DevOps)
print(DevOps)

Skill = random.choice(DevOps)
print(Skill)

for test in DevOps:
    print(f"***Skill is Testing {test}")
    if test ==  Skill:
        print(f"{test} Skill is found")
        break
    print("Test failed")


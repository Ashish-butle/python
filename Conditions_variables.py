"""
This Script will implement our knowledge on conditions and diffrent datatypes
"""
print("This org has various skill sets")
print("Find your match")

DevOps = ["Linux", "vagrant", "Bash", "AWS", "jenkins", "python", "Ansible"]
Developement = ("Java", "Ruby", "Pearl", ("C"), ("C++"))
Contarct_Emp1 = {"Name": "Ashish", "Skill": "AI","code":1337}
Contarct_Emp2 = {"Name": "Satish", "Skill": "IOT","code":1338}

user_skill = input("Please Enter your skills: ")
# Chekc in the database if we have this skill

if user_skill in DevOps:
    print(f"We have {user_skill} in DevOps team")
elif user_skill in Developement:
    print(f"We have {user_skill} in Developement team")
elif user_skill in Contarct_Emp1.values() or user_skill in Contarct_Emp2.values():
    print(f"we have {user_skill} in contarct emp")
else:
    print("Your skill does not matched")

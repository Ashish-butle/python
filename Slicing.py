# Slicing
Name = "Ashish is the DevOps Eng"

# Printing the Slicing
print(Name[1])
print(Name[2])
print(Name[5])
print(Name[2])
print(Name[7])
print(Name[8])

print(Name[-1])
print(Name[-2])
print(Name[-5])
print(Name[-2])

# Slicing a string, get a substring from a string
print(Name[1:4])
print(Name[:])
print(Name[:6])

# Slicing a touple
DevOps = ("Linux", "vagrant", "Bash", "AWS", "jenkins", "python", "Ansible")
print("")
print(DevOps[0])
print(DevOps[3])
print(DevOps[5])
print(DevOps[1])
print()
print(DevOps[-0])
print(DevOps[-2])
print()
print(DevOps[-1])
print()
print(DevOps[0:3][0][4])

# Slicing a List
DevOps = ["Linux", "vagrant", "Bash", "AWS", "jenkins", "python", "Ansible"]
print("")
print(DevOps[0])
print(DevOps[3])
print(DevOps[5])
print(DevOps[1])
print()
print(DevOps[-0])
print(DevOps[-2])
print()
print(DevOps[-1])
print()
print(DevOps[0:3][0][4])

# Slicing a Dictionary
Skills = {"DevOps": ("AWS", "jenkins", "python"), "Developement": ["java", "Nodejs", "Python"]}
print()
print(Skills)
print()
print(Skills["DevOps"])
print()
print(Skills["DevOps"][-1][4:6])

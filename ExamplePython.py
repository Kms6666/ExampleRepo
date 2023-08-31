a = "string 1"
b = "string 2"
print("a = " + a + " and b = " + b)
#how we learned

x = "string 3"
y = "string 4"
print(f"x = {x} and y = {y}")
#Using F-string

#also possible
print("c = {c} and d = {d}".format(c=1, d=2))

job_list = {'John': 'Doctor', 'Jane': 'Engineer', 'Jim': 'Teacher'}

for name, job in job_list.items():
    print(f"{name} is a {job}")


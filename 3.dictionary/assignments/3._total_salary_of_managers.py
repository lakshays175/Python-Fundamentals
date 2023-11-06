import nested_dictt 

json_dict = nested_dictt.json_dict

# Integers used to calculate the sum of salaries of all the managers
sum=0 

for manager in json_dict.get("Employees")[0].get("Managers"): 
    for classes,values in manager.items():
        if classes == "L1":
            for salaries in values[:]: 
                for names,salary in salaries.items(): 
                    if names == "Salary": 
                        sum += salary
        if classes in("L2","L3"): 
            for name,salary in values.items(): 
                if name == "Salary":
                    sum += salary

print(f"Total Salary of L1, L2 and L3 Managers are : {sum}")



        
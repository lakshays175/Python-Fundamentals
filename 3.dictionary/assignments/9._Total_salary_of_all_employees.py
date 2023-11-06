import nested_dictt 

json_dict = nested_dictt.json_dict

#print(json_dict.get("Employees")[0].get("Developers")[0].get("FrontEnd"))
# Integers used to calculate the sum of salaries of all the managers
sum=0

for manager in json_dict.get("Employees")[0].get("Managers"): 
    for classes,values in manager.items():
        if classes == "L1":
            for salaries in values: 
                for names,salary in salaries.items(): 
                    if names == "Salary": 
                        sum += salary
        if classes in("L2","L3"): 
            for name,salary in values.items(): 
                if name == "Salary":
                    sum += salary

for developer in json_dict.get("Employees")[0].get("Developers"): 
    for values in developer.values():
        for salaries in values:
            for keys,values in salaries.items(): 
                if keys == "Salary":
                    sum += values


print(f"Total Salary of Employees are : {sum}")


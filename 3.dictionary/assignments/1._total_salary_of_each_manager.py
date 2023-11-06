import nested_dictt 

json_dict = nested_dictt.json_dict

# Integers used to calculate the sum of salaries of all the managers
l1_manager_sum,l2_manager_sum,l3_manager_sum = (0,0,0) 

for manager in json_dict.get("Employees")[0].get("Managers"): 
    for classes,values in manager.items():
        if classes == "L1":
            for salaries in values[:]: 
                for names,salary in salaries.items(): 
                    if names == "Salary": 
                        l1_manager_sum += salary
        if classes in("L2"): 
            for name,salary in values.items(): 
                if name == "Salary":
                    l2_manager_sum += salary
        if classes in("L3"): 
            for name,salary in values.items(): 
                if name == "Salary":
                    l3_manager_sum += salary

print(f"L1 Manager salary is : {l1_manager_sum}")
print(f"L2 Manager salary is : {l2_manager_sum}")
print(f"L3 Manager salary is : {l3_manager_sum}")



        
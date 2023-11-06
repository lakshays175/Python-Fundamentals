import nested_dictt 

json_dict = nested_dictt.json_dict

#print(json_dict.get("Employees")[0].get("Developers")[0].get("FrontEnd"))
# Integers used to calculate the sum of salaries of all the managers
sum=0 

for developer in json_dict.get("Employees")[0].get("Developers")[0].get("FrontEnd"): 
    for keys,values in developer.items():
        if keys == "Salary": 
            sum+= values

print(f"Total Salary of Frontend Developers are : {sum}")



        
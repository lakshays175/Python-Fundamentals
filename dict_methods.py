demo = { 'india' : 'new delhi', 'france' : 'paris', 'uk' : 'london' }

# 1. to get all keys from dict

print(demo.keys())

print(type(demo.keys()))

for item in demo.keys():
    print(item.upper())

# 2. to get all values from dict
print(demo.values())

for item in demo.values():
    print(item.upper())

# 3. To get all items from dict

print(demo.items())

for key, value in demo.items():
    print(key,value)

## to remove item from dict :
# 1. pop

demo_1 = { 'india' : 'new delhi', 'france' : 'paris', 'uk' : 'london' }

demo_1.pop('france')

print(demo_1)

demo_1.popitem()
demo_1.popitem()
print(demo_1)

## 5. To clear the dict
demo_1.clear()
print(demo_1)

# 6. Copy : to copy all elment from one to another

demo_2 = demo_1.copy()
print(demo_2)


## Updating a dict

demo = { 'india' : 'new delhi', 'france' : 'paris', 'uk' : 'london' }
demo_1 = { 'india' : 'New Delhi', 'netherlands' : 'amsterdam' }

demo.update(demo_1)

print(demo)

# ## 
demo_dict = {
    "data" : [
        { "key1" : "val1"},
        { "key2" : "val2" },
        {"key3" : "val3"}
    ]
}

print(demo_dict)
demo_all = {}
for item in demo_dict.get("data"):
    print(item)
    demo_all.update(item)

print(demo_all)

## 7. get method

demo = { 'india' : 'new delhi', 'france' : 'paris', 'uk' : 'london' }
#print(demo['india2'])
print(demo.get('indiagdhh','demo'))

#demo.setdefault('inida123',_value: 'demo')

demo_list = [ 'ram' , 'krishna']

new_dict = dict.fromkeys(demo_list)
print(new_dict)

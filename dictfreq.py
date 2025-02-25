data={3:1,2:6,4:3,5:6,7:9,2:4,3:6}
count={}
for value in data.values():
    count[value]=count.get(value,0)+1
for key,value in count.items():
    print(f"Value{key}:{value}times")
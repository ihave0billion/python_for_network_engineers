devices = ["router1","router2","router3"]

#append adds object to end of list
devices.append("switch1")
print(devices)

#insert adds object to specific index location in list
#Index from left to right: 0,1,2...
#Index from right to left: -1, -2, -3... 
# -1 is always the last item in the list

devices.insert(3,"router4")
print(devices)

#remote last object added to list
devices.pop()
print(devices.pop())
print(devices)

test_devices = ["r1", "r2","r3","r4","sw1"]
print(test_devices)
test_devices.pop()
print(test_devices)

#remote object from a specific index location in a list
print(devices)
devices.pop(2)
print(devices)

#remote an element from a list
devices.remove("router1")
print(devices)

#count number of times object appears in list
print(test_devices.count("r1"))

#count total number of objects in list
print(len(test_devices))

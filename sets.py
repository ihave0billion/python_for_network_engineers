# Sets
# uses curly brackets {} , are unordered and NOT indexed and has no duplicates . they are mutable
# sets are commonly used to remove duplicates

# Example 1
os_type = {'IOS','IOS-XE','IOS-XR', 'NX-OS'}
print(os_type) 

# Example 2 - remove duplicate from list
hostnames = set(['R1', 'R2', 'R3', 'R4'])
print(hostnames)

Router_1 = {'R1', 'IOS-XE'}
Router_2 = {'R2', 'IOS-XE'}

# Union - combine two sets with no duplicates
Router_1.union(Router_2)
print(Router_1.union(Router_2))

# Intersection - remove duplicate between two sets
Router_1.intersection(Router_2)
print(Router_1.intersection(Router_2))



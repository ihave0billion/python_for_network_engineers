os_type = ("IOS","IOS-XE", "IOS-XR", "NX-OS")

#tuples are indexed the same as lists. from left to right 0, 1, 2.. from right to left -1, -2..

#tuples are IMMUTABLE
print(os_type[2])
print(os_type[-4])

print(os_type.count("IOS"))
print(os_type.index("IOS-XR"))
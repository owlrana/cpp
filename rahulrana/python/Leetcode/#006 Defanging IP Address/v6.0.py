# Defanging and IP Address
# Turning "." into a "[.]"
# https://leetcode.com/problems/defanging-an-ip-address/

def defangIPaddr(address):
    add_list = address.split(".")
    print(add_list)
    defanged = ""
    for i in range(len(add_list)):
        defanged += add_list[i]
        if i != len(add_list) -1:
            defanged += "[.]"
    return print(defanged)

defangIPaddr("192.168.0.1")

# 28 ms; faster than 68%
# 14.3MB; less than 20%
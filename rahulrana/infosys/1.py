input_list=[4,3,1,4,5]
val = 0
while(len(input_list)!=1):
    input_list.pop(1)
    input_list.remove(input_list[0])
    input_list.append(val+1)
    val+=1
print(input_list)
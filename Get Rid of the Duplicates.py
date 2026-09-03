dictionary={1:2,2:5,3:3,4:2}
print("ORIGINAL DICTIONARY: ",dictionary)
K=2
count=0
for key in dictionary:
    if dictionary[key]==K:
        count=count+1
print("AMOUNT OF 2s IN DICTIONARY: ",count)
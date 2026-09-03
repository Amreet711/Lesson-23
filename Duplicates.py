class1={"id1":{"Name":"Kailah","Class":"5/6C","Subject":"English"},"id2":{"Name":"Lucy","Class":"5/6B","Subject":"Maths"},"id3":{"Name":"Airlie","Class":"5/6A","Subject":"Math"},"id4":{"Name":"Kailah","Class":"5/6C","Subject":"English"}}
result={}
seen_keys=[]
for  class1,details in class1.items():
    unique_key=details["Name"],details["Class"],details["Subject"]
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[class1]=details
for k,v in result.items():
    print(k,":",v)
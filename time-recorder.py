from datetime import datetime

now = datetime.now()
now_str = now.strftime("%d/%m/%y %H:%M:%S")
print("date and time : ",now_str)

with open('D:/my-documents/code/python/time-recorder/text-store.txt',"a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(now_str)
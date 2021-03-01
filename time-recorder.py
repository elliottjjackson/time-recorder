from datetime import datetime
import platform

now = datetime.now()
now_str = now.strftime("%d/%m/%y %H:%M:%S")
print("date and time : ",now_str)
osName = platform.system()

if osName == "Linux":
    dirFolder = '/home/pi/code/time-recorder/text-store.txt'
else:
    dirFolder = 'D:/my-documents/code/python/time-recorder/text-store.txt'

with open(dirFolder,"a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(now_str)
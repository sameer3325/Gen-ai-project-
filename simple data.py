import datetime

file = open("kitchen_log.txt","a")

file.write("Kitchen checked at : ")
file.write(str(datetime.datetime.now()))
file.write("\n")

file.close()
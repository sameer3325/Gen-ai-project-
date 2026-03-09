import time

seconds = int(input("Enter cooking time (seconds): "))

for i in range(seconds,0,-1):
    print(i)
    time.sleep(1)

print("Food Ready!")
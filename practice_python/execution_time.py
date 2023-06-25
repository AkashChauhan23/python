import time

print("Enter number amd if you want to see time execution time please provide the number in lakhs : " )
number = int(input())

start_time = time.time()
countdown = 3

while(countdown>0):
    print(f"tick tick {countdown}")
    countdown-=1
    if countdown >0: time.sleep(1) 
    else: pass

# time start
start_time = time.time()
sum = 0
for i in range(1,number):
    sum = sum + i
    i+=1

print(f"Sum is : {sum}")

end_time = time.time()
execution_time = end_time-start_time

print(f"Execution time : {execution_time}")





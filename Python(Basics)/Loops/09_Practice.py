# Double the wait time for user at each attempts max attempt are 5 
import time
wait_time = 1
max_attempt = 5
attempt = 1
while(attempt <= max_attempt):
    print("Attempt number is ",attempt,"waiting Time ",wait_time,"s")
    time.sleep(wait_time)
    attempt +=1
    wait_time *=2
from time import sleep

#variables for work
sec = minute = hour = 0

#main loop for stopwatch
while True:
    sleep(1)
    sec += 1
    #zjsitime zda ubehlo 60 sekund
    if sec / 60 >= 1:
        minute += 1
        sec -= 60
        #zjistime zda ubehlo 60 minut
        if minute / 60 >=1:
            hour += 1
            minute -= 60
            #todo
    
    print('Time: {} hodin, {} minut, {} sekund'.format(hour, minute, sec))

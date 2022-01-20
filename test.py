import time
def countdown(t):
    while t:
        # This showing the time in seconds
        # if t >=60 and t< 120 then time 1:x
        mins, secs = divmod(t,60)

        hour, secs = divmod(t,60)
        hour = 60*mins
        hour = t//3600
        # second I've to format the mins, secs time format
        # 2d means formats to 2 characters using padding
        timer = f"{hour}:{mins}:{secs:2d}"
        # above line could be: '{:02d}:{:02d}'.format(mins, secs)
        # \r: To make next time into beginning of the current line
        print(timer,end = "\r")
        # Program wait for 1 second
        time.sleep(1)
        t-=1
        
    print("timer completed!")
    
t = input("Enter the time in seconds:")
countdown(int(t))
        
        

           
                
                
                
                
    
    
    
    
    
    
    
    
        
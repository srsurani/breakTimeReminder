import time
import webbrowser

total_break = 3
break_count = 0

print "Program has started on " + time.ctime()

while break_count < total_break:
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=scUSg51jWHI")
    break_count = break_count+1

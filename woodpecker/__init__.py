#main init
#Writed By Silver Spider
#Follow Me => twitter(x): silverspider_x
#Follow Me => github: @silverspiderofficial
# 100% Human Coded
######################################################
import time
start_time = time.time()
########
from terminalfolder import terminal

#terminal start
terminal.asci()



########
end_time = time.time()
execution_time = end_time - start_time
etime=str(round(execution_time,5))
terminal.printbossmessage(">>>Modules Import Time: "+etime+" Seconds")
terminal.interactive_terminal()


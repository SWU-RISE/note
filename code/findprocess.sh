
ps -fe | grep filename # first way
fuser filename # second way

# find the relaste socket port for the file
ps -ef | grep ID # find the relaste socket port for the file
lsof -p ID # find the files which opened by process ID
lcat /proc/ID/maps # find process ID's  memory allow 
pstack 11 ID  # find proccess ID's stack
strace -p ID # find which process invoke this process ID
ltrace -p ID # find the call lib of proccess ID

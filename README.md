This a a test app written in python command line to return current
system memory profile.
Main libraries used in this implementation are  matplotlib ,memory_profiler,psutil.

MatplotLib: This library used to plot the memusage of specified ProcessId over 1 second timeout.

psutil : This library used to get the System Information
CPU Information,
Memory Usage,
Disk Usage,
Network Information,
GPU Information 

memory_profiler : This package is used to get  Profile Memory Usage Of Specific Process (Process ID) for Specified Time Interval.
Here we are using the API mem_usage which accept process id as argument and out put the specified time interval memory usage of that particular process

$ mem_usage = memory_usage(-1, interval=.2, timeout=1)

-1 used for current Process
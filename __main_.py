import  src.memoryUsage as src
import psutil

print("Enter the input [1,2,3,4,q]")
user_input=1,
while user_input!='q':
    print("1.SystemInfo \n 2.NetworkInfo\n 3.ListofProcess\n 4.StatisticsByPid")
    user_input = input('>')

    if user_input =='1':
        src.getSystemInfo()
        src.getSystemDiskusage()
        src.getSystemMemDetails()

    elif user_input =='2':
        src.getNetworkInfo()
    elif user_input =='3':
        src.getListOfPidsAndInfo()
    elif user_input =='4':
        print("Please enter the PID from the below list to see more process details  ")
        print(psutil.pids())

        pid_input = int(input(">>"))
        src.statiticsofProcess(pid_input)
    else:
        if user_input =='q':
            print("Existing the App!!!")
            break

        else:

            print("Please Enter Valid Input!!![1,2,3,4,q]")



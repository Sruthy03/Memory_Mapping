import psutil
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import platform
import numpy as np


def getSystemInfo():
    print("=" * 40, "System Information", "=" * 40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")



def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def getNetworkInfo():
    # Network information
    print("=" * 40, "Network Information", "=" * 40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")


#System memory  Details

def getSystemMemDetails():

    print("=" * 40, "System Memeory Usage", "=" * 40)
    mem_usage = psutil.virtual_memory()

    print(f"Free: {mem_usage.percent}%")
    print(f"Total: {mem_usage.total / (1024 ** 3):.2f}G")
    print(f"Used: {mem_usage.used / (1024 ** 3):.2f}G \n")

def getSystemDiskusage():
    print("=" * 40, " System Disk Usage ", "=" * 40)
    disk_usage = psutil.disk_usage('/')
    print(f"Total: {disk_usage.total / (1024 ** 3):.2f}%")
    print(f"Used: {disk_usage.used / (1024 ** 3):.2f}G")
    print(f"Free: {disk_usage.free / (1024 ** 3):.2f}G")
    print(f"Percentage: {disk_usage.percent}%\n")


 # printing logic for each process Id, name, memoru and CPU Usage
def getListOfPidsAndInfo():
    print("1. List out all PIDs with %MEM and %CPU usage")
    for process in [psutil.Process(pid) for pid in psutil.pids()]:
        try:
            pid = process.pid
            name = process.name()
            mem = process.memory_percent()
            cpu = process.cpu_percent(interval=1)
        except psutil.NoSuchProcess as e:
            print(e.pid, "killed before analysis")
        else:
            print("PID: ",pid)
            print("Name:", name)
            print("CPU%:", cpu)
            print("MEM%:", mem)
            print("--------------------")

# statistics  of Process by ID

def statiticsofProcess(pid_input):
    # print(type(pid_input))
    if pid_input not in psutil.pids():
        print("No process found !!Please enter a valid ID")
    else:
        selected_process = psutil.Process(int(pid_input))

        statistics_dict = selected_process.as_dict(['name', 'status', 'pid', 'ppid', 'cpu_times', 'num_threads', ])
        print("Process Statistic")
        print('%CPU :', selected_process.cpu_percent(interval=1), )
        for key in statistics_dict:
            print(key, ":", statistics_dict[key])
        mem_usage = memory_usage(int(pid_input), interval=.2, timeout=1, backend="psutil")
        print(mem_usage)
        # memory = [pair[0] for pair in mem_usage ]
        # time =  [pair[1] for pair in mem_usage ]
        # print(memory)
        # print(time)
        #
        #
        # xpoints = np.array(time)
        # ypoints = np.array(memory)
        # plt.plot(xpoints,ypoints)
        #
        plt.xlabel("Time(with in 1 second)")
        plt.ylabel("MemUsage")
        plt.plot(mem_usage)
        plt.show()
























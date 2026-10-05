import psutil
import time
import subprocess
import os

def main():
    try:
        while True:
            command = "cls" if os.name == "nt" else "clear"
            subprocess.run(command, shell=True) 
            cpu_data = get_cpu()
            ram_data = get_ram()
            disk_data = get_storage()
            display(cpu_data, ram_data, disk_data)
            time.sleep(1)        
    except KeyboardInterrupt:
        print("\nExiting SysWatch.")
def get_cpu():
    cpu = psutil.cpu_percent(interval=None)
    logi = psutil.cpu_count(logical=True)
    physi = psutil.cpu_count(logical=False)
    return {
        "percent": cpu,
        "logical": logi,
        "physical": physi,
    }
def get_ram():
    mem = psutil.virtual_memory()
    byte_convert(mem.total)
    return {
        "percent": mem.percent,
        "total": byte_convert(mem.total),
    }
def get_storage():
    storage = psutil.disk_usage("C:\\")
    return {
        "percent": storage.percent,
        "total": byte_convert(storage.total),
    }
def display(cpu, ram, disk):
    print("=" * 35)
    print(f"{'SYSTEM MONITOR':^35}")
    print("=" * 35)
    print(f"{'Metric':<20} | {'Value'}")
    print("-" * 35)
    print(f"{'CPU Usage':<20} | {cpu['percent']}%")
    print(f"{'Logical Cores':<20} | {cpu['logical']}")
    print(f"{'Physical Cores':<20} | {cpu['physical']}")
    print(f"{'RAM Usage':<20} | {ram['percent']}%")
    print(f"{'Total RAM':<20} | {ram['total']}GB")
    print(f"{'DISK USAGE':<20} | {disk['percent']}%")
    print(f"{'DISK SPACE':<20} | {disk['total']}GB")
    print("=" * 35)
    print("Press Ctrl+C to exit.")
def byte_convert(bytes_value):
    return  round(bytes_value / 1024 ** 3)
    
if __name__ == "__main__":
    main()
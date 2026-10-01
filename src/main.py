import psutil
#import time
import argparse
#import platform

def main():
    cpu_data =get_cpu()
    ram_data =get_ram()
    display(cpu_data,ram_data)

def get_cpu():
    cpu = psutil.cpu_percent(interval=1)
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
def display(cpu, ram,):
    print(f"CPU: {cpu['percent']}%")
    print(f"LOGICAL CORES: {cpu['logical']}")
    print(f"PHYSICAL CORES: {cpu['physical']}")
    print(f"RAM: {ram['percent']}%")
    print(f"TOTAL RAM: {ram['total']}GB")
def byte_convert(bytes_value):
    return  round(bytes_value / 1024 ** 3)
    
if __name__ == "__main__":
    main()  
import os

#New-VM -Name "Test" -Version 8.1 -MemoryStartupBytes 4GB -Generation 2 -NewVHDPath "Test.vhdx" -NewVHDSizeBytes 80GB

#VM Name
VM_NAME = input("Enter the name of the new virtual machine: ").replace(" ","_")

#VM ver.
while True:
    VM_VERSION = input("Enter the version of the new virtual machine (default 8.1): ")
    if VM_VERSION == "":
        VM_VERSION = "8.1"
        break
    else:
        try:
            float(VM_VERSION)
            break
        except ValueError:
            print("Please enter in this format x.x")

#VM cpu
while True:
    VM_CPU_CORE_NUMBER = input("Enter the number of cores for new virtual machine (default 12): ")
    if VM_CPU_CORE_NUMBER == "":
        VM_CPU_CORE_NUMBER = "12"
        break
    else:
        try:
            int(VM_CPU_CORE_NUMBER)
            break
        except ValueError:
            print("Please enter an integer.")
            
#VM ram
while True:
    VM_MEMORY = input("Enter the amount of memory for the new virtual machine (default 4GB) (No need \"GB\"): ")
    if VM_MEMORY == "":
        VM_MEMORY = "4"
        break
    else:
        try:
            temp = int(VM_MEMORY)
            break
        except ValueError:
            print("Please enter an integer.")

#VM gen
while True:
    VM_GENERATION = input("Enter the generation of the new virtual machine (1 or 2) (default Gen 2): ")
    if VM_GENERATION == "":
        VM_GENERATION = "2"
        break
    elif VM_GENERATION != "1" and VM_GENERATION != "2":
        print("Please enter \"1\" or \"2\" ")
    else:
        break

#VHD size
while True:
    VM_VHD_SIZE = input("Enter the size of the new virtual hard disk (default 80GB) (No need \"GB\"): ")
    if VM_VHD_SIZE == "":
        VM_VHD_SIZE = "80"
        break
    else:
        try:
            int(VM_VHD_SIZE)
            break
        except ValueError:
            print("Please enter an integer.")

#Run area
os.system(f"powershell New-VM -Name \"{VM_NAME}\" -Version {VM_VERSION} -MemoryStartupBytes {VM_MEMORY}GB -Generation {VM_GENERATION} -NewVHDPath \"{VM_NAME}.vhdx\" -NewVHDSizeBytes {VM_VHD_SIZE}GB")
os.system(f"powershell Set-VMProcessor -VMName \"{VM_NAME}\" -Count {VM_CPU_CORE_NUMBER}")
os.system(f"powershell Add-VMDvdDrive -VMName \"{VM_NAME}\" 2>$null") #" 2>$null" is throw to void
if float(VM_VERSION) >= 8.0:
    os.system(f"powershell Set-VMProcessor -VMName \"{VM_NAME}\" -ExposeVirtualizationExtensions $true")

#Finish
input("Done, Press Enter Twice To Exit")

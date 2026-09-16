import os
import time
#-------------------------------------------------------#
vhd_path = "C:\\ProgramData\\Microsoft\\Windows\\Virtual Hard Disks\\"
#-------------------------------------------------------#
def clean_screen(command = "cls"):
    os.system(command)
def delay(secs = 1):
    time.sleep(secs)
#Preset-------------------------------------------------#
vm_name = "Not Configured"
vm_gen = "2"
vm_config_version = "8.1"
vm_cpu = "4"
vm_cpu_enabled_nested = False
vm_ram_unit = "GB"
vm_ram = "8"
vm_storage_unit = "GB"
vm_storage = "128"
vm_storage_logical = "512"
vm_storage_physical = "4096"
#Configured-(Preset-Use)--------------------------------#
vm_name_configured = False
vm_gen_configured = True
vm_config_version_configured = True
vm_cpu_configured = True
vm_cpu_enabled_nested_configured = True
vm_ram_unit_configured = True
vm_ram_configured = True
vm_storage_unit_configured = True
vm_storage_configured = True
#-------------------------------------------------------#
#Name
def get_vm_name():
    global vm_name
    global vm_name_configured
    while True:
        vm_name = input("Name of the virtual machine: ")
        if vm_name == "":
            print("VM must have a name.")
            delay(2)
            clean_screen()
            continue
        else:
            clean_screen()
            vm_name_configured = True
            break
#-------------------------------------------------------#
#VM Generation
def get_vm_gen():
    global vm_gen
    global vm_gen_configured
    while True:
        print("Virtual Machine Generation")
        print("(1)    Generation 1")
        print("(2)    Generation 2")
        vm_gen = input("Virtual machine's Generation: ")
        if vm_gen == "1":
            clean_screen()
            vm_gen_configured = True
            break
        elif vm_gen == "2":
            clean_screen()
            vm_gen_configured = True
            break
        else:
            print("Please insert number to choose between each option.")
            delay(2)
            clean_screen()
            continue
        clean_screen()
#-------------------------------------------------------#
#VM Config Version
def get_vm_config_version():
    global vm_config_version
    global vm_config_version_configured
    while True:
        print("Virtual Machine's configuration versions")
        vm_config_version = input("Version: ")
        try:
            float(vm_config_version)
            clean_screen()
            vm_config_version_configured = True
            break
        except ValueError:
            print("Config Version is like 10.0 11.0, is a float.")
            delay(2)
            clean_screen()
            continue
#-------------------------------------------------------#
#Cpu core(s) amount
def get_vm_cpu():
    global vm_cpu
    global vm_cpu_configured
    while True:
        vm_cpu = input("Virtual Machine's CPU Core Amount (Just Number): ")
        try:
            int(vm_cpu)
            if int(vm_cpu) >= 1:
                clean_screen()
                vm_cpu_configured = True
                break
            else:
                print("Please insert a number > 0.")
                delay(2)
                clean_screen()
                continue
        except ValueError:
            print("Please insert a integer.")
            delay(2)
            clean_screen()
            continue
        clean_screen()
def get_vm_enabled_nested():
    global vm_cpu_enabled_nested
    while True:
        print("Enable Nested Virtualization")
        print("(Y)  Yes")
        print("(N)  No")
        vm_cpu_enabled_nested = input("(Y/N): ").upper()
        if vm_cpu_enabled_nested == "Y":
            vm_cpu_enabled_nested = True
            break
        elif vm_cpu_enabled_nested == "N":
            vm_cpu_enabled_nested = False
            break
        else:
            print("")
            print("Choose with \"Y\" or \"N\"")
            input("Press Enter To Retry")
            clean_screen()
            continue
#-------------------------------------------------------#
#Ram amount
def get_vm_ram_unit():
    global vm_ram_unit
    global vm_ram_unit_configured
    while True:
        print("Ram Unit")
    #    print("(0)    B") #(As extent use)(I don't think powershell support this)
    #    print("(1)    KB")
        print("(2)    MB")
        print("(3)    GB")
        print("(4)    TB")
        vm_ram_unit = input("Virtual Machine's Ram unit (Just Number): ")
    #    if vm_ram_unit == "0":
    #        vm_ram_unit = "B"
    #        vm_ram_unit_configured = True
    #        clean_screen()
    #        break
    #    if vm_ram_unit == "1":
    #        vm_ram_unit = "KB"
    #        vm_ram_unit_configured = True
    #        clean_screen()
    #        break
        if vm_ram_unit == "2":
            vm_ram_unit = "MB"
            clean_screen()
            vm_ram_unit_configured = True
            break
        elif vm_ram_unit == "3":
            vm_ram_unit = "GB"
            clean_screen()
            vm_ram_unit_configured = True
            break
        elif vm_ram_unit == "4":
            vm_ram_unit = "TB"
            clean_screen()
            vm_ram_unit_configured = True
            break
        else:
            print("Please insert number to choose between each option.")
            delay(2)
            clean_screen()
            continue
def get_vm_ram():
    global vm_ram
    global vm_ram_configured
    while True:
        vm_ram = input("Ram for the virtual machine (Just Number): ")
        try:
            int(vm_ram)
            if int(vm_ram) >= 1:
                clean_screen()
                vm_ram_configured = True
                break
            else:
                print("Please insert a number > 0.")
                delay(2)
                clean_screen()
                continue
        except ValueError:
            print("Please insert a integer.")
            delay(2)
            clean_screen()
            continue
        clean_screen()
#-------------------------------------------------------#
#Disk space
def get_vm_storage_unit():
    global vm_storage_unit
    global vm_storage_unit_configured
    while True:
        print("Storage Unit")
    #    print("(0)    B")
    #    print("(1)    KB")
        print("(2)    MB")
        print("(3)    GB")
        print("(4)    TB")
        vm_storage_unit = input("Virtual machine's storage unit (Just Number): ")
    #    if vm_storage_unit == "0":
    #        vm_storage_unit == "B"
    #            clean_screen()
    #        vm_storage_unit_configured = True
    #        break
    #    if vm_storage_unit == "1":
    #        vm_storage_unit = "KB"
    #            clean_screen()
    #        vm_storage_unit_configured = True
    #        break
        if vm_storage_unit == "2":
            vm_storage_unit = "MB"
            clean_screen()
            vm_storage_unit_configured = True
            break
        elif vm_storage_unit == "3":
            vm_storage_unit = "GB"
            clean_screen()
            vm_storage_unit_configured = True
            break
        elif vm_storage_unit == "4":
            vm_storage_unit = "TB"
            clean_screen()
            vm_storage_unit_configured = True
            break
        else:
            print("Please insert number to choose between each option.")
            delay(2)
            clean_screen()
            continue
        clean_screen()
def get_vm_storage():
    global vm_storage
    global vm_storage_configured
    while True:
        vm_storage = input("Virtual machine's virtual harddisk space: ")
        try:
            int(vm_storage)
            if int(vm_storage) >= 1:
                clean_screen()
                vm_storage_configured = True
                break
            else:
                print("Please insert a number > 0.")
                delay(2)
                clean_screen()
                continue
        except ValueError:
            print("Please insert a integer.")
            delay(2)
            clean_screen()
            continue
        clean_screen()
def get_vm_storage_sector():
    global vm_storage_logical
    global vm_storage_physical
    while True:
        print("Only Insert Number")
        vm_storage_logical = input("Logical Sector Byte   (Default:  512): ")
        vm_storage_physical = input("physical Sector Byte: (Default: 4096): ")
        try:
            int(vm_storage_logical)
            int(vm_storage_physical)
            break
        except ValueError:
            print("Please insert a integer, Press Enter To Try again")
            input()
            clean_screen()
            continue 
#-------------------------------------------------------#
#Network Adapter (Planning)
#-------------------------------------------------------#
#Main UI
def print_main_ui():
    print(time.strftime("%Y/%m/%d"))
    print(f"Nice to meet you, Administrator.")
    print(f"")
    print(f"Press the number in () and ENTER to config:")
    print(f"(1)  Virtual Machine's Name is                  : {vm_name}")
    print(f"(2)  Virtual Machine's Generation is            : {vm_gen}")
    print(f"(3)  Virtual Machine's Configuration Version is : {vm_config_version}")
    print(f"(4)  Virtual Machine's Cpu Core Number is       : {vm_cpu}")
    print(f"(5)  Virtual Machine's RAM is                   : {vm_ram}{vm_ram_unit}")
    print(f"(6)  Virtual Machine's Storage is               : {vm_storage}{vm_storage_unit}")
    print(f"")
    print(f"Advanced Config (Dangerous)")
    print(f"(A)  Nested Virtualization is Enabled           : {vm_cpu_enabled_nested}")
    print(f"(B)  Virtual Harddisk's Sector          Logical : {vm_storage_logical}Bytes")
    print(f"                                        Physical: {vm_storage_physical}Bytes")
    print(f"")
    print(f"Press the letter in () and ENTER to:")
    print(f"(C)  Create The VM")
    print(f"")
#-------------------------------------------------------#
#Main loop
while True:
    print_main_ui()
    action = input().upper()
    clean_screen()
    if action == "1":
        get_vm_name()
        continue
    elif action == "2":
        get_vm_gen()
        continue
    elif action == "3":
        get_vm_config_version()
        continue
    elif action == "4":
        get_vm_cpu()
        continue
    elif action == "5":
        get_vm_ram_unit()
        get_vm_ram()
        continue
    elif action == "6":
        get_vm_storage_unit()
        get_vm_storage()
        continue
    elif action == "A":
        get_vm_enabled_nested()
        continue
    elif action == "B":
        get_vm_storage_sector()
        continue
    elif action == "C":
        if vm_name_configured != True:
            print("Please config virtual machine's name first.")
            delay(2)
            clean_screen()
            continue
        elif vm_gen_configured != True:
            print("Please config virtual machine's generation first.")
            delay(2)
            clean_screen()
            continue
        elif vm_config_version_configured != True:
            print("Please config virtual machine's configuration version first.")
            delay(2)
            clean_screen()
            continue
        elif vm_cpu_configured != True:
            print("Please config virtual machine's cpu core number first.")
            delay(2)
            clean_screen()
            continue
        elif vm_ram_unit_configured != True:
            print("Please config virtual machine's ram unit first.")
            delay(2)
            clean_screen()
            continue
        elif vm_ram_configured != True:
            print("Please config virtual machine's ram amount first.")
            delay(2)
            clean_screen()
            continue
        elif vm_storage_unit_configured != True:
            print("Please config virtual machine's storage unit first.")
            delay(2)
            clean_screen()
            continue
        elif vm_storage_configured != True:
            print("Please config virtual machine's storage size first.")
            delay(2)
            clean_screen()
            continue
        else: #COMMANDS
            vm_storage_command = f"New-VHD '{vhd_path}{vm_name}.vhdx' -Dynamic -SizeBytes {vm_storage}{vm_storage_unit} -PhysicalSectorSizeBytes {vm_storage_physical} -LogicalSectorSizeBytes {vm_storage_logical}"
            vm_command = f"New-VM '{vm_name}' -Generation {vm_gen} -Version {vm_config_version} -MemoryStartupBytes {vm_ram}{vm_ram_unit} -VHDPath '{vhd_path}{vm_name}.vhdx'"
            vm_cpu_command = f"Set-VMProcessor '{vm_name}' -Count {vm_cpu} -ExposeVirtualizationExtensions ${str(vm_cpu_enabled_nested).lower()}"
            check = os.system(f"Powershell -Command \"Get-VM '{vm_name}'\"")
            if check == 0: #No error is 0, mean have this vm.
                print(f"Virtual Machine With Name \"{vm_name}\" Already Exist, Please Chenage Name First.")
                input("Press Enter To Go Back")
                clean_screen()
                continue
            else:
                clean_screen()
                error = os.system(f"Powershell -Command \"{vm_storage_command}\"")
                if error != 0:
                    print(f"Something Went Wrong")
                    input("Press Enter To Go Back")
                    clean_screen()
                    continue
                error = os.system(f"Powershell -Command \"{vm_command}\"")
                if error != 0:
                    print(f"Something Went Wrong")
                    print(f"Remember To Remove The Old Virtual Harddisk \"{vhd_path}{vm_name}.vhdx\"")
                    input("Press Enter To Go Back")
                    clean_screen()
                    continue
                error = os.system(f"Powershell -Command \"{vm_cpu_command}\"")
                if error != 0:
                    print(f"Something Went Wrong")
                    print(f"Remember To Remove The Old Virtual Harddisk \"{vhd_path}{vm_name}.vhdx\"")
                    input("Press Enter To Go Back")
                    clean_screen()
                    continue
                else:
                    print("================================================================================")
                    print("Done")
                    vm_name = "Not Configured"
                    vm_name_configured = False
                    input("\nPress Enter To Go Back")
                    clean_screen()
                    continue
    else:
        print("Please choose 1 option to do")
        delay(2)
        clean_screen()
        continue

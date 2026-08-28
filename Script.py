import os
import time
#-------------------------------------------------------#
#Default is cls
def run(command = "cls"):
    os.system(command)
#Default is 1 sec
def delay(secs = 1):
    time.sleep(secs)
#-------------------------------------------------------#
invalid_action_count = 0
def check_invalid_action_count():
    global invalid_action_count
    if invalid_action_count >10:
        run()
        print("This program is designed for Pros.\n")
        exit()
#-------------------------------------------------------#
vm_name = "Not Configured"
vm_gen = "Not Configured"
vm_config_version = "Not Configured"
vm_cpu = "Not Configured"
vm_ram_unit = ""
vm_ram = "Not Configured"
vm_storage_unit = ""
vm_storage = "Not Configured"
#-------------------------------------------------------#
vm_name_configured = False
vm_gen_configured = False
vm_config_version_configured = False
vm_cpu_configured = False
vm_ram_unit_configured = False
vm_ram_configured = False
vm_storage_unit_configured = False
vm_storage_configured = False
#-------------------------------------------------------#
#Name
def get_vm_name():
    global invalid_action_count
    global vm_name
    global vm_name_configured
    while True:
        vm_name = input("Name of the virtual machine: ").replace(" ","_")
        if vm_name == "":
            print("VM must have a name.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        else:
            run()
            vm_name_configured = True
            break
#-------------------------------------------------------#
#VM Generation
def get_vm_gen():
    global invalid_action_count
    global vm_gen
    global vm_gen_configured
    while True:
        print("Virtual Machine Generation")
        print("(1)    Generation 1")
        print("(2)    Generation 2")
        vm_gen = input("Virtual machine's Generation: ")
        if vm_gen == "1":
            run()
            vm_gen_configured = True
            break
        elif vm_gen == "2":
            run()
            vm_gen_configured = True
            break
        else:
            print("Please insert number to choose between each option.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        run()
#-------------------------------------------------------#
#VM Config Version
def get_vm_config_version():
    global invalid_action_count
    global vm_config_version
    global vm_config_version_configured
    while True:
        print("Virtual Machine's configuration versions")
        vm_config_version = input("Version: ")
        try:
            float(vm_config_version)
            run()
            vm_config_version_configured = True
            break
        except ValueError:
            print("Config Version is like 10.0 11.0, is a float.")
            invalid_action_count += 1
            delay(2)
            run()
            pass
#-------------------------------------------------------#
#Cpu core(s) amount
def get_vm_cpu():
    global invalid_action_count
    global vm_cpu
    global vm_cpu_configured
    while True:
        vm_cpu = input("Virtual Machine's CPU Core Amount (Just Number): ")
        try:
            int(vm_cpu)
            if int(vm_cpu) >= 1:
                run()
                vm_cpu_configured = True
                break
            else:
                print("Please insert a number > 0.")
                invalid_action_count += 1
                delay(2)
                run()
                check_invalid_action_count()
                pass
        except ValueError:
            print("Please insert a integer.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        run()
#-------------------------------------------------------#
#Ram amount
def get_vm_ram_unit():
    global invalid_action_count
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
    #        run()
    #        break
    #    if vm_ram_unit == "1":
    #        vm_ram_unit = "KB"
    #        vm_ram_unit_configured = True
    #        run()
    #        break
        if vm_ram_unit == "2":
            vm_ram_unit = "MB"
            run()
            vm_ram_unit_configured = True
            break
        elif vm_ram_unit == "3":
            vm_ram_unit = "GB"
            run()
            vm_ram_unit_configured = True
            break
        elif vm_ram_unit == "4":
            vm_ram_unit = "TB"
            run()
            vm_ram_unit_configured = True
            break
        else:
            print("Please insert number to choose between each option.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
def get_vm_ram():
    global invalid_action_count
    global vm_ram
    global vm_ram_configured
    while True:
        vm_ram = input("Ram for the virtual machine (Just Number): ")
        try:
            int(vm_ram)
            if int(vm_ram) >= 1:
                vm_ram_configured = True
                break
            else:
                print("Please insert a number > 0.")
                invalid_action_count += 1
                delay(2)
                run()
                check_invalid_action_count()
                pass
        except ValueError:
            print("Please insert a integer.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        run()
#-------------------------------------------------------#
#Disk space
def get_vm_storage_unit():
    global invalid_action_count
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
    #            run()
    #        vm_storage_unit_configured = True
    #        break
    #    if vm_storage_unit == "1":
    #        vm_storage_unit = "KB"
    #            run()
    #        vm_storage_unit_configured = True
    #        break
        if vm_storage_unit == "2":
            vm_storage_unit = "MB"
            run()
            vm_storage_unit_configured = True
            break
        elif vm_storage_unit == "3":
            vm_storage_unit = "GB"
            run()
            vm_storage_unit_configured = True
            break
        elif vm_storage_unit == "4":
            vm_storage_unit = "TB"
            run()
            vm_storage_unit_configured = True
            break
        else:
            print("Please insert number to choose between each option.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        run()
def get_vm_storage():
    global invalid_action_count
    global vm_storage
    global vm_storage_configured
    while True:
        vm_storage = input("Virtual machine's virtual harddisk space: ")
        try:
            int(vm_storage)
            if int(vm_storage) >= 1:
                run()
                vm_storage_configured = True
                break
            else:
                print("Please insert a number > 0.")
                invalid_action_count += 1
                delay(2)
                run()
                check_invalid_action_count()
                pass
        except ValueError:
            print("Please insert a integer.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        run()
#-------------------------------------------------------#
#Network Adapter (Planning)
#-------------------------------------------------------#
#Main UI
def print_main_ui():
    print(time.strftime("%Y/%m/%d"))
    print("Nice to meet you, Administrator.")
    print("")
    print(f"Virtual Machine's Name is                  : {vm_name}")
    print(f"Virtual Machine's Generation is            : {vm_gen}")
    print(f"Virtual Machine's Configuration Version is : {vm_config_version}")
    print(f"Virtual Machine's Cpu Core Number is       : {vm_cpu}")
    print(f"Virtual Machine's RAM is                   : {vm_ram}{vm_ram_unit}")
    print(f"Virtual Machine's Storage is               : {vm_storage}{vm_storage_unit}")
    print("")
    print("Press the number in () and ENTER to config:")
    print("(0) Virtual Machine's Name")
    print("(1) Virtual Machine's Generation")
    print("(2) Virtual Machine's Configuration Version")
    print("(3) Virtual Machine's Cpu Core Number")
    print("(4) Virtual Machine's RAM")
    print("(5) Virtual Machine's Storage")
    print("")
    print("Press the letter in () and ENTER to:")
    print("(C) Create The VM")
    print("(Q) Quit")
    print()
#-------------------------------------------------------#
#Main loop
while True:
    print_main_ui()
    action = input().upper()
    run()
    if action == "0":
        get_vm_name()
        pass
    elif action == "1":
        get_vm_gen()
        pass
    elif action == "2":
        get_vm_config_version()
        pass
    elif action == "3":
        get_vm_cpu()
        pass
    elif action == "4":
        get_vm_ram_unit()
        get_vm_ram()
        pass
    elif action == "5":
        get_vm_storage_unit()
        get_vm_storage()
        pass
    elif action == "C":
        if vm_name_configured != True:
            print("Please config virtual machine's name first.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        elif vm_gen_configured != True:
            print("Please config virtual machine's generation first.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        elif vm_config_version_configured != True:
            print("Please config virtual machine's configuration version first.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        elif vm_cpu_configured != True:
            print("Please config virtual machine's cpu core number first.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        elif vm_ram_unit_configured != True:
            print("Please config virtual machine's ram unit first.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        elif vm_ram_configured != True:
            print("Please config virtual machine's ram amount first.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        elif vm_storage_unit_configured != True:
            print("Please config virtual machine's storage unit first.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        elif vm_storage_configured != True:
            print("Please config virtual machine's storage size first.")
            invalid_action_count += 1
            delay(2)
            run()
            check_invalid_action_count()
            pass
        else: #COMMANDS
            is_failed = os.system(f"powershell -Command \"New-VM -Name \"{vm_name}\" -Generation {vm_gen} -Version {vm_config_version} -MemoryStartupBytes {vm_ram}{vm_ram_unit} -NewVHDPath \"{vm_name}.vhdx\" -NewVHDSizeBytes {vm_storage}{vm_storage_unit}\"")
            run()
            if is_failed == 0:
                run(f"powershell -Command \"Set-VMProcessor \"{vm_name}\" -Count {vm_cpu}\"")
                print("Done, Press Enter to exit")
                input("")
                exit()
            else:
                print(f"Failed")
                print(f"Press Enter to go back")
                input("")
                run()
                pass
    elif action == "Q":
        exit()
    else:
        print("Please choose 1 option to do")
        invalid_action_count += 1
        delay(2)
        run()
        check_invalid_action_count()
        pass

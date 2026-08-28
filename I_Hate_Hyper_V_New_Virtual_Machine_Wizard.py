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
idiot_count = 0
def check_idiot_count():
    global idiot_count
    if idiot_count >10:
        run()
        print("This program is not designed for idiots.\n")
        exit()
#-------------------------------------------------------#
vm_name = "Not Configured"
vm_gen = "Not Configured"
vm_cpu = "Not Configured"
vm_ram_unit = ""
vm_ram = "Not Configured"
vm_storage_unit = ""
vm_storage = "Not Configured"
#-------------------------------------------------------#
vm_name_configured = False
vm_gen_configured = False
vm_cpu_configured = False
vm_ram_unit_configured = False
vm_ram_configured = False
vm_storage_unit_configured = False
vm_storage_configured = False
#-------------------------------------------------------#
#Name
def get_vm_name():
    global vm_name
    global vm_name_configured
    while True:
        check_idiot_count()
        vm_name = input("Name of the virtual machine: ").replace(" ","_")
        run()
        if vm_name == "":
            print("VM must have a name.")
            idiot_count += 1
            delay(2)
            check_idiot_count()
            run()
            pass
        else:
            vm_name_configured = True
            break
#-------------------------------------------------------#
#VM Generation
def get_vm_gen():
    global vm_gen
    global vm_gen_configured
    while True:
        print("Virtual Machine Configuration Version (Aka. VM Generation)")
        print("(1)    Generation 1")
        print("(2)    Generation 2")
        vm_gen = input("Virtual machine's Configuration Version: ")
        if vm_gen == "1":
            vm_gen_configured = True
            break
        elif vm_gen == "2":
            vm_gen_configured = True
            break
        else:
            print("Please insert number to choose between each option.")
            idiot_count += 1
            delay(2)
            check_idiot_count()
            run()
            pass
        run()
#-------------------------------------------------------#
#Cpu core(s) amount
def get_vm_cpu():
    global vm_cpu
    global vm_cpu_configured
    while True:
        vm_cpu = input("CPU Core Amount (Just Number): ")
        try:
            int(vm_cpu)
            if int(vm_cpu) >= 1:
                vm_cpu_configured = True
                break
            else:
                print("Please insert a number > 0.")
                idiot_count += 1
                delay(2)
                check_idiot_count()
                run()
                pass
        except ValueError:
            print("Please insert a integer.")
            idiot_count += 1
            delay(2)
            check_idiot_count()
            run()
            pass
        run()
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
    #        run()
    #        break
    #    if vm_ram_unit == "1":
    #        vm_ram_unit = "KB"
    #        vm_ram_unit_configured = True
    #        run()
    #        break
        if vm_ram_unit == "2":
            vm_ram_unit = "MB"
            vm_ram_unit_configured = True
            run()
            break
        elif vm_ram_unit == "3":
            vm_ram_unit = "GB"
            vm_ram_unit_configured = True
            run()
            break
        elif vm_ram_unit == "4":
            vm_ram_unit = "TB"
            vm_ram_unit_configured = True
            run()
            break
        else:
            print("Please insert number to choose between each option.")
            idiot_count += 1
            delay(2)
            check_idiot_count()
            run()
            pass
def get_vm_ram():
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
                idiot_count += 1
                delay(2)
                check_idiot_count()
                run()
                pass
        except ValueError:
            print("Please insert a integer.")
            idiot_count += 1
            delay(2)
            check_idiot_count()
            run()
            pass
        run()
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
    #        vm_storage_unit_configured = True
    #        break
    #    if vm_storage_unit == "1":
    #        vm_storage_unit = "KB"
    #        vm_storage_unit_configured = True
    #        break
        if vm_storage_unit == "2":
            vm_storage_unit = "MB"
            vm_storage_unit_configured = True
            break
        elif vm_storage_unit == "3":
            vm_storage_unit = "GB"
            vm_storage_unit_configured = True
            break
        elif vm_storage_unit == "4":
            vm_storage_unit = "TB"
            vm_storage_unit_configured = True
            break
        else:
            print("Please insert number to choose between each option.")
            idiot_count += 1
            delay(2)
            check_idiot_count()
            run()
            pass
        run()
def get_vm_storage():
    global vm_storage
    global vm_storage_configured
    while True:
        vm_storage = input("Virtual machine's virtual harddisk space: ")
        try:
            int(vm_storage)
            if int(vm_storage) >= 1:
                vm_storage_configured = True
                break
            else:
                print("Please insert a number > 0.")
                idiot_count += 1
                delay(2)
                check_idiot_count()
                run()
                pass
        except ValueError:
            print("Please insert a integer.")
            idiot_count += 1
            delay(2)
            check_idiot_count()
            run()
            pass
        run()
#-------------------------------------------------------#
#Main UI
def print_main_ui():
    print(time.strftime("%Y/%m/%d"))
    print("Nice to meet you, Administrator.")
    print("")
    print(f"Virtual Machine's Name is                  : {vm_name}")
    print(f"Virtual Machine's Configuration Version is : {vm_gen}")
    print(f"Virtual Machine's Cpu Core Number is       : {vm_cpu}")
    print(f"Virtual Machine's RAM is                   : {vm_ram}{vm_ram_unit}")
    print(f"Virtual Machine's Storage is               : {vm_storage}{vm_storage_unit}")
    print("")
    print("Press the number in () and ENTER to config:")
    print("(0) Virtual Machine's Name")
    print("(1) Virtual Machine's Configuration Version")
    print("(2) Virtual Machine's Cpu Core Number")
    print("(3) Virtual Machine's RAM")
    print("(4) Virtual Machine's Storage")
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
    if action == "0":
        get_vm_name()
        pass
    elif action == "1":
        get_vm_gen()
        pass
    elif action == "2":
        get_vm_cpu()
        pass
    elif action == "3":
        get_vm_ram_unit()
        get_vm_ram()
        pass
    elif action == "4":
        get_vm_storage_unit()
        get_vm_storage()
        pass
    elif action == "C":
        if vm_name_configured != True:
            print("Please config virtual machine's name first.")
            idiot_count += 1
            delay(2)
            run()
            pass
        elif vm_gen_configured != True:
            print("Please config virtual machine's configuration version first.")
            idiot_count += 1
            delay(2)
            run()
            pass
        elif vm_cpu_configured != True:
            print("Please config virtual machine's cpu core number first.")
            idiot_count += 1
            delay(2)
            run()
            pass
        elif vm_ram_unit_configured != True:
            print("Please config virtual machine's ram unit first.")
            idiot_count += 1
            delay(2)
            run()
            pass
        elif vm_ram_configured != True:
            print("Please config virtual machine's ram amount first.")
            idiot_count += 1
            delay(2)
            run()
            pass
        elif vm_storage_unit_configured != True:
            print("Please config virtual machine's storage unit first.")
            idiot_count += 1
            delay(2)
            run()
            pass
        elif vm_storage_configured != True:
            print("Please config virtual machine's storage size first.")
            idiot_count += 1
            delay(2)
            run()
            pass
        else: #COMMANDS
            is_failed = run(f"powershell -Command \"New-VM -Name \"{vm_name}\" -ProcessorCount {vm_cpu} -MemoryStartupBytes {vm_ram}{vm_ram_unit} -Generation {vm_gen} -NewVHDPath \"{vm_name}.vhdx\" -NewVHDSizeBytes {vm_storage}{vm_storage_unit}\"")
            if is_failed == 0:
                print("Press Enter to exit")
                input("")
                exit()
            else:
                print(f"Failed")
                print(f"Press Enter to go back")
                input("")
                pass
    elif action == "Q":
        exit()
    else:
        print("Please choose 1 option to do")
        idiot_count += 1
        delay(2)
        run()
        pass

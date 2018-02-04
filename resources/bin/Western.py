# -*- coding: utf-8 -*-
import sys, os
sys.path.append("ipwndfu")
import dfu
#Credits
def credits() :

    os.system("clear")

    print("Main Credits: @32Bites, @Vyce_Merculous\nSoftware Used: XPwn, idevicerestore, ipwndfu\nSpecial Thanks To: Axi0mX, Planetbeing, and The iPhoneDevTeam.")

#Info
def information_fkp() :

    os.system("clear")

    print("Nothing, really. Just a project the @32Bites maintains... sometimes.")
    credits()

#Update manually, lol
def update_fkp() :

    os.system("clear")

    print("I won't bother to add this option, If you need to update, do it manually.")

#Verbose Boot
def install_verbose_boot() :

    enter_pwned_dfu()

    print("This option, only supports these versions on both BR: \n1) iOS 3.1.3\n2) iOS 4.1\n3) iOS 4.2.1\n4) iOS 5.0.1\n5) iOS 5.1.1\n6) iOS 6.1\n7) iOS 6.1.3\n8) iOS 6.1.6")

    try:

        verbose_option = input("Your selected version ! ")

    except:

        print("The option you have chosen is not a integer!")

        exit()

    if verbose_option == 1:

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/3.1.3_.dump")

    elif verbose_option == 2:

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/4.1_.dump")

    elif verbose_option == 3:

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/4.2.1_.dump")

    elif verbose_option == 4:

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/5.0.1_.dump")

    elif verbose_option == 5:

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/5.1.1_.dump")

    elif verbose_option == 6:

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/6.1_.dump")

    elif verbose_option == 7:

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/6.1.3_.dump")

    elif verbose_option == 8:

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/6.1.6_.dump")

    else:


        print("NOT A VALID OPTION!")
        exit()


#Restore to a Custom firmware
def restore_cfw() :

    os.system("clear")

    print("Your going to restore to a custom ipsw.\nBE IN DFU NOT PWNED DFU!!!\n")

    cfw_path = raw_input("Path to custom ipsw ! ")

    os.system("idevicerestore -c " + cfw_path)


#Create Custom Firmware ipsw
def create_cfw() :

    os.system("clear")

    print("Your about to create a custom ipsw. \nNOTE: you have to have the proper FirmwareBundle in the .resources/FirmwareBundles/ folder.")

    base_ipsw_path = raw_input("Path to base ipsw ! ")

    save_cfw_path = raw_input("Path to save ipsw ! ")

    os.system("./ipsw " + base_ipsw_path + " " + save_cfw_path + "-b Logos/0.png -r Logos/1.png -bbupdate")


#Pwned DFU
def enter_pwned_dfu() :
    device = dfu.acquire_device()
    if 'PWND:[' in device.serial_number:
        print 'Device is already in pwned DFU Mode. Not executing exploit.'
    else:    
         print("Be in dfu, then hit any key once in dfu.")
         ddffuu = raw_input("")
         os.system("clear && cd ipwndfu/ && ./ipwndfu -p")
         print("Pwned")

#24KPwn
def install_24kpwn_exploit() :

    enter_pwned_dfu()

    os.system("clear && cd ipwndfu/ && ./ipwndfu --24kpwn")


#Alloc8
def install_alloc8_exploit() :

    enter_pwned_dfu()

    os.system("clear && cd ipwndfu/ && ./ipwndfu -x")


def main() :

    os.system("clear && cd bin/")

    print("Western has started.\n Script Written By @32Bites\n")

    print("Options:\n")

    print("1) Create ipsw\n2) Install custom ipsw (Be in DFU, not PWNed DFU)\n3) Update\n4) Credits :D\n5) Info\n6) Install verbose boot (BE IN DFU)\n7) Install 24kpwn on old BR devices(BE IN DFU)\n8) Install Alloc8 on new BR devices(BE IN DFU)\n9) Enter PWNed DFU")

    try:

        option_1 = input("Your Option ! ")

    except:

        print("The option you have chosen is not a integer!")

        exit()

    if option_1 == 1:

        create_cfw()

    elif option_1 == 2:

        restore_cfw()

    elif option_1 == 3:

        update_fkp()

    elif option_1 == 4:

        credits()

    elif option_1 == 5:

        information_fkp()

    elif option_1 == 6:

        install_verbose_boot()

    elif option_1 == 7:

        install_24kpwn_exploit()

    elif option_1 == 8:

        install_alloc8_exploit()

    elif option_1 == 9:

        enter_pwned_dfu()

    else :

        print("NOT A VALID OPTION!")

        exit()

    print("\nI am done doing my job, please donate some BTC to: 12ixMaq2FnRkdwNBZGLrmG6NAdez7Cbt1Y")

main()

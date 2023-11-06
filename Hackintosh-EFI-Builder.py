# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:30:57 2021

@author: Arun Vaithianathan
"""

import os
os.system('pip install --upgrade pip')
os.system('pip install pywin32')

#Imported packages
import urllib.request
import zipfile
import time
import win32api
import shutil
from os import system, name 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
 
    
Name=win32api.GetUserName()
    
clear()
#Script start 
print('Welcome to Hackintosh EFI Builder by AKVAITHI')
print('What do you like to do today', Name,'?')
print('-------------------------------------------------------')
print('1: Start making a bootable USB')
print('Q: Quit')
Selection=input()
clear()


#Selection 1: Start making a bootable USB 
while Selection=='1':
    

    print('Beginning Rufus.exe Download')
    Rufus = 'https://github.com/pbatard/rufus/releases/download/v3.13/rufus-3.13.exe'
    RufusDownload='C:\\Users\Public\Desktop\Rufus.exe'
    urllib.request.urlretrieve(Rufus, RufusDownload)
    print('Rufus.exe has been Downloaded')
    os.system('start C:\\Users\Public\Desktop\Rufus.exe')
    os.system('start https://akvaithi.tk/index.php/s/Hmga4bRQJC5cddr')
        
    print('What USB do you want to use to make the installer?')
    print('You need to make a bootable USB so I recommend that you plug in a USB to get started (Pressing enter will default to your Downloads folder)')
    print('If you are directely downloading to the USB (Which I recommend) MAKE SURE THE DRIVE IS FORMATTED WITH AT LEAST 4 GB AND FAT32')
    print('-------------------------------------------------------')    
    #Prints drive letters
    DriveList = win32api.GetLogicalDriveStrings()
    DriveList = DriveList.split('\000')[:-1]
    print('The following drive letters are available')
    print('')
    print(DriveList)
    print('')
    print('Your drive is likely the last one')
    print('Below, enter the drive letter for your USB drive. The format should be like so')
    print('e.g. "F:"')
    
   
    #Input from user regarding where the file should be stored
    Drive=input()
    clear()
    print('The selected drive is ',Drive)
    print('Press ENTER to begin')
    temp=input()
    clear()
    os.remove('C:\\Users\Public\Desktop\Rufus.exe')
    os.remove(Drive+'autorun.ico')
    os.remove(Drive+'autorun.inf')
    
    Location=Drive+'OpenCore.zip'
    
    clear()
    #Downloading the OpenCore Release from Github
    print('Beginning OpenCore Package Download')
    urlopncre = 'https://github.com/acidanthera/OpenCorePkg/releases/download/0.6.5/OpenCore-0.6.5-RELEASE.zip'
    urllib.request.urlretrieve(urlopncre, Location)
    print('OpenCore Package Downloaded')
    time.sleep(1)

    #Unzipping the .zip file
    print('Extracting the Downloaded Package' )
    with zipfile.ZipFile(Location, 'r') as zip_ref:
        zip_ref.extractall(Drive+'OpenCore')
    print('Package has been extracted')
    time.sleep(1)

    #Deleting the .zip file
    print('Removing zip file')
    os.remove(Location)
    
    clear()
    #setting up the EFI Folder
    print('First of all, DO KEEP IN MIND this tool is not the be all and end all of Hackintoshing')
    print('This tool will try its best to create the boot USB')
    print('-------------------------------------------------------')
    print('The drive selected is ',Drive)
    print('Before we begin, I will download and delete all of the files that are universal')
    print('Just one quick question, is your CPU 64 or 32 bit?')
    print('-------------------------------------------------------')
    print('1: 32-bit')
    print('2: 64-bit')
    Bit=input()

    clear()    
    #32-Bit
    print('.')
    if Bit=='1':
        os.renames(Drive+'OpenCore\Docs\Sample.plist', Drive+'OpenCore\IA32\EFI\OC\config.plist')
        shutil.rmtree(Drive+'OpenCore\X64')
        os.renames(Drive+'OpenCore\IA32\EFI', Drive+'EFI')
    
    #64-bit
    print('.')
    if Bit=='2':
        os.renames(Drive+'OpenCore\Docs\Sample.plist', Drive+'OpenCore\X64\EFI\OC\config.plist')
        shutil.rmtree(Drive+'OpenCore\IA32')
        os.renames(Drive+'OpenCore\X64\EFI', Drive+'EFI')
    
    #Universal
    print('.')
    shutil.rmtree(Drive+'OpenCore\Docs')
    print('.')
    shutil.move(Drive+'OpenCore\\Utilities\macrecovery', Drive+'com.apple.recovery.boot')
    print('.')
    shutil.rmtree(Drive+'OpenCore')
    print('.')
    shutil.rmtree(Drive+'EFI\OC\Tools')
    print('.')
    os.mkdir(Drive+'EFI\OC\Tools')
    print('.')
    shutil.move(Drive+'EFI\OC\Drivers\OpenRuntime.efi', Drive+'EFI\OC')
    print('.')
    shutil.rmtree(Drive+'EFI\OC\Drivers')
    print('.')
    os.renames(Drive+'EFI\OC\OpenRuntime.efi', Drive+'EFI\OC\Drivers\OpenRuntime.efi')
    
    #HfsPlus download
    print('.')
    Driverurl='https://github.com/acidanthera/OcBinaryData/raw/master/Drivers/HfsPlus.efi'
    print('.')
    urllib.request.urlretrieve(Driverurl, Drive+'EFI\OC\Drivers\HfsPlus.efi')
    
    #VirtualSMC download
    print('.')
    Driverurl='https://github.com/acidanthera/VirtualSMC/releases/download/1.1.9/VirtualSMC-1.1.9-RELEASE.zip'
    print('.')
    urllib.request.urlretrieve(Driverurl, Drive+'EFI\OC\Kexts\VirtualSMC.zip')
    
    #Lilu download
    print('.')
    Driverurl='https://github.com/acidanthera/Lilu/releases/download/1.5.0/Lilu-1.5.0-RELEASE.zip'
    print('.')
    urllib.request.urlretrieve(Driverurl, Drive+'EFI\OC\Kexts\Lilu.zip')
    
    #Whatever Green download
    print('.')
    Driverurl='https://github.com/acidanthera/WhateverGreen/releases/download/1.4.6/WhateverGreen-1.4.6-RELEASE.zip'
    print('.')
    urllib.request.urlretrieve(Driverurl, Drive+'EFI\OC\Kexts\WhateverGreen.zip')
    

    #Unzip and delete Kexts
    print('.')
    with zipfile.ZipFile(Drive+'EFI\OC\Kexts\VirtualSMC.zip', 'r') as zip_ref:
        print('.')
        zip_ref.extractall(Drive+'EFI\OC\Kexts\VirtualSMC')
    print('.')
    os.remove(Drive+'EFI\OC\Kexts\VirtualSMC.zip')
    print('.')
    shutil.move(Drive+'EFI\OC\Kexts\VirtualSMC\Kexts\VirtualSMC.kext', Drive+'EFI\OC\Kexts\VirtualSMC.kext')
    print('.')
    shutil.rmtree(Drive+'EFI\OC\Kexts\VirtualSMC')
    
    print('.')
    with zipfile.ZipFile(Drive+'EFI\OC\Kexts\Lilu.zip', 'r') as zip_ref:
        print('.')
        zip_ref.extractall(Drive+'EFI\OC\Kexts\Lilu')
    print('.')
    os.remove(Drive+'EFI\OC\Kexts\Lilu.zip')
    print('.')
    shutil.move(Drive+'EFI\OC\Kexts\Lilu\Lilu.kext', Drive+'EFI\OC\Kexts\Lilu.kext')
    print('.')
    shutil.rmtree(Drive+'EFI\OC\Kexts\Lilu')
    
    print('.')
    with zipfile.ZipFile(Drive+'EFI\OC\Kexts\WhateverGreen.zip', 'r') as zip_ref:
        print('.')
        zip_ref.extractall(Drive+'EFI\OC\Kexts\WhateverGreen')
    print('.')
    os.remove(Drive+'EFI\OC\Kexts\WhateverGreen.zip')
    print('.')
    shutil.move(Drive+'EFI\OC\Kexts\WhateverGreen\WhateverGreen.kext', Drive+'EFI\OC\Kexts\WhateverGreen.kext')
    print('.')
    shutil.rmtree(Drive+'EFI\OC\Kexts\WhateverGreen')
    
    clear()   
    print('All tasks complete')
    time.sleep(3)

    clear()
    print('What version of macOS will you be installing?')
    print('-------------------------------------------------------')
    print('1: 11.0')
    print('2: 10.15')
    print('3: 10.14')
    print('4: 10.13')
    print('5: 10.12')
    print('6: 10.11')
    print('7: 10.10')
    print('8: 10.9')
    print('9: 10.8')
    print('10: 10.7')
    Version=input()
    exec(open('macrecovery.py').read())

    #First Choice
    clear()
    print('Now for the first step, select your type of CPU (AMD Laptop CPUs are not supported)')
    print('-------------------------------------------------------')
    print('1: AMD Desktop')
    print('2: Intel Desktop')
    print('3: Intel Laptop')
    CPUbrand=input()
    
    #CPU Brand AMD Desktop
    clear()
    if CPUbrand=='1':
        print('Great, so it seems that youre on team red')
        print('What generation is your CPU from?')
        print('-------------------------------------------------------')
        print('1: Bulldozer(15h) and Jaguar(16h)')
        print('2: Ryzen(17h) and Threadripper(19h)')
        GenAMD=input()
                        
    #CPU Brand Intel Desktop    
    clear()
    if CPUbrand=='2':
        print('Team blue I see')
        print('What generation is your CPU from?')
        print('-------------------------------------------------------')
        print('1:')
        
    #CPU Brand Intel Laptop
    clear()
    if CPUbrand=='3':
        print('A mobile user, trying to turn their laptop into a Macbook. Good luck!')
        print('What generation is your CPU from?')
        print('-------------------------------------------------------')
        print('1:')
    
    #Ethernet Selection
    clear()
    print('What ethernet NIC do you have?')
    print('-------------------------------------------------------')
    NICbrand=input()
    
    
    
    
#Selection Q: Quit
if Selection=='Q'or'q':
    print('Goodbye, and thanks for using Hackintosh EFI Builder!')
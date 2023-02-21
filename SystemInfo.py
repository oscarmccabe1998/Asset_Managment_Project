import psutil
import platform
import json
import subprocess
import ipaddress
import unittest
import re


uname = platform.uname()

#function to get the system ip
def getIP():
    temp_ip_list = []
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET' or str(address.family) == '2':  #code to get the system ip and ignores the loopback address
                if address.address != '127.0.0.1':
                    ip = address.address
                    interfaceinfo = []
                    interfaceinfo.append(ip)
                    if uname.system == "Darwin":
                        interface = interface_name
                        macaddress = subprocess.getoutput([f'ifconfig {interface} | grep ether '])
                        macaddress = macaddress.split(" ")
                        macaddress = macaddress[1]
                    elif uname.system == "Windows":
                        macaddress = subprocess.getoutput(['ipconfig', '/all', '|', 'findstr', 'Physical'])
                        macaddress = macaddress.split(" : ")[1]
                        #temp_ip_list.append(address.address)
                        #ip = temp_ip_list[0]
                        #return ip
                    #print(interface)
                    #ip = temp_ip_list[1]
                    interfaceinfo.append(macaddress)
                    return interfaceinfo


#function to get the system model

def getModel():
    testlst = []
    if uname.system == "Darwin":    #system check to run the correct command
        commandResult = subprocess.getoutput(["sysctl hw.model"])
        model = commandResult.split(" ")[1]
        return model
    elif uname.system == "Windows":
        commandResult = subprocess.getoutput(['wmic', 'computersystem', 'get', 'model'])
        model = commandResult.split("\n")[2]        #ensures the correct formatting before adding to object
        return model

def getManufacturer():          #Checcks OS type and returns dummy data for mac and runs command for windows machines
    if uname.system == "Darwin":
        manufacturer = "Apple"
    elif uname.system == "Windows":
        getManufacturerCommand = subprocess.getoutput(['wmic', 'computersystem', 'get', 'manufacturer'])
        manufacturer = getManufacturerCommand.split("\n")[2]
    return manufacturer

#Class to store the system information

class Sysinfo:
    def __init__(self, sysName, sysMachine, sysMacAddress, sysIP, sysModel, sysManufacturer):
        self.sysName = sysName
        self.sysMachine = sysMachine
        self.sysMacAddress = sysMacAddress
        self.sysIP = sysIP
        self.sysModel = sysModel
        self.sysManufacturer = sysManufacturer

#Class to store the OS information

class SoftwareInfo:
    def __init__(self, Name, Version, BuildVersion, Manufacturer):
        self.Name = Name
        self.Version = Version
        self.BuildVersion = BuildVersion
        self.Manufacturer = Manufacturer

#Main function to call other functions and add results to this_system object

def getInfo():
        model = getModel()
        interfaceinfo = getIP()
        ip = interfaceinfo[0]
        mac = interfaceinfo[1]
        manufacturer = getManufacturer()
        this_system = Sysinfo(uname.node, uname.machine, mac, ip, model, manufacturer)
        jsonStr = json.dumps(this_system.__dict__)
        print(jsonStr)
        return this_system

def getSoftware():
    if uname.system == "Darwin":
        OS_info = subprocess.getoutput(["sw_vers"])
        result = OS_info.split(":")
        newlist = []
        finallist = []
        for item in result:
            item = item.replace('\t\t', '')
            newlist.append(item)
        for item in newlist:
            item = item.replace('\n', ' ')
            tempitem = item.split(" ")
            item = tempitem[0]
            finallist.append(item)
        del finallist[0]
        Name = finallist[0]
        Version = finallist[1]
        BuildVersion = finallist[2]
        Manufacturer = "Apple"
        SystemSoftware = SoftwareInfo(Name, Version, BuildVersion, Manufacturer)
        return SystemSoftware
    elif uname.system == "Windows":
        OS_info = subprocess.getoutput('systeminfo | findstr /B /C:"OS Name" /B /C:"OS Version"')
        #OS_info = OS_info.replace(" ", "")
        returnlist = []
        OS_info = OS_info.split(":")
        for item in OS_info:
            if item != " ":
                returnlist.append(item.lstrip())
        #for item in range(OS_info):
        #    if OS_info[item] != " ":
        #        returnlist.append(OS_info[item])
        #returnlist = returnlist.split("\n")
        print(returnlist)
        finallist = []
        for item in returnlist:
            item = item.split("\n")
            finallist.append(item)
        extralist = finallist[2]
        finallist = finallist[1]
        extralist = extralist[0].split(" Build ")
        #print(finallist)
        baseinfo:str = finallist[0].split(" ")
        #print(extralist[1].split(" Build "))

        print(extralist)

        Name = baseinfo[1]
        Version = baseinfo[2]
        Manufacturer = baseinfo[0]
        BuildVersion = extralist[1]
        print(Name)
        print(Version)
        print(Manufacturer)
        print(BuildVersion)
        SystemSoftware = SoftwareInfo(Name, Version, BuildVersion, Manufacturer)
        return SystemSoftware


class TestNetworkInformation(unittest.TestCase):
    def testIP(self):
        interface = getIP()
        returnedip = interface[0]
        try:
            ip = ipaddress.ip_address(returnedip)
            result = True
        except ValueError:
            result = False
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()
    #getInfo()
    #getSoftware()

import subprocess
import optparse
import re


def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface",
                            dest="interface", help="mac to change!")
    parse_object.add_option(
        "-m", "--mac", dest="mac_address", help="new mac address")

    return parse_object.parse_args()


# user_interface = user_inputs.interface
# user_mac_adress = user_inputs.mac_address

# print(user_inputs.interface)
# print(user_inputs.mac_address)

# optparse Manuel Mac address

# interface = "eth0"
# mac_address = "00:22:33:77:99:11"


def change_mac_adress(user_interface, user_mac_address):

    subprocess.call(["ifconfig", "user_interface", "down"])
    subprocess.call(["ifconfig", "user_interface",
                     "hw", "ether", "user_mac_address"])
    subprocess.call(["ifconfig", "user_interface", "up"])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", "interface"])
    new_mac = re.search(r"\W\W:\W\W:\W\W:\W\W:\W\W:\W\W", ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None


print("Get Started!")
(user_input, arguments) = get_user_input()
change_mac_adress(user_input.interface, user_input.mac_address)
final_mac = control_new_mac(user_input.interface)

if final_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")


# Çalıştırma komutu python Subpro.py Linux Terminal Mac address değiştirme

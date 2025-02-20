import platform
from main_mac import menu_mac
from main_lin import menu_lin

def cur_platform():
    return platform.system()

def main():
    if cur_platform() == "Darwin":
        menu_mac()
    elif cur_platform() == "Linux":
        menu_lin()
    else:
        return "Looks like you are Windows user"

main()
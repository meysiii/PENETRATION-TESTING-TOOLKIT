from modules import port_scanner, brute_forcer

def main():
    print("1. Port Scanner")
    print("2. Brute Force (Demo)")
    choice = input("Select module: ")

    if choice == '1':
        target = input("Enter target IP: ")
        port_scanner.scan_ports(target)
    elif choice == '2':
        username = input("Enter username: ")
        brute_forcer.brute_force(username)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
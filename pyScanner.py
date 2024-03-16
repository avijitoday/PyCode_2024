# Simple port scanner in Python ...

import socket

def port_scan(target_ip, port ):
    """
    Scan specific port on the target machine
    :param target_ip:
    :param port:
    :return:
    """
    try:
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # set socket timeout time to 1 second.
        s.settimeout(1)
        #  connecting to target IP and specific port
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print ("Port {} is open".format(port))
        else:
            print ("Port {} is closed".format(port))
        # close th socket connection
        s.close()
    except socket.error as e:
        print(f"Error: {e}")

def main():
    target_ip = input("Please Enter Target IP Address :")
    start_port = int(input("Please enter start port no: "))
    end_port = int(input("Please ebter end-port no: "))
    for port in range(start_port, end_port+1):
        port_scan(target_ip, port)

if __name__ == "__main__":
    main()
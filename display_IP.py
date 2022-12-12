import socket, os

# display current IP
hostnm = socket.gethostname()
ipaddr = socket.gethostbyname(hostnm)
print("\nIP Address is:", ipaddr)

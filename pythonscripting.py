from scapy.all import *
import time


SRC_IP = "192.168.1.100"
DST_IP = "192.168.2.100"
NUM_PACKETS = 10

def test_vpn_latency():
    latencies = []

    for i in range(NUM_PACKETS):
        pkt = IP(src = SRC_IP, dst = DST_IP) / ICMP()
        start_time = time.time()
        reply = sr1(pkt, timeout = 2, verbose = False)
        end_time = time.time()

        if reply:
            latency = (end_time - start_time) * 1000
            latencies.append(latency)
            print(f"Packet {i+1}: {latency:.2f} ms")
        else:
            print(f"Packet {i+1} timed out")

    print("\nAverage Latency:", sum(latencies) / len(latencies) if latencies else "N/A")

test_vpn_latency()

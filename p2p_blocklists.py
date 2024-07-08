#!/usr/local/bin/python3.11

import sys
import ipaddress

out = open(sys.argv[2], "w")

def is_valid_address(address):
    try:
        ipaddress.ip_address(address)
    except ValueError:
        return False
    return True

def generate(ip_lower, ip_upper):
    if is_valid_address(ip_lower) is True and is_valid_address(ip_upper) is True:
        lower = ipaddress.ip_address(ip_lower)
        upper = ipaddress.ip_address(ip_upper)
        ranges = [ipaddr for ipaddr in ipaddress.summarize_address_range(lower, upper)]
        for range in ranges:
            out.write(str(range) + "\n")

with open(sys.argv[1]) as src:
    ip_ranges = src.readlines()[0].split(",")

while("" in ip_ranges):
    ip_ranges.remove("")

for ip_range in ip_ranges:
    ip_range_list = ip_range.split("-")
    if len(ip_range_list) == 2:
        generate(ip_range_list[0],ip_range_list[1])

out.close()

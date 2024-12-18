




log_data = """192.168.1.1 - - [18/Dec/2024:08:00:25 +0000] "GET /index.html HTTP/1.1" 200 2326
192.168.1.2 - - [18/Dec/2024:08:00:30 +0000] "POST /login HTTP/1.1" 301 527
"""

# 로그 데이터를 줄 단위로 분리
lines = log_data.splitlines()

# IP 주소만 추출
ip_addresses = [line.split()[0] for line in lines]
print(ip_addresses)

ip_addresses_set = set(ip_addresses)

ip_frequency = {f'{ip}' : ip_addresses.count(ip) for ip in ip_addresses_set}

print(ip_frequency)
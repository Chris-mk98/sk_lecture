import re
import os.path
import sys

class LogData():
    def __init__(self, filepath):
        self.filepath=filepath
        self.ips = []

    def extract_ips(self):
        try:
            with open(self.filepath, 'r') as file:
                log_content = file.readline()
                ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                self.ips = re.findall(ip_pattern, log_content)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()
    
    def frequency(self):
        self.set = set(self.ips)
        self.ip_frequency = {f'{ip}' : self.ips.count(ip) for ip in self.set}
        self.ip_frequency = sorted(self.ip_frequency.items(), key=lambda x: x[1], reverse=True)

    def top_3(self):
        print(self.ip_frequency[0:3])

    def to_csv(self):
        csv_file = open("ip_log.csv", 'w')
        csv_file.write('IP, Frequency\n')
        for (ip, frequency) in self.ip_frequency:
            csv_file.writelines(f"{ip},{frequency}\n")
        csv_file.close()
        if os.path.isfile('ip_log.csv'):
            print('file save success')
        else:
            print('Fail to save')

if __name__ == '__main__':
    filepath = input("Input log file's path: ")
    log_data = LogData(filepath)
    log_data.extract_ips()
    log_data.frequency()
    log_data.top_3()
    log_data.to_csv()

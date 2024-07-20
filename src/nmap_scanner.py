import nmap
import json

def scan_target(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sS -O -sV')
    return nm.csv()

def save_report(results, filename):
    with open(filename, 'w') as f:
        f.write(results)

if __name__ == "__main__":
    target = input("Nhập IP hoặc Domain để quét: ")
    results = scan_target(target)
    save_report(results, 'nmap_report.csv')
    print("Báo cáo đã được lưu vào nmap_report.csv")

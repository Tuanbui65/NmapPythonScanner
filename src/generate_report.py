import pandas as pd

def generate_html_report(csv_file, output_file):
    df = pd.read_csv(csv_file)
    html = df.to_html()
    with open(output_file, 'w') as f:
        f.write(html)

if __name__ == "__main__":
    generate_html_report('nmap_report.csv', 'nmap_report.html')
    print("Báo cáo HTML đã được tạo và lưu vào nmap_report.html")

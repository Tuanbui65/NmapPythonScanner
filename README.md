## Usage

### Prepare Your Environment
- Ensure that Nmap is installed on your system. You can download it from the [Nmap official website](https://nmap.org/download.html).

### Running the Scanner
1. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
2. Run the Python script to perform a network scan. The script will prompt you to enter the target IP address or domain.
   ```bash
   python src/nmap_scanner.py
3. Follow the prompts to enter the IP address or domain you wish to scan. The scanner will execute the scan and save the results.
### Viewing the Results
- Once the scan is complete, the results will be saved in a file named nmap_report.csv.
- Open nmap_report.csv with any spreadsheet application like Microsoft Excel or Google Sheets to view and analyze the scan results.

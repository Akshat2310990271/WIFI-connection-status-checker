import csv
import sys
from pathlib import Path

def analyze_log(log_file):
    counts = {"CONNECTED": 0, "DISCONNECTED": 0, "ERROR": 0}
    with open(log_file, encoding="utf-8") as file:
        for line in file:
            for event in counts:
                if event in line.upper():
                    counts[event] += 1
    return counts

def main():
    log_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sample_logs/device_log.txt")
    counts = analyze_log(log_file)
    output = Path("output/connection_report.csv")
    output.parent.mkdir(exist_ok=True)
    with open(output, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Event", "Count"])
        writer.writerows(counts.items())
    print(counts)
    print("Report:", output)

if __name__ == "__main__":
    main()

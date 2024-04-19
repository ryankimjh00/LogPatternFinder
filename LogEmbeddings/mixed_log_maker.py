import re
import os
from datetime import datetime, timedelta
import glob

def extract_timestamp(log_line):
    match = re.search(r'\[(\d{2}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2})\]', log_line)
    if match:
        timestamp_str = match.group(1)
        timestamp = datetime.strptime(timestamp_str, '%y.%m.%d %H:%M:%S')
        return timestamp
    else:
        return None

def remove_numbers(log_line):
    return re.sub(r'\d+', '', log_line)

def split_logs_with_overlap(input_file, output_directory, total_files, current_file_index):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    start_time = extract_timestamp(lines[0])
    end_time = extract_timestamp(lines[-1])

    if start_time is None or end_time is None:
        print(f'❌ Failed to extract timestamps from log lines on {input_file}')
        return

    current_time = start_time
    interval = timedelta(seconds=30)
    overlap = timedelta(seconds=10)

    while current_time + interval <= end_time:
        file_name = os.path.join(output_directory, f"log_{current_time.strftime('%Y.%m.%d %H:%M:%S')}.txt")
        with open(file_name, 'w') as output_file:
            for line in lines:
                timestamp = extract_timestamp(line)
                if timestamp and current_time <= timestamp < current_time + interval:
                    # if "INFO" in line or "DEBUG" in line:
                    output_file.write(remove_numbers(line))
        current_time += interval - overlap

    print(f'✅ Completed processing file {current_file_index} of {total_files}: {input_file}')

def process_all_log_files(directory):
    log_files = glob.glob(os.path.join(directory, '*.log.*'))
    output_directory = "/mnt/c/LogPatternFinder/LogEmbeddings/mixed_docs"
    total_files = len(log_files)
    for index, log_file in enumerate(log_files, start=1):
        print(f'⌛ Processing file {index} of {total_files}: {log_file} ')
        split_logs_with_overlap(log_file, output_directory, total_files, index)

directory = "/mnt/c/LogPatternFinder/LogEmbeddings/input"
process_all_log_files(directory)

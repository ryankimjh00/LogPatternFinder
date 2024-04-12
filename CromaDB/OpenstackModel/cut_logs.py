import re
import os
from datetime import datetime, timedelta

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

# 로그 파일을 읽고 30초 간격으로 자르고 10초씩 겹치게 하는 함수
def split_logs_with_overlap(input_file, output_directory):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    start_time = extract_timestamp(lines[0])
    end_time = extract_timestamp(lines[-1])

    if start_time is None or end_time is None:
        print("Failed to extract timestamps from log lines.")
        return

    current_time = start_time
    interval = timedelta(seconds=30)
    overlap = timedelta(seconds=10)

    while current_time + interval <= end_time:
        file_name = os.path.join(output_directory, f"log_{current_time.strftime('%Y.%m.%d %H:%M:%S')}.log")
        with open(file_name, 'w') as output_file:
            for line in lines:
                timestamp = extract_timestamp(line)
                if timestamp and current_time <= timestamp < current_time + interval:
                    output_file.write(remove_numbers(line))
        current_time += interval - overlap

# 입력 로그 파일과 출력 디렉토리를 지정하고 함수 호출
input_file = "/mnt/c/LogPatternFinder/CromaDB/tester copy 2.log"
output_directory = "/mnt/c/LogPatternFinder/CromaDB/log"
# output_directory = "/mnt/c/LogPatternFinder/CromaDB/out"
split_logs_with_overlap(input_file, output_directory)

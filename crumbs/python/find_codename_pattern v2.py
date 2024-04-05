import re

# 파일 경로
file_path = "/mnt/c/LogPatternFinder/extracted_data.txt"
output_file_path = "/mnt/c/LogPatternFinder/thread_count_result2.txt"

# 이전 스레드 정보
previous_thread = None

# 각 스레드의 등장 횟수를 저장할 딕셔너리
thread_count = {}

# 각 스레드 패턴이 몇 번 반복되었는지를 저장할 딕셔너리
pattern_count = {}

# 스레드 등장 순서를 저장할 리스트
thread_order = []

# 정규식 패턴
pattern = r"\b\w+-\w+\b-\w"

# 파일 열기
with open(file_path, 'r') as file:
    # 파일의 각 줄에 대해 작업 수행
    for line in file:
        # 전체 줄을 하나의 단어로 처리
        current_thread = line.strip()
        # 이전 스레드와 현재 스레드가 다른 경우
        if current_thread != previous_thread:
            # 현재 스레드 등장 횟수 초기화
            thread_count[current_thread] = 1
        # 이전 스레드와 현재 스레드가 같은 경우
        else:
            # 현재 스레드의 등장 횟수 증가
            thread_count[current_thread] += 1
        # 스레드 등장 순서 저장
        thread_order.append(current_thread)
        # 이전 스레드 정보 업데이트
        previous_thread = current_thread

# 결과를 파일에 저장
with open(output_file_path, 'w') as output_file:
    for thread in thread_order:
        if thread not in thread_count:
            continue
        count = thread_count[thread]
        output_file.write(f"{thread}    {count}번\n")

print("결과가", output_file_path, "에 저장되었습니다.")

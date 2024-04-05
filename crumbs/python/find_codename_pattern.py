import re

# 파일 경로
file_path = "/mnt/c/Log Pattern/extracted_data.txt"

# 이전 스레드 정보
previous_thread = None

# 각 스레드의 등장 횟수를 저장할 딕셔너리
thread_count = {}

# 각 스레드 패턴이 몇 번 반복되었는지를 저장할 딕셔너리
pattern_count = {}

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
            # 이전 스레드와 같은 패턴이 있는지 확인
            if previous_thread:
                if previous_thread not in pattern_count:
                    pattern_count[previous_thread] = 1
                else:
                    pattern_count[previous_thread] += 1
        # 이전 스레드와 현재 스레드가 같은 경우
        else:
            # 현재 스레드의 등장 횟수 증가
            thread_count[current_thread] += 1
        # 이전 스레드 정보 업데이트
        previous_thread = current_thread

# 결과 출력
for thread, count in thread_count.items():
    pattern_repeat = pattern_count.get(thread, 0)
    # print(f"{thread}: {count}번 (패턴 반복 횟수: {pattern_repeat})")
    print(f"{thread} * {pattern_repeat}")

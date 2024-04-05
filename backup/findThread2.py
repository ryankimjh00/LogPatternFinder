import json
import glob

# 파일 패턴
file_pattern = "./sample/*.json"

# 파일 목록 얻기
file_list = glob.glob(file_pattern)

# 이전에 등장한 스레드 이름과 개수를 저장할 변수
previous_thread_info = None
count = 0

for file_path in file_list:
    # 파일 열기
    with open(file_path, 'r') as file:
        # 파일 내용 읽기
        log_data = json.load(file)

        # 모든 로그 라인에 대해 반복
        for log_line in log_data:
            # thread_name 값 추출
            thread_name = log_line['fields']['thread_name']

            # 이전에 처리한 스레드와 현재 스레드가 다른 경우에만 출력
            if thread_name != previous_thread_info:
                if previous_thread_info:
                    print(f"{previous_thread_info} {count}")
                previous_thread_info = thread_name
                count = 1
            else:
                count += 1
# for file_path in file_list:
#     # 파일 열기
#     with open(file_path, 'r') as file:
#         # 파일 내용 읽기
#         log_data = json.load(file)

#         # 모든 로그 라인에 대해 반복
#         for log_line in log_data:
#             # thread_name 값 추출
#             thread_name = log_line['fields']['thread_name']

#             # 이전에 처리한 스레드와 현재 스레드가 다른 경우에만 출력
#             if thread_name != previous_thread_info:
#                 if previous_thread_info:
#                     print(f"{count}")
#                 previous_thread_info = thread_name
#                 count = 1
#             else:
#                 count += 1
# # 마지막 스레드 정보 
# if previous_thread_info:
#     print(f"스레드 이름: {previous_thread_info}, 개수: {count}")

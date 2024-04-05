import json
import glob

# 파일 패턴
file_pattern = "./sample/*.json"

# 파일별 발견된 스레드 이름을 저장할 딕셔너리
file_threads = {}

# 모든 파일에 대해 반복
for file_path in glob.glob(file_pattern):
    # 발견된 스레드 이름을 저장할 리스트
    discovered_threads = []
    
    # 파일 열기
    with open(file_path, 'r') as file:
        # 파일 내용 읽기
        log_data = json.load(file)

        # 각 로그 라인에 대해 반복하면서 스레드 이름 추출하여 리스트에 추가
        for log_line in log_data:
            thread_name = log_line['fields']['thread_name']
            discovered_threads.append(thread_name)

    # 파일명에서 디렉토리 부분을 제외한 부분을 키로 사용
    file_key = file_path.split("/")[-1]

    # 발견된 스레드 이름을 파일별 딕셔너리에 추가
    file_threads[file_key] = discovered_threads

# 각 파일별로 발견된 스레드 이름을 쉼표로 구분하여 나열
for file_name, threads in file_threads.items():
    thread_str = "\n".join(threads)
    print(f"파일: {file_name}")
    print(f"   {thread_str}\n")

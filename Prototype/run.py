import os
import subprocess

# 실행할 파일들의 경로
file_paths = [
    "./step1-cut thread in log file.py",
    "./step2-group by thread name.py",
    "./step3-scale-thread.py",
    "./step4-find pattern.py",
    "./step5-scale pattern.py"
]

# 각 파일을 순차적으로 실행
for file_path in file_paths:
    # 파일이 존재하고 실행 가능한 상태인지 확인
    if os.path.exists(file_path) and os.access(file_path, os.X_OK):
        # 파일 실행 명령어 생성
        command = ["python3", file_path]

        # 파일 실행
        try:
            subprocess.run(command, check=True)
            print(f"{file_path} 실행 완료")
        except subprocess.CalledProcessError as e:
            print(f"{file_path} 실행 중 오류 발생: {e}")
    else:
        print(f"{file_path} 파일을 찾거나 실행할 수 없습니다.")

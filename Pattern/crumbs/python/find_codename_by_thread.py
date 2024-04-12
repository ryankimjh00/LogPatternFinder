import difflib

# 파일 경로
file_path = "/mnt/c/LogPatternFinder/extracted_data.txt"

# 파일을 읽어서 각 줄을 리스트에 저장
with open(file_path, 'r') as file:
    lines = file.read().splitlines()

# 각 줄의 반복되는 패턴 찾기
patterns = {}
for line in lines:
    # 줄을 공백을 기준으로 단어로 분할하여 처리
    words = line.split()
    # 각 단어들의 시퀀스 매칭을 이용하여 반복되는 패턴 찾기
    seq_matcher = difflib.SequenceMatcher(None, *words)
    match = seq_matcher.find_longest_match(0, len(words[0]), 0, len(words))
    if match.size > 0:
        pattern = " ".join(words[match.a : match.a + match.size])
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1

# 반복되는 패턴과 그 빈도 출력
for pattern, frequency in patterns.items():
    print(f"Pattern: {pattern}, Frequency: {frequency}")

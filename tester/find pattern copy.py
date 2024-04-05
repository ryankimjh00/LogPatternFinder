import re

def analyze_patterns(text, pattern):
    # 주어진 정규 표현식을 이용하여 일치하는 패턴을 찾음
    matches = re.findall(pattern, text)
    
    # 중복 패턴 카운트를 위한 딕셔너리 생성
    repeating_patterns = {}
    
    # 일치하는 패턴을 반복하면서 딕셔너리에 추가하고 카운트 증가
    for match in matches:
        if match in repeating_patterns:
            repeating_patterns[match] += 1
        else:
            repeating_patterns[match] = 1
    
    # 패턴을 반복 횟수에 따라 정렬
    sorted_patterns = sorted(repeating_patterns.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_patterns

def find_patterns_in_sentences(file_path, pattern):
    with open(file_path, 'r') as file:
        text = file.read()
        patterns_found = analyze_patterns(text, pattern)
    
    return patterns_found

file_path = "/mnt/c/Log Pattern/tester/conclusion/thread-grouping.txt"
pattern = r'\b\w+(?:-\w+)+\b'
patterns_found = find_patterns_in_sentences(file_path, pattern)

# 결과 출력
for pattern, count in patterns_found:
    print(f"Pattern: {pattern}")
    print(f"Repeats: {count}\n")

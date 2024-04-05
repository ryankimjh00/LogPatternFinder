import re

# 정규 표현식 패턴
pattern = r"\[.*?\] \[.*?\]  \[(\w*-+.*?)\]"

def suffix_array(string):
    suffixes = [(string[i:], i) for i in range(len(string))]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

def lcp_array(string, suffix_array):
    n = len(string)
    lcp = [0] * n
    rank = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = suffix_array[rank[i] + 1]
        while i + k < n and j + k < n and string[i + k] == string[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp

def find_longest_repeating_pattern(string):
    suffix_arr = suffix_array(string)
    lcp_arr = lcp_array(string, suffix_arr)
    max_length = max(lcp_arr)
    if max_length == 0:
        return ""
    else:
        idx = lcp_arr.index(max_length)
        return string[suffix_arr[idx]: suffix_arr[idx] + max_length]

def process_lines(lines):
    extracted_data = []
    for line in lines:
        match = re.search(pattern, line)
        if match:
            result = match.group(1)
            extracted_data.append(result)
    return extracted_data

def process_file(input_file_path):
    with open(input_file_path, 'r') as input_file:
        while True:
            # 파일에서 1000줄씩 읽어옴
            lines = [input_file.readline() for _ in range(1000)]
            if not lines:
                break  # 파일의 끝에 도달하면 종료
            extracted_data = process_lines(lines)
            # 추출된 데이터를 파일에 저장
            with open(output_file_path, 'a') as output_file:
                for data in extracted_data:
                    output_file.write(data + ' \n')

# 입력 파일 경로
input_file_path = "./test.log"
# 출력 파일 경로
output_file_path = "./extracted_data11.txt"
# 파일 처리
process_file(input_file_path)

# 추출된 데이터로부터 최장 반복 패턴 찾기
longest_pattern = find_longest_repeating_pattern(output_file_path)
print(longest_pattern)
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

def find_all_repeating_patterns(string):
    suffix_arr = suffix_array(string)
    lcp_arr = lcp_array(string, suffix_arr)
    patterns = []
    for i, length in enumerate(lcp_arr):
        if length > 0:
            patterns.append(string[suffix_arr[i]: suffix_arr[i] + length])
    return patterns

# 파일에서 라인을 읽어와 단어로 취급하여 계산
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    words = []
    for line in lines:
        line = line.strip()  # 라인 앞뒤 공백 제거
        words.extend(line.split())  # 단어로 분리하여 리스트에 추가
    
    text = ""
    for word in words:
        if word[-1].isdigit() and word[-3] == ":" or word[-4]==":" or word[-5]==":":
            text += word + "\n"
        else:
            text += word + " "
    return find_all_repeating_patterns(text)

# 예시 파일 경로
file_path = "/mnt/c/LogPatternFinder/extracted_data copy.txt"
all_patterns = process_file(file_path)

# 결과 출력
print("All repeating patterns:")
for pattern in all_patterns:
    print(pattern)

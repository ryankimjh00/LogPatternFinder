import re
# 이건 현재 스레드만 패턴찾는중
def suffix_array(words):
    n = len(words)
    suffixes = [(words[i:], i) for i in range(n)]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

def lcp_array(words, suffix_array):
    n = len(words)
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
        while i + k < n and j + k < n and words[i + k] == words[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp

def extract_number_after_colon(pattern):
    # 정규식을 사용하여 콜론(:) 뒤에 있는 숫자 추출
    match = re.search(r':([0-9]+)', pattern)
    if match:
        return match.group(1)  # 매치된 그룹의 첫 번째 숫자 문자열 반환
    return 'inf'  # 숫자가 없는 경우 문자열 'inf' 반환

def find_all_repeating_patterns(file_path, output_file):
    with open(file_path, 'r') as file:
        text = file.readlines()  # 줄 단위로 읽기
        processed_text = []
        for line in text:
            matches = re.findall(r'\[(.*?)\]', line)  # '\[(.*?)\ ]'에 매칭되는 부분 찾기
            for match in matches:
                processed_text.append(match)
        suffix_arr = suffix_array(processed_text)
        lcp_arr = lcp_array(processed_text, suffix_arr)
        repeating_patterns = {}
        for i, lcp in enumerate(lcp_arr):
            if lcp:  # 빈 패턴이 아닌 경우
                pattern = '\n'.join(processed_text[suffix_arr[i]: suffix_arr[i] + lcp])
                if pattern in repeating_patterns:
                    repeating_patterns[pattern] += 1
                else:
                    repeating_patterns[pattern] = 1

    # 패턴을 길이에 따라 정렬하고, 각 패턴도 정렬
    sorted_patterns = sorted(repeating_patterns.items(), key=lambda x: (extract_number_after_colon(x[0]), len(x[0]), x[0]))
    # sorted_patterns = sorted(repeating_patterns.items(), key=lambda x: (len(x[0]), x[0]))

    with open(output_file, 'w') as out_file:
        for pattern, count in sorted_patterns:
            if count >= 2:
                out_file.write(f"Pattern: \n{pattern}\n")
                out_file.write(f"Repeats: {count}\n\n")

                
file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/2.thread-grouping-cleaned.txt"
output_file = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/3.patterns.txt"
find_all_repeating_patterns(file_path, output_file)
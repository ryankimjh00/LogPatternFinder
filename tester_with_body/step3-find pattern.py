import re

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

def find_all_repeating_patterns(file_path, output_file):
    with open(file_path, 'r') as file:
        text = file.readlines()  # 줄 단위로 읽기
        processed_text = []
        for line in text:
            matches = re.findall(r'\[(.*?)\ ]', line)
            for match in matches:
                processed_text.append(match)
            processed_text.append(''.join(re.split(r'\[.*?\ ]', line)))  # []를 제거한 문자열 추가
        suffix_arr = suffix_array(processed_text)
        lcp_arr = lcp_array(processed_text, suffix_arr)
        repeating_patterns = {}
        for i, lcp in enumerate(lcp_arr):
            if lcp > 9 and lcp < 50:  # 빈 패턴이 아닌 경우
                pattern = ''.join(processed_text[suffix_arr[i]: suffix_arr[i] + lcp])
                if pattern in repeating_patterns:
                    repeating_patterns[pattern] += 1
                else:
                    repeating_patterns[pattern] = 1

    # 결과를 output_file에 출력
    with open(output_file, 'w') as out_file:
        for pattern, count in repeating_patterns.items():
            # repeat이 2 이상인 패턴만 출력
            if count >= 1:
                out_file.write(f"Pattern: \n{pattern}\n")
                out_file.write(f"Repeats: {count}\n\n")

file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/2.thread-grouping-cleaned.txt"
output_file = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/3.patterns.txt"
find_all_repeating_patterns(file_path, output_file)

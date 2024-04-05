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
        text = file.read().strip().split()  # 줄바꿈으로 구분되는 단어로 분리
        processed_text = []
        for word in text:
            if re.match(r'\d+:', word):  # 콜론(:)뒤에 숫자가 오면 줄바꿈 추가
                processed_text.append(word + '\n')
            else:
                processed_text.append(word)
        suffix_arr = suffix_array(processed_text)
        lcp_arr = lcp_array(processed_text, suffix_arr)
        repeating_patterns = {}
        for i, lcp in enumerate(lcp_arr):
            if lcp > 10 and lcp < 20:  # 4개 이상의 단어로 이루어진 패턴만 선택
                pattern = ' '.join(processed_text[suffix_arr[i]: suffix_arr[i] + lcp])
                if pattern in repeating_patterns:
                    repeating_patterns[pattern] += 1
                else:
                    repeating_patterns[pattern] = 1

    # 패턴을 짧은 순서대로 정렬하여 출력
    sorted_patterns = sorted(repeating_patterns.items(), key=lambda x: len(x[0]))

    # 결과를 output_file에 출력
    with open(output_file, 'w') as out_file:
        for pattern, count in sorted_patterns:
            
            # out_file.write(f"Repeats: {count}\n\n")

            # 패턴이 한 번 이상 반복될 때만 반복 횟수를 출력
            if count >= 1:
                out_file.write(f"Pattern: \n{pattern}\n")
                out_file.write(f"Repeats: {count}\n\n")

file_path = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/3.thread-scaled.txt"
output_file = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/4.patterns.txt"
find_all_repeating_patterns(file_path, output_file)

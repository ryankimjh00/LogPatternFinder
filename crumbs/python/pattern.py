# 접미사 배열 생성
# Manber-Myers 알고리즘 - 기수정렬을 이용한 접미사 배열 생성
#  문자열의 모든 접미사를 사전식 순서로 정렬하여 저장하는 배열
def suffix_array(string):
    n = len(string)
    suffixes = [(string[i:], i) for i in range(n)]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

# LCP 배열에서 가장 큰 값이 반복되는 패턴의 길이
# 최장 공통 접두사(Longest Common Prefix, LCP) 배열
# 접미사 배열에서 인접한 두 접미사의 공통 접두사의 길이를 저장하는 배열
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

def find_all_repeating_patterns(string):
    suffix_arr = suffix_array(string)
    lcp_arr = lcp_array(string, suffix_arr)
    repeating_patterns = []
    for i, lcp in enumerate(lcp_arr):
        if lcp > 1:
            repeating_patterns.append(string[suffix_arr[i]: suffix_arr[i] + lcp])
    return repeating_patterns

# 예시 문자열
example_string = "AABCAAB"
find_pattern = find_all_repeating_patterns(example_string)
print("Longest repeating pattern:", find_pattern)
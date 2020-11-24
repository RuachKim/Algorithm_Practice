from bisect import bisect_left, bisect_right


def count_by_range(a, left, right):
    l = bisect_left(a, left)
    r = bisect_right(a, right)

    return r-l


array = [[] for _ in range(10001)]
rev_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)
        rev_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        rev_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[q(len)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(array[q(len)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

        answer.append(res)

    return answer
    
    






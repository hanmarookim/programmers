from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words: return 0
    words = [begin] + words
    visit = 0
    q = deque([(0, 0)])
    while q:
        num, tick = q.popleft()
        if not visit & 1<<num:
            if words[num] == target: return tick
            visit = visit | 1<<num
            for w in range(len(words)):
                dif = 0
                for l in range(len(words[num])):
                    if words[num][l] != words[w][l]: dif += 1
                    if dif > 1: break
                if dif == 1:
                    q.append((w, tick+1))

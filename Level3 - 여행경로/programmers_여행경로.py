def solution(tickets):
    answer = []
    stack = []
    visit = []
    stack.append(['ICN', tickets, ['ICN']])
    while stack:
        node = stack.pop()
        if len(node[1]) == 0:
            visit.append(node[2])
        for t in range(len(node[1])):
            if node[1][t][0] == node[0]:
                ti = node[1][:t] + node[1][t+1:]
                stack.append([node[1][t][1], ti, node[2]+[node[1][t][1]]])
    visit = sorted(visit)
    return visit

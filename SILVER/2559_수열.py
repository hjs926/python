N, K = map(int, input().split())
tem_list = list(map(int, input().split()))

result_list = []
for i in range(len(tem_list)):
    if i + K - 1 == len(tem_list) - 1:
        result_list.append(sum(tem_list[i:i+K]))
        break
    result_list.append(sum(tem_list[i:i+K]))

print(max(result_list))
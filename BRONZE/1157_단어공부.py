# word_list에 단어들을 담아주는데 이때 set라는 함수를 사용했다
# set함수는 중복되는 값을 제거하는 함수이기 때문에 
# 이후에 cnt에 각각의 단어들의 개수를 count로 세어 담아주고 
# 개수의 값들을 count_list에 담아준다
# 이후 count_list의 최대값의 개수가 1개를 초과한다면 ?를 출력해주고
# 그렇지 않으면 count_list 최대값의 index를 구한 후 
# word_list에 출력해주는 식으로 마무리한다
word = input().upper()
word_list = list(set(word)) 
count_list = []

for i in word_list:
    cnt = word.count(i)
    count_list.append(cnt)
    
if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(word_list[max_index])
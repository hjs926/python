n=int(input())
people = [input().split()for _ in range(n)]
print(people)
people.sort(key=lambda x:x[0])
print(people)
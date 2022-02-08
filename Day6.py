#두수의 비교
'''
a = 3
b = 2
if a>b:
    print('a가 크다.')
elif a<b:
    print('b가 크다.')
else:
    print('a,b는 같다.')

# https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day6.drawio#R3VlNd6MgFP01LNvjd3VZjTNdtKsuOrs5qESdweAh2CT99QOKMUrT2DNtSLvxwH0gcLmP90RgR9X2J4V18UAyhIFlZFtgL4Bl3QQefwpg1wGOZ3RATsusg8wBeCxfkAT7Zk2ZofWoISMEs7IegylZrVDKRhiklGzGzZYEj0etYY4U4DGFWEWfyowVHepbNwN%2Bh8q86Ec2vaCzVLBvLFeyLmBGNgeQHQM7ooSwrlRtI4QFdz0vXb8fR6z7iVG0YnM6lJF9%2B%2FLrwb6DzdasPffpijVXplzHM8SNXLGcLdv1FKCMMyKrhLKC5GQFcTygISXNKkNiHIPXhjb3hNQcNDn4BzG2k9sLG0Y4VLAKS2s3phjo6OIktCYNTdFbK5IigTRH7K121n4PuHYRqRCjO96RIgxZ%2BTyeCJQqyvftBqJ5QXL9Ht4V2iGIIxAEwOe7aCQgDsGtC0L%2BdqM1xMB3W9AQ%2BHSLhg0QbG6KkqHHGrY8bbhbvkb2M6IMbd%2BmW2VHdnCkpqVTW4asbwYXMXvdFwfu0ff7cD6tGTLGmB8a6Cz8uNaYIEc3P%2FZpfvj5VItiRtKmatd5iqikU9198onM7WnSRp0zgzpGyd99fLDGLPW8VttcRMjrJSabtICUXWN%2BPP7GZVUe4%2FoD%2BPT8C1Oie5pOWpAqadZn8dQpP%2Fr15qkE8XM%2FMEFgiEJoixDBQ4Lvg8BvY8NCFKzW6i9AaEgwdEC8AL4jEGG9BaHbvmQh4ozo8j9RZFliHBFMaNvXXi6Rl6ZC7q0vHFiymyAxjE%2BJO9rFbL6yWV87fZL54On06fV9Ok%2F2pCataz5hpjXkO5d2jlhqjvnFtenP1aarU5y%2BQvs0tY9A6IEgOp7OX0YqNlG0q13R5gxFn%2FtLyPYuLSSp%2Bvvibm9ac%2F3e1un3%2FTQPiOcRyYOVEB0WPnwFtct1%2BuHua5dr8O3kas%2BVq6NVruqVAJzINbk0ue4PW31JlfHt5OrMlKuvVa3qLUwyUaua%2FmtWq6M%2FF1AvW9AqUwWr7zPJ%2B8SbY14d%2Fq60toNfVHb8Dw%3D%3D
'''
arr = [12,13,11,15,10]
max = arr[0]

for i in arr:
    if i > max:
        max = i

print(max)
'''
유명한 알고리즘
기본적인 처리 절차를 가지고있는 좋은 알고리즘이다.
좋은 프로그램을 만들기 위한 사고방식이나 힌트가 많이 포함되어있다.

탐색 Search
Liner Search 선형탐색 - 앞에서부터 순서대로 찾는다.
Binary Search 이진탐색법 - 범위를 절반식 줄여서 찾는다.
Hash Search 해시탐색법 - 검색 즉시 찾는다. 단, 저장할떄 가공해서 저장한다.

정렬 Sort
Selection Sort 단순 선택법 - 최소/최대값을 선택하여 앞/뒤로부터 순서대로 나열한다.
Bubble Sort 단순교환법 - 옆에 있는 데이터를 교환하면서 자리를 바꾼다.
Insertion Sort 단순 삽입법 - 데이터를 올바른 위치에 삽입하면서 자리를 바꾼다.
Quick Sort 퀵정렬 - 기준 데이터를 기반으로 대소 분할을 반복하여 자리를 바꾼다.

에라토스테네스의 체 Sieve of Eratosthenes - 소수 구하는 알고리즘
유클리드 알고리즘 - 최대 공약수를 구하는 알고리즘.
'''
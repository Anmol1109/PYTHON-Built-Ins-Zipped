# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int,input().split())

s = []
for _ in range(x):
    s.append(map(float,input().split()))
    
for i in zip(*s):
    print(sum(i) / len(i))

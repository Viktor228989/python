input()
s = input()
a = s.count('A')
d = s.count('D')
if a > d:
    print('Anton')
elif d == a:
    print("Friendship")
else:
    print("Danik")
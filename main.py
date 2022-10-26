import time

# mat = [
#     [0,1,2],
#     [3,4,5],
#     [6,7,8]
# ]

# def snail(mat):
#     ans = []
#     while len(mat)!=0:
#         ans+=mat[0]
#         del mat[0]
#         mat = list(zip(*mat))
#         mat.reverse()
#     return ans

# print(snail(mat))

s = 'AaabBB'
initial_time = time.time()
import string
def count_dublicates(string_1):
    string_1 = string_1.upper()
    s = string.ascii_uppercase
    for i in s:
        if i in string_1:
            id = string_1.index(i)
            string_1 = string_1[0:id]+string_1[id:]
    return len(set(string_1))

print(count_dublicates(s))
print(time.time()-initial_time)

def c_d(s):
    return len([ch for ch in(set (s.lower())) if s.lower().count(ch) >1])
initial_time = time.time()
c_d(s)
print(time.time()-initial_time)
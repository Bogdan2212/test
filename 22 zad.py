#1-36 и 43
f = open("22f").read().split("\n")
m = {}
for i in f:
    s = i.split('\t')
    if s[2] == '0':
        m[s[0]] = int(s[1])
    else:
        s[2] = s[2].replace(' ' , '')
        w = s[2].split(";")
        sp = []
        for j in w:
            sp.append(int(m[j]))
        m[s[0]] = int(s[1]) + max(sp)
print(max(m.values()))
print(m)

# 37 - 38
# f = open("22f").read().split("\n")
# m = {}
# # print(f)
# for i in f:
#     s = i.split('\t')
#     if len(s) == 2:
#         m[s[0]] = int(s[1])
#     else:
#         w = s[2].split(";")
#         sp = []
#         for j in w:
#             j = j.replace(" ", "")
#             sp.append(int(m[j]))
#         m[s[0]] = int(s[1]) + max(sp) + 3
# print(max(m.values()))
# print(m)

#39 - 40
# f = open("22f").read().split("\n")
# m = {}
# # print(f)
# for i in f:
#     s = i.split('\t')
#     if s[2] == '0':
#         m[s[0]] = int(s[1])
#     else:
#         w = s[2].split(";")
#         sp = []
#         for j in w:
#             j = j.replace(" ", "")
#             sp.append(int(m[j]))
#         m[s[0]] = int(s[1]) + max(sp)
# print(m)
#
#
# k = 0
# for item in m.values():
#     if item <= 120:
#         k+=1
# print(k)

#41-42
# f = open("22f").read().split("\n")
# m = {}
# # print(f)
# for i in f:
#     s = i.split('\t')
#     if s[2] == '0':
#         m[s[0]] = int(s[1])
#     else:
#         w = s[2].split(";")
#         sp = []
#         for j in w:
#             j = j.replace(" ", "")
#             sp.append(int(m[j]))
#         m[s[0]] = int(s[1]) + max(sp)
# print(m)
#
#
# f1 = open("22f").read().split("\n")
# m1 = {}
# for i in f1:
#     s = i.split('\t')
#     m1[s[0]] = int(s[1])
# print(m1)
#
#
# k = 0
# for item in m.keys():
#     if m[item] >= 150 and (m[item] - m1[item]) <= 150:
#         k += 1
#
# print(k)

#45
# f = open("22f").read().split("\n")
# m = {}
# for i in f:
#     s = i.split('\t')
#     if s[2] == '0':
#         m[s[0]] = int(s[1])
#     else:
#         w = s[2].split(";")
#         sp = []
#         for j in w:
#             j = j.replace(" ", "")
#             sp.append(int(m[j]))
#         m[s[0]] = int(s[1]) + max(sp)
# print(m)
# m_sort = dict(sorted(m.items() , key=lambda x: x[1]))
# print(m_sort)
#
# k = 0
# for item in m_sort.items():
#     k += 1
#     if k == 70:
#         print(item)
#         break


#47-50
f = open("22f").read().split("\n")
m = {}

mm = -1
for t in range(1,100):
    for i in f:
        s = i.split('\t')
        if s[2] == '0':
            m[s[0]] = int(s[1])
        else:
            w = s[2].split(";")
            sp = []
            for j in w:
                j = j.replace(" ", "")
                sp.append(int(m[j]))
            if s[1] == 't':
                m[s[0]] = int(t) + max(sp)
            else:
                m[s[0]] = int(s[1]) + max(sp)
    if max(m.values()) <= 19:
        mm = max(mm , t)
print(mm)


51-52
f = open("22f").read().split("\n")
m = {}
# print(f)
for i in f:
    s = i.split('\t')
    if s[2] == '0':
        m[s[0]] = int(s[1])
    else:
        w = s[2].split(";")
        sp = []
        for j in w:
            j = j.replace(" ", "")
            sp.append(int(m[j]))
        m[s[0]] = int(s[1]) + max(sp)
print(m)

f1 = open("22f").read().split("\n")
m1 = {}
for i in f1:
    s = i.split('\t')
    m1[s[0]] = int(s[1])
print(m1)

for item in m1.keys():
    m[item] -= m1[item]

k = 0
for i in m.values():
    if i >= 80:
        k+=1

print(k)


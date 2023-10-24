def is_subset(s, t):
    s_index = 0
    for c in t:
        if s_index < len(s) and s[s_index] == c:
            s_index += 1

    return s_index == len(s)


s1 = "ace"
t1 = "abcde"
print(is_subset(s1, t1))

s2 = "met"
t2 = "stream"
print(is_subset(s2, t2))

s3 = "stem"
t3 = "stream"
print(is_subset(s3, t3))

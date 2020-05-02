def stringSimilarity(s):
    s_list = []
    sum = []
    final_sum = 0
    count = 0
    for m in range(len(s)):
        s_list.append(s[m:])
    print(s_list)
    for i in range(len(s_list)):
        #print(i)
        count = 0
        str = s_list[i]
        if s[0] == str[0]:
            count += 1
            for j in range(1, len(s_list[i])):
                #str = s_list[i]
                    if s[j] == str[j]:
                        count += 1
                    else:
                        break
                        #print(count)
            print(count)
        final_sum = final_sum + count
    print(final_sum)

s = 'abcabccba'
(stringSimilarity(s))
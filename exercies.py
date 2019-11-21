def xor(a,b):
    return (a and (not b)) or ((not a) and b)

def ex13(num):

def ex12(letter1, letter2):
    print(letter1.upper())
    print(letter2.isdigit())

def ex14():
    str1 = "seehemewe"
    print(str1[:3])
    print(str1[3:5])
    print(str1[5:7])
    print(str1[-2:])
    print(str1[3:6])
    print(str1[-4:-7:-1])
    print(str1[1:8:3][::-1])

def ex15(palindrom):
    print((palindrom == palindrom[::-1]))

def ex19():
    line1 = '+' + '-'*43 + '+'
    line2 = "+{0}+{1}+{1}+{1}+{1}+".format('-'*15,'-'*6)
    header1 = "|{0:^43}|".format("Cereal Yields (kg/ha)")
    fmt_center = "|{0:^15}|{1:^6}|{2:^6}|{3:^6}|{4:^6}|"
    fmt_left = "|{0:<15}|{1:^6}|{2:^6}|{3:^6}|{4:^6}|"
    header2 = fmt_center.format("Country",1980,1990,2000,2010)
    china = fmt_left.format("China",2937,4321,4752,5527)
    germany = fmt_left.format("Germany", 2937, 4321, 4752, 5527)
    us = fmt_left.format("United States", 2937, 4321, 4752, 5527)
    print(line1,header1,line2,header2, line2,china,germany,us,line2,sep='\n')

def ex20(sentence):
    print(' '.join(sentence.split()[::-1]))

def ex23(year):
    if year % 4 == 0 and year % 400 == 0:
        print('Leap year')
    else:
        print('No leap year')

def ex25(n):
    a,b = 1,1
    for i in range(n):
        print(a, end= " ")
        a,b = b, a+b

def rank(lst):
    rank_list =[]
    sort_list = sorted(lst)
    # for grade in zip(sort_list,sort_list[1:]):

    return rank_list

def q5(A,S):
    res = []
    if sum(A) == S:
        return res.append(A)

    for i in range(len(A)):
        lst = [A[i]]
        for j in range(i+1, len(A)):
            lst.append(q5(A[i+1:], S- A[i]))

    return res

def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


if __name__ == '__main__':
    # ex12('t','8')
    # ex14()
    # ex15("rbr")
    # ex19()
    # ex20("An apple a day keeps the doctor away")
    # ex23(1600)
    # ex25(20)
    # grade_list = [56,70,56,43,98,100,40]
#     # grade_list.sort()
#     # test = zip(grade_list, grade_list[1:])
#     # print (list(test))
    print(xor(False,False))
    print(xor(False, True))
    print(xor(True, False))
    print(xor(True, True))

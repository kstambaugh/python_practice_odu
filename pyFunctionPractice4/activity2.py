# ----------------- find max number -----------------------


def max_num(a, b, c):
    myNums = [a, b, c]
    return max(myNums)


newNum = max_num(3, 23, 60)

print(newNum)

# ----------------- muliply numbers in list -----------------------


def mult_list(varlist):
    myTotal = 1
    for i in varlist:
        myTotal *= i
    return myTotal


multiplyList = [1, 2, 3, 4, 5, 6, 7, 8]

myMulti = mult_list(multiplyList)

print(myMulti)


# ----------------- reverse a string -----------------------

revWord = "Hello World"


def rev_string(stringinput):
    return stringinput[::-1]


newRevWord = rev_string(revWord)

print(newRevWord)

# ----------------- check if num is in range --------------------


def num_within(num, start, end):
    if start > end:
        if num <= start and num >= end:
            return True
        else:
            return False

    if num >= start and num <= end:
        return True
    else:
        return False


print(num_within(7, 22, 9))


# --------------------- pascal's triangle ----------------------

triangle = [[1], [1, 1]]


def pascal(n):
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(
                        triangle[row_number - 1][i - 1] + triangle[row_number - 1][i]
                    )
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)


pascal(6)

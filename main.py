import time
import itertools
import math

# n = int(input())
b = input()
# t1 = input()
# t2 = input()


def collatz(n1):
    if n1 == 1:
        return
    if n1 % 2 == 0:
        n2 = int(n1/2)
        print("n = " + str(n2))
        collatz(n2)
    else:
        n2 = int((3*n1+1)/2)
        print("n = " + str(n2))
        collatz(n2)


def previous_odd(z1):
    try:
        if z1 % 3 == 0:
            print("No previous odd numbers")
            return
    finally:
        for x in itertools.count(1,):
            if ((2**x * z1)-1) % 3 == 0:
                z2 = int(((2**x * z1)-1) / 3)
                print("z = " + str(z2))
                previous_odd(z2)


def binary_collatz(b1, count1, max_b1_length, b4, power_3, power_2, complete_index):
    count2 = count1 + 1
    if len(b1) > max_b1_length:
        max_b1_length2 = len(b1)
    else:
        max_b1_length2 = max_b1_length
#     print("b1 length:                       " + str(len(b1)))
#     zero_count = 0
#     for i in b1:
#         if i == "0":
#             zero_count += 1
#     print("b1 zero count                    " + str(zero_count))
#     one_count = 0
#     for i in b1:
#         if i == "1":
#             one_count += 1
#     print("b1 one count                     " + str(one_count))
    if b1 == 1 or b1 == "":
        print("no proof of convergence for numbers ending in: " + b4 + "\n")
        return
    while b1[-1] == "0":  # removing all leading zeros makes it odd
        b1 = b1[:-1]
#     print("odd number:                      " + b1)
#     if zero_count != 0:
#         print("1 to 0 ratio:                    " + str(round(one_count/zero_count, 2)))
    if b1 == "1":         # collatz complete if input goes to 1
#         print("b1 max length:                   " + str(max_b1_length2))
#         print("iterations to reduce:            " + str(complete_index))
#        print("")
        return
    b2 = b1 + "0"         # to 3x we double it and it initial value, this step doubles b1
    b3 = binary_add(b1, b2)
    b3 = binary_add(b3, "1")  # b3 is now next even
    power_3 += 1
#     print("next even number:                " + b3)
    while b3[-1] == "0":  # removing all leading zeros makes it odd
        b3 = b3[:-1]
        power_2 += 1
#     print("original number:                 " + b4)
#     print("next odd number:                 " + b3)
#     print("powers:                          " + "3^" + str(power_3) + " , 2^" + str(power_2))
#     print("power ratio:                     " + str(round(3**power_3/2**power_2, 5)))
#     print("Number of steps so far           " + str(count2))
    if 3**power_3/2**power_2 < 1 and complete_index == 0:
        complete_index = count2
        print("collatz complete for strings ending in: " + b4)             # theses four lines are for string testing
        print("iterations to reduce:            " + str(complete_index))
        print("power ratio:                     " + str(round(3**power_3/2**power_2, 5)))
        print("powers:                          " + "3^" + str(power_3) + " , 2^" + str(power_2))
        print("")
        return
    b3 = b3[1:]
    binary_collatz(b3, count2, max_b1_length2, b4, power_3, power_2, complete_index)


def binary_add(a, c):
    max_len = max(len(a), len(c))
    a = a.zfill(max_len)
    c = c.zfill(max_len)

    # Initialize the result
    result = ''

    # Initialize the carry
    carry = 0

    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if c[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        # Compute the carry.
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)


# previous_odd(n)

# collatz(n)
start_time = time.time()
binary_collatz(b, 0, 0, b, 0, 0, 0)

# binary_add(t1, t2)




print("--- %s seconds ---" % (time.time() - start_time))

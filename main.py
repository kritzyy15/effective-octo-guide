# GcdSolution, ArmstrongSolution, LCMSolution, Divisors
# from math_utils import Prime

# PrintName, PrintNum, PrintNumReverse, PrintSum, Factorial
# from recursion import ReverseArray

from hash import CountFrequencies

if __name__ == "__main__":
    # gcd = GcdSolution()
    # arm = ArmstrongSolution()
    # lcm = LCMSolution()
    # div = Divisors()
    # prime = Prime()
    # name = PrintName()
    # num = PrintNum()
    # reverse_num = PrintNumReverse()
    # sum = PrintSum()
    # fact = Factorial()
    # r_arr = ReverseArray()
    c_freq = CountFrequencies()

    # print(gcd.GCD(48, 18))
    # print(arm.isArmstrong(123))
    # print(lcm.LCM(48, 18))
    # print(div.divisors(8))
    # print(prime.isPrime(11))
    # name.printName(1, 3)
    # num.printNum(1,5)
    # reverse_num.printNumReverse(5, 1)
    # print(sum.printSum(5))
    # print(fact.factorial(3))

    # arr = [1, 2, 3, 4, 5]
    # r_arr.reverse_arr(arr, 0, len(arr) - 1)
    # print(arr)

    arr = [1, 2, 2, 1, 3]
    print(c_freq.countFrequencies(arr))

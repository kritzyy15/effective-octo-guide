from math_utils import GcdSolution, ArmstrongSolution

if __name__ == "__main__":
    gcd = GcdSolution()
    arm = ArmstrongSolution()

    print(gcd.GCD(48, 18))
    print(arm.isArmstrong(123))
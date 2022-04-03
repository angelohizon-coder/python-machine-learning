def testCases(N, Ncounter):
    if N == 0:
        #recursive function base case
        return
    X = int(input("Enter the number of X value: "))

    if X <= 0 or X > 100:
        print("Wrong input of the X value, 0 < X <= 100")

    #{} serves as a placeholder for the function format
    print("Sum of Square for #{} test case: ".format(Ncounter), sumOfSquare(X, 1),"\n")
    testCases(N-1, Ncounter+1)

def sumOfSquare(X, Xcounter):
    if X == 0:
        #recursive function base case
        return 0
    Yn = int(input("Enter the number Y{} value: ".format(Xcounter)))

    if Yn < -100 or Yn > 100:
        print("Wrong input of Yn value, -100 <= Yn <= 100")
    
    if Yn <= 0:
        return sumOfSquare(X-1, Xcounter+1)
    return sumOfSquare(X-1, Xcounter+1) + Yn * Yn

def main():
    N = int(input("Enter the number of test cases: "))
    #Invalid input since the N value requires it to be within the inclusion of 1 and 100
    if N < 1 or N > 100:
        print("Wrong input of the N value, 1 <= N <= 100")
    else:
        testCases(N, 1)
    

main()




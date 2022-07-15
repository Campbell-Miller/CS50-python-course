def main():
    x = int(input("Input the KG as an integer "))
    print("The input converted to Joules is ", convert(x))

def convert(n):
    return int(10 ** 16 * 9 * n)

main()
# Multiplication table printer - working with .format

def multi_table(a):
    for i in range(1, 11):
        print("{} x {} = {}".format(a, i, a*i))

if __name__ == "__main__":
    a = input("Enter a number: ")
    multi_table(float(a))

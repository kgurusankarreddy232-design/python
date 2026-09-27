i=1
# while i<=10:
#     print(i)
#     i=i+1

# n=4
# f=1
# i=1
# while i<=n:
#     f=f*i
#     i=i+1
# print(f)

# i=2
# while i<=50:
#     print(i)
#     i=i+2

# n=int(input("ENTER THE VALUE:"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i=i+1

# n = int(input("Enter n: "))
# i = 2

# while i < n:
#     if n % i == 0:
#         print("Not Prime")
#         break
#     i += 1
# else:
#     print("Prime")



# n = int(input("Enter number: "))

# ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# if n < 10:
#     print(ones[n])
# else:
#     print("Use ones/tens logic")


# s = input("Enter string: ")
# i = len(s)-1

# while i >= 0:
#     print(s[i], end="")
#     i -= 1

# n = int(input("Enter binary: "))
# d = 0
# p = 1

# while n > 0:
#     r = n % 10
#     d += r * p
#     p *= 2
#     n //= 10

# print(d)

n = int(input("Enter n: "))
i = 2

while i > 1:
    if n % i == 0:
        print(i)
        n //= i
    else:
        i += 1
# 1-amaliy
# numbers = 20
# while numbers < 30 + 1:
#     print(numbers)
#     numbers = numbers + 1



# 2-amaliy
# s = 'Hello world!'
# l = 0
# while l < len(s):
#     print(s[l])
#     l = l + 1



# 3-amaliy
# a = input('Ismingizni kiriting: ')
# m = 1
# while m < len(a):
#     print(a[m])
#     m = m + 2



# 4-amaliy
# i = 0
# while i < 10:
#     if i == 4:
#         break
#     print(i)
#     i += 1



# 5-amaliy
# a = int(input('a sonni kiriting: '))
# b = int(input('b sonni kiriting: '))
# c = 0
# while a < b:
#    c = c + a
#    a = a + 1
# print(c)



# 6-amaliy
# a = int(input('a kesmani kiriting: '))
# b = int(input('b kesmani kiriting: '))
# c = 0
# while a > b:
#  a = a - b
#  c += 1
# print(a)



# while masalalari
# 1-masala
# A = int(input("A = "))
# B = int(input("B = "))
# primes = [2, 3, 5, 7, 11, 13, 17, 19]
# factors_A = {}
# factors_B = {}
# for p in primes:
#   power_A = 0
#   while A % p == 0:
#     power_A += 1
#     A //= p
#   factors_A[p] = power_A
#   power_B = 0
#   while B % p == 0:
#     power_B += 1
#     B //= p
#   factors_B[p] = power_B
# gcd = 1
# lcm = 1
# for p in primes:
#   gcd *= p ** min(factors_A[p], factors_B[p])
#   lcm *= p ** max(factors_A[p], factors_B[p])
# n = lcm // gcd
# r = A - n * B
# print("A kesmada B kesmani", n, "marta joylashtirish mumkin")
# print("Bo'sh qism uzunligi", r)



# 2-masala
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
# if A <= B:
#     print("Xatolik! A soni B sonidan katta bo'lishi kerak.")
# else:
#     C = A - B
#     D = C // B
#     E = C % B
#     if E > 0:
#         D += 1
#     print(f"A ustunlikdagi kesmada B kesmadan {D} ta joylashtirish mumkin.")



# 3-masala
# N = int(input('N sonini kiriting: '))
# K = int(input('K sonini kiriting: '))
# qoldiq = N % K
# butun = N // K
# print("Qoldiq:", qoldiq)
# print("Butun:", butun)



# 4-masala
# N = int (input ("N sonini kiriting: "))
# if N <= 0:
#     print ("N soni musbat bo'lishi kerak")
# elif pow (3, -4) % N == 0:
#     print ("3 - ning darajasi")
# else:
#     print ("3 - ning darajasi emas")



# 5-masala
# n = int(input("n sonini kiriting: "))
# k = 0
# while n > 1 and n % 2 == 0:
#     n = n // 2
#     k = k + 1
# if n == 1:
#     print("k =", k)
# else:
#     print("n soni 2 ning darajasi emas")



# 6-masala
# n = int(input("n sonini kiriting: "))
# def double_factorial(n):
#   if n == 0 or n == 1:
#     return 1
#   else:
#     return n * double_factorial(n-2)
# print("n!! =", double_factorial(n))



# 7-masala
# N = int(input("N sonini kiriting: "))
# K = N//2
# bosh = 1
# oxir = N
# while bosh < oxir - 1:
#   orta = (bosh + oxir) // 2
#   if orta**2 > N:
#     oxir = orta - 1
#   else:
#     bosh = orta + 1
# if bosh**2 > N:
#   K = bosh
# else:
#   K = oxir
# print("K soni:", K)



# 8-masala
# N = int(input('N sonini kiriting: '))
# K = N
# while K**2 > N:
#     K = K - 1
# print(K)



# 9-masala
# n = int(input("N natural sonini kiriting: "))
# k = 0
# while 3**k <= n:
#     k = k + 1
# print("3K > N shartni qanoatlantiruvchi eng kichik butun K soni:", k)



# 10-masala
# n = int(input("N natural sonini kiriting: "))
# k = 0
# while 3**k <= n:
#     k = k + 1
# print("3K <= N shartni qanoatlantiruvchi eng katta butun K soni:", k - 1)
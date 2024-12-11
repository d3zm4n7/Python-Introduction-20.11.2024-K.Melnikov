# # Ülesanne 2.   Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
# while True:
#     try:
#         A=int(input("Sisesta A:"))
#         break
#     except:
#         print("On vaja naturaalne arv")
# summa=0
# if A > 0:
#     for i in range(1,A+1,1):
#         summa+=i                #summa=summa+i
#         print(f"{i}. samm summa={summa}")
#     print(f"Vastus {summa}")

# # Ülesanne 3.   Вводят 8 чисел. Найти их произведение (только положительных).
# p=1
# for j in range(8):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {j+1} arv: "))
#             break
#         except:
#             print("On vaja arv")
#     if arv>0: 
#         p*=arv #если число положительное то умнажай на "arv", если нет, то нечего не будет
#     else:
#         print("Korrutame arvud rohkem kui 0")
#     print(f"{j+1}. samm korrutis= {p}")
# print(f"Lõpptulemus on {p}")

# # Ülesanne 4.    Составьте программу, выводящую на экран квадраты чисел от 10 до 20.

# for i in range(10,21,1):
#     print(i**2, end=";")

# print()

# # Ülesanne 16.  Напишите программу, печатающую столбик строк такого вида:
# for j in range(1,10):
#     for i in range(1,10):
#         if i==j: 
#             print(j, end=".")
#         else:
#             print("0", end=".")
#     print()

# # Ülesanne 15.    Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде

# for read in range(10):
#     for rida in range(10):
#         print(rida, end=" ") #print("{:>3}.format(rida**2), end="") для матрицы в cmd
#     print()
# print()

# Ülesanne 30.    В программе создаются 2 случайных числа M и N. И выводятся на экран в срочку 2 последовательности от N к M, и обратно.
from random import *
M=randint(1,100)
N=randint(1,100)
print(f"{N} and {M}")
for M in range(M,N):
    for N in range(N,M):
        print('{:>3}'.format(N**2), end="")
        print()
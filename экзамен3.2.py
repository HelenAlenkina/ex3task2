#2. Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrom(a):

    return a[::-1] == a

while True:
    a = input("Введите слово: ")
    print(f"{a} является палиндромом!" if palindrom(a)
          else "не является палиндромом!")
    break

#или (не через функцию)
s = input("Введите слово: ")

if s == s[::-1]:
    print("Это слово- палиндром")
else:
    print("Это слово - не палиндром")
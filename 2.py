def palindrome(a):
    data = a.replace(' ','').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'
print(palindrome('Спел лепс'))
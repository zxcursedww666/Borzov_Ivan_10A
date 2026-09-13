a = "Neo_2088"
b = "FollowTheWhiteRabbit"
print("Введите логин >>")
c = input()
print("Введите пароль >>")

d = input()
tryd = 2
flag = 0

if c != a:
    print(f"ДОСТУП ЗАПРЕЩЕН: Пользователь {c} не найден в системе.")
else:
    while tryd != -1:
        if d != b:
            print("ОШИБКА АУТЕНТИФИКАЦИИ: Неверный пароль!")
            print(f"Попыток осталось: {tryd}")
            tryd = tryd - 1
            d = input()
        if d == b:
            flag = 1
            break
        if tryd == 0 and d != b:
            print("ОШИБКА АУТЕНТИФИКАЦИИ: Попытки закончились!")
            print("ТЕРМИНАЛ ЗАБЛОКИРОВАН!")
            break

if flag == 1 and c == a:
    print(f"ДОСТУП РАЗРЕШЕН: Добро пожаловать, {c}!")
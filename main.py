print("Введите количество кредитов:")
a = float(input())
U = 1.25
E = 1.15
dollar = a * U
evro = a * E
if a == int(a):
    a_str = f"{a:.1f}"
else:
    a_str= f"{a}"
if dollar == int(dollar):
    print(f"{a_str} кредитов = {dollar:.1f} $")
else:
    print(f"{a_str} кредитов = {dollar:.2f} $")
if evro == int(evro):
    print(f"{a_str} кредитов = {evro:.1f} €")
else:
    print(f"{a_str:} кредитов = {evro:.2f} €")
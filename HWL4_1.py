# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, production, time_rate, plan_execution = argv
c_salary = int(production)*int(time_rate)
bonus = c_salary*int(plan_execution)/100
if int(plan_execution) >= 100:
    print(f'Выработка в часах {production} * '
          f'ставка в час {time_rate} + '
          f' премия {bonus} = {c_salary+bonus}')
else:
    print(f'Выработка в часах {production} * '
          f'ставка в час {time_rate} + '
          f' премия {0} = {c_salary}')



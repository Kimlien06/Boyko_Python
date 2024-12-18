# Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч
# (U < V). Время движения лодки по озеру T1 ч, а по реке (против течения) — T2 ч. Определить
# путь S, пройденный лодкой (путь = время • скорость). Учесть, что при движении против
# течения скорость лодки уменьшается на величину скорости течения.

V = float(input("Введите скорость лодки (км/ч): "))
U = float(input("Введите скорость течения реки (км/ч): "))
T1 = float(input("Введите время движения лодки по озеру (ч): "))
T2 = float(input("Введите время движения лодки по реке (ч): "))

try:
    if V <= 0 or U <= 0 or T1 < 0 or T2 < 0 or U >= V:
        raise ValueError("Некорректные входные данные")

    speed_river = V - U

    speed_lake = V

    s = speed_river * T2 + speed_lake * T1

    print(f"Общий путь лодки составит {s} км")

except ValueError as e:
    print(f"Ошибка: {e}")

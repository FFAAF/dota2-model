import numpy as np
import matplotlib.pyplot as plt
import random

LEVEL_1 = 20
LEVEL_2 = 30
LEVEL_3 = 40
LEVEL_4 = 50

ROUND = 1000000


class Result:
    def __str__(self) -> str:
        return 'leftMana: %d, damage: %d' % (self.leftMana, self.damage)

    leftMana = 100.00
    damage = 0.00


def attack(mana, level):
    result = Result()
    result.leftMana = mana * 0.8
    result.damage = mana * 0.16
    if (random.randint(1, 10) < 4) and 1 or 0:
        result.leftMana += level
    return result


def get_result(level):
    mana_array = []
    damage_array = []
    mana = 100
    for i in range(ROUND):
        result = attack(mana, level)
        mana = result.leftMana
        mana_array.append(mana)
        damage_array.append(result.damage)
    return {"mana": mana_array, "damage": damage_array}


def draw_lines(x, result, label, line_type, ):
    y = np.array(result.get("mana"))
    p = np.poly1d(np.polyfit(x, y, 4))
    print(p)
    yvals = p(x)
    # plt.plot(x, y, 'c.', label='left mana')
    plt.plot(x, yvals, line_type, label=label)


x = np.linspace(0, ROUND, ROUND)
draw_lines(x, get_result(LEVEL_1), "level-1", 'r')
draw_lines(x, get_result(LEVEL_2), "level-2", 'r--')
draw_lines(x, get_result(LEVEL_3), "level-3", 'r-.')
draw_lines(x, get_result(LEVEL_4), "level-4", 'r:')

plt.xlabel('attack time')
plt.ylabel('left mana')
plt.legend(loc=4)  # 指定legend的位置,读者可以自己help它的用法
plt.title('mana and level')
plt.show()

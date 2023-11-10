import random
import numpy as np

print(f"Introduzca la probabilidad de lluvia")
rain = int(input()) / 100
print(f"Introduzca la temperatura inicial")
temp = int(input())

prob = np.arange(0, 1, 0.01)

def temperature_predict(temp, rain, days):
    """
        Method to predict temperature based in temperature, rain and days introduced by the user.
        :param temp Temperature introduced by the user
        :param rain Rain introduced by the user
        :param days Days introduced by the user
        :return Returns the maximum and minimum temperature during those days, and which days rainy.
    """
    temp_list = []
    rain_days = []
    for day in range(0, days):
        random_prob = random.choice(prob)
        if random_prob <= 0.1:
            random_temp = random.choice(range(1, 2))
            if random_temp == 1:
                temp += 2
            else:
                temp -= 2
        if temp > 25:
            rain += 0.2
        if temp < 5:
            rain -= 0.2
        if rain == 1:
            temp -= 1
            rain_days.append(day)
        temp_list.append(temp)
        
    temp_min = min(temp_list)
    temp_max = max(temp_list)
    return temp_min, temp_max, rain_days

print(temperature_predict(temp, rain, 105))


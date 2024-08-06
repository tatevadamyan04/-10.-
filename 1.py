import scipy.stats as stats
import pandas as pd

# Данные роста
footballers = [173, 175, 180, 178, 177, 185, 183, 182]
hockey_players = [177, 179, 180, 188, 177, 172, 171, 184, 180]
weightlifters = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]

# Объединение данных в один DataFrame для удобства анализа
data = pd.DataFrame({
    'Height': footballers + hockey_players + weightlifters,
    'Sport': ['Footballer'] * len(footballers) + ['Hockey Player'] * len(hockey_players) + ['Weightlifter'] * len(weightlifters)
})

# Проведение однофакторного дисперсионного анализа
f_value, p_value = stats.f_oneway(footballers, hockey_players, weightlifters)

print(f'F-статистика: {f_value}')
print(f'p-значение: {p_value}')

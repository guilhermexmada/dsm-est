import pandas as pd 
import matplotlib.pyplot as plt 

os = [
    'windows', 'linux', 'macos', 'android', 'ios',
    'windows', 'linux', 'macos', 'android', 'ios',
    'windows', 'linux', 'macos', 'android', 'ios',
    'windows', 'linux', 'macos', 'android', 'ios',
    'windows', 'linux', 'macos', 'android', 'ios',
    'windows', 'linux', 'macos', 'android', 'ios',
    'windows', 'linux', 'macos', 'android', 'ios',
    'windows', 'linux', 'macos', 'android', 'ios',
    'windows', 'linux', 'macos', 'android', 'ios',
    'android', 'ios', 'android', 'ios', 'android',
    'windows', 'linux', 'windows', 'linux', 'windows',
    'windows', 'linux', 'windows', 'linux', 'windows',
    'windows', 'linux', 'windows', 'linux', 'windows',
]

series = pd.Series(os)

freq_abs = series.value_counts().sort_index()
perc = series.value_counts(normalize=True)

sys_freq_max = freq_abs.idxmax()
freq_max = freq_abs.max()

print(f'OS mais frequente: {sys_freq_max} | Ocorrências: {freq_max}')

freq_abs.plot(kind='bar')
plt.title('Distribuição dos sistemas operacionais')
plt.show()

freq_abs.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição dos sistemas operacionais')
plt.show()
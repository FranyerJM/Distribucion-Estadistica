import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametros
mu, sigma, n = 800, 40, 64
se = sigma / np.sqrt(n)  # Error estandar

# a) P(X̄ < 790)
prob_a = norm.cdf(790, mu, se)

# b) P(790 < X̄ < 810)
prob_b = norm.cdf(810, mu, se) - norm.cdf(790, mu, se)

# c) falta

# Grafico
x = np.linspace(mu - 4*se, mu + 4*se, 1000)
y = norm.pdf(x, mu, se)
plt.plot(x, y, 'b-')
plt.fill_between(x, y, where=(x < 790), color='red', alpha=0.3, label='P(X̄ < 790)')
plt.fill_between(x, y, where=(x >= 790) & (x <= 810), color='green', alpha=0.3, label='P(790 ≤ X̄ ≤ 810)')
plt.title('Distribución Muestral de la Media')
plt.xlabel('Horas de vida útil')
plt.ylabel('Densidad')
plt.legend()

print(f"a) P(X̄ < 790) = {prob_a:.4f}")
print(f"b) P(790 < X̄ < 810) = {prob_b:.4f}")
print(f"c) falta completar el inciso c")

plt.show()
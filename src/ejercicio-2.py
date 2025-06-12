import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametros
p, n = 0.35, 100
se_p = np.sqrt(p * (1 - p) / n)  # Error estandar

# a) P(p̂ < 0.30)
prob_a_p = norm.cdf(0.30, p, se_p)

# b) P(0.30 ≤ p̂ ≤ 0.40)
prob_b_p = norm.cdf(0.40, p, se_p) - norm.cdf(0.30, p, se_p)

# c) Falta

# Grafico
x_p = np.linspace(p - 4*se_p, p + 4*se_p, 1000)
y_p = norm.pdf(x_p, p, se_p)
plt.plot(x_p, y_p, 'b-')
plt.fill_between(x_p, y_p, where=(x_p < 0.30), color='red', alpha=0.3, label='P(p̂ < 0.30)')
plt.fill_between(x_p, y_p, where=(x_p >= 0.30) & (x_p <= 0.40), color='green', alpha=0.3, label='P(0.30 ≤ p̂ ≤ 0.40)')
plt.title('Distribución Muestral de la Proporción')
plt.xlabel('Proporción muestral')
plt.ylabel('Densidad')
plt.legend()

print(f"a) P(p̂ < 0.30) = {prob_a_p:.4f}")
print(f"b) P(0.30 ≤ p̂ ≤ 0.40) = {prob_b_p:.4f}")
print(f"c) Falta completar el inciso c")

plt.show()
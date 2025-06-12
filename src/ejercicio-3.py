import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros
mu_A, sigma_A, n_A = 120, 15, 50
mu_B, sigma_B, n_B = 115, 12, 50
se_diff = np.sqrt(sigma_A**2 / n_A + sigma_B**2 / n_B)  # Error estándar

# a) P(D > 8)
prob_a_diff = 1 - norm.cdf(8, mu_A - mu_B, se_diff)

# b) P(4 < D < 7)
prob_b_diff = norm.cdf(7, mu_A - mu_B, se_diff) - norm.cdf(4, mu_A - mu_B, se_diff)

# c) Intervalo del 90%
# z_critical_diff = norm.ppf(0.95)
# lower_diff = (mu_A - mu_B) - z_critical_diff * se_diff
# upper_diff = (mu_A - mu_B) + z_critical_diff * se_diff

# Gráfico
x_diff = np.linspace(-10, 20, 1000)
y_diff = norm.pdf(x_diff, mu_A - mu_B, se_diff)
plt.plot(x_diff, y_diff, 'b-')
plt.fill_between(x_diff, y_diff, where=(x_diff > 8), color='red', alpha=0.3, label='P(D > 8)')
plt.fill_between(x_diff, y_diff, where=(x_diff >= 4) & (x_diff <= 7), color='green', alpha=0.3, label='P(4 ≤ D ≤ 7)')
# plt.axvline(lower_diff, color='purple', linestyle='--', label='Límite inferior (90%)')
# plt.axvline(upper_diff, color='purple', linestyle='--', label='Límite superior (90%)')
plt.title('Distribución Muestral de la Diferencia de Medias')
plt.xlabel('Diferencia (X̄_A - X̄_B)')
plt.ylabel('Densidad')
plt.legend()


print(f"a) P(D > 8) = {prob_a_diff:.4f}")
print(f"b) P(4 < D < 7) = {prob_b_diff:.4f}")
# print(f"c) Intervalo 90%: [{lower_diff:.2f}, {upper_diff:.2f}] mg/dL")

plt.show()
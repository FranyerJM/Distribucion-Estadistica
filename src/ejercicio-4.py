import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametros
p_N, n_N = 0.48, 200
p_S, n_S = 0.42, 200
se_diff_p = np.sqrt(p_N*(1-p_N)/n_N + p_S*(1-p_S)/n_S)  # Error estandar

# a) P(D_p > 0.10)
prob_a_diff_p = 1 - norm.cdf(0.10, p_N - p_S, se_diff_p)

# b) P(D_p < 0.02)
prob_b_diff_p = norm.cdf(0.02, p_N - p_S, se_diff_p)

# c) falta

# Grafico
x_diff_p = np.linspace(-0.15, 0.25, 1000)
y_diff_p = norm.pdf(x_diff_p, p_N - p_S, se_diff_p)
plt.plot(x_diff_p, y_diff_p, 'b-')
plt.fill_between(x_diff_p, y_diff_p, where=(x_diff_p > 0.10), color='red', alpha=0.3, label='P(D_p > 0.10)')
plt.fill_between(x_diff_p, y_diff_p, where=(x_diff_p < 0.02), color='green', alpha=0.3, label='P(D_p < 0.02)')

plt.title('Distribución Muestral de la Diferencia de Proporciones')
plt.xlabel('Diferencia (p̂_N - p̂_S)')
plt.ylabel('Densidad')
plt.legend()

print(f"a) P(D_p > 0.10) = {prob_a_diff_p:.4f}")
print(f"b) P(D_p < 0.02) = {prob_b_diff_p:.4f}")
print(f"c) falta completar el inciso c")

plt.show()
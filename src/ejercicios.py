import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def ejercicio_1():
    # Parámetros
    mu, sigma, n = 800, 40, 64
    se = sigma / np.sqrt(n)  # Error estándar

    # a) P(X̄ < 790)
    prob_a = norm.cdf(790, mu, se)

    # b) P(790 < X̄ < 810)
    prob_b = norm.cdf(810, mu, se) - norm.cdf(790, mu, se)

    # c) P(X̄ > 815) [COMPLETADO]
    prob_c = 1 - norm.cdf(815, mu, se)

    # Gráfico
    x = np.linspace(mu - 4*se, mu + 4*se, 1000)
    y = norm.pdf(x, mu, se)
    plt.plot(x, y, 'b-')
    plt.fill_between(x, y, where=(x < 790), color='red', alpha=0.3, label='P(X̄ < 790)')
    plt.fill_between(x, y, where=(x >= 790) & (x <= 810), color='green', alpha=0.3, label='P(790 ≤ X̄ ≤ 810)')
    plt.fill_between(x, y, where=(x > 815), color='purple', alpha=0.3, label='P(X̄ > 815)')  # Nuevo
    plt.title('Distribución Muestral de la Media')
    plt.xlabel('Horas de vida útil')
    plt.ylabel('Densidad')
    plt.legend()

    print(f"a) P(X̄ < 790) = {prob_a:.4f}")
    print(f"b) P(790 < X̄ < 810) = {prob_b:.4f}")
    print(f"c) P(X̄ > 815) = {prob_c:.4f}")  # Completado

    plt.show()
    
def ejercicio_2():
    # Parámetros
    p, n = 0.35, 100
    se_p = np.sqrt(p * (1 - p) / n)  # Error estándar

    # a) P(p̂ < 0.30)
    prob_a_p = norm.cdf(0.30, p, se_p)

    # b) P(0.30 ≤ p̂ ≤ 0.40)
    prob_b_p = norm.cdf(0.40, p, se_p) - norm.cdf(0.30, p, se_p)

    # c) P(p̂ > 0.42) [COMPLETADO]
    prob_c_p = 1 - norm.cdf(0.42, p, se_p)

    # Gráfico
    x_p = np.linspace(p - 4*se_p, p + 4*se_p, 1000)
    y_p = norm.pdf(x_p, p, se_p)
    plt.plot(x_p, y_p, 'b-')
    plt.fill_between(x_p, y_p, where=(x_p < 0.30), color='red', alpha=0.3, label='P(p̂ < 0.30)')
    plt.fill_between(x_p, y_p, where=(x_p >= 0.30) & (x_p <= 0.40), color='green', alpha=0.3, label='P(0.30 ≤ p̂ ≤ 0.40)')
    plt.fill_between(x_p, y_p, where=(x_p > 0.42), color='purple', alpha=0.3, label='P(p̂ > 0.42)')  # Nuevo
    plt.title('Distribución Muestral de la Proporción')
    plt.xlabel('Proporción muestral')
    plt.ylabel('Densidad')
    plt.legend()

    print(f"a) P(p̂ < 0.30) = {prob_a_p:.4f}")
    print(f"b) P(0.30 ≤ p̂ ≤ 0.40) = {prob_b_p:.4f}")
    print(f"c) P(p̂ > 0.42) = {prob_c_p:.4f}")  # Completado

    plt.show()
    
def ejercicio_3():
    # Parámetros
    mu_A, sigma_A, n_A = 120, 15, 50
    mu_B, sigma_B, n_B = 115, 12, 50
    diff_mu = mu_A - mu_B  # Diferencia poblacional
    se_diff = np.sqrt(sigma_A**2 / n_A + sigma_B**2 / n_B)  # Error estándar

    # a) P(D > 8)
    prob_a_diff = 1 - norm.cdf(8, diff_mu, se_diff)

    # b) P(4 < D < 7)
    prob_b_diff = norm.cdf(7, diff_mu, se_diff) - norm.cdf(4, diff_mu, se_diff)

    # c) Intervalo del 90% [COMPLETADO]
    z_critical_diff = norm.ppf(0.95)  # Z para 90% confianza (cola superior 5%)
    lower_diff = diff_mu - z_critical_diff * se_diff
    upper_diff = diff_mu + z_critical_diff * se_diff

    # Gráfico
    x_diff = np.linspace(diff_mu - 4*se_diff, diff_mu + 4*se_diff, 1000)
    y_diff = norm.pdf(x_diff, diff_mu, se_diff)
    plt.plot(x_diff, y_diff, 'b-')
    plt.fill_between(x_diff, y_diff, where=(x_diff > 8), color='red', alpha=0.3, label='P(D > 8)')
    plt.fill_between(x_diff, y_diff, where=(x_diff >= 4) & (x_diff <= 7), color='green', alpha=0.3, label='P(4 ≤ D ≤ 7)')
    plt.axvline(lower_diff, color='purple', linestyle='--', label='Límite inferior (90%)')  # Nuevo
    plt.axvline(upper_diff, color='purple', linestyle='--', label='Límite superior (90%)')  # Nuevo
    plt.title('Distribución Muestral de la Diferencia de Medias')
    plt.xlabel('Diferencia (X̄_A - X̄_B)')
    plt.ylabel('Densidad')
    plt.legend()

    print(f"a) P(D > 8) = {prob_a_diff:.4f}")
    print(f"b) P(4 < D < 7) = {prob_b_diff:.4f}")
    print(f"c) Intervalo 90%: [{lower_diff:.2f}, {upper_diff:.2f}] mg/dL")  # Completado

    plt.show()
    
def ejercicio_4():
    # Parámetros
    p_N, n_N = 0.48, 200
    p_S, n_S = 0.42, 200
    diff_p = p_N - p_S  # Diferencia poblacional
    se_diff_p = np.sqrt(p_N*(1-p_N)/n_N + p_S*(1-p_S)/n_S)  # Error estándar

    # a) P(D_p > 0.10)
    prob_a_diff_p = 1 - norm.cdf(0.10, diff_p, se_diff_p)

    # b) P(D_p < 0.02)
    prob_b_diff_p = norm.cdf(0.02, diff_p, se_diff_p)

    # c) P(0.04 < D_p < 0.08) [COMPLETADO]
    prob_c_diff_p = norm.cdf(0.08, diff_p, se_diff_p) - norm.cdf(0.04, diff_p, se_diff_p)

    # Gráfico
    x_diff_p = np.linspace(diff_p - 4*se_diff_p, diff_p + 4*se_diff_p, 1000)
    y_diff_p = norm.pdf(x_diff_p, diff_p, se_diff_p)
    plt.plot(x_diff_p, y_diff_p, 'b-')
    plt.fill_between(x_diff_p, y_diff_p, where=(x_diff_p > 0.10), color='red', alpha=0.3, label='P(D_p > 0.10)')
    plt.fill_between(x_diff_p, y_diff_p, where=(x_diff_p < 0.02), color='green', alpha=0.3, label='P(D_p < 0.02)')
    plt.fill_between(x_diff_p, y_diff_p, where=(x_diff_p >= 0.04) & (x_diff_p <= 0.08), color='purple', alpha=0.3, label='P(0.04 ≤ D_p ≤ 0.08)')  # Nuevo
    plt.title('Distribución Muestral de la Diferencia de Proporciones')
    plt.xlabel('Diferencia (p̂_N - p̂_S)')
    plt.ylabel('Densidad')
    plt.legend()

    print(f"a) P(D_p > 0.10) = {prob_a_diff_p:.4f}")
    print(f"b) P(D_p < 0.02) = {prob_b_diff_p:.4f}")
    print(f"c) P(0.04 < D_p < 0.08) = {prob_c_diff_p:.4f}")  # Completado

    plt.show()

def main():

    print("Presione 1 para el Ejercicio 1")
    print("Presione 2 para el Ejercicio 2")
    print("Presione 3 para el Ejercicio 3")
    print("Presione 4 para el Ejercicio 4")
    print("")
    opcion = input("Ingrese su opción: ")
    if opcion == '1':
        ejercicio_1()
    elif opcion == '2':
        ejercicio_2()
    elif opcion == '3':
        ejercicio_3()
    elif opcion == '4':
        ejercicio_4()
    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 4.")

main()
print("")
print("Presione r para reiniciar el programa o cualquier otra tecla para salir.")
while input().lower() == 'r':
    main()
    print("")
    print("Presione r para reiniciar el programa o cualquier otra tecla para salir.")
    print("")
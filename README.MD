# 📊 Ejercicios Estadística II - Solución Manual Detallada

## 👥 Autores

| Estudiante         | Cédula      |
|--------------------|-------------|
| Franyer Marin      | 32.293.396  |
| Ricardo Alzurutt   | 25.971.680  |

---

## 🔬 Ejercicio 1: Distribución Muestral para la Media (Población Normal)

### 📝 Enunciado:
Una fábrica de componentes electrónicos produce resistencias con vida útil distribuida normalmente (μ = 800 horas, σ = 40 horas). Semanalmente se analiza una muestra de 64 resistencias para verificar cumplimiento de estándares. La gerencia requiere comprender el comportamiento estadístico de estas muestras.

### 🔍 Solución Manual:

#### a) Probabilidad de vida media < 790 horas
**Paso 1:** Calcular error estándar  
$$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{40}{\sqrt{64}} = \frac{40}{8} = 5$$

**Paso 2:** Calcular Z  
$$Z = \frac{\bar{X} - \mu}{\sigma_{\bar{X}}} = \frac{790 - 800}{5} = \frac{-10}{5} = -2.0$$

**Paso 3:** Buscar en tabla Z  
- P(Z < -2.0) = 0.0228 (área bajo curva normal estándar)

**📌 Conclusión:**  
Probabilidad = 0.0228 (2.28%)


---

#### b) Probabilidad entre 790 y 810 horas
**Paso 1:** Calcular Z para 810  
$$Z = \frac{810 - 800}{5} = \frac{10}{5} = 2.0$$

**Paso 2:** Buscar en tabla Z  
- P(Z < 2.0) = 0.9772  
- P(Z < -2.0) = 0.0228  

**Paso 3:** Calcular diferencia  
$$P(790 < \bar{X} < 810) = 0.9772 - 0.0228 = 0.9544$$

**📌 Conclusión:**  
Probabilidad = 0.9544 (95.44%)

---

#### c) Probabilidad de vida media superior a 815 horas
**Paso 1:** Calcular error estándar  
$$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{40}{\sqrt{64}} = 5$$

**Paso 2:** Calcular Z  
$$Z = \frac{\bar{X} - \mu}{\sigma_{\bar{X}}} = \frac{815 - 800}{5} = 3.0$$

**Paso 3:** Buscar en tabla Z  
- P(Z > 3.0) = 1 - \Phi(3.0) \approx 0.0013

**📌 Conclusión:**  
Probabilidad ≈ 0.0013 (0.13%). Valores tan extremos sugieren anomalías en el proceso o mediciones atípicas.



---

## 📈 Ejercicio 2: Distribución Muestral para la Proporción

### 📝 Enunciado:
Estudio en universidades estatales revela que 35% de estudiantes usa transporte público. Para evaluar políticas de movilidad, se encuestan grupos de 100 estudiantes en distintos campus.

### 🔍 Solución Manual:

#### a) Probabilidad de proporción muestral < 30%
**Paso 1:** Verificar normalidad  
$$np = 100 \times 0.35 = 35 \geq 5$$  
$$n(1-p) = 100 \times 0.65 = 65 \geq 5$$  
→ Se aproxima a normal  

**Paso 2:** Calcular error estándar  
$$\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.35 \times 0.65}{100}} = \sqrt{0.002275} \approx 0.0477$$

**Paso 3:** Calcular Z  
$$Z = \frac{\hat{p} - p}{\sigma_{\hat{p}}} = \frac{0.30 - 0.35}{0.0477} \approx -1.048$$

**Paso 4:** Buscar en tabla Z  
- P(Z < -1.05) ≈ 0.1469  

**📌 Conclusión:**  
Probabilidad ≈ 0.1469 (14.69%)

---

#### b) Probabilidad entre 30% y 40%
**Paso 1:** Calcular Z para 40%  
$$Z = \frac{0.40 - 0.35}{0.0477} \approx 1.048$$

**Paso 2:** Buscar en tabla Z  
- P(Z < 1.05) ≈ 0.8531  
- P(Z < -1.05) ≈ 0.1469  

**Paso 3:** Calcular diferencia  
$$P(0.30 < \hat{p} < 0.40) = 0.8531 - 0.1469 = 0.7062$$

**📌 Conclusión:**  
Probabilidad ≈ 0.7062 (70.62%)

---

#### c) Probabilidad de proporción muestral > 42%
**Paso 1:** Verificar normalidad  
$$np = 100 \times 0.35 = 35 \geq 5$$  
$$n(1-p) = 100 \times 0.65 = 65 \geq 5$$  
→ Aproximación válida

**Paso 2:** Calcular error estándar  
$$\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.35 \times 0.65}{100}} \approx 0.0477$$

**Paso 3:** Calcular Z  
$$Z = \frac{\hat{p} - p}{\sigma_{\hat{p}}} = \frac{0.42 - 0.35}{0.0477} \approx 1.47$$

**Paso 4:** Buscar en tabla Z  
- P(Z > 1.47) ≈ 1 - 0.9292 = 0.0708

**📌 Conclusión:**  
Probabilidad ≈ 0.0708 (7.08%). Esto indica que en ~7% de las muestras se sobreestimaría el uso real en ≥7 puntos porcentuales.

---

## ⚗️ Ejercicio 3: Diferencia de Medias (Dos Poblaciones)

### 📝 Enunciado:
Laboratorio farmacéutico compara antihipertensivos (Fármaco A: μ=120 mg/dL, σ=15; Fármaco B: μ=115 mg/dL, σ=12). Ensayo con 50 pacientes por grupo analiza diferencias en reducción de colesterol.

### 🔍 Solución Manual:

#### a) Probabilidad de diferencia > 8 mg/dL
**Paso 1:** Calcular diferencia poblacional  
$$\mu_A - \mu_B = 120 - 115 = 5$$

**Paso 2:** Calcular error estándar  
$$\sigma_{\bar{X}_A - \bar{X}_B} = \sqrt{\frac{\sigma_A^2}{n_A} + \frac{\sigma_B^2}{n_B}} = \sqrt{\frac{15^2}{50} + \frac{12^2}{50}} = \sqrt{4.5 + 2.88} \approx 2.717$$

**Paso 3:** Calcular Z  

$$\text{Numerador} = (\bar{X}_A - \bar{X}_B) - (\mu_A - \mu_B) = 8 - 5 = 3

$$\sigma_D = \sqrt{\frac{\sigma_A^2}{n_A} + \frac{\sigma_B^2}{n_B}} = \sqrt{\frac{15^2}{50} + \frac{12^2}{50}} = \sqrt{4.5 + 2.88} = \sqrt{7.38} \approx 2.717


$$Z = \frac{\text{Numerador}}{\sigma_D} = \frac{3}{2.717} \approx 1.104


**Paso 4:** Buscar en tabla Z  
- P(Z > 1.10) = 1 - 0.8643 = 0.1357  

**📌 Conclusión:**  
Probabilidad ≈ 0.1357 (13.57%)

---

#### b) Probabilidad entre 4 y 7 mg/dL
**Paso 1:** Calcular Z para 4 y 7  
$$Z_4 = \frac{4 - 5}{2.717} \approx -0.368$$  
$$Z_7 = \frac{7 - 5}{2.717} \approx 0.736$$

**Paso 2:** Buscar en tabla Z  
- P(Z < 0.74) ≈ 0.7704  
- P(Z < -0.37) ≈ 0.3557  

**Paso 3:** Calcular diferencia  
$$P(4 < D < 7) = 0.7704 - 0.3557 = 0.4147$$

**📌 Conclusión:**  
Probabilidad ≈ 0.4147 (41.47%)

---

#### c) Intervalo del 90% para diferencia real
**Paso 1:** Identificar Z crítico  
- Para 90% confianza: Z = 1.645  

**Paso 2:** Calcular límites  
$$\text{Límite inferior} = 5 - 1.645 \times 2.717 \approx 0.53$$  
$$\text{Límite superior} = 5 + 1.645 \times 2.717 \approx 9.47$$

**📌 Conclusión:**  
Intervalo: [0.53, 9.47] mg/dL

---

## 🗳️ Ejercicio 4: Diferencia de Proporciones

### 📝 Enunciado:
Consultora política mide aprobación presidencial en Norte (p=0.48) y Sur (p=0.42). Previo a elecciones, encuestas de 200 personas por región detectan cambios significativos.

### 🔍 Solución Manual:

#### a) Probabilidad de diferencia > 10%
**Paso 1:** Calcular diferencia poblacional  
$$p_N - p_S = 0.48 - 0.42 = 0.06$$

**Paso 2:** Calcular error estándar  
$$\sigma_{\hat{p}_N - \hat{p}_S} = \sqrt{\frac{p_N(1-p_N)}{n_N} + \frac{p_S(1-p_S)}{n_S}} = \sqrt{\frac{0.48 \times 0.52}{200} + \frac{0.42 \times 0.58}{200}} \approx \sqrt{0.001248 + 0.001218} \approx 0.0497$$

**Paso 3:** Calcular Z  
$$Z = \frac{0.10 - 0.06}{0.0497} \approx 0.805$$

**Paso 4:** Buscar en tabla Z  
- P(Z > 0.80) = 1 - 0.7881 = 0.2119  

**📌 Conclusión:**  
Probabilidad ≈ 0.2119 (21.19%)

---

#### b) Probabilidad de diferencia < 2%
**Paso 1:** Calcular Z  
$$Z = \frac{0.02 - 0.06}{0.0497} \approx -0.805$$

**Paso 2:** Buscar en tabla Z  
- P(Z < -0.80) = 0.2119  

**📌 Conclusión:**  
Probabilidad ≈ 0.2119 (21.19%)

---

#### c) Probabilidad de diferencia entre 4% y 8%
**Paso 1:** Calcular error estándar  
$$\sigma_{D} = \sqrt{\frac{p_N(1-p_N)}{n_N} + \frac{p_S(1-p_S)}{n_S}}} \approx 0.0497$$

**Paso 2:** Calcular Z para 4% y 8%  
$$Z_{0.04} = \frac{0.04 - 0.06}{0.0497} \approx -0.40 $$  
$$Z_{0.08} = \frac{0.08 - 0.06}{0.0497} \approx 0.40$$

**Paso 3:** Buscar en tabla Z  
- P(Z < 0.40) ≈ 0.6554  
- P(Z < -0.40) ≈ 0.3446  

**Paso 4:** Calcular diferencia  
$$P(0.04 < D < 0.08) = 0.6554 - 0.3446 = 0.3108$$

**📌 Conclusión:**  
Probabilidad ≈ 0.3108 (31.08%). Esto muestra que en ~31% de las encuestas, la brecha observada subestimaría la diferencia real (6%) en un 33-50%.

---

## 📚 Apéndice: Tabla Z Estándar (Valores Seleccionados)
| Z      | 0.00   | 0.05   | 0.10   | ...    |
|--------|--------|--------|--------|--------|
| -2.0   | 0.0228 | 0.0202 | 0.0179 | ...    |
| -1.5   | 0.0668 | 0.0606 | 0.0548 | ...    |
| -1.0   | 0.1587 | 0.1469 | 0.1357 | ...    |
| 0.0    | 0.5000 | 0.4801 | 0.4602 | ...    |
| 1.0    | 0.8413 | 0.8531 | 0.8643 | ...    |
| 1.5    | 0.9332 | 0.9394 | 0.9452 | ...    |
| 2.0    | 0.9772 | 0.9798 | 0.9821 | ...    |

*Nota: Los valores mostrados corresponden a la distribución acumulada estándar Φ(z)*

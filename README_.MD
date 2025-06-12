# Ejercicios Estadistica

## Autores

| Estudiante | Cedula  |
| :-------- | :------- |
| `Franyer Marin` | `32.293.396` | 
| `Nombre Apellido` | `CEDULA` | 


---

## Ejercicio 1: Distribución Muestral para la Media (Población Normal)

### 🔍 Enunciado:
Una fábrica de componentes electrónicos produce resistencias con vida útil distribuida normalmente (μ = 800 horas, σ = 40 horas). Semanalmente se analiza una muestra de 64 resistencias para verificar cumplimiento de estándares. La gerencia requiere comprender el comportamiento estadístico de estas muestras.

### 📊 Incisos:

#### a) Probabilidad de vida media inferior a 790 horas
- **Explicación:** Calcula la probabilidad de encontrar muestras con desempeño significativamente inferior, alertando sobre posibles fallas en lotes.
- **Fórmula:**  
  $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} = \frac{790 - 800}{40 / \sqrt{64}} = -2.0$$
- **Interpretación:** Un Z-score de -2.0 indica que 790 horas está a 2 errores estándar debajo de la media. Solo el 2.28% de muestras mostrarían este comportamiento si el proceso está controlado.

#### b) Probabilidad entre 790 y 810 horas
- **Explicación:** Determina la proporción de muestras "típicas" que reflejan fielmente la calidad real del proceso.
- **Interpretación:** 95.44% de muestras caen en este rango, validando que con n=64, el muestreo captura efectivamente la calidad real (±10 horas de μ).


---

## Ejercicio 2: Distribución Muestral para la Proporción (Población Normal)

### 🔍 Enunciado:
Estudio en universidades estatales revela que 35% de estudiantes usa transporte público. Para evaluar políticas de movilidad, se encuestan grupos de 100 estudiantes en distintos campus.

### 📊 Incisos:

#### a) Probabilidad de proporción muestral < 30%
- **Explicación:** Examina el riesgo de subestimar el uso real de transporte público en muestras pequeñas.
- **Fórmula:**  
  $$\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.35 \times 0.65}{100}} \approx 0.048$$
- **Interpretación:** 14.66% de probabilidad indica que en 1 de cada 7 muestras, la proporción observada subestima en >5% el valor real.

#### b) Probabilidad entre 30% y 40%
- **Explicación:** Evalúa confiabilidad de encuestas para reflejar realidad poblacional.
- **Interpretación:** 70.63% de muestras capturan el valor real dentro de ±5%, validando que n=100 es adecuado para estimaciones con margen aceptable.


---

## Ejercicio 3: Diferencia de Medias (Dos Poblaciones Normales)

### 🔍 Enunciado:
Laboratorio farmacéutico compara antihipertensivos (Fármaco A: μ=120 mg/dL, σ=15; Fármaco B: μ=115 mg/dL, σ=12). Ensayo con 50 pacientes por grupo analiza diferencias en reducción de colesterol.

### 📊 Incisos:

#### a) Probabilidad de diferencia > 8 mg/dL
- **Explicación:** Evalúa probabilidad de que Fármaco A parezca significativamente más efectivo por variabilidad muestral.
- **Fórmula:**  
  $$\sigma_{\bar{X_A}-\bar{X_B}} = \sqrt{\frac{15^2}{50} + \frac{12^2}{50}} \approx 2.74$$
- **Interpretación:** 11.93% de probabilidad indica que en casi 1 de cada 8 ensayos, se exageraría la diferencia real en >60%.

#### b) Probabilidad entre 4 y 7 mg/dL
- **Explicación:** Determina frecuencia con que muestras reflejan fielmente ventaja real del Fármaco A (5 mg/dL).
- **Interpretación:** 41.48% de muestras muestran diferencias moderadas (4-7 mg/dL), sugiriendo necesidad de muestras mayores para precisión.

#### c) Intervalo del 90% para diferencia real
- **Explicación:** Proporciona rango de valores plausibles para verdadera diferencia terapéutica.
- **Interpretación:** [0.49, 9.51] mg/dL indica superioridad de Fármaco A (no incluye 0), pero con gran incertidumbre en magnitud.

---

## Ejercicio 4: Diferencia de Proporciones (Dos Poblaciones Normales)

### 🔍 Enunciado:
Consultora política mide aprobación presidencial en Norte (p=0.48) y Sur (p=0.42). Previo a elecciones, encuestas de 200 personas por región detectan cambios significativos.

### 📊 Incisos:

#### a) Probabilidad de diferencia > 10%
- **Explicación:** Cuantifica riesgo de sobreestimar diferencias regionales por error muestral.
- **Interpretación:** 4.00% de probabilidad indica que solo en 1 de 25 encuestas se exageraría la brecha al doble de su valor real (6%→12%).

#### b) Probabilidad de diferencia < 2%
- **Explicación:** Evalúa riesgo de que encuestas oculten diferencias reales entre regiones.
- **Interpretación:** 20.66% de probabilidad muestra que en 1 de cada 5 muestras, la brecha parecería insignificante (<2%) aunque exista.

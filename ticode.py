import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Datos de distancia y potencia medida (reemplaza con tus valores)
distances = np.array([1.32, 1.42, 1.52, 1.62, 1.72, 1.82, 1.92, 2.02, 2.12, 2.22,
                      2.32, 2.42, 2.52, 2.62, 2.72, 2.82, 2.92, 3.02, 3.12, 3.22,
                      3.32, 4.32, 5.32, 6.32, 7.32, 8.32, 9.32, 10.32, 11.32, 11.82,
                      12.32, 12.82, 13.32, 13.82, 14.32, 14.82, 15.32, 15.82, 16.32,
                      16.82, 17.32, 17.82, 18.32, 18.82, 19.32, 19.82, 20.32, 20.82,
                      21.32, 21.82, 22.32])
received_power = np.array([-86.4, -90, -83.3, -88.8, -84.4, -84.8, -89.4, -94.7, -91, -87.8,
                           -85.7, -84.1, -85.7, -94.1, -97.4, -95.3, -91.3, -87.5, -89.2, -88.8,
                           -96.2, -96.5, -95.9, -103.5, -106.2, -104.6, -104.1, -108.4, -122.3,
                           -110.6, -116.9, -113.2, -120.9, -115.6, -112.6, -109.4, -111.3, -110.1,
                           -112.7, -107, -121.1, -106.9, -101.4, -104.7, -111.6, -99.3, -102.7,
                           -105.7, -105.6, -115.7, -114.6])

# Potencia transmitida constante en dBm (ajusta según tus datos)
transmit_power = 0  # Ajusta según tu configuración de potencia de transmisión

# Cálculo de PathLoss
path_loss = transmit_power - received_power

# Crear subplots para ambos gráficos en la misma ventana
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico de PathLoss vs Distancia Logarítmica
log_distances = np.log10(distances)
ax1.scatter(log_distances, path_loss, label="Datos de PathLoss", color='b')
ax1.set_xlabel("Log10(Distancia) [m]")
ax1.set_ylabel("PathLoss [dB]")
ax1.set_title("Gráfico de PathLoss en función de la distancia logarítmica")

# Ajuste lineal (regresión lineal)
slope, intercept = np.polyfit(log_distances, path_loss, 1)
ax1.plot(log_distances, slope * log_distances + intercept, color='r', linestyle="--", 
         label=f"Ajuste lineal: y = {slope:.2f} * log10(d) + {intercept:.2f}")
ax1.legend()
ax1.grid()

# Cálculo de ensombrecimiento (shadowing) como la desviación respecto a la recta de ajuste
predicted_path_loss = slope * log_distances + intercept
shadowing = path_loss - predicted_path_loss

# Gráfico de CDF del ensombrecimiento
shadowing_sorted = np.sort(shadowing)
cdf = np.arange(1, len(shadowing) + 1) / len(shadowing)
ax2.plot(shadowing_sorted, cdf, label="CDF del ensombrecimiento", color='g')
ax2.set_xlabel("Shadowing [dB]")
ax2.set_ylabel("Probabilidad acumulada")
ax2.set_title("CDF del ensombrecimiento")
ax2.grid()
ax2.legend()

# Mostrar ambos gráficos
plt.tight_layout()
plt.show()

# Impresión de los resultados de análisis
print(f"Pendiente (slope): {slope:.4f}")
print(f"Intercepto (intercept): {intercept:.2f}")
print(f"Media del ensombrecimiento: {np.mean(shadowing):.2f} dB")
print(f"Desviación estándar del ensombrecimiento: {np.std(shadowing):.2f} dB")

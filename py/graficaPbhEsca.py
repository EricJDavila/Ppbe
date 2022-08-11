#*******************************************************************************
# 3.6.1.4. Grafica de pbhEsca.
#*******************************************************************************
import matplotlib.pyplot as plt
import pandas as pd
pbhEsca = pd.read_parquet('parquet/pbhEsca.parquet.gzip', engine='fastparquet')

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1, 1, 1)  # Crea una figura conteniendo un solo eje.
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, \
    hspace=None)
ax1.set_title ('Precios horarios de energía en bolsa con el techo del Precio \
    de Escasez')
ax1.set_ylabel ('COP/kWh')
ax1.set_xlabel ('Hora')
ax1.plot(pbhEsca.index, pbhEsca.precioConEsca, 'g-', label='Pbh con Escasez', \
    linewidth=1, alpha=0.8)
plt.ylim(0, 1000)
plt.grid(axis='y', color='k', alpha=0.2)
plt.show()
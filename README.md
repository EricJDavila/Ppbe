# Ppbe
Proyección de precio de bolsa de la energía (programando en Python).

Este programa proyecta los precios de bolsa de energía horarios, en el Sistema Eléctrico de Colombia, a muy largo plazo, que puede estar entre 5 y 10 años.

El programa es útil para poder tomar una mejor decisión sobre la mejor propuesta de precios de energía recibidas por una gran consumidor de energía o usuario no regulado, teniendo en cuenta las altas incertidumbres de esta variable y las diferentes modalidades que se ofertan en este mercado. Por ejemplo, precios fijos, precios de bolsa horarios y precios de bolsa con techo y piso, entre otras.

Los datos o variables de entrada que servirán para alaborar el modelo de predicción se obtienen principalmente de seis fuentes: a. XM; b. NOAA, especialmente el índice multivariado El Niño (MEI); c. EIA; d. Banco de la República de Colombia; e. Dane. y f. Las curvas de demanda entregadas por el Cliente que es Usuario No Regulado.

Para obtener los datos de entrada, este programa aplicará la conexión a través de las API de XM, de la NOAA y de EIA. Los datos del Banco de la República, del DANE y del Usuario se usarán los archivos en formato Excel. Esta conexión y el programa en general utilizará el lenguaje Python.

Este sitio es mantenido por Eric Dávila, eric.davila@eseisa.com.

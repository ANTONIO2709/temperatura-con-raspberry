# temperatura-con-raspberry para python
temperatura con raspberry y termistor
En este capítulo, aprenderemos otro nuevo tipo de resistencia, el termistor.
La resistencia del termistor cambiará con el cambio de temperatura. Así que podemos hacer un termómetro
de acuerdo con esta característica.


El termistor es una resistencia sensible a la temperatura. Cuando la temperatura cambie, la resistencia del termistor
cambio. Con esta función, podemos utilizar el termistor para detectar la intensidad de la temperatura. El termistor y el símbolo son
de la siguiente manera.
La relación entre el valor de resistencia y la temperatura del termistor es:
Rt-R*EXP [B*(1/T2-1/T1)]
Dónde:
Rt es la resistencia del termistor bajo temperatura T2;
R está en la resistencia nominal del termistor bajo temperatura T1;
EXP[n] es el enésimo poder de E;
B es para el índice térmico;
T1, T2 es Kelvin temperatura (temperatura absoluta). Temperatura de Kelvin 273.15+temperatura celsius.
Los parámetros del termistor que utilizamos son: B-3950, R-10k, T1-25.
El método de conexión del circuito del termistor es similar al fotorresistor, como el siguiente método:
Podemos usar el valor medido por el convertidor ADC para obtener el valor de resistencia del termistor, y luego podemos usar
la fórmula para obtener el valor de temperatura.
En consecuencia, la fórmula de temperatura puede concluirse:
T2 a 1/(1/T1 + ln(Rt/R)/B)

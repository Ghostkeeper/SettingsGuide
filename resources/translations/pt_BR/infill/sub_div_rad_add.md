Casca de subdivisão cúbica
====
Esse ajuste significa que o motivo de enchimento da subdivisão cúbica está começando a reduzir um pouco mais o preenchimento interno, para melhorar a resistência à impressão.

![Subdivisão cúbica sem casca adicional](../../../articles/images/sub_div_rad_add_small.png)

![5 mm de casca adicional](../../../articles/images/sub_div_rad_add_large.png)

A subdivisão cúbica funciona removendo os limites entre oito cubos adjacentes se nenhum dos cubos tocar a borda do volume de enchimento.Esse ajuste move essa borda mais para dentro, impedindo assim a supressão das fronteiras entre os cubos.

De fato, isso permite que o modelo de subdivisão cúbica desenhe a densidade máxima com mais frequência.Isso aumenta a resistência do objeto, mas também o tempo e o material necessário para imprimi -lo.No extremo, aumentando esse parâmetro suficientemente, o esquema de subdivisão cúbica acabará sendo o mesmo que o diagrama cúbico simples.

Você também pode definir esse parâmetro como um número negativo.Isso torna possível remover as fronteiras entre os cubos com mais frequência, reduzindo a quantidade de enchimento nas bordas.
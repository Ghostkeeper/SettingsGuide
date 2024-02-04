Ative as configurações da ponte
====
Quando o seu modelo apresenta uma certa saliência que é suportada em ambos os lados, a Cura o detecta e modifica a área de pele pendente para melhor imprimir.Se esse parâmetro for ativado, você poderá ajustar a detecção dessas áreas sobrepostas e o comportamento resultante para que haja melhor sobreposição.

![Quando uma ponte é detectada, as linhas de pele são orientadas para preencher a lacuna da melhor maneira possível](../../../articles/images/bridge_settings_enabled_default.png)

![Com as configurações de ponte ativadas, as linhas da ponte são impressas com parâmetros diferentes](../../../articles/images/bridge_settings_enabled_enabled.png)

Normalmente, o Cura usará uma técnica de transição bastante rudimentar.Cura detectará áreas de pele salientes que são suportadas em vários lados.A [direção dessas linhas de pele](../top_bottom/skin_angles.md) é ajustada para cobrir essas áreas automaticamente.Isso possibilita garantir que a maior parte possível da área de saliência seja suportada em vários lados e melhorar a qualidade da impressão.

Quando esse parâmetro é ativado, você pode ajustar esse comportamento com mais precisão de acordo com suas necessidades.Isso permite que você faça alterações:
* Velocidade de impressão
* Velocidade
* densidade (como densidade de enchimento, mas com as linhas da pele)
* Velocidade do ventilador
* Para as paredes, também na costa

Esses parâmetros podem ser ajustados separadamente para a pele que preenche um vácuo e para as paredes.Se a opção [a ponte tiver várias camadas](Bridge_enable_more_layers.md) for ativada, elas também poderão ser ajustadas separadamente para a segunda e a terceira camada acima da lacuna de ponte.Também é possível modificar as partes da impressão que são consideradas zonas de ponte, ajustando [que fração da área deve estar acima do vácuo](Bridge_skin_support_threshold.md) e uma [largura mínima para as paredes](Bridge_Wall_Min_Length.md ).

Ao ativar as configurações de cerdas, você tem melhor controle sobre como as pontes são tratadas na sua impressão.Ao definir muito bem os parâmetros de ponte, você pode melhorar a qualidade de você, talvez de maneira significativa, e melhorar a precisão na direção vertical.A única desvantagem é que, se você não ajustar as configurações de direção à sua impressora, a impressão pode ser tão ruim.



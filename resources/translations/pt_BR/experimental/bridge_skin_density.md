Densidade da camada externa da ponte
====
Este parâmetro controla a densidade da parte inferior da impressão quando preenche um vácuo.Em uma densidade de 100 %, as linhas são colocadas diretamente ao lado dela.Em densidades mais baixas, as linhas são mais espaçadas.

![Para uma densidade 100 %, as linhas são colocadas diretamente ao lado da outra](../../../articles/images/bridge_skin_density_100.png)

![Tem uma densidade de 50%, há um certo espaçamento entre as linhas](../../../articles/images/bridge_skin_density_50.png)

Dois efeitos principais entram em jogo ao definir este parâmetro: adesão entre linhas e resfriamento.

Quando as linhas da pele são diretamente adjacentes, elas aderem um ao outro.Isso tornará o lado inferior do espaço com paned mais bonito, pois a superfície será contínua em vez de estar em um cordão.Além disso, a segunda linha pode confiar um pouco na primeira linha durante a ponte, o que reduz um pouco a flacidez da ponte.

Mas há outro efeito, é refrescante.Quando as linhas estão mais espaçadas, elas podem esfriar mais rapidamente e também não ceder muito.Obviamente, isso só se aplica quando o ventilador estiver em andamento; portanto, para materiais de alta temperatura, essa estratégia não funcionará.

Qual desses efeitos é o mais forte depende da viscosidade do material, na velocidade em que ele solidifica e a velocidade do ventilador.Uma certa configuração é sempre necessária.

** Se a [taxa de fluxo da camada externa da ponte](Bridge_skin_material_flow.md) for menor que 100 %, também haverá um certo espaçamento entre as linhas, mesmo que a densidade seja 100 %, porque as linhas serão então Finer. **
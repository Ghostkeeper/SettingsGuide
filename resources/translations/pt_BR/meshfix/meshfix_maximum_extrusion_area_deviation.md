Diferença máxima na superfície de extrusão
====
Ao imprimir linhas de diferentes larguras, é comum ter uma linha que deve gradualmente voltar a uma de suas extremidades.Esse parâmetro determina o tamanho das etapas nas quais essas linhas estão diminuindo ou ampliando, controlando a proximidade das linhas em comparação com a área que elas devem cobrir idealmente.

![Menor resolução em caso de alto desvio](../../../articles/images/meshfix_maximum_extrusion_area_deviation_high.png)

![Largura de linha suave quando o desvio é baixo](../../../articles/images/meshfix_maximum_extrusion_area_deviation_low.png)

Os comandos do Código G não podem pedir à impressora para imprimir uma linha de largura variável.Ele deve imprimir as linhas com uma largura fixa.O Cura pode dividir uma linha em vários segmentos cuja largura muda gradualmente.No entanto, isso adiciona muitos segmentos de linha à impressão.A unidade de impressora central pode não ser capaz de seguir todas essas instruções durante a impressão.Este parâmetro permite escolher a discretização de segmentos de linha com largura variável.Uma resolução mais alta (diferença reduzida) permite obter linhas mais precisas em teoria, mas também aumenta consideravelmente a quantidade de instruções.

Embora a modificação gradual da largura de uma linha seja agradável de olhar no modo de camada, ela praticamente não tem efeito na impressão real.As impressoras 3D físicas não regulam seu fluxo com precisão suficiente para que qualquer melhoria seja vista, aumentando a resolução aqui.Nas circunstâncias normais, esse parâmetro deve ser alto o suficiente para nunca ser um fator que limite a resolução do Código G. Dessa forma, o risco de ter uma memória de buffer é reduzido e os riscos de ultrapassar o buffer é minimizado.
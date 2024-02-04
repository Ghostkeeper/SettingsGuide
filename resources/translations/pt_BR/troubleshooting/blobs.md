As gotas (blobs)
====
Blubs são pequenas gotas na lateral do modelo.Às vezes, esses são apenas pontos.Às vezes eles são arranhões.Eles constituem um defeito na superfície visual e podem aumentar o atrito entre as superfícies que devem deslizar um no outro em um mecanismo.

![Algumas gotas nesta superfície](../../../articles/images/blobs.jpg)

Existem várias causas possíveis para blobs.Este é um dos defeitos mais comuns na impressão 3D.Este artigo lista algumas causas possíveis e suas soluções.

O bico diminui
----
Se o bico se mover mais devagar em um determinado curso do que em outros, ele colocará mais material.Este material flui para fora a superfície da parede, formando uma gota.

O suprimento de alimentos provavelmente deve ser reduzido com ele.No entanto, mesmo que a extrusora se mova mais lentamente, ele pode fluir alguns segundos antes da saída da abertura do bico, é reduzida de acordo.Enquanto isso, muito material será extrudado, o que dá essas gotas.

Para lutar contra esse fenômeno, veja as seguintes configurações:
* Equalize a velocidade da [parede externa](../speed/speed_wall_0.md) para que seja idêntico ao que é impresso antes (como [paredes interiores](../speed/speed_wall_x.md) ou [Preenchimento](../speed/speed_infill.md)).Portanto, não haverá desaceleração.
* Aumente o [Jerk da parede externo](../Speed/jerk_wall_0.md).Isso impedirá que o bico desacelere nos cantos.
* Você pode reduzir a [resolução](../meshfix/meshfix_maximum_resolution.md) e aumentar o [desvio](../meshfix/meshfix_maximum_deviação.md) para impedir que o controlador desacelere o bico para seguir os códigos G que ele deve tratar.
* Desative o parâmetro [compense as sobreposições das paredes externas](../shell/Travel_complensate_overlapping_walls_0_nabled.md).Este parâmetro permite criar novos comandos de deslocamento com diferentes avanços.A desativação desta função reduz o número de ordens de deslocamento nas paredes.

O bico para
----
Se o bico feito de pequenas quebras durante a impressão da parede externa, é muito provável que ele esteja aguardando o processador da sua impressora 3D lidar com novos comandos de movimento.O software de planejamento de movimentos da impressora geralmente mantém uma memória de buffer com ordens prontas para tais ocasiões, quando os comandos de movimento já foram processados ​​para que a impressora conheça exatamente os tempos de ativação dos motores a não ou outros movimentos.Se esse selo estiver esgotado, falamos de "Buffer Underrun".Isso causa a aparência de manchas na superfície.

Para evitar isso, você deve reduzir a resolução do Código G.
* Aumente o parâmetro [resolução máxima](../meshfix/meshfix_maximum_resolution.md), que permite que a cura produza segmentos de linha mais longos.
* Aumente o parâmetro [desvio máximo](../meshfix/meshfix_maximum_devial.md), que permite que a cura reduza ainda mais a resolução, desviando -se mais do caminho original.
* Desative o parâmetro [compense as sobreposições das paredes externas](../shell/Travel_complensate_overlapping_walls_0_nabled.md).Se a parede externa se sobrepor a outras paredes externas, isso daria uma parte da parede uma largura de linha diferente, mas isso requer um controle de movimento adicional.Para reduzir os comandos de movimento, você pode desativar essa configuração.No entanto, isso também pode levar a uma superextrusão nessas paredes, o que também causa subsídios.
* Reduza a [velocidade de impressão da parede externa](../speed/speed_wall_0.md).Isso reduz a velocidade de execução dos controles de deslocamento, o que permite que a CPU o alcance.

O deslocamento é feito através das paredes
----
Embora o Cura geralmente evite atravessar a parede externa o máximo possível, isso às vezes é inevitável.Se o bico transportar um material escorrendo enquanto atravessa uma parede externa, esse material poderá ser limpo lá, deixando uma mancha.

É possível evitar essa causa de rebarbas ajustando os seguintes parâmetros:
* Verifique se a função [Modo Detours](../Travel/Retaction_Combing.md) está ativada.Isso permite que o bico ignore as paredes o máximo possível, em vez de atravessá -las.
* Ative [retrair em z](../Travel/Retaction_hop_enabled.md).Se as paredes forem francas, o bico se moverá um pouco para cima, para passar pelas paredes em vez de atravessá -las.O material escorrendo provavelmente não será limpo na parede, mas onde o bico pousa após a viagem.Cura sempre tentará atracar ou pele, se possível.
* Verifique se [a ordem de imprimir as paredes está otimizada](../shell/otimize_wall_printing_order.md).Isso reduz o número de movimentos feitos durante a impressão das paredes, o que permite movimentos mais eficazes e reduz o risco de alguns desses movimentos passarem por uma parede externa.

Aumento da pressão
----
Se o bico for exagerado, a extrusão pode se tornar irregular.Às vezes, isso pode encontrar de repente um resultado quando um canto específico da sua pegada é impresso (especialmente no excesso).Às vezes, essa pressão reprimida explode, deixando uma grande mancha.Em geral, uma tira de pressão gradualmente decrescente se forma após a queda.

Para reduzir esse efeito, aqui estão alguns parâmetros para levar em consideração:
* Reduza a [largura da linha de parede](../Resolução/Wall_line_width.md).Isso reduz a pressão no bico do bico em geral.
* Reduza a [largura da parede externa](../shell/wall_0_inset.md).Esse ajuste significa que a parede externa monta na parede interna adjacente, para que a parede seja empurrada mais fortemente na parede interna, o que melhora a resistência.No entanto, esse impulso também aumenta a pressão dentro da sala do bico.

Filamento molhado
----
Se o filamento acumular a umidade enquanto ainda estava na bobina, essa água será aquecida no bico além de seu ponto de ebulição.O vapor de água explodirá do bico quando for expulso.Essa pequena explosão pode explodir plástico, o que resulta em uma pequena mancha na superfície.

Costuras
----
Um selo será criado no local onde o perímetro da parede externa é iniciado e fechado.Não é isso que as pessoas normalmente chamam de gota, embora tenha uma aparência semelhante.Consulte o artigo sobre [costuras](costing.md) para saber como reduzir esse efeito.

Se o parâmetro [alinhamento do z -z](../shell/z_seam_type.md) estiver definido como "aleatório", a costura será distribuída em torno do modelo, criando assim pequenas costuras em todos os lugares.Pode parecer exatamente uma bolha, mesmo que seja realmente uma costura.Modifique o parâmetro [alinhamento do z](../shell/z_seam_type.md) para ocultar essas costuras.
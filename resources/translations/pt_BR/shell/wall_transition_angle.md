Ângulo do limiar de transição da parede
====
Este ângulo indica o ângulo do qual o Cura começa a criar transições para preencher corretamente o espaço.Todos os ângulos mais agudos do que esse ângulo serão preenchidos com linhas de largura variável.

![Mais largo que 10 °, não cria mais transições](../../../articles/images/wall_transition_angle.png)

Este parâmetro permite ou desativar a largura variável das linhas para certos ângulos.Se duas paredes opostas são quase paralelas, menores que o ângulo especificado neste parâmetro, o espaço entre elas é preenchido com linhas cuja largura pode variar.Se eles formam um ângulo maior em relação ao outro, o espaço entre eles é preenchido com cabos de largura constante.

Como sempre, é um compromisso.O uso de uma largura variável tem certas vantagens, como:
* Ele não deixa vácuo entre as linhas.
* Não preenche o mesmo espaço várias vezes.
* As dimensões da impressão serão mais precisas neste local.

No entanto, também tem certas desvantagens:
* Introduz cantos em partes finas que podem aparecer como ondulações na superfície.
* Isso cria viagens adicionais.
* A impressora pode não modificar com precisão a largura da linha em rápida sucessão.

Na prática, é bom garantir que esse ângulo seja grande o suficiente para reduzir o tamanho dos espaços nos ângulos agudos, como podemos ver na visão do plano, mas também menor possível.Um ângulo menor geralmente dá à superfície uma aparência mais suave.

Não é possível reduzir o ângulo a 0 ° para eliminar completamente as larguras da linha variável.As paredes paralelas opostas sempre verão sua largura de linha ajustada para se adaptar ao espaço.

** Este parâmetro não se aplica apenas às paredes normais, mas também a paredes de contorno adicionais, paredes de suporte, paredes de enchimento e padrões concêntricos. **
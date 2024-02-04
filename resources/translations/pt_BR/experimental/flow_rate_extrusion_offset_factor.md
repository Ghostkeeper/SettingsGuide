Fator de compensação de fluxo
====
A compensação de débito é uma experiência semelhante à funcionalidade [avanço linear](http://marlinfw.org/docs/features/lin_advance.html) de Marlin.O objetivo da compensação da taxa é compensar a subestusão e a superextrusão quando o fluxo do material que sai do bico muda.Essa configuração permite configurar a extensão do efeito.

A compensação do fluxo avança o filamento do material adicional necessário no segundo em que se segue, a cada movimento.Entre cada movimento, existem três cenários possíveis.
* Se os dois comandos de movimento adjacente tiverem o mesmo fluxo (porque a largura da linha, a altura da camada e a velocidade são os mesmos), o avanço também será o mesmo.O filamento não será movido em nenhuma direção entre essas linhas.
* Se o fluxo aumentar com a próxima linha, o filamento será movido mais adiante durante a segunda linha.Isso aumenta a pressão na sala dos bicos, para que o material possa extrudar mais rapidamente durante a impressão da linha e as seguintes linhas.
* Se a taxa de fluxo diminuir com a próxima linha, o filamento será movido para trás durante a segunda linha.A pressão na sala dos bicos é assim reduzida, de modo que o material diminua durante a impressão da segunda linha e das seguintes linhas.

A distância em que o filamento é movido é igual à quantidade de material que seria extrudada a cada segundo durante a linha (se a linha fosse longa o suficiente para imprimir um segundo).No entanto, graças a esse ajuste, essa distância pode ser ajustada.Ao aumentar o fator, o efeito de compensação será mais forte.Reduzir isso tornará o efeito de compensação mais baixo.Fatores mais altos também exigirão mais tempo para impressão, porque o filamento deve ser movido mais para cima e para baixo.

Se essa compensação de fluxo for ativada, a pressão dentro da sala do bico deve estar melhor equipada para gerenciar o fluxo.Isso pode reduzir o subestimado e o excesso de Extrusão e dará ao objeto dimensões mais precisas.

No entanto, a compensação é aplicada para uma única linha.Às vezes, pode ser uma linha curta, durante a qual o filamento deve se mover muito rapidamente.A cabeça de impressão pode precisar desacelerar para que o carregador possa seguir, o que causará a aparência de uma mancha.Às vezes, pode ser uma linha longa, o que reduz a força do efeito.Isso faz com que toda a compensação funcione das taxas de extrusão não confiáveis, e é por isso que esse ajuste ainda é experimental.
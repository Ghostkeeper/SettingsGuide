Lá inicia a camada
====
Se houver várias peças para imprimir em uma camada, o Cura otimizará a ordem em que essas peças são impressas.Para permitir que a peça esfrie antes de imprimir a próxima camada, ele imprimirá cada camada aproximadamente na mesma ordem.Os parâmetros [X inicial da camada](Layer_Start_X.MD) e ** y Iniciar da camada ** Determine qual peça será impressa primeiro: a peça mais próxima das coordenadas especificadas.Este parâmetro determina a coordenada Y desta parte.

Este é um parâmetro diferente de costura Z. Os parâmetros de alinhamento da costura Z determinam apenas o local em que a impressora começará a imprimir o contorno de uma peça, enquanto esse parâmetro determina a parte pela qual começará.

Se a sua impressora fizer algo específico quando começar com uma nova camada ou quando mudar de extrusão, é bom ajustar esses detalhes de contato onde a cabeça de impressão termina quando estiver pronto para continuar a impressão.Isso torna possível minimizar as viagens e vazamento.

Esses detalhes de contato são encontrados no sistema de coordenadas do código G, que é diferente do sistema de coordenadas que o Cura usa para mostrar a colocação de objetos.
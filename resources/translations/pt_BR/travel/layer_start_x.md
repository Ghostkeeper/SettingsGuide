X camada inicial
====
Se houver várias peças para imprimir em uma camada, o Cura otimizará a ordem em que essas peças são impressas.Para permitir que a peça esfrie antes de imprimir a próxima camada, ele imprimirá cada camada aproximadamente na mesma ordem.Os parâmetros ** x início da camada ** e [y começam na camada](camada_start_y.md) determinam qual peça será impressa primeiro: a peça mais próxima das coordenadas especificadas.Este parâmetro determina a coordenada x desta parte.

Este é um parâmetro diferente do Z. Os parâmetros de alinhamento da costura Z apenas determinam onde a impressora começará a imprimir o contorno de uma peça, enquanto esse parâmetro determina com qual parte será iniciada.

Se a sua impressora fizer algo específico quando começar com uma nova camada ou quando mudar de extrusão, é bom ajustar esses detalhes de contato onde a cabeça de impressão termina quando estiver pronto para continuar a impressão.Isso torna possível minimizar as viagens e vazamento.

Esses detalhes de contato são encontrados no sistema de coordenadas do código G, que é diferente do sistema de coordenadas que o Cura usa para mostrar a colocação de objetos.
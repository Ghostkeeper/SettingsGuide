Inclua temperaturas do material
====
Este parâmetro indica ao gerador de código se deve ou não escrever controles de temperatura de impressão para o início da impressão antes do código G.É definido automaticamente ao iniciar uma impressão.

Para a maioria das operações realizadas durante o [código g de partida](MACHING_START_GCODE.MD), é útil que o bico de impressão esteja na temperatura certa para impressão.Para facilitar a tarefa de imprimir designers de definição, o Cura aquece automaticamente o bico antes do [código G inicial](MACHING_START_GCODE.MD) ser executado.No entanto, se o código g de partida contiver uma referência a um ajuste de temperatura, ele não será mais aquecido automaticamente.

*Como é um ajuste da máquina, essa configuração normalmente não é visível na lista de configurações.Modificá -lo não tem efeito, pois será alterado automaticamente por cura.*
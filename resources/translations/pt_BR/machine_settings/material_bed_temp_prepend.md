Inclua a temperatura da bandeja
====
Este parâmetro indica ao gerador de código se deve ou não gravar os controles de temperatura do bico para o início da impressão antes do código g de inicialização.É definido automaticamente ao iniciar um arquivo.

Para a maioria das operações realizadas durante o [código g de partida](MACHING_START_GCODE.MD), é sábio que o bico esteja na temperatura certa para impressão.Para facilitar o design das definições da impressora, o Cura aquece automaticamente o bico antes do [código G de Starting](MACHING_START_GCODE.MD) ser executado.No entanto, se o código de partida G contiver uma referência a um ajuste de temperatura do bico, ele não será mais aquecido automaticamente.

*Como é um ajuste da máquina, essa configuração normalmente não é visível na lista de configurações.Modificá -lo não tem efeito, pois será alterado automaticamente por cura.*
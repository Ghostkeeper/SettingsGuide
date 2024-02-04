Alternar os departamentos das paredes
====
Se for ativado, esse parâmetro alterna a sensação de enrolamento das paredes entre o significado por hora e o significado anti -threading.

A primeira parede interna será impressa na direção oposta da parede externa, e a segunda parede interna será impressa novamente na direção oposta.Além disso, na próxima camada, o significado também será oposto, para que as paredes empilhadas entre si também sejam alternadas.

A alternância da direção da impressão reduz o efeito de restrições internas dentro do modelo, o que reduz o [desapego](../solucionando problemas/warping.md).Ao imprimir uma linha, o bico puxa bastante forte no cordão de material derretido, que estica o plástico.Durante a solidificação, essa restrição pode distorcer o modelo.Se a linha adjacente for impressa na direção oposta, essa restrição será frustrada pelas linhas adjacentes que puxam na direção oposta.A força de restrição é combatida pela restrição na direção oposta.

A desvantagem da alternância do significado das paredes vem da histerese do pórtico da impressora.Se houver jogo nos eixos ou polias da impressora, as linhas diagonais serão colocadas em um local ligeiramente diferente durante a impressão na direção oposta.Consequentemente, a parede se torna menos suave e as dimensões de impressão menos precisa.Uma impressora bem ajustada não mostrará esse efeito; portanto, se a impressora tiver cintos, polias e componentes precisos apertados, a alternância das paredes das paredes provavelmente dará apenas vantagens.

Durante [impressão de dentro para fora](../shell/inet_direction.md), esse parâmetro torna a costura das paredes mais visível e causa certas vibrações, porque o bico faz uma volta completa de 180 ° logo antes do Início das paredes ao ar livre, o que causa vibrações.Não é um efeito impressionante quando impressões de fora para dentro.
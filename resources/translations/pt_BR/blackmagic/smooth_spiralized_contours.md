Contornos em espiral suaves
====
Se [espiralar o contorno externo](Magic_spiralize.md) for ativado, esse parâmetro ativa ou desativa a característica mais distinta do modo Spriralize: em vez de imprimir cada camada uma após a outra em intervalos de altura, a altura é gradualmente aumentada durante a camada.

Como o modo Spriralize envolve apenas a impressão das paredes para a maioria das camadas com um único contorno, esse contorno exclusivo assumirá a forma de uma espiral, emprestando o nome à função Spriralize.A primeira e a última camada de impressão vê seu fluxo gradualmente reduzido para evitar a superextrusão e atingir a altura certa.

Como o bico é movido gradualmente para a próxima altura da camada em toda a camada, não haverá mais uma costura em que o bico se move para a próxima camada.De fato, isso remove a costura Z.

Por outro lado, a camada é movida para cima ou para baixo meia camada.É menos preciso.Pode ter um efeito vago nos detalhes finos da impressão.

Este parâmetro não é eficaz na remoção de costuras se houver vários contornos para imprimir em uma camada.Ainda será necessário parar a extrusão após o esboço para ir para a próxima peça impressa.Isso deixa uma costura de qualquer maneira.

** Este efeito não é visível em vista das camadas devido às limitações de renderização. **
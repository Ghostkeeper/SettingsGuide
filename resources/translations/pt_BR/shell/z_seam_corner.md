Preferência da junta ângulo
====
Com esse ajuste, você pode controlar a posição das costuras em comparação com os cantos do seu modelo.

Em geral, existem duas opções para o local onde a costura pode ser colocada: escondida em um canto interno ou exposto em um canto externo.Geralmente, é preferível esconder a costura em um canto interno, porque a costura será pouco visível.Mas também é possível colocá-lo em uma esquina ao ar livre, para que você possa cortar o selo com uma faca ou lixar com lixa, se um pós-processamento puder ser feito na sala.

Aqui estão as opções disponíveis para esta configuração e seus efeitos.
*** Nenhum: ** Não há preferência por cantos.A costura será escolhida para melhor corresponder aos requisitos de [alinhamento do z](z_seam_type.md).
*** Ocultar junta: ** É melhor esconder a costura em um canto interno.Se o alinhamento da costura em Z estiver definido como "o ângulo mais agudo", o canto mais interior será sempre escolhido.Se estiver definido como "o mais curto", um canto interno será escolhido, próximo à posição atual do bico quando inicia o contorno.
*** Junta de exposição: ** É preferível expor a costura em um canto externo.Se o alinhamento da junta Z estiver definido como "o ângulo mais agudo", o canto externo mais agudo será sempre escolhido.Se estiver definido como "o mais curto", um canto externo será escolhido próximo à posição atual do bico quando inicia o contorno.
*** Esconda ou exponha a junta: ** Esta função permite que você coloque uma articulação em um canto agudo, seja interior ou exterior, desde que não esteja em uma parede plana.
<!-Se Cura_version> = 4.2-> ** Mascaramento inteligente: ** Isso permite que você coloque a articulação em um canto, como se "ocultar ou exponha articulações", mas os cantos do interior são escolhidos com mais frequência do que os cantos ao ar livre se Os cantos internos estão disponíveis no contorno.Se não houver cantos internos, escolheremos um canto ao ar livre. <!-endif->>
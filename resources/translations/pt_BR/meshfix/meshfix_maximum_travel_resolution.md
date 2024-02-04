Resolução máxima de viagem
====
Se o modelo tiver uma resolução muito alta, o Cura reduzirá a resolução para que o processador da impressora possa seguir o processamento dos comandos do código G à medida que forem executados.A resolução máxima dos deslocamentos pode ser determinada separadamente da [resolução máxima](Meshfix_maximum_resolution.md) durante a impressão.

Como a viagem é executada muito mais rápida que as impressões, a cabeça de impressão percorre os segmentos de linha da viagem muito mais rápido que os outros segmentos de linha.A unidade central deve processar esses segmentos de linha muito mais rapidamente para seguir o bico.É por isso que a resolução dos movimentos de movimento deve ser menor que a dos movimentos de extrusão mais lentos.

A resolução do movimento durante a viagem geralmente não é importante para a qualidade da impressão.Como não é uma extrusão, não há superfície para ficar embaçado ou angular.É por isso que a redução na resolução dos movimentos de movimento não tem impacto significativo na qualidade da impressão.

A maioria das viagens da cura são linhas retas.Estes são os movimentos mais rápidos que produzem as menos vibrações.No entanto, se o Cura deve evitar colisões, ele tende a seguir a superfície da superfície que ele tenta evitar.O movimento de deslocamento em torno dessa superfície terá uma resolução semelhante à da superfície que evita.Consequentemente, esse parâmetro só pode ter um efeito real se o [Modo Detours](../Travel/Retraction_Combing.md) for ativado.
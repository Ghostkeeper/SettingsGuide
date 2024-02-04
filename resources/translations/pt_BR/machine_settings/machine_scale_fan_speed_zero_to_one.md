Escala de velocidade do ventilador em 0-1
====
Para controlar a velocidade na qual os ventiladores da impressora são executados, o Cura Place controla no código G com um parâmetro que controla a velocidade.Normalmente, esse parâmetro é um número entre 0 e 255. No entanto, algumas impressoras também aceitam um número entre 0 e 1 e depois o interpretam de maneira diferente.Este parâmetro garante que o Cura escreva as velocidades dos fãs como um número entre 0 e 1, em vez de 0 e 255.

Existem 3 tipos de comportamentos de firmware nas diferentes impressoras de mercado.
* A maioria das impressoras aceita a velocidade do ventilador apenas na forma de um número entre 0 e 255. Esse parâmetro deve ser desativado; caso contrário, o ventilador nunca se voltará.
* Algumas impressoras (em particular reprimpirmandware) aceitam números entre 0 e 255, mas se forem menores ou iguais a 1, eles os interpretam como números entre 0 e 1. Esse parâmetro deve ser ativado neste caso, caso contrário, poderia haver Um caso raro em que o Cura tenta ajustar a velocidade de 0,4% do ventilador (1 em 255), mas a impressora 100%.
* Algumas impressoras aceitam apenas os números entre 0 e 1. Este parâmetro também deve ser ativado neste caso, caso contrário, o ventilador sempre será completamente extinto ou completamente iluminado.
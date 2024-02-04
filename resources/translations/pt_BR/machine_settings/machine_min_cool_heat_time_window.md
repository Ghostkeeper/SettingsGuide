Duração mínima da temperatura de vigília
====
Esse ajuste configura a duração mínima de um modo de espera durante o qual o bico deve ser frio na temperatura de espera.Se o bico estiver definido para um período mais curto, ele não será resfriado, mas permanecerá em [temperatura final de impressão](../MATEMCIAL/MATTER_FINAL_PRINT_TEMPERATURA.MD).

Seu bico está equipado com um regulador PID, que regula a quantidade de energia usada para aquecer o bico para atingir as temperaturas corretas.Quando o bico é ordenado para esfriar e se aquecer com grandes diferenças de temperatura na rápida sucessão, o regulador PID tende a fornecer a quantidade de calor necessária.Isso leva a grandes flutuações na temperatura real do bico.Assim, você pode impedir que ele atinja a [temperatura de espera](../material/material_standby_temperature.md) se o bico estiver inativo por um período muito curto.

O valor ideal dessa configuração depende da configuração do seu regulador PID.Alguns reguladores gerenciam melhor as mudanças rápidas de temperatura -alvo que outras, e elas podem gerenciar melhor um breve período de espera.Abaixar esse ajuste impediria que o material se deteriorasse dentro do bico.

*Como é uma configuração da máquina, esse ajuste normalmente não é visível na lista de configurações.*
Y začátku vrstvy
====
Pokud existuje několik částí, které se mají tisknout na vrstvu, Cura optimalizuje pořadí, ve kterém se tyto části tisknou. Aby mohla součást vychladnout před tiskem další vrstvy, vytiskne každou vrstvu zhruba ve stejném pořadí. Parametry [X začátku vrstvy](layer_start_x.md) a **Y začátku vrstvy** určí, která část bude vytištěna jako první: část, která je nejblíže zadaným souřadnicím. Tento parametr určuje souřadnici Y této části.

Toto je jiné nastavení, než pro Z šev. Nastavení zarovnání švů v Z určuje pouze, kde tiskárna začne tisknout obrys součásti, zatímco toto nastavení určuje, se kterým kusem začne.

Pokud vaše tiskárna provede něco konkrétního, když začíná novou vrstvou nebo když mění extrudér, je vhodné tyto souřadnice nastavit tam, kde končí tisková hlava, když je připravena pokračovat v tisku. To minimalizuje přesuny a prosakování.

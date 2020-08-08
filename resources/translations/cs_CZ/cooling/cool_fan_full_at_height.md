Výška normální rychlosti ventilátoru
=====

Rychlost ventilátoru začíná na hodnotě parametru [počáteční rychlost ventilátoru](cool_fan_speed_0.md) na začátku tisku. Během prvních vrstev tisku, dokud nedosáhne výšky uvedené v tomto parametru, bude rychlost ventilátoru postupně zvyšována až do [normální rychlosti ventilátoru](cool_fan_speed_min.md).

![Jaká rychlost ventilátoru se používá, a kde](../images/cool_fan_speed_cs.svg)

Normálně je počáteční rychlost ventilátoru výrazně snížena, protože počáteční vrstva musí během tisku zůstat horká. Pokud se počáteční vrstva zchladí, materiál se začne [deformovat](../troubleshooting/warping.md). Tím se první vrstva odlepí od podložky tisku, což způsobí selhání tisku. Pokud však druhá vrstva zchladne příliš rychle, bude se stále zmenšovat a střihovým třením vytáhne první vrstvu nahoru a deformuje také tisk. Účelem tohoto nastavení je umožnit tisk více vrstev s nižší rychlostí ventilátoru. Tímto způsobem lze deformaci zabránit, dokud tisk nemá dostatečnou tuhost, aby deformacím odolával.

* Zvýšení tohoto nastavení může zlepšit [přilnutí k tiskové podložce](../troubleshooting/bed_adhesion_problems.md).
* Pokud je podložka tisku zahřáta na vysokou teplotu, možná budete muset toto nastavení snížit, abyste zabránili [sloní noze](../troubleshooting/elephants_foot.md) nebo výtokům.

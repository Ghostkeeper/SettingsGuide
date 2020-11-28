Množství extra materiálu plnění při přepnutí trysek
====
Toto nastavení umožňuje nakonfigurovat tiskárnu tak, aby se po přepnutí extrudéru propláchla trochu dalšího materiálu. Záměrem je obnovit tlak na trysce poté, co vytékala, zatímco jiné extrudéry tiskly nebo během přepnutí extrudéru.

Zatímco ostatní extrudéry tisknou, bude tento extrudér pozastaven. Ale během této doby to vytéká. Tuto ztrátu materiálu lze kompenzovat předáním dalšího materiálu. Tlak je poté v komoře trysky obnoven. Vytékající materiál však zůstává na špičce trysky, takže pokud nepoužíváte [aktivační věž](prime_tower_enable.md) nebo [ochranu proti výtoku](ooze_shield_enabled.md) najdete ho na straně vašeho tisku.

**Tento parametr lze konfigurovat pro každý extrudér. Konfigurované Množství materiálu je vyčištěno na *začátku* plánu tohoto extrudéru, před tiskem s materiálem.**
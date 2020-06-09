Obraz hustoty křížové výplně pro podpěru
====
V tomto parametru můžete poskytnout obrázek, který určuje hustotu na různých místech podpěry. Hustotu podpěry se v některých místech liší v závislosti na jasu obrazu. Toto funguje pouze pro [křížový vzor](../support/support_pattern.md), protože tento vzor je schopen upravit svou hustotu bez přerušení linií, což by přerušilo tok a snížilo pevnost.

![Hustota podpěry je po stranách důležitější](../../../articles/images/cross_support_density_image.png)
![Soubor obrázku použitý k vytvoření tohoto vzoru](../../../articles/images/cross_support_density_image_mask.png)

Cesta k obrázku je poskytována jako místní cesta, například `C:\Projects\3D Printing\support_density.png` ve Windows nebo `/home/ghostkeeper/3d_printing/support_density.png` v Unixu. Podporované formáty souborů jsou JPG, PNG, TGA, BMP, PSD, GIF, HDR a PIC. Jas obrázku určuje hustotu výplně:
* Tam, kde je obrázek černý, použije se [hustota podpěry](../support/support_infill_rate.md).
* Tam, kde je obrázek bílý, hustota podpěry se přiblíží 0 %.

Hustota podpěry nikdy nepřesáhne hodnotu specifikovanou v parametru [Vzdálenost linií podpěry](../support/support_line_distance.md). Lze ji pouze omezit. Vzor, kde může snížit hustotu, je rovněž omezen. I když se snaží aproximovat požadovanou hustotu podpěry co nejblíže, není to vždy možné. Pokud je hustota podpěry opravdu nízká, bude zvláště málo příležitostí hustotu podpěry upravit, což způsobí, že tisk bude sledovat obraz velmi volně. Na místech, kde je hustota podpěry vysoká, bude obraz sledován velmi pečlivě. Zvolená hustota je také silně kvantifikována. Hustotu lze zdvojnásobit nebo snížit na polovinu, ale Cura vzor [rozptyluje](https://en.wikipedia.org/wiki/Dither), aby se dosáhlo větší efektivní přesnosti.

S tímto nastavením můžete svou podpěru upravit velmi daleko. Pokud jsou některé části vašeho tisku náchylné k prohýbání nebo je třeba je tisknout velmi přesně, můžete na místě zvýšit hustotu, abyste je lépe podepřeli, aniž byste museli dělat velký zásah v době tisku nebo ztížit odejmutí podpěry. 

**Tento parametr nebude správně přenesen do projektových souborů Cura. Soubor projektu uloží cestu k obrázku jako nastavení, ale neukládá obrázek. Pokud se soubor projektu otevře na jiném počítači, obraz hustoty pravděpodobně nebude obnoven.**


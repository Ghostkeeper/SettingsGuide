Obraz hustoty křížové výplně
====
V tomto nastavení můžete poskytnout obrázek, který určuje hustotu na různých místech výplně. Hustota výplně se bude na některých místech lišit v závislosti na jasu obrazu. Toto funguje pouze pro [(3D) křížový vzor](../infill/infill_pattern.md), protože tento vzor je schopen upravit svou hustotu bez rozsekání linií, což by mělo za následek přerušený tok a sníženou pevnost.

![Hustota výplně se v objektu liší](../../../articles/images/cross_infill_density_image.png)
![Soubor obrázku použitý k vytvoření tohoto vzoru](../../../articles/images/cross_infill_density_image_mask.png)

Cesta k obrázku je poskytována jako místní cesta, například `C:\Projects\3D Printing\infill_density.png` ve Windows nebo `/home/ghostkeeper/3d_printing/infill_density.png` v Unixu. Podporované formáty souborů jsou JPG, PNG, TGA, BMP, PSD, GIF, HDR a PIC. Jas obrázku určuje hustotu výplně:
* Tam, kde je obrázek černý, použije se [hustota výplně](../infill/infill_sparse_density.md).
* Tam, kde je obrázek bílý, hustota výplně se přiblíží 0 %.

Hustota výplně nikdy nepřesáhne hodnotu určenou [vzdálenost linií výplně](../infill/infill_line_distance.md). Lze ji pouze omezit. Vzor, kde může snížit hustotu, je rovněž omezen. I když se snaží aproximovat požadovanou hustotu výplně co nejblíže, není to vždy možné. Pokud je hustota výplně opravdu nízká, bude zvláště málo příležitostí hustotu výplně upravit, což způsobí, že tisk bude sledovat obraz velmi volně. Na místech, kde je hustota výplně vysoká, bude obraz sledován velmi pečlivě. Zvolená hustota je také silně kvantifikována. Hustotu lze zdvojnásobit nebo snížit na polovinu, ale Cura vzor [rozptyluje](https://en.wikipedia.org/wiki/Dither), aby se dosáhlo větší efektivní přesnosti.

S tímto nastavením můžete svou výplň upravit velmi daleko. Protože vzory křížové výplně mají většinu použití s pružnými materiály, toto nastavení se používá k dosažení velmi specifických omezení měkkosti nebo tvrdosti. Například by bylo možné vytisknout podrážku boty s přizpůsobenou měkkostí, aby lépe seděla na nohou nebo strojní zařízení, které se musí ohýbat v určitých částech.

**Tento parametr nebude správně přenesen do projektových souborů Cura. Soubor projektu uloží cestu k obrázku jako nastavení, ale neukládá obrázek. Pokud se soubor projektu otevře na jiném počítači, obraz hustoty pravděpodobně nebude obnoven.**


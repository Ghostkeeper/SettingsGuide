Is oorsprongpunt centraal
====
Als deze instelling is ingeschakeld, bevindt de 0,0-coördinaat van de printer zich in het midden van het buildvolume in plaats van in de linkervoorhoek.

Voor sommige printers gaat de firmware ervan uit dat de 0,0-coördinaat zich in het midden van het buildvolume bevindt. Dit is gebruikelijk bij delta-printers, die meestal cilindrische bouwvolumes hebben en geen kubussen.

Als de nulcoördinaat van de printer in het midden ligt, bevat de uiteindelijke g-code zowel negatieve als positieve coördinaten. De oorsprong van de coördinaten bevindt zich in het midden van het bouwvolume van Cura. Cura toont ook zijn driekleurige coördinatenmarkering in het midden. De coördinaten van 3MF-bestanden worden echter nog steeds behandeld alsof de oorsprong van de coördinaten zich in de linkervoorhoek van de printer bevindt, aangezien het 3MF-bestandsformaat dit vereist.

**Omdat dit een apparaatinstelling is, wordt deze normaal gesproken niet vermeld in de normale lijst met instellingen. Er is echter een selectievakje voor deze instelling in het dialoogvenster Printerinstellingen, dat u kunt vinden in de lijst met toegevoegde printers in het dialoogvenster Instellingen.**
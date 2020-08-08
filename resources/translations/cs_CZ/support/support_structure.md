Struktura podp�ry
====
S t�mto nastaven�m si m��ete vybrat, kter� algoritmus pou�ijete k vytvo�en� podp�rn�ch struktur. Tyto konstrukce maj� v�razn� odli�n� vlastnosti, tak�e v�b�r algoritmu bude m�t velk� vliv na to, jak dob�e bude v� tisk podp�r�n. K dispozici jsou dv� mo�nosti.

Norm�ln�
----
![Norm�ln� podp�rn� konstrukce](../../../articles/images/support_type_everywhere.png)

Jedn� se o tradi�n� podp�rnou strukturu, na kterou je v�t�ina lid� zvykl�. Struktura je generov�na pod p�evisl�mi oblastmi a obvykle je vypln�na vzorem, kter� p��mo podp�r� p�evisl� oblasti. Odtud kles� p��mo dol�, dokud nedos�hne tiskovou podlo�ku nebo ��sti modelu, kterou podp�r�.

Norm�ln� konstrukce podp�ry byla v�choz� pro v�t�inu historie 3D tisku a funguje podobn� ve v�ech slicerech. Toto je zlat� standard, a ne bez d�vodu:
* D�ky sv� robustn� struktu�e, velk�m kontaktn�m ploch�m na modelu a podlo�ce tisku je velmi spolehliv�. Odpou�t� velmi �patn� nastaven� nebo �patn� nalad�n� tisk�rny.
* Proto�e je tvar jednoduch�, lze ji rychle slicovat.
* P��mou strukturu podp�ry lze snadno p�izp�sobit pro u�ivatele, proto�e je okam�it� jasn�, kter� hranice budou podp�r�ny a kter� nikoli.

Nejd�le�it�j�� nev�hody vypl�vaj� ze stejn�ch vlastnost�:
* D�ky velk�m kontaktn�m oblastem je podp�ra �asto obt�n� odstraniteln� a m��e na povrchu, kde se dot�k�, zanechat zna�n� jizvy.
* P�esto�e je stabiln�, m��e spot�ebovat spoustu materi�lu a tisk m��e zabrat spoustu �asu. To lze do ur�it� m�ry potla�it pomoc� [k�nick� podp�ry](../experimental/conical_overhang_enabled.md).

Proto�e podp�ra bude obvykle velk� a �irok�, je pro spr�vn� podep�en� povrchu pot�eba [v�pl�ov� vzor](support_pattern.md). Cik-cak vzor v�pln� m��e b�t pou�it k tisku podp�ry z velk� ��sti z jedn� linie a pro umo�n�n� snadn�j��ho odstran�n�. Dal�� vzory lze kombinovat s extra [obrysy](support_wall_count.md) aby byla podp�ra m�sto toho robustn�.

Strom
----
![Stromov� podp�ra](../../../articles/images/support_structure_tree.png)

P�i stromov� podp��e za�ne podp�rn� struktura na desce sestavy mal� a jej� v�tve rostou sm�rem k ��stem tisku, kter� pot�ebuj� podep��t.

Stromov� podp�ra se m��e vyhnout p�ek�k�m, kdy� roste sm�rem k p�evisl�m oblastem, proto�e nemus� spl�vat p��mo dol�. Pokud je to v�bec mo�n�, bude podp�ra spo��vat pouze na tiskov� podlo�ce, aby se zabr�nilo zjizven� povrchu, na kter�m podp�ra spo��v�. Pokud z podlo�ky tisku k p�evisu neexistuje ��dn� cesta, bude podp�ra spo��vat na povrchu, kter� je co nejbl�e p�evisu, aby se minimalizovalo pou�it� materi�lu. V�tve stromov� podp�ry jsou omezeny hodnotou parametru [�hel v�tve stromov� podp�ry](support_tree_angle.md) tak�e samotn� nevytv��� p��li� strm� p�evis. To omezuje schopnost r�st kolem p�ek�ek a tak� ur�uje v��ku, ve kter� se kmeny za�nou rozv�tvovat.

Konstrukce stromov� podp�ry m� oproti b�n� podp��e �adu velk�ch v�hod:
* Stromov� podp�ra �asto pou��v� mnohem m�n� materi�lu ne� b�n� podp�ra. B�n� je 25 a� 50% vyu�it� materi�lu. To �et�� spoustu �asu a sni�uje n�klady na tisk.
* Vzhledem k jeho mal� kontaktn� plo�e m� p�evis p�i pou�it� stromov� podp�ry tendenci vypadat l�pe.
* Tak� d�ky mal� kontaktn� oblasti bude podp�ru snadn�j�� odstranit.
* Zanech�v� na povrchu m�n� jizev ne� b�n� podp�ra, proto�e je schopna se pohybovat kolem modelu od tiskov� podlo�ky sm�rem k p�evisu.

Hlavn� nev�hody jsou:
* Slicov�n� trv� podstatn� d�le ne� norm�ln� podp�ra. Bude zapot�eb� trp�livosti, zejm�na u vysok�ch model�.
* P�i tisku nejmen��ch v�tv� doch�z� v toku k mnoha p�eru�en�m, co� zp�sobuje, �e stromov� podp�ra nen� vhodn� pro tisk pomoc� materi�l�, kter� lze t�ko vytla�ovat, jako je PVA nebo pru�n� materi�ly.
* Stromov� podp�ra nefunguje dob�e pro podp�r�n� n�kter�ch mechanick�ch model�. Zejm�na m� tendenci um�s�ovat p��li� m�lo v�tv� na podporu ploch�ch, �ikm�ch p�evis�.

Ve v�choz�m nastaven� je stromov� podp�ra dut�. V�tve budou m�t mal� hrot, tak�e v�pl�ov� vzor neposkytuje zvl�tn� podporu pro p�evisl� povrch ti�t�n� polo�ky. D�ky sv�mu zubat�mu tvaru je stromov� podp�ra obvykle pom�rn� robustn�. B�n� nastaven� podp�ry v�ak st�le plat� pro oblast ohrani�enou v�tvemi stromu. Pro zv��en� pevnosti podp�rn� struktury m��e b�t pou�it parametr [Hustota podp�ry](support_infill_rate.md).
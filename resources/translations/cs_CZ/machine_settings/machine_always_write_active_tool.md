V�dy zapsat aktivn� n�stroj
====
Toto nastaven� ud�v�, jak tisk�rna interpretuje ur�it� p��kazy g-k�du s parametrem n�stroje. N�kter� p��kazy g-k�du mohou zahrnovat parametr, kter� ozna�uje, na kter� extrud�r se vztahuje. N�kter� firmware interpretuje tento parametr jako p��kaz k p�epnut� na tento n�stroj a pot� spou�t� g-k�d, zat�mco jin� firmware interpretuje tento parametr jako p��kaz, aby aplikoval g-k�d na jin� extrud�r, ne� je ten, kter� je aktu�ln� aktivn�..

Jedin� p��kazy, kter� se vztahuj� na 3D tisk, jsou p��kazy oh�evu trysek, `M104` a `M109`. Vezm�te n�sleduj�c� p��klad p��kazu oh�evu, prov�d�n�ho b�hem tisku prvn�ho extrud�ru (`T0`):

`M104 S210 T1`

Tento p��kaz lze interpretovat dv�ma zp�soby:
* Zat�mco pokra�ujete v tisku prvn�m extrud�rem, za�n�te zah��vat druh� extrud�r na 210 �C. Toto je interpretace Marlin, Reprap, Sailfish a jejich odvozen�ch firmwarov�ch bal��k�.
* Nejprve p�epn�te na druh� extrud�r, pot� zah�ejte druh� extrud�r na 210 �C. Toto je interpretace spole�nosti Smoothieware a jeho odvozen�ho firmwaru.

Vzhledem ke strategii regulace teploty Cury, nemus� nikdy prov�d�t druhou interpretaci. Pokud tisk�rna interpretuje p��kaz g-k�du druh�m zp�sobem, Cura m�sto toho zap�e n�sleduj�c� g-k�d:

`M104 S210 T1`

`T0`

V podstat� v�, �e tisk�rna se p�epne na druh� extrud�r kv�li tomuto p��kazu, a proto mus� p�epnout zp�t na prvn� extruder, aby tam pokra�ovala v tisku.
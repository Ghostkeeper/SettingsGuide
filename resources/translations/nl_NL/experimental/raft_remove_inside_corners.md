Binnenhoeken raft verwijderen
====
Wanneer deze instelling is ingeschakeld, worden alle binnenhoeken van het raft volledig verwijderd, waardoor het raft een [convexe vorm](https://en.wikipedia.org/wiki/Convex_set) krijgt. Het raft heeft dan alleen buitenhoeken.

<!--screenshot {
"image_path": "raft_remove_inside_corners.png",
"modellen": [{"script": "microwave_hook.scad"}],
"camerapositie": [59, 59, 200],
"instellingen": {
	"adhesion_type": "raft",
	"raft_remove_inside_corners": true
},
"kleuren": 64
}-->
![Het raft volgt niet langer de vorm van het model](../../../articles/images/raft_remove_inside_corners.png)

Dit komt in principe overeen met een zeer hoge [Raft effenen](../platform_adhesion/raft_smoothing.md). Het verwijderen van de binnenhoeken van het raft heeft een aantal effecten:
* Het is niet meer mogelijk dat een klein deel van het raft ver boven de rest van het raft uitsteekt. Kleine delen van het raft zullen eerder losraken van de platform, vooral bij sterk vervormde materialen. Het verwijderen van de binnenhoeken vermindert dit effect, waardoor de print betrouwbaarder wordt.
* Het raft is groter, waardoor de totale hechtkracht op de platform toeneemt.
* Het printen van het raft duurt langer en gebruikt meer materiaal.
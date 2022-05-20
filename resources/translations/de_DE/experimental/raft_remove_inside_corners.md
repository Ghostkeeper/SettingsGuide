Innenecken des Rafts entfernen
====
Wenn diese Einstellung aktiviert ist, werden alle inneren Ecken des Floßes vollständig entfernt, wodurch das Floß zu einer [konvexen Form](https://en.wikipedia.org/wiki/Convex_set) wird. Das Raft hat dann nur noch Außenecken.

<!--screenshot {
"image_path": "raft_remove_inside_corners.png",
"models": [{"script": "microwave_hook.scad"}],
"camera_position": [59, 59, 200],
"settings": {
	"adhesion_type": "raft",
	"raft_remove_inside_corners": true
},
"colours": 64
}-->
![Das Raft folgt nicht mehr der Form des Modells](../../../articles/images/raft_remove_inside_corners.png)

Dies entspricht im Grunde einer sehr hohen [Glättung](../platform_adhesion/raft_smoothing.md). Das Entfernen der Innenecken aus dem Raft hat eine Reihe von Auswirkungen:
* Es ist nicht mehr möglich, dass ein kleiner Teil des Rafts weit über den Rest des Rafts hinaus ragt. Es ist wahrscheinlicher, dass sich kleine Teile des Rafts von der Bauplatte lösen, besonders bei stark verziehenden Materialien. Durch das Entfernen der Innenecken wird dieser Effekt verringert, wodurch der Druck zuverlässiger wird.
* Das Raft ist größer, wodurch sich die gesamte Haftkraft auf der Bauplatte erhöht.
* Das Drucken des Rafts dauert länger und verbraucht mehr Material.
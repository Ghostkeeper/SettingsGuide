Brim距离
====
此设置会导致模型与Brim之间出现间隙。Brim线不再与模型牢固相邻。


<!--screenshot {
"image_path": "brim_gap.png",
"models": [
{
"script": "arrow.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [-22, 32, 133],
"settings": {
"adhesion_type": "brim",
"brim_gap": 1
},
"colours": 32
}-->
![Brim与模型保持一定距离](../images/brim_gap.png)

此间隙的目的是为了更容易地从模型中移除Brim。通过将Brim线与实际模型稍微分开放置（大约为线宽度的一半），Brim和模型之间的连接将变得比整层弱，这有助于用手撕下Brim。它还将减少Brim删除后留下的伤痕或象脚。这在较大的[起始层高](../resolution/layer_height_0.md)时尤其有效，因为较厚的Brim往往更难移除。

另一方面，这也降低了Brim保持模型粘在构造板上的有效性。通过较薄的接触区域，Brim将无法在模型上施加很大的力，以保持其向下，从而抵抗[翘曲](../troubleshooting/warping.md)。

Raft 平滑度
====
使用此设置，可以使Raft 的内角更平滑。该设置指定圆弧的半径。所有比指定圆弧半径更尖锐的内角都将被平滑化以具有圆弧半径。

<!--screenshot {
"image_path": "raft_smoothing_0mm.png",
"models": [{"script": "question_stick_clip.scad"}],
"camera_position": [0, 97, 191],
"settings": {
"adhesion_type": "raft",
"raft_smoothing": 0
},
"layer": 509,
"colours": 64
}-->
<!--screenshot {
"image_path": "raft_smoothing_5mm.png",
"models": [{"script": "question_stick_clip.scad"}],
"camera_position": [0, 97, 191],
"settings": {
"adhesion_type": "raft",
"raft_smoothing": 5
},
"layer": 509,
"colours": 64
}-->
![未平滑](../images/raft_smoothing_0mm.png)
![平滑半径5mm](../images/raft_smoothing_5mm.png)

专业术语为[形态闭合运算](https://en.wikipedia.org/wiki/Closing_\(morphology\))。所有小于指定半径的孔都将被封闭。最锐利的内角将不再锐利。

该设置的功能是使Raft 更坚硬。当多个部件通过薄连接件连接时，Raft 可以在那些地方弯曲。这使得它们的硬度和抗翘曲性较低。增加此设置将使各个部分更好地连接，从而使Raft 更坚固。Raft 的表面积会更大，所以Raft 会粘得更好。此外，Raft 的总周长将更小，从而减少了开始翘曲的地方。总的来说，翘曲应该较少。

然而，Raft 的总体积也将增加。这使用了更多的材料，需要更多的时间来打印，特别是因为Raft 通常打印得非常慢。

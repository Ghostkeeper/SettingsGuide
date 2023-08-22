支撑块走线数
====
如果[将支撑结构分拆为块装](support_skip_some_zags.md)，则此设置确定将有多少支持线合并到一个块中。

<!--screenshot {
"image_path": "support_skip_some_zags.png",
"models": [{"script": "rack.scad"}],
"camera_position": [0, 184, 10],
"settings": {
"support_enable": true,
"support_pattern": "zigzag",
"support_skip_some_zags": true,
"support_skip_zag_per_mm": 20
},
"colours": 32
}-->
![每个区块包含8条线](../images/support_skip_some_zags.png)

较小的块状物往往比较大的块状物更容易折断。粘在模型上的表面积更小，所以将支撑物拉开所需的力更小。然而，也会有更多的大块需要拉离，因此，如果拉离支架通常并不困难，这可能会使拉离支架的工作量更大。然后每一块都要单独拉下来，而不是把所有的支撑都拉下来一大块。

如果将块制成非常小，则可能损害支撑件的结构完整性。支撑图案将更类似于线条图案，从而更有可能发生翻倒。这将导致支撑下跌的地方有更多的拉丝和更差的悬垂质量。

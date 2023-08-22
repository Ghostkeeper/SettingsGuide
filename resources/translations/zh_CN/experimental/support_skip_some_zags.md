将支撑结构分拆成块状
====
如果使用锯齿[图案](../support/support_pattern.md)作为支撑，则可以将支撑弄皱，这是移除支撑的一种简单方法。如果支撑很宽，这就变得更加困难。在这种设置下，锯齿形支撑被分解成更容易单独折断但仍足够宽以保持其稳定性的碎片。

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
![每8行省略一个连接行，将支持拆分为块](../images/support_skip_some_zags.png)

将支撑分成几块，这样更容易将支撑折断，因为您可以一次折断一块支撑。不过，这确实会略微降低支持面的强度和刚度，尤其是在[支撑块大小](support_skip_zag_per_mm.md) 设置为非常小的情况下。因此，支持翻倒的机会稍大，导致大量的拉丝和坏的悬垂。

该设置还可防止将所有支撑整体拉出。如果有多个支撑件，则必须单独取下。如果支持脱落足够容易，否则，这个设置实际上可能会为拉下支持（虽然它可能仍然更容易）做更多的工作。

此设置不能与[支撑墙行数](../support/support_wall_count.md)很好地结合使用。如果支撑物周围有一堵额外的墙，那堵墙会再次连接这些块，使它们更难折断。

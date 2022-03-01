Break Up Support In Chunks
====
If the zigzag [pattern](../support/support_pattern.md) is used for support, the support can be crumpled up as an easy way to remove the support. This becomes more difficult if the support is very wide. With this setting, the zigzag support is broken up into pieces that are easier to break off individually but are still wide enough to maintain their stability.

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
![Every 8 lines a connecting line is left out, breaking the support up in chunks](../images/support_skip_some_zags.png)

Breaking the support up in chunks makes it easier to break the support off, because you can break the support one piece at a time. This does reduce the strength and rigidity of the support slightly though, especially if the [chunk size](support_skip_zag_per_mm.md) is set to be very small. As a result, there is a slightly greater chance for the support to fall over, resulting in lots of stringing and bad overhangs.

This setting also prevents pulling off all of the support in one piece. If there are many pieces of support, they have to be taken off individually. If the support comes off easily enough otherwise, this setting may actually make it more work to pull off the support (albeit it might still be easier).

This setting doesn't combine well with [Support Wall Line Count](../support/support_wall_count.md). If the support has an extra wall around it, that wall will connect the chunks again, making it harder to break pieces off.
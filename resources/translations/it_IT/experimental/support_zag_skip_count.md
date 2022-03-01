Support Chunk Line Count
====
If the support is [broken up in chunks](support_skip_some_zags.md), this setting determines how many lines of support will be combined into one chunk.

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
![Each chunk contains 8 lines](../images/support_skip_some_zags.png)

Smaller chunks tend to be easier to break off than larger chunks. There is less surface area to stick to the model, so it will require less force to pull the support away. However there will also be more chunks to pull away, so if pulling off the support is not normally difficult, this may make pulling off support more work. Each piece has to be pulled off individually then, instead of pulling all of the support off in one big chunk.

If the chunks are made to be very small, the structural integrity of the support may be compromised. The support pattern will resemble the lines pattern more then, which has a greater chance of falling over. This would result in more stringing and worse overhang quality in places where the support fell over.
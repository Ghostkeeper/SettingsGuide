Skin Overlap
====
This setting makes the skin overlap a bit with the adjacent structures. This makes the skin adhere better to those structures.

<!--screenshot {
"image_path": "skin_overlap_none.png",
"models": [{"script": "mounting_plate.scad"}],
"camera_position": [0, 0, 84],
"settings": {
    "skin_outline_count": 0,
    "skin_overlap": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "skin_overlap_20.png",
"models": [{"script": "mounting_plate.scad"}],
"camera_position": [0, 0, 84],
"settings": {
    "skin_outline_count": 0,
    "skin_overlap": 40
},
"colours": 64
}-->
![No overlap](../images/skin_overlap_none.png)
![Some overlap](../images/skin_overlap_20.png)

This overlap technically produces overextrusion, but the amount of overextrusion is small enough that it won't be visible. It will have a significant influence on the strength though, because the skin can adhere better to the walls and infill. After all, these structures only add to the strength of the model if they have something to hold on to.

Having a bit of overlap can also help to reduce the occurrence of gaps in the skin.
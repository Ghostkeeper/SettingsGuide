Remove Raft Inside Corners
====
When this setting is enabled, all inside corners of the raft are completely removed, turning the raft into a [convex shape](https://en.wikipedia.org/wiki/Convex_set). The raft will only have outside corners.

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
![The raft doesn't follow the shape of the model any more](../images/raft_remove_inside_corners.png)

This is effectively equivalent to having a very high [smoothing](../platform_adhesion/raft_smoothing.md). Removing inside corners from the raft has a number of effects:
* It's no longer possible for a small part of the raft to protrude far beyond the rest of the raft. Small parts of the raft are more likely to get loose from the build plate, especially with highly warping materials. Removing the inside corners reduces that effect, making the print more reliable.
* The raft is bigger, increasing the total adhesion force to the build plate.
* The raft takes longer to print and uses more material.
Cubic Subdivision Shell
====
This setting makes the Cubic Subdivision infill pattern start reducing infill a bit more towards the inside, to improve the strength of the print.

![Cubic Subdivision with no additional shell](../images/sub_div_rad_add_small.png)
![Additional shell of 5mm](../images/sub_div_rad_add_large.png)

Cubic Subdivision works by removing the borders between eight adjacent cubes if none of the cubes touch the border of the infill volume. This setting moves that border further inside, preventing the borders between the cubes from being removed.

Effectively, this causes the Cubic Subdivision pattern to draw the maximum density more often. This increases the strength of the object, but also increases the amount of time and material it takes to print it. In the extreme, increasing this setting enough will eventually cause the Cubic Subdivision pattern to be the same as the simple Cubic pattern.

You can also set this to a negative number. This causes the borders between cubes to be removed more often, effectively reducing the amount of infill around the edges.
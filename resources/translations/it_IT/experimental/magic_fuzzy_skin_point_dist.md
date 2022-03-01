Fuzzy Skin Point Distance
====
This setting configures the distance along the original wall between movements for the fuzzy skin. If the distance is small, the print head will move in different directions very often along the wall. It will vibrate at high frequency.

With smaller distances, the roughness will be more fine, resulting in a rougher texture. This also affects the printing time significantly. To create a smoother, but bumpy texture, you can increase the distance.

When Fuzzy Skin is enabled, the outer wall will consist entirely of straight line segments between the vibration movements, instead of the original surface. With high distances, it could happen that curved surfaces are not very curved any more because the original resolution was higher than the density of coordinates due to the fuzzy skin effect.

Due to algorithmic constraints, the distance between points can't be too small if the [thickness](magic_fuzzy_skin_thickness.md) is very high.
This setting configures the frequency at which the nozzle vibrates as it moves along the wall. At a higher density, the nozzle will move up and down more often along the surface. The "density" here refers to the density of points in which the nozzle can change direction.

At higher density, the roughness will be more fine, resulting in a rougher texture. This also affects the printing time significantly. To create a smoother, but bumpy texture, you can reduce the density.

When Fuzzy Skin is enabled, the outer wall will consist entirely of straight line segments between the vibration movements, instead of the original surface. With a low density, it could happen that curved surfaces are not very curved any more because the original resolution was higher than the density of coordinates due to the fuzzy skin effect.

Due to algorithmic constraints, the density can't be increased too far if the [thickness](magic_fuzzy_skin_thickness.md) is very high.
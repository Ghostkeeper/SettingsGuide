Jerk determines the speed at which the nozzle can go through corners. If jerk control is enabled, Cura will take control of how much jerk to apply during various parts of the print. If it's disabled, the printer firmware will choose a jerk value. The printer's jerk value is typically fairly high as to give more control to the slicer, but it may have more information about its own hardware than Cura has. 

![The relation between velocity, acceleration and jerk](images/velocity_acceleration_jerk.svg)

**Jerk in 3D printing is not the same as jerk in physics.** The term "jerk" was introduced by Marlin. It was designed there as a workaround for the inherent problem in trying to perfectly follow a path. Since the nozzle is not allowed to deviate from the path (in theory), the nozzle would need to decelerate to 0mm/s in every corner. This would ruin your print, because decelerating to 0mm/s would cause a blob in every corner. It is not allowed to make curves to shortcut the corner, nor can it overshoot. Instead, Marlin allows for an instantaneous change in the velocity vector in every corner. The magnitude of this change in the velocity vector is coined "jerk".

So jerk is the maximum instantaneous change in velocity, applied at every corner of the motion.

Firmware that is not based on Marlin, such as the Sailfish firmware family, will ignore changes in jerk. This setting will not have any effect then.

Example mathematics of jerk
----
As an example, take a very simple print: First move 100mm to the right, then move 100mm down. The printing speed is set to 50mm/s. Acceleration is set to 1000mm/s^2. Jerk is set to 10mm/s. This is what will happen:
1. At the start of a print, Marlin takes half of the jerk value to start, so it will theoretically accelerate to 5mm/s instantaneously.
2. At an acceleration of 1000mm/s^2, it will take 0.045s to accelerate from 5mm/s to the maximum velocity of 50mm/s. During this time, the nozzle will cover 1.2375mm.
3. The nozzle cruises for a while at 50mm/s, the maximum printing velocity.
4. Marlin will calculate at which speed the nozzle may go through the corner: The nozzle will make a 90 degree corner, first going to the right, then going downwards. To limit this velocity change, it's going to go into the corner at cos(90/2) * (10/2)mm/s going to the right, and exit at cos(90/2) * (10/2)mm/s going down. So it'll go through the corner at about 7.07mm/s.
5. It will take 0.043s to decelerate from a speed of 50mm/s to 7.07mm/s.
6. The corner is made with an instantaneous velocity change. The magnitude of the difference between the vectors [7.07, 0] and [0, 7.07] is exactly 10mm/s, so it can make this corner instantaneously.
7. It will take 0.043s to accelerate from 7.07mm/s to 50mm/s.
8. The nozzle cruises for a while again at 50mm/s, the maximum printing velocity.
9. Towards the end of the print, the nozzle will decelerate from 50mm/s to 0mm/s in 0.05s.
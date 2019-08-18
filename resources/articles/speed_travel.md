This setting configures the speed at which the print head moves when it's not extruding any material.

![Various structures printed at different speeds](images/speed_difference.png)

The travel speed is generally much higher than any other speed setting. Some effects of increasing the travel speed include:
* A higher travel speed can slightly reduce the print time.
* It will reduce the time that the filament has to ooze out of the material, making a cleaner part overall with smaller blobs due to oozing.
* However, increasing the speed also tends to make the printer vibrate more, which increases ringing. This can be reduced with Z hops, but the Z hop will often take more time than can be saved by increasing the travel speed.
* Increasing the speed increases the chance of your print being knocked over, especially if [combing](retraction_combing) is disabled.
* When taken to extreme speeds, the motors of the printer might also lose some steps, causing a layer shift.

**The travel speed has less of an effect on the total printing time than most people assume. This is because the travel time is usually only a small fraction of the total printing time, and because it takes a long time for the high speeds are reached, being limited mostly by acceleration rather than maximum speed.**
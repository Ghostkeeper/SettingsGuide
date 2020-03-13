Normally, Cura doesn't bother to make the nozzle avoid support structures as well when [avoiding other parts](travel_avoid_other_parts.md). With this setting, Cura will avoid hitting support structures while travelling.

Support doesn't need to be pretty, so it's not a problem if a blob ends up on support. In fact, this may prevent the blob from appearing on the wall. Also, a scar in the support is not a problem for its function. However, if the material oozes a lot and the blob from that ooze is applied on the same location on the support in every layer, then this blob can build up big, eventually causing the nozzle to knock over the support structure. In that case, avoiding support when travelling may be beneficial.

Some advantages and disadvantages of enabling this setting include:
* Greater reliability because there is a lower chance to knock over support by hitting the same blob repeatedly.
* Slightly longer travel moves and more oozing as a result.
* The ooze will not get wiped off on the support, but ends up on the wall of the part that the nozzle travels to.
* There might not be any path that avoids support as well, in which case the printer will resort to a retraction and travelling in a straight line, which incurs extra time and might leave extra scars on the walls.
steps = 5;
stepsize = 10;
for(step = [0:steps]) {
	translate([0,0,step * stepsize]) {
		cube([(steps - step) * stepsize, stepsize, stepsize]);
	}
}
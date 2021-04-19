width = 5;

module bridge(height, length) {
	cube([width, width, height]);
	translate([width + length, 0, 0]) {
		cube([width, width, height]);
	}
	translate([0, 0, height]) {
		cube([width + length + width, width, width]);
	}
}

h = 5;
anglestep = 10;
for(a = [0:anglestep:90]) {
	rotate([0,0,a]) {
		bridge(h, 20);
	}
	h = h + a / anglestep * width;
}
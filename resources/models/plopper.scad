$fn = 60;

difference() {
	sphere(r=20);
	sphere(r=18);
	translate([-20, -20, -20])
		cube([40, 40, 20]);
}
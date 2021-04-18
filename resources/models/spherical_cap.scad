$fs = 0.4;
$fa = 1;

difference() {
	sphere(r=20);
	scale([1, 0.95, 1]) {
		sphere(r=19);
	}
	translate([-20, -20, 0]) {
		cube(40);
	}
	translate([-20, -20, -50]) {
		cube(40);
	}
}
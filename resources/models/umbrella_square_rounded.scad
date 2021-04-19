$fs = 0.3;
$fa = 1;

cube(10);
translate([-10, -10, 10]) {
	minkowski() {
		cube([30, 30, 9]);
		cylinder(r=5, h=1);
	}
}
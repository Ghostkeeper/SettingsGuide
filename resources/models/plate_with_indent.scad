$fs = 0.2;
$fa = 1;

difference() {
	minkowski() {
		cube([40, 30, 5]);
		scale([1, 1, 0]) {
			cylinder(r=4, h=1);
		}
	}
	translate([2, 2, -1]) {
		cylinder(r=1.5, h=7);
	}
	translate([2, 28, -1]) {
		cylinder(r=1.5, h=7);
	}
	translate([38, 2, -1]) {
		cylinder(r=1.5, h=7);
	}
	translate([30, 20, 2]) {
		cylinder(r=10, h=4);
	}
}
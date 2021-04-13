$fs = 0.5;
$fa = 1;

difference() {
	cube([80, 40, 5]);
	translate([20, 20, -1]) {
		cylinder(r=15, h=7);
	}
	translate([60, 20, -1]) {
		difference() {
			cylinder(r=15, h=7);
			cylinder(r=5, h=7);
		}
	}
}
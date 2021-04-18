$fs = 0.3;
$fa = 1;

difference() {
	cylinder(r=15, h=5);
	translate([0, 0, -1]) {
		cylinder(r=10, h=7);
	}
}
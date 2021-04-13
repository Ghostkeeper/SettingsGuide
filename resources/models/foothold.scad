$fs = 0.2;
$fa = 1;

difference() {
	union() {
		minkowski() {
			scale([1, 1, 0]) {
				cube([30, 10, 10]);
			}
			cylinder(r1=4, r2=0, h=10);
		}
		minkowski() {
			translate([15, 0, 0]) {
				scale([1, 1, 0]) {
					cube([15, 10, 2]);
				}
			}
			cylinder(r1=4, r2=0, h=12);
		}
	}
	cube([30, 10, 10]);
}
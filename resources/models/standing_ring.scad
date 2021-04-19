$fs = 0.3;
$fa = 1;

rotate([-90, 0, 0]) {
	difference() {
		union() {
			cylinder(r=20, h=10);
			translate([-20, 0, 0]) {
				cube([40, 20, 10]);
			}
		}
		translate([0, 0, -1]) {
			cylinder(r=16, h=12);
		}
	}
}
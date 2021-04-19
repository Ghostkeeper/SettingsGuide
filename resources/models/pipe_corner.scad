$fs = 0.3;
$fa = 1;

rotate([0, -90, 0]) {
	rotate_extrude(angle=90) {
		translate([30, 0, 0]) {
			difference() {
				union() {
					circle(r=30);
					translate([-30, -30]) {
						square([30, 60]);
					}
				}
				circle(r=25);
			}
		}
	}
}
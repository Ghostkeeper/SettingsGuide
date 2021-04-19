$fs = 0.2;
$fa = 1;

intersection() {
	rotate([90, 0, 0]) {
		difference() {
			cylinder(r=30, h=10);
			translate([0, 0, -1]) {
				cylinder(r=25, h=2);
			}
			translate([0, 0, 9]) {
				cylinder(r=25, h=2);
			}
		}
		for(a = [90:20:270]) {
			translate([0, 0, 5]) {
				rotate([90, 0, a]) {
					cylinder(r=3, h=45);
					translate([0, 0, 45]) {
						cylinder(r1=3, r2=0, h=3);
					}
				}
			}
		}
	}
	translate([-100, -100, 0]) {
		cube(200);
	}
}
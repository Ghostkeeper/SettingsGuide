$fn = 180;

difference() {
	union() {
		cylinder(r1=5, r2=20, h=5);
		cylinder(r=5, h=25);
		translate([0, 0, 5]) {
			for(i=[0:10 / $fn:10]) {
				cylinder(r1=5 + pow(10 - i, 2) / 10, r2=5, h=pow(i, 2) / 10);
			}
		}
	}
	translate([-20, 0, 15]) {
		rotate([0, 90, 0]) {
			cylinder(r=3, h=40);
		}
	}
}
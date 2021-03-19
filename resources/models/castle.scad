$fs = 0.4;
$fa = 1;

module tower(r=15, h=50, thickness=3) {
	difference() {
		cylinder(r=r, h=h);
		translate([0, 0, h - thickness * 2]) {
			cylinder(r=r - thickness, h=thickness * 2 + 1);
		}
		translate([0, 0, h - thickness]) {
			num_crenelations = round(r * PI / 2 / thickness);
			for(a = [0 : 360 / num_crenelations : 360]) {
				rotate([0, 0, a]) {
					hull() {
						cylinder(r=0.01, h=thickness + 1);
						translate([r + thickness, 0, 0]) {
							cylinder(r=thickness, h=thickness + 1);
						}
					}
				}
			}
		}
	}
}

tower();
translate([15, 0, 20]) {
	tower(r=10, h=20, thickness=2);
}
for(i = [0:8]) {
	rotate([0, 0, i * 138]) {
		translate([14.5, -1, 4 + i * 5]) {
			cube(2);
		}
	}
}
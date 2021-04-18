//Physical.
m3_radius = 1.5;
m3_nut_radius = 3.1;
m3_nut_thickness = 2.4;
print_play = 0.2;

//Preferences.
box_radius = 60;
box_height = 150;
thickness = 3;
box_grooves = 8;
box_groove_depth = 6;
lid_lip_length = 10;
$fs = 0.4;
$fa = 1;

module m3_nut() {
	cylinder(r=m3_nut_radius + print_play, h=m3_nut_thickness + print_play * 2, $fn=6);
}

module lid() {
	difference() {
		union() {
			cylinder(r=box_radius + thickness * 3, h=thickness);
			cylinder(r=box_radius - print_play * 3, h=thickness + lid_lip_length * 2); //Need lots of extra play for blips here.
		}
		translate([0, 0, thickness]) {
			cylinder(r=box_radius - box_groove_depth, h=lid_lip_length * 2);
			linear_extrude(height=box_height + thickness, twist=120) {
				for(i = [0 : box_grooves]) {
					rotate([0, 0, i / box_grooves * 360]) {
						translate([box_radius - box_groove_depth - thickness, -box_groove_depth / 2 - print_play * 2]) {
							square([box_groove_depth + thickness, box_groove_depth + print_play * 4]);
						}
					}
				}
			}
		}
		twist_at_screwholes = lid_lip_length / (box_height + thickness * 3) * 120;
		rotate([0, 0, twist_at_screwholes * 2]) {
			translate([-box_radius, 0, thickness + lid_lip_length]) {
				rotate([0, 90, 0]) {
					cylinder(r=m3_radius + print_play, h=box_radius * 2);
					translate([0, 0, box_groove_depth / 2 - m3_nut_thickness / 2]) {
						hull() {
							m3_nut();
							translate([m3_nut_radius + print_play, 0, 0]) {
								m3_nut();
							}
						}
					}
					translate([0, 0, box_radius * 2 - box_groove_depth / 2 - m3_nut_thickness / 2]) {
						hull() {
							m3_nut();
							translate([m3_nut_radius + print_play, 0, 0]) {
								m3_nut();
							}
						}
					}
				}
			}
		}
	}
}

translate([box_radius * 2 + thickness * 2 + 20, 0, 0]) {
	lid();
}
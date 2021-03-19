//Measurements.
wood_thickness = 6.0; //Actually 5.7 but with some play.
screw_height = 42.5;
screw_radius = 1.5;
cord_gap_width = 12; //Actually 11.5 but with some play.
phone_width = 75; //Actually 74.5 but with some play.
phone_thickness = 9.5; //Actually 9.2 but with some play.
jack_gap_width = 16.3; //Actually 15.9 but with some play.
jack_gap_position = 20.3;

//Settings.
thickness = 2;
screw_holder_thickness = 7; //Bit thicker here please.
height = 30;
back_height = 5;
$fs = 0.1;
$fa = 1;

//Actual model.
//-------------
cube([phone_width, thickness, thickness + back_height]); //Backplate.

difference() {
	union() {
		cube([phone_width, thickness + wood_thickness + thickness + phone_thickness + thickness, thickness]); //Bottom plate.
		translate([0, thickness + wood_thickness + thickness + phone_thickness, thickness]) {
			cube([phone_width, thickness, height]); //Front plate.
		}
	}
	translate([phone_width - jack_gap_position - jack_gap_width / 2, thickness + wood_thickness + thickness, 0]) {
		cube([jack_gap_width, phone_width + thickness, thickness + height]); //Jack gap.
	}
	translate([phone_width / 2 - cord_gap_width / 2, thickness + wood_thickness + thickness, 0]) {
		cube([cord_gap_width, phone_width + thickness, thickness + height]); //Cord gap.
	}
	translate([phone_width / 2 + cord_gap_width / 2, thickness + wood_thickness + thickness + phone_thickness, thickness]) {
		cube([phone_width / 2 - cord_gap_width / 2 - jack_gap_position - jack_gap_width / 2, thickness, height]); //Pin between cord gap and jack gap doesn't extend upwards.
	}
}

translate([0, thickness + wood_thickness, thickness]) {
	difference() {
		hull() {
			cube([phone_width, thickness, back_height]);
			translate([phone_width / 2, 0, screw_height]) {
				rotate([-90, 0, 0]) {
					cylinder(r=screw_radius + screw_holder_thickness, h=thickness);
				}
			}
		}
		translate([phone_width / 2, 0, screw_height]) {
			rotate([-90, 0, 0]) {
				cylinder(r=screw_radius, h=thickness + 0.1); //Extra 0.1 for rounding errors in OpenSCAD.
			}
		}
	}
}
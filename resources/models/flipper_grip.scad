//Physical dimensions.
printing_play = 0.2;
printing_overhang = 50; //Maximum overhang angle. 90 is perfect bridging. 0 is no overhang possible.
flipper_solenoid_pinhole_position = 2.5;
flipper_solenoid_pin_retracted = 8.5; //Length when retracted.
flipper_solenoid_pin_expansion = 10; //Stroke length.
flipper_solenoid_pin_radius = 2;
flipper_solenoid_height = 15;
flipper_solenoid_pingap_thickness = 1.6;
hexkey_radius = 2; //Radius of circumscribed circle around hex key.
m3_bolt_radius = 1.5;
m3_nut_radius = 5.5 / 2;
m3_nut_height = 2.4;
spring_end_thickness = 2; //How thick the attachment part of the spring is.

//Preference settings.
grip_length = 60;
radius = flipper_solenoid_pin_retracted - flipper_solenoid_pinhole_position;
spring_arm = 60; //How far the spring must be from the centre of rotation.
spring_min_thickness = 5; //How thick to make the handles above and below the spring.
flipper_rotation_angle = 45; //Degrees rotation when activated.
$fs = 0.4;
$fa = 1;

//Calculations.
solenoid_arm = flipper_solenoid_pin_expansion / 2 / sin(flipper_rotation_angle / 2);
around_pin = flipper_solenoid_height / 2 - flipper_solenoid_pin_radius;

module attachment(arm, min_thickness, spacing) {
	difference() {
		arm_height = min_thickness * 2 + spacing + tan(90 - printing_overhang) * radius * 2;
		union() { //Body of arm.
			translate([arm, 0, 0]) {
				cylinder(r=radius, h=arm_height);
			}
			translate([0, -radius, 0]) {
				cube([arm, radius * 2, arm_height]);
			}
		}
		translate([arm - radius, -radius, min_thickness]) { //Gap to fit the attachment.
			cube([radius * 2, radius * 2, spacing]);
			diagonal = radius * 2 / cos(printing_overhang);
			intersection() { //Making this end printable.
				translate([0, 0, spacing]) {
					rotate([0, printing_overhang, 0]) {
						cube([radius * 2 / cos(printing_overhang), radius * 2, arm_height]);
					}
				}
				cube([radius * 2, radius * 2, arm_height]);
			}
		}
		cylinder($fn=6, r=hexkey_radius + printing_play, h=arm_height); //Overlap with main hex key.
		translate([arm, 0, 0]) {
			cylinder(r=m3_bolt_radius + printing_play, h=arm_height); //Putting a bolt here to attach it.
			cylinder($fn=6, r=m3_nut_radius + printing_play, h=m3_nut_height); //Leave space for nut.
		}
	}
}

module flipper_grip() {
	solenoid_min_thickness = flipper_solenoid_height / 2 - flipper_solenoid_pingap_thickness / 2;
	difference() {
		union() {
			cylinder(r=radius, h=grip_length); //Main body.
			attachment(solenoid_arm, solenoid_min_thickness, flipper_solenoid_pingap_thickness);
			rotate([0, 0, 180]) {
				attachment(spring_arm, spring_min_thickness, spring_end_thickness);
			}
		}
		cylinder($fn=6, r=hexkey_radius + printing_play, h=grip_length); //Slot for hex key.
		translate([solenoid_arm, 0, solenoid_min_thickness]) {
			rotate([0, 0, flipper_rotation_angle / 2]) {
				translate([-radius - printing_play, -radius - printing_play, 0]) {
					cube([(radius + printing_play) * 2, 99999999, flipper_solenoid_pingap_thickness]);
				}
			}
		}
	}
}

flipper_grip();
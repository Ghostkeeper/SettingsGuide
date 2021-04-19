//Physical dimensions.
printer_height = 300; //Maximum height that we can print. Assuming it is square.
printing_play = 0.2; //Horizontal error in 3D printing.
movement_play = 0.2; //Play to leave if stuff has to move past each other.
ball_radius = 15; //Standard pinball size (7/6 inch).
ball_slit = ball_radius * 2 + movement_play * 2 + 4; //Allow 4mm extra space to make the ball fall through faster.
lane_wall_thickness = 0.35 * 6; //6 wall line widths with a 0.4mm 3D printer nozzle.
roll_slope = atan2(0.1, 1.5); //About 4 degrees. Minimum slope necessary to make the ball roll with 0.1mm layer height.
plunger_gate_alignment_length = 10; //At the front of the gate, how long the alignment ramps are that align the ball in the centre.
plunger_handle_overlap = 10; //How far the rod protrudes in the handle.
plunger_rod_length = 100; //TODO: Buy a rod?
push_solenoid_radius = 12.7 / 2;
push_solenoid_length = 6.35 + 26.2 + 1.9;
push_solenoid_rod_length = 19.05 - 6.35;
m3_bolt_radius = 1.5;
m3_bolt_head_radius = 2.5;
cabinet_thickness = 18; //1.8cm wooden planks.
playfield_thickness = 18;
playfield_slope = 6; //Degrees.
lane_chamfer_radius = 10;

//Settings.
extra_top_spacing = 10; //Because of inaccuracy of the ball movement, leave some extra space at the top to prevent the ball from hitting the playfield edge.
attachment_width = 30;
$fs = 0.4;
$fa = 1;

//Calculations.
gutter_width = lane_wall_thickness * 2 + ball_slit;
gutter_height = ball_radius * 2 + lane_wall_thickness + printing_play + movement_play + sin(roll_slope) * printer_height;
top_height = ball_radius * 2 + printing_play + movement_play + extra_top_spacing;
distance_to_launcher = -ball_slit + plunger_rod_length - cabinet_thickness - plunger_handle_overlap + plunger_gate_alignment_length;

module gutter_lift() {
	difference() {
		union() {
			cube([gutter_width, gutter_width, gutter_height + playfield_thickness + printing_play * 2 + top_height]); //Main body.

			//Attachment to the underside of the playfield.
			translate([0, gutter_width - attachment_width, gutter_height - attachment_width]) {
				multmatrix(m=[[1, 0, 0, 0],
				              [0, 1, 1, 0],
				              [0, 0, 1, 0],
				              [0, 0, 0, 1]]) {
					cube([gutter_width, attachment_width, attachment_width]);
				}
			}

			//Guide towards the launching bay.
			translate([0, gutter_width, gutter_height + playfield_thickness + printing_play * 2]) {
				cube([gutter_width, distance_to_launcher, top_height]);
			}
			intersection() {
				translate([gutter_width, gutter_width + distance_to_launcher, gutter_height + playfield_thickness + printing_play * 2]) {
					cylinder(r=gutter_width, h=top_height);
				}
				translate([0, gutter_width + distance_to_launcher, gutter_height + playfield_thickness + printing_play * 2]) {
					cube([gutter_width, gutter_width, top_height]);
				}
			}

			//Bottom part to hold the solenoid.
			total_solenoid_length = push_solenoid_rod_length + push_solenoid_length;
			translate([gutter_width / 2, gutter_width / 2, -total_solenoid_length - lane_wall_thickness]) {
				cylinder(r=ball_radius + printing_play + movement_play + lane_wall_thickness, h=total_solenoid_length + lane_wall_thickness);
			}
		}

		//Remove part that intersects with cabinet front wall.
		translate([-0.1, 0, gutter_height - 1 / sin(playfield_slope) * lane_wall_thickness]) {
			rotate([90 - playfield_slope, 0, 0]) {
				cube([gutter_width + 0.2, top_height + playfield_thickness + printing_play * 2 + gutter_height, gutter_width]);
			}
		}

		//render(convexity=4) {
			//Hollow out bottom.
			translate([0, lane_wall_thickness + lane_chamfer_radius, lane_wall_thickness + lane_chamfer_radius]) {
				minkowski() {
					cube([gutter_width - lane_wall_thickness - lane_chamfer_radius, gutter_width - lane_wall_thickness * 2 - lane_chamfer_radius * 2, gutter_height - lane_chamfer_radius - lane_wall_thickness]);
					sphere(r=lane_chamfer_radius);
				}
			}
			//Hole for kicker.
			translate([gutter_width / 2, gutter_width / 2, -push_solenoid_rod_length]) {
				cylinder(r=ball_radius + printing_play + movement_play, h=lane_wall_thickness + lane_chamfer_radius + push_solenoid_rod_length);
			}
			//Hole for solenoid.
			translate([gutter_width / 2, gutter_width / 2, -push_solenoid_rod_length - push_solenoid_length]) {
				cylinder(r=push_solenoid_radius + printing_play, h=push_solenoid_length + 0.1);
				translate([push_solenoid_radius - 2, 0, -lane_wall_thickness - 0.1]) {
					cylinder(r=2, h=lane_wall_thickness + 0.2);
				}
			}

			//Hollow out middle.
			translate([lane_wall_thickness + lane_chamfer_radius, lane_wall_thickness + lane_chamfer_radius, gutter_height]) {
				minkowski() {
					cube([gutter_width - lane_chamfer_radius * 2 - lane_wall_thickness * 2, gutter_width - lane_chamfer_radius * 2 - lane_wall_thickness * 2, playfield_thickness + printing_play * 2 + 0.1]);
					scale([1, 1, 0]) {
						cylinder(r=lane_chamfer_radius, h=1);
					}
				}
			}

			//Hollow out top.
			translate([lane_wall_thickness + lane_chamfer_radius, lane_wall_thickness + lane_chamfer_radius, gutter_height + playfield_thickness + printing_play * 2]) {
				minkowski() {
					cube([gutter_width - lane_chamfer_radius * 2 - lane_wall_thickness * 2, gutter_width - lane_chamfer_radius - lane_wall_thickness, top_height - (gutter_width - lane_wall_thickness)]);
					scale([1, 1, 0]) {
						cylinder(r=lane_chamfer_radius, h=1);
					}
				}
			}
			intersection() {
				translate([lane_wall_thickness + lane_chamfer_radius, gutter_width, gutter_height + playfield_thickness + printing_play * 2 + top_height - gutter_width]) {
					rotate([0, 90, 0]) {
						minkowski() {
							cylinder(r=gutter_width - lane_wall_thickness - lane_chamfer_radius, h=gutter_width - lane_wall_thickness * 2 - lane_chamfer_radius * 2);
							sphere(r=lane_chamfer_radius);
						}
					}
				}
				translate([lane_wall_thickness, lane_wall_thickness, gutter_height + playfield_thickness + printing_play * 2 + top_height - gutter_width]) {
					cube([gutter_width - lane_wall_thickness * 2, gutter_width - lane_wall_thickness + 0.1, top_height]);
				}
			}

			//Hollow out lane towards launcher.
			translate([lane_wall_thickness, gutter_width, gutter_height + playfield_thickness + printing_play]) {
				translate([0, 0, -0.1]) {
					cube([gutter_width - lane_wall_thickness * 2, distance_to_launcher + 0.1, top_height - lane_wall_thickness - lane_chamfer_radius + 0.1]);
				}
				translate([lane_chamfer_radius, 0, 0]) {
					cube([gutter_width - lane_wall_thickness * 2 - lane_chamfer_radius * 2, distance_to_launcher + 0.1, top_height - lane_wall_thickness + printing_play]);
				}
				translate([lane_chamfer_radius + printing_play, 0, top_height - lane_wall_thickness - lane_chamfer_radius]) {
					rotate([-90, 90, 0]) {
						cylinder(r=lane_chamfer_radius + printing_play, h=distance_to_launcher + 0.1);
					}
				}
				translate([gutter_width - lane_wall_thickness * 2 - lane_chamfer_radius - printing_play, 0, top_height - lane_wall_thickness - lane_chamfer_radius]) {
					rotate([-90, 0, 0]) {
						cylinder(r=lane_chamfer_radius + printing_play, h=distance_to_launcher + 0.1);
					}
				}
			}
			intersection() {
				translate([gutter_width, gutter_width + distance_to_launcher, gutter_height + playfield_thickness + printing_play * 2 - 0.1]) {
					minkowski() {
						cylinder(r=gutter_width - lane_wall_thickness - lane_chamfer_radius, h=top_height - lane_wall_thickness - lane_chamfer_radius + 0.1);
						sphere(r=lane_chamfer_radius);
					}
				}
				translate([0, gutter_width + distance_to_launcher, gutter_height + playfield_thickness + printing_play * 2 - 0.1]) {
					cube([gutter_width + 0.1, gutter_width, top_height + 0.2]);
				}
			}

			//Pin holes to attach to gutter.
			translate([-0.1, lane_wall_thickness, lane_wall_thickness * 2]) {
				rotate([0, 90, 0]) {
					cylinder(r=m3_bolt_radius, h=10.1);
				}
			}
			translate([-0.1, gutter_width - lane_wall_thickness, lane_wall_thickness * 2]) {
				rotate([0, 90, 0]) {
					cylinder(r=m3_bolt_radius, h=10.1);
				}
			}
			//Last alignment screw on the attachment piece.
			translate([-0.1, gutter_width + attachment_width / 3, gutter_height - attachment_width / 3]) {
				rotate([0, 90, 0]) {
					cylinder(r=m3_bolt_radius, h=10.1);
				}
			}
			//Screw hole to attach to underside of playfield.
			translate([gutter_width / 2, gutter_width + attachment_width * 2 / 3, gutter_height - attachment_width / 3]) {
				cylinder(r=m3_bolt_radius, h=attachment_width / 3 + 0.1);
			}
			translate([gutter_width / 2, gutter_width + attachment_width * 2 / 3, 0]) { //Small 4mm hole for wires.
				cylinder(r=m3_bolt_head_radius + printing_play, h=gutter_height - 8);
			}
		//}
	}

	difference() {
		//Plate above gutter (because we hollowed out too much in the bottom).
		translate([0, lane_wall_thickness, gutter_height]) {
			cube([lane_wall_thickness, gutter_width - lane_wall_thickness * 2, lane_chamfer_radius]);
		}
		//Remove part that intersects with cabinet front wall.
		translate([-0.1, 0, gutter_height - 1 / sin(playfield_slope) * lane_wall_thickness]) {
			rotate([90 - playfield_slope, 0, 0]) {
				cube([gutter_width + 0.2, top_height + playfield_thickness + printing_play * 2 + gutter_height, gutter_width]);
			}
		}
	}
}

gutter_lift();
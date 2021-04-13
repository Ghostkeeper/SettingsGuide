//New rolling blind spacer.

//Measurements.
vertical_offset = 32.8;
horizontal_offset = 4.0;
bead_radius = 2.25;
screw_radius = 2; //Not the screw head but the bolt.

//Settings.
bead_spacing = 1;
screw_edge_spacing = 1;
bead_wall_thickness = 1;
screw_wall_thickness = 2;
reel_joint_thickness = 1;
fa = 1;
fs = 0.1;

//Computed values.
thickness_screws = horizontal_offset + screw_radius * 2 + screw_edge_spacing * 2;
thickness_beads = bead_radius * 2 + bead_spacing * 2;
thickness = max(thickness_screws, thickness_beads);
height = vertical_offset + screw_radius * 2 + screw_edge_spacing * 2;
turn_radius = (height - screw_radius * 4 - screw_edge_spacing * 4) / 2;
width = (turn_radius + bead_radius + bead_spacing) * 2 + screw_wall_thickness;

module bottom_part() {
    difference() { //Wall mount.
        cube([screw_wall_thickness, height / 2 + screw_wall_thickness / 2, thickness]); //Main body.
        translate([0, height / 2 - screw_wall_thickness / 2, thickness / 3]) { //Binding.
            cube([screw_wall_thickness, screw_wall_thickness, thickness / 3]);
        }
        translate([0, height / 2 - vertical_offset / 2, thickness / 2 - horizontal_offset / 2]) { //Screw hole.
            rotate([0, 90, 0]) {
                cylinder(r = screw_radius, h = screw_wall_thickness + 0.1, $fa = fa, $fs = fs);
            }
        }
    }
    translate([screw_wall_thickness, height / 2, 0]) { //Bead wheel. Base is center-down on top of the mount.
        translate([turn_radius + bead_radius + bead_spacing, 0, thickness / 2 - thickness_beads / 2]) {
            difference() {
                cylinder(r = turn_radius, h = thickness_beads, $fa = fa, $fs = fs);
                translate([0, 0, thickness_beads / 2]) {
                    rotate_extrude(convexity = 10, $fa = fa, $fs = fs) {
                        translate([turn_radius, 0, 0]) {
                            circle(r = bead_radius + bead_spacing, $fa = fa, $fs = fs);
                        }
                    }
                }
                translate([0, 0, thickness_beads - reel_joint_thickness]) { //Reel joint.
                    cylinder(r = turn_radius - bead_radius - bead_spacing, h = reel_joint_thickness, $fa = fa, $fs = fs);
                }
            }
        }
        translate([0, -turn_radius, 0]) { //Wheel holder bottom.
            cube([turn_radius + bead_radius + bead_spacing, turn_radius * 2, thickness / 2 - thickness_beads / 2]);
        }
        translate([turn_radius + bead_radius + bead_spacing, 0, 0]) { //Wheel holder top.
            cylinder(r = turn_radius, h = thickness / 2 - thickness_beads / 2, $fa = fa, $fs = fs);
        }
    }
}

module top_part() {
    difference() { //Wall mount.
        translate([0, height / 2 + screw_wall_thickness / 2, 0]) {
            cube([screw_wall_thickness, height / 2 - screw_wall_thickness / 2, thickness]); //Main body.
        }
        translate([0, height / 2 + vertical_offset / 2, thickness / 2 + horizontal_offset / 2]) { //Screw hole.
            rotate([0, 90, 0]) {
                cylinder(r = screw_radius, h = screw_wall_thickness + 0.1, $fa = fa, $fs = fs);
            }
        }
    }
    translate([0, height / 2 - screw_wall_thickness / 2, thickness / 3]) { //Binding.
        cube([screw_wall_thickness, screw_wall_thickness, thickness / 3]);
    }
    translate([screw_wall_thickness, height / 2 - turn_radius, thickness - thickness / 2 + thickness_beads / 2]) { //Wheel holder bottom.
        cube([turn_radius + bead_radius + bead_spacing, turn_radius * 2, thickness / 2 - thickness_beads / 2]);
    }
    translate([screw_wall_thickness + turn_radius + bead_radius + bead_spacing, height / 2, thickness - thickness / 2 + thickness_beads / 2]) { //Wheel holder top.
        cylinder(r = turn_radius, h = thickness / 2 - thickness_beads / 2, $fa = fa, $fs = fs);
    }
    translate([screw_wall_thickness + turn_radius + bead_radius + bead_spacing, height / 2, thickness - thickness / 2 + thickness_beads / 2 - reel_joint_thickness]) { //Reel joint.
        cylinder(r = turn_radius - bead_radius - bead_spacing, h = reel_joint_thickness, $fa = fa, $fs = fs);
    }
}

color("red") {
    bottom_part();
}
color("blue") {
    top_part();
}
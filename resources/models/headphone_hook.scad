angle_span = 40; //The total curve length (determines the width of the hook).
radius = 70; //The radius of the curve.
breadth = 50; //How far the hook should protrude from the wall (how wide the headphone band is).
tilt_shear = 10; //How much higher the tip is than the wall.
lip_height = 2; //How high the lip at the end of the hook should rise.
plate_lip_height = 12; //How high the lip at the wall side should be.
thickness = 5; //Overall thickness of the model, for strength.
plate_dip_height = 60; //How long the plate at the underside must be.
screw_diameter = 3.2; //Diameter of the screw holes.
screw_countersink = 2; //Extra radius of countersunk screw head.
roundness = 1; //Overall radius of rounded corners and chamfers.
diagonal_lower = thickness; //The diagonal won't extend all the way from corner to corner.
$fa = 1;
$fs = 0.1;

module screw_hole() { //Already moved to correct radius, just rotate around Z.
	translate([radius + thickness + plate_lip_height / 2, 0, 0]) {
		cylinder(r=screw_diameter / 2, h=thickness + 1);
		translate([0, 0, thickness - screw_countersink]) {
			cylinder(r1=screw_diameter / 2, r2=screw_diameter / 2 + screw_countersink + 1, h=screw_countersink + 1); //+1 to prevent clipping and non-manifold stuff.
		}
	}
}

shear = tilt_shear / breadth;
shear_matrix = [
	[1, 0, shear, 0],
	[0, 1, 0, 0],
	[0, 0, 1, 0],
	[0, 0, 0, 1]
];
shear_matrix_2d = [
	[1, shear, 0],
	[0, 1, 0],
	[0, 0, 1]
];

difference() {
	//Everything except the diagonal is a simple rotate extrude.
	rotate([0, 0, -angle_span / 2]) {
		rotate_extrude(angle = angle_span) {
			multmatrix(shear_matrix_2d) {
				//The resting surface.
				translate([radius, 0]) {
					difference() {
						minkowski() {
							translate([roundness, 0]) {
								square([thickness - roundness * 2, breadth - roundness + thickness * 2]);
							}
							circle(r=roundness);
						}
						translate([0, -roundness]) {
							square([thickness, roundness]);
						}
					}
				}
				//Surface chamfering.
				translate([radius - roundness, thickness]) {
					difference() {
						square([thickness + roundness * 2, roundness]);
						translate([0, roundness]) {
							circle(r=roundness);
						}
						translate([thickness + roundness * 2, roundness]) {
							circle(r=roundness);
						}
					}
				}
				//The lip.
				translate([radius + thickness / 2 + roundness, breadth + thickness + roundness]) {
					minkowski() {
						square([thickness / 2 + lip_height - roundness * 2, thickness - roundness * 2]);
						circle(r=roundness);
					}
				}
				//Lip upper chamfering.
				if(lip_height >= roundness * 2) {
					translate([radius + thickness, thickness + breadth - roundness]) {
						difference() {
							square([roundness, roundness]);
							translate([roundness, 0]) {
								circle(r=roundness);
							}
						}
					}
				}
			}
			//The back plate.
			difference() {
				translate([radius - plate_dip_height + roundness, 0]) {
					minkowski() {
						square([plate_dip_height + thickness + plate_lip_height - roundness * 2, thickness - roundness]);
						circle(r=roundness);
					}
				}
				translate([radius - plate_dip_height, -roundness]) {
					square([plate_dip_height + thickness + plate_lip_height, roundness]);
				}
			}
		}
	}
	rotate([0, 0, -angle_span / 4]) {
		screw_hole();
	}
	rotate([0, 0, angle_span / 4]) {
		screw_hole();
	}
}

//Diagonal.
multmatrix(shear_matrix) {
	translate([radius - plate_dip_height + roundness, -thickness / 2, thickness]) {
		difference() {
			cube([plate_dip_height - roundness, thickness, breadth + thickness - roundness]);
			translate([0, -1, -diagonal_lower]) { //-1 to prevent z-fighting in preview.
				rotate([0, -atan((breadth + thickness - roundness) / (plate_dip_height - roundness)), 0]) {
					cube([sqrt(pow((plate_dip_height - roundness), 2) + pow((breadth + thickness - roundness), 2)) + diagonal_lower, thickness + 2, breadth + thickness + diagonal_lower]);
				}
			}
		}
	}
}
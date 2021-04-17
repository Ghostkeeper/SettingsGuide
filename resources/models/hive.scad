tileRadius = 25;
tileHeight = 8;
$fs = 0.5;
$fa = 5;

module tile() {
    cylinder(r = tileRadius,h = tileHeight,$fn = 6); //Hexagonal tiles.
}

module bee() {
    //Main body.
    translate([-tileRadius * 0.1, 0, 0]) {
        scale([2, 1, 0.5]) { //Body.
            sphere(r = tileRadius * 0.15);
        }
        translate([tileRadius * 0.06, 0, 0]) { //Subtle ribbing.
            rotate([0, -10, 0]) {
                scale([1.5, 1, 0.5]) {
                    sphere(r = tileRadius * 0.15);
                }
            }
        }
        translate([tileRadius * -0.06, 0, 0]) { //Subtle ribbing.
            rotate([0, -5, 0]) {
                scale([1.5, 1, 0.5]) {
                    sphere(r = tileRadius * 0.15);
                }
            }
        }
    }

    //Head.
    translate([tileRadius * 0.2, 0, 0]) {
        scale([0.8, 1, 0.5]) { //Main head shape.
            sphere(r = tileRadius * 0.1);
        }
        rotate([0, 0, 20]) { //Left antenna.
            translate([tileRadius * 0.075, 0, 0]) {
                beeAntenna(5);
            }
        }
        mirror([0, 1, 0]) { //Right antenna.
            rotate([0, 0, 20]) {
                translate([tileRadius * 0.075, 0, 0]) {
                    beeAntenna(5);
                }
            }
        }
    }
}

module beeAntenna(piecesLeft) {
    //This uses a recursive definition to count piecesLeft down to 0.
    if(piecesLeft >= 1) {
        rotate([0, 90, 0]) {
            cylinder(r = tileRadius * 0.01, h = tileRadius * 0.04);
        }
        translate([tileRadius * 0.038, 0, 0]) {
            rotate([0, 0, 5]) {
                beeAntenna(piecesLeft - 1);
            }
        }
    }
    else { //At the end of the antenna.
        sphere(r = tileRadius * 0.01);
    }
}

module beeTile() {
    difference() {
        tile();
        translate([0, 0, tileHeight]) {
            bee();
        }
    }
}

beeTile();
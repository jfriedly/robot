// Note:  Our robot functions on a 360 compass with East being 0 degrees, not on a 180 degree compass like the course provides. See function update_heading().
//Note:  We use very strong magnets to pull the wagon, so a "hooking up" function is not needed.


function gps_update():
//This function is run in the background to update the robot's heading
//The robot's heading is saved as an integer from 0 to 359 degrees,
//with 90 degrees pointing toward the barn, as in the normal course coordinates.
    if get_gps_data fetches new data:
       determine robot heading from GPS data, as an angle from 0 to 179 degrees
       If the robot is facing south, add 180 degrees
       If the heading rolled over from 0 to 179, 179 to 0, 180 to 359, or 359 to 180:
       	  Toggle whether the robot is facing north or south
	  Adjust the heading angle accordingly


function wait_for_start():
    while CdS cell is not bright:
        wait
    return


function turn(angle):
    while(heading is not close enough to angle):
        if(heading > angle):
            try to turn CCW to angle with shaft encoder
        else:
            try to turn CW to angle with shaft encoder
    return


function align_with_metal_strip(angle):
//Align to the given angle, with the assistance of a metal strip
//As a precondition, the robot must start above the strip

    //First, make sure we're facing approximately towards angle
    while(heading is not within 10 degrees of angle):
        determine if the robot should turn CW or CCW
        if CW:
            while heading is not within 10 degrees:
                pivot right until the right optosensor loses the metal
                back straight up until the left optosensor loses the metal
        else:
            while heading is not within 10 degrees:
                pivot left until the left optosensor loses the metal
                back straight up until the right optosensor loses the metal

    //Now we're facing (approximately) toward angle.  Just follow the metal.
    //If one optosensor loses the metal, then the robot should turn so it's back on.
    //If both lose the metal, then the robot is at the end of the metal strip
    while(either optosensor sees metal):
        if (only the left optosensor sees metal) or
                (angle from heading to target angle > 0):
            drive with more power to the right motor to compensate
        elif (only the right optosensor sees metal) or
                (angle from heading to target angle < 0):
            drive with more power to the left motor to compensate
        else:
            drive with equal power to both motors

    return


function detect_light_color():
    //In lab 1, it was found that a CdS sensor with a red filter can distinguish between
    //red, blue, and no light.  The values read from the sensor look like:
    //  Red  - 3
    //  Blue - 25
    //  None - 70
    Using the red filter, distinguish between red, blue, and no light.
    return red, blue, or none


function forward_by_inches(inches):
//Drive forward a given number of inches

    if inches < 0, drive backwards instead
    determine number of transitions needed by each shaft encoder (about 5.1 transitions per inch)
    while(more transitions are needed):
        if the right side needs more transitions than the left:
            drive with more power to the right motor
        elif the left side needs more transitions then the right:
            drive with more power to the left motor
        else:
            drive with equal power to both motors
    return


function pick_up_corn():
//Precondition: robot is aligned at end of metal strip, facing directly toward 90 degrees
    activate servo to raise corn arm, picking up corn
    return


function lower_corn():
    lower servo to drop corn
    return


function drop_hay_bale():
//Precondition: robot is lined up with hay bale elevator
    activate motor to push hay bale off robot
    wait until hay bale has fallen
    return

function hookup_with_wagon():
    //Drive forward to connect to wagon
    forward_by_inches(2)


void get_corn()
{
	turn_to_angle(135);  
	forward_by_inches(29);
	align_with_metal_strip(90);
	detect_light_color();
	if(!blue)
	{
		forward_by_inches(-8);
		turn_to_angle(0);
		align_with_metal_strip(90);
		detect_light_color();
		if(!blue)
		{
			forward_by_inches(-8);
			turn_to_angle(0);
			align_with_metal_strip(90);
		}
	}
	pick_up_corn();
	turn_to_angle(315);
	forward_by_inches(29);
}


void drop_hay();
{
	turn_to_angle(90);
	forward_by_inches(36);
	turn_to_angle(120);
	forward_by_inches(18);
	align_with_metal_strip(135);
	drop_hay_bale();
	forward_by_inches(1);
}


void drop_corn()
{
	if(corn_bin_left)
	{
		turn_to_angle(340);	
		forward_by_inches(22);
		align_with_metal_strip(0);
		lower_corn();
		turn_to_angle(150);
	}
	else
	{
		turn_to_angle(225);	
		forward_by_inches(9);
		align_with_metal_strip(180);
		lower_corn();
		turn_to_angle(45);
	}
}


void get_wagon()
{
	forward_by_inches(20);
	align_with_metal_strip(90);  //Note:  We use very strong magnets to pull the wagon, so a "hooking up" function is not needed.
	forward_by_inches(-10);
	turn_to_angle(235);
	forward_by_inches(-9);
	turn_to_angle(90);
	forward_by_inches(-36);
}

int main()
{
	calibrate_gps();
    wait_for_start_light();

	get_corn();
	drop_hay();
	drop_corn();
	get_wagon();
}



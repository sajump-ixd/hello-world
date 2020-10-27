let t = 0; // define new variable: time
let p = 0; // switch for starting and stopping loop

function setup() { // sets up the enviroment. can only be used once
  createCanvas(1440, 900); // width, height of canvas in pixels
  // full screen size on my 13" macbook pro
  noStroke(); // no outline of wiggle worms
  fill('white'); // beginning color of the wiggle worms or anything drawn
  hue = -30; // changing this later to make rainbow on click, -30 so it starts on red
  cursor(CROSS); // makes the cursor a cross
  button = createButton('⏯️'); // pause button stops the loop + starts again
  button.position(10, 10); // button location
  button.mousePressed(pause); // calls the pause function when clicked
}

function draw() { // continous excutes code
  background(0, 10); // background and opacity to create fading effect
 
  // for makes a loop to make a x and y grid of ellipses
  // first part is the initial state; second is what's being check each time
  // if false, loop ends; third excutes after each loop
  for (let x = 0; x <= width; x = x + 55) { // 55 creates the width between each wiggle worm
    for (let y = 0; y <= height; y = y + 18) { // 18 creates height between each wiggle worm
      // starting point of each circle depends on mouse position
      //const declares a variable that cannot be redeclared
      //map re-maps a variable
      //mouseY is the vertical position of the mouse
      // 0 and height are current values, the next two are target values
      const yAngle = map(mouseY, 0, height, 13, 160, true);
      const xAngle = map(mouseX, 0, width, 29, 200);
      // variable that makes each circle vary based on it's position 
      // creates a wave effect
      const angle = yAngle * (y / height) + xAngle * (x / width);
      // each wiggle worm moves in a circle
      const myX = x + 20 * cos(2 * PI * t + angle);
      const myY = y + 20 * sin(2 * PI * t + angle);
      // make tiny circle while any key is pressed
      if (keyIsPressed === true){
        size = 3;
      } else {
        size = 18;
      }
      // draws the ellipse: location x, location y, width, height
      ellipse(myX, myY, size); // draw wiggle worm 
    }
  }

  t = t + 0.0089; // controls speed
  
}
// change color in rainbow order each time mouse is clicked!
function mouseClicked() {
  if (hue > 300) { // so it doesn't get stuck at red after 12 clicks
    hue = 0; 
  } else {
    hue += 30; 
} 
//hue > 360 ? hue = 0 : hue += 30;
// ?? ternary operator: using this instead breaks my code??? 
colorMode (HSL, 360); // changes color mode to hue, sat, brightness. 360 is max
fill(hue, 220, 200);
}

function pause(){
 if (p == 0 ){
  noLoop();
  p = 255;
} else if (p == 255){
    loop();
    p = 0;
}
}

function keyTyped(){
    if (key == 'p' && p == 0 ){
      noLoop();
      p = 255;
    } else if (key == 'p' && p == 255){
        loop();
        p = 0;
    }
}

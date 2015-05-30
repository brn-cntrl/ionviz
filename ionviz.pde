//Ionviz
//Brian Cantrell
//Project completed as part of Data Visualization course at 
//USC School of Cinematic Arts with Evan Hughes

float w;
float lat;
String [] latStrings;
String [] valStrings;
int [] theVals;
PImage map;
PImage heatmap;
color c;
int count;
int curVals;

// -- Setup --//

void setup() {
 
  latStrings = loadStrings("data/ionLats.txt");
  valStrings = loadStrings("data/ionValsFull2.txt");
  map = loadImage("images/map.png");
  heatmap = loadImage("images/heatmapColors.png");
  size(1080, 544, P3D);
  smooth();
  curVals = 0;
}

// -- Main Loop -- //

void draw() {

  noStroke();
  //only animate until end of file
  //Loop through the lattitude values
  if (count == 5) { 
    count = 0;
  }
  if (count == 0) {
    background(255);
    if (curVals >= valStrings.length) {
      curVals = 0;
    }
    for (int i = 0; i < latStrings.length; i++) {

      lat = map(float(latStrings[i]), 90., -90., 0., float(height));
      theVals = parseVals(valStrings[i+curVals]);
      //For every lattitude value grab its array of sensor readings
      for (int j = 0; j < theVals.length; j++) {
        //map the color of each "pixel" to the value of the sensor reading
        c = heatmap.get(int(map(theVals[j], 0, 1000, 0, 428)), 0);
        fill(c);
        w = width/theVals.length;
        //fill a row of "pixels"
        rect(j*w, lat-5, theVals.length, 10);
      }
    }
    curVals+=71;
    image(map, 0, 0);
    tint(255, 50);
    //uncomment to save images for animation
    //saveFrame("map-####.jpg");
  }
  count++;
}

// -- Function for returning integer array for TEC values --//

int [] parseVals(String s) {
  //Grab string from file
  String theString = s;
  // strip string of brackets, quotations, and spaces
  String stripped = theString.replace("[", "").replace("]", "").replace("\"", "").replace("“", "").replace(" ", "");
  // split string on commas and cast as int
  int [] parsed = int(stripped.split(","));
  return parsed;
}


This is where I store all my TI-Basic (and a few Python) programs I use on my TI-84 Plus CE.

If you want to use them, go ahead!
  1. Download and install the TI-Connect software ([https://education.ti.com/en/software/details/en/B59F6C83468C4574ABFEE93D2BC3F807/swticonnectsoftware](https://education.ti.com/en/software/details/en/B59F6C83468C4574ABFEE93D2BC3F807/swticonnectsoftware))
  2. Download the programs you want to use.
  3. Run the TI-Connect app, and hook up your calculator to your pc using a USB-A-to-USB-mini-b cable.
  4. Select the "Add content from computer to selected calculator(s)" button in TI-Connect and select the programs you want to upload.

Description of Programs:\
  TI-BASIC\
    ARC\
      Inputs: DEGREES, RADIUS\
      Outputs: ARC LENGTH\
      Calculates ARC LENGTH based on DEGREES and RADIUS\
      Displays arc\
    BIRD\
      Inputs: None\
      Outputs: Score\
      Flappy bird\
    CIRCLE\
      Inputs: H, K, RADIUS\
      Outputs: DIAMETER, CIRCUMFERENCE, AREA\
      Calculates diameter, circumference, and area based on radius\
      Displays circle with radius RADIUS at (H, K)\
    CLOCK\
      Inputs: Choice between Clock and Set alarm\
      Outputs: Date, time\
      Displays an analog clock. Shuts off after alarm if Set alarm was selected\
      Set alarm displays analog clock until alarm time occurs\
      Pressing a key ends program\
    CMNFCTRS\
      Inputs: N1, N2\
      Outputs: Common factors\
      Finds common factors of N1 and N2 and displays logic\
    DIALATE\
      Inputs: X, Y, K\
      Outputs: (H, K) scaled by K\
      Dialates (H, K) by a factor of K\
    DISTANCE
      Inputs: X1, Y1, X2, Y2\
      Outputs: Distance, H, K\
      Finds distance between (X2, Y2) and (X2, Y2) and Δx and Δy\
    FACTORS\
      Inputs: N\
      Outputs: Factors\
      Finds factors of N\
    FCTRTREE\
      Inputs: A*C, B\
      Outputs: Factors\
      Finds factors of AC that add to B\
      Useful for factoring quadratics (Ax^2+Bx+C)\
    HYPO\
      Inputs: LEG1, LEG2\
      Outputs: HYPOTENUSE\
      Finds hypotenuse of a right triangle with legs LEG1 and LEG2\
    MIDPOINT\
      Inputs: X1, Y1, X2, Y2\
      Outputs: X, Y\
      Finds midpoint (X, Y) of line segment (X1, Y1), (X2, Y2)\
    PARTITION\
      Inputs: X1, Y1, X2, Y2, RATIO\
      Outputs: X, Y\
      Partitions line segment (X1, Y1), (X2, Y2) by ratio RATIO\
    PERSQUR\
      Inputs: N\
      Outputs: Bool\
      Outputs if N is a perfect square\
    POLYGON\
      Inputs: SIDES, SIDE LENGTH, APOTHEM\
      Outputs: AREA, PERIM, ANGLE\
      Calculates area, perimeter, and angle between sides of a regular polygon with sides SIDES, side length SIDE LENGTH, and apothem APOTHEM\
    PRIME\
      Inputs: N\
      Outputs: Bool\
      Outputs true if N is prime\
    QUAD\
      Inputs: A, B, C\
      Outputs: ROOTS, Y-INTERCEPT, AOS, VERTEX, DISCRIMINANT, FACTORED FORM, VERTEX FORM\
      Find roots, y-intercept, aos (axis of symmetry), vertex, discriminant, factored form, and vertex form from quadratic Ax^2+Bx+C\
      This does not use a CAS to find factored and vertex form, so it is technically allowed on the ACT and SAT. HOWEVER, it is longer than 25 lines, so still banned.\
    REFLECT\
      Inputs: X, Y, LINE SLOPE, Y-INTERCEPT\
      Outputs: Point\
      Reflects (X, Y) over line y=(LINE SLOPE)(x)+(Y-INTERCEPT) (y=mx+b)\
    RESET\
      Inputs: None\
      Outputs: None\
      Resets many calculators functions\
      THIS PROGRAM IS REQUIRED FOR MANY OTHERS TO FUNCTION!\
      Sets axes to black\
      Radian mode\
      Real mode\
      Viewport rect set to (-15, 10), (15, 10)\
      Clears graph screen\
      Turns background off\
    REVARC\
      Inputs: ARC LENGTH, RADIUS\
      Outputs: DEGREES\
      Finds DEGREES based on ARC LENGTH and RADIUS\
      Reverse of ARC\
    REVHYPO\
      Inputs: HYPO, LEG1\
      Outputs: LEG2\
      Finds LEG2 of triangle with hypotenuse HYPO and leg LEG1\
      Reverse of HYPO\
    ROTATE\
      Inputs: X1, Y1, X2, Y2, ANGLE\
      Outputs: X, Y\
      Rotates (X1, Y1) around (X2, Y2) by ANGLE, in degrees or radians based on mode\
    SECTOR\
      Inputs: RADIUS, ANGLE\
      Outputs: AREA\
      Finds area of sector of ANGLE of circle with radius RADIUS\
    SICONV\
      Inputs: FROM (VALUE, UNIT), TO (UNIT)\
      Outputs: Value\
      Converts between FROM(VALUE) FROM(UNIT) (SI units) to Value TO(UNIT) (SI UNITS)\
    SIMPLIFY\
      Inputs: NUMERATOR, DENOMINATOR\
      Outputs: Simplified fraction\
      Simplifies fraction NUMERATOR/DENOMINATOR\
    TEST2\
      Inputs: None\
      Outputs: None\
      Orbital simulation of Earth and Moon\
    TEST3\
      Inputs: None\
      Outputs: None\
      Pool\
      WIP\
    TICTACTO\
      Inputs: Move\
      Outputs: Board\
      Tic-tac-toe\
      Board is number keypad\
      789\
      456\
      123\
    TRANS\
      Input: X, Y, H, K\
      Output: Point\
      Translates (X, Y) by (H, K)\

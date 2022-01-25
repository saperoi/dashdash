import matplotlib.mathtext as mt

import fx as floppy

function GraphThat(f, name)
  m = mt.MathTextParser("Bitmap")
  m.to_png(name + '.png', f)
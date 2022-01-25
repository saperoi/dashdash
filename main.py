import matplotlib.mathtext as mt

import fx as floppy

function GraphThat(f, name)
  m = mt.MathTextParser("Bitmap")
  m.to_png(name + '.png', f)

fx.d = 0
for fx.d <= 1:
  GraphThat(fx.animone, fx.d)
  fx.d += 0.04
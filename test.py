import pyvista as pv

pv.OFF_SCREEN = True

pl = pv.Plotter()
pl.add_mesh(pv.Wavelet())
pl.show(screenshot="test.png")

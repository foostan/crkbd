# execfile '/tmp/pcbnew.py'
import pcbnew

OFFSET_X = float(70)
OFFSET_Y = float(70)
PITCH = float(19)

def set_position(ref, xp, yp, orientation = 0):
  module = pcb.FindModuleByReference(ref)
  module.SetPosition(pcbnew.wxPointMM(xp + OFFSET_X, yp + OFFSET_Y))
  module.SetOrientation( orientation * 10.0 )

def set_matrix_position(ref_prefix, matrix):
  i = 0
  for yi, rows in enumerate(matrix):
      for xi, p in enumerate(rows):
        i += 1
        ref = "%s%s" % (ref_prefix, i)
        xp = xi * PITCH + p[0]
        yp = yi * PITCH + p[1]
        orientation = p[2]
        set_position(ref, xp, yp, orientation)

  xp = xi * PITCH + p[0]
  yp = yi * PITCH + p[1]
  orientation = p[2]
  set_position(ref, xp, yp, orientation)


  module = pcb.FindModuleByReference(ref)
  module.SetPosition(pcbnew.wxPointMM(xp + OFFSET_X, yp + OFFSET_Y))
  module.SetOrientation( orientation * 10.0 )

#-------------

pcb = pcbnew.GetBoard()

# ProMicro
#set_position('U1', 115.25, 20.25, 0)

# OLED
#set_position('J2', 110.75, 38.5, 0)

# OLED JP
#set_position('JP2', 118.375, 35.25, -90)
#set_position('JP3', 115.875, 35.25, -90)
#set_position('JP4', 113.375, 35.25, -90)
#set_position('JP5', 110.875, 35.25, -90)
#set_position('JP6', 118.375, 35.25, -90)
#set_position('JP7', 115.875, 35.25, -90)
#set_position('JP8', 113.375, 35.25, -90)
#set_position('JP9', 110.875, 35.25, -90)

# Undergrow LED
#set_position('J3', 102, 29.5, 0)

# TRRS Jack
#set_position('J1', 124.75, 45, -90)

# Reset Switch
#set_position('RSW1', 120, 51, 0)

# R
#set_position('R1', 105.5, 46, 90)
#set_position('R2', 108, 46, 90)

# JP1
#set_position('JP1', 105.5, 41, 0)

# Switch
set_matrix_position('SW', [
    [[0, 0.375*PITCH, 180], [0, 0.375*PITCH, 180], [0, 0.125*PITCH, 180], [0, 0*PITCH, 180], [0, 0.125*PITCH, 180], [0, 0.25*PITCH, 180]],
    [[0, 0.375*PITCH, 180], [0, 0.375*PITCH, 180], [0, 0.125*PITCH, 180], [0, 0*PITCH, 180], [0, 0.125*PITCH, 180], [0, 0.25*PITCH, 180]],
    [[0, 0.375*PITCH, 180], [0, 0.375*PITCH, 180], [0, 0.125*PITCH, 180], [0, 0*PITCH, 180], [0, 0.125*PITCH, 180], [0, 0.25*PITCH, 180]],
                        [[3.5*PITCH, 0*PITCH+3, 180], [3.5*PITCH+2, 0.25*PITCH+1, 160], [3.5*PITCH+5.25, 0.25*PITCH+4.75, 240]]
])

# Diode
set_matrix_position('D', [
    [[-8, 0.375*PITCH, 270], [8, 0.375*PITCH, 270], [8, 0.125*PITCH, 270], [8, 0*PITCH, 270], [8, 0.125*PITCH, 270], [-8, 0.25*PITCH-2.375, 270]],
    [[-8, 0.375*PITCH, 270], [8, 0.375*PITCH, 270], [8, 0.125*PITCH, 270], [8, 0*PITCH, 270], [8, 0.125*PITCH, 270], [-8, 0.25*PITCH-2.375, 270]],
    [[-8, 0.375*PITCH, 270], [8, 0.375*PITCH, 270], [8, 0.125*PITCH, 270], [8, 0*PITCH, 270], [8, 0.125*PITCH, 270], [-8, 0.25*PITCH-2.375, 270]],
                   [[3.5*PITCH-8, 0*PITCH+3, 270], [3.5*PITCH-11, 0.25*PITCH-2, 270], [3.5*PITCH-27, 0.25*PITCH-2, 270]]
])

# LED
set_matrix_position('L', [
    [[0, 0.375*PITCH-5.5, 0], [0, 0.375*PITCH-5.5, 0], [0, 0.125*PITCH-5.5, 0], [0, 0*PITCH-5.5, 0], [0, 0.125*PITCH-5.5, 0], [0, 0.25*PITCH-5.5, 0]],
    [[0, 0.375*PITCH-5.5, 0], [0, 0.375*PITCH-5.5, 0], [0, 0.125*PITCH-5.5, 0], [0, 0*PITCH-5.5, 0], [0, 0.125*PITCH-5.5, 0], [0, 0.25*PITCH-5.5, 0]],
    [[0, 0.375*PITCH-5.5, 0], [0, 0.375*PITCH-5.5, 0], [0, 0.125*PITCH-5.5, 0], [0, 0*PITCH-5.5, 0], [0, 0.125*PITCH-5.5, 0], [0, 0.25*PITCH-5.5, 0]],
                        [[3.5*PITCH, 0*PITCH-5.5+3, 0], [3.5*PITCH+3.5, 0.25*PITCH-5.25+1, 165], [3.5*PITCH+0.5, 0.25*PITCH+8.5-6.5, 240]]
])

#hole_xn = 8
#hole_yn = 6
#hole_ox = float(60.5)
#hole_oy = float(60.5)
#pitch = float(19)
#
#for hole_i in range(0, hole_xn * hole_yn):
#  hole_xi = (hole_i / hole_yn)
#  hole_yi = (hole_i % hole_yn) - 1
#
#  hole_px = hole_ox + pitch * hole_xi
#  hole_py = hole_oy + pitch * hole_yi
#
#  hole_module = pcb.FindModuleByReference("H%s" % (hole_i+1))
#  hole_module.SetPosition(pcbnew.wxPointMM(0, 0))

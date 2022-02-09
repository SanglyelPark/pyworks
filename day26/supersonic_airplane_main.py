from day26.classlib.supersonic_airplane import SuperSonicAirPlane

sa = SuperSonicAirPlane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirPlane.SUPERSONIC
sa.fly()
sa.fly_mode = SuperSonicAirPlane.NORMAL
sa.fly()
sa.land()

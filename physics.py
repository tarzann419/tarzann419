gravity = 10
class Physics:
    def speed(self, distance, time):
        return (distance/time)

    def workdone(self, force, distance):
        return (force*distance)

    def potentialenergy(self, mass, height):
        return (mass*gravity *height)

    def kineticenergy(self, mass, velocity):
        return (0.5*mass*(velocity**2))

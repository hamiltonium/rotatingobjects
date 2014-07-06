'''
'''

import visual
import numpy


def main():
    visual.sphere()
    frame = BodyFrame()
    pass
    #make a loop that updates the frame every dt seconds
    #draw a cube with vertices at whatever points i, j, and k are.

class BodyFrame(object):
    """An instance is a set of coordinates that is connected to some rotating
    object.  It shares the same origin as the space coordinate frame.
    
    I:    An array containing the principle moments associated with each
          principle axis.
    i:    An array representing the i principle axis in the space frame
          coordinate system.
    j:    An array representing the j principle axis in the space frame
          coordinate system.
    k:    An array representing the k principle axis in the space frame
          coordinate system.
    omega: the angular velocity that the frame is rotating at. In the body frame
    omega_dot: the first derivative of the angular velocity omega.
    omega_norm: the norm of omega. Should remain constant."""
    def __init__(self):
        """Creates an instance of the class BodyFrame."""
        self.I = numpy.array([1,1,1])
        self.i = numpy.array([1,0,0])
        self.j = numpy.array([0,1,0])
        self.k = numpy.array([0,0,1])
        self.omega = numpy.array([0,0,0])
        self.omega_dot = numpy.array([0,0,0])
        self.omega_norm = numpy.linalg.norm(self.omega)


    def update(self,dt):
        """Updates the attributes of Body Frame for one timestep."""
        i_dot = numpy.cross(self.omega, i)
        j_dot = numpy.cross(self.omega, j)
        k_dot = numpy.cross(self.omega, k)

        omega_opendot=((self.I[1]-self.I[2])/self.I[0]*
                       self.omega[1]*self.omega[2]*self.i
                       +(self.I[2]-self.I[0])/self.I[1]*
                       self.omega[0]*self.omega[2]*self.j
                       +(self.I[0]-self.I[1])/self.I[2]*
                       self.omega[0]*self.omega[1]*self.k)

        self.omega_dot = (omega_opendot + self.omega[0]*i +
                          self.omega[1]*j +self.omega[2]*k)
        
        self.i = self.i + i_dot * dt #this is not normalized
        self.j = self.j + j_dot * dt #this is not normalized
        self.k = self.k + k_dot * dt #this is not normalized

        self.omega = self.omega + self.omega_dot * dt #this is not normalized

        self._scale()

    def _scale(self):
        """Scales the body frame axes and omega to their proper lengths.  For
        the axes, this is unit length, and for omega, this is the original
        length."""
        badnorm = numpy.linalg.norm(self.i)
        self.i = 1/badnorm * self.i

        badnorm = numpy.linalg.norm(self.j)
        self.j = 1/badnorm * self.j

        badnorm = numpy.linalg.norm(self.k)
        self.k = 1/badnorm * self.k
        
        if self.omega_norm != 0:
            badnorm = numpy.linalg.norm(self.omega)
            self.omega = self.omega_norm/badnorm * self.omega

if __name__ == "__main__":
    main()

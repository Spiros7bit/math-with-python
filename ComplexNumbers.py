'''
A module to deal with Complex Numbers
'''

from math import atan, sqrt, pi, degrees
from abc import ABC, abstractmethod
from math import atan, sqrt, pi, cos, sin, degrees

#Class for complex numbers
class Complex(ABC):
    #initializer
    def __init__(self):
        pass
    
    @abstractmethod
    def conjugate(self):
       pass
    
    @abstractmethod
    def transform():
        pass

#Class that specialize complex number to polar form (z = r,θ)
class Polar(Complex):
    #initializer
    def __init__(self, amplitude, phase):
        super().__init__()
        self.amplitude = amplitude
        self.phase = phase
    
    def __str__(self):
        return f"Polar Form: ({self.amplitude} , {self.phase})"

    def __repr__(self):
        return f"Polar( {self.amplitude},{self.phase} )"
    
    def __eq__(self, n):
        if self.amplitude == n.amplitude and self.phase == n.phase:
            return True
        return False
    
    def __gt__(self, n):
        if self.amplitude > n.amplitude and self.phase > n.phase:
            return True
        return False

    def __add__(self, n):
        if isinstance(n, Polar):
            #transform to cartesian
            real_n, imaginary_n = n.transform()
            real_self, imaginary_self = self.transform()

            #add them
            real = real_n + real_self
            imaginary = imaginary_n + imaginary_self

            #turn to polar again
            if real >= 0 and imaginary >= 0:
                phase = degrees( atan(imaginary/real ))
            elif real >= 0 and imaginary < 0:
                phase = degrees( 2*pi ) - degrees( atan(imaginary/real ))
            elif real < 0 and imaginary >= 0:
                phase = degrees( pi/2 ) - degrees( atan(imaginary/real ))  
            elif real < 0 and imaginary < 0:
                phase = degrees( pi ) - degrees( atan(imaginary/real ))
            amplitude = sqrt((real)**2 + (imaginary)**2)

            return Polar(amplitude, phase)

    def __sub__(self, n):
        if isinstance(n, Polar):
             #transform to cartesian
            real_n, imaginary_n = n.transform()
            real_self, imaginary_self = self.transform()

            #sub them
            real = real_self - real_n
            imaginary = imaginary_self - imaginary_n

            #turn to polar again
            if real >= 0 and imaginary >= 0:
                phase = degrees( atan(imaginary/real ))
            elif real >= 0 and imaginary < 0:
                phase = degrees( 2*pi ) - degrees( atan(imaginary/real ))
            elif real < 0 and imaginary >= 0:
                phase = degrees( pi/2 ) - degrees( atan(imaginary/real ))  
            elif real < 0 and imaginary < 0:
                phase = degrees( pi ) - degrees( atan(imaginary/real ))
            amplitude = sqrt((real)**2 + (imaginary)**2)

            return Polar(amplitude, phase)

    def __mul__(self, n):
        if isinstance(n, Polar):
            new_amplitude = self.amplitude * n.amplitude
            new_phase = self.phase + n.phase
        return Polar(new_amplitude, new_phase)
      
    
    def __truediv__(self, n):
        if isinstance(n, Polar):
            new_amplitude = self.amplitude / n.amplitude
            new_phase = self.phase - n.phase
        return Polar(new_amplitude, new_phase)
            

    #method to transform from polar to cartesian
    def transform(self):
        real = self.amplitude*cos(self.phase)
        imaginary = self.amplitude*sin(self.phase)

        return real, imaginary
    
    def conjugate(self):
        return Polar(self.amplitude, -self.phase)
        
#Class that specialize complex number to cartesian form ( z = x + yi )
class Cartesian(Complex):
    #initializer
    def __init__(self, real, imaginary):
        super().__init__()
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f"Cartesian Form: {self.real}+{self.imaginary}i"
        return f"Cartesian Form: {self.real}{self.imaginary}i"
    
    def __eq__(self, n):
        if self.real == n.real and self.imaginary == n.imaginary:
            return True

    def __gt__(self, n):
        if self.real > n.real and self.imaginary > n.imaginary:
            return True
        return False

    def __add__(self, n):
        if isinstance(n, Cartesian):
            return Cartesian(self.real+n.real, self.imaginary+n.imaginary)
    
    def __sub__(self, n):
        if isinstance(n, Cartesian):
            return Cartesian(self.real-n.real, self.imaginary-n.imaginary)
    
    def __mul__(self, n):
        if isinstance(n, Cartesian):
            rea = (self.real*n.real - self.imaginary*n.imaginary)
            im = (self.real*n.imaginary + self.imaginary*n.real)
            return Cartesian(rea, im)
    
    def __truediv__(self, n):
        if isinstance(n, Cartesian):
            a = Cartesian( n.real/((n.real)**2 + (n.imaginary)**2 ), -n.imaginary/((n.real)**2 + (n.imaginary)**2) ) 
            return self * a

    def __pow__(self, n):
        if isinstance(n, Cartesian):
            pass

    def conjugate(self):
        return Cartesian(self.real, -self.imaginary)

    #method to transform from cartesian to polar
    def transform(self):
        if self.real >= 0 and self.imaginary >= 0:
            phase = degrees( atan(self.imaginary/self.real ))
        elif self.real >= 0 and self.imaginary < 0:
            phase = degrees( 2*pi ) - degrees( atan(self.imaginary/self.real ))
        elif self.real < 0 and self.imaginary >= 0:
            phase = degrees( pi/2 ) - degrees( atan(self.imaginary/self.real ))  
        elif self.real < 0 and self.imaginary < 0:
            phase = degrees( pi ) - degrees( atan(self.imaginary/self.real ))
        amplitude = sqrt((self.real)**2 + (self.imaginary)**2)

        return amplitude, phase
    
    def plot(self):
        pass



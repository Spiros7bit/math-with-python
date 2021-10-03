'''
A module to deal with Complex Numbers
'''

from math import atan, sqrt, pi, degrees, cos, sin
from abc import ABC, abstractmethod

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
    def __init__(self, amplitude=0, phase=0):
        super().__init__()
        self.amplitude = amplitude
        self.phase = phase
    
    def __str__(self):
        return f"({self.amplitude} , {self.phase})"

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
        if isinstance(n, int):
           n = Polar(n,0)
        if isinstance(n, Polar):
            #transform to cartesian
            n = n.transform()
            self = self.transform()
            #add them
            cartesian_z = self + n
            #turn to polar again
            polar_z = cartesian_z.transform()
        #return in radians
        return polar_z


    def __sub__(self, n):
        if isinstance(n, int):
           n = Polar(n,0)
        if isinstance(n, Polar):
            #transform to cartesian
            n = n.transform()
            self = self.transform()
            #add them
            cartesian_z = self - n
            #turn to polar again
            polar_z = cartesian_z.transform()
        #return in radians
        return polar_z

    def __mul__(self, n):
        if isinstance(n, Cartesian):
            #if complex number is in Cartesian Form then transform to Polar Form...
            n.transform()
        if isinstance(n, Polar):
            new_amplitude = self.amplitude * n.amplitude
            new_phase = self.phase + n.phase
            return Polar(new_amplitude, new_phase)
      
    
    def __truediv__(self, n):
        if isinstance(n, Cartesian):
            #if complex number is in Cartesian Form then transform to Polar Form...
            n.transform()
        if isinstance(n, Polar):
            new_amplitude = self.amplitude / n.amplitude
            new_phase = self.phase - n.phase
            return Polar(new_amplitude, new_phase)
            
    #method to transform from polar to cartesian
    def transform(self):
        if isinstance(self, Polar):
            real = self.amplitude*cos(self.phase)
            imaginary = self.amplitude*sin(self.phase)
        return Cartesian(real, imaginary)
    
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
            return f"{self.real}+{self.imaginary}i"
        return f"{self.real}{self.imaginary}i"
    
    def __repr__(self):
        return f"Cartesian({self.real},{self.imaginary})"
    
    def __eq__(self, n):
        if self.real == n.real and self.imaginary == n.imaginary:
            return True
        #else
        #is not equal
        return False

    def __gt__(self, n):
        if self.real > n.real and self.imaginary > n.imaginary:
            return True
        #else
        #is less-equal
        return False
    
    def __lt__(self, n):
        if self.real > n.real and self.imaginary > n.imaginary:
            return True
        #else
        #is greater-equal
        return False

    def __add__(self, n):
        if isinstance(n, Polar):
            #if complex number is in Polar Form then transform to Cartesian Form...
            n = n.transform()
            return Cartesian(self.real+n.real, self.imaginary+n.imaginary)
        elif isinstance(n, int):
            n = Cartesian(n,0)
        return Cartesian(self.real-n.real, self.imaginary-n.imaginary)
    
    def __sub__(self, n):
        if isinstance(n, Polar):
            #if complex number is in Polar Form then transform to Cartesian Form...
            n = n.transform()
            return Cartesian(self.real+n.real, self.imaginary+n.imaginary)
        elif isinstance(n, int):
            n = Cartesian(n,0)
        return Cartesian(self.real-n.real, self.imaginary-n.imaginary)
    
    def __mul__(self, n):
        #the algorithm is to multiplicate in polar form and transform the result to cartesian form
        self = self.transform()
        if isinstance(n, Cartesian):
            n = n.transform()
        z = self*n
        z.transform()

        if isinstance(n, int):
            self = self.transform()
            z = Cartesian(self.real*n, self.imaginary*n)
        return z    
        
    def __truediv__(self, n):
        #the algorithm is to divide in polar form and transform the result to cartesian form
        self = self.transform()
        if isinstance(n, Cartesian):
            n = n.transform()
        z = self/n
        z.transform()

        if isinstance(n, int):
            self = self.transform()
            z = Cartesian(self.real/n, self.imaginary/n)
        return z 

    def conjugate(self):
        return Cartesian(self.real, -self.imaginary)

    #method to transform from cartesian to polar
    def transform(self):
        if isinstance(self, Cartesian):
            if self.real >= 0 and self.imaginary >= 0:
                phase = degrees( atan(self.imaginary/self.real ))
            elif self.real >= 0 and self.imaginary < 0:
                phase = degrees( 2*pi ) - degrees( atan(self.imaginary/self.real ))
            elif self.real < 0 and self.imaginary >= 0:
                phase = degrees( pi/2 ) - degrees( atan(self.imaginary/self.real ))  
            elif self.real < 0 and self.imaginary < 0:
                phase = degrees( pi ) - degrees( atan(self.imaginary/self.real ))
            amplitude = sqrt((self.real)**2 + (self.imaginary)**2)

        return Polar(amplitude, phase)
    



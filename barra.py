import numpy as np

g = 9.81 #kg*m/s^2


class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, R, t, E, ρ, σy):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.R = R
        self.t = t
        self.E = E
        self.ρ = ρ
        self.σy = σy

    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_area(self):
        A = np.pi*(self.R**2) - np.pi*((self.R-self.t)**2)
        return A

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        xi = reticulado.obtener_coordenada_nodal(self.ni)
        xj = reticulado.obtener_coordenada_nodal(self.nj)
        dij = xi-xj
        return np.sqrt(np.dot(dij,dij))

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        L = self.calcular_largo(reticulado)
        A = self.calcular_area()
        
        return self.ρ * A * L * g



    def obtener_rigidez(self, ret):
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz]).reshape((6,1))

        return self.E * A / L * (Tθ @ Tθ.T )

    def obtener_vector_de_cargas(self, ret):
        W = self.calcular_peso(ret)

        return np.array([0, 0, -W, 0, 0, -W])


    def obtener_fuerza(self, ret):
        ue = np.zeros(6)
        ue[0:3] = ret.obtener_desplazamiento_nodal(self.ni)
        ue[3:] = ret.obtener_desplazamiento_nodal(self.nj)
        
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz]).reshape((6,1))

        return self.E * A / L * (Tθ.T @ ue)





    def chequear_diseño(self, Fu,ret, ϕ=0.9):
        A = self.calcular_area()
        Fn = A*self.σy
        
        if ϕ*Fn < abs(Fu):
            return False
        else:
            return True


    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        calcular y devolver el factor de utilización
        """
        A = self.calcular_area()
        Fn = A*self.σy   
        FU = abs(Fu) / (ϕ*Fn) 
        
        return FU


    def rediseñar(self, Fu, ret, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        re-calcular el radio y el espesor de la barra de modo que
        se cumplan las disposiciones de diseño lo más cerca posible
        a FU = 1.0.
        """
        FU = self.obtener_factor_utilizacion(Fu, ϕ)
        A = self.calcular_area()
        Fn = A*self.σy
        
        def inercia(self):
            I = 3.141592*((self.R**4)-(self.R-self.t)**4)/4
            return I
        
        L = self.calcular_largo(ret)
        I = inercia(self)
        i =(I/A)**(1/2)
        landa = L/i
        
        while (FU <= 0.95) or (FU >= 1) or (Fn*ϕ < Fu) or (landa > 300):
            
            if (FU <= 0.95):
                self.R = 0.9*self.R #self.R += -1*cm   
                self.t = 0.9*self.t # self.t += -1*mm
        
            if (FU >= 1) or (Fn*ϕ < Fu):
                self.R = 1.1*self.R #self.R += 1*cm   
                self.t = 1.1*self.t #self.t += 1*mm
                
            I = inercia(self)
            i = (I/A)**(1/2)
            landa = L/i    
            FU = self.obtener_factor_utilizacion(Fu, ϕ)    
            A = self.calcular_area()
            Fn = A*self.σy
            
            if (landa > 300):
                self.R = 1.1*self.R #self.R += 1*cm
        
        
        
        return 
     
    
    
    
    
    
    
    
    
    
    
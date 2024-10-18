class Venta:
    def __init__(self, departamento):
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento
    
class Departamento:
    def __init__(self, nombre, cantidadVentas):
        self.nombre = nombre
        self.cantidadVentas = cantidadVentas

    def getNombre(self):
        return self.nombre
    
    def getCantidadVentas(self):
        return self.cantidadVentas
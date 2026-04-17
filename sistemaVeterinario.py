from abc import ABC, abstractmethod

# =========================
# CLASE ABSTRACTA PERSONA
# =========================
class Persona(ABC):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @abstractmethod
    def mostrar_rol(self):
        pass


# =========================
# CLASE CLIENTE
# =========================
class Cliente(Persona):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.mascotas = []  # Lista de mascotas del cliente

    def mostrar_rol(self):
        print(f"Cliente: {self.nombre}")

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota {mascota.nombre} agregada al cliente {self.nombre}")


# =========================
# CLASE VETERINARIO
# =========================
class Veterinario(Persona):
    def mostrar_rol(self):
        print(f"Veterinario: {self.nombre}")

    def tratar_mascota(self, mascota):
        print(f"Tratando a la mascota {mascota.nombre}")


# =========================
# CLASE RECEPCIONISTA
# =========================
class Recepcionista(Persona):
    def mostrar_rol(self):
        print(f"Recepcionista: {self.nombre}")

    def registrar_mascota_cliente(self, cliente, mascota):
        cliente.agregar_mascota(mascota)
        print(f"Recepcionista registró la mascota {mascota.nombre}")


# =========================
# CLASE MASCOTA
# =========================
class Mascota:
    def __init__(self, id_mascota, nombre, color, raza):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.color = color
        self.raza = raza

    def imprimir_info(self):
        print(f"Mascota: {self.nombre}, Color: {self.color}, Raza: {self.raza}")


# =========================
# CLASE TRATAMIENTO
# =========================
class Tratamiento:
    def __init__(self, id_tratamiento, nombre, tiempo_duracion):
        self.id_tratamiento = id_tratamiento
        self.nombre = nombre
        self.tiempo_duracion = tiempo_duracion

    def realizar_tratamiento(self):
        print(f"Realizando tratamiento: {self.nombre} ({self.tiempo_duracion} dias)")


# =========================
# CLASE CONSULTA
# =========================
class Consulta:
    def __init__(self, id_consulta):
        self.id_consulta = id_consulta
        self.tratamientos = []  # Lista de tratamientos

    def crear_tratamiento(self, tratamiento):
        self.tratamientos.append(tratamiento)
        print(f"Tratamiento {tratamiento.nombre} agregado a la consulta")

    def mostrar_tratamientos(self):
        for t in self.tratamientos:
            t.realizar_tratamiento()


# =========================
# CLASE ABSTRACTA METODO DE PAGO
# =========================
class MetodoPago(ABC):
    def __init__(self, id_pago, tipo, monto):
        self.id_pago = id_pago
        self.tipo = tipo
        self.monto = monto

    @abstractmethod
    def procesar_pago(self):
        pass


# =========================
# PAGOS CONCRETOS
# =========================
class PagoEfectivo(MetodoPago):
    def procesar_pago(self):
        print(f"Pago en efectivo de ${self.monto*2.2} pesos realizado")


class PagoTarjeta(MetodoPago):
    def procesar_pago(self):
        print(f"Pago con tarjeta de ${self.monto*2.5} pesos realizado")


class PagoTransferencia(MetodoPago):
    def procesar_pago(self):
        print(f"Pago por transferencia de ${self.monto*2} pesos realizado")


# =========================
# CLASE FACTURA
# =========================
class Factura:
    def __init__(self, id_factura, consulta):
        self.id_factura = id_factura
        self.consulta = consulta
        self.subtotal = 0
        self.impuesto = 0

    def totalizar(self):
        # Supongamos que cada tratamiento cuesta 70.000
        self.subtotal = len(self.consulta.tratamientos) * 70000
        self.impuesto = self.subtotal * 0.19
        total = self.subtotal + self.impuesto

        print(f"Subtotal: {self.subtotal}")
        print(f"Impuesto: {self.impuesto}")
        print(f"Total: {total}")

        return total

    def pagar(self, metodo_pago: MetodoPago):
        total = self.totalizar()
        metodo_pago.monto = total
        metodo_pago.procesar_pago()



# Crear personas
cliente1 = Cliente(1, "Marlon")
cliente2 = Cliente(2, "Adela")
cliente3 = Cliente(3, "Maria")
veterinario = Veterinario(2, "Dr. Cristian")
recepcionista = Recepcionista(3, "Ana")

# Crear mascota
mascota1 = Mascota(101, "Firulais", "Negro", "Labrador")
mascota2 = Mascota(102, "Fiona", "Cafe", "Persa")
mascota3 = Mascota(103, "Tiger", "Manchado", "Montañes")

# Registrar mascota
recepcionista.registrar_mascota_cliente(cliente1, mascota1)
recepcionista.registrar_mascota_cliente(cliente2, mascota2)
recepcionista.registrar_mascota_cliente(cliente3, mascota3)

# Crear consulta
consulta1 = Consulta(5001)
consulta2 = Consulta(5002)
consulta3 = Consulta(5003)


# Crear tratamientos
t1 = Tratamiento(1, "Vacunación", 30)
t2 = Tratamiento(2, "Desparasitación", 20)
t3 = Tratamiento(3, "Parto", 1)

consulta1.crear_tratamiento(t1)
consulta2.crear_tratamiento(t2)
consulta3.crear_tratamiento(t3)

# Mostrar tratamientos
consulta1.mostrar_tratamientos()
consulta2.mostrar_tratamientos()
consulta3.mostrar_tratamientos()

# Crear factura
factura1 = Factura(9001, consulta1)
factura2 = Factura(9002, consulta2)
factura3 = Factura(9003, consulta3)

# Pagar con tarjeta
pago1 = PagoTarjeta(1, "Tarjeta", 10000)
factura1.pagar(pago1)        


pago2 = PagoEfectivo(2, "Efectivo", 20000)
factura2.pagar(pago2)


pago3 = PagoTransferencia(3, "Transferencia", 50000)
factura3.pagar(pago3)
import os
import json
import datetime

Venta = []
Archivo = 'Pedidos.json'

Pizzas = {
  "margarita": {"pequeña": 5500, "mediana": 8500, "familiar": 11000},
  "mexicana": {"pequeña": 7000, "mediana": 10000, "familiar": 13000},
  "vegetariana": {"pequeña": 5000, "mediana": 8000, "familiar": 10500},
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def Orden():
  clear_console()  # Limpiar la consola al iniciar una nueva orden
  NombreCliente = input("ingrese su Nombre: ").lower()
  JornadaCliente = input("ingrese su jornada\nDiurno\nVespertino\nAdministrativo\n").lower()
  PizzaCliente = input("ingrese la Pizza que desea\nMargarita\nMexicana\nVegetariana: ").lower()
  TamañoPizza = input(f"ingrese el tamaño de la pizza de {PizzaCliente} tenemos \npequeña\nmediana\nfamiliar:\n").lower()

  if PizzaCliente in Pizzas and TamañoPizza in Pizzas[PizzaCliente]:
    precio = Pizzas[PizzaCliente][TamañoPizza]
    
    if JornadaCliente == "diurno":
      print(f"Por ser de la modalidad {JornadaCliente} posee un descuento del 15%")
      descuento = precio * 0.15
      precioPagar = precio - descuento
    elif JornadaCliente == "vespertino":
      print(f"Por ser de la modalidad {JornadaCliente} posee un descuento del 18%")
      descuento = precio * 0.18
      precioPagar = precio - descuento
    elif JornadaCliente == "administrativo":
      print(f"Por ser de la modalidad {JornadaCliente} posee un descuento del 11%")
      descuento = precio * 0.11
      precioPagar = precio - descuento
      
    DatosVenta = {
      "Nombre Cliente": NombreCliente,
      "Pizza Ordenada": PizzaCliente,
      "Tamaño Pizza": TamañoPizza,
      "Jornada Cliente": JornadaCliente,
      "Costo a Pagar": precioPagar,
      "Fecha": datetime.datetime.now().isoformat() 
    }

    Venta.append(DatosVenta)
  else:
    print("Tu Pizza o tamaño no está en el menú")

def buscar_ventas_cliente(NombreClienteBuscar):
  ventas_cliente = [venta for venta in Venta if venta["Nombre Cliente"] == NombreClienteBuscar.lower()]
  
  if ventas_cliente:
    print(f"Las ventas del cliente {NombreClienteBuscar} son las siguientes:\n")
    for venta in ventas_cliente:
      print(f"Pizza Ordenada: {venta['Pizza Ordenada']}, Tamaño: {venta['Tamaño Pizza']}, Jornada: {venta['Jornada Cliente']}, Costo: {venta['Costo a Pagar']}")
  else:
    print("No se encontró el cliente.")

def guardar_ventas():
  with open(Archivo, 'w') as archivo:
    json.dump(Venta, archivo)
  print("Se guardo Correctamente.")

def cargar_ventas():
  global Venta
  if os.path.exists(Archivo):
    with open(Archivo, 'r') as archivo:
      Venta = json.load(archivo)
    print(f"Las ventas han sido cargadas desde {Archivo}.")
  else:
    print(f"No se encontró el archivo {Archivo}.")
    
    
def generar_boleta():
  if not Venta:
    print("No hay ventas para generar boleta.")
    return

  NombreClienteBuscar = input("Ingrese el nombre del cliente para generar la boleta: ").lower()
  ventas_cliente = [venta for venta in Venta if venta["Nombre Cliente"] == NombreClienteBuscar]
  
  if ventas_cliente:
    print(f"Generando boleta para {NombreClienteBuscar}:\n")
    for venta in ventas_cliente:
      print(f"Pizza Ordenada: {venta['Pizza Ordenada']}, Tamaño: {venta['Tamaño Pizza']}, Jornada: {venta['Jornada Cliente']}, Costo: {venta['Costo a Pagar']}, Fecha: {venta['Fecha']}")
    total = sum(venta['Costo a Pagar'] for venta in ventas_cliente)
    print(f"\nTotal a pagar: {total} pesos.")
  else:
    print("No se encontraron ventas para el cliente.")

def Anular_Venta():
  NombreCliente = input("Ingrese el nombre del cliente para anular la venta: ").lower()
  PizzaCliente = input("Ingrese la pizza que desea anular: ").lower()
  TamañoPizza = input("Ingrese el tamaño de la pizza que desea anular: ").lower()
  JornadaCliente = input("Ingrese la jornada del cliente: ").lower()

  venta_encontrada = None
  for venta in Venta:
    if (venta["Nombre Cliente"] == NombreCliente and
        venta["Pizza Ordenada"] == PizzaCliente and
        venta["Tamaño Pizza"] == TamañoPizza and
        venta["Jornada Cliente"] == JornadaCliente):
      venta_encontrada = venta
      break

  if venta_encontrada:
    Venta.remove(venta_encontrada)
    print(f"La venta de la pizza {PizzaCliente} de tamaño {TamañoPizza} para el cliente {NombreCliente} ha sido anulada.")
  else:
    print("No se encontró una venta que coincida con los detalles.")

while True:
  try:
    print("-------------------------------------------------")
    print("****Bienvenidos a la Pizzas Duoc.****\n")
    print("1. Registrar una venta.")
    print("2. Mostrar todas las ventas.")
    print("3. Buscar ventas por cliente.")
    print("4. Guardar las ventas en un archivo.")
    print("5. Cargar las ventas desde un archivo.")
    print("6. Generar Boleta")
    print("7. Anular venta")
    print("8. Salir del programa.")
    print("-------------------------------------------------\n")
    opcion = int(input("Favor ingresar la opción deseada: "))

    if opcion == 1:
      Orden()
      print("Venta registrada correctamente.")

    elif opcion == 2:
      if Venta:
        for venta in Venta:
          print(venta)
          print("-------------------------------------------------")
      else:
        print("No hay ventas registradas.")
   
    elif opcion == 3:
      NombreClienteBuscar = input("Ingrese el nombre del cliente que quiere buscar las ventas: ").lower()
      buscar_ventas_cliente(NombreClienteBuscar)
    
    elif opcion == 4:
      guardar_ventas()
   
    elif opcion == 5:
      cargar_ventas()
    
    elif opcion == 6:
      generar_boleta()
    
    elif opcion == 7:
      Anular_Venta()
   
    elif opcion == 8:
      print("Saliendo del programa.")
      break
    else:
      print("Opción no válida, por favor intente de nuevo.")
  except Exception as e:
    print(f"Error: {e}")
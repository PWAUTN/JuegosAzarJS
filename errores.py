from decoracion import decorar


def validarIngresoEntero(leyenda=" "):
  while True:
    try:
      entero = int(input(leyenda))
      break
    except ValueError:
      print("Por favor debe ingresar un numero entero.")
      decorar()
  return entero

def validarIngresoPPT(leyenda=" "):
  while True:
    try:
      entero =int(input(leyenda))
      break
    except ValueError:
      print("Por favor debe ingresar una opcion valida.")
      decorar()
  return entero
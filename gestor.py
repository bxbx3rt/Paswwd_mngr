import os
import time

def guardar_cuentas(cuentas, archivo):
    with open(archivo, 'w') as f:
        for cuenta in cuentas:
            f.write(f"{cuenta['plataforma']},{cuenta['usuario']},{cuenta['contraseña']}\n")

def cargar_cuentas(archivo):
    cuentas = []
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            for line in f:
                plataforma, usuario, contraseña = line.strip().split(',')
                cuentas.append({'plataforma': plataforma, 'usuario': usuario, 'contraseña': contraseña})
    return cuentas

def mostrar_cuentas(cuentas):
    for i, cuenta in enumerate(cuentas, start=1):
        print(f"{i}. Plataforma: {cuenta['plataforma']}, Usuario: {cuenta['usuario']}, Contraseña: {cuenta['contraseña']}")

def buscar_cuenta(cuentas, palabra_clave):
    resultados = []
    for cuenta in cuentas:
        if palabra_clave.lower() in cuenta['plataforma'].lower():
            resultados.append(cuenta)
    return resultados

def eliminar_cuenta(cuentas, indices):
    indices.sort(reverse=True)
    for i in indices:
        cuentas.pop(i)

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def buscar_archivo_cuentas():
    archivo = 'cuentas.txt'
    
    for root, _, files in os.walk(os.getcwd()):
        if archivo in files:
            with open(os.path.join(root, archivo), 'r') as f:
                contenido = f.read()
                if contenido.strip() != "":
                    cuentas = cargar_cuentas(os.path.join(root, archivo))
                    return os.path.join(root, archivo), cuentas
                else:
                    with open(os.path.join(root, archivo), 'w') as f:
                        f.write("")
                    return os.path.join(root, archivo), []
    
    with open(archivo, 'w') as f:
        f.write("")
    return archivo, []

def verificar_usuario():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario == "rosoca2" and contraseña == "Roberto$oria":
        return "admin"
    elif usuario == "otro_usuario" and contraseña == "otra_contraseña":
        return "otro_admin"
    else:
        return "usuario_no_reconocido"

def main():
    acceso = verificar_usuario()
    if acceso == "admin" or acceso == "otro_admin":
        if acceso == "admin" or acceso == "otro_admin":
            print("\n\033[92mACCESO CONCEDIDO\033[0m")
            input("Presione cualquier tecla para continuar...")
        
        archivo, cuentas = buscar_archivo_cuentas()
        limpiar_pantalla = False  # Variable para controlar si se debe limpiar la pantalla

        while True:
            if limpiar_pantalla:
                clear_screen()

            print("\nMenu:")
            print("1. Añadir cuenta")
            if acceso == "admin" or acceso == "otro_admin":
                print("2. Eliminar cuenta(s)")
                print("3. Limpiar pantalla")
            print("4. Mostrar todas las cuentas")
            print("5. Buscar cuenta")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                plataforma = input("Plataforma: ")
                usuario = input("Usuario: ")
                contraseña = input("Contraseña: ")
                cuentas.append({'plataforma': plataforma, 'usuario': usuario, 'contraseña': contraseña})
                guardar_cuentas(cuentas, archivo)
                print("Cuenta añadida exitosamente.")

            elif (opcion == '2' and acceso == "admin") or (opcion == '2' and acceso == "otro_admin"):
                mostrar_cuentas(cuentas)
                eliminar_indices = input("Ingrese los números de las cuentas que desea eliminar (separados por comas): ")
                indices = [int(idx) - 1 for idx in eliminar_indices.split(',') if idx.isdigit() and int(idx) <= len(cuentas)]
                eliminar_cuenta(cuentas, indices)
                guardar_cuentas(cuentas, archivo)
                print("Cuentas eliminadas exitosamente.")

            elif (opcion == '3' and acceso == "admin") or (opcion == '3' and acceso == "otro_admin"):
                limpiar_pantalla = True

            elif opcion == '4':
                mostrar_cuentas(cuentas)

            elif opcion == '5':
                palabra_clave = input("Ingrese una palabra clave para buscar: ")
                resultados = buscar_cuenta(cuentas, palabra_clave)
                if resultados:
                    print("Resultados de la búsqueda:")
                    mostrar_cuentas(resultados)
                else:
                    print("No se encontraron resultados.")

            elif opcion == '6':
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    else:
        print("\n\033[91mACCESO DENEGADO\033[0m")
        time.sleep(3)

if __name__ == "__main__":
    main()

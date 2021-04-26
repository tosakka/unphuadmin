import mysql.connector as mysql
import sys
from mysql.connector import Error

base = mysql.connect(host="localhost",user="root",password="",database="unfu")
command_handler = base.cursor(buffered=True)

def sesion():
    while 1:
        print("\n Menu")
        print("1. Manejar estudiantes")
        print("2. Manejar profesores")
        print("3. Manejar materias")
        print("4. Manejar carreras")
        print("5. Manejar sesiones")
        print("6. Salir de la sesión")

        user_option = input(str("Digite su opcion: "))
        if user_option == "1":
            print("\n Menu de manejo de Estudiantes")
            print("1. Registrar estudiante")
            print("2. Eliminar estudiante")
            print("3. Listar estudiantes")
            print("4. Consultar estudiante")
            print("5. Actualizar estudiante")
            print("6. Regresar al menu principal.")
                    
            me_opcion = input(str("Digite su opcion: "))
            if me_opcion == "1":
                print("\n Registre al nuevo estudiante")
                nombre_usuario = input(str("Nombre de usuario del estudiante: "))
                contrasena = input(str("Clave del estudiante: "))
                query_vals = (nombre_usuario,contrasena)
                command_handler.execute("INSERT INTO estudiant (nombre,contrasena,privilegio) VALUES (%s,%s,'estudiante')",query_vals)
                base.commit()
                print(nombre_usuario + " ha sido registrado como estudiante")
            elif me_opcion == "2":
                print("\n Eliminar estudiante")
                nombre_usuario = input(str("Digite el usuario que desea eliminar: "))
                query_vals = (nombre_usuario,"estudiante")
                command_handler.execute("DELETE FROM estudiant WHERE nombre = %s AND privilegio = %s",query_vals)
                base.commit()
                if command_handler.rowcount < 1:
                    print("Ese usuario no existe")
                else:
                    print(nombre_usuario + " Ha sido removido del sistema.")
            elif me_opcion == "3":
                cursor = base.cursor()
                cursor.execute("SELECT * FROM estudiant")
                
                result = cursor.fetchall()
                for row in result:
                    print(row, '\n')
            elif me_opcion == "4":
                nombre_usuario = input(str("Nombre de usuario del estudiante: "))
                query_vals = (nombre_usuario)
                cursor = base.cursor()
                cursor.execute("SELECT * FROM estudiant WHERE nombre = '%s'",query_vals)
                base.commit()
                resultado = cursor.fetchone()
                print(resultado)

            elif me_opcion == "6":
                break
            else:
                print("Esa opcion no existe")

        elif user_option == "2":
            print("\n Menu de manejo de Profesores")
            print("1. Registrar profesor")
            print("2. Eliminar profesor")
            print("3. Listar profesores")
            print("4. Consultar profesor")
            print("5. Actualizar profesor")
            print("6. Regresar al menu principal.")

            mp_opcion = input(str("Digite su opcion: "))
            if mp_opcion == "1":
                print("\n Registre al nuevo profesor")
                nombre_usuario = input(str("Nombre de usuario del profesor: "))
                contrasena = input(str("Clave del profesor: "))
                query_vals = (nombre_usuario,contrasena)
                command_handler.execute("INSERT INTO maestro (nombre,contrasena,privilegio) VALUES (%s,%s,'profesor')",query_vals)
                base.commit()
                print(nombre_usuario + " ha sido registrado como profesor")
            elif mp_opcion == "2":
                print("\n Eliminar profesor")
                nombre_usuario = input(str("Digite el usuario que desea eliminar: "))
                query_vals = (nombre_usuario,"profesor")
                command_handler.execute("DELETE FROM maestro WHERE nombre = %s AND privilegio = %s",query_vals)
                base.commit()
                if command_handler.rowcount < 1:
                    print("Ese usuario no existe")
                else:
                    print(nombre_usuario + " Ha sido removido del sistema.")
            elif mp_opcion == "3":
                cursor = base.cursor()
                cursor.execute("SELECT * FROM maestro")
                
                result = cursor.fetchall()
                for row in result:
                    print(row, '\n')
            elif mp_opcion == "6":
                break
            else:
                print("Esa opcion no existe")

             

        elif user_option == "3":
            print("\n Menu de manejo de Materias")
            print("1. Registrar materia")
            print("2. Eliminar materia")
            print("3. Listar materias")
            print("4. Consultar materia")
            print("5. Actualizar materia")
            print("6. Regresar al menu principal.")

            mm_opcion = input(str("Digite su opcion: "))
            if mm_opcion == "1":
                print("\n Registre la nueva materia")
                nombre_materia = input(str("Nombre de la materia: "))
                creditos = input(str("Digite cuantos creditos tendra: "))
                query_vals = (nombre_materia,creditos)
                command_handler.execute("INSERT INTO materias (nombre_materia,creditos) VALUES (%s,%s)",query_vals)
                base.commit()
                print(nombre_materia + " ha sido registrado como materia")
            elif mm_opcion == "2":
                print("\n Eliminar Materia")
                nombre_usuario = input(str("Digite la materia que desea eliminar: "))
                query_vals = (nombre_materia)
                command_handler.execute("DELETE FROM maestro WHERE nombre = %s",query_vals)
                base.commit()
                if command_handler.rowcount < 1:
                    print("Esa materia no existe")
                else:
                    print(nombre_materia + " Ha sido removido del sistema.")
            elif mm_opcion == "3":
                cursor = base.cursor()
                cursor.execute("SELECT * FROM materias")
                
                result = cursor.fetchall()

        elif user_option == "4":
            print("\n Menu de manejo de Carreras")
            print("1. Registrar carrera")
            print("2. Eliminar carrera")
            print("3. Listar carreras")
            print("4. Consultar carrera")
            print("5. Actualizar carrera")
            print("6. Regresar al menu principal.")

            mc_opcion = input(str("Digite su opcion: "))
            if mc_opcion == "1":
                print("\n Registre la nueva carrera")
                nombre_carrera = input(str("Nombre de la carrera: "))
                periodos = input(str("Digite cuantos periodos tendra: "))
                query_vals = (nombre_carrera,periodos)
                command_handler.execute("INSERT INTO carreras (nombre_materia,creditos) VALUES (%s,%s)",query_vals)
                base.commit()
                print(nombre_carrera + " ha sido registrado como carrera")
            elif mc_opcion == "2":
                print("\n Eliminar Carrera")
                nombre_carrera = input(str("Digite la carrera que desea eliminar: "))
                query_vals = (nombre_materia)
                command_handler.execute("DELETE FROM carreras WHERE nombre_carrera = %s",query_vals)
                base.commit()
                if command_handler.rowcount < 1:
                    print("Esa carrera no existe")
                else:
                    print(nombre_carrera + " Ha sido removida del sistema.")
            elif mc_opcion == "3":
                cursor = base.cursor()
                cursor.execute("SELECT * FROM carreras")
                
                result = cursor.fetchall()

        elif user_option == "5":
            print("\n Menu de manejo de Sesiones")
            print("1. Registrar sesion")
            print("2. Eliminar sesion")
            print("3. Listar sesiones")
            print("4. Consultar sesion")
            print("5. Actualizar sesion")
            print("6. Regresar al menu principal.")

            ms_opcion = input(str("Digite su opcion: "))

        elif user_option == "6":
            print("Hasta luego")
            break


def auth():
    intentos = 0
    suceso = False
    while intentos <= 3 and not suceso:
        nombre_usuario = input(str("Nombre de usuario: "))
        contrasena = input(str("Clave: "))
            
        if nombre_usuario == "user" and contrasena == "1234":
            print("Bienvenido")
            sesion()
            suceso = True
        if not suceso:
            print("Datos incorrectos, por favor intente de nuevo.")
            intentos += 1
        if intentos == 3:
            sys.exit("Ha agotado todos sus intentos, el usuario queda bloqueado temporalmente.")
            
        else:
            print("Credenciales incorrectas.")


def main():
    while 1:
        print("placeholder")
        print("\n Presione 1 para iniciar sesion")

        user_option = input(str("Presione la tecla necesaria: "))
        if user_option == "1":
            auth()
            print("\n Inicio de Sesion \n")
        else:
            print("Esa funcion no se ha desarrollado aun.")

main()
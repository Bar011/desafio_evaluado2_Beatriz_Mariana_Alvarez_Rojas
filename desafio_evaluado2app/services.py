from desafio_evaluado2app.models import Curso, Profesor, Estudiante, Direccion
def crear_curso(codigo, nombre, version):

        # Verifica si ya existe un curso con el mismo código
        if Curso.objects.filter(codigo=codigo).exists():
            print("Ya existe un curso con este código.")
            return None
        
        # Crea un nuevo curso
        curso = Curso(codigo=codigo, nombre=nombre, version=version)
        curso.save()
        
        print("Curso creado exitosamente.")
        return curso

def crear_profesor(rut, nombre, apellido, activo=False, creado_por=None):

        # Verifica si ya existe un profesor con el mismo Rut
        if Profesor.objects.filter(rut=rut).exists():
            print("Ya existe un profesor con este Rut.")
            return None
        
        # Crea un nuevo profesor
        profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por) 
        profesor.save()
        #Imprime
        print("Profesor ingresado exitosamente.")
        return profesor
    

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo=False, creado_por=None):
        # Verifica si ya existe un estudiante con el mismo Rut
        if Estudiante.objects.filter(rut=rut).exists():
            print("Ya existe un estudiante con este Rut.")
            return None
        
        # Crea un nuevo estudiante
        estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)
        estudiante.save()
        
        print("Estudiante ingresado exitosamente.")
        return estudiante

def crear_direccion(estudiante,calle, numero, departamento, comuna, ciudad, region):
        
        try:
                estudiante = Estudiante.objects.get(rut=estudiante.rut)
                         # Aquí puedes usar el estudiante obtenido
                print(f"Estudiante encontrado: {estudiante.nombre} {estudiante.apellido}")
        except Estudiante.DoesNotExist:
                 print("No se encontró ningún estudiante con el ID especificado.")
        
        # Crea una nueva dirección para el estudiante
        direccion = Direccion(
            estudiante=estudiante,calle=calle,numero=numero,departamento=departamento,comuna=comuna,ciudad=ciudad,region=region
        )
        #Guarda la dirección creada
        direccion.save()
        #Imprime por pantalla
        print("Dirección del estudiante creada exitosamente.")
        return direccion

def obtiene_estudiante(rut):
        #Obtiene los estudiantes por rut
        estudiante = Estudiante.objects.get(rut=rut)
        print(f"Estudiante encontrado: {estudiante.nombre} {estudiante.apellido}")
        return estudiante
    
def obtiene_profesor(rut):
        #Obtiene los profesores por rut
        profesor = Profesor.objects.get(rut=rut)
        print(f"Profesor encontrado: {profesor.nombre} {profesor.apellido}")
        return profesor


def obtiene_curso(codigo):
        #Obtiene los cursos por código
        curso = Curso.objects.get(codigo=codigo)
        print(f"Curso encontrado: {curso.nombre}")
        return curso

def agrega_profesor_a_curso(profesor, curso):
        #Agrega el profesor al curso
        curso.profesores.add(profesor)
        print("Profesor asignado al curso correctamente.")


def agrega_cursos_a_estudiante(estudiante, curso):
        # Agrega el curso al estudiante
        estudiante.curso=curso
        estudiante.save()
        print("Curso asignado al estudiante correctamente.")

def imprime_estudiante_cursos():
        # Obtiene todos los cursos registrados
        cursos = Curso.objects.all()
        
        # Itera sobre cada curso
        for curso in cursos:
            print(f"Curso: {curso.codigo} - {curso.nombre} (Versión {curso.version})")
            print("Estudiantes:")
            estudiantes_curso = curso.estudiante_set.all()
            #Comprueba si la relación existe
            if estudiantes_curso.exists():
                for estudiante_curso in estudiantes_curso:
                    print(f"- {estudiante_curso.nombre} {estudiante_curso.apellido} (RUT: {estudiante_curso.rut})")
            else:
                print("- No hay estudiantes asociados a este curso")


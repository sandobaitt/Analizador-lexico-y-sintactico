import ply.lex as lex
import json
import sys
import os

tokens = [
    'FIRMA_DIGITAL_t', 'EQUIPOS_t', 'EDAD_t', 'FECHA_INICIO_t', 'FECHA_FIN_t',
    'NOMBRE_EQUIPO_t', 'IDENTIDAD_EQUIPO_t', 'DIRECCION_t', 'LINK_t', 'CARRERA_t', 'ASIGNATURA_t',
    'UNIVERSIDAD_REGIONAL_t', 'ALIANZA_EQUIPO_t', 'INTEGRANTES_t', 'PROYECTOS_t', 'CIUDAD_t',
    'CALLE_t', 'PAIS_t', 'NOMBRE_t', 'CARGO_t', 'FOTO_t', 'EMAIL_t', 'HABILIDADES_t', 'SALARIO_t',
    'ACTIVO_t', 'ESTADO_t', 'RESUMEN_t', 'TAREAS_t', 'VIDEO_t', 'CONCLUSION_t',
    'COMA', 'VERSION_t', 'LLAVEIZQ', 'LLAVEDER', 'CORCHIZQ', 'CORCHDER', 'DOS_PUNTOS', 'NULL_t', 'STRING_t'
]

# Ignorar espacios, tabs y saltos de línea
t_ignore = ' \t'
t_LLAVEIZQ    = r'\{'
t_LLAVEDER    = r'\}'
t_CORCHIZQ    = r'\['
t_CORCHDER    = r'\]'
t_DOS_PUNTOS  = r':'

# null
def t_NULL_t(t):
    r'null'
    t.value = None
    return t

# Nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comentarios
def t_COMMENT(t):
    r'\#.*|//.*'
    pass

# Tokens principales con valor asociado
def t_FIRMA_DIGITAL_t(t):
    r'FIRMA_DIGITAL_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_NOMBRE_EQUIPO_t(t):
    r'NOMBRE_EQUIPO_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_IDENTIDAD_EQUIPO_t(t):
    r'IDENTIDAD_EQUIPO_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_DIRECCION_t(t):
    r'DIRECCION_t\s+"[^"\n]+"'
    t.value = t.type
    return t

def t_CIUDAD_t(t):
    r'CIUDAD_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_CALLE_t(t):
    r'CALLE_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_PAIS_t(t):
    r'PAIS_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_CARRERA_t(t):
    r'CARRERA_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_ASIGNATURA_t(t):
    r'ASIGNATURA_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_UNIVERSIDAD_REGIONAL_t(t):
    r'UNIVERSIDAD_REGIONAL_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_ALIANZA_EQUIPO_t(t):
    r'ALIANZA_EQUIPO_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_NOMBRE_t(t):
    r'NOMBRE_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_PROYECTO_t(t):
    r'PROYECTO_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_RESUMEN_t(t):
    r'RESUMEN_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_CONCLUSION_t(t):
    r'CONCLUSION_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_ESTADO_t(t):
    r'ESTADO_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_LINK_t(t):
    r'LINK_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_VERSION_t(t):
    r'VERSION_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t
def t_EDAD_t(t):
    r'EDAD_t\s+[0-9]+'
    t.value = int(t.value.split()[1])
    return t

def t_EMAIL_t(t):
    r'EMAIL_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t
def t_CARGO_t(t):
    r'CARGO_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_FOTO_t(t):
    r'FOTO_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_HABILIDADES_t(t):
    r'HABILIDADES_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_SALARIO_t(t):
    r'SALARIO_t\s+[0-9]+(\.[0-9]+)?'
    salario = t.value.split()[1]
    t.value = float(salario) if '.' in salario else int(salario)
    return t

def t_ACTIVO_t(t):
    r'ACTIVO_t\s+(true|false)'
    t.value = t.value.split()[1] == "true"
    return t

def t_TAREAS_t(t):
    r'TAREAS_t'
    t.value = t.type  
    return t
    return t

def t_INTEGRANTES_t(t): 
    r'INTEGRANTES_t'
    t.value = t.type  
    return t
    return t

def t_FECHA_INICIO_t(t):
    r'FECHA_INICIO_t\s+"[0-9]{4}-[0-9]{2}-[0-9]{2}"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_FECHA_FIN_t(t):
    r'FECHA_FIN_t\s+"[0-9]{4}-[0-9]{2}-[0-9]{2}"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

def t_VIDEO_t(t):
    r'VIDEO_t\s+"[^"\n]+"'
    t.value = t.value.split('"', 1)[1][:-1]
    return t

# Reconocer nombres de tokens terminados en _t (si es que están en la lista de tokens)
def t_NAMETOKEN(t):
    r'[A-Z_]+_t'
    if t.value in tokens:
        t.type = t.value
        return t
    else:
        # Si no está en la lista de tokens, lo ignora
        pass

# Capturar valores booleanos
def t_BOOL_t(t):
    r'\btrue\b|\bfalse\b'
    return t


# Capturar números enteros
def t_INTEGER_t(t): 
    r'[0-9]+'
    return t

# Capturar números flotantes con dos decimales
def t_FLOAT_t(t):
    r'[0-9]+[.][0-9][0-9]'
    return t

# Capturar cadenas de texto 
def t_STRING_t(t):                   
    r'"[^\)^\]^\}^\"^\n]+"'                              
    return t  

# Detectar comas separadoras para listas
def t_COMA(t):
    r','
    return t

# Aca maneja los errores léxicos que pueden ocurrir durante el análisis
def t_error(t):
    print(f"[Error léxico] Línea {t.lineno}: carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Es ta es la construcción del lexer
lexer = lex.lex()

# Cargar JSON
def cargar_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error de formato JSON: {e}")
        return None

# Convertir JSON a texto plano para el lexer
def convertir_json_a_texto(datos):
    if not datos:
        return ""
    texto = ""
    texto += "{\n"
    if "firma_digital" in datos:
        texto += f'FIRMA_DIGITAL_t "{datos["firma_digital"]}"\n'
    for equipo in datos.get("equipos", []):
        if "nombre_equipo" in equipo:
            texto += f'NOMBRE_EQUIPO_t "{equipo["nombre_equipo"]}"\n'
        if "identidad_equipo" in equipo:
            texto += f'IDENTIDAD_EQUIPO_t "{equipo["identidad_equipo"]}"\n'
        if "link" in equipo:
            texto += f'LINK_t "{equipo["link"]}"\n'
        if "asignatura" in equipo:
            texto += f'ASIGNATURA_t "{equipo["asignatura"]}"\n'
        if "carrera" in equipo:
            texto += f'CARRERA_t "{equipo["carrera"]}"\n'
        if "universidad_regional" in equipo:
            texto += f'UNIVERSIDAD_REGIONAL_t "{equipo["universidad_regional"]}"\n'
        if "dirección" in equipo:
            dir = equipo["dirección"]
            texto += 'DIRECCION_t "DIRECCION"\n'
            texto += f'CALLE_t "{dir.get("calle","")}"\n'
            texto += f'CIUDAD_t "{dir.get("ciudad","")}"\n'
            texto += f'PAIS_t "{dir.get("país","")}"\n'
        if "alianza_equipo" in equipo:
            texto += f'ALIANZA_EQUIPO_t "{equipo["alianza_equipo"]}"\n'
        texto += "INTEGRANTES_t\n"
        for integrante in equipo.get("integrantes", []):
            texto += (
                f'NOMBRE_t "{integrante.get("nombre","")}", '
                f'EDAD_t {integrante.get("edad","")}, '
                f'CARGO_t "{integrante.get("cargo","")}", '
                f'FOTO_t "{integrante.get("foto","")}", '
                f'EMAIL_t "{integrante.get("email","")}", '
                f'HABILIDADES_t "{integrante.get("habilidades","")}", '
                f'SALARIO_t {integrante.get("salario","")}, '
                f'ACTIVO_t {str(integrante.get("activo","")).lower()}\n'
            )
        if "proyectos" in equipo:
            texto += "PROYECTOS_t\n"
            for proyecto in equipo.get("proyectos", []):
                if "nombre" in proyecto:
                    texto += f'NOMBRE_t "{proyecto["nombre"]}"\n'
                if "estado" in proyecto:
                    texto += f'ESTADO_t "{proyecto["estado"]}"\n'
                if "resumen" in proyecto:
                    texto += f'RESUMEN_t "{proyecto["resumen"]}"\n'
                texto += "TAREAS_t\n"
                for tarea in proyecto.get("tareas", []):
                    texto += (
                        f'NOMBRE_t "{tarea.get("nombre","")}", '
                        f'ESTADO_t "{tarea.get("estado","")}", '
                        f'RESUMEN_t "{tarea.get("resumen","")}", '
                        f'FECHA_INICIO_t "{tarea.get("fecha_inicio","")}", '
                        f'FECHA_FIN_t "{tarea.get("fecha_fin","")}"\n'
                    )
                if "fecha_inicio" in proyecto:
                    texto += f'FECHA_INICIO_t "{proyecto["fecha_inicio"]}"\n'
                if "fecha_fin" in proyecto:
                    texto += f'FECHA_FIN_t "{proyecto["fecha_fin"]}"\n'
                if "video" in proyecto:
                    texto += f'VIDEO_t "{proyecto["video"]}"\n'
                if "conclusion" in proyecto:
                    texto += f'CONCLUSION_t "{proyecto["conclusion"]}"\n'
    if "version" in datos:
        texto += f'VERSION_t "{datos["version"]}"\n'
    texto += "}\n"
    return texto

# Función para analizar el texto generado por el JSON con el lexer
def analizar_con_lexer(nombre_archivo_json):
    datos = cargar_json(nombre_archivo_json)
    texto = convertir_json_a_texto(datos)

    if texto:
        print("===================================")
        print("       Proyecto Lexer")
        print("     Grupo: Los Parceros")
        print("===================================\n")

        lexer.input(texto)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(f"Se encontró el token {tok.type} (tipo: {tok.type}) con valor: {tok.value}")
        input("\nPresione Enter para salir...")

def analizar_texto_directo():
    print("===================================")
    print("       Proyecto Lexer")
    print("     Grupo: Los Parceros")
    print("===================================\n")
    print("Ingrese el texto a analizar (puede pegarlo todo junto o línea por línea).")
    print("Finalice con una línea vacía o escriba 'salir':")
    lineas = []
    while True:
        try:
            linea = input()
        except EOFError:
            break
        if linea == "" or linea.strip().lower() == "salir":
            break
        lineas.append(linea)
    texto = "\n".join(lineas)
    # Si todo está en una sola línea, se procede a dividirlo de forma automatica
    if texto.count('\n') == 0:
        import re
        texto = re.sub(r'(?<!^)\b([A-Z_]+_t)\b', r'\n\1', texto)
    if texto:
        print("\n===================================")
        print("       Análisis de texto             ")
        print("===================================\n")
        lexer.input(texto)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(f"Se encontró el token {tok.type} (tipo: {tok.type}) con valor: {tok.value}")
    input("\nPresione Enter para salir...")

def analizar_json_por_pantalla():
    print("===================================")
    print("       Proyecto Lexer")
    print("     Grupo: Los Parceros")
    print("===================================\n")
    print("Pegue el JSON a analizar (finalice con una línea vacía o 'salir'):")
    lineas = []
    while True:
        try:
            linea = input()
        except EOFError:
            break
        if linea.strip() == "" or linea.strip().lower() == "salir":
            break
        lineas.append(linea)
    texto_json = "\n".join(lineas)
    try:
        datos = json.loads(texto_json)
    except Exception as e:
        print(f"Error al parsear el JSON: {e}")
        input("\nPresione Enter para salir...")
        return
    texto = convertir_json_a_texto(datos)
    print("\nTexto plano generado para el lexer:\n")
    print(texto)
    print("\n======= Análisis del lexer =======\n")
    lexer.input(texto)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Se encontró el token {tok.type} (tipo: {tok.type}) con valor: {tok.value}")
    input("\nPresione Enter para salir...")
    
def analizar_json_por_ruta():
    print("===================================")
    print("       Proyecto Lexer")
    print("     Grupo: Los Parceros")
    print("===================================\n")
    ruta = input("Ingrese la dirección del archivo a analizar:\n").strip()
    if not ruta:
        print("No se ingresó ninguna ruta.")
        return
    analizar_con_lexer(ruta)
    input("\nPresione Enter para salir...")

# Punto de entrada del nuestro programa 
if __name__ == "__main__":
    if len(sys.argv) == 2:
        archivo_json = sys.argv[1]
        analizar_con_lexer(archivo_json)
    else:
        print("Opciones:")
        print("1. Analizar texto plano por pantalla")
        print("2. Analizar JSON pegado por pantalla")
        print("3. Analizar archivo JSON por ruta")
        opcion = input("Seleccione opcion (1/2/3): ").strip()
        if opcion == "1":
            analizar_texto_directo()
        elif opcion == "2":
            analizar_json_por_pantalla()
        elif opcion == "3":
            analizar_json_por_ruta()
        else:
            print("Opción no válida.") 

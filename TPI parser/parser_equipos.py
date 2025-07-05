import ply.yacc as yacc
from Lexer import tokens
import json
import sys

#cd C:\Users\Sando\Desktop\Sintaxis\TPI 2025\TPI parser
#python parser_equipos.py datos.json

precedence = (
    ('nonassoc', 'STRING_t'),
    ('nonassoc', 'NULL_t'),
    
    ('nonassoc', 'VERSION_t'),
    ('nonassoc', 'FIRMA_DIGITAL_t'),
    ('nonassoc', 'NOMBRE_EQUIPO_t'),
    ('nonassoc', 'IDENTIDAD_EQUIPO_t'),
    ('nonassoc', 'DIRECCION_t'),
    ('nonassoc', 'LINK_t'),
    ('nonassoc', 'CARRERA_t'),
    ('nonassoc', 'ASIGNATURA_t'),
    ('nonassoc', 'UNIVERSIDAD_REGIONAL_t'),
    ('nonassoc', 'ALIANZA_EQUIPO_t'),
    ('nonassoc', 'INTEGRANTES_t'),
    ('nonassoc', 'PROYECTOS_t'),
    ('nonassoc', 'CALLE_t'),
    ('nonassoc', 'CIUDAD_t'),
    ('nonassoc', 'PAIS_t'),
    ('nonassoc', 'NOMBRE_t'),
    ('nonassoc', 'EDAD_t'),
    ('nonassoc', 'CARGO_t'),
    ('nonassoc', 'FOTO_t'),
    ('nonassoc', 'EMAIL_t'),
    ('nonassoc', 'HABILIDADES_t'),
    ('nonassoc', 'SALARIO_t'),
    ('nonassoc', 'ACTIVO_t'),
    ('nonassoc', 'ESTADO_t'),
    ('nonassoc', 'RESUMEN_t'),
    ('nonassoc', 'TAREAS_t'),
    ('nonassoc', 'FECHA_INICIO_t'),
    ('nonassoc', 'FECHA_FIN_t'),
    ('nonassoc', 'VIDEO_t'),
    ('nonassoc', 'CONCLUSION_t'),
    
    ('left', 'COMA'),
    ('left', 'DOS_PUNTOS'),
    ('left', 'LLAVEIZQ', 'LLAVEDER'),
    ('left', 'CORCHIZQ', 'CORCHDER'),
)

def p_inicio(p):
    'inicio : LLAVEIZQ ojson LLAVEDER'
    p[0] = f"<html><body>{p[2]}</body></html>"
    global html_result
    html_result = p[0]

def p_ojson(p):
    '''ojson : elemento
             | ojson COMA elemento'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[3]

def p_elemento(p):
    '''elemento : equipos
                | version
                | firma'''
    p[0] = p[1]

def p_version(p):
    'version : VERSION_t DOS_PUNTOS STRING_t'
    p[0] = f"<p><strong>Versión:</strong> {p[3]}</p>"

def p_firma(p):
    'firma : FIRMA_DIGITAL_t DOS_PUNTOS STRING_t'
    p[0] = f"<p><strong>Firma digital:</strong> {p[3]}</p>"

def p_equipos(p):
    'equipos : EQUIPOS_t DOS_PUNTOS CORCHIZQ lista_equipos CORCHDER'
    p[0] = p[4]

def p_lista_equipos(p):
    '''lista_equipos : LLAVEIZQ equipo LLAVEDER
                     | LLAVEIZQ equipo LLAVEDER COMA lista_equipos'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[2] + p[5]

def p_equipo(p):
    '''equipo : NOMBRE_EQUIPO_t COMA IDENTIDAD_EQUIPO_t COMA link COMA direccion COMA carrera_asignatura COMA universidad_regional COMA alianza_equipo COMA integrantes COMA proyectos
              | NOMBRE_EQUIPO_t COMA IDENTIDAD_EQUIPO_t COMA link COMA direccion COMA carrera_asignatura COMA universidad_regional COMA integrantes COMA proyectos'''
    nombre = f"<h1>{p[1]}</h1>"
    contenido = ''.join(x for x in p if isinstance(x, str) and not x.startswith("<h1>"))
    p[0] = f'<div style="border: 1px solid gray; padding: 20px;">{nombre}{contenido}</div>'

def p_direccion(p):
    '''direccion : DIRECCION_t DOS_PUNTOS NULL_t
                 | DIRECCION_t DOS_PUNTOS LLAVEIZQ direccion_campos LLAVEDER'''
    if len(p) == 4:
        p[0] = "<p>Dirección: No disponible</p>"
    else:
        p[0] = f"<p>Dirección: {p[4]}</p>"

def p_direccion_campos(p):
    '''direccion_campos : calle COMA ciudad COMA pais'''
    p[0] = ', '.join([p[1], p[3], p[5]])
    
def p_calle(p):
    'calle : CALLE_t'
    p[0] = p[1]

def p_ciudad(p):
    'ciudad : CIUDAD_t'
    p[0] = p[1]

def p_pais(p):
    'pais : PAIS_t'
    p[0] = p[1]

def p_link(p):
    'link : LINK_t'
    p[0] = f'<p><b>Link:</b> <a href="{p[1]}" target="_blank">{p[1]}</a></p>'

def p_universidad_regional(p):
    'universidad_regional : UNIVERSIDAD_REGIONAL_t'
    p[0] = f'<p><b>Universidad Regional:</b> {p[1]}</p>'

def p_carrera_asignatura(p):
    'carrera_asignatura : CARRERA_t COMA ASIGNATURA_t'
    p[0] = f"<p>Carrera: {p[1]} | Asignatura: {p[3]}</p>"

def p_alianza_equipo(p):
    'alianza_equipo : ALIANZA_EQUIPO_t'
    p[0] = f"<p><b>Alianza del equipo:</b> {p[1]}</p>"

def p_integrantes(p):
    'integrantes : INTEGRANTES_t DOS_PUNTOS CORCHIZQ lista_integrantes CORCHDER'
    p[0] = p[4]

def p_lista_integrantes(p):
    '''lista_integrantes : LLAVEIZQ integrante LLAVEDER
                         | LLAVEIZQ integrante LLAVEDER COMA lista_integrantes'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[2] + p[5]

def p_integrante(p):
    '''integrante : NOMBRE_t COMA EDAD_t COMA CARGO_t COMA FOTO_t COMA EMAIL_t COMA HABILIDADES_t COMA SALARIO_t COMA ACTIVO_t'''
    if len(p) != 16:
        print("[Error] Integrante con cantidad incorrecta de campos.")
        p[0] = "<div style='color:red;'>Error: Integrante con campos faltantes o de más.</div>"
    else:
        p[0] = (
            f"<h2>{p[1]}</h2><ul>"
            f"<li>Edad: {p[3]}</li>"
            f"<li>Cargo: {p[5]}</li>"
            f"<li>Foto: {p[7]}</li>"
            f"<li>Email: {p[9]}</li>"
            f"<li>Habilidades: {p[11]}</li>"
            f"<li>Salario: {p[13]}</li>"
            f"<li>Activo: {p[15]}</li>"
            "</ul>"
        )

def p_proyectos(p):
    'proyectos : PROYECTOS_t DOS_PUNTOS CORCHIZQ lista_proyectos CORCHDER'
    p[0] = p[4]

def p_lista_proyectos(p):
    '''lista_proyectos : LLAVEIZQ proyecto LLAVEDER
                       | LLAVEIZQ proyecto LLAVEDER COMA lista_proyectos'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[2] + p[5]

def p_proyecto(p):
    '''proyecto : NOMBRE_t COMA ESTADO_t COMA RESUMEN_t COMA tareas COMA FECHA_INICIO_t COMA FECHA_FIN_t COMA video COMA conclusion
                | NOMBRE_t COMA ESTADO_t COMA RESUMEN_t COMA tareas COMA FECHA_INICIO_t COMA FECHA_FIN_t'''
    if len(p) == 14:
        tabla = f'<table border="1"><tr><th>Nombre</th><th>Estado</th><th>Resumen</th><th>Fecha Inicio</th><th>Fecha Fin</th><th>Video</th><th>Conclusión</th></tr>'
        fila = f'<tr><td>{p[1]}</td><td>{p[3]}</td><td>{p[5]}</td><td>{p[7]}</td><td>{p[9]}</td><td>{p[11]}</td><td>{p[13]}</td></tr>'
        p[0] = f'<h3>{p[1]}</h3>{tabla}{fila}</table>'
    else:
        tabla = f'<table border="1"><tr><th>Nombre</th><th>Estado</th><th>Resumen</th><th>Fecha Inicio</th><th>Fecha Fin</th></tr>'
        fila = f'<tr><td>{p[1]}</td><td>{p[3]}</td><td>{p[5]}</td><td>{p[7]}</td><td>{p[9]}</td></tr>'
        p[0] = f'<h3>{p[1]}</h3>{tabla}{fila}</table>'

def p_video(p):
    'video : VIDEO_t'
    p[0] = f'<a href="{p[1]}" target="_blank">Ver video</a>'
    
def p_conclusion(p):
    'conclusion : CONCLUSION_t'
    p[0] = f'{p[1]}'

def p_tareas(p):
    'tareas : TAREAS_t lista_tareas'
    p[0] = p[2]

def p_lista_tareas(p):
    '''lista_tareas : LLAVEIZQ tarea LLAVEDER
                    | LLAVEIZQ tarea LLAVEDER COMA lista_tareas'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[2] + p[5]

def p_tarea(p):
    'tarea : NOMBRE_t COMA ESTADO_t COMA RESUMEN_t COMA FECHA_INICIO_t COMA FECHA_FIN_t'
    # Arma el HTML de la tarea aquí
    p[0] = f"<li>{p[1]} - {p[3]} - {p[5]} - {p[7]} - {p[9]}</li>"

def p_error(p):
    if p:
        print(f"[Error de sintaxis] Token inesperado: {p.type} en línea {p.lineno}")
    else:
        print("[Error de sintaxis] Fin de entrada inesperado")

parser = yacc.yacc()

def parse_input(data):
    return parser.parse(data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("===================================")
        print("   Proyecto Parser TPI 2025")
        print("     Grupo: Los Parceros")
        print("===================================\n")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        sys.exit(1)

    # Convertir el JSON a texto simulado para el lexer
    from Lexer import convertir_json_a_texto, lexer
    texto = convertir_json_a_texto(datos)

    # Ya no necesitas importar parser_equipos ni crear el parser aquí
    resultado_html = parse_input(texto)

    # Guardar HTML
    salida = archivo.replace(".json", ".html")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(resultado_html)
    print(f"\n✅ Archivo HTML generado: {salida}")

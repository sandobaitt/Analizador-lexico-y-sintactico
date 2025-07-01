import ply.yacc as yacc
from Lexer import tokens
import json
import sys

#cd C:\Users\Sando\Desktop\Sintaxis\TPI 2025\TPI parser
#python parser_equipos.py datos.json

html_result = ""

precedence = (
    ('nonassoc', 'STRING_t'),
    ('nonassoc', 'INTEGER_t'),
    ('nonassoc', 'FLOAT_t'),
    ('nonassoc', 'BOOL_t'),
    ('nonassoc', 'NULL_t'),
    ('nonassoc', 'EQUIPOS_t'),
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
    ('nonassoc', 'PROYECTO_t'),
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
    '''ojson : equipos
            | version
            | firma
            | equipos COMA version
            | version COMA equipos
            | equipos COMA firma
            | firma COMA equipos
            | version COMA firma
            | firma COMA version
            | equipos COMA version COMA firma
            | version COMA firma COMA equipos
            | firma COMA equipos COMA version'''
    p[0] = ''.join(str(x) for x in p[1:] if isinstance(x, str))

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
    '''equipo : NOMBRE_EQUIPO_t COMA IDENTIDAD_EQUIPO_t COMA direccion COMA carrera_asignatura COMA integrantes COMA proyectos
              | NOMBRE_EQUIPO_t COMA IDENTIDAD_EQUIPO_t COMA carrera_asignatura COMA integrantes COMA proyectos'''
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
    '''direccion_campos : calle COMA ciudad COMA pais
                        | ciudad COMA calle COMA pais
                        | pais COMA ciudad COMA calle'''
    p[0] = ', '.join([x for x in p[1::2]])
    
# NUEVOOOOOOOOOOOOOOOOOOOOO
def p_calle(p):
    'calle : CALLE_t'
    p[0] = p[1]

def p_ciudad(p):
    'ciudad : CIUDAD_t'
    p[0] = p[1]

def p_pais(p):
    'pais : PAIS_t'
    p[0] = p[1]

def p_carrera_asignatura(p):
    'carrera_asignatura : CARRERA_t COMA ASIGNATURA_t'
    p[0] = f"<p>Carrera: {p[1]} | Asignatura: {p[3]}</p>"

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
    p[0] = f"<h2>{p[1]}</h2><ul><li>Edad: {p[3]}</li><li>Cargo: {p[5]}</li><li>Foto: {p[7]}</li><li>Email: {p[9]}</li><li>Habilidades: {p[11]}</li><li>Salario: {p[13]}</li><li>Activo: {p[15]}</li></ul>"

def p_proyectos(p):
    'proyectos : PROYECTO_t DOS_PUNTOS CORCHIZQ lista_proyectos CORCHDER'
    p[0] = p[4]

def p_lista_proyectos(p):
    '''lista_proyectos : LLAVEIZQ proyecto LLAVEDER
                       | LLAVEIZQ proyecto LLAVEDER COMA lista_proyectos'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[2] + p[5]

def p_proyecto(p):
    'proyecto : NOMBRE_t COMA ESTADO_t COMA RESUMEN_t COMA tareas COMA FECHA_INICIO_t COMA FECHA_FIN_t COMA VIDEO_t COMA CONCLUSION_t'
    tabla = f'<table border="1"><tr><th>Nombre</th><th>Estado</th><th>Resumen</th><th>Fecha Inicio</th><th>Fecha Fin</th><th>Video</th><th>Conclusión</th></tr>'
    fila = f'<tr><td>{p[1]}</td><td>{p[3]}</td><td>{p[5]}</td><td>{p[7]}</td><td>{p[9]}</td><td>{p[11]}</td><td>{p[13]}</td></tr>'
    p[0] = f'<h3>{p[1]}</h3>{tabla}{fila}</table>'

def p_tareas(p):
    'tareas : ESTADO_t'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"[Error de sintaxis] Token inesperado: {p.type} en línea {p.lineno}")
    else:
        print("[Error de sintaxis] Fin de entrada inesperado")

def parse_input(data):
    parser = yacc.yacc()
    return parser.parse(data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python parser.py archivo.json")
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

    import parser_equipos  # asegurate de que el nombre del archivo no se llame igual
    resultado_html = parser_equipos.parse_input(texto)

    # Guardar HTML
    salida = archivo.replace(".json", ".html")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(resultado_html)
    print(f"\n✅ Archivo HTML generado: {salida}")

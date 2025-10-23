"""
SISTEMA DE MONITOREO INTELIGENTE DE CONSUMO HOGAREÑO

Proyecto ABP - Elementos de Matemática y Lógica
Aplicación de: Conjuntos, Conteo y Lógica Proposicional

Autor:

- Fernando Agustín Moyano

"""

from artefacto import Artefacto
from conjuntos import GestorConjuntos
from conteo import AnalizadorConteo
from logica import SistemaLogico
import os


def limpiar_pantalla():
    """Limpia la consola"""
    os.system("cls" if os.name == "nt" else "clear")


def pausa():
    """Pausa hasta que el usuario presione Enter"""
    input("\nPresiona Enter para continuar...")


def mostrar_banner():
    """Muestra el banner del sistema"""
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║    🏠 SISTEMA DE MONITOREO DE CONSUMO HOGAREÑO 🏠       ║
║                                                          ║
║         Aplicando Matemática y Lógica al Hogar          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)


def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "=" * 60)
    print("                    MENÚ PRINCIPAL")
    print("=" * 60)
    print()
    print("  1️⃣  Agregar artefacto")
    print("  2️⃣  Ver todos los artefactos")
    print("  3️⃣  Consultas por conjuntos")
    print("  4️⃣  Análisis estadístico (Conteo)")
    print("  5️⃣  Sistema de recomendaciones (Lógica)")
    print("  6️⃣  Reporte completo")
    print("  7️⃣  Cargar datos de ejemplo")
    print("  0️⃣  Salir")
    print()
    print("=" * 60)


def menu_agregar_artefacto(gestor):
    """Menú para agregar un nuevo artefacto"""
    limpiar_pantalla()
    print("\n" + "=" * 60)
    print("           AGREGAR NUEVO ARTEFACTO")
    print("=" * 60 + "\n")

    try:
        nombre = input("📝 Nombre del artefacto: ").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío")
            pausa()
            return

        watts = float(input("⚡ Potencia en watts (W): "))
        if watts <= 0:
            print("❌ La potencia debe ser mayor a 0")
            pausa()
            return

        horas = float(input("⏰ Horas de uso diario: "))
        if horas < 0 or horas > 24:
            print("❌ Las horas deben estar entre 0 y 24")
            pausa()
            return

        ubicacion = input("📍 Ubicación (ej: Cocina, Dormitorio): ").strip()
        if not ubicacion:
            print("❌ La ubicación no puede estar vacía")
            pausa()
            return

        tipo = input("🔧 Tipo (ej: Electrodoméstico, Iluminación): ").strip()
        if not tipo:
            print("❌ El tipo no puede estar vacío")
            pausa()
            return

        artefacto = Artefacto(nombre, watts, horas, ubicacion, tipo)
        gestor.agregar_artefacto(artefacto)

        print(f"\n{artefacto.info_completa()}")

    except ValueError:
        print("\n❌ Error: Debes ingresar valores numéricos válidos")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")

    pausa()


def menu_ver_artefactos(gestor):
    """Muestra todos los artefactos registrados"""
    limpiar_pantalla()
    print("\n" + "=" * 60)
    print("           ARTEFACTOS REGISTRADOS")
    print("=" * 60 + "\n")

    if not gestor.universo:
        print("⚠️  No hay artefactos registrados todavía.\n")
        pausa()
        return

    print(f"Total de artefactos: {len(gestor.universo)}\n")

    for nombre in sorted(gestor.universo):
        art = gestor.obtener_artefacto(nombre)
        print(f"  • {art.nombre}")
        print(
            f"    └─ {art.watts}W | {art.horas_dia}h/día | {art.ubicacion} | {art.tipo}"
        )
        print(
            f"       Nivel: {art.nivel_consumo()} | Consumo: {art.consumo_mensual():.2f} kWh/mes\n"
        )

    pausa()


def menu_consultas_conjuntos(gestor):
    """Menú de operaciones con conjuntos"""
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 60)
        print("           CONSULTAS POR CONJUNTOS")
        print("=" * 60 + "\n")

        if not gestor.universo:
            print("⚠️  No hay artefactos registrados todavía.\n")
            pausa()
            return

        print("  1. Ver por ubicación")
        print("  2. Ver por tipo")
        print("  3. Ver por nivel de consumo")
        print("  4. Operación: Unión (A ∪ B)")
        print("  5. Operación: Intersección (A ∩ B)")
        print("  6. Operación: Diferencia (A - B)")
        print("  7. Operación: Complemento (U - A)")
        print("  0. Volver al menú principal")
        print()

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "0":
            break
        elif opcion == "1":
            consulta_por_ubicacion(gestor)
        elif opcion == "2":
            consulta_por_tipo(gestor)
        elif opcion == "3":
            consulta_por_consumo(gestor)
        elif opcion == "4":
            operacion_union(gestor)
        elif opcion == "5":
            operacion_interseccion(gestor)
        elif opcion == "6":
            operacion_diferencia(gestor)
        elif opcion == "7":
            operacion_complemento(gestor)
        else:
            print("❌ Opción no válida")
            pausa()


def consulta_por_ubicacion(gestor):
    """Consulta artefactos por ubicación"""
    limpiar_pantalla()
    print("\n📍 CONSULTA POR UBICACIÓN\n")

    ubicaciones = gestor.obtener_todas_ubicaciones()
    print("Ubicaciones disponibles:")
    for ubi in sorted(ubicaciones):
        print(f"  • {ubi}")

    ubicacion = input("\nIngresa la ubicación: ").strip()
    conjunto = gestor.obtener_por_ubicacion(ubicacion)
    gestor.mostrar_conjunto(conjunto, f"Artefactos en '{ubicacion}'")
    pausa()


def consulta_por_tipo(gestor):
    """Consulta artefactos por tipo"""
    limpiar_pantalla()
    print("\n🔧 CONSULTA POR TIPO\n")

    tipos = gestor.obtener_todos_tipos()
    print("Tipos disponibles:")
    for tipo in sorted(tipos):
        print(f"  • {tipo}")

    tipo = input("\nIngresa el tipo: ").strip()
    conjunto = gestor.obtener_por_tipo(tipo)
    gestor.mostrar_conjunto(conjunto, f"Artefactos tipo '{tipo}'")
    pausa()


def consulta_por_consumo(gestor):
    """Consulta artefactos por nivel de consumo"""
    limpiar_pantalla()
    print("\n⚡ CONSULTA POR NIVEL DE CONSUMO\n")
    print("Niveles disponibles: ALTO, MEDIO, BAJO\n")

    nivel = input("Ingresa el nivel: ").strip().upper()
    if nivel in ["ALTO", "MEDIO", "BAJO"]:
        conjunto = gestor.obtener_por_nivel_consumo(nivel)
        gestor.mostrar_conjunto(conjunto, f"Artefactos de consumo {nivel}")
    else:
        print("❌ Nivel no válido")
    pausa()


def operacion_union(gestor):
    """Realiza operación de unión entre dos conjuntos"""
    limpiar_pantalla()
    print("\n∪ OPERACIÓN: UNIÓN (A ∪ B)\n")
    print("Elementos que están en A o en B o en ambos\n")

    # Ejemplo práctico
    print("Ejemplo: Cocina ∪ Alto Consumo")
    cocina = gestor.obtener_por_ubicacion("Cocina")
    alto = gestor.obtener_por_nivel_consumo("ALTO")

    gestor.mostrar_conjunto(cocina, "A: Artefactos en Cocina")
    gestor.mostrar_conjunto(alto, "B: Artefactos de Alto Consumo")

    union = gestor.union(cocina, alto)
    gestor.mostrar_conjunto(union, "A ∪ B: Unión")

    print("\n📊 Verificación: |A ∪ B| = |A| + |B| - |A ∩ B|")
    print(f"   {len(union)} = {len(cocina)} + {len(alto)} - {len(cocina & alto)}")

    pausa()


def operacion_interseccion(gestor):
    """Realiza operación de intersección entre dos conjuntos"""
    limpiar_pantalla()
    print("\n∩ OPERACIÓN: INTERSECCIÓN (A ∩ B)\n")
    print("Elementos que están en A y en B simultáneamente\n")

    print("Ejemplo: Cocina ∩ Alto Consumo")
    cocina = gestor.obtener_por_ubicacion("Cocina")
    alto = gestor.obtener_por_nivel_consumo("ALTO")

    gestor.mostrar_conjunto(cocina, "A: Artefactos en Cocina")
    gestor.mostrar_conjunto(alto, "B: Artefactos de Alto Consumo")

    interseccion = gestor.interseccion(cocina, alto)
    gestor.mostrar_conjunto(interseccion, "A ∩ B: Intersección")

    print("\n💡 Interpretación: Artefactos críticos en la cocina")

    pausa()


def operacion_diferencia(gestor):
    """Realiza operación de diferencia entre dos conjuntos"""
    limpiar_pantalla()
    print("\n- OPERACIÓN: DIFERENCIA (A - B)\n")
    print("Elementos que están en A pero no en B\n")

    print("Ejemplo: Todos - Alto Consumo")
    todos = gestor.universo.copy()
    alto = gestor.obtener_por_nivel_consumo("ALTO")

    gestor.mostrar_conjunto(todos, "A: Todos los artefactos (Universo)")
    gestor.mostrar_conjunto(alto, "B: Artefactos de Alto Consumo")

    diferencia = gestor.diferencia(todos, alto)
    gestor.mostrar_conjunto(diferencia, "A - B: Diferencia")

    print("\n💡 Interpretación: Artefactos que NO son de alto consumo")

    pausa()


def operacion_complemento(gestor):
    """Realiza operación de complemento"""
    limpiar_pantalla()
    print("\n¬ OPERACIÓN: COMPLEMENTO (U - A)\n")
    print("Elementos del universo que no están en A\n")

    print("Ejemplo: Complemento de 'Cocina'")
    cocina = gestor.obtener_por_ubicacion("Cocina")

    gestor.mostrar_conjunto(gestor.universo, "U: Universo (Todos)")
    gestor.mostrar_conjunto(cocina, "A: Artefactos en Cocina")

    complemento = gestor.complemento(cocina)
    gestor.mostrar_conjunto(complemento, "U - A: Complemento")

    print("\n💡 Interpretación: Artefactos fuera de la cocina")

    pausa()


def menu_analisis_estadistico(conteo):
    """Menú de análisis estadístico"""
    limpiar_pantalla()
    print(conteo.generar_reporte_estadistico())
    pausa()


def menu_sistema_logico(sistema_logico):
    """Menú del sistema de recomendaciones"""
    limpiar_pantalla()
    print(sistema_logico.generar_reporte_logico())
    pausa()


def generar_reporte_completo(gestor, conteo, logica):
    """Genera un reporte completo del sistema"""
    limpiar_pantalla()

    print("\n" + "╔" + "=" * 58 + "╗")
    print("║" + " " * 14 + "REPORTE COMPLETO DEL SISTEMA" + " " * 16 + "║")
    print("╚" + "=" * 58 + "╝")

    # Sección 1: Estadísticas
    print(conteo.generar_reporte_estadistico())

    # Sección 2: Análisis Lógico
    print(logica.generar_reporte_logico())

    # Sección 3: Detalles por conjunto
    print("\n" + "=" * 60)
    print("   ANÁLISIS DETALLADO POR CONJUNTOS")
    print("=" * 60 + "\n")

    print("📍 POR UBICACIÓN:")
    for ubicacion in sorted(gestor.obtener_todas_ubicaciones()):
        conjunto = gestor.obtener_por_ubicacion(ubicacion)
        print(f"   {ubicacion}: {len(conjunto)} artefacto(s)")

    print("\n🔧 POR TIPO:")
    for tipo in sorted(gestor.obtener_todos_tipos()):
        conjunto = gestor.obtener_por_tipo(tipo)
        print(f"   {tipo}: {len(conjunto)} artefacto(s)")

    print("\n⚡ POR NIVEL DE CONSUMO:")
    for nivel in ["ALTO", "MEDIO", "BAJO"]:
        conjunto = gestor.obtener_por_nivel_consumo(nivel)
        print(f"   {nivel}: {len(conjunto)} artefacto(s)")

    print("\n" + "=" * 60 + "\n")

    pausa()


def cargar_datos_ejemplo(gestor):
    """Carga datos de ejemplo para pruebas"""
    limpiar_pantalla()
    print("\n🔄 Cargando datos de ejemplo...\n")

    ejemplos = [
        Artefacto("Heladera", 150, 24, "Cocina", "Electrodoméstico"),
        Artefacto("Microondas", 1200, 0.5, "Cocina", "Electrodoméstico"),
        Artefacto("Aire Acondicionado", 2000, 8, "Dormitorio", "Climatización"),
        Artefacto("Televisor LED", 80, 6, "Sala", "Electrónica"),
        Artefacto("Notebook", 65, 8, "Oficina", "Electrónica"),
        Artefacto("Lámpara LED", 10, 5, "Dormitorio", "Iluminación"),
        Artefacto("Cafetera", 1000, 0.3, "Cocina", "Electrodoméstico"),
        Artefacto("Ventilador", 75, 6, "Sala", "Climatización"),
        Artefacto("Plancha", 1500, 1, "Lavadero", "Electrodoméstico"),
        Artefacto("Router WiFi", 12, 24, "Oficina", "Electrónica"),
    ]

    for art in ejemplos:
        gestor.agregar_artefacto(art)

    print(f"\n✅ {len(ejemplos)} artefactos cargados exitosamente!\n")
    pausa()


def main():
    """Función principal del programa"""
    # Inicializar componentes
    gestor = GestorConjuntos()
    conteo = AnalizadorConteo(gestor)
    logica = SistemaLogico(gestor, conteo)

    while True:
        limpiar_pantalla()
        mostrar_banner()
        mostrar_menu_principal()

        opcion = input("👉 Selecciona una opción: ").strip()

        if opcion == "1":
            menu_agregar_artefacto(gestor)
        elif opcion == "2":
            menu_ver_artefactos(gestor)
        elif opcion == "3":
            menu_consultas_conjuntos(gestor)
        elif opcion == "4":
            if not gestor.universo:
                print("\n⚠️  No hay artefactos registrados. Carga datos primero.")
                pausa()
            else:
                menu_analisis_estadistico(conteo)
        elif opcion == "5":
            if not gestor.universo:
                print("\n⚠️  No hay artefactos registrados. Carga datos primero.")
                pausa()
            else:
                menu_sistema_logico(logica)
        elif opcion == "6":
            if not gestor.universo:
                print("\n⚠️  No hay artefactos registrados. Carga datos primero.")
                pausa()
            else:
                generar_reporte_completo(gestor, conteo, logica)
        elif opcion == "7":
            cargar_datos_ejemplo(gestor)
        elif opcion == "0":
            limpiar_pantalla()
            print("\n" + "=" * 60)
            print("   Gracias por usar el Sistema de Monitoreo Hogareño")
            print("=" * 60 + "\n")
            print("   Desarrollado con 💚 aplicando:")
            print("   • Teoría de Conjuntos")
            print("   • Principios de Conteo")
            print("   • Lógica Proposicional")
            print("\n" + "=" * 60 + "\n")
            break
        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")
            pausa()


if __name__ == "__main__":
    main()

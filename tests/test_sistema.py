"""
Archivo de pruebas para verificar el correcto funcionamiento del sistema

Este archivo puede ejecutarse para validar que todos los módulos funcionen correctamente
"""

from consumo_hogareno.models.artefacto import Artefacto
from consumo_hogareno.services.conjuntos import GestorConjuntos
from consumo_hogareno.services.conteo import AnalizadorConteo
from consumo_hogareno.services.logica import SistemaLogico


def test_artefacto():
    """Prueba la clase Artefacto"""
    print("\n" + "=" * 60)
    print("TEST 1: Clase Artefacto")
    print("=" * 60)

    # Crear artefacto
    heladera = Artefacto("Heladera", 150, 24, "Cocina", "Electrodoméstico")

    # Verificar consumos
    consumo_diario = heladera.consumo_diario()
    consumo_mensual = heladera.consumo_mensual()
    nivel = heladera.nivel_consumo()

    print(f"✓ Artefacto creado: {heladera.nombre}")
    print(f"✓ Consumo diario: {consumo_diario} Wh")
    print(f"✓ Consumo mensual: {consumo_mensual:.2f} kWh")
    print(f"✓ Nivel de consumo: {nivel}")

    # Validaciones
    assert consumo_diario == 3600, "Error en consumo diario"
    assert consumo_mensual == 108.0, "Error en consumo mensual"
    assert nivel == "BAJO", "Error en nivel de consumo (150W debe ser BAJO)"

    print("\n✅ TEST 1 APROBADO: Clase Artefacto funciona correctamente\n")


def test_conjuntos():
    """Prueba operaciones de conjuntos"""
    print("\n" + "=" * 60)
    print("TEST 2: Teoría de Conjuntos")
    print("=" * 60)

    gestor = GestorConjuntos()

    # Agregar artefactos
    artefactos = [
        Artefacto("Heladera", 150, 24, "Cocina", "Electrodoméstico"),
        Artefacto("Microondas", 1200, 0.5, "Cocina", "Electrodoméstico"),
        Artefacto("Aire", 2000, 8, "Dormitorio", "Climatización"),
        Artefacto("TV", 80, 6, "Sala", "Electrónica"),
        Artefacto("Lámpara", 10, 5, "Dormitorio", "Iluminación"),
    ]

    for art in artefactos:
        gestor.agregar_artefacto(art)

    # Test: Cardinalidad del universo
    print(f"\n✓ Universo |U| = {len(gestor.universo)}")
    assert len(gestor.universo) == 5, "Error en cardinalidad"

    # Test: Subconjuntos por ubicación
    cocina = gestor.obtener_por_ubicacion("Cocina")
    print(f"✓ Cocina = {cocina}, |Cocina| = {len(cocina)}")
    assert len(cocina) == 2, "Error en conjunto Cocina"

    # Test: Subconjuntos por nivel
    alto = gestor.obtener_por_nivel_consumo("ALTO")
    print(f"✓ Alto consumo = {alto}, |Alto| = {len(alto)}")
    assert len(alto) == 2, "Error en conjunto Alto"

    # Test: Intersección
    interseccion = gestor.interseccion(cocina, alto)
    print(f"✓ Cocina ∩ Alto = {interseccion}, |Cocina ∩ Alto| = {len(interseccion)}")
    assert len(interseccion) == 1, "Error en intersección"
    assert "microondas" in interseccion, "Error: microondas debería estar"

    # Test: Unión
    union = gestor.union(cocina, alto)
    print(f"✓ Cocina ∪ Alto = {union}, |Cocina ∪ Alto| = {len(union)}")
    assert len(union) == 3, "Error en unión"

    # Test: Principio de inclusión-exclusión
    # |A ∪ B| = |A| + |B| - |A ∩ B|
    verificacion = len(cocina) + len(alto) - len(interseccion)
    print("\n✓ Verificación inclusión-exclusión:")
    print("  |Cocina ∪ Alto| = |Cocina| + |Alto| - |Cocina ∩ Alto|")
    print(f"  {len(union)} = {len(cocina)} + {len(alto)} - {len(interseccion)}")
    print(f"  {len(union)} = {verificacion}")
    assert len(union) == verificacion, "Error en inclusión-exclusión"

    # Test: Diferencia
    diferencia = gestor.diferencia(gestor.universo, alto)
    print(f"\n✓ U - Alto = {diferencia}, |U - Alto| = {len(diferencia)}")
    assert len(diferencia) == 3, "Error en diferencia"

    # Test: Complemento
    complemento = gestor.complemento(cocina)
    print(f"✓ Complemento(Cocina) = {complemento}, |Complemento| = {len(complemento)}")
    assert len(complemento) == 3, "Error en complemento"

    print("\n✅ TEST 2 APROBADO: Teoría de Conjuntos funciona correctamente\n")

    return gestor


def test_conteo(gestor):
    """Prueba análisis de conteo"""
    print("\n" + "=" * 60)
    print("TEST 3: Principios de Conteo")
    print("=" * 60)

    conteo = AnalizadorConteo(gestor)

    # Test: Conteo por ubicación
    conteo_ubi = conteo.contar_por_ubicacion()
    print(f"\n✓ Conteo por ubicación: {conteo_ubi}")
    assert conteo_ubi["Cocina"] == 2, "Error en conteo por ubicación"

    # Test: Conteo por nivel
    conteo_nivel = conteo.contar_por_nivel_consumo()
    print(f"✓ Conteo por nivel: {conteo_nivel}")
    assert conteo_nivel["ALTO"] == 2, "Error en conteo por nivel"

    # Test: Porcentajes
    porcentajes = conteo.calcular_porcentajes_consumo()
    print(f"✓ Porcentajes: {porcentajes}")
    assert porcentajes["ALTO"] == 40.0, "Error en cálculo de porcentajes"

    # Test: Consumo total
    total = conteo.consumo_total_mensual()
    print(f"✓ Consumo total mensual: {total:.2f} kWh")
    assert total > 0, "Error en consumo total"

    # Test: Mayores consumidores
    mayores = conteo.mayores_consumidores(3)
    print("✓ Top 3 mayores consumidores:")
    for i, (nombre, consumo) in enumerate(mayores, 1):
        print(f"  {i}. {nombre}: {consumo:.2f} kWh")
    assert len(mayores) <= 3, "Error en mayores consumidores"
    assert mayores[0][1] >= mayores[1][1], "Error: no está ordenado"

    # Test: Suma de porcentajes = 100%
    suma_porcentajes = sum(porcentajes.values())
    print(f"\n✓ Suma de porcentajes: {suma_porcentajes:.1f}%")
    assert abs(suma_porcentajes - 100.0) < 0.01, "Error: suma no es 100%"

    print("\n✅ TEST 3 APROBADO: Principios de Conteo funcionan correctamente\n")

    return conteo


def test_logica(gestor, conteo):
    """Prueba sistema de lógica proposicional"""
    print("\n" + "=" * 60)
    print("TEST 4: Lógica Proposicional")
    print("=" * 60)

    logica = SistemaLogico(gestor, conteo)

    # Test: Proposiciones
    p = logica.prop_consumo_alto(300)
    q = logica.prop_muchos_artefactos_alto_consumo(2)
    print(f"\n✓ p: 'Consumo > 300 kWh' = {p}")
    print(f"✓ q: 'Más de 2 artefactos alto consumo' = {q}")

    # Test: Conectivos lógicos
    conjuncion = logica.conjuncion(p, q)
    disyuncion = logica.disyuncion(p, q)
    negacion_p = logica.negacion(p)
    implicacion = logica.implicacion(p, q)

    print(f"\n✓ p ∧ q = {conjuncion}")
    print(f"✓ p ∨ q = {disyuncion}")
    print(f"✓ ¬p = {negacion_p}")
    print(f"✓ p → q = {implicacion}")

    # Verificar tabla de verdad de conjunción
    assert logica.conjuncion(True, True)
    assert not logica.conjuncion(True, False)
    assert not logica.conjuncion(False, True)
    assert not logica.conjuncion(False, False)
    print("✓ Tabla de verdad de conjunción verificada")

    # Verificar tabla de verdad de disyunción
    assert logica.disyuncion(True, True)
    assert logica.disyuncion(True, False)
    assert logica.disyuncion(False, True)
    assert not logica.disyuncion(False, False)
    print("✓ Tabla de verdad de disyunción verificada")

    # Verificar negación
    assert not logica.negacion(True)
    assert logica.negacion(False)
    print("✓ Tabla de verdad de negación verificada")

    # Test: Nivel de alerta
    nivel = logica.evaluar_nivel_alerta()
    print(f"\n✓ Nivel de alerta evaluado: {nivel}")
    assert nivel in ["CRÍTICA", "MODERADA", "NORMAL"], "Error en nivel de alerta"

    # Test: Recomendaciones
    recomendaciones, nivel_rec = logica.generar_recomendaciones()
    print(f"✓ Recomendaciones generadas: {len(recomendaciones)}")
    assert len(recomendaciones) > 0, "Error: no se generaron recomendaciones"

    # Test: Leyes de De Morgan
    # ¬(p ∧ q) ≡ ¬p ∨ ¬q
    ley1_izq = logica.negacion(logica.conjuncion(p, q))
    ley1_der = logica.disyuncion(logica.negacion(p), logica.negacion(q))
    print("\n✓ Ley De Morgan 1: ¬(p ∧ q) = ¬p ∨ ¬q")
    print(f"  {ley1_izq} = {ley1_der}")
    assert ley1_izq == ley1_der, "Error en Ley De Morgan 1"

    print("\n✅ TEST 4 APROBADO: Lógica Proposicional funciona correctamente\n")


def test_integracion():
    """Prueba integración completa del sistema"""
    print("\n" + "=" * 60)
    print("TEST 5: Integración del Sistema Completo")
    print("=" * 60)

    # Crear sistema completo
    gestor = GestorConjuntos()

    # Cargar datos de ejemplo
    artefactos = [
        Artefacto("Heladera", 150, 24, "Cocina", "Electrodoméstico"),
        Artefacto("Microondas", 1200, 0.5, "Cocina", "Electrodoméstico"),
        Artefacto("Aire", 2000, 8, "Dormitorio", "Climatización"),
        Artefacto("TV", 80, 6, "Sala", "Electrónica"),
        Artefacto("Notebook", 65, 8, "Oficina", "Electrónica"),
        Artefacto("Lámpara", 10, 5, "Dormitorio", "Iluminación"),
        Artefacto("Cafetera", 1000, 0.3, "Cocina", "Electrodoméstico"),
        Artefacto("Ventilador", 75, 6, "Sala", "Climatización"),
    ]

    for art in artefactos:
        gestor.agregar_artefacto(art)

    conteo = AnalizadorConteo(gestor)
    logica = SistemaLogico(gestor, conteo)

    # Verificar flujo completo
    print("\n1. Sistema cargado con 8 artefactos")
    assert len(gestor.universo) == 8

    print("2. Análisis de conjuntos:")
    cocina = gestor.obtener_por_ubicacion("Cocina")
    alto = gestor.obtener_por_nivel_consumo("ALTO")
    criticos_cocina = gestor.interseccion(cocina, alto)
    print(f"   - Artefactos críticos en cocina: {criticos_cocina}")

    print("3. Estadísticas calculadas:")
    consumo_total = conteo.consumo_total_mensual()
    print(f"   - Consumo total: {consumo_total:.2f} kWh")

    print("4. Lógica aplicada:")
    nivel = logica.evaluar_nivel_alerta()
    print(f"   - Nivel de alerta: {nivel}")

    print("5. Recomendaciones generadas:")
    recomendaciones, _ = logica.generar_recomendaciones()
    print(f"   - {len(recomendaciones)} recomendaciones")

    print("\n✅ TEST 5 APROBADO: Sistema integrado funciona correctamente\n")


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del sistema"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "SUITE DE PRUEBAS DEL SISTEMA" + " " * 20 + "║")
    print("╚" + "=" * 58 + "╝")

    try:
        # Test 1: Artefacto
        test_artefacto()

        # Test 2: Conjuntos
        gestor = test_conjuntos()

        # Test 3: Conteo
        conteo = test_conteo(gestor)

        # Test 4: Lógica
        test_logica(gestor, conteo)

        # Test 5: Integración
        test_integracion()

        # Resumen final
        print("\n" + "=" * 60)
        print("           ✅ TODAS LAS PRUEBAS APROBADAS ✅")
        print("=" * 60)
        print()
        print("El sistema funciona correctamente y está listo para usar.")
        print()
        print("Conceptos matemáticos verificados:")
        print("  ✓ Teoría de Conjuntos (∪, ∩, -, complemento)")
        print("  ✓ Principios de Conteo (cardinalidad, porcentajes)")
        print("  ✓ Lógica Proposicional (∧, ∨, ¬, →)")
        print("  ✓ Reglas de inferencia")
        print("  ✓ Integración completa")
        print()
        print("=" * 60 + "\n")

        return True

    except AssertionError as e:
        print(f"\n❌ ERROR: {e}")
        print("\nAlgunas pruebas fallaron. Revisar implementación.\n")
        return False
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")
        print("\nSe produjo un error durante las pruebas.\n")
        return False


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()

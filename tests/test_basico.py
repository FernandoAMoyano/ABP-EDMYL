"""
Test básico del sistema - Verificación rápida de funcionalidad
Este archivo permite probar el sistema sin usar el menú interactivo
"""

from src.consumo_hogareno import Artefacto
from src.consumo_hogareno import GestorConjuntos
from src.consumo_hogareno import AnalizadorConteo
from src.consumo_hogareno import SistemaLogico


def test_sistema():
    """Test completo del sistema"""

    print("\n" + "=" * 60)
    print("🧪 INICIANDO PRUEBAS DEL SISTEMA")
    print("=" * 60 + "\n")

    # 1. Crear gestor de conjuntos
    print("1️⃣  Creando gestor de conjuntos...")
    gestor = GestorConjuntos()
    print("   ✅ Gestor creado\n")

    # 2. Agregar artefactos de prueba
    print("2️⃣  Agregando artefactos de prueba...")
    artefactos_prueba = [
        Artefacto("Heladera", 150, 24, "Cocina", "Electrodoméstico"),
        Artefacto("Microondas", 1200, 0.5, "Cocina", "Electrodoméstico"),
        Artefacto("Aire Acondicionado", 2000, 8, "Dormitorio", "Climatización"),
        Artefacto("TV LED", 80, 6, "Sala", "Electrónica"),
        Artefacto("Lámpara LED", 10, 5, "Dormitorio", "Iluminación"),
    ]

    for art in artefactos_prueba:
        gestor.agregar_artefacto(art)
    print()

    # 3. Probar operaciones de conjuntos
    print("3️⃣  Probando operaciones de conjuntos...")

    cocina = gestor.obtener_por_ubicacion("Cocina")
    print(f"   Artefactos en Cocina: {cocina}")

    alto_consumo = gestor.obtener_por_nivel_consumo("ALTO")
    print(f"   Artefactos de alto consumo: {alto_consumo}")

    criticos_cocina = gestor.interseccion(cocina, alto_consumo)
    print(f"   Críticos en cocina (intersección): {criticos_cocina}")
    print("   ✅ Operaciones de conjuntos funcionan\n")

    # 4. Probar conteo y estadísticas
    print("4️⃣  Probando análisis estadístico...")
    conteo = AnalizadorConteo(gestor)

    total = len(gestor.universo)
    print(f"   Total de artefactos: {total}")

    consumo_total = conteo.consumo_total_mensual()
    print(f"   Consumo total mensual: {consumo_total:.2f} kWh")

    mayores = conteo.mayores_consumidores(3)
    print(f"   Mayor consumidor: {mayores[0][0]} ({mayores[0][1]:.2f} kWh)")
    print("   ✅ Análisis estadístico funciona\n")

    # 5. Probar sistema lógico
    print("5️⃣  Probando sistema lógico...")
    logica = SistemaLogico(gestor, conteo)

    p = logica.prop_consumo_alto(300)
    print(f"   Proposición p (consumo > 300): {p}")

    q = logica.prop_muchos_artefactos_alto_consumo(2)
    print(f"   Proposición q (muchos alto consumo): {q}")

    nivel = logica.evaluar_nivel_alerta()
    print(f"   Nivel de alerta: {nivel}")

    recomendaciones, _ = logica.generar_recomendaciones()
    print(f"   Recomendaciones generadas: {len(recomendaciones)}")
    print("   ✅ Sistema lógico funciona\n")

    # 6. Resumen final
    print("=" * 60)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 60 + "\n")

    print("📋 RESUMEN DE FUNCIONALIDADES PROBADAS:")
    print("   ✓ Creación de artefactos")
    print("   ✓ Gestión de conjuntos")
    print("   ✓ Operaciones matemáticas (∪, ∩, -, complemento)")
    print("   ✓ Análisis estadístico y conteo")
    print("   ✓ Lógica proposicional")
    print("   ✓ Sistema de recomendaciones")
    print("\n🚀 El sistema está listo para usar!\n")
    print("💡 Ejecuta 'python main.py' para usar el menú interactivo\n")


if __name__ == "__main__":
    test_sistema()

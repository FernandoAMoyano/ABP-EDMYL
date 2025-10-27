"""
Módulo: conteo.py
Análisis estadístico y conteo de artefactos

CONCEPTOS MATEMÁTICOS APLICADOS:
- Cardinalidad de conjuntos
- Principio de inclusión-exclusión
- Porcentajes y proporciones
- Estadísticas descriptivas
"""

from typing import Dict, List, Tuple
from .conjuntos import GestorConjuntos


class AnalizadorConteo:
    """
    Realiza análisis de conteo y estadísticas sobre los artefactos
    """

    def __init__(self, gestor_conjuntos: GestorConjuntos) -> None:
        self.gestor: GestorConjuntos = gestor_conjuntos

    def contar_por_ubicacion(self) -> Dict[str, int]:
        """
        Cuenta artefactos por ubicación

        Returns:
            dict: {ubicacion: cantidad}
        """
        conteo = {}
        for ubicacion in self.gestor.obtener_todas_ubicaciones():
            conjunto = self.gestor.obtener_por_ubicacion(ubicacion)
            conteo[ubicacion] = len(conjunto)
        return conteo

    def contar_por_tipo(self) -> Dict[str, int]:
        """
        Cuenta artefactos por tipo

        Returns:
            dict: {tipo: cantidad}
        """
        conteo = {}
        for tipo in self.gestor.obtener_todos_tipos():
            conjunto = self.gestor.obtener_por_tipo(tipo)
            conteo[tipo] = len(conjunto)
        return conteo

    def contar_por_nivel_consumo(self) -> Dict[str, int]:
        """
        Cuenta artefactos por nivel de consumo

        Returns:
            dict: {nivel: cantidad}
        """
        conteo = {}
        for nivel in ["ALTO", "MEDIO", "BAJO"]:
            conjunto = self.gestor.obtener_por_nivel_consumo(nivel)
            conteo[nivel] = len(conjunto)
        return conteo

    def calcular_porcentajes_consumo(self) -> Dict[str, float]:
        """
        Calcula porcentajes por nivel de consumo

        Returns:
            dict: {nivel: porcentaje}
        """
        conteo = self.contar_por_nivel_consumo()
        total = len(self.gestor.universo)

        if total == 0:
            return {"ALTO": 0, "MEDIO": 0, "BAJO": 0}

        return {nivel: (cantidad / total) * 100 for nivel, cantidad in conteo.items()}

    def consumo_total_mensual(self) -> float:
        """
        Calcula el consumo mensual total de todos los artefactos

        Returns:
            float: Consumo total en kWh
        """
        total = 0
        for artefacto in self.gestor.artefactos_dict.values():
            total += artefacto.consumo_mensual()
        return total

    def consumo_por_ubicacion(self) -> Dict[str, float]:
        """
        Calcula consumo mensual agrupado por ubicación

        Returns:
            dict: {ubicacion: consumo_kWh}
        """
        consumo = {}
        for ubicacion in self.gestor.obtener_todas_ubicaciones():
            conjunto = self.gestor.obtener_por_ubicacion(ubicacion)
            consumo[ubicacion] = sum(
                self.gestor.obtener_artefacto(nombre).consumo_mensual()
                for nombre in conjunto
            )
        return consumo

    def consumo_por_tipo(self) -> Dict[str, float]:
        """
        Calcula consumo mensual agrupado por tipo

        Returns:
            dict: {tipo: consumo_kWh}
        """
        consumo = {}
        for tipo in self.gestor.obtener_todos_tipos():
            conjunto = self.gestor.obtener_por_tipo(tipo)
            consumo[tipo] = sum(
                self.gestor.obtener_artefacto(nombre).consumo_mensual()
                for nombre in conjunto
            )
        return consumo

    def mayores_consumidores(self, n: int = 5) -> List[Tuple[str, float]]:
        """
        Identifica los N artefactos con mayor consumo

        Args:
            n (int): Cantidad de artefactos a retornar

        Returns:
            list: Lista de tuplas (nombre, consumo_kWh)
        """
        consumos = [
            (nombre, art.consumo_mensual())
            for nombre, art in self.gestor.artefactos_dict.items()
        ]
        consumos_ordenados = sorted(consumos, key=lambda x: x[1], reverse=True)
        return consumos_ordenados[:n]

    def generar_reporte_estadistico(self) -> str:
        """
        Genera un reporte estadístico completo

        Returns:
            str: Reporte formateado
        """
        reporte = "\n" + "=" * 60 + "\n"
        reporte += "   REPORTE ESTADÍSTICO - ANÁLISIS DE CONTEO\n"
        reporte += "=" * 60 + "\n\n"

        # Cardinalidad del universo
        total = len(self.gestor.universo)
        reporte += "📊 CARDINALIDAD DEL UNIVERSO\n"
        reporte += f"   Total de artefactos: |U| = {total}\n\n"

        # Conteo por ubicación
        reporte += "📍 DISTRIBUCIÓN POR UBICACIÓN\n"
        conteo_ubi = self.contar_por_ubicacion()
        for ubicacion, cantidad in sorted(conteo_ubi.items()):
            porcentaje = (cantidad / total * 100) if total > 0 else 0
            reporte += f"   {ubicacion}: {cantidad} ({porcentaje:.1f}%)\n"
        reporte += "\n"

        # Conteo por tipo
        reporte += "🔧 DISTRIBUCIÓN POR TIPO\n"
        conteo_tipo = self.contar_por_tipo()
        for tipo, cantidad in sorted(conteo_tipo.items()):
            porcentaje = (cantidad / total * 100) if total > 0 else 0
            reporte += f"   {tipo}: {cantidad} ({porcentaje:.1f}%)\n"
        reporte += "\n"

        # Conteo por nivel de consumo
        reporte += "⚡ DISTRIBUCIÓN POR NIVEL DE CONSUMO\n"
        porcentajes = self.calcular_porcentajes_consumo()
        conteo_consumo = self.contar_por_nivel_consumo()
        for nivel in ["ALTO", "MEDIO", "BAJO"]:
            reporte += (
                f"   {nivel}: {conteo_consumo[nivel]} ({porcentajes[nivel]:.1f}%)\n"
            )
        reporte += "\n"

        # Consumo total
        consumo_total = self.consumo_total_mensual()
        reporte += "💡 CONSUMO ENERGÉTICO\n"
        reporte += f"   Consumo mensual total: {consumo_total:.2f} kWh\n"
        reporte += f"   Consumo diario promedio: {consumo_total / 30:.2f} kWh\n\n"

        # Mayores consumidores
        reporte += "🔝 TOP 5 MAYORES CONSUMIDORES\n"
        mayores = self.mayores_consumidores(5)
        for i, (nombre, consumo) in enumerate(mayores, 1):
            porcentaje = (consumo / consumo_total * 100) if consumo_total > 0 else 0
            reporte += (
                f"   {i}. {nombre.title()}: {consumo:.2f} kWh ({porcentaje:.1f}%)\n"
            )

        reporte += "\n" + "=" * 60 + "\n"

        return reporte

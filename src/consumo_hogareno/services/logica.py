"""
Módulo: logica.py
Sistema de recomendaciones usando Lógica Proposicional

CONCEPTOS MATEMÁTICOS APLICADOS:
- Proposiciones simples (p, q, r)
- Conectivos lógicos: ∧ (AND), ∨ (OR), ¬ (NOT), → (implicación)
- Tablas de verdad
- Reglas de inferencia (Modus Ponens, Modus Tollens)
"""

from typing import List, Optional, Tuple
from .conjuntos import GestorConjuntos
from .conteo import AnalizadorConteo


class SistemaLogico:
    """
    Sistema de recomendaciones basado en lógica proposicional
    """

    def __init__(
        self, gestor_conjuntos: GestorConjuntos, analizador_conteo: AnalizadorConteo
    ) -> None:
        self.gestor: GestorConjuntos = gestor_conjuntos
        self.conteo: AnalizadorConteo = analizador_conteo

    # ==================== PROPOSICIONES SIMPLES ====================

    def prop_consumo_alto(self, umbral: float = 300) -> bool:
        """
        Proposición p: "El consumo mensual es mayor a umbral kWh"

        Args:
            umbral (float): Umbral de consumo en kWh

        Returns:
            bool: True si se cumple la proposición
        """
        consumo_total = self.conteo.consumo_total_mensual()
        return consumo_total > umbral

    def prop_muchos_artefactos_alto_consumo(self, umbral: int = 2) -> bool:
        """
        Proposición q: "Hay más de N artefactos de alto consumo"

        Args:
            umbral (int): Número mínimo de artefactos

        Returns:
            bool: True si se cumple la proposición
        """
        alto_consumo = self.gestor.obtener_por_nivel_consumo("ALTO")
        return len(alto_consumo) > umbral

    def prop_ubicacion_critica(self, ubicacion: str, umbral_kwh: float = 50) -> bool:
        """
        Proposición r: "Una ubicación tiene consumo crítico"

        Args:
            ubicacion (str): Ubicación a evaluar
            umbral_kwh (float): Umbral de consumo en kWh

        Returns:
            bool: True si se cumple la proposición
        """
        consumo_ubicacion = self.conteo.consumo_por_ubicacion()
        return consumo_ubicacion.get(ubicacion, 0) > umbral_kwh

    def prop_artefactos_simultaneos_criticos(self, ubicacion: str) -> bool:
        """
        Proposición s: "En una ubicación hay múltiples artefactos de alto consumo"

        Args:
            ubicacion (str): Ubicación a evaluar

        Returns:
            bool: True si hay 2 o más artefactos de alto consumo
        """
        artefactos_ubicacion = self.gestor.obtener_por_ubicacion(ubicacion)
        alto_consumo = self.gestor.obtener_por_nivel_consumo("ALTO")
        # Intersección: artefactos de alto consumo EN esta ubicación
        criticos_en_ubicacion = artefactos_ubicacion & alto_consumo
        return len(criticos_en_ubicacion) >= 2

    # ==================== CONECTIVOS LÓGICOS ====================

    def conjuncion(self, p: bool, q: bool) -> bool:
        """
        Conjunción: p ∧ q (AND)
        Verdadero solo si ambas proposiciones son verdaderas
        """
        return p and q

    def disyuncion(self, p: bool, q: bool) -> bool:
        """
        Disyunción: p ∨ q (OR)
        Verdadero si al menos una proposición es verdadera
        """
        return p or q

    def negacion(self, p: bool) -> bool:
        """
        Negación: ¬p (NOT)
        Invierte el valor de verdad
        """
        return not p

    def implicacion(self, p: bool, q: bool) -> bool:
        """
        Implicación: p → q
        Falso solo cuando p es verdadero y q es falso
        Equivalente a: ¬p ∨ q
        """
        return (not p) or q

    # ==================== REGLAS DE INFERENCIA ====================

    def modus_ponens(self, p: bool, implicacion_pq: bool) -> Optional[bool]:
        """
        Modus Ponens: [(p → q) ∧ p] → q
        Si p implica q, y p es verdad, entonces q es verdad

        Args:
            p (bool): Premisa
            implicacion_pq (bool): p → q

        Returns:
            bool or None: Conclusión q
        """
        if p and implicacion_pq:
            return True
        return None  # No se puede concluir

    # ==================== SISTEMA DE ALERTAS ====================

    def evaluar_nivel_alerta(self) -> str:
        """
        Evalúa el nivel de alerta usando lógica proposicional

        Reglas:
        1. (p ∧ q) → CRÍTICA: Consumo alto Y muchos artefactos de alto consumo
        2. p ∨ q → MODERADA: Consumo alto O muchos artefactos de alto consumo
        3. ¬(p ∨ q) → NORMAL: Ni consumo alto ni muchos artefactos

        Returns:
            str: 'CRÍTICA', 'MODERADA' o 'NORMAL'
        """
        p = self.prop_consumo_alto(300)
        q = self.prop_muchos_artefactos_alto_consumo(2)

        # Tabla de verdad para decisiones
        if self.conjuncion(p, q):  # p ∧ q
            return "CRÍTICA"
        elif self.disyuncion(p, q):  # p ∨ q
            return "MODERADA"
        else:  # ¬(p ∨ q)
            return "NORMAL"

    def identificar_ubicaciones_criticas(self) -> List[str]:
        """
        Identifica ubicaciones con consumo crítico

        Returns:
            list: Lista de ubicaciones críticas
        """
        criticas = []
        for ubicacion in self.gestor.obtener_todas_ubicaciones():
            # Proposición compuesta: r ∨ s
            r = self.prop_ubicacion_critica(ubicacion, 50)
            s = self.prop_artefactos_simultaneos_criticos(ubicacion)

            if self.disyuncion(r, s):
                criticas.append(ubicacion)

        return criticas

    # ==================== SISTEMA DE RECOMENDACIONES ====================

    def generar_recomendaciones(self) -> Tuple[List[str], str]:
        """
        Genera recomendaciones personalizadas usando reglas lógicas

        Returns:
            tuple: (lista de recomendaciones, nivel de alerta)
        """
        recomendaciones = []

        # Evaluación de proposiciones
        p = self.prop_consumo_alto(300)
        q = self.prop_muchos_artefactos_alto_consumo(2)
        nivel_alerta = self.evaluar_nivel_alerta()

        # Regla 1: Si consumo alto → recomendar revisión general
        if p:
            recomendaciones.append(
                "⚠️  Tu consumo mensual supera los 300 kWh. "
                "Considera revisar el uso de tus artefactos."
            )

        # Regla 2: Si muchos artefactos de alto consumo → sugerir alternativas
        if q:
            recomendaciones.append(
                "🔌 Tienes varios artefactos de alto consumo. "
                "Evalúa reemplazarlos por modelos más eficientes."
            )

        # Regla 3: (p ∧ q) → Alerta crítica con acción inmediata
        if self.conjuncion(p, q):
            recomendaciones.append(
                "🚨 CRÍTICO: Consumo alto con múltiples dispositivos potentes. "
                "Acción recomendada: Evita usar varios simultáneamente."
            )

        # Regla 4: Identificar ubicaciones problemáticas
        ubicaciones_criticas = self.identificar_ubicaciones_criticas()
        if ubicaciones_criticas:
            recomendaciones.append(
                f"📍 Ubicaciones críticas detectadas: {', '.join(ubicaciones_criticas)}. "
                "Revisa el uso de artefactos en estas áreas."
            )

        # Regla 5: Analizar mayores consumidores
        mayores = self.conteo.mayores_consumidores(3)
        if mayores:
            top_consumidor = mayores[0][0]
            recomendaciones.append(
                f"💡 Tu mayor consumidor es '{top_consumidor.title()}'. "
                "Optimiza su uso para reducir costos."
            )

        # Regla 6: Si ¬p ∧ ¬q → Felicitación
        if self.negacion(p) and self.negacion(q):
            recomendaciones.append(
                "✅ ¡Excelente! Tu consumo es eficiente. "
                "Mantén estos buenos hábitos energéticos."
            )

        return recomendaciones, nivel_alerta

    def generar_reporte_logico(self) -> str:
        """
        Genera un reporte completo del análisis lógico

        Returns:
            str: Reporte formateado
        """
        reporte = "\n" + "=" * 60 + "\n"
        reporte += "   ANÁLISIS LÓGICO - SISTEMA DE RECOMENDACIONES\n"
        reporte += "=" * 60 + "\n\n"

        # Evaluación de proposiciones
        reporte += "📋 EVALUACIÓN DE PROPOSICIONES\n\n"

        p = self.prop_consumo_alto(300)
        reporte += f"   p: 'Consumo mensual > 300 kWh' = {p}\n"

        q = self.prop_muchos_artefactos_alto_consumo(2)
        reporte += f"   q: 'Más de 2 artefactos de alto consumo' = {q}\n\n"

        # Operaciones lógicas
        reporte += "🔗 OPERACIONES LÓGICAS\n\n"
        reporte += f"   p ∧ q (Conjunción) = {self.conjuncion(p, q)}\n"
        reporte += f"   p ∨ q (Disyunción) = {self.disyuncion(p, q)}\n"
        reporte += f"   ¬p (Negación de p) = {self.negacion(p)}\n"
        reporte += f"   p → q (Implicación) = {self.implicacion(p, q)}\n\n"

        # Nivel de alerta
        nivel = self.evaluar_nivel_alerta()
        emoji_nivel = {"CRÍTICA": "🚨", "MODERADA": "⚠️", "NORMAL": "✅"}
        reporte += f"🎯 NIVEL DE ALERTA: {emoji_nivel[nivel]} {nivel}\n\n"

        # Ubicaciones críticas
        ubicaciones = self.identificar_ubicaciones_criticas()
        reporte += "📍 UBICACIONES CRÍTICAS: "
        if ubicaciones:
            reporte += f"{', '.join(ubicaciones)}\n\n"
        else:
            reporte += "Ninguna\n\n"

        # Recomendaciones
        recomendaciones, _ = self.generar_recomendaciones()
        reporte += "💡 RECOMENDACIONES PERSONALIZADAS\n\n"
        for i, rec in enumerate(recomendaciones, 1):
            reporte += f"   {i}. {rec}\n\n"

        reporte += "=" * 60 + "\n"

        return reporte

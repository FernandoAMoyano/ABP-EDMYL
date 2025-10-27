"""
Módulo: conjuntos.py
Gestión de artefactos usando Teoría de Conjuntos

CONCEPTOS MATEMÁTICOS APLICADOS:
- Conjunto Universo (U): Todos los artefactos del hogar
- Subconjuntos: Clasificaciones por criterios (ubicación, tipo, consumo)
- Operaciones: Unión (∪), Intersección (∩), Diferencia (-), Complemento
- Cardinalidad: |A| = número de elementos en conjunto A
"""

from typing import Set, Dict, Optional
from ..models.artefacto import Artefacto


class GestorConjuntos:
    """
    Gestiona los artefactos como conjuntos matemáticos
    Aplica operaciones de teoría de conjuntos
    """

    def __init__(self) -> None:
        # Conjunto Universo U: Todos los artefactos
        self.universo: Set[str] = set()
        self.artefactos_dict: Dict[
            str, Artefacto
        ] = {}  # Para mantener objetos completos

    def agregar_artefacto(self, artefacto: Artefacto) -> None:
        """
        Agrega un artefacto al conjunto universo

        Args:
            artefacto (Artefacto): Objeto artefacto a agregar
        """
        nombre_normalizado = artefacto.nombre.lower().strip()
        self.universo.add(nombre_normalizado)
        self.artefactos_dict[nombre_normalizado] = artefacto
        print(f"✓ Artefacto '{artefacto.nombre}' agregado al sistema")

    def obtener_por_ubicacion(self, ubicacion: str) -> Set[str]:
        """
        Obtiene el subconjunto de artefactos por ubicación

        Args:
            ubicacion (str): Ubicación a filtrar

        Returns:
            set: Conjunto de nombres de artefactos
        """
        return {
            nombre
            for nombre in self.universo
            if self.artefactos_dict[nombre].ubicacion.lower() == ubicacion.lower()
        }

    def obtener_por_tipo(self, tipo: str) -> Set[str]:
        """
        Obtiene el subconjunto de artefactos por tipo

        Args:
            tipo (str): Tipo a filtrar

        Returns:
            set: Conjunto de nombres de artefactos
        """
        return {
            nombre
            for nombre in self.universo
            if self.artefactos_dict[nombre].tipo.lower() == tipo.lower()
        }

    def obtener_por_nivel_consumo(self, nivel: str) -> Set[str]:
        """
        Obtiene el subconjunto de artefactos por nivel de consumo

        Args:
            nivel (str): 'ALTO', 'MEDIO' o 'BAJO'

        Returns:
            set: Conjunto de nombres de artefactos
        """
        return {
            nombre
            for nombre in self.universo
            if self.artefactos_dict[nombre].nivel_consumo() == nivel.upper()
        }

    def union(self, conjunto_a: Set[str], conjunto_b: Set[str]) -> Set[str]:
        """
        Operación de Unión: A ∪ B
        Elementos que están en A o en B o en ambos

        Returns:
            set: A ∪ B
        """
        return conjunto_a | conjunto_b

    def interseccion(self, conjunto_a: Set[str], conjunto_b: Set[str]) -> Set[str]:
        """
        Operación de Intersección: A ∩ B
        Elementos que están en A y en B simultáneamente

        Returns:
            set: A ∩ B
        """
        return conjunto_a & conjunto_b

    def diferencia(self, conjunto_a: Set[str], conjunto_b: Set[str]) -> Set[str]:
        """
        Operación de Diferencia: A - B
        Elementos que están en A pero no en B

        Returns:
            set: A - B
        """
        return conjunto_a - conjunto_b

    def complemento(self, conjunto_a: Set[str]) -> Set[str]:
        """
        Complemento: U - A
        Todos los elementos del universo que no están en A

        Returns:
            set: Complemento de A
        """
        return self.universo - conjunto_a

    def cardinalidad(self, conjunto: Set[str]) -> int:
        """
        Cardinalidad: |A|
        Número de elementos en el conjunto

        Returns:
            int: |A|
        """
        return len(conjunto)

    def obtener_todas_ubicaciones(self) -> Set[str]:
        """Retorna conjunto de todas las ubicaciones únicas"""
        return {art.ubicacion for art in self.artefactos_dict.values()}

    def obtener_todos_tipos(self) -> Set[str]:
        """Retorna conjunto de todos los tipos únicos"""
        return {art.tipo for art in self.artefactos_dict.values()}

    def mostrar_conjunto(self, conjunto: Set[str], titulo: str = "Conjunto") -> None:
        """
        Muestra un conjunto de forma legible

        Args:
            conjunto (set): Conjunto a mostrar
            titulo (str): Título descriptivo
        """
        print(f"\n{titulo}:")
        print(f"Cardinalidad |A| = {len(conjunto)}")
        if conjunto:
            print(f"Elementos: {{{', '.join(sorted(conjunto))}}}")
        else:
            print("Conjunto vacío: ∅")

    def obtener_artefacto(self, nombre: str) -> Optional[Artefacto]:
        """Obtiene el objeto artefacto completo por nombre"""
        nombre_norm = nombre.lower().strip()
        return self.artefactos_dict.get(nombre_norm)

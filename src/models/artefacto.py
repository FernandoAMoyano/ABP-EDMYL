"""
Módulo: artefacto.py
Representa un artefacto eléctrico del hogar con sus características
"""

from typing import Literal


class Artefacto:
    """
    Clase que representa un artefacto eléctrico

    Atributos:
        nombre (str): Nombre del artefacto
        watts (float): Potencia en watts
        horas_dia (float): Horas de uso diario
        ubicacion (str): Ubicación en el hogar
        tipo (str): Tipo de artefacto
    """

    def __init__(
        self,
        nombre: str,
        watts: float,
        horas_dia: float,
        ubicacion: str,
        tipo: str
    ) -> None:
        self.nombre = nombre
        self.watts = watts
        self.horas_dia = horas_dia
        self.ubicacion = ubicacion
        self.tipo = tipo

    def consumo_diario(self) -> float:
        """Calcula el consumo diario en Wh (watt-hora)"""
        return self.watts * self.horas_dia

    def consumo_mensual(self) -> float:
        """Calcula el consumo mensual en kWh (kilowatt-hora)"""
        return (self.consumo_diario() * 30) / 1000

    def nivel_consumo(self) -> Literal['ALTO', 'MEDIO', 'BAJO']:
        """
        Clasifica el nivel de consumo del artefacto según su potencia

        Returns:
            Literal['ALTO', 'MEDIO', 'BAJO']: Nivel de consumo del artefacto
        """
        if self.watts > 1000:
            return "ALTO"
        elif self.watts >= 200:
            return "MEDIO"
        else:
            return "BAJO"

    def __str__(self) -> str:
        return f"{self.nombre} ({self.watts}W) - {self.ubicacion}"

    def __repr__(self) -> str:
        return self.nombre

    def info_completa(self) -> str:
        """Retorna información detallada del artefacto"""
        return f"""
            {"=" * 50}
            Artefacto: {self.nombre}
            {"=" * 50}
            Potencia:          {self.watts} W
            Uso diario:        {self.horas_dia} horas
            Ubicación:         {self.ubicacion}
            Tipo:              {self.tipo}
            Nivel de consumo:  {self.nivel_consumo()}
            Consumo diario:    {self.consumo_diario():.2f} Wh
            Consumo mensual:   {self.consumo_mensual():.2f} kWh
            {"=" * 50}
        """

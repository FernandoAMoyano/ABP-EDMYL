"""
Configuración de instalación del paquete consumo_hogareno
"""

from setuptools import setup, find_packages

setup(
    name="consumo-hogareno",
    version="1.0.0",
    author="Fernando Agustín Moyano",
    description="Sistema de Monitoreo Inteligente de Consumo Hogareño",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        # Aquí irían las dependencias externas si las hubiera
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

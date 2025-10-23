# Sistema de Monitoreo Inteligente de Consumo Hogareño

---

# Proyecto ABP - Elementos de Matemática y Lógica

**Autor:**

- Fernando Agustín Moyano

---

# Descripción del Proyecto

Sistema desarrollado en Python que permite monitorear y analizar el consumo eléctrico hogareño aplicando conceptos matemáticos de:

- **Teoría de Conjuntos**
- **Principios de Conteo**
- **Lógica Proposicional**

---

# Objetivos

### Objetivo General

Desarrollar un software que permita al usuario visualizar y controlar su consumo eléctrico, identificando áreas críticas y fomentando un uso energético responsable y eficiente.

### Objetivos Específicos

1. Clasificar artefactos por ubicación, tipo y otros parámetros mediante conjuntos
2. Utilizar lógica proposicional para definir el comportamiento del sistema y brindar recomendaciones personalizadas
3. Evaluar y categorizar los niveles de consumo registrados

---

# Conceptos Matemáticos Aplicados

### 1. Teoría de Conjuntos

#### Conjunto Universo (U)

Todos los artefactos registrados en el sistema.

#### Subconjuntos

- **Por ubicación:** Cocina, Dormitorio, Sala, etc.
- **Por tipo:** Electrodoméstico, Iluminación, Climatización, etc.
- **Por nivel de consumo:** Alto (>1000W), Medio (200-1000W), Bajo (<200W)

#### Operaciones

- **Unión (A ∪ B):** Artefactos que están en A o en B
- **Intersección (A ∩ B):** Artefactos que están en A y en B
- **Diferencia (A - B):** Artefactos que están en A pero no en B
- **Complemento (U - A):** Artefactos que NO están en A

**Ejemplo práctico:**

```
Cocina = {heladera, microondas, cafetera}
Alto_Consumo = {microondas, aire_acondicionado, plancha}

Cocina ∩ Alto_Consumo = {microondas}
→ Artefactos críticos en la cocina
```

### 2. Principios de Conteo

#### Cardinalidad

Número de elementos en un conjunto: |A|

#### Principio de Inclusión-Exclusión

|A ∪ B| = |A| + |B| - |A ∩ B|

#### Análisis Estadístico

- Conteo de artefactos por categoría
- Cálculo de porcentajes
- Identificación de mayores consumidores

**Ejemplo práctico:**

```
Total artefactos: 10
Alto consumo: 3
Porcentaje: (3/10) × 100 = 30%
```

### 3. Lógica Proposicional

#### Proposiciones Simples

- **p:** "El consumo mensual > 300 kWh"
- **q:** "Hay más de 2 artefactos de alto consumo"
- **r:** "Una ubicación tiene consumo crítico"

#### Conectivos Lógicos

- **Conjunción (∧):** p ∧ q → "Consumo alto Y múltiples artefactos"
- **Disyunción (∨):** p ∨ q → "Consumo alto O múltiples artefactos"
- **Negación (¬):** ¬p → "Consumo normal"
- **Implicación (→):** (p ∧ q) → "Emitir alerta crítica"

#### Reglas de Inferencia

**Modus Ponens:** Si (p → q) y p es verdad, entonces q es verdad

**Ejemplo práctico:**

```
Si consumo > 300 kWh Y artefactos_críticos > 2
Entonces: ALERTA CRÍTICA
```

---

# Estructura del Proyecto

```
ABP-Matemática/
│
├── 🗒️artefacto.py          # Clase Artefacto con cálculos de consumo
├── 🗒️conjuntos.py          # Gestión mediante teoría de conjuntos
├── 🗒️conteo.py             # Análisis estadístico y conteo
├── 🗒️logica.py             # Sistema de recomendaciones (lógica)
├── 🗒️main.py               # Programa principal con menú interactivo
└── 🗒️README.md             # Este archivo
```

---

# Cómo Ejecutar el Proyecto

### Requisitos

- Python 3.6 o superior
- No requiere librerías externas

### Ejecución

1. Ejecutar el programa principal:

```bash
python main.py
```

---

## Manual de Usuario

### Menú Principal

```
1️⃣  Agregar artefacto
2️⃣  Ver todos los artefactos
3️⃣  Consultas por conjuntos
4️⃣  Análisis estadístico (Conteo)
5️⃣  Sistema de recomendaciones (Lógica)
6️⃣  Reporte completo
7️⃣  Cargar datos de ejemplo
0️⃣  Salir
```

### 1. Agregar Artefacto

Permite ingresar un nuevo artefacto con:

- Nombre
- Potencia en watts (W)
- Horas de uso diario
- Ubicación
- Tipo

**Ejemplo:**

```
Nombre: Heladera
Potencia: 150 W
Horas diarias: 24
Ubicación: Cocina
Tipo: Electrodoméstico
```

### 2. Ver Artefactos

Lista todos los artefactos registrados con su información completa.

### 3. Consultas por Conjuntos

Operaciones matemáticas con los artefactos:

#### 3.1 Ver por ubicación

Filtra artefactos de una ubicación específica.

#### 3.2 Ver por tipo

Filtra artefactos de un tipo específico.

#### 3.3 Ver por nivel de consumo

Filtra por ALTO, MEDIO o BAJO consumo.

#### 3.4 Unión (A ∪ B)

Muestra artefactos que cumplen una condición U otra.

**Ejemplo:**

```
Cocina ∪ Alto_Consumo
→ Artefactos que están en cocina O tienen alto consumo
```

#### 3.5 Intersección (A ∩ B)

Muestra artefactos que cumplen ambas condiciones.

**Ejemplo:**

```
Cocina ∩ Alto_Consumo
→ Artefactos críticos en la cocina
```

#### 3.6 Diferencia (A - B)

Elementos en A que no están en B.

#### 3.7 Complemento (U - A)

Todos los artefactos excepto los de A.

# 4. Análisis Estadístico

Genera un reporte con:

- Cardinalidad del universo
- Distribución por ubicación (conteo y porcentajes)
- Distribución por tipo
- Distribución por nivel de consumo
- Consumo energético total y promedio
- Top 5 mayores consumidores

# 5. Sistema de Recomendaciones

Análisis lógico que:

- Evalúa proposiciones sobre el consumo
- Aplica operaciones lógicas
- Determina nivel de alerta (CRÍTICA, MODERADA, NORMAL)
- Identifica ubicaciones críticas
- Genera recomendaciones personalizadas

**Ejemplo de recomendación:**

```
🚨 CRÍTICO: Consumo alto con múltiples dispositivos potentes.
Acción recomendada: Evita usar varios simultáneamente.
```

---

# 6. Reporte Completo

Combina todos los análisis en un reporte único.

---

# 7. Cargar Datos de Ejemplo

Carga 10 artefactos de ejemplo para probar el sistema.

---

# Ejemplos de Uso

### Caso de Uso 1: Identificar Artefactos Críticos en Cocina

1. Cargar datos de ejemplo (opción 7)
2. Ir a "Consultas por conjuntos" (opción 3)
3. Seleccionar "Intersección" (opción 5)
4. Ver: Cocina ∩ Alto_Consumo
5. **Resultado:** Identifica artefactos que consumen mucho en la cocina

### Caso de Uso 2: Reducir Consumo

1. Ver reporte completo (opción 6)
2. Identificar TOP consumidores
3. Verificar recomendaciones del sistema lógico
4. **Resultado:** Plan de acción para reducir consumo

### Caso de Uso 3: Análisis por Ubicación

1. Ir a análisis estadístico (opción 4)
2. Ver distribución por ubicación
3. Identificar ubicación con más consumo
4. **Resultado:** Focalizar esfuerzos en esa área

---

## Vinculación con Conceptos Matemáticos

### Conjuntos → Clasificación

Los artefactos se agrupan en conjuntos según criterios, permitiendo:

- Análisis por categorías
- Operaciones matemáticas rigurosas
- Identificación de intersecciones críticas

### Conteo → Estadísticas

Los principios de conteo permiten:

- Cuantificar elementos por categoría
- Calcular porcentajes y proporciones
- Aplicar inclusión-exclusión

### Lógica → Decisiones

La lógica proposicional permite:

- Evaluar condiciones complejas
- Tomar decisiones automatizadas
- Generar recomendaciones basadas en reglas

---

## Ejemplo de Salida

### Reporte Estadístico

```
============================================================
   REPORTE ESTADÍSTICO - ANÁLISIS DE CONTEO
============================================================

📊 CARDINALIDAD DEL UNIVERSO
   Total de artefactos: |U| = 10

📍 DISTRIBUCIÓN POR UBICACIÓN
   Cocina: 3 (30.0%)
   Dormitorio: 2 (20.0%)
   Sala: 2 (20.0%)
   ...

⚡ DISTRIBUCIÓN POR NIVEL DE CONSUMO
   ALTO: 4 (40.0%)
   MEDIO: 3 (30.0%)
   BAJO: 3 (30.0%)

💡 CONSUMO ENERGÉTICO
   Consumo mensual total: 285.50 kWh
   Consumo diario promedio: 9.52 kWh

🔝 TOP 5 MAYORES CONSUMIDORES
   1. Aire acondicionado: 120.00 kWh (42.0%)
   2. Heladera: 108.00 kWh (37.8%)
   ...
```

### Sistema de Recomendaciones

```
============================================================
   ANÁLISIS LÓGICO - SISTEMA DE RECOMENDACIONES
============================================================

📋 EVALUACIÓN DE PROPOSICIONES

   p: 'Consumo mensual > 300 kWh' = False
   q: 'Más de 2 artefactos de alto consumo' = True

🔗 OPERACIONES LÓGICAS

   p ∧ q (Conjunción) = False
   p ∨ q (Disyunción) = True
   ¬p (Negación de p) = True
   p → q (Implicación) = True

🎯 NIVEL DE ALERTA: ⚠️ MODERADA

💡 RECOMENDACIONES PERSONALIZADAS

   1. 🔌 Tienes varios artefactos de alto consumo.
      Evalúa reemplazarlos por modelos más eficientes.

   2. 💡 Tu mayor consumidor es 'Aire acondicionado'.
      Optimiza su uso para reducir costos.
```

---

# Características del Código

- **Nivel:** Básico-Intermedio
- **Interfaz:** Consola interactiva
- **Modular:** Separado en 4 módulos especializados
- **Documentado:** Comentarios explicativos en cada función
- **Sin dependencias externas:** Solo Python estándar
- **Educativo:** Vincula claramente matemática con código

---

# Conceptos Aprendidos

1. **Aplicación práctica de conjuntos** a problemas reales
2. **Conteo y estadística** para análisis de datos
3. **Lógica proposicional** para toma de decisiones
4. **Programación orientada a objetos** en Python
5. **Diseño de sistemas** modulares y escalables

---

## Notas Técnicas

### Clasificación de Consumo

- **ALTO:** > 1000W (ej: microondas, aires acondicionados)
- **MEDIO:** 200-1000W (ej: televisores, ventiladores)
- **BAJO:** < 200W (ej: lámparas LED, routers)

### Cálculo de Consumo

```
Consumo diario (Wh) = Potencia (W) × Horas de uso
Consumo mensual (kWh) = (Consumo diario × 30) / 1000
```

---

# Contacto

Para consultas sobre el proyecto:

- Instituto Superior Politécnico Córdoba (ISPC)
- Tecnicatura Superior en Desarrollo de Software
- Espacio Curricular: Elementos de Matemática y Lógica

---

## Licencia

Proyecto académico desarrollado con fines educativos.

---

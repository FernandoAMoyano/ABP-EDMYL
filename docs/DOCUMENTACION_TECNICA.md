# Documentación Técnica - Vinculación Matemática-Código

---

## Índice

1. [Teoría de Conjuntos](#teoría-de-conjuntos)
2. [Principios de Conteo](#principios-de-conteo)
3. [Lógica Proposicional](#lógica-proposicional)
4. [Diagramas y Ejemplos](#diagramas-y-ejemplos)

---

# 1. Teoría de Conjuntos

### 1.1 Conceptos Matemáticos

#### Conjunto Universo (U)

**Definición matemática:**

> U = {x | x es un artefacto eléctrico registrado en el sistema}

**Implementación en código:**

```python
class GestorConjuntos:
    def __init__(self):
        self.universo = set()  # Conjunto U
```

#### Subconjuntos

**Definición matemática:**

> A ⊆ U si y solo si ∀x ∈ A → x ∈ U

**Implementación:**

```python
def obtener_por_ubicacion(self, ubicacion):
    # Retorna subconjunto de artefactos en una ubicación
    return {nombre for nombre in self.universo
            if self.artefactos_dict[nombre].ubicacion.lower() == ubicacion.lower()}
```

**Ejemplo:**

```
U = {heladera, microondas, tv, aire, lámpara}
Cocina = {heladera, microondas} ⊆ U
```

### 1.2 Operaciones de Conjuntos

#### Unión (A ∪ B)

**Definición matemática:**

> A ∪ B = {x | x ∈ A ∨ x ∈ B}

**Implementación:**

```python
def union(self, conjunto_a, conjunto_b):
    return conjunto_a | conjunto_b  # Operador | en Python
```

**Tabla de verdad:**

```
x ∈ A  |  x ∈ B  |  x ∈ A∪B
-------|---------|----------
  T    |    T    |    T
  T    |    F    |    T
  F    |    T    |    T
  F    |    F    |    F
```

**Ejemplo práctico:**

```python
Cocina = {heladera, microondas}
Alto = {microondas, aire}
Cocina ∪ Alto = {heladera, microondas, aire}
```

#### Intersección (A ∩ B)

**Definición matemática:**

> A ∩ B = {x | x ∈ A ∧ x ∈ B}

**Implementación:**

```python
def interseccion(self, conjunto_a, conjunto_b):
    return conjunto_a & conjunto_b  # Operador & en Python
```

**Tabla de verdad:**

```
x ∈ A  |  x ∈ B  |  x ∈ A∩B
-------|---------|----------
  T    |    T    |    T
  T    |    F    |    F
  F    |    T    |    F
  F    |    F    |    F
```

**Aplicación:** Identificar artefactos críticos en una ubicación específica.

#### Diferencia (A - B)

**Definición matemática:**

> A - B = {x | x ∈ A ∧ x ∉ B}

**Implementación:**

```python
def diferencia(self, conjunto_a, conjunto_b):
    return conjunto_a - conjunto_b  # Operador - en Python
```

**Ejemplo:**

```python
Todos = {heladera, microondas, tv, aire, lámpara}
Alto = {microondas, aire}
Todos - Alto = {heladera, tv, lámpara}
# Artefactos que NO son de alto consumo
```

#### Complemento (A')

**Definición matemática:**

> A' = U - A = {x | x ∈ U ∧ x ∉ A}

**Implementación:**

```python
def complemento(self, conjunto_a):
    return self.universo - conjunto_a
```

#### Cardinalidad (|A|)

**Definición matemática:**

> |A| = número de elementos en A

**Implementación:**

```python
def cardinalidad(self, conjunto):
    return len(conjunto)
```

### 1.3 Leyes de Conjuntos Aplicadas

#### Ley de De Morgan

**Matemática:**

> (A ∪ B)' = A' ∩ B'
> (A ∩ B)' = A' ∪ B'

**Verificación en código:**

```python
# Se puede verificar que se cumple con cualquier par de conjuntos
complemento_union = complemento(union(A, B))
interseccion_complementos = interseccion(complemento(A), complemento(B))
# complemento_union == interseccion_complementos debe ser True
```

#### Principio de Inclusión-Exclusión

**Matemática:**

> |A ∪ B| = |A| + |B| - |A ∩ B|

**Implementación y verificación:**

```python
def verificar_inclusion_exclusion(self, A, B):
    union_AB = self.union(A, B)
    interseccion_AB = self.interseccion(A, B)

    # Lado izquierdo: |A ∪ B|
    izquierda = len(union_AB)

    # Lado derecho: |A| + |B| - |A ∩ B|
    derecha = len(A) + len(B) - len(interseccion_AB)

    return izquierda == derecha  # Debe ser True
```

**Aplicación en el sistema:**

```python
# En el menú, al mostrar operación de unión:
print(f"Verificación: |A ∪ B| = |A| + |B| - |A ∩ B|")
print(f"   {len(union)} = {len(cocina)} + {len(alto)} - {len(cocina & alto)}")
```

---

# 2. Principios de Conteo

### 2.1 Cardinalidad y Conteo

**Definición matemática:**

> Para conjuntos finitos A₁, A₂, ..., Aₙ disjuntos dos a dos:
> |A₁ ∪ A₂ ∪ ... ∪ Aₙ| = |A₁| + |A₂| + ... + |Aₙ|

**Implementación:**

```python
def contar_por_ubicacion(self):
    conteo = {}
    for ubicacion in self.gestor.obtener_todas_ubicaciones():
        conjunto = self.gestor.obtener_por_ubicacion(ubicacion)
        conteo[ubicacion] = len(conjunto)  # Cardinalidad |A|
    return conteo
```

### 2.2 Porcentajes y Proporciones

**Matemática:**

> Porcentaje de A en U = (|A| / |U|) × 100

**Implementación:**

```python
def calcular_porcentajes_consumo(self):
    conteo = self.contar_por_nivel_consumo()
    total = len(self.gestor.universo)

    if total == 0:
        return {'ALTO': 0, 'MEDIO': 0, 'BAJO': 0}

    return {
        nivel: (cantidad / total) * 100
        for nivel, cantidad in conteo.items()
    }
```

**Ejemplo:**

```
Total artefactos: 10
Alto consumo: 3
Porcentaje = (3/10) × 100 = 30%
```

### 2.3 Producto Cartesiano (Implícito)

**Concepto:**
Cada artefacto es una tupla (nombre, watts, horas, ubicación, tipo), representando un punto en el espacio cartesiano:

> Artefactos ⊆ Nombres × ℝ⁺ × [0,24] × Ubicaciones × Tipos

**En código:**

```python
class Artefacto:
    def __init__(self, nombre, watts, horas_dia, ubicacion, tipo):
        # Representa elemento del producto cartesiano
        self.nombre = nombre        # ∈ Nombres
        self.watts = watts          # ∈ ℝ⁺
        self.horas_dia = horas_dia  # ∈ [0, 24]
        self.ubicacion = ubicacion  # ∈ Ubicaciones
        self.tipo = tipo            # ∈ Tipos
```

### 2.4 Estadísticas Descriptivas

**Suma de consumos:**

```python
def consumo_total_mensual(self):
    # Σ(consumo_i) para i en U
    total = 0
    for artefacto in self.gestor.artefactos_dict.values():
        total += artefacto.consumo_mensual()
    return total
```

**Promedio:**

```python
# Consumo promedio = (Σ consumos) / |U|
promedio = consumo_total / len(universo)
```

---

# 3. Lógica Proposicional

### 3.1 Proposiciones

**Definición:**

> Una proposición es una declaración que puede ser verdadera o falsa, pero no ambas.

#### Proposiciones del Sistema

**p: "El consumo mensual es mayor a 300 kWh"**

```python
def prop_consumo_alto(self, umbral=300):
    consumo_total = self.conteo.consumo_total_mensual()
    return consumo_total > umbral  # Retorna bool (True/False)
```

**q: "Hay más de 2 artefactos de alto consumo"**

```python
def prop_muchos_artefactos_alto_consumo(self, umbral=2):
    alto_consumo = self.gestor.obtener_por_nivel_consumo('ALTO')
    return len(alto_consumo) > umbral
```

### 3.2 Conectivos Lógicos

#### Conjunción (∧) - AND

**Definición matemática:**

> p ∧ q es verdadero si y solo si p es verdadero Y q es verdadero

**Tabla de verdad:**

```
p  |  q  |  p∧q
---|-----|-----
T  |  T  |  T
T  |  F  |  F
F  |  T  |  F
F  |  F  |  F
```

**Implementación:**

```python
def conjuncion(self, p, q):
    return p and q  # Operador 'and' de Python
```

**Aplicación en el sistema:**

```python
# Si consumo alto Y muchos artefactos críticos → Alerta CRÍTICA
if self.conjuncion(p, q):
    return 'CRÍTICA'
```

#### Disyunción (∨) - OR

**Definición matemática:**

> p ∨ q es verdadero si p es verdadero O q es verdadero O ambos

**Tabla de verdad:**

```
p  |  q  |  p∨q
---|-----|-----
T  |  T  |  T
T  |  F  |  T
F  |  T  |  T
F  |  F  |  F
```

**Implementación:**

```python
def disyuncion(self, p, q):
    return p or q  # Operador 'or' de Python
```

**Aplicación:**

```python
# Si consumo alto O muchos artefactos → Alerta MODERADA
elif self.disyuncion(p, q):
    return 'MODERADA'
```

#### Negación (¬) - NOT

**Definición matemática:**

> ¬p es verdadero si y solo si p es falso

**Tabla de verdad:**

```
p  |  ¬p
---|----
T  |  F
F  |  T
```

**Implementación:**

```python
def negacion(self, p):
    return not p  # Operador 'not' de Python
```

#### Implicación (→)

**Definición matemática:**

> p → q es falso solo cuando p es verdadero y q es falso

**Tabla de verdad:**

```
p  |  q  |  p→q
---|-----|-----
T  |  T  |  T
T  |  F  |  F
F  |  T  |  T
F  |  F  |  T
```

**Equivalencia:**

> p → q ≡ ¬p ∨ q

**Implementación:**

```python
def implicacion(self, p, q):
    return (not p) or q  # ¬p ∨ q
```

### 3.3 Reglas de Inferencia

#### Modus Ponens

**Definición matemática:**

> Si p → q es verdadero y p es verdadero, entonces q es verdadero
> Forma: [(p → q) ∧ p] → q

**Implementación:**

```python
def modus_ponens(self, p, implicacion_pq):
    """
    Si p es verdad y (p → q) es verdad, entonces q es verdad
    """
    if p and implicacion_pq:
        return True
    return None  # No se puede concluir
```

**Aplicación en recomendaciones:**

```python
# Premisa: Si consumo > 300 kWh → recomendar revisión
# Si consumo > 300 kWh (p es verdad)
# Entonces: recomendar revisión (q es verdad)

if self.modus_ponens(p, True):
    recomendaciones.append("Revisa tu consumo...")
```

#### Modus Tollens (implícito)

**Definición:**

> Si p → q es verdadero y q es falso, entonces p es falso
> Forma: [(p → q) ∧ ¬q] → ¬p

**Aplicación:**

```python
# Si ¬p ∧ ¬q → felicitación
if self.negacion(p) and self.negacion(q):
    recomendaciones.append("¡Excelente consumo!")
```

### 3.4 Leyes Lógicas Aplicadas

#### Ley de De Morgan para Lógica

**Matemática:**

> ¬(p ∧ q) ≡ ¬p ∨ ¬q
> ¬(p ∨ q) ≡ ¬p ∧ ¬q

**Aplicación en código:**

```python
# Verificar si NO hay alerta
# ¬(consumo_alto ∨ muchos_criticos)
# = ¬consumo_alto ∧ ¬muchos_criticos

sin_alerta = not (p or q)
# Equivalente a:
sin_alerta = (not p) and (not q)
```

---

# 4. Diagramas y Ejemplos

### 4.1 Diagrama de Venn - Ejemplo Real

```
        Universo U (Todos los artefactos)
    ┌────────────────────────────────────────┐
    │                                        │
    │    ┌──────────┐      ┌──────────┐     │
    │    │  Cocina  │      │   Alto   │     │
    │    │          │      │ Consumo  │     │
    │    │  ┌───────┼──────┤          │     │
    │    │  │Micro- │      │          │     │
    │    │  │ondas  │      │          │     │
    │    │  └───────┼──────┤          │     │
    │    │          │      │          │     │
    │    │ Heladera │      │   Aire   │     │
    │    │          │      │          │     │
    │    └──────────┘      └──────────┘     │
    │                                        │
    │      TV       Lámpara    Router        │
    │                                        │
    └────────────────────────────────────────┘

Cocina ∩ Alto = {Microondas}  ← Crítico!
```

### 4.2 Tabla de Decisiones (Lógica)

```
p: Consumo > 300  |  q: Muchos críticos  |  Resultado
------------------|----------------------|-------------
      True        |         True         |  CRÍTICA
      True        |         False        |  MODERADA
      False       |         True         |  MODERADA
      False       |         False        |  NORMAL
```

**Implementación:**

```python
def evaluar_nivel_alerta(self):
    p = self.prop_consumo_alto(300)
    q = self.prop_muchos_artefactos_alto_consumo(2)

    if self.conjuncion(p, q):      # Fila 1
        return 'CRÍTICA'
    elif self.disyuncion(p, q):     # Filas 2 y 3
        return 'MODERADA'
    else:                            # Fila 4
        return 'NORMAL'
```

### 4.3 Árbol de Decisión

```
                    Inicio
                      |
            ¿Consumo > 300 kWh?
              /              \
            SÍ               NO
            /                  \
    ¿>2 críticos?          ¿>2 críticos?
      /      \               /       \
    SÍ       NO             SÍ       NO
    |         |              |        |
 CRÍTICA  MODERADA      MODERADA  NORMAL
```

---

# 5. Casos de Prueba Matemáticos

### Test 1: Verificar Inclusión-Exclusión

```python
def test_inclusion_exclusion():
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    union = A | B          # {1, 2, 3, 4, 5, 6}
    interseccion = A & B   # {3, 4}

    # |A ∪ B| = |A| + |B| - |A ∩ B|
    assert len(union) == len(A) + len(B) - len(interseccion)
    # 6 = 4 + 4 - 2  ✓
```

### Test 2: Verificar De Morgan (Conjuntos)

```python
def test_de_morgan_conjuntos():
    U = {1, 2, 3, 4, 5}
    A = {1, 2}
    B = {2, 3}

    # (A ∪ B)' = A' ∩ B'
    izq = U - (A | B)
    der = (U - A) & (U - B)

    assert izq == der  # {4, 5} = {4, 5}  ✓
```

### Test 3: Verificar Tabla de Verdad

```python
def test_tabla_verdad_and():
    casos = [
        (True, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, False)
    ]

    for p, q, esperado in casos:
        resultado = p and q
        assert resultado == esperado  ✓
```

---

# 6. Complejidad y Rendimiento

### Operaciones de Conjuntos (Python sets)

- **Agregar elemento:** O(1) promedio
- **Verificar pertenencia:** O(1) promedio
- **Unión:** O(len(A) + len(B))
- **Intersección:** O(min(len(A), len(B)))
- **Diferencia:** O(len(A))

### Iteraciones

```python
# Conteo por ubicación: O(|U| × k)
# donde k = número de ubicaciones únicas
def contar_por_ubicacion(self):
    for ubicacion in ubicaciones:  # k iteraciones
        for artefacto in universo:  # |U| iteraciones
            # verificación...
```

**Optimización aplicada:**

```python
# Usando comprensión de conjuntos: O(|U|)
{nombre for nombre in self.universo
 if condicion(nombre)}
```

---

# 7. Extensiones Matemáticas Posibles

### 7.1 Relaciones y Funciones

```python
# Función de consumo: f: Artefactos → ℝ⁺
def consumo(artefacto):
    return artefacto.watts * artefacto.horas_dia
```

### 7.2 Relaciones de Orden

```python
# Orden parcial por consumo
# a ≤ b si consumo(a) ≤ consumo(b)
artefactos_ordenados = sorted(
    artefactos,
    key=lambda a: a.consumo_mensual()
)
```

### 7.3 Grafos (futuro)

```python
# Nodo: Artefacto
# Arista: Uso simultáneo
# Útil para detectar picos de consumo
```

---

## 8. Conclusión

Este sistema demuestra cómo conceptos matemáticos abstractos se convierten en herramientas prácticas para resolver problemas reales:

- **Conjuntos** → Clasificación y filtrado
- **Conteo** → Análisis estadístico
- **Lógica** → Toma de decisiones automatizada

La matemática no es solo teoría, ¡es código funcional! 🚀

---

**Documento preparado para el ABP**
**Elementos de Matemática y Lógica - ISPC**

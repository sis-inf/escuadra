# Herramienta: Calculadora de Subredes IP/CIDR

## Descripción

La calculadora de subredes permite obtener información de una red IPv4 a partir de una dirección IP y un prefijo CIDR.

La herramienta calcula automáticamente:

- Dirección de red.
- Dirección de broadcast.
- Máscara de subred.
- Primer host disponible.
- Último host disponible.
- Total de hosts disponibles.

Esta funcionalidad facilita el análisis y planificación de redes IP.

---

## Conceptos clave

### Dirección IP

Es el identificador de un dispositivo dentro de una red.

Ejemplo:

```
192.168.1.10
```

---

### Prefijo CIDR

El prefijo CIDR indica cuántos bits pertenecen a la red.

Ejemplo:

```
/24
```

equivale a la máscara:

```
255.255.255.0
```

---

### Dirección de red

Es la primera dirección del bloque y representa la subred completa.

---

### Dirección de broadcast

Es la última dirección del bloque y permite enviar información a todos los dispositivos de la red.

---

### Hosts disponibles

Son las direcciones IP que pueden asignarse a dispositivos dentro de la subred.

---

## Ejemplo de cálculo

### Enunciado

Calcular la información de la red para la dirección IP:

```
192.168.1.50/24
```

---

### Datos

- Dirección IP: `192.168.1.50`
- Prefijo CIDR: `/24`

---

### Desarrollo

#### 1. Determinar la máscara

El prefijo `/24` corresponde a la máscara:

```
255.255.255.0
```

---

#### 2. Calcular la dirección de red

La dirección pertenece a la red:

```
192.168.1.0
```

---

#### 3. Calcular la dirección de broadcast

El último valor del bloque es:

```
192.168.1.255
```

---

#### 4. Determinar el primer host

El primer host disponible es:

```
192.168.1.1
```

---

#### 5. Determinar el último host

El último host disponible es:

```
192.168.1.254
```

---

#### 6. Calcular la cantidad de hosts disponibles

Una red `/24` posee:

```
254 hosts disponibles
```

---

## Resultado

| Campo | Valor |
|--------|-------|
| Red | `192.168.1.0` |
| Broadcast | `192.168.1.255` |
| Máscara | `255.255.255.0` |
| Primer host | `192.168.1.1` |
| Último host | `192.168.1.254` |
| Total de hosts | `254` |

---

## Uso en el sistema

La herramienta recibe una dirección IP y un prefijo CIDR, realiza los cálculos correspondientes y devuelve la información de la subred en formato de texto.

```python
from escuadra.modulos.sistemas.herramienta_calculadora_subred import (
    herramienta_calculadora_subred,
)

resultado = herramienta_calculadora_subred(
    "192.168.1.50",
    "24",
)

print(resultado)
```

Salida esperada:

```text
RED: 192.168.1.0
BROADCAST: 192.168.1.255
MÁSCARA: 255.255.255.0
PRIMER HOST: 192.168.1.1
ÚLTIMO HOST: 192.168.1.254
TOTAL HOSTS: 254
```

---

## Validaciones

La herramienta valida que:

- El prefijo CIDR sea un número entero.
- El prefijo esté entre 0 y 32.
- La dirección IP tenga un formato válido.

Si alguna validación falla, la herramienta devuelve un mensaje de error indicando la causa.
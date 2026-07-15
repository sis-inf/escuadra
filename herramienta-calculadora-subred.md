# 🖥️ Calculadora de Subredes IP/CIDR

Esta herramienta permite calcular la **dirección de red**, el **rango de hosts disponibles**, la **dirección de broadcast** y el **número total de hosts** para una dirección IP dada con su máscara CIDR.

---

## 🎯 ¿Qué hace la calculadora de subredes?

La calculadora de subredes permite:

- **Calcular la dirección de red** a partir de una IP y su máscara.
- **Determinar el rango de hosts** válidos en la subred.
- **Calcular la dirección de broadcast**.
- **Obtener el número total de hosts** disponibles.

---

## 📋 Fórmulas utilizadas

### Dirección de red

Se obtiene aplicando la **máscara de subred** a la dirección IP mediante una operación **AND** binaria.
Red = IP AND Máscara

text

### Dirección de broadcast

Se obtiene aplicando la **máscara de subred invertida** a la dirección IP mediante una operación **OR** binaria.
Broadcast = IP OR (~Máscara)

text

### Rango de hosts

El rango de hosts va desde **Red + 1** hasta **Broadcast - 1**.

---

## 📝 Ejemplo completo

### Datos de entrada

| Parámetro | Valor |
|-----------|-------|
| Dirección IP | `192.168.1.0` |
| Máscara CIDR | `/24` |

### Cálculo de la máscara

- **Máscara de subred:** `255.255.255.0`
- **Wildcard (máscara invertida):** `0.0.0.255`

### Dirección de red
Red = 192.168.1.0 AND 255.255.255.0 = 192.168.1.0

text

### Dirección de broadcast
Broadcast = 192.168.1.0 OR 0.0.0.255 = 192.168.1.255

text

### Rango de hosts disponibles
192.168.1.1 → 192.168.1.254

text

### Número total de hosts
2^(32 - 24) - 2 = 254 hosts

text

### Resultados

| Parámetro | Valor |
|-----------|-------|
| **Dirección de red** | `192.168.1.0` |
| **Primer host** | `192.168.1.1` |
| **Último host** | `192.168.1.254` |
| **Dirección de broadcast** | `192.168.1.255` |
| **Número de hosts** | `254` |

---

## 📋 Otro ejemplo: `/16`

### Datos de entrada

| Parámetro | Valor |
|-----------|-------|
| Dirección IP | `10.0.0.0` |
| Máscara CIDR | `/16` |

### Resultados

| Parámetro | Valor |
|-----------|-------|
| **Dirección de red** | `10.0.0.0` |
| **Primer host** | `10.0.0.1` |
| **Último host** | `10.0.255.254` |
| **Dirección de broadcast** | `10.0.255.255` |
| **Número de hosts** | `65,534` |

---

## 🛠️ Solución de problemas

| Problema | Solución |
|----------|----------|
| **El resultado no coincide** | Verificar que la máscara CIDR sea correcta (ej. `/24` = `255.255.255.0`) |
| **Error en el cálculo** | Asegurarse de que la dirección IP y la máscara estén en el mismo formato |

---

## 📚 Referencias

- [Calculadora de subredes IPv4](https://es.wikipedia.org/wiki/Subred)
- [Notación CIDR](https://es.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
- [Guía de redes](https://es.wikipedia.org/wiki/Direcci%C3%B3n_IP)

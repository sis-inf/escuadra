# ⚙️ Perfiles de Configuración Guardables

Esta guía explica cómo utilizar los **perfiles de configuración** en Escuadra, una funcionalidad que permite guardar y cargar diferentes conjuntos de configuraciones según las necesidades del usuario.

---

## 🎯 ¿Qué son los perfiles de configuración?

Los perfiles de configuración son **conjuntos guardados de preferencias** que permiten cambiar rápidamente entre diferentes configuraciones de la aplicación. Esto es útil para:

- **Alternar entre entornos**: trabajo, estudio, presentación, etc.
- **Compartir configuraciones**: entre diferentes usuarios o equipos.
- **Personalización**: adaptar la interfaz y el comportamiento según la tarea.

---

## 📋 Ejemplos de perfiles

### Perfil "Proyector"

Configuración ideal para **presentaciones en pantalla grande**:

| Configuración | Valor |
|---------------|-------|
| **Tema** | Claro |
| **Tamaño de fuente** | 18 pt |
| **Modo** | Presentación |
| **Barra de herramientas** | Visible |
| **Ayudas visuales** | Habilitadas |

### Perfil "Estudio Nocturno"

Configuración ideal para **sesiones de estudio prolongadas en ambientes oscuros**:

| Configuración | Valor |
|---------------|-------|
| **Tema** | Oscuro |
| **Tamaño de fuente** | 14 pt |
| **Modo** | Enfoque |
| **Barra de herramientas** | Ocultar automáticamente |
| **Ayudas visuales** | Reducidas |

---

## 🚀 Cómo guardar un perfil

1. Abrí Escuadra y configurá la aplicación según tus preferencias.
2. Hacé clic en el menú **"Configuración"** > **"Guardar perfil"**.
3. Ingresá un nombre para el perfil (ej. *"Proyector"*).
4. El perfil se guarda automáticamente.

---

## 📂 Cómo cargar un perfil

1. Abrí Escuadra.
2. Hacé clic en el menú **"Configuración"** > **"Cargar perfil"**.
3. Seleccioná el perfil guardado (ej. *"Estudio Nocturno"*).
4. La aplicación se actualiza con la configuración seleccionada.

---

## 🗑️ Cómo eliminar un perfil

1. Abrí Escuadra.
2. Hacé clic en el menú **"Configuración"** > **"Administrar perfiles"**.
3. Seleccioná el perfil que deseás eliminar.
4. Presioná **"Eliminar"**.

---

## 📁 Ubicación de los perfiles

Los perfiles se guardan en el directorio de configuración del usuario:

| Sistema operativo | Ruta |
|-------------------|------|
| **Windows** | `%APPDATA%/Escuadra/perfiles/` |
| **Linux** | `~/.config/escuadra/perfiles/` |
| **macOS** | `~/Library/Application Support/Escuadra/perfiles/` |

---

## 🛠️ Solución de problemas

| Problema | Solución |
|----------|----------|
| **No se guarda el perfil** | Verificar permisos de escritura en el directorio de configuración |
| **El perfil no aparece** | Asegurarse de que el archivo no esté corrupto o en una ubicación incorrecta |
| **Configuración no se aplica** | Reiniciar la aplicación después de cargar el perfil |

---

## 📚 Referencias

- [Documentación de configuración de Escuadra](configuracion.md)
- [Guía de personalización de la interfaz](ui-tema-oscuro.md)

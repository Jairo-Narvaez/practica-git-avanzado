# 🧮 Calculadora en Python — Práctica de Git Avanzado

Proyecto simple de calculadora con operaciones básicas, usado 
para practicar comandos avanzados de Git.

## ⚙️ Funcionalidades
- Sumar
- Restar
- Multiplicar
-dividir
-potencia
-raiz cuadrada

## 📝 Cómo ejecutar
```
python calculadora.py
```

---

## 📚 Teoría — Comandos que vas a usar

### git commit --amend
Modifica el ÚLTIMO commit que hiciste (cambia su mensaje y/o 
agrega archivos que olvidaste). No crea un commit nuevo, corrige 
el anterior.
```
git commit --amend -m "nuevo mensaje"
```

### git reset
Deshace commits. `HEAD~1` significa "un commit atrás del actual" 
(`HEAD~2` serían dos atrás, etc.)

Tiene 3 tipos:
- `--soft`: deshace el commit, pero tus cambios siguen listos 
  para volver a commitear
- `--mixed` (el que se usa si no escribes nada): deshace el 
  commit y el "add", los cambios quedan en tus archivos sin preparar
- `--hard`: borra TODO, incluso los cambios en tus archivos 
  (¡cuidado, esto no se puede deshacer!)

```
git reset --soft HEAD~1
```

---

## 🎯 Tu tarea

### Paso 1 — Configurar tu identidad
```
git config user.name "Tu Nombre"
git config user.email "tu-correo"
```

### Paso 2 — Explorar el historial
```
git log --oneline
```
Verás algo como:
```
a1b2c3d agrego cosas
cbf1618 arreglo
fd78525 agrego funcion
e6375a2 primer commit
```

### Paso 3 — Corregir el ÚLTIMO commit con amend
El mensaje "agrego cosas" no sigue el formato de conventional 
commits. Corrígelo:
```
git commit --amend -m "docs: agregar instrucciones del proyecto"
```
Verifica con `git log --oneline` — el mensaje del último commit 
ya cambió.

### Paso 4 — Practicar reset
Deshaz el commit que acabas de corregir, usando `--soft`:
```
git reset --soft HEAD~1
```
Ejecuta `git log --oneline` — notarás que ese commit YA NO 
aparece. Ejecuta `git status` — verás que los cambios siguen 
ahí, listos para commitear de nuevo:
```
git commit -m "docs: agregar instrucciones del proyecto"
```

### Paso 5 — Nuevos commits (conventional commits)
Agrega al menos 2 mejoras al proyecto. Escribe TÚ MISMO el 
mensaje, siguiendo el formato:
- `feat:` para funcionalidad nueva
- `docs:` para cambios en documentación
- `fix:` para corregir un error

### Paso 6 — Subir a tu repositorio
```
git push -u origin main
```
### Investigación adicional
Ejecuta git reflog. En tu README.md, en una sección 
"Investigación adicional", explica en 2-3 líneas qué información 
muestra este comando.

# git reflog.
Muestra el historial de movimientos de la referencia HEAD en tu repositorio. Es decir, te enseña todos los cambios de posición que ha tenido tu rama actual: commits, resets, merges, rebases, checkouts, etc.

## ✅ Entrega
Link de tu repositorio (fork) + pantallazo de "git log --oneline"


## 📌 Semantic Versioning (SemVer)

**Semantic Versioning (SemVer)** es un sistema de numeración de versiones que sigue el formato:


### 🔢 Estructura
- **MAJOR (X):** cambios incompatibles en la API → `2.4.1` → `3.0.0`
- **MINOR (Y):** nuevas funcionalidades compatibles → `2.4.1` → `2.5.0`
- **PATCH (Z):** correcciones de errores compatibles → `2.4.1` → `2.4.2`

### 🏷️ Etiquetas adicionales
- **Pre-release:** `1.0.0-beta`, `2.0.0-rc.1`
- **Metadata de compilación:** `1.0.0+build.123`

### 🎯 Ventajas
- Claridad en el impacto de los cambios  
- Compatibilidad entre dependencias  
- Estandarización en proyectos open source  
- Mejor gestión de versiones y librerías  

### 📊 Ejemplo
| Versión | Cambio realizado | Compatibilidad |
|---------|-----------------|----------------|
| `1.2.3` → `1.2.4` | Corrección de bug | Compatible |
| `1.2.3` → `1.3.0` | Nueva función | Compatible |
| `1.2.3` → `2.0.0` | Cambio en API | Incompatible |

---

## Lista de comandos con git stash
Los comandos de git stash sirven para guardar, listar, aplicar y administrar cambios temporales 
en el repositorio. Es como tener un `cajon` donde puedes meter tus modificaciones sin tener que hacer un commit
y luego recuperarlas cuando quieras.

## Lista de comandos
- **git stash** Sirve para guardar los cambios sin tener que hacer un commit y limpia el direcctorio
- **git stash save "Mensaje"** Sirve para guardar los cambios y agrega un mensaje.
- **git stash list** Muestra todos los stashes guardados
- **git stash show stash@{n}** Muestra los cambios aplicados a un stash especifico.
- **git stash apply stash@{n}** Aplica un stash especifico sin necesidad de eliminarlo de la lista
- **git stash pop stash@{n}** Aplica un stash y lo elimina de la lista
- **git stash drop stash@{n}** Elimina un stash sin aplicarlo
- **git stash clear** Elimina todos los stashes guardados
- **git stash branch nombre-rama stash@{n}** Crea una rama nueva con el contenido del stash

En resumen los comandos git stash sirven para pausar o reanudar el trabajo sin necesidad de ensuciar
el historial de commits.

## Usos del comando git tag
- **git tag** Se usa para crear etiquetas en el historial de commits de git.
Las etiquetas son como marcadores que señalan un commit importante, normalmente para 
identificar versiones de lanzamiento.
- git tag
- git show V1.0.0 Ver detalles de una etiqueta.
- git tag v1.1.0 mensaje123 crea etiqueta en un commit especifico
- git push origin v1.0.0 o git push origin --tags Envia etiquetas al remoto
- git tag -d v1.0.0 Eliminar etiqueta

En resumen git tag sirve para marcar commits importantes, normalmente versiones 
y facilita el control de lanzamiento de proyectos.
 
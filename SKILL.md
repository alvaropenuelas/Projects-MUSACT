---
name: modpack
description: Flujo de trabajo para desarrollar, diagnosticar y validar Crusader’s Chronicle, un modpack RPG de Minecraft 1.20.1 con Forge, KubeJS, datapacks, recursos y mods propios.
when_to_use: Úsalo para tareas del modpack: errores de carga, scripts KubeJS, datapacks, recursos, mods propios, JAR, compilación, pruebas en juego y despliegue controlado.
---

# Crusader’s Chronicle

## Objetivo
Ayudar con tareas concretas del modpack sin cargar información innecesaria.

## Comunicación
- Responde en español, breve y directo.
- No repitas el encargo ni decisiones ya aprobadas.
- Resume cambios, pruebas, bloqueos y siguiente paso.
- Conserva identificadores, comandos y términos técnicos.
- Amplía la explicación solo si se solicita o existe un riesgo importante.

## Flujo de trabajo
1. Identifica la tarea y los archivos relevantes.
2. Consulta `docs/ESTADO.md`, `docs/DECISIONES.md` y `docs/PROYECTO.md` solo si aportan información necesaria.
3. Investiga evidencia real: logs, configuración, scripts, recursos y código.
4. Propón una corrección mínima antes de implementar cambios amplios.
5. Espera aprobación para implementar, compilar o desplegar.
6. Valida el resultado y actualiza `docs/ESTADO.md` solo al cerrar un bloque.

## Contexto del proyecto
- La instancia está en `./instancia`.
- Las fuentes, cuando existan, están en `./fuentes`.
- El trabajo temporal va en `./trabajo`.
- El encargo activo está en `docs/encargos/`.
- El historial está en `docs/historial/`.

No leas todo el historial ni descompiles todos los JAR. Prioriza búsquedas dirigidas y archivos concretos.

## JAR y código
Consulta `references/jares-y-descompilacion.md` antes de inspeccionar, extraer o descompilar JAR.

- Prioriza fuentes originales.
- Si solo hay JAR, descompila solo lo necesario.
- Separa código original de código reconstruido.
- Registra el JAR de origen, versión y ruta.
- No asumas que el código decompilado puede recompilarse directamente.
- Comprueba licencias antes de reutilizar o distribuir código.

## Compilación y pruebas
Consulta `references/compilacion-y-pruebas.md` antes de compilar, desplegar o validar.

- Usa el Gradle Wrapper existente.
- Registra comando, resultado y artefacto.
- La compilación no prueba el comportamiento en juego.
- Separa versión entregada, compilada e instalada.
- No declares pruebas o entregables inexistentes.

## Seguridad
Consulta `references/seguridad-y-despliegue.md` antes de modificar la instancia, mundos, JAR o publicar cambios.

- No modifiques la instancia activa sin aprobación.
- No borres progreso ni reemplaces carpetas completas.
- No hagas commits, push ni publicaciones sin permiso.
- No leas ni muestres secretos.
- Respeta cambios del usuario.

## Estados
Usa estos estados en `docs/ESTADO.md`:
`pendiente`, `diagnóstico`, `implementado sin validar`, `compilado sin prueba en juego`, `validado (indicar quién y cómo)`, `bloqueado`, `sustituido`.
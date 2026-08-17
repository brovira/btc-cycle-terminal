# Ingesta local de transcripts

**Por qué esto no corre en GitHub Actions.** YouTube bloquea las IPs de datacenter de los
runners. Comprobado el 17-ago-2026 en los dos canales:

```
ERROR: [youtube] Sign in to confirm you're not a bot.
       Use --cookies-from-browser or --cookies for the authentication.
```

No es yt-dlp desactualizado ni los `player_client` caducados: es **la IP**. Desde una conexión
doméstica funciona sin fricción. Por eso esta ingesta se ejecuta en tu máquina y sube el
resultado al repo.

`ingest-transcripts.yml` se queda en GitHub **sin cron**, solo como disparador manual.

---

## Instalación

### 1. Requisitos

```bash
python3 -m pip install --upgrade yt-dlp
```

Necesitas además un clon del repo con permiso de push y `git` autenticado (SSH o token en el
keychain). El script hace `pull` y `push` sobre `main`.

### 2. Prueba a mano

```bash
cd /ruta/a/btc-cycle-terminal
./ingesta/local/ingesta_local.sh
```

Debe terminar con `─── fin OK ───`. Si sale `NO PUDE LEER`, el problema es de red o de yt-dlp,
no del repo: el mensaje literal de YouTube aparece en la misma línea.

### 3. Recuperar el hueco de julio-agosto

La ingesta normal solo mira 10 días atrás, así que **los vídeos del 21-jul al 7-ago no vuelven
solos**. Una pasada única para recuperarlos:

```bash
./ingesta/local/ingesta_local.sh 20260721
```

Tarda bastante más (baja subtítulos de cada vídeo del periodo) y es normal.

### 4. Programarlo

**macOS · launchd** — copia el plist y cárgalo:

```bash
cp ingesta/local/com.brovira.btc-ingesta.plist ~/Library/LaunchAgents/
# edita la ruta del repo dentro del plist ANTES de cargarlo
launchctl load  ~/Library/LaunchAgents/com.brovira.btc-ingesta.plist
launchctl start com.brovira.btc-ingesta          # probar ya
```

Con `StartCalendarInterval`, si el portátil está dormido a la hora prevista, launchd lanza el
trabajo **en cuanto despierta**. Es justo lo que queremos para una máquina que no está siempre
encendida — y la razón de elegir launchd antes que `cron` en macOS, que se saltaría el turno.

Para quitarlo:

```bash
launchctl unload ~/Library/LaunchAgents/com.brovira.btc-ingesta.plist
```

**Linux · cron** — `crontab -e`:

```cron
30 8 * * *  /ruta/a/btc-cycle-terminal/ingesta/local/ingesta_local.sh >/dev/null 2>&1
```

---

## Cómo saber si está funcionando

Tres capas, de más a menos inmediata:

1. **Notificación** en el escritorio cuando entran transcripts nuevos o cuando falla.
2. **`.local/ingesta.log`** — el registro completo, con el error literal de yt-dlp si lo hubo.
   Está en `.gitignore`, no se sube.
3. **`frescura.yml`** en GitHub Actions — se pone **rojo** si los transcripts se quedan viejos,
   da igual el motivo. Esta es la que de verdad importa: no depende de que tu máquina esté
   encendida, ni de que te acuerdes de mirar el log.

Esa tercera capa es la lección de agosto de 2026. La ingesta llevaba cuatro semanas parada
saliendo en verde porque cada pipeline informaba de **su propia ejecución** y ninguno del
**estado del dato**. Ahora el que vigila mira el dato:

```bash
python3 ingesta/frescura.py
```

---

## Qué hace el script, en orden

1. Aborta si hay cambios sin commitear o si no estás en `main`.
2. `git pull --rebase`.
3. Actualiza yt-dlp (cambia cada pocas semanas persiguiendo a YouTube).
4. Baja los transcripts nuevos de LMEC y de Cowen. **Un canal ilegible no aborta el otro.**
5. Commitea y sube lo que haya entrado, aunque el otro canal haya fallado.
6. Sale con **código 1** si algún canal fue ilegible.

Ese último punto es el corazón del asunto: `fetch_captions.py` distingue *"no hay vídeos
nuevos"* (código 0, normal) de *"no pude leer el canal"* (código 1, avería). Confundir los dos
fue el bug que tuvo esto parado un mes sin que nadie se enterase.

---

## Alternativas si algún día quieres volver a la nube

- **Cookies en un secret** — exportas las cookies de YouTube y el workflow las usa con
  `--cookies`. Funciona, pero caducan cada pocas semanas y estarías metiendo credenciales de
  una cuenta de Google en Actions: usa una cuenta secundaria, nunca la principal.
- **Proxy residencial** — resuelve el bloqueo sin tocar credenciales, pero es de pago.
- **Self-hosted runner** en tu propia máquina — misma IP doméstica, pero mantienes la ejecución
  dentro de Actions. Más piezas que este script para el mismo resultado.

# agentes — base de conocimiento de los analistas

Cada analista tiene su carpeta con **su material** y su fuente marcada. Los agentes
Claude Code (`.claude/agents/<persona>.md`) leen SOLO de aquí y **citan la fuente**.

| Carpeta | Analista | Fuentes |
|---|---|---|
| `lmec/` | LMEC (canal YouTube) | `yt-transcripts/` → transcripts de vídeo (**hablado**) |
| `cowen/` | Benjamin Cowen (Into The Cryptoverse) | `reports/` → memos escritos (**escrito**) · `reports-pdf/` → PDFs originales · `yt-transcripts/` → vídeos (**hablado**) |

> **Vídeo ≠ escrito.** Un transcript de vídeo es habla (muletillas, redondeos, erratas de transcripción); un report es texto editado y preciso. Por eso se separan y se etiquetan: cuando el agente cita, se sabe de dónde viene el dato y con qué fiabilidad.

**Para añadir material:** suelta el `.md` en la subcarpeta de la fuente correcta. El agente lo cubre automáticamente (grep).

## Lecturas diarias (`data/lecturas/`)

Un pase al día (`.github/workflows/lecturas-diarias.yml` → `agentes/tools/lecturas.py`) mantiene
la **lectura actual** de Cowen, LMEC y el Week On-Chain: tendencia, escenario, niveles, y según
quién, sus pools de farming (LMEC) o el rango de precio que espera (WoC). Solo llama al modelo
cuando hay material nuevo (transcript o informe con fecha posterior a la última lectura); sin
novedad no gasta ni toca nada. Se paga con la suscripción (`claude -p` + `CLAUDE_CODE_OAUTH_TOKEN`).
Cada lectura lleva fecha y fuente; el panel de LPs (sección "Decisiones") la enseña cruzada con
las posiciones reales y marca en ámbar la que supera el doble de su cadencia.

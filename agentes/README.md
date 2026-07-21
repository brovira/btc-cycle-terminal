# agentes — base de conocimiento de los analistas

Cada analista tiene su carpeta con **su material** y su fuente marcada. Los agentes
Claude Code (`.claude/agents/<persona>.md`) leen SOLO de aquí y **citan la fuente**.

| Carpeta | Analista | Fuentes |
|---|---|---|
| `lmec/` | LMEC (canal YouTube) | `yt-transcripts/` → transcripts de vídeo (**hablado**) |
| `cowen/` | Benjamin Cowen (Into The Cryptoverse) | `reports/` → memos escritos (**escrito**) · `reports-pdf/` → PDFs originales · `yt-transcripts/` → vídeos (**hablado**) |

> **Vídeo ≠ escrito.** Un transcript de vídeo es habla (muletillas, redondeos, erratas de transcripción); un report es texto editado y preciso. Por eso se separan y se etiquetan: cuando el agente cita, se sabe de dónde viene el dato y con qué fiabilidad.

**Para añadir material:** suelta el `.md` en la subcarpeta de la fuente correcta. El agente lo cubre automáticamente (grep).

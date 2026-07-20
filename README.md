# BTC Cycle Terminal

Panel personal de indicadores de ciclo de Bitcoin (semanal) + journal + señales de compra,
con alertas por Telegram. Uso educativo — **no es asesoramiento financiero**.

## Contenido

| Ruta | Qué es |
|---|---|
| `index.html` | Terminal completo: régimen de mercado, BMSB, SMA200, RSI, MACD, MVRV Z, bandas del Halving Cycle, journal de operaciones. |
| `lmec.html` | Dashboard enfocado en la **señal de compra LMEC** (2ª ruptura de la Bull Market Support Band + MACD verde + RSI 40-50). |
| `alerts/check_signals.py` | Script (stdlib) que calcula los indicadores y envía un mensaje de Telegram cuando una señal se cumple por primera vez. |
| `.github/workflows/alerts.yml` | Cron diario (GitHub Actions) que ejecuta el script. |
| `alerts/state.json` | Estado de las últimas señales (dedup por transición). Lo actualiza el workflow. |
| `lmec/transcripts/` | Transcripts del analista (canal LMEC) — base de conocimiento. |
| `.claude/agents/lmec.md` | Subagente Claude Code para consultar su plan de inversión. |

**Dashboard en vivo:** https://btc-cycle-terminal.vercel.app

## Alertas por Telegram — configuración

1. Crea un bot con [@BotFather](https://t.me/BotFather) → `/newbot` → copia el **token**.
2. Escribe algo a tu bot, luego abre
   `https://api.telegram.org/bot<TOKEN>/getUpdates` y copia tu **chat id** (`result[0].message.chat.id`).
3. En este repo → **Settings → Secrets and variables → Actions → New repository secret**, crea:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
4. (Opcional) Ejecuta el workflow a mano: pestaña **Actions → BTC signal alerts → Run workflow**.

## Señales que avisa
- 🟢 **Compra fuerte (LMEC):** 2ª ruptura de la BMSB + MACD recuperándose (histograma verde) + RSI 40-50.
- 📈 **MACD** cruce alcista en negativo.
- 📊 **RSI** semanal recupera >34 (confirmación de giro).
- 🟩 **MVRV Z** sale de zona de infravaloración (>0).
- ⚑ **Precio** recupera la BMSB.
- 🔄 **Cambio de régimen** (bajista → suelo/acumulación → alcista…).

Fuentes de datos: Binance / CoinGecko (precio) y Coin Metrics Community (MVRV), todo gratuito.

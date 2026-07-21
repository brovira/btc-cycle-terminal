# Bitcoin's Smart Money Signals EXPLAINED

**Fuente (VÍDEO):** onchainmind · YouTube — https://www.youtube.com/watch?v=EduAAGaR2jA
**Publicado:** 20250516 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20250516-bitcoin-s-smart-money-signals-explained.md]`.

---

Today, I want to dive deep into
something that might sound a bit
technical at first, but I promise it's
incredibly powerful and practical if
you're serious about understanding
Bitcoin's market behavior. We're going
to explore the power of UTXO data in
Bitcoin onchain analysis, what it is,
why it matters, and how I've combined
some custom indicators to give you
clearer, actionable insights into the
market. So, let's dive in.
First things first, what is a
UTXO? Well, it stands for unspent
transaction output. It's almost a
digital coin in the Bitcoin world. But
unlike physical coins, these unspent
transaction outputs come with two key
differences you need to understand to
really grasp what's going on under the
hood. Number one, every time you spend
one, it's spent in full. You can't just
spend part of it. It's all or nothing.
Imagine you have a $20 bill. You can't
just hand over $10 from that same bill.
You have to hand over the entire $20
bill and then get change back. Which
brings me to the second difference. They
don't have fixed face values like
physical currency bills do. Instead,
their values are completely flexible and
expressed in Satoshi's, the smallest
unit of Bitcoin. So if you have a
unspent transaction output worth three
bitcoin and you want to send two bitcoin
to someone else, what happens onchain is
that the original three bitcoin output
is spent entirely basically completely
destroyed and then two new outputs are
created. Two bitcoin that goes to the
recipient and one bitcoin that's the
change which comes back to
you. If you don't get it, don't worry,
you don't have to. We're about to go
through what the data is telling us in a
simple to view format. This type of
onchain analysis allows us to track not
just the movement of Bitcoin, but the
behavior behind these
movements. It's a rich source of data
that helps us decode what different
market participants, especially the big
players, are
doing. So, enough of the complicated
background. Let's get into some of the
custom indicators I've developed to
analyze Bitcoin's market action using
this data. The first one I want to talk
about is the whale distribution
indicator. This tracks when large
Bitcoin holders, often called whales,
might be offloading coins, but
importantly, they tend to do this during
periods of market strength. How do we
know this? Well, the indicator uses a
metric from Glass Node called the mean
value spent, which measures the average
USD value of spent transaction outputs.
When we see spikes in this value, it
suggests older or higher value coins,
usually held by long-term holders or
whales, are
moving. But here's the key. To avoid
false alarms from routine onchain
activity, this indicator compares
short-term and long-term exponential
moving averages of this metric, and it
only triggers when there's a significant
surge, in this case, 30% or more. On top
of that, it filters for context. It only
fires when Bitcoin is trading above its
30-day simple moving average, which
means whales are distributing into
strength, not panic selling during
downturns. It also requires a big daily
price move, a candle greater than 5% to
make sure the signal coincides with
meaningful price action. What you get
from this is a high confidence low
frequency signal that highlights
potential whale exits. It's not perfect
for pinpointing the exact day to sell or
buy, but it's incredibly useful to
understand how big holders are
positioning themselves on a macro level.
If you look at the past bull run, you'll
see this signal perfectly timed whale
distributions around the 35,000, 70,000,
and 100,000 rallies. So, yes, whales do
tend to sell at big rallies, but don't
think they're always smart or perfect.
They sometimes sell during downturns,
too, showing they're human like the rest
of
us. Next up, let's talk about the soaper
profit surge indicator. This one takes
the concept of spent transaction output
values a step further by merging median
spent values with the well-known SOA
metric, the spent output profit ratio,
which tells us if coins are being sold
at a profit or loss. The way it works is
by applying two moving averages to the
median spend and filtering these with
the famous soap metric, but only when it
is greater than one, meaning coins are
being sold at a profit. This isolates
moments where smart money or experienced
traders are either accumulating or
distributing at profitable levels. So
why does this matter? Well, because it
filters out the noise created by retail
traders or small
fluctuations. It zeros in on when
serious players are moving the market,
which often marks important turning
points.
During the major cycles like 2019 and
2021, this indicator lit up during heavy
profit taking phases. For instance, the
massive profit taking near the $100,000
level in this bull run was clearly
visible, showing many long-term holders
cashing out at this psychological
milestone. Now, combining these two
powerful tools, I created the UTXO
master index. This synthesizes the whale
distribution and the soaper profit surge
indicator to capture the nuances of
Bitcoin market dynamics in a single
comprehensive metric. It effectively
isolates moments where smart investors
are realizing profits while median
transaction sizes are
surging. This helps us distinguish
between healthy accumulation phases and
imminent sell-offs. Crucial for anyone
trying to time the market with more
precision. What makes the master index
especially valuable is its multi-layered
smoothing and filtering, which reduces
noise and highlights only the most
meaningful shifts in transaction
behavior. On the charts, you'll see
purple triangles that mark confluence
points where both the whale distribution
and the profit surge indicator
align. This confluence is key because no
single indicator tells the full story.
When multiple signals agree, the picture
becomes clearer and more reliable. It's
like triangulating a position. The more
points you have, the more accurate your
reading. If you're finding these onchain
insights valuable and want to stay ahead
of the game, hit the like button,
subscribe to the channel, and turn on
notifications so you never miss an
update. Now, let's dive back into the
analysis.
Finally, I want to introduce the
activity flow index, which is a
different but complimentary way of
looking at Bitcoin's onchain behavior.
This indicator measures the percentage
of Bitcoin's circulating supply that has
moved in the past 12 months, but with
smoothing to cut down on day-to-day
volatility and noise. When the active
supply percentage is rising, it means
more coins are changing hands over the
past year.
This generally signals increased market
participation or distribution by
long-term holders, often during phases
where holders are realizing profits or
reacting to major market events. These
periods often precede volatility or
price corrections. Conversely, when the
active supply percentage is declining or
staying low, it shows a large chunk of
Bitcoin is dormant, being held tightly
by investors who aren't moving their
coins.
This accumulation phase is a bullish
sign because it means reduced selling
pressure and supply tightening often
setting the stage for price rallies. I
have also converted this signal into a
momentum oscillator that measures the
rate of change in the active supply over
the trailing year. This oscillator uses
exponential moving averages and
calculates the rate of change over a
default 100day period. The output is
visualized as a colored line beneath the
price chart with a gradient from deep
purple to deep pink. Deep purple signals
strong negative momentum, meaning
declining activity. And deep pink shows
strong positive momentum, meaning
accelerating activity. This color-coded
oscillator gives you an intuitive feel
for how long-term holder activity is
shifting, which is invaluable for
anticipating market turning points. It's
especially powerful at spotting tops and
bottoms because long-term holders often
lead these phases. Looking at recent
history, the $70,000 and $100,000
rallies showed huge spikes in this
indicator, reflecting intense activity
from long-term
holders. Right now, though, despite the
price being above those levels, activity
remains relatively low, and we're
nowhere near overheated territory. This
is a very bullish sign suggesting
there's still room to run. I'm currently
putting the finishing touches on a
comprehensive suite of custom indicators
that will soon be available on Trading
View exclusively for premium members.
So, if you want to take your Bitcoin
analysis to the next level, stay tuned.
Big things are
coming. So, to wrap things up, the UTXO
model is really the backbone of
understanding Bitcoin's onchain
behavior. It lets us see not just where
Bitcoin is moving, but also reveals the
intentions of major players behind those
moves. This isn't just surface level
price action. It's about the deeper flow
of coins and what that tells us about
market sentiment. Then when we bring in
the whale distribution and profit surge
indicators, we get a clearer picture of
when the smart money is stepping in or
stepping out. These signals highlight
moments when experienced investors are
either taking profits or accumulating,
filtering out the noise from everyday
traders. That kind of insight is
invaluable if you want to understand the
market beyond just the price
charts. Finally, the activity flow index
adds another layer by showing us how
coins are circulating over the long
term. When activity is low, it suggests
strong accumulation and tightening
supply, which often precedes bullish
moves. On the other hand, spikes in
activity usually signal distribution or
profit taking, often leading to price
corrections. Together, these tools give
a much richer, more nuanced view of the
Bitcoin market, helping you anticipate
key turning points with better
confidence. And that's all for today's
analysis. Want more in-depth insights on
today's topic? If you prefer written
content, join my free newsletter for
exclusive analysis. Click the link in
the description. Thanks for tuning in
and I'll see you in the next one.

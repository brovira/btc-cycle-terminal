# On-chain 101: Reserve Risk - A Macro Oscillator capturing HODLer Behaviour Onchain

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=Qfm_XB3fhF0
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-on-chain-101-reserve-risk-a-macro-oscillator-capturing-hodler-behaviou.md]`.

---

hello everyone and welcome to your glass
node on chain 101 where today we're
looking at the reserve risk oscillator
which is actually one of my favorite
on-chain metrics simply because of how
much on-chain hodler mentality is baked
into a single line it really has a lot
of the underlying concepts that we use
in on-chain analysis baked into it and
therefore it provides a very very
interesting behavioral model as to what
the hodlers are doing both on the upside
when they're exiting and on the downside
when they start accumulating
so the reserve risk metric is this big
picture cyclical oscillator and what
it's really trying to track is when the
reward and the risk profile is in the
favor of hodler's i.e at the end of bear
markets when they're undertaking extreme
accumulation or when it's getting
towards the end of bulls and they're
actually liquidating a large portion of
their coins into strength
so what we're going to look at today is
an overview of reserve risk and how it's
used we're also going to start diving
into the calculation method how do we
get there how is reserve risk calculated
and what are the different inputs that
affect it
so we're going to look at things like
calculating the value of coin days
destroyed which is trying to bring the
amount of life span that's destroyed and
spent back into the market into the
price domain we're going to look at the
concept of hodl opportunity cost and
what that actually means in terms of
accumulation or spending behaviors and
then how all that distills down into the
single line that is the reserve risk
oscillator so let's get into the
analysis
so we're going to start the very big
picture just so we can see what reserved
risk looks like and what the general
concept of it is
so we're here in glass node studio and
what you can see is that reserves
typically trades
between these very very high peaks where
it's in the overvalued zone around
market tops we can see we had two of
them in 2013 one of them in 2017. we
didn't quite get there during 2021 and
we can explore that a little bit more as
we get into the component section of
this
you can also see that it pulls down into
these low undervalued zones these green
zones and interestingly it seems to
trade down here for quite some time you
can see that it picks up the back half
of the bear market in 2014 all of the
capitulations earned in 2015 and
actually captures the vast majority of
the 2016-17 bull run so it almost picks
up the first half of the ball before it
really accelerates into the blow off top
we can see here in the 2018 bear that it
essentially picked up the capitulation
zone as being undervalued 2019 poked its
head above but was hauled back down into
that zone and you can see that whilst
price was more or less sideways on a
macro scale in 2019 and again in 2018 we
had a floor price of around six thousand
dollars the market traded sideways note
how reserved risk hauled this metric to
the downside it's interesting that it's
almost like it has a form of gravity
it's being pulled down into the
accumulation zone or into this
undervalued zone and it really remained
there almost until we broke the previous
cycle's all-time high
so you can see that there's a gravity
that's pulling this metric down during
bearish periods but also note the speed
and how quickly it rallies up into the
all-time highs
so this is the dynamic that we're going
to explore a little bit in a little bit
more detail on how this metric is
constructed and why in this particular
instance we do get this very very long
and slow accumulation bottoms and a very
very rapid and reflexive rally to the
upside and note that reserve risk is on
a log scale so every point that it's
moving up is a factor of 10 rather than
in linear scale so you can see it really
does move to the upside very very
quickly and spends long times in the
downside
and relevant to our current market
structure even though we set an
additional all-time high here in october
and november note that reserve risk was
much much lower and again it's being
hauled back down into this accumulation
zone and we're going to explore these
mechanics actually using the workbench
tool
so here we are in glass node workbench
which is our tool that we can use to
create compare and contrast different
metrics to really dive into the weeds
and find out what's going on with each
of these particular inputs
so you'll find this particular metric
reserve risk components underneath our
presets for market indicators you'll
find it here termed reserve risk
components where it really breaks down
all the different puzzle pieces that go
into constructing the reserve risk
metric
so let's start with what we have shown
here which is price m1 in our grape
gray marker to the left hand axis and
supply adjusted coin days destroyed in
the blue
so let's start with what coin day's
destroyed are
when we have a coin in the coin supply
each one btc will accumulate one coin
day per day two btc will accumulate two
coin days and half of bitcoin will
accumulate half a coin day so it's a
measure of lifespan how long a coin has
been unmoved or unspent in an investor's
wallet
now we typically see coin day
destruction which is when that coin is
spent the life span is destroyed and it
starts re-accumulating
so we see large amounts of coin day
destruction in bull markets we can see
here in 2017 in 2013 again in 2019 and
then in 2020 and 2021 and this is when
those hodlers who have older coins and
they've accumulated during the bear
market start selling into strength
they're essentially looking at the
current price and saying i'm now going
to liquidate my coins and therefore more
demand needs to come in and soak those
coins up
now conversely during a bear market we
have a much smaller amount of coin data
destruction it shows that more of those
coins getting sucked out of the supply
into investor cold storage where they
start to actually accumulate coin days
we're not seeing that selling of those
one year and two year old coins we're
generally seeing younger coins being
pulled off the market and going into
cold storage
now we can bring coin day destruction
into the price space by multiplying by
price and thus we get the value of coin
days destroyed
now that's what this orange chart is
showing and the way to think about this
is the actual amount of value that
hobblers are liquidating they're
essentially spending their coins and
taking some amount of profit or loss out
of the market it's the spending behavior
that is therefore saying the current
price is sufficient to motivate me to
spend my coins
now there's a couple of observations
here we can see that during the blow of
tops 2013 and 17 note how the orange
curve starts to overlap with the price
curve
so the way to think about this that
price is the incentive to sell and the
actual sell side is matching the
incentive so hodlers are saying i am
going to spend my older coins because
the current price is enough to get those
coins out of my cold storage i think
that it's a fair price and i'm going to
therefore sell my coins
now conversely during a bear market note
how there's more white space these two
charts separate the incentive to sell is
not enough to bring those coins out of
cold storage this is because hobblers
believe that bitcoin is going to be
worth more in the future and even though
the price back here in 2015 was 230
dollars 250
the amount of spending was much much
lower so they're choosing to keep those
coins in their wallet and not spending
them so it's showing this level of
conviction and strength within the
market
now we can see that value of coin data
is destroyed is quite noisy there's lots
of daily noise and it moves around quite
a bit
so what we're going to put on now is the
median value of coindays destroyed so
we're just taking a running median that
essentially smooths out and gives us
kind of the center line or the average
typical price
now what we can see is that much more
clearly we get the median value of coin
days destroy which is the amount of
spending starts to match up with the
incentive to sell which is the price
particularly during the late stage of
bull markets we saw this again in 2021
as we pulled into the january peak and
we can see it again in 2013 in both of
these peaks where the the median value
of coin days destroyed matched up with
the actual incentive to sell so the
price was sufficient to bring those
coins out of hodler wallets and their
spending matched the actual incentive
now the flip side of that is during bear
markets note this wide separation of
these two values you can see it again in
the 2018 and 19 bare phase and then we
can see it after the top here in may we
saw another opening up a widening up of
these two two metrics
now this is suggesting that even though
the incentive to sell the current price
is up here around 38 000 and back here
it was 69 000 there was some increase in
spending but generally speaking hotlines
were actually keeping the coins in their
wallets there's less spending or there's
higher conviction in the market
and the gap between the incentive to
sell and the actual selling you can
think about this is almost the
opportunity cost it's the amount of
dollars that hodlers decided to leave on
the table they could have taken profits
at any point during this market cycle
but they chose not to because they
believed that bitcoin was worth more
than the current price
and this is how we construct the
huddlebank
so bank is actually the denominator of
the reserve risk metric and it will
trend higher and it will get larger when
there's more holding going on
so being in the denominator of reserve
risk when there's more hoddling and
there's more opportunity cost that
hoddles are choosing not to sell
then you're going to get an increasing
denominator and that's going to pull
down the reserve risk metric which is
what we saw before that during these
bearish markets reserve risk got pulled
down into the green zone
now conversely note during the 2017 top
and here again in the 2021 top we
started to get this flattening out
hollow banks stopped moving as much
because we're getting that closing up
there's less opportunity cost the actual
sell side is matching up with the
offered price by the market
so during that period of time the whole
bank in the denominators increases much
much less and therefore we get that
acceleration into the top the spending
is matching the actual price and
therefore we're seeing more coins come
back into circulation and we get this
very reflexive move of reserve risk into
that top
so now we can actually add in reserve
risk and we've got our bounds
and what we can see is that during
periods where we have this um this
matching up of the amount of sell side
with the incentive to sell you can see
that reserve risk rallies into the top
and you can see that this is a very
reflexive maneuver
and then likewise during these more
bearish periods when the gap between the
incentive to sell and the actual selling
is much less even though price trades
somewhat sideways on a macro scale 2018
is a good example sideways price with a
floor at 6 000 but reserve risk is being
pulled down this increasing opportunity
cost that hodlers are choosing not to
sell is creating this down draft and
pulling reserve risk into this macro low
zone
so what we're really seeing here is that
reserve risk will weight down when
there's more accumulation when the
hodler behavior is favorable for price
noting that it can take some time to
actually generate these macro bottoms
but that's why it really pulls down
price during the late stage of the bear
and even keeps it in the undervalued
zone all the way into the almost around
the middle of the ball before we get
that euphoric push up to higher levels
so when we look at our current market
cycle we can see that previously we
broke well and truly above the
overvalued zone as the spending pressure
was sustained for a number of weeks
number of months as the overall price
pushed higher more and more coins came
back into circulation and eventually the
bull had to be exhausted
now what we saw during our 2020 and 2021
bull is that there was a peak in overall
hotless spending but at no point did it
really sustain that for a long period of
time and we really saw that they went
back into that hoddling accumulation
behavior much much sooner which started
to apply this downwards force and pull
the reserve risk metric back down into
the undervalued zone
so it's quite an interesting dynamic
that even though we saw much much higher
prices the overall hodler base after
that may sell-off really moved back into
accumulation and hobbling mode which is
quite an interesting dynamic it's
certainly nothing that we've seen in any
of these previous market cycles if
anything it looks a little bit more like
this 2013 top where we had an initial
bout of sell side which then opened back
up into a period of dormancy and
toddlers not realizing that opportunity
cost now granted we haven't had the
follow-on rally what we've essentially
seen is a pull back into this uh this
more bearish trend so we've really
pulled this reserve risk metric back
down into the undervalued zone and in
past cycles it has remained there for a
somewhat extended period of time so that
tries to set the expectations for how
this metric actually functions
so overall the reserve risk metric is a
very big picture and macro oscillator
and it's trying to capture that hodler
conviction the spending behavior and
really trying to identify when a
hodler's choosing not to sell and
leaving that opportunity cost on the
table
as a result of this it generally creates
very very long bottoming patterns during
accumulation periods and they can last a
number of months and sometimes even
years as those hodlers just soak up the
supply and we generally have to use
reserve risk alongside a number of other
metrics that really speak to the demand
side
but what we also see is that during
those euphoric peaks when the market is
very excited lots of those hoddlers
start liquidating those coins and
spending they believe that the current
price is enough to bring their coins out
of cold storage and we see that increase
in coin day destruction that's when we
start to signal these very very
reflexive blow-off tops that the reserve
risk is actually quite good at picking
up because it's showing that the amount
of sell side is in fact matching the
current price so essentially it's enough
to bri enough incentive to bring those
coins out of cold storage
so hopefully you enjoyed this on chain
101 doing more of these deep dives into
how these metrics are constructed and
what to pay attention to
do let us know what your favorite
metrics are and what you would like us
to cover in the future be sure to give
us a rate of review and to subscribe and
we look forward to seeing you in the
next one
cheers

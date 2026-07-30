# Glassnode Onchain Analysis Week 27, 2021

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=Prw2uo-LM3w
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-glassnode-onchain-analysis-week-27-2021.md]`.

---

hello everyone and welcome to your glass
node video report for the week on chain
week 27
we're recording this on the 6th of july
2021.
so this week we really focused on the
mining migration that's going on what
we're calling the great hash power
migration
and what we're trying to provide here is
a bit of context and looking at the
on-chain data to understand the
magnitude of how large this migration
actually is
so what we're going to look at is a lot
of the on-chain data that relates to the
mining market some of the mining
dynamics
we look at things like block intervals
look at hash rate look at difficulty
multiples
just to get a bit of a feel for what the
estimated impact actually is
and how much of the actual hash power is
currently on the move or what our best
estimate is of that
and we'll also look at things like the
minor revenue and some of the logistical
costs incurred because we have a very
interesting dynamic
where approximately 50 percent of the
hash power is currently offline
and incurring a great number of costs
due to logistics and just simply not
being hashing having hardware that's not
currently working
and the other 50 has essentially seen
half of their competition drop off the
network so
whilst the protocol is now issuing the
same number of coins that it regularly
does having difficulty now wound down
we're now in a situation where half of
the network has doubled their income
and the other half of the network is
essentially producing nothing
so it's this very interesting dynamic
and what we're looking for is what is
the potential risk and what is the
magnitude of potential cell pressure
or otherwise accumulation pressure that
we may see from the mining market
and within that we'll also look at some
of the nuances and some of the on-chain
metrics so there's a number of different
indicators that
may flash certain signals certain
indicators
but what we really need to do is correct
some of that for some of the immense
amount of changes that's going on in
terms of the hash power what happens
when blocks actually slow down
is you see a reduction in the overall
issuance over that
period of time so it's really about
understanding the mining market
and some of the dynamics that are going
on to fully appreciate what these
metrics are telling us
so let's jump across the glass node
studio and we'll get started with the
report
so here we are in glass node studio
we're looking at our week on chain
dashboard
now whilst this week we've really seen
volatility seeping out of the pricing
market we trade in a fairly narrow range
of about 32 000 to the upper 36 000 this
week
what we have seen is a lot more
volatility going on in the mining space
and
this is a truly impressive event that's
going on as this this mining migration
that's coming out of china is
many many miners now looking for
relocating reallocating their capital
moving their hardware to somewhere else
to actually re-establish their
businesses
some of them are waiting on the
sidelines just waiting for the dust to
settle to see whether they can
re-establish their operations
it's a really really complex and very
very large shift in the market and
there's very few industries that can
really see this degree of their
industrial base pick up and move
or essentially relocate their their
capital and their hardware
with generally minimal disruption so we
saw some slightly slower block times
uh what we've got here is our mean block
interval so
just for those who don't know at a
protocol level or at a
on chain level bitcoin really only knows
about the block interval so what is the
timestamp that miners are encoding into
the block header
and the mining difficulty so these are
the two on chain parameters that we have
we can then using those two as inputs we
can derive an estimated hash rate or a
mean hashrate
so the way that we actually calculate
this we look at our mining difficulty
which is fixed over a 14 day period
we then look at what the overall block
times that are coming in what is the
the typical or the average protocol
block time that's coming in
we can then use that to back out and
back calculate what the estimated hash
rate is in order to achieve that block
interval
under this particular mining difficulty
so the protocol
hashrate is actually an estimate so in
terms of looking for
purely accurate information we generally
would rely on block interval and
difficulty to understand what's going on
at the base level
we can then use that to imply a hash
rate
so prior to the difficulty adjusting
down as we see hash power coming off the
network
the mean block interval starts to slow
and what we saw this week was actually
the longest average block time on a 24
hour rolling window
in all history essentially you have to
go back to 2009 when bitcoin was mined
on cpus and before it even had a price
to find a block time that was this slow
on a 24-hour basis
so really we're talking about in all of
bitcoin's modern history and all the
time where bitcoin has had pricing
markets and
really was outside the bootstrapping
phase of 2009 2010
we had to go all that way back to find a
block time that was this slow and this
gives us a bit of a scale on just how
large this shift in the mining market
really is
now if we then revert that back to mean
hash rate so hash rate is a derivative
we mentioned that block interval
and difficulty are protocol core metrics
the hash rate is then estimated using
those two
instances so we have a mining difficulty
which is the complexity of the puzzle to
be solved
we then have the speed at which blocks
are being solved under that difficulty
regime
we can then use that to estimate what is
the overall hash power that is on the
network so let's take an estimate as to
what our maximum hash power that was on
the network
prior to this sell-off and prior to the
mining ban coming in in china
if we look back to around april to early
may the hash rate was roughly around 180
to 160 extra hash per second so that
gives us a bit of an idea of
the total number of machines that were
operational that period of time
now since we've had our price sell off
by approximately 50 percent
and we've then had the mining band come
in and miners start to switch off out of
necessity
where we're now trading in the current
range and again this may change over the
coming weeks
but where we are at the moment is about
88 to 110 extra hash per second which
gives us from our 180
exah baseline at the top that gives us
roughly around 38 to 49
drawdown in the total number of miners
so if we take the upper bound of that we
can say that approximately on an
estimate of the current day
about 50 of the market is currently
offline which gives us a scale of just
how large this migration really is
now we saw the largest downwards
difficulty of mining
the mining protocol down 28 percent this
week we're estimating there's going to
be another about 13
at the current time downwards difficulty
adjustment so the reason that we're
estimating about 50 percent of mining
power off the network but the difficulty
adjustment was only 28
is because the difficulty adjustment is
measuring over that 14-day window
and over the 14-day window we can see
that the the overall block time actually
accelerated to the downside so we're
seeing
an increasing number of longer and
longer blocks
but the front end of that 14-day window
has slightly faster blocks so on
average the bitcoin protocol estimated
about a 20
downshift was necessary and it's
therefore going to take a number of
weeks
depending on how hash rate trades even
if it starts to stabilize if it
stabilizes at this level for the next
14 day period then likely the next
difficulty adjustment
will return it to equilibrium and we'll
start seeing that 10 minute block time
if however we start to see more hash
power coming offline
or in the converse we actually see hash
power coming back online when those
machines get relocated
then the difficulty adjust will take a
number of weeks to actually find out
what is the happy medium what is the
equilibrium that it's going to take
so it is quite a interesting market that
it's going to take time
and the rate of response for the mean
hash rate how long it takes to actually
start to revert
will give us some indication as to the
amount of time or how prolonged miners
in china
are currently under financial stress
because at the moment they're not
producing any income
their machines are essentially sitting
there without producing you know they're
not costing
opex but they certainly have debt and
capex obligations that remain
in play so those machines are currently
unproductive
and the faster that they can get back
online the sooner that the income
stress will start to deviate so this
will tell us the mean hash rate as it
starts to recover
that will tell us how quickly these
miners are actually getting their hard
way back into operation
and potentially helping revert that
headwind risk of
perhaps having more cell pressure from
their treasury so the longer that the
hash rate remains depressed
the more likely that income stress is
going to lead to treasuries having to be
spent
now just finally on the protocol level
so the difficulty ribbon is an
interesting metric that will
established a number of years ago and
what it was really designed to look at
is minor capitulations in particular at
the end of bear markets
so we saw this at the end of the 2018
bear market we saw it twice in 2020
first after the halving of
price in march 2020 then again after the
protocol halving so
that really reduced the aggregate income
for miners by
50 twice back to back after the 2018
bear market obviously it's been an
extended period of depressed pricing so
what happens with the difficulty ribbon
is we're looking at the fast moving
averages the nine day and the 14 day
when they dive underneath the slower
moving averages the 128 day
and the 200 day and what this is really
indicating is when is their income
stress in the mining market and when are
miners having to switch
off their machines now when some miners
have to switch off their machines
what that effectively does is it
increases the number of coins that are
gained by the miners who remain
operational
because the same number of deterministic
coins are issued based on the
overall uh monetary policy for bitcoin
so because the difficulty is adjusting
up and down to make sure that that
deterministic issuance remains in play
the miners who remain on the network are
spending the same amount on their
hardware costs and on their electricity
costs but the amount of coins they're
earning per hash
starts to increase so really what the
difficulty ribbon is telling us
is when we're getting that income
squeeze when some of those miners are
experiencing an income squeeze
and that also means that other miners
are actually gaining in hash share and
therefore are able to sell fewer of
their coins
now we're in a very interesting scenario
here where it could be a very prolonged
period of time until the hash rate
starts to come back online and that's
really how we can use this dashboard and
these metrics
to really track how this this migration
and how quickly and how or how slowly
the mining hardware can get back online
because the longer that income stress
remains in play
the more likely miners in china will
have to liquidate treasuries to cover
their obligations and cover their costs
so this is where we can jump into
looking at minor revenues which
as i mentioned there's about fifty
percent of the mining market that we
estimate to be offline
at the current time and that means that
the other 50 has essentially seen half
of their competition drop off
so we're in this very interesting
dynamic where half of the miners are
incurring extraordinary logistical costs
and opportunity costs by their hardware
not hashing
and the other half of the market is
actually seeing their revenues
approximately double so where we were
back in april
when we were trading at the 55 60 000
range
we saw aggregate minor incomes or across
the entirety of the
mining market somewhere between 50 and
60 million dollars per day
so since that point we've obviously had
a approximately 50
price correction we've traded down from
60 000 to roughly 30 000
and that means that the aggregate mining
income purely from the block issuance
is coming out at roughly 25 to 30
million dollars per day
so whilst the overall revenue has
essentially halved
the miners who remain operational have
seen half of their their
competition drop off the network so the
profitability of miners who remain
online at this point in time has
actually reverted back to somewhere
similar to where we were at the all-time
high zone
so this is a very interesting dynamic
where half the miners are incurring huge
costs
half of them just saw their income
essentially double
so what we can then look at is what kind
of cell pressure we're seeing on
aggregate
so we have two metrics here one is the
minor outflow multiple
and the other one is the minor unspent
supply so the minor unspent supply is
essentially looking at all of the coin
based transactions when a miner mine's a
fresh block
there's a special transaction called the
coinbase transaction which includes the
newly issued coins
so what we're looking at with the minor
unspent supply
is summing up all of the total unspent
coinbase transactions or essentially
coins have been mined and have never
moved
now just note that on the axis here
we're up in the 1.7
ish million coins this does include the
early coins that were mined by satoshi
because they remain
coinbase transactions and they're also
going to be early miners from very early
on
who very likely have lost those keys
some of them will still have them but
some of those will also be lost so just
bearing in mind when we're looking at
this axis this includes all coinbase
transactions that remain unspent
so what's really key to look at in this
particular metric is the trend
when we have a downtrend in unspent
supply it means that miners are by and
large selling more coins and they're so
they're mining
a certain amount and they're selling
more than they're holding on to right
there is a net outflow of unspent coins
conversely when we have an uptrend it
means that miners are essentially
accumulating they're
selling less than they're holding and
what we've seen is that during 2020 we
saw a fairly dramatic
increase in the overall unspent supply
so miners were clearly accumulating
likely in response to the monetary uh
environment and the macro environment
that bitcoin found itself in
we saw a large amount of distribution as
we rallied up into the 42 000
first peak and then we actually reverted
back into a zone of accumulation
now that has started to slow down we've
started to see a softening of this
gradient and a number of these
treasuries appear to have been
liquidated in
this recent consolidation so this is
certainly one to watch do we continue
with this uptrend in a macro sense
does it start to revert to a downtrend
suggesting that miners are in fact
stressed and need to offload more of
their coins to cover their costs
or do we start to trend sideways which
is really saying that for all the coins
that are coming in
the same amount of coins are being held
onto so the trend of this metric is
going to provide us a bit of insight to
this
now the minor outflow multiple really
tries to capture this in a bit of an
oscillator
and it will spike higher when we're
seeing a over relative to the the
previous year the
last 365 days how many coins are being
spent so it's a relative metric that's
looking at what is the spending behavior
today
relative to the previous year now what
we saw is that same behavior we saw a
significant spike in the minor outflow
multiple as we rallied in this bull
market
we've then seen a resumption of this
downtrend we're suggesting that
overall there is more coins being held
onto in the minus spending behavior is
actually declining
now will we actually see this start to
trend higher if it starts trending
higher that would tell us that yes
miners are actually spending and it will
correlate largely to our unspent supply
trending down
so between these two metrics we can
start to see what that balance is
between miners who have to spend their
treasuries out of necessity
and miners who remain on the network
live at the moment who are currently
operating a very very high profitability
somewhere like where we were back in
april
and potentially we'll be able to sell
far fewer of their coins and hold on to
a lot more
and just to close out we'll look at uh
the puel multiple
which is a very interesting metric that
flashes green uh this week
however it's only done this on a very
very select few number of times and
quite often the pure multiple will flash
green
at the same time as the difficulty
ribbon will invert they tend to
correlate with very very large
capitulation events historic events that
are
typically generational bottoms of some
form
so the pure multiple is calculated as
the aggregate us dollar
revenue so the revenue that we have
coming in for miners in u.s dollars per
day
divided by its 365 day or its yearly
average
so what we're looking at there is what
is the overall income today relative to
the yearly average
so this will trend higher when miners
are very very profitable and relative to
their yearly average making a lot more
money
and it will trend down when they're
making a lot less relative to their
yearly average
so as we noted the overall issuance of
blocks
slowed down substantially this week and
on the 28th of july we actually hit an
all-time low of daily inflation rate
which is 0.71
so what that actually means is that
instead of the 144 blocks that bitcoin
typically mines on a daily basis
we only saw 58 blocks mined and what
that's really telling us is that fewer
coins were issued that day
now when fewer coins issued naturally
minor income is also going to fall
particularly relative to the slow one
year moving average
and therefore our pure mult will
actually dip down into this
undervalued zone before quickly
reverting as a result
of the difficulty adjustment changing
the complexity of the puzzle
and adjusting it so that the current
mining hash power was more suitable to
the puzzle to be solved so we saw the
issuance then spike back higher
we saw our inflation weight return back
into the stable deterministic range
and it really goes to show how there has
to be some nuance and understanding of
how these metrics are put together
to fully understand what this signal
means and whether it's actually a
technicality or whether it's genuinely
flashing a capitulation style event
so in terms of the pure multiple we've
recently refreshed our glass node
academy instance for this
and we include a lot of details not only
on the pure multiple and how to
understand it
but certainly on the mining market
itself because the pure multiple is
really capturing a lot of dynamics and a
very simple indicator
of what's going on in the aggregate
mining space so it talks about a number
of elements like when miners have to be
have greater profitability when they
have reduced profitability and what are
the overall
impacts of that business that are then
reflected in something like the pure
multiple
so thanks for listening in i hope you
enjoyed this session and i look forward
to seeing you in the next one
cheers

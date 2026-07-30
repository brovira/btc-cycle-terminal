# Fundamentals of Bitcoin Mining (On-chain 101 Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=NZANBZ_lNqw
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-fundamentals-of-bitcoin-mining-on-chain-101-analysis.md]`.

---

hello everyone and welcome to your class
note on chain 101 where today we're
going to be exploring the fundamentals
of proof-of-work mining now mining is
one of the most interesting but probably
least understood components of the
bitcoin network and what we're going to
explore today is some of the dynamics
about how the mining industry operates
and how that then manifests in these
metrics and we can actually track and
see where the industry is at whether
it's currently in a period of higher
profitability or whether it's currently
experiencing significant income stress
and then what that means for the market
moving forward
so what we're really going to explore in
this session are these mining dynamics
and how we can really track them using
on-chain metrics so we're going to talk
about things like understanding
difficulty block intervals and how that
is then calculated into the estimate of
hash rate
we're going to look at minor revenues
and profitability and various metrics
that help us track this
we're going to particularly look at
minor capitulation cycles as we know the
coin price is going to influence minor
revenue so therefore they are also
subject to the cyclicality of these
markets
and then we're also going to look into
some advanced modelling of some of these
minor cycles and divergences things to
be paying attention to when we start
seeing a divergence between metrics what
that may mean moving forward
so just before we get started with some
of the metrics i know that some people
who are watching this clip may not
actually understand the basics the very
very fundamentals of what bitcoin mining
is so let's start with a very very
simple overview of what's actually going
on when it comes to bitcoin mining
so we really have four different
elements that we're going to focus on
here we have the bitcoin nodes now these
are elements they can be raspberry pi's
they can be laptops or computers they
broadcast transactions and verify blocks
so whenever you use a bitcoin wallet it
will talk to a node and then that node
will broadcast that transaction
now the miners job is to solve the
blocks and actually put all of those
transactions into a block and build the
blockchain
now once they've solved the block the
nodes will come in and actually verify
it so the nodes are the ones that are
checking the rules and the bitcoin
miners are the ones that are putting the
transactions into blocks
now the bitcoin protocol will then pay
these miners for their service they need
to expend power and actually deploy
hardware and capex to this problem so
therefore the bitcoin miners are paid
with the bitcoin block reward which
consists of both the subsidy and the
fees
and then we also have the protocol
difficulty which we'll talk about a bit
later on and this is really regulating
the puzzle complexity that the miners
must solve
now let's actually talk about this from
a linear standpoint what is actually
going on with this system
so
let's imagine we have two blocks this is
at the end of the the existing
blockchain these have been solved and
these contain the confirmed transactions
there's a whole blockchain built behind
this but we're looking at just the last
two blocks that have been confirmed
now as a result of this last one it's
paid these miners over here these are
the asic rigs it has paid them the block
reward consisting of the block subsidy
and the fees so this is how the miners
are incentivized to continue to mine on
the chain because they have power input
costs they also have to buy their
hardware they need facilities there are
costs associated with it and this is why
the block subsidy in the fees are there
to pay the miners
now at the same time as this is
happening we have a network of bitcoin
nodes these as i said these can be
raspberry pi's laptops they can be
computers whatever they are that are
running the bitcoin software
now they have two jobs they broadcast
transactions into what we call the
mempool this is kind of the circulating
pool of all the transactions that want
to be confirmed
and when a block is mined they verify
that all of the transactions in that
block followed the consensus rules that
they didn't double spend that there
wasn't any theft they essentially are
the ones that check to make sure that
the miners are not cheating the system
so from this pool of transactions they
have all got a transaction fee different
ones will be paying a different
transaction fee depending on how urgent
it is to get solved
so what's going on is that the miners
have this pool of transactions in the
mempool and each individual miner i've
just marked out three here and red
yellow and blue but there are obviously
many many miners out there each one
selects from the transactions that are
currently waiting to be confirmed which
ones are going to pay them the most they
look at all the transaction fees
they look at the limits that they have
on the block size and they can only fit
so many transactions in that block so
they select the ones that are going to
pay them the maximum amount for that
particular block
now what is going on is that all of
these miners are trying to solve a
complex mathematical puzzle they're
trying to solve a sha-256 hash
now what they're trying to do is is
solve a puzzle that is as difficult the
way to think about this it's like
finding a needle in a haystack where the
haystack happens to be about the size of
the universe so if you took every single
person on the planet it would be them
guessing every single second multiple
quadrillion guesses of this shah 256
hash so it's a very very complex puzzle
solving many many repetitions
and each one of these miners is trying
to solve and find the answer to this
puzzle because the one that does solve
the answer to that puzzle is able to put
their selection of transactions into a
block get paid the block subsidy and the
fees
and the moment that that happens when
this block is confirmed all those
transactions go into it they become this
last orange block here and the process
repeats and on average the reason that
this protocol difficulty will change up
and down is to try and regulate the 10
minute block time which we will talk
about momentarily in all of the charts
so i hope that's a bit of a an overview
of how bitcoin mining works a bit of a
crash course in case you haven't heard
it before these are the different
components the miners are competing to
solve blocks so that they can get paid
the reward and the transaction fees and
the nodes are then broadcasting the
transactions which can then be selected
to go into that block
so what we're going to start off is
probably the most well-known mining
metric which is mean hashrate and we
have this plotted out in two different
scales the one in the left in blue is in
a linear scale and you can see that the
previous history has essentially
collapsed down to not much much like the
price chart when it's plotted out in
linear you lose the early years up to
about 2017 onwards
now on the right hand side we then have
it plotted out in logarithmic scale we
can actually see the expansion of hash
rate and this is a result of various
mining hardware upgrades so initially
when it was just satoshi bitcoin mining
was performed only using a laptop or a
cpu and over time that started to move
into the gpu phase which is a graphics
card it has a dedicated ability to
process just graphics so it's much
better doing singular tasks where cpu is
more general
so we saw an expansion of hashrate
particularly through the 2011 2011-2012
era we then moved into this phase where
we had what we call fpgas which is these
programmable chips that can also do one
particular task but they're programmed
to do so so they're not designed for
that particular task but they can be
programmed to perform a specific task
and we saw an additional expansion
however that phase really didn't last
very long before asic chips application
specific integrated circuits
they started to come to market in late
2012 and we can see this logarithmic or
this massive expansion of hash power so
this is the growing efficiency of
machines coming to market and bitcoin
has gone through many cycles and you can
see it generally goes through these
large expansions of hash rate during
bear markets when there's less capital
available it starts to plateau and then
as the bull market kicks back in we see
a yet another expansion
so we can see that it is quite volatile
in a linear scale you can see here in
may 2021 where we had that event where
many of the miners were forced to leave
china they were 52
or thereabouts of the overall hash power
we have since seen a recovery of that
but you can see that it is quite
volatile over time
but that's the fundamentals let's kind
of step through some of the building
blocks because hash rate is actually an
estimate not something we can measure
from the chain directly we actually have
to calculate it from two other metrics
so the most fundamental metric when it
comes to the mining space is called the
protocol difficulty now this is
essentially the complexity of the puzzle
that bitcoin sets for miners
now the way the difficulty works that
every 2016 blocks which is approximately
14 days the bitcoin protocol looks at
all of the all of the blocks mined in
that window and it looks at the time
stamps between them and the target is
that those time stamps should be on
average 10 minutes or 600 seconds
now when there's more miners coming to
market or the hash rate is increasing
the amount of machines that are on there
the efficiency of the machines has
increased
what it will do is it will wind up the
difficulty it will make the puzzle
harder to solve
now this puzzle is akin to trying to
find a needle in a haystack but in this
instance the haystack is about as big as
the universe we're talking about
quadrillions and quadrillions of guesses
per second that are being performed by
these machines
so what we see is that over time
difficulty has been on the way up we can
see periods where it starts to pull back
this is generally towards later stage
bear markets and we'll explore this in
more detail but this is when mining
equipment is being turned off as a
result of that financial pressure you
can then get these expansions when more
miners literally in number or in
efficiency are starting to come they're
more efficient miners they can do more
computations per second and that becomes
part of this industry of competitiveness
these miners are competing to solve
blocks the puzzle is increasingly
getting harder and what this essentially
does by the puzzle getting harder and
keeping block time at 10 minutes it
keeps that supply curve nice and clean
we have this deterministic supply curve
where we can estimate bitcoin's
inflation rate and the amount of coins
issued per day well into the future
that's really what the difficulty
protocol is doing by ensuring that the
the overall block time is within 600
seconds the puzzle adjusts up and down
depending on the observed block times
now this is where we move to the block
interval this is the second piece of the
puzzle that can be directly pulled from
the network so we can observe difficulty
it's encoded into each block what the
difficulty is and how much accumulated
work has been put into that chain this
is how we know that the blockchain how
it keeps consensus called nakamoto
consensus the protocol and every single
node in the network can look at all of
the blocks all the different versions of
the blockchain and see the one that has
the most accumulated proof of work and
it uses that difficulty function to work
this out
now the block interval is the observed
performance every time a miner solves a
block they encode the timestamp into the
block header so what the bitcoin
protocol does it then looks at all of
the blocks in sequence and looks at what
is the average block time
now we've got marked out here in black
is the target block time this is the
protocol what it will adjust the
difficulty to try and get that block
time in line with and that's 600 seconds
or 10 minutes
now you can see that through periods of
time in the orange and being quite noisy
there's natural variability in when
blocks are solved but this orange is the
average block time so in terms of
seconds so when it's dipping down below
the black line it's essentially showing
that the overall block time is faster
than what's going on with the target so
the difficulty during these periods
where mean block time is below the
target during this period which is
generally bull markets as miners are
expanding their operations and more
hardware is coming to market blocks will
be coming in faster on average
now every two weeks the bitcoin protocol
will make the puzzle harder but if we
have an expansion that occurs over the
course of that two weeks or across that
boundary this is why we get these
expansions where the actual hat the
actual block time is less or shorter in
duration blocks are coming in faster
more hash rate is being applied
now typically 2013 being a good example
as we move into more bearish territory
and miners essentially have to wind down
their operations or at least slow their
expansion the bitcoin protocol has time
to get the difficulty back in line and
we see this uptrend in overall mean
block interval so we're seeing that
blocks are starting to come in a little
bit slower it's actually moving it back
towards the target so rather than a
period of expansion where faster blocks
come in here we're looking at slower
blocks and it eventually converges back
to that mean block time
and you can see that we have here's
another example we mentioned this ban in
in may uh 2021 where we had about fifty
percent of the network turn off over the
span of about one to two months it's a
very very fast and rapid change and you
can see here it's historically the
largest change that we've ever seen
now during that brief period of time
blocks really slowed down they were
coming in much much slower because over
that period the difficulty took time to
actually wind down to address where the
new mining hash power was as 52 percent
almost switched off overnight
but you can see how quickly this
actually returned back to its original
trend you can see the difficulty wind
down and the overall hash power even if
there's not more hash power coming
online the block time gets returned back
to its equilibrium of oscillating around
this 600 second interval
now from those we know the complexity of
the puzzle from difficulty and we know
the observed outcome which is the time
stamps and the block interval so from
that we can then estimate the mean hash
rate how much hash rate is required in
order to solve this particular puzzle
when we're observing this result that's
essentially how we calculate hash rate
now with those metrics before
particularly the block interval you can
see it's quite noisy on a day day-to-day
basis that's why we had that blue curve
which is mapping out that 14 day median
so when we look at hashrate it is
advised to put some kind of roughly 14
day moving average or a moving median
because it smooths out that daily noise
and also because it's naturally variable
if you take a single daily data point it
can be misleading so you may see an
all-time high on a daily data point but
in reality that's just a series of
blocks that happen to come in faster
it's a probabilistic process of solving
these blocks
so you can see here with a 14 day simple
moving average it's much much smoother
and we can really see when miners are
starting to switch off their rigs and
bears we can see the expansions during
bull markets we can see this particular
ban here in may 2021 which was quite
significant and you can also see the
significant recovery
so note here that we not only saw all of
the rigs that were switched off in china
they were relocated rehomed some of them
are still there and we've seen those
come back online and we've also seen
additional fleets come to market so you
can see that we actually have had an
expansion of the mining industry we're
going to touch on this
shortly because this is quite important
when assessing revenues and potential
capitulation risks
now why do miners actually apply this
hash power in the first place well
there's two sources of income for them
the first one is the block reward which
is essentially the newly minted coins up
to that cap of 21 million and this also
undergoes the halving we'll explore that
more in a second
the second source of revenue is from
bitcoin fees these are transaction fees
that people are actually spending their
coins moving value around the system and
paying that transaction fee in order to
do so
so here we have plotted out the bitcoin
fees this is the total amount of fees
paid per day in btc and you can see that
generally during more bullish markets we
tend to get these up ticks and
particularly as you can see here in 2017
there was a period of significant spikes
now what this is speaking to is the
urgency people really wanted to get
their transactions confirmed there's
also more people coming into the network
the awareness has expanded we're seeing
that there is more congestion on chain
because block space is a limited
resource there's only so many
transactions that could fit in each
block so if there's more people trying
to get their transactions confirmed than
the system will allow you end up with
congestion and people have to pay a
higher priority fee if they want to get
theirs minded in a near-term block
so we generally see an expansion in
transaction fees during bulls and you
can also see that we see a reduction
during bearish markets we see less
activity there's less attention on the
space and over time
we do see these kind of bull and bear
cycles play into it
now remember that's not the only element
the cycles are certainly part of the mix
but there's also things like
transactional efficiencies so we can see
through the period of 2021 and 2022 we
did have a more depressed market cycle
so that is certainly in play but there
was also an additional upgrade in terms
of adoption of segwit which allows more
transactions per block which is going to
reduce uh overall congestion and there
was also exchanges particularly from
2020 onwards adopting transaction
batching so rather than sending one
transaction per withdrawal they would
send a transaction every 10 minutes or
every hour for example and process all
of those transactions in a single go so
more efficiency in terms of the way that
exchanges in particular are actually
using that block space and they account
for about forty percent of block space
at the at the time of recording
so when we combine the transaction fees
in btc
with the actual block subsidy that's the
reward coming that pushes us towards
that 21 million cap we end up with our
total block reward so there's three
there's two components there's the block
subsidy which is the amount of new coins
that are minted there's the transaction
fees and when you add them together you
get the total block reward
and you can see that over time this has
been gradually descending in btc terms
you can see the halving events here
where we actually cut the block subsidy
in half
you can see that it generally trades at
a fairly stable level this is monitored
by that the difficulty protocol and the
block interval and then each halving we
get this consistent amount of coins
mined per day this will fluctuate more
because we have the transaction fees you
can see here in 2017 we got more of that
income being sourced from transaction
fees and the subsidy but generally we
see these plateaued levels which is
largely driven by that subsidy level
being kept in line that deterministic
curve of the supply as a result of the
difficulty protocol so that's really
keeping things in line and this is why
we can actually predict bitcoin's
overall supply well into the future
now of course miners their costs whether
it be in buying hardware whether it be
in power contracts logistics paying
staff their costs are normally
denominated in fiat currencies so whilst
their reward comes in in btc terms their
actual revenue is actually should be
priced in u.s dollar terms or fiat
currency terms because that's what their
costs are imposed in
now when we actually overlay when we
look so even though we have our total
block reward which is overtime halving
because of the uh because of the halving
events and we also have the transaction
fees which are somewhat cyclical in
nature
in terms of their actual revenue we can
see that if we look at our current
market structure even though we're near
all time lows in terms of btc
denominated revenue you can see that our
usd denominated revenue is much much
higher than it was following the last
halving
so over time minor revenue in dollar
terms has actually been on the ascent
we've seen this through multiple cycles
you can actually see that back here
we've more or less lost that prehistory
because it's essentially insignificant
relative to our current market pricing
so really when we're looking at minus
stress and income levels and where we
are in that cyclical performance it
generally makes a lot more sense to pay
attention to minor revenues in fiat
denomination rather than in you in btc
denomination
so whilst we are seeing that decline
over time minor revenue in fiat
denomination term continues to climb and
this is really that point of reference
for a lot of these metrics we'll look at
moving forward
now because mining the mining cycle is
reliant on the coin price like any
commodity industry that goes through
boom and bust cycles and there is a
process in terms of actually tracking
this and we have tools available such as
the difficulty ribbon
so as i mentioned difficulty will climb
and descend and adjust itself according
to the actual observed block times
now during bearish markets when you see
miners that are actually having to turn
off their rigs what happens is when
miners turn off their rigs the miners
who remain on the network gain their
share of overall hash power
so what happens is that miners who
potentially are over leveraged have over
capitalized they haven't run their
operations as smoothly what we would
classify as weaker miners they will have
to turn off their rigs to conserve power
and essentially stop expending that opex
now the miners who have ma more
efficient or better or cheaper power
contracts or whatever it is that makes
them a more efficient or a stronger
miner
their overall share of the hash rate
will increase so that means that the btc
reward more of that reward is going to
them per day than it was before
so their revenue actually increases on a
relative scale whilst the other miners
are turning off now as those miners turn
off the difficulty will start to adjust
down and we can actually see that the
faster ribbons this is the difficulty
ribbon is just taking moving averages of
difficulty and we have everything
ranging from the
from the 9-day up to the 200 days so the
bluer curves are the fast ones the red
curves of the 200 day and 128 which are
much slower
and as this capitulation takes place the
faster moving averages will descend
below the slower one so let's zoom in on
our last five years and we can really
see this in detail we can see that the
blue curves dive below the red ones this
is showing the difficulty is winding
down and when we get these inversions it
has historically coincided with
capitulation events when we're getting
close to the end of the bear market
miners once they've spent money on their
hardware
generally because that capex has already
been expended they will keep operating
their miners until the operational costs
exceed the revenue so it really comes
down to that power costs and maintaining
the machines running because the capex
has already been spent so they will try
and recover that fund until it is not
even worth it on an operational
standpoint and generally that's after an
extended period of depressed prices and
often at the end of capitulation events
now we can see in march 2020 we actually
had what we would call a double halving
event price halved in the march 2020
covered sell-off so we actually saw
miners have experienced a miniature
capitulation at that point too
and barely a few months later we
actually had the actual halving which
again halved their revenue so we
actually had two capitulations
back-to-back
and then you can see here very clearly
this
may 2021 event where china essentially
banned all mining operations within
their geography and we saw over 52
percent of the hash rate turn off in a
handful of months and this signified a
major capitulation event
now why these capitulations are
important is that miners build up btc
denominated treasuries and when you see
these major costs in cost imposed
whether it be via expansions whether it
be because the overall coin price has
declined they need to sell
more coin to cover the same fiat
denominated costs
and often during the end of these
capitulation cycles they will have to
dip into their treasuries to cover these
costs which increases the amount of cell
side pressure that's coming to the
market they have fixed usd denominated
costs but the price of their income the
actual commodity that they are mining is
losing value so they must sell more of
it to cover the same costs
so just before we finish up just wanted
to introduce you to some of the mining
metrics we have under a glass node
advanced plan which really try to take
this to the next level and show you even
more insight into what's going on
so we can look at things like the
difficulty ribbon compression this is
really taking that difficulty ribbon
concept that we looked at and mapping it
out into an oscillator where we can see
when we enter these periods of mining
stress it's actually mapping out where
those moving averages are really
reaching that point of capitulation
we can also look at a metric like the
minor revenue per exah this is where
we're looking at an individual miner or
miners as a whole looking at what their
revenue is in comparison to the entire
market so in other words we can look at
how much revenue is coming in per extra
hash on the network and from this we can
start to calculate things like the
average cost to mine a bitcoin we can
pull out more information both at a
macro level but also at an individual
minor level
we have oscillators like the pure
multiple which maps out the average
minor income over the compared to its
yearly average and you can see that this
tends to fluctuate between extremes of
very very low values during minor
capitulation when their incomes are very
very stressed and all the way up to very
high values when miners are in extreme
amounts of profit and that's typically
around cycle top so you can see we can
develop these cyclical oscillators that
also takes into account the halving
events
and then we have the mining pulse which
is one of these metrics it's actually
quite interesting it's mapping out that
concept of faster and slower blocks and
we can much more easily see these
periods of minor capitulation where we
have these large slowdowns in block
times and we can see when we get large
expansions in the mining hash rate when
we're seeing more miners coming online
and mining at a faster rate
and lastly we have the hash ribbon which
is very similar to the difficulty ribbon
but really looks at it from a hash rate
perspective and you can see in these
areas marked in red this is where we get
an inversion of the hash ribbon where we
actually see that the faster moving
average cuts down below the slower one
and this typically signifies that miners
are entering that period of income
stress and when we combine that with
things like the pure multiple or the
mining pulse or any of the other metrics
we've looked at we can really start to
get confluence for when the miners are
under serious stress and again this
typically comes towards the end of bear
markets
so thanks for tuning in for this session
hopefully you found this useful as a bit
of an overview of the mining
fundamentals hopefully you learned
something new about how these different
mining metrics come together into a
single cohesive piece and we are going
to explore the concept of mining metrics
and how we can really track this in even
more detail and look for various
expansions versus revenue declines we
will look at this in future videos to
really explore this in even more detail
so until the next one i'll see you then
cheers
you

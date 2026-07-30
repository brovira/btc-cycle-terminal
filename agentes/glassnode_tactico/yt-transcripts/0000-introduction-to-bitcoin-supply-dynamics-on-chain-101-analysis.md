# Introduction to Bitcoin Supply Dynamics (On-chain 101 Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=3OQVG56B6K4
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-introduction-to-bitcoin-supply-dynamics-on-chain-101-analysis.md]`.

---

hello everyone and welcome to your glass
dirt on chain 101 where this week we're
focusing on a very important topic which
is an introduction to bitcoin supply
dynamics
now this concept of supply dynamics is
actually one of these big picture
concepts that underpins a great deal of
on-chain analytics what we're trying to
do is assess the macro flow of funds
holding times across the network
whereabouts the supply is held and
really diving into all levels of
granularity on what is going on with
supply and demand
now as i mentioned on-chain analysis
really helps us observe the holding
patterns the spending patterns the flows
of funds we can watch coins as they move
throughout the network and see as they
move between different entities they
come into the miners through issuance
they're then transferred to exchanges
and they move around the system between
investors different entities financial
institutions and the like
so what we're really going to do in this
session is start very very simple this
is very much an introductory course and
we're going to look at the circulating
supply issuance and inflation starting
very very simple where do these coins
come from and what does it mean
we're then going to start to assess
things like economic metrics inflation
rates stock to flow we'll look at
holding patterns what's going on in
terms of investors who've held their
coins for one year and those who've held
them for less than one year what the
cyclicality of that means
and then we're going to introduce at the
very end a net position change metric
this is a concept that you'll see in a
number of glass node tools and there is
a sister video to this which looks at
how we actually build this in workbench
so i will point you to that later on and
you'll find it in the description below
but for now let's get started
so as i mentioned in the introduction
we're going to start with a fairly
simple concept and really give you a bit
of a bit of an insight into what supply
dynamics is all about
now one of the really important
components that we have to build in and
we can use within the supply dynamics is
the concept of time
now every coin in the system is
contained within a utxo or an unspent
transaction output think about it like
container the nearest equivalent is like
a 50 bill that 50 bill contains 50 worth
of value
so a utxo contains a certain amount of
btc value and we can actually tell which
block it was last moved in so we can see
the transaction output we can see where
that coin was last mined on the
blockchain and if we then look at the
timestamp between when it was mined into
a block and the current period we can
assess the holding time
so what we can see here is the
circulating supply in orange this is
obviously the total supply cap and you
can see these halving events where it
kinks and then we start to trend up
towards that 21 million hard cap which
will happen somewhere in the era of year
2140 so some time left to go
now bringing that concept of time into
the mix this red curve here maps out the
proportion of that supply in btc that is
older than one year so coins that have
not moved for over one year now there's
going to be satoshi's coins down here in
this early phase
we can also see that as we start to move
to the
2013-14-15 cycle this is where bitcoin
markets were starting to develop very
very early but we can see that we
started to move into this more cyclical
behavior we've got these peaks in these
older coins and then as we move into the
2016-17 bull we have a major decline we
see that we get this spending behavior
the population of coins that are older
than one year starts to decline and
these are when people are actually
spending them and taking profits in the
bull
as we move into the 2018 bear market you
can see that this actually starts to
reverse again we get this uptrend in
these older coins
now what's going on here is we're seeing
a transition of wealth people are
actually buying and sticking those coins
away in colder storage for the long term
we're seeing a growing amount of coins
coming out of circulation going into
wallets where they're remaining in a
dormant state
now where are these coins coming from
well if we look at circulating supply
and we subtract the coins that are older
than one year in red then we're left
with the opposite which is the coins
that are younger than one year and we
see this in blue
and you can see how these two
essentially oscillate inverse to each
other by design
so when we're getting these periods take
the 2015 late stage bear market note how
late in the bear we see this massive
explosion these coins are older than one
year these are people who've bought all
the way down kept them in their wallet
and those coins are now starting to
mature
and note here how the coins younger than
one year start to really decline and
they eventually this is essentially
where those coins are coming from
long-term investors people with a very
long time horizon who believe in what
bitcoin really is they are accumulating
coins taking them off the market and
that means that there are less coins
that are mobile and active and actively
traded and this eventually creates
somewhat of a supply squeeze we combine
this with the halving event that happens
in the circulating supply so miners stop
reduc stop issuing as much coins into
the market and we start to get this
cyclical behavior where young coins
explode during the bull this is the
maximum number of brand new people
they've heard about bitcoin from their
friend they heard about it on the tv
they come in and historically speaking
they tend to buy near the top of these
markets so we get a massive swelling up
of these younger coins a minimum in
terms of older coins this shows that the
smarter money who bought in the bear
have essentially exited the system and
the cycle tends to repeat
so you can see that with a very very
simple metric of supply last active one
year we can actually start to build
dynamic supply and demand models and
look at the cyclicality of coins moving
throughout the system
now as i noted supply last active is
really one of these important metrics
and not only can we look at it at the
one-year-old basis but we can also we'll
look at this at the end of the video
expand this to many other age brackets
so we can actually see how this behaves
across multiple age categories
now what we can see here this is the
supply last active one year metric and
this actually plots it out in terms of
percent so we can see the percent of the
supply that is older than a certain age
and we can see here that during the
early years of 20s 2011 and 2012 we
oscillated around 30
and you can see that over time we've
seen this gradual increase
in the overall supply last active at the
top of the 2016 market we had some 60 of
the circulating supply that was held in
these one-year-old wallets and you can
see that more or less as the bull market
started prices started to appreciate and
particularly when we broke past the
previous all-time high you can see that
the spending behavior this is the
opposite this is not accumulation this
is distribution those people who bought
all the way through this bear and built
up this supply actually start spending
into the bull and you can see that the
intensity of the bull run actually was
met equal and opposite by the intensity
of the amount of spending
these older hands are essentially
liquidating their coins and taking
profits now eventually the amount of
coins being sold creates an oversupply
and the market tends to saturate there's
simply not enough buyers and we revert
back into a bearish market
now note that some distance after the
all-time high once the bear market has
set in things have started to equalize
the dust has settled a little bit and
also those buyers who still have that
long-term time horizon see that there
are now coins that are trading at a much
cheaper discount to the all-time high
and it's at this point in time that they
start to accumulate before we can
actually see them in this metric
remember spending is instantaneous you
will get a decline in this the second
that a coin is mined into a block that
has gone from one year or two year or
five years to zero so spending is
instantaneous we can see this during
bull markets and particularly powerful
for looking at when markets are starting
to get a bit overvalued you can see all
of this spending happening in near real
time
as we move into more bearish markets we
actually have to wait for that one year
period of time before we start to see
this metric react because a coin that
was purchased a year ago won't reach
that maturity for 12 months so you can
see that this starts to climb following
at some point in the middle of the bear
when that yearly mark has passed you can
see it continues to accelerate
now later in this course we're going to
look at things like the hollow ways
where we map it out beyond just the one
year and we can actually see coins
moving from one day to one week to one
month to three months and then
eventually getting to that one year so
we can see a more granular view of how
coins are moving through that system
but you can see how the cyclicality of
this this particular asset you can see
the supply moving through the system you
can see periods of maximum hotel where
the most number of people hold their
coins nice and tight put them away to
cold storage and you can see that
spending behavior that typically happens
during bull markets and how that cycles
through time
now obviously these coins have to come
from somewhere we can look at what's
called issuance this is essentially the
amount of coins that are being mined
into the supply to the miners
now this is obviously a daily a fairly
noisy metric we're going to cover in the
next tutorial the mining fundamentals it
explains a bit more as to why this is
actually a noisy metric we see that it
actually oscillates quite a bit
day-to-day because we don't have a
uniform amount of hash power on the
network we also don't have a uniform
number of blocks being mined but you can
clearly see these halving events where
we get this reduction of 50 of the
issuance so every four years or 210 000
blocks we get a halving event with
bitcoin so what happens is it goes from
50 50 btc per block and approximately
144 blocks per day 50 btc per block it
then drops down to 25 and then we get
another four year period until it drops
down to
12 and a half and we're currently in a
regime where we're sitting at 6.25 btc
per block
now interestingly with every halving
event there's another mine's 50 so every
four years it mines 50 of the remaining
coins that were left so not only is it
reducing the issuance per block by 50
percent but it also over that four year
period will absorb some will mint some
fifty percent of the remaining coins so
if there's two million coins left over
the next four year period it will mint
one million of them this is this
interesting characteristic that the
halving event actually has installed
but you can see here that we've applied
this 14 day simple moving average really
just to smooth it out so you can really
see where the supply is at any
particular point in time and understand
how much of those coins are actually
coming into the supply and in in later
sessions we can actually look at how
much the miners are then releasing to
the market how much they're hodling so
we can then build even more detail
bottles of supply and demand
now over time as that halving event
occurs what we call the inflation rate
or the amount of supply that's coming
into circulation relative to the
existing circulating supply will
decrease
so you can see that our inflation rate
in orange here continues to decline over
time so much the same with the harvings
we get more or less a halving of the
inflation rate each cycle
now note also that there is a gradual
decline that's because over the course
of that four year period before the next
halving this circulating supply is
increasing we have approximately the
same number of coins coming into
circulation but they're they're diluting
a much much larger and increasingly
large pool of circulating supply so over
time we still get these downwards
gradients as the inflation rate
continues to drop and bitcoin is
programmatically designed so we can
actually estimate what the inflation
rate will be at any point into the
future and as i said it will take about
another 118 years by the year 2140
to mine those final coins and eventually
the inflation rate will essentially
trend towards a level of zero
now if we take the inverse of the
inflation rate we get a model called the
stock to flow metric now what this is
essentially showing us is the stock is
the amount of circulating supply divided
by the flow which is the annualized
amount of coins coming into circulation
now there's actually an easier way to
conceptualize this you can see how it
moves opposite to inflation rate what
this is actually modeling let's say here
we've got a value of 20. this means it
would take 20 years of bitcoin issuing
at its current rate at this point here
it will take 20 years to recreate the
circulating supply
now as we know every four years we get a
halving of that event so this is why
bitcoin essentially that scarcity layer
comes in because yes we may require 20
years at this particular issuance rate
but we know that in four years time it's
going to be half that and you can see
how the stock to flow ratio continues to
climb
now for reference the gold stock to flow
ratio is somewhere around the era of 60
to 80 depending on how you measure it
whether you include jewelry and various
other investment bars and gold but what
we're looking at here is a bitcoin stock
to flow ratio of somewhere between 55
and 60 on any particular day
now that means that after the next
halving that stock to flow ratio is more
or less going to double up to the 100 to
120 range within daily fluctuations and
that will in fact put bitcoin as a more
scarce asset by this metric in relative
to gold and this will be the first time
that gold has actually experienced a
flipping so to speak um within this
particular metric but that's the way to
think about this dr flow is describing
how many years will it take at the
current issuance rate to recreate the
circulating supply
now the last section i want to look at
is kind of bringing a lot of these
concepts together and i will direct you
to a video that we've created that
actually explores how to build this
particular metric this is one that we
built in workbench and we do have a
guide that shows you how to actually
model this and build this up but what
we've essentially mapped out here is
what we call a net position change
metric and you'll see this show up in a
number of glass node tools because it
really shows us that 30-day change of
any particular metric it's a common tool
we can use to really assess the flow of
funds
so as we mentioned those longer-term
investors are going to be accumulating
bitcoin during bear markets this is one
of these patterns that we see and they
generally start to liquidate during bull
markets
so what this blue curve here is showing
positive numbers are essentially showing
when those long-term investors are
adding coins to their balance over the
last 30 days
now and the negative values that we can
see here are when they're actually
distributing those when they're getting
that spending behavior going on
and you can see let's take the 2017
market for example
as we rally into the all-time high note
how we get very very large negative
numbers now remember negative numbers
mean spending and spending is
instantaneous we see this immediately
there's no time lag between the spending
and a coin going from from one year or
two years to zero days
on the hotlink side of the equation it's
a more delayed reaction so we tend to
have to look for sustained periods where
we're getting this increasing supply
moving into these one-year cohorts
so what we're trying to track here is
when we're getting these impulses of
buyers these impulses of sellers to
really help us gauge where we are in
that market cycle and you can see
through our 2021 period we had a
significant amount of spending into the
january peak we then had a softening
through that market high and really
since we got to around november the
all-time high this is where we really
started to see this peaking higher now
remember that's one year delayed so
these buyers here these these coins that
were accumulated during this period are
actually from that 2020 initial rally so
we're seeing a huge number of those
coins remain within that hoddled state
from that first impulse of the 2021 bull
cycle
now moving into some glass node advanced
metrics tools that we have access to
that really provide that even deeper
level of granularity for how we can
assess supply dynamics
we have over here our wrapped bitcoin
chart now we can consider things like
etfs or exchange traded products the
grayscale premium we can see when we get
these pools of capital where bitcoin is
actually held within some other asset in
this instance we're looking at the
wrapped bitcoin contract on the ethereum
blockchain so we can see how much btc is
actually being deployed into various d5
protocols so we can look at this on an
entity basis whether it's grayscale
whether it's an etf we can also look at
it in terms of smart contracts of where
those funds of funds are flowing on
different blockchains
over here we have our 90 coin days
destroyed what this is looking at is the
sum of the amount of coin day
destructions this is introduced in that
concept of lifespan we mentioned when
old coins are spent we generally get
these peaks in these older coins
spending profiles this is showing that
their coins are coming back to life and
we can typically see that these happen
around market peaks when we actually get
this explosion of old coins being spent
which creates that oversupply so we can
start to track out the cyclical behavior
looking at coin data structure
we can look at our net realized profit
and loss this introduces not only the
time stamping but also the price
stamping of these coins we can see when
they're spent are they realizing a
profit here in green or are they
realizing losses in red and what we
typically see here is that these will
occur during bull market peaks you get
this large amount of profits being taken
during bear market lows you see large
periods of losses these are capitulation
events and they typically stand out from
the rest
we then have our accumulation trend
score this is a metric that essentially
looks over the last 30 days is a large
portion of the market adding to their
balance we typically see this at bull
market peaks on the way up but also
during capitulation events on the way
down march 2020 and during our current
bear market sell-off we can see that we
get these large periods of buy-side this
shows that there's bull market strength
but also shows when the tides may be
turning towards the lows
and we can also see these yellow colors
these are periods of distribution when
overall on chain entities appear to be
relinquishing coins from their balance
and we get a genuine slowdown in the
amount of accumulation that's going on
so it really does trend between the zero
and one to show us when we have
aggregate distribution or aggregate
accumulation
and lastly as i mentioned and one of my
personal favorite metrics is the hollow
waves and this is where we can map out
different parts of the coin supply at
different age brackets to see how it
moves through the supply process we can
see when coins are purchased and there's
an impulse of these younger coins we can
see as they mature up through the
different age brackets and generally
speaking the older the coin is the more
likely it is to stay put and this really
helps us understand more granularly
what's going on at the supply dynamics
level
so thanks for tuning in for this session
i do hope you learned something new i do
recommend checking out our workbench
tutorial which shows us how we actually
built that net position change metric
you will find that that's a very
powerful tool and once you understand
how to build something like that in
workbench the amount of options that are
opened up to you expands even further
there are many more things you can do
with this toolset to really take your
analysis to the next level so i look
forward to seeing you in the next
session and i'll see you then
cheers

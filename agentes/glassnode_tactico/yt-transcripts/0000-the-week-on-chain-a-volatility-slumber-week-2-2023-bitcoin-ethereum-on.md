# The Week On-chain: A Volatility Slumber - Week 2, 2023 (Bitcoin + Ethereum On-chain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=m5oo9b8Tsr4
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-the-week-on-chain-a-volatility-slumber-week-2-2023-bitcoin-ethereum-on.md]`.

---

foreign
and happy New Year welcome to 2023
um we've come into 2023 in a pretty
quiet and boring fashion to be perfectly
honest uh what we're going to be
covering today is how the digital asset
Market really went to sleep over the
break and uh I for one and not too mad
because it actually gave me a bit of
time to rest recharge and rethink about
what's going on in the space so what
we're going to talk about today is a
very very quiet patch of volatility and
this is both in the markets so the
pricing but also on the change
themselves it was a very very quiet
December historically quiet in fact and
really we generally see these events
proceed fairly explosive moves so it
looks like 2023 is setting up to be uh
pretty wild Straight Out The Gate
so as I mentioned it opened up the New
Year in a very very quiet manner we're
going to be looking at a very very low
level of volatility and some of the
metrics we can do to actually explain
and track these and also look for
periods of time using workbench to
identify where we've seen similar levels
of volatility we've got some really
clever functions in here that can really
help with the the visualization of these
events we're going to look at the very
quiet on-chan activity for both Bitcoin
and ethereum both chains are very very
quiet at this point in time across
almost all angles so we're going to
explore that from a few different places
and we're also going to look at the
collapse of volume especially when they
relate to 10 million dollar Plus Sizes
these are institutional whale sized
Capital flows and there's some very
interesting Dynamics going on that we'll
explore in a bit of detail
and what we'll close that with is a
drawdown in the realized cap and I want
to spend a bit of time explaining what
the realize cap is why it's such a
powerful metric and also exploring a a
new implementation or a concept that we
can use to probably better track
dominance Within These markets really
based on the realized cap and taking out
some of the challenges that we see with
market cap based calculations
so just before we get started and as
usual please do give us a rate of
sharing a subscribe it really does help
this Channel and for the new year if I
could really ask you just to let me know
in the comments a few things if there's
particular topics or ideas or concepts
you want more depth or more explanation
on please do let me know in the comments
what you're looking for so I can really
help you understand more about it and
bonus points if you do happen to have a
glass note subscription whether a user
on the free plan or you have a paid plan
letting me know that as well really
gives me a lot of insight because what
I'm trying to do in this season me and
my team are really going to try and
expand more content especially for folks
who are paying attention which if you're
watching these videos generally speaking
you are so what we're looking for is
just a bit more insight to understand
how you guys are using the platform what
topics and Concepts you need a little
bit more detail explained on because
that really helps us tailor the content
to make sure that you're getting the
maximum value and that we're focusing in
the right place to help you out so
please do let me know those I do read
all the comments so uh please let me
know and let's get stuck into the
analysis
okay here we are in our week two
dashboard for the week on chain and as
you can see almost just visually from
looking at this price chart this is all
nice and volatile up down up down up
down and then stable coin now quite
remarkably Bitcoin has essentially been
trading within if you can believe it
since the 17th of December within about
a 550 range this is just 3.4 percent for
just shy of a month it really is quite
remarkable and there are very few
instances in history where Bitcoin and
any digital asset really goes to sleep
to this level
um on a volatility framework so really
it's been a very very quiet break we do
actually see this over Christmas breaks
generally uh at the end of the year
markets tend to go a lot quieter not
just in digital assets but traditional
markets as well and clearly Bitcoin and
ethereum were no exception in this
instance
now what we have here are two really
interesting workbench charts now for
anybody who's really in the weeds
actually playing around with these
charts um you can always open up using a
little magnifying glass you can actually
see these within workbench so you'll
find a description to this dashboard or
a link to this dashboard in the
description below and you can always
open up these charts to actually inspect
how we've built them look at the
different functions that we're using now
what we're looking at here is this light
blue curve is mapping out the current
value of the orange and the Orange is
looking at the monthly volatility how
volatile has Bitcoin been how volatile
has ethereum been so what we're doing is
we're looking at the current value of
that and then we've used an if then
statement to highlight for Bitcoin in
blue and for ethereum in Orange periods
of time where the volatility was less
than our current level and as you can
see there really aren't many instances
now for Bitcoin back here in 2015 this
was all it was quite volatile on a
intraday basis right we're seeing the
market still recovering from the bear
Market we get these Peaks and then 50
pullbacks but generally speaking it goes
quite quiet before very significant
moves
back here in November 2018 for both
Bitcoin and for ethereum price was
trading in to this Apex of this triangle
and then we saw over the course of one
month I was here for both the sell-off
and the rally here in April this cut the
whole price in half the whole Market
fell by over 50 in just one month and
conversely here in April 2019 April
Fool's Day actually we were essentially
traded from 4 000 up to fourteen
thousand in a matter of about three
months so generally speaking low
volatility precedes High volatility and
as we can see here it can actually trade
in both directions so it's almost a
little bit about put the seat belt on
because there are historical examples of
it going both ways and you can also see
following the covert collapse we had a
bit of a recovery the market went pretty
quiet and we actually then had the
2020-21 bull market so as you can see it
generally precedes High volatility moves
with examples in both Direction
now moving into the on chain space we're
going to start with Bitcoin then we'll
jump over to ethereum and what we're
looking at here is a fairly quiet and
somewhat lackluster on-chain activity
space
so this first metric is called new
address momentum and what we care about
here is how active is the network we're
looking all the new addresses coming in
on chain and what we really care about
here is not the absolute value but where
is the yearly average in blue relative
to the monthly average
positive momentum means our monthly is
above our yearly and negative momentum
is the other way around and what this is
just telling us is do we have the
monthly activity that's currently
happening is it growing relative to the
yearly so you can see back here in 2018
we actually got a nice break back above
and it actually remained there even
though price was a little bit bearish
through 2019 and 2020 we still had
growing momentum the monthly activity
still exceeded the yearly and that
actually was indicating that there was a
bit more momentum it wasn't this super
bearish character that we had through
2018 and super bearish character we had
through 20 uh 2021 so you can see that
after our collapse here in May 2021
we've been trying to recover and we've
only recently had a burst back above
that yearly average now that was
actually triggered by FTX so you almost
have to wait and give it a bit of time
to see whether this can actually sustain
momentum do we get a bit of a 2019 style
grind higher or does this actually fail
and fall lower so in both of those
instances it's telling us something
about the momentum of the on-chain
activity and that's really a bit of a
proxy for what's going in terms of
demand and the user base
now on a very similar vein we have our
revenue from fees this is a statistical
model it will be blue when there's
basically no free pressure and it will
be red when lots of people are bidding
for Block space get my transaction
confirmed and there's urgency imposed
within that so at the moment you can see
it's fairly lackluster we had a very
very small uptick during the FTX
collapse but it's essentially gone back
to basically no fee pressure so this
model is a great one to look for when we
actually get that uptick and we start to
see that fee pressure building this will
start to move back into the red zone as
it stands at the moment it's pretty
quiet and we can essentially deduce if
there's very little fee pressure at the
moment
now on the transaction volume this is
looking at on a USD basis how much USD
value is flowing through the network you
can see we here's the bull market and
FTX collapses and this thing
is basically in free fall it has fallen
from somewhere in the order of 65 or 66
billion dollars per day and we are
currently down here about 5.8 billion
dollars per day so a very very dramatic
decline pretty much immediately
following well there was a bit of a
decline leading into but definitely
following the FTX collapse a major
washout now what I want to do is quickly
jump over to another chart
now this particular model is in our
professional package and what we're
looking at here is the breakdown of
transaction size as it relates to the
amount of volume right so we're looking
at 10 million dollar plus transactions
is in this dark blue down the bottom
here that's what we're going to focus on
in a moment we've got our 1 million to
10 million 100 000 to 1 million and so
and so forth but what you can really see
is that the 10 million plus has a very
very similar profile to our change
adjusted volume we were just looking at
note particularly the collapse from
about 42 and a half percent dominance
through most of 2021 and 2022 and we've
seen it collapse down to about 19 so
more than cut in half the overall
transaction volume associated with these
10 million dollar plus entities now
there's kind of two key interpretations
that I would take away from that the
first one is there's probably been a
shaking of confidence but also just some
serious losses sustained by institutions
they've seen what happened over the last
year and there is a probably a bit of
less willingness there's been a shake
taking confidence so those institutions
are going to have to go through a whole
process of of re-understanding what's
going on with this uh this asset space
and how it fits into their portfolios
the other one as we've now found out and
as more things come to light and again
this is a bit of a gray area there was a
lot of transaction volume going on that
was associated with the FTX Alameda
entity and it is likely that a
reasonable chunk of this had something
to do with them so since that entity is
more or less out of the picture we've
seen a flushing out of that volume and
it's in a way probably returning to some
kind of a more natural and realistic
Baseline but again all of these things
take a lot more analysis but they're
kind of the two big takeaways that I
certainly sense are leading to eat to
this collapse in whale volume in
particular but more specifically a very
very significant decline in overall
transaction volume
so what we're looking at here is the
exchange inflow and outflow volumes for
BTC and eth obviously BTC and orange eth
is in blue and inflow volumes to
exchanges is on the top side and
outflows are on the bottom side now
generally speaking we see a fairly
evenly matched inflow versus outflow
there's obviously a net position that's
slightly different between these two but
generally speaking we see if there's a
billion dollars flowing in of Bitcoin
there's somewhere around a billion
dollars flowing out on any one
particular day they're generally fairly
well matched
now what I want to really highlight here
is how similar the pattern between 2017
this is the irrational exuberance we
come into the top there's a whole lot of
transaction and trade volume note also
ethereum peaked following BTC BTC was
the first one to put the market high in
and transaction activity for ethereum
peaked after the top had already been
established and here we are back in 2020
2021 we had the same effect Bitcoin
peaked and then we had the explosive
volume come in for ethereum following
that now following both of these events
you see a significant decline an overall
compression transaction volume start to
fall you see less and less exchange
activity this is again getting us into
that very quiet on-chan activity space
quiet volatility the market goes into a
bit of a sleep but generally speaking
that precedes some kind of move down the
line
now the other Insight from this is the
purple line now this is looking at the
essentially the ethereum dominance let's
look at all the transaction volume that
we can see on this screen and what we're
going to do is say how much of that is
represented by the ethereum chain now as
you can see through most of 2020 and
2019 this was hovering somewhere between
around 20 25
now since the bull market came in in
2020 and 2021 and particularly as we
came into May 2021 this has really
established a higher Plateau so we're
oscillating somewhere between around 38
and 45 of all exchange activity has is
ethereum relative to ethereum plus
Bitcoin so we're only looking at the two
majors here but it does show there's
been a bit of a structural change in the
overall Market liquidity and really the
market is treating both of these as the
two major assets within this space
um and you know it's just one of those
interesting market dynamics that we can
start to observe over time so it
represents not quite half but it is
getting close you can certainly see the
dominant of the blue relative to the
orange has expanded over the course of
the last couple of years
now moving on to the ethereum side so
Bitcoin is not the only chain that's
seeing a very very quiet on-chan
activity space we have much the same
going on on the ethereum Chain so on the
right hand side we can look at the mean
transactional this is the mean gas price
paid we are down at very very low cycle
lows the last time we saw this was July
2021 after we had our first major peak
in sell-off and then back here before
the bull market in 2020 so following the
covert collapse so very very light
on-chan activity there's not a great
deal of sectors that are really booming
at the moment on the left hand side
we're looking at the actual gas
consumption broken down to different
transaction types and the one that I
really want to highlight most whether
it's D5 stable coins are quite stable
strangely enough in terms of the amount
of gas consumption some are around 12
percent if I remember correctly defy and
bridges and Mev all of these that
generally tend to Peak during bull
markets they've actually been in a
fairly long term decline really since
around August 2021 we've seen a decline
in all of these different sectors the
one that really was consuming much of
that and exploding in the in overall
activity was the orange which is nft
trading volume so we're seeing that nfts
really entered the scene July August
September of 2021 they maintained
somewhere around 25 to 35 percent gas
consumption we saw a significant decline
down to around 20 percent
um somewhere around November 2022 and
following the FTX collapse and the kind
of dust all settling nfts over recent
weeks have seen an expansion back up to
around 38 dominance so what we're seeing
is that most sectors are actually seeing
less activity during this bear the only
exception to that and only in recent
weeks has actually been the nft space
which is staying to pick up a little bit
more of that volume so just again one of
these interesting structural Dynamics
that's occurring within the on-chain
space
now the last topic that I want to touch
on is the realize cap so for those who
aren't familiar the realized cap is one
of the most important and fundamental uh
building blocks within the on-chain
analysis discipline now there are some
challenges that we have with market cap
the problem with market cap is it values
satoshi's coins which are long lost as
well as all the other lost coins it
values those coins at the spot price now
that's a little bit disingenuous because
if Satoshi was to move and sell those
coins it's very unlikely that spot price
is going to stick around for very long
likewise there's other projects and a
great example of this unfortunately was
the ftt token and many of the tokens
that were kind of within that FTX orbit
there was a lot of tokens that were
vested or remained with uh with the
founding teams but were never actually
circulating
so what that means is that a very small
proportion of the token Supply can
maintain what would be argued to be an
inflated market cap so when we're
looking at things like market cap
dominance or relative valuation valuing
all of those tokens that may not
actually be liquid and circulating like
satoshi's coins or like a a protocols
treasury or these coins that just aren't
really part of the circulating supplies
a little bit can lead to some well as we
saw on with the fgx disaster people over
value these tokens and then loans get
issued against them and it can create
some havoc in the market
so what the realized cap does the
concept behind the realize cap is it
will only value every individual coin at
the price when it last transacted so
it's not perfect but what it's doing
there is it's picking up all those coins
that we saw flowing in and out of
exchanges they're going to get
constantly revalued at the current spot
price let's imagine a world where
Satoshi does wake up and spend his coins
they're going to go from a realized
price of zero to a realized price of
whatever the current price is so what
we're doing is getting a bit more of a
true transacted volume weighted average
of price
so it also reflects the cost basis what
we're doing is we're looking at what is
the price at which these coins
transacted if we make a you know higher
level assumption and we can look at
realized cap from a few different lenses
but if we look at the realized cap just
as a very simple assumption it's the
last price they transacted let's assume
that that's the cost base or the cost of
acquisition because for every seller
there's a buyer so you're getting this
this transaction this cost basis type
effect so it shows the real Capital
inflows if a coin was acquired at 10 000
and then sold at 50 000 that transaction
is going to revalue the coin higher
someone else had to come in with forty
thousand dollars to buy that coin
conversely when you see coins go from 50
000 down to well 16 000 that Delta
between the acquisition and the sale
price is a realized loss so when you
aggregate all this together you both get
a discounting of lost or unvested tokens
you get a tool that tries to volume
weight where the cost basis is for the
market and and the end result is a more
accurate tool to compare assets
so these two charts are looking on the
left obviously a Bitcoin on the right at
ethereum you can see the realized cap
goes through these almost stair stepping
patterns there's a few insights we can
take from this generally this stair
stepping happens during bull market so
if you can guess why that's because all
the folks who are buying coins down here
in the bear Market are selling for a
profit and those coins are going from
five thousand six thousand three
thousand up to fifty thousand forty
thousand thirty thousand sixty thousand
so the value of those coins those the
transaction prices going up people are
realizing profits now during a bear
market we've got here the all-time high
in blue you can see this pullback in the
overall realize cat these are people who
bought it 50 000 and sold at 40 30 20
16. so what we're seeing is the overall
net change in the market valuation
so you can also see here in the red
we've got our drawdown and you can see
here where we are at the moment this is
18.8 percent for Bitcoin
um it is the second largest drawdown of
the realized cap in history you can
really only compare it back here to the
2011 market and for any of you who've
watched been watching these videos for a
while you know I generally don't pay too
much attention to that early cycle it
was just too different to where we
currently are so in a way in terms of
modern history this is the worst bear
market we've ever seen in terms of the
overall realized losses the drawdown of
capital from the peak has been
significant now the other Insight I want
you to take away is note that the
realize cap has essentially erased all
of the gains that were made on the
second pump right the second rally that
we saw up to the November October
all-time high has been completely
flushed out all the profits that were
taken during that period have been
completely flushed out so in a way it
kind of reflects a capital reset we've
seen that flushing out of the excesses
and all of that extra speculation
Capital that came in on that second
rally we've essentially flushed all of
that back out and now we're probably
approaching something closer to a more
fundamentally driven valuation
now when we look at ethereum we haven't
quite got the largest drawdown in
history but it's still one it's 25 or
29.2 percent of the realized cap has
drawn down it's not quite as bad as we
saw here in 2018 2019
um but it's you know it's still pretty
significant it's much larger than we had
back here in 2016 but same thing let's
not uh compare too much to the old days
now the last thing I want to touch on as
we've established that the realized cap
is probably a superior metric for
comparing assets this is just a very
simple implementation of looking at
market cap or sorry market dominance
you'll often see that Bitcoin dominance
metric and the challenge with the
Bitcoin dominance metric is it's got all
of the pitfalls of market cap that we
discussed earlier all of the tokens and
all of the assets that may not really be
fairly valued and that includes Bitcoin
satoshi's coins and unmoved coins from
the ethereum Ico all of these illiquid
coins it's not really fair to Value them
at the spot price because it's not a
it's not a real representation of value
and capital flow
so what this model is doing when we're
up at higher levels it's showing that
there is more realized value flowing
into Bitcoin and conversely when it's at
lower levels we're seeing more realized
value flowing into ethereum now this is
just looking at the two major assets but
this same concept can be applied to all
sorts of things and if you were to run
this particular model with a larger and
increasingly large basket you will start
to see a bit more of an accurate
representation of what's going on when
it comes to true market dominance and
where importantly the capital is Flowing
not so much what the price is telling us
at the moment but more so whereas the
true structural long-term capital flows
moving around the space
now there are some limitations with it
if you're looking at privacy tokens for
example we can't measure the transaction
uh how many coins were moved and when so
you can't apply the same heuristics so
there are some limitations to this model
but at the very least just having an
appreciation for the realized price then
the realized cap and what it really
means relative to the market cap will
give you a lot of insight when it comes
to one chain analytics it really is a
powerful tool it's a foundational
element and it really sets you up to
understand more about what's really
going on in this space
so thank you for tuning in for that
session I hope you did have a very
refreshing break over the new year I am
looking forward to this series it's
going to be a really fun one there's
going to be lots of interesting topics
who knows what the Market's going to
hold in front of us um and just a quick
reminder if you do get a chance please
do leave some comments on the topics and
the ideas and the things you want to
hear about this year if there's anything
you're unclear on you can always ask
questions and as I said any information
about whether you're a Glasgow member
and how you're actually finding things
where I can best help you understand
your Edge is really going to go a long
way and help me shape this uh shape this
season so until the next one I will see
you then cheers

# One Bitcoin On-chain Metric to Rule Them All: Mastering the Realized Cap Part 1

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=-xFi-VJlotM
**Publicado:** 20230801 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20230801-one-bitcoin-on-chain-metric-to-rule-them-all-mastering-the-realized-ca.md]`.

---

foreign
video report for week 31 2023
now last week when we're looking at
Wales that was some pretty heavy
on-chain analytics right we really went
down some pretty you know a lot of those
tools are very nuanced very new pretty
heavy stuff so today we're actually
going to pair it back a bit and have a
bit of a break we're going to be looking
at what I think is the most important
metric in all of on-chain analytics and
that is the realized cap and this may
sound a bit fundamental right people
like oh I know what the relays cap is
well I guarantee you that you don't know
how far this Rabbit Hole goes because I
am still exploring it and really when we
look at all of the on-chained space I
cannot even begin to tell you how much
value is either a direct derivative of
or an idea that comes from the realized
cap it is one of the most powerful tools
in the entire discipline and getting a
good grasp of it really is the first
step to kind of elevating your on-chain
Analytics
so the relays cap it was actually
spawned back in 2018 uh coinmetrics was
the first company that kind of came up
with it and what it relies on is just an
absolutely genius concept of price
stamping for every utxo within the
entire Bitcoin chain what we do is that
whenever it moves on chain we assign a
price stamp to it so what that means
that we can look at the price when a
coin was moved and then we can compare
that to when it is spent and suddenly we
can start saying well we can actually
discount all of satoshi's coins which
were moved at zero dollars even though
there's a million of them they're not
worth anything on a realized sense
likewise the person who transacted
yesterday has a cost basis of 29 500 and
whoever transacted back in November 2021
has a cost base of 69 000 so what we
really look at here is what is the cost
basis for every coin and because it
represents that cost basis it's also
going to capture the capital that flows
in or out of this space because big in
order for a coin to move somebody has to
make a very conscious decision to move
it
now on a micro scale right on an
individual level sure you may have
bought your coin at you know 29 000 you
withdrew it at 30 but on the aggregate
it is remarkably clean it's one of these
things where there's error bars on every
single transaction but those error bars
kind of cancel each other out when you
look across the entire network and Time
After Time and as you'll see today cycle
after cycle we get these patterns that
are just so elegant and so repeatable
that we can start to really find signal
out of it so we're really going to go a
bit just a bit of an exploration we are
only going to scratch the surface of
what you can do with a realized cap this
is something I'm spending a lot more
time focusing on so uh there will be
follow-up series
um this is really a bit of a primer to
get you in the mood and understanding
why this metric is so important so let's
get started
so here we are starting with the humble
realized cat so as we discussed before
the realized cap is essentially that the
value the cumulative value of every coin
at the price when it moved now why does
this matter well you can see this kind
of this stair stepping pattern
immediately right it goes vertical
during bull markets and then it goes
sideways to down during bear markets
much like the price chart you can see
that the early history just doesn't
exist we will zoom on this in a second
there's a lot going on down here it just
gets compressed to nothingness and
requires a log scale to view now what's
really happening here is that during
uptrends coins that were required in the
bear Market are revalued to higher
prices the smart money who buys the
bottom sells the top so you can see here
that when this really starts to escalate
in 2021 is as we break the previous
cycle twenty thousand dollar all-time
high so what you see is that this is
coins being sold coins acquired cheap
and sold at a higher price going from an
eight thousand dollar cost basis to a
fifty thousand dollar cost base or a
sixty thousand cost basis
now the exact opposite happens during a
bear market during a bear Market the guy
who bought his coins at 69 000 sells
them at thirty thousand he took a thirty
thousand dollar hit times whatever the
coin volume is um that he was holding
right so you can see here that
immediately the shape of the realized
cap has a piece of information and we'll
explore this later on we can see that it
kind of has these two modes it's got
kind of vertical upwards and then it's
got down to sideways let's actually get
rid of our recent Market cycle and we'll
start just showing you how the detail
kind of expands you can see that now
that we're kind of zoomed in on our
previous Market Cycles it looks very
much the same we have our vertical
plateau in the 2017 Peak note that the
relays cap really plateaus pretty early
in the bear Market when that selling
stops it's usually over right the price
up here was at uh 17 000 when the relays
cap started smoothing out so again you
can already see there's signal in all of
this and you can also see the recovery
right the recovery in 2019 right this
all period you can see March 2020 was
nothing in the amount of realized losses
compared to what we had back here kind
of gives you that confidence that this
thing really does want to keep trending
higher let's zoom in on our even earlier
cycles and as you can expect you see all
of the same behaviors right you can go
down to all levels of granularity so
let's uh let's move on but that is the
relays cap in a nutshell
now the realize cap has two components
that when summed together actually gives
you the realized cat there's what we
call the thermo cap down here in blue
now this represents about 50 billion of
the 570 billion the realize Cap's 570
the thermocap is 50 and that represents
all of the coins that are mined priced
at the time when they are mine so it's
kind of like the initial time stamp that
gets put on those coins
now once a minus spends it it moves into
the green curve which is the investor
cap this is essentially looking at all
of the coins beyond their initial Mining
and look and they will transact I'll
move around multiple times if a coin is
never spent it will always stay within
the thermocat
um generally speaking miners now don't
lose coins very often but in the early
days there's lots of coins back here
that never left the thermo cap they
remain in there and they've never been
spent since
now the final takeaway from this is note
that for that 50 billion dollars that
means that the largest majority
contributor to the realize cap is the
investor cap the other way to think
about that the coins that are
transacting on the open market that
unless you're a miner they're probably
the only coins you'll ever see or uh or
transact with those are the ones that
dominate the realized cap the miners are
actually a very small component and I'm
doing a lot more research to really
describe just how small the mining
component really is but on a macro scale
it's 50 billion out of the 570 and
that's about nine percent if memory
serves so most of the coins we're
talking about are those transacting and
moving around the system
now this just puts in order we're going
to break that down one step further
here's our little thermocat right here's
our realize cap in Black that's kind of
the target goal and the investor cap is
here in blue right so you can see if you
added this Blue Zone down the bottom
here to our investor cap you would have
the realize cat now the investor cap is
now where we're going to dive into
because it itself has two components and
these two components are so important to
understand these are the Bedrock of
on-chain analysis if you can understand
these Concepts your entire analysis will
be elevated to just a new tier
realized the investor cap is the
component of realized profits so all of
the coins that were moved and then moved
at a higher price that's a profit that
gets locked in minus the realized losses
here in the red
so if you take all of the profits that
have ever been locked in by the system
and you subtract all of the losses right
normally the profits happen in Bull
markets and then you take away the
losses that happen in a bear and you add
these together you get the investor cut
now what you can see is that the total
amount of realized losses is actually
larger than the realize cap is and the
profits are even larger than that so on
net the Bitcoin Market is net profitable
right because we have a lot more profit
that when we subtract the loss we still
have a non-trivial sum right 300 and
sorry I think it's about 570 billion at
the time of a time of recording so that
kind of puts things into a bit of
perspective that it's actually all about
that profit and that loss
but don't just think about profit and
loss in terms of profit and loss what
does it mean for the investor well you
may have experienced this how many times
have you told your friend about I mean
aside from a funny story how many times
have you gone and raved about how much
money you lost in the market very very
infrequently but how many friends do you
know who've told you about how much
money they made buying X Y or Z
prophets are what brings people into
these markets losses tend to happen
during the most catastrophic bear
markets and that is where stocks move
back towards their rightful owners it is
where the hodlers come in and put a
floor under Bitcoin despite all of the
Doom so really that profit and loss is
both a financial position and
understanding positioning is super
powerful it's essentially what we're
doing here we're trying to track where
the money is Flowing around the system
but also tracking the losses and the
magnitude of them helps us understand
when people get flushed out and when
it's only the hodlers that remain these
two things work in Tandem and they tell
us a lot of information which we'll
continue to dive into
so we'll start with realized profit so
again these are coins that were acquired
at a cheap price let's just say in the
previous cycle at eight thousand or six
thousand or four thousand and you can
see the enormous spike in realized
profit occurs during a bull market and
note when it accelerates is pretty much
breaking the previous all-time high
other metrics that will start changing
their behavior when you break the
all-time high long-term holder Supply
starts declining coins older than one
year starts declining what does that
tell you the smart money who acquired
and held their coins through the chaos
of the bear they start to distribute
their coins in the bull and you can see
that the realized cap Rises and rallies
as those profits are taken you can see
here on our second rally we had in 2021
we had another burst of profit but
here's a piece just another piece of
information we needed less profit to put
in an equal High that's a big bearish
Divergence less profit was required to
be taken in order to establish a roughly
equal higher in terms of price so it's
telling you that this is kind of like an
exit liquidity type event right and much
like our previous chart you can
obviously zoom in and see all of the
microstructure right this obviously
scales with market cap but you can zoom
in and see all of the profit taking that
went on in each market cycle right the
maximum profits are taken typically at
the cycle top
so now let's bring in our realized loss
component now remember realized loss is
essentially that component that only
shows up in the bear markets now whilst
our profits was kind of like a big
parabolic run and then once it's done
it's done
notice that relays losses take a lot
longer they're kind of spread out over
the entire period of the bear and you
can see there's typically a series of
capitulation events you can see how
angry 2021 and 22 was by the way we had
the first sell-off the first major
uptick in losses after a parabolic bull
market right here's our May 2021 that's
telling you that something isn't right
this is what we call the shot across the
bow it's that first major sell-off that
people go oh that was different that
wasn't a correction that felt different
and the smart money at that point in
time is essentially taking the Final
Exit liquidity so typically that first
major sell-off is kind of the scary
moment where bear Market sentiment
starts and by my read in 2021 that was
the May 2021 that's when the bear Market
on a sentiment standpoint even though we
hit an all-time high later the bear
Market sentiment had started in May 2021
and it was signified by this enormous
explosion in realized losses
you can also see the capitulation events
you can see when three arrows and Luna
blew up you can see when FTX happened
but note also that price was going lower
in the back half of 2022 but the
realized losses were getting smaller and
smaller and smaller
the same way that I realized profit less
profit higher high bearish Divergence
less loss lower price that's a
constructive Divergence that's getting
to the point when people have been
flushed out the losses that were going
to be taken have been taken it starts to
look like seller exhaustion and again
you can spot this all through these
different metrics but really you can see
how profit and loss they work in tandem
they offset each other to create the
realized cap but at the end of the day
these two components are what drives the
human beings behind those decisions the
profit and the loss is our emotive
decision we choose to spend our coin for
a profit we choose to capitulate because
we cannot deal with the pain any further
and these are the things that drive
markets and that's why getting ahead
around these things is so important
now this is looking at the drawdown of
realize cat now what you'll notice is
that in in the market cap sense we go
down 92 back here in 2012 I think it was
85 back here in 2015 it was 85 again
um in 2018 and then we did 75 here in
2022. now the realized cap pulls down
much less we're talking about 23 14 you
know 16 I think the worst case scenario
we had back here 23 so we're talking
about roughly you know something on the
order of a quarter sometimes less than a
quarter of the market cap now why does
this drawdown matter well if somebody
bought that coin at 50 000 and sells it
at 20 they took a thirty thousand dollar
loss right times the coin value
if they take a thirty thousand dollar
loss that's capital leaving the market
they invested 50 and they only got back
20. that capital's gone it's destroyed
um so what you're seeing there is that
that transfer the the drawdowns and the
realized losses on net that's capital
outflow from the industry so whilst
Bitcoin Drew Down 85 75 92 percent the
amount of actual Capital that left the
market and left the asset is much closer
to 20 or 18 or 14 so we actually don't
see the same level of dramatic outflows
even though the price goes down that
much now for those who are kind of
thinking there's another study which I'm
not going to cover here but
the realize cap is a view of how much
capital is coming in True Market Capital
coins on an exchange we don't really
care because until they get withdrawn
the human decision to say I'm going to
sell this coin or I'm going to send this
to an exchange it doesn't exist they're
one button away from hitting buy or sell
so to me just ignore it and in many of
these metrics particularly our entity
adjusted variants which you'll find in
our professional plan all of those will
remove the exchange activity which
cleans up the data a lot but what we're
looking at is until a coin comes out of
the exchange we're not even going to
worry about it it's not it's just kind
of sitting there on the exchange it
hasn't had that human decision getting
printed onto it yet and even with that
constraint these things still they tell
such a there's such a large subset of
coins off exchanges I think it's about
88 or thereabouts last I checked so that
kind of volume is still very significant
and we still get all of the human
behavior baked into it but really this
is telling you about capital outflows
seeing these drawdowns
so what we're now going to do because as
you saw with many of those previous
charts they were looking at it in USD
and as we know with the price with
market cap with realize cap you can't
really see what happened back in 2012 it
just disappears into the miss
what we're looking at here is everything
priced in BTC the profit and loss in BTC
now what this does is it normalizes
across all of the Cycles because we're
removing the coin price and we're only
looking at how much Bitcoin volume was
realized in profit or loss and you can
immediately start to see some really
interesting cycle patterns there's a
certain threshold that we hit when the
profit is simply too large remember this
is the counter-intuitive thing about
Bitcoin markets when people are taking
profits
that is the thing that eventually puts a
top in because the profits get taken at
the local tops all the way up to the
global top until it oversaturates demand
and that's what literally creates the
bear you over saturate with too many
coins coming back into circulation
there's not enough demand it gets
overwhelmed so ironically enough the
period of Maximum profit is actually the
top and likewise the period of Maximum
capitulation these massive red spikes
here this is historically where we see
these capitulations these complete flush
outs of everyone who is going to sell is
done they're out so what we're seeing
here is these major events and you can
use this to help understand where we are
in the cycle right now where we are
today you can see it's very very small
right there's we've seen the
capitulation of FTX we saw it after
lunar in three arrows and we're kind of
pretty quiet at this point in time
one more take away from this you can see
this little blue line here this is
issuance
so think about this as daily profit
taking daily loss taking and daily
issuance all on the same axis BTC volume
what you can see is in the early in the
early years of Bitcoin right 50 BTC per
block 25 pretty much to the second
halving
maybe not at the bull market Peaks and
the bear Market bottoms but through most
of the rest of the cycle issuance was
meaningful it was roughly equal to
profit and loss therefore the mining had
a very significant impact on what's
going on in the space
if we look at it today you have to
squint to see it now when we're very
quiet and there's not much going on like
where we currently are issuance has a
larger impact but during the full Bull
and the full Bear Mining does absolutely
nothing because most of the value is the
coins that are already in circulation so
we've talked you know this is one of
these topics that um it takes a bit of
thinking about but really the profit and
the loss particularly today drives the
vast majority of the momentum the actual
people transacting with the existing
Supply taking profits trading hodling
all of this behavior taking L's this is
what drives the market the issuance is a
very small component by comparison
changes obviously as the market goes
from quiet to booming or to chaos but
generally speaking the issuance is a
small component just kind of puts things
into scale and perspective
now another way to visualize this is by
what percent change well how much did
the realized cap change on a percent
basis
um which again percentages are really
nice to normalize things
um here I've just visualized those
losses and profits um obviously in two
different axes and coming from top and
bottom but again a really nice tool to
just help spot periods of extreme and
those extremes typically correlate with
cycle transitions so positive changes
you can see happen during a bull and
they Crescendo near tops note that
profit collapses to nothing very soon
after it goes stagnant until 2019.
there's like a whole year where nobody
was making any money right it was all
dominated by losses and you can see the
capitulation event stands out like a
sore thumb right which then leads into
the 2019 rally so these extremes and
these kind of patterns of behavior on
net shows us the Dynamics of the market
it helps us visualize inflection points
major topping signal major bottoming
signals how the market is behaving based
on the value flowing in or out the
profits and the loss the changes in the
realized cap that's really the dynamic
that we're tracking here
and again we've really owned we've
barely strayed from the realized cap and
again this is just scratching the
surface the derivatives of where you can
take profit and loss which is a whole
nother video
um where you can take those components
into cohorts um you look at it from Long
Term short term you look at it into sopa
you can do all sorts of magic with it
these are just exploring kind of the
most fun foundational principles of what
goes into the realized cap
so just to kind of close out I want to
touch on a couple of applications
um touching a couple of very popular
metrics and just really explain why
they're so useful and they're all pretty
much direct ascendants uh or some
derivative of the realized cap just kind
of showing you how pivotal it is now the
mvrv is I mean it's one of the the best
metrics it's just a fantastic oscillator
and it is essentially because the
realize cap is the cost basis we're
taking the ratio between MV market value
and RV realized value it's basically
looking at what's the current price
divided by the average cost basis right
and if you think about that that is an
unrealized profit or loss multiple how
in the money is the market or how out of
the money is the market now I won't
spend too much time on the mvrv because
we have a whole paper which you'll find
in the description below called
mastering the mvrv aside from the
realized cap that is the paper that you
want to assess and actually have a read
of because that is the quintessential
on-chain tool this is a good example of
just a very simple cycle indicator when
it's above its 100-day moving average
typically we're in an uptrend but here's
the most important thing here's the
Nuance of why this thing is so special
at the top what did we see on the
realized profits everyone sells the
smart money that is
but who are they selling to well they're
selling to top buyers what happens when
all of those coins now have a cost basis
of 20 000 or 65 000 right or back here
was 14 1400. what happens when all of
those coins now have a very high cost
basis while price goes from 20 to 6 and
look how devastating this is the
unrealized profit everyone's on the moon
having a fantastic time
and they just absolutely collapse the
profitability of the system gets wiped
out and remember going back to the first
thing I said in this this session how
many times have you gone and bragged
about how much money you lost in a
market very very infrequently so this
event this top heavy market and this
collapse of mvrv you can see it in every
previous cycle these dramatic drops
these bearish divergences we cover all
this in the in the research paper that
is the thing that creates that big spike
of realized loss it's what shifts bear
Market sentiment it's what get everybody
on the other side of the boat it scares
people and that's scare that loss that
unrealized
um uh you know basically seeing all
those red candles that is what creates
the bear Market sentiment and that
Echoes for the next two sometimes three
years but essentially that's what the uh
this metric is tracking and the exact
opposite happens at the bottom coins get
distributed to the lows people
capitulate massive realized losses
there's no sellers left you get seller
exhaustion and all those coins suddenly
return to a very Swift realized profit
that is what creates the next Market
structure so the MVR is super powerful
but it all comes back to that very
simple concept where were those profit
and loss taken
now the realize cap Hollow waves this
thing is one of my favorite metrics I
use it all the time it's very similar to
the hollow waves but if you look at the
traditional Hollow waves there's a big
purple bulb up here that's satoshi's in
the early miners right coins that are
older than 10 years old so on a BTC
basis there's 1.4 million coins that
haven't moved since 2010.
but they were moved at zero dollars they
have no realized value so do they really
matter not well that meant they do if
they get spent but if they get spent
this metric will auto correct what you
can see here is that our 10 year old
coins have no value our seven to ten
year old coins have no value right these
are very five to seven is only barely
getting just the tiniest little bit of
value because they were moved at dollars
cents ten dollars at most so when we're
looking back over this period of time
these coins have a very very small
amount of the value in the market
what happens at bull market tops well
the smart money with old green coins
sells them to new buyers who heard about
Bitcoin on the on the news or because
their friend told them they were getting
rich
this big red bulb here is top buyers a
swelling of value held by coins that
recently transacted this is the
signature of the top buyers what is the
signature of the hodlers a swelling out
of all of the older coin bands this is
the people who are buying in the bear
they hold for one month three month six
month one year two years they don't care
about the price these are people who
huddle and they put their coins away and
they're waiting for the next cycle so
you can actually visualize and see these
Cycles I will often use a binary system
I'll either look at coins you know maybe
six months or three months is my
threshold I'll turn all the coins off
older than that or all the coins off
that are younger than that and then I
can see what are the old money doing and
what are the new money doing because a
coin can only be old or young it can't
be both so it's a really nice way to
just frame this up
now another very popular metric and this
is the second last one as we get towards
the end of this this is the net
unrealized profit and loss often called
nupal and this particular metric it's
it's basically a derivative of the
relays cap it is the marker cap minus
the realized cap and think about what
that is how much what's the spot price
minus the cost basis as a proportion of
the market cap and what's really nice
about this it just helps us visualize
the Cycles right and obviously it's
color coded for easy understanding but
when we get into these real extremes
right Market tops typically speaking if
every man in his dog is in profit
that's usually a good sign that things
are starting to get pretty frothy and
pretty overheated in many ways this is
just another way to visualize the market
cycle that everybody knows about when
they when they kind of enter markets and
typically you've got to go through one
cycle yourself to kind of experience it
but all that's that Mark of psychology
is all baked into the amount of profit
or loss held within the coin Supply
massive losses create Sellers and
eventually they exhaust sellers massive
profits also create sellers but they
also create a lot of buyers right
they're on the wrong side of that trade
and that is essentially how these
structures tend to go
now closing out with that very same
topic and this is just a kind of a final
note to show you that this is just the
surface of this rabbit hole
this is our noopul just shown in a
different format you can see here when
it when it was red here it's actually
just negative under zero
well we can also break this down by when
did you acquire your coins we can look
at for example the short term holders
this is that hot ball of money that's
following the price within the last five
months that's kind of that red zone of
the realized Capital waves they're
always following the price we can
calculate all sorts of things like their
cost basis and all that fun stuff but
notice that the short-term holders at
the bottom they capitulate first they
are the first ones to bail out of the
system they're also the last ones to buy
the top the short-term holders typically
speaking are the ones on the far extreme
of the market to be a short-term holder
at the bottom means that you were the
you bought like a couple of months ago
and it just it's the dip that keeps on
dipping and eventually you go I'm done
I'm out I hate this thing I'm finished
so short-term holders typically at cycle
extremes are the kind of speculators who
are following the price
well then we've got the hodlers the
long-term holders now their profit and
loss is a much more kind of cyclical
manner but note how much they get
destroyed in the bear what happens is
the bear markets are typically like 12
to 24 months long but in the first year
there's a bunch of people who bought the
top and they still think the bull
Market's going to continue and they keep
buying and they keep buying and then
finally the price absolutely nukes and
they all go underwater so suddenly
you've got this Market where everyone's
underwater no one's in profit people are
just there's capitulation happening all
over the place
we can actually map this out and look
for that point of Maximum pain
show me the areas right which is what
this chart's about to do show me all of
the areas where the whole Market in
Orange the short-term holders in red and
the long-term holders are all underwater
absolutely everybody no matter when you
bought your coins is underwater on their
Holdings
not a bad way to start visualizing when
things are at the maximum extreme
so now you can overlay look at the
realized loss at this point in time look
at the relays cat percent change all the
metric the drawdowns all the metrics be
covered helps us describe a market low
well then we can look it on the other
side and we're going to use a bit of
Statistics here
show me when at least one of those nupal
charts for the market for the short-term
holders or the long-term holders show me
when it's above one standard deviation
of its long-term mean right show me when
we're getting statistically out of band
for at least one of them I don't care
which one just at least one of them
that's what these yellow zones are
showing us now that's not half bad right
we're starting to get local Peaks we're
starting to get cycle Peaks but it's
really telling us it's pretty hot
through most of the bull market right
2013 is a bit of an exception this thing
here managed to pick up both but it's a
bit of a broad base
so now let's go one step deeper show me
when two of those models are above their
one standard deviation band now this is
not rocket science right one standard
deviation is just a very simple way to
kind of frame things up and you can see
that like we can start really piecing
the puzzle together and what we're just
simply looking for here is when is the
market
really really in profit and as we saw
before when the market is really in
profit more people start to take them
and when more people start to take them
our realize profit climbs our realized
cap goes vertical and there's a bunch of
top buyers who heard about Bitcoin on
the news who just bought their first
coin which by the way that was me back
here in 2018 I was that guy
and then you'd get the bear Market that
follows so you can start seeing these
Market Cycles they're all derivatives of
people making decisions and those
decisions are typically based on profit
and loss it's kind of that fundamental
factor that drives all markets here we
just happen to be able to see it and
visualize it in full color
so thanks for tuning in for that session
folks hope I mean let me know there's a
bit of a longer one I can see here going
about just over half an hour but as you
can see I love this metric I think it's
a really powerful tool there's a huge
amount of value we have only barely
scratched the surface there's so many
charts that come off this but really
coming to terms with what the realize
cap is why it matters why it's so
important this is essentially the Crux
if you can get your head around this all
the world of on-chain analysis will
become infinitely easier because at the
end of the day so much of it boils down
to and distills down to the realized cap
it is essentially an amalgamation of all
the profit all the loss all the
decisions all the wins all the losses
everything that's happened in bitcoin's
transaction history
is all backed into this one metric and
it's a really really great tool and you
can see all of these Rivers have come
out of it so anyway hopefully you
enjoyed that please let me know in the
comments if you enjoyed this kind of
more fundamental type content
um and there will be more because I love
looking at this stuff anyway so that's
what's going to happen and I'll see you
in the next one cheers

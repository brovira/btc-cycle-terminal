# The Fall of the FTX Empire - Glassnode Onchain Analysis

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=Q1A3ehEg2yU
**Publicado:** 20221110 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20221110-the-fall-of-the-ftx-empire-glassnode-onchain-analysis.md]`.

---

foreign
report where we are going to be covering
the fall of the FTX Empire
now this is a obviously a very
significant and quite dramatic event
that's happened in the industry
um it isn't good and what I really want
to do is just explore some of the
details but we've certainly found our
data science team has been doing a lot
of work trying to understand what's been
going on understanding the flow of funds
between FTX and Alameda and binance and
really I just want to give you a bit of
an update on essentially what we found
to date just give you a bit of an
overview so you understand what's going
on some of the mechanics about what's
happening now look this is obviously
going to be an evolving story it is
going to change and and things will be
different you know almost hour by hour
at the moment so this is a bit of a read
at the moment and what we're going to
skip all the intro stuff I'm going to
get straight into the analysis just so I
can get this out so you can really just
see what's been going on because I know
that times like this can be very
challenging I hope that you're all okay
this can be a really really difficult
time Bitcoin bear markets are
unforgiving so if you do have any
questions or queries please do reach us
in the comments it's more than happy to
answer those as they come through anyway
let's get stuck into the analysis
okay so we're going to go through really
three different topics here the first
thing we're going to look at is a bit
about the relationship between Alameda
FTX and binance just understanding the
flow of funds so you can kind of see the
scale of this thing I'm just going to
talk through the data obviously we still
have to wait for what the true details
look like but at the moment it it
doesn't look overly good we're then
going to look at token balances and just
understand what happened during the
event in terms of the actual flow of
funds and kind of the State of Affairs
and then we're going to close out by
looking at the Bitcoin side of the
equation and try and assess exactly what
Bitcoin is doing given the chaos and
again this thing will evolve over the
course of the weekend and there will be
more of an update on the week on chain
we'll really explore this in much more
detail so what we're looking at here up
the top and we did put out a tweet
thread um from this from glass node
you'll find that in the in the
description below
on the left hand side here we're looking
at the token flows in USD denomination
from Alameda so Alameda has a wallet um
let's let's just consider that there's
three entities in this equation there's
alamater there's FTX and there's binance
and we're essentially looking for the
flow of funds between those entities and
comparing it to all the other entities
that coins are flowing around to so this
left hand side chart is a relative chart
so from zero to 100 of all of the funds
that are flowing out of elevators
wallets where are they going and as you
can see it maintains and this is about a
year of data going back to pretty much
the market all-time high 8th of November
uh 2021 so we're really looking at one
year of data for all these charts we can
see that 90 of all transaction activity
from Alameda was going into FTX nine
percent of it was going into binance so
what we can really see is there is that
there's there's a flow of funds from
Alameda towards FTX and it is the
dominant proportion of what they're
actually sending right so a very very
snippet and then one percent you can see
all these tiny sections at the top here
about one percent was going elsewhere
now when we look at the inflow patterns
into FTX now we're only looking here at
coins that are flowing from known
entities we're not talking about
individual deposits this is Alameda and
various other exchanges much the same
story this is a cumulative sum of all of
the tokens that were flowing from
Alameda now just for reference these are
tokens excluding Ethan BTC we'll explore
those more in more detail shortly this
is looking at everything from stable
coins to ftt tokens and really they're
the dominant format so really we're
looking at tokens here excluding the two
majors Ethan BTC
now over the course of the last year
Alameda 2 FTX accounted for 49 billion
dollars worth of token inflows and as
you can see is the vast vast majority so
um in terms of inter exchange there's
very little transfer volume on a
relative basis going from binance to FDX
from bitfinex from coinbase from Kraken
from kucoin Alameda into fgx was by far
and away the largest depositor
um of these known entities right so
we're removing all the the individuals
here what we're looking at is
institutions and um into into exchange
transfer so what this really tells us
here is that there is a bit of a flow of
funds where Alameda sits in between the
flow of funds
um essentially depositing to FDX so
coming out of binance into FDX
now if we look at the makeup of
alameda's wallet that's what this chart
here is looking at in general we can
essentially I mean it typically hovered
around 200 million dollars you can see
that it starts decline as we got into
the the late last couple of months
um and you can see all the activity that
was going on earlier on that really
starts to decline now the token maker of
alameda's wallet was what we would
generally consider to be the higher
quality collateral stable coins or
various forms usdc tether dye
um and ethereum and wbtc so for the
ethereum wallet of Alameda it was
primarily using relatively liquid
capital and the vast majority of this
was stable coin so really what we're
starting to describe here is a flow of
funds of stable coins from binance to
Alameda from Alameda to FTX this was
kind of that flow and then there was
obviously flows going in both directions
here
if we look at the token flows into
elevators wallets we can see that about
15.5 billion dollars came from binance
to Alameda and 7.1 went from FTX to
elevator and you can see that both of
these areas are quite significant you
can see that they had operations in
other exchanges
um where they were withdrawing funds
from other trades but you can really see
here that there's a strategy being
played Alameda was essentially using
binance and FTX as their primary venues
they were a dominant depositor to FTX
itself a much smaller relative to
binance because bonuses obviously a much
much larger exchange but really what
we're seeing here is the elevator was
almost a middleman between these two
exchanges when running their strategies
um if we look at the token outflows from
FTX this is where is ftx's funds going
again that same logic we're looking at
the named entities here you can see that
36 of those flows went to binance so
you're starting to see a bit of a circle
here coins go from FTX to binance they
get withdrawn through alamater and then
back into FDX and there's this flow of
funds obviously it goes the other
direction as well but FTX 2 alimeter was
then 38 of the funds so the funds coming
out of FTX were going primarily to
binance and alamator at almost a equal
split between the two and then you can
see that there's the other entities that
we were looking at before that were
captured in the flows from Alameda so
these are essentially funds coming out
of those institutions into Alameda
highly likely to then be going back into
FTX
um but what we're looking at here is
that FTX would then send those funds
back to those other exchanges so you
could start to see these Loops
um playing out so when we actually break
this down what does it mean it will
really suggest that Alameda has been in
between many many transfers on the order
of several billion dollars between
binance and FTX as being this kind of
flow of funds and also their various
other exchanges it really highlights
that these were the two primary venues
for Alameda and sadly it's increasingly
looking like Alameda and FTX were let's
just say misbehaving and potentially
misappropriating funds that appears to
be what the the state of play is it's
certainly what the data would tend to
suggest what I don't want to do is kind
of postulate too much and speculate
because we do have to wait for just the
reality of this thing to come out so
really what we're seeing here is there's
in terms of just the sheer Capital
moving between these entities there is a
very clear a relationship that looks
like a kind of a circular flow of funds
that appears to be some form of trading
strategy but it really just shows the
scale of how I guess integral or
connected the FTX and the elevator
entities really are or were because it's
the right word at this point in time
so now let's move on and look at
stablecoin BTC ethereum balances on the
two exchanges on the left hand side I
have binance charts on the right hand
side FTX really just so we can kind of
explore the Delta between these two
because obviously you know one's in a
very different position to the other so
in terms of stable coins the red curve
here is the aggregator top four so
um uh dye usdt usdc and
um
and tether so when we combine all of
these things together
um the top four oh sorry binance USD we
can essentially see that this here this
red curve for binance is more or less
just been in a steady steady Ascent
right it keeps climbing you can also see
here tethering usdc losing dominance
recently and B USD picking up this is
how binance is now essentially moving
towards a busd standard on their
exchange now if we compare that to the
stablecoin balance on FTX it was
hovering up here about 700 to 800
million dollars for some time right for
most of this consolidation range we've
been in and it's essentially at zero it
has seen a complete and total collapse
down to zero
um you know this is this is the bank run
this is essentially what we saw we saw
everybody rush to the exits
um and now we're in a position where it
is set where it essentially looks like
I'm CZ and binance will not be stepping
into to save FTX
um so it essentially is a it's a bank
run and you know the status of how that
plays out over coming years probably is
is remains to be seen
um in terms of net flows you know we're
talking about on the order of several
hundred million dollars uh moving in and
out each day and you can see that FTX
has seen a massive massive outflow right
very very significant outflows of
overall funds
um now we can move on to ftt BTC and eth
which is where things get a bit
interesting and what I might just
quickly do is scroll back up here and
just highlight this 4.2 billion dollars
worth of tokens on the 28th of September
from Alameda into FTX now for those who
are aware the ftt token was kind of the
the linchpin in this whole thing that
started the implosion because there was
a large amount of Leverage applied on
top of that essentially elevator and FTX
that balance sheets were you know
essentially heavily levered towards the
the value of the ftt token so on the
28th of September we saw here's that
same point we saw an extraordinary
amount 74 000 up to 250 000 ftt tokens
so essentially that that 4.2 billion
dollar inflow was essentially Alameda
sending a stack of ftt
um into their FTX uh balance now whether
this was for collaterals or what
whatever is going on it's you know it's
it's obviously a lot of money to be
moving around 4.2 billion dollars in a
single transaction that's that's
significant stuff and then on the left
hand side here you can see binance this
is essentially where binance moved there
um their sum of tokens 39 uh 39 million
uh um tokens in total um on their
balance
um up from 1.1 so a very very
significant sum I think
um uh binance themselves had about 30
million ftt tokens that they transferred
onto uh onto their exchange and as you
can see that was essentially what really
catalyzed
um all of the events of the last 48
hours uh which have happened so we can
really see that there was something
wrong as far back here with FTX in in
late September
um you know there was something in terms
of moving uh these these tokens around
and trying to re-shore things so it's
you know we could say that this thing
has obviously had uh it's got some
history to it
if we look at our BTC balance right
here's binance which you know by and
large is largely unaffected we've seen
somewhat of an inflow over recent days
uh it looks like about 30 000 BTC has
flowed in now again this is not the most
bizarre thing you can say this is kind
of well within range so this doesn't
really look like a mass panic yet even
though price is pretty nasty
um we will be monitoring this and just
seeing how this plays out over coming
weeks FTX on the other hand this you can
see has been in a macro Decline and what
I would just highlight here is that
right after Luna sold off note how
significantly the balance impairment
really was so again here in September we
saw this ftt flow in following Luna we
started to see a massive decline in
overall BTC on those balances it starts
to speak to perhaps there was actually
balance sheet impairment between the FTX
Alameda entity as far back as the lunar
collapse and we know that that I mean
that wiped out a very very significant
portion of capital took a lot of of
people by surprise as many of these
events have this year sadly and you know
this this is kind of the the state of
play so it looks like there was some
some damage done back then and it may
well have been all kind of baked into
the cake by that point in time and we
just really are finding out about it now
which tends to be how Financial
um you know Financial collapses tend to
happen they come out months later the
damage gets done and it takes time for
it to echo through the system and sadly
it's likely
um that this collapse of FTX and Alameda
we will also have some duration ahead of
us of extreme uncertainty where we have
to wait and see how this all plays out
and who is affected
um looking at eighth balances you can
see for uh for binance it's much the
same right they're fairly stable in
terms of their overall exchange balance
has been very little change over recent
weeks um it's kind of flatlining here
fgx basically gone to zero so their
balance has essentially gone to zero on
stable coins on BTC on eth it's the
definition of a bank run it's
essentially been a uh you know get in
there and people have taken whatever
they could get out
um and uh you know it is a very sad
scenario but it's also the it's the
market that's in front of us so you know
we'll try and assess it as it goes but
uh you can clearly see that you know
it's not the healthiest looking chart
so now I want to just pivot and have a
look at essentially what's the impact
right what's what's happened well first
thing is that our drawdown is uh is back
down to a over 70 73
um down from the top we're now down into
March 2020 levels um it's you know it's
it's obviously not great
um this is this is this is kind of how
these things play out and uh the market
is just in a very a very serious period
of uncertainty doesn't know what is the
contagion effect how far does this go
um you know we will find out but uh this
chart here I think is actually quite
interesting now you will find this chart
we've recently rolled out on our new
dashboards in the exchange section
you'll find this chart what this is
looking at is if we start on the 1st of
January on every year let's look at all
of the exchange withdrawals and let's
just imagine that's the cost basis right
all the dollar cost averages and buyers
and sellers you can do this for deposits
as well and they generally come out more
or less the same so for all intents and
purposes this gives us a good enough
view what we're looking at here is
basically the class of 2017 class of
2018 2019 if you started let's just
imagine a dollar cost average regime on
the 1st of January 2017 and did it all
the way up to now what would your
average cost basis be that's what these
curves are showing now there's a few
insights here at the bottom we've got
the all time right now it's hovering
much much lower it's down here around uh
10 800. now what you can see is the
class of 2017 plus this blue of here is
about fourteen thousand nine hundred so
at the time of recording we're about
fifteen thousand seven hundred so oh
um you know we do have this uh all of
2017 onwards
um uh cost base is down here just under
15 grand now that's essentially saying
that only if you've been here since 2017
and Beyond and before are you in profit
it's tough but uh you know if you're
essentially a dollar cost averager
um we lost the 2018 level at 18 500 this
green curve
um the uh the class of 2019 has
essentially been resistance up here at
22 000 until very recently
um class of 2020 is up here at 27 000.
uh class of 2022 is actually
outperforming class 2021 uh also pretty
tough
um they're currently sitting up here so
class 2022 is it's uh 29 000 and 2021's
at 39. so I mean this is a this is this
is serious pain and uh if you've been
here for a while I've been through
several of these bear markets before
um I'm certainly no uh I'm no stranger
to being under the cost basis and uh you
know this this is essentially what uh
Max Payne capitulation type levels look
like right people have been here for
five years
um still underwater on their position so
you know this Bitcoin can be uh can be
pretty cruel at times
um but you know it's uh this is why it's
designed to be resilient because it will
live to fight another day
now this here is the adjusted percent
Supply in profit so what we're doing
here is trying to remove the coins that
are older than seven years let's just
take them out of the picture because you
know once they're older than seven years
it's it's pretty unlikely they're going
to get spent and if they are spent this
metric will self-adjust
so the blue curve is just our base level
percent Supply and profit now what
you'll notice if you look at this chart
is it typically bottoms out around you
know 45 50 thereabouts but if we
actually take out those lost coins you
know satoshi's coins I don't
particularly care the satoshi's coins
are in profit it's not really useful
information to me if he spends them okay
he spends them and then we can readjust
this metrical auto adjust but for now I
know he's in profit and I don't
particularly care because it's not
relevant in terms of the market dynamics
so this metric has broken down to a new
cycle low we are down here at 31 of
Supply in profit this is below March
2020 by some margin actually 37 so an
additional uh what is that about six
percent of Supply we are at the worst
level we were in 2018.
um we've done a report as far back as
June um but you'll find in our insights
page called a bear of historic
proportions and in that report we
essentially came to the conclusion that
the sell-off down to 17.5 K back in June
made this the worst bear Market in
history this metric here is essentially
telling us that uh We've essentially
gone over and above
um we have dotted the t's crossed the
eyes and uh put a star of excellence on
this bear Market as being the most
horrific
um from pretty much every angle so even
though we're not even at the lowest
drawdown percent it doesn't really
matter because a percentage is just a
percentage the amount of value lost and
value destroyed and coins in that just
underwater by an enormous margins it
just blows everything else out of the
water so you know by any reasonable time
weighted volume weighted metric
um this is the worst bear Market that
Bitcoin has ever seen
um and you know if you survive this long
um man good good resolve right that's
what that's what that's what Bitcoin is
all about
now moving on and looking at the Bitcoin
spending Behavior because you know what
we want to see in this moment and again
this is this is kind of front-faced data
we're finding it this out as it happens
this will evolve and you'll see this
over over coming weeks and reports I
want to see about how how are people
reacting right what are the hodlers
doing in particular I'm not overly
fussed as we said in our previous video
on Monday we're in a hodler dominated
Market I don't particularly care about
speculators because they're more or less
exhausted and I'm also given today's
events um not expecting too many
speculators to be coming back anytime
soon so thus we're in a hodler market
let's see what the hotlers are doing so
at the top here we've got our a super
and net realized profit and loss the way
to think about these on the left hand
side is kind of a relative of all the
coins that were spent this day what is
the average percent that they locked in
as a profit or a loss you can see this
pretty angry looking Wick down here um
which got down to if I can get my cursor
right 0.9 so that means that the average
spend it was locking at a 10 loss now as
you can see I mean that may not sound
like much but you have to remember that
every single coin that was spent was
locking in some kind of loss and the
average was 10 most of the time it's
like two three four percent at most so
these large events 10 loss when we saw
this in the June week the last time we
were down here at these angry numbers
um uh we also saw it here in July it's
kind of coincident with down here it's
uh in the the June sell-off that we had
so it's it's significant right it's
pretty bad now the right hand side is
the USD value on net so take all the
losses um subtract them from the total
realized profits and we have this chart
now you can see here that whilst this is
pretty angry on a relative basis this
isn't anywhere near as angry I mean it's
still a billion dollar loss it's it's
not it's not small change it's a big
number
um it is still a capitulation worthy but
you can see that it's kind of
similar to what we've seen over the last
couple of months it's not the most out
of bounds thing we've ever seen so what
that kind of tells me is that we've seen
a lot of this is Max Payne this in terms
of like people just getting flushed out
and just saying get me out of this thing
this is what this looks like this looks
a lot more like people are certainly
locking in losses but we're not seeing
uh you know the the ultimate flush out
of top buyers this has been the ultimate
flush out of top buyers this is a much
closer to a seller exhaustion
capitulation and a lack of demand that's
really what this speaks to me as and
it's kind of coincidence what we've been
talking about that it's a hodler
dominated Market there's a lot of
hodlers out there who are like oh man
all right okay we've got time and
duration ahead of us 15K BTC right all
right not the best thing in the world
but you know has it changed the thesis
probably not so we've got a lot more of
those folks than we did certainly back
here in June so this process has been
flushing out a lot of those speculators
um and this is probably going to be you
know know one of one of a few Nails in
the coffin to just really solidify that
you can also see that in a realized loss
it's up but it's also not it's not
horrifically bad I mean this thing here
is over four billion dollars in a day
almost five
um so this here at uh what a total
realized loss 1.1 billion now by the way
that net realized profit and loss is 1
billion relays loss is 1.1 billion which
means there's only a hundred million in
profits now that's actually very small
even though it sounds like a big number
obviously but
um you know we're talking about
multi-billion dollar asset here
um 100 million in profits and especially
compared to 1.1 billion in losses really
shows the coins from the previous cycle
pretty stationary they're not moving
coins that are in profit of which as
we've discussed there's not many of them
but from the previous cycle they're
pretty static
average coin dormant is the average days
or average holding time of coins that
was spent right so let's actually just
jump this back to a five-year period
here
you can see the bull market is very
recently I mean we're talking about
numbers that are getting up to like 80
90 days on average capitulation events
down here in 2018 I mean this is just an
over 200 days so we're talking about
people who are selling coins of hell for
very very on average for 200 days right
that's these are big big numbers
this is kind of not really showing up
too much so the average age of coins
being spent kind of confirms that people
from last cycle are just not spending in
any kind of volume which means that it's
more than likely current capitulation is
from people who just recently bought
now we're going to go look at our spent
output price distribution so you may
have seen me look at the urpd which is
the kind of overall spread of coins what
their current price bucket is this one
here is essentially looking at only the
coins that were spent that day now this
is on a log scale by the way
um here's 10 BTC right so if I just put
my cursor here you can pretty much
ignore all of this so previous Cycles
typically less than 10 BTC I mean 10 BTC
is not it's you know it's big for each
of us but it's not big for the market
all these yeah okay sum them all up
you've got a couple of hundred BTC these
ones here are up over a hundred thousand
so compared to this one of these candles
Above This tent is just so many more of
these bars so we can more or less ignore
those bars down there and I'm actually
just going to turn this off log scale so
we can basically see what that means
all the coins that are being spent right
now in any size are essentially from our
recent price range so there's a huge
amount of transaction activity where the
vast majority of it are people who just
bought right so it's essentially those
same people who are jostling for a low
are trying to jostle for another low
we can see this in our long-term holder
Supply there's been a downtick but it's
not exactly I mean it looks like many of
these other little ticks it almost looks
like a pause and again we need to just
watch this is the obviously very very
front-facing data we need to look for
Trends to develop but we can see here
that the amount of maturation that's
going on is is amazing it's it's
historic we will see if this
deteriorates but at the moment it
doesn't yet look like long-term holders
are saying that's it I've had enough of
this thing get me out we haven't seen
that now I don't know whether we need to
see that I don't think we need to see
that but if we do start seeing that that
would then be a loss of conviction right
so looking at these metrics looking for
upticks in dormancy looking for upticks
and old coin volume that's this chart
down here
um spent old coin volume so there's a
coins older than six months and again
you'll find this in one of our recently
released dashboards if we get a
significant uptick right in this
particular model at the moment talking
about 15 000 BTC it's kind of within the
bounds of daily noise it's not think
compared to what we've seen in previous
markets to Market drawdowns 30 40 50 000
PTC a day and the other thing is that a
number of addresses with a non-zero
balance is just kind of in this stagnant
holding pattern we haven't seen this
Mass Purge that we saw here in in May
so anyway look the big takeaway here is
um you know let's go top to bottom
obviously there's a lot to come out of
this story with FTX and Alameda the data
here shows that they were definitely
there was a lot going on between those
two entities and we will find out more
about that in the coming uh coming weeks
and maybe months
um in terms of the overall balance I
mean you can see the difference between
binance and FTX in terms of the way that
customers are treating that that big
particular change FTX the balances that
we're tracking at least are pretty much
empty
um so it's been a quite significant Bank
Run
um it's pretty much cemented this is the
worst bear Market in Bitcoin history
um by by no small magnitude and when we
look at the overall Supply Dynamics it's
kind of the same as what we've seen
previously where the hodlers just seem
unfazed I mean I don't think they're
pleased about the scenario but
um there also don't seem to be reacting
at least with their with their coins
just yet now this is something we'll be
monitoring so make sure you check in on
uh on Tuesday next week for uh the week
on chain we'll be covering this in a bit
more detail once we've got a bit more of
data and time
um to really explore what's going on
um as always please do give me any
comments if you have any questions you
can reach us in the comments you can you
know ping me on Twitter you can ping
glass note on Twitter whatever it is
we'll try and get around to you
um and yeah look hopefully everybody's
okay these are these are challenging
times it's never good when events like
this go down bear markets are pretty
ruthless and uh you know really really
stay safe out there
um so anyway hopefully that reaches you
well and I'll see you in the next one
cheers

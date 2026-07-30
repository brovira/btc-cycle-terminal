# Bitcoin Whale Watching - The Week On-chain - Week 30 (Bitcoin Onchain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=IUbaDI_6zSM
**Publicado:** 20230725 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20230725-bitcoin-whale-watching-the-week-on-chain-week-30-bitcoin-onchain-analy.md]`.

---

foreign
video report for week 30 2023 we are
Beyond Bitcoin block 8 800 000 now of
course this means absolutely nothing
like 800 000 is just another block but
it is pretty impressive when you see
that Bitcoin has been around for 14 and
a half years it settled 109 trillion
dollars
um in terms of total value and utxo
value you spent over 867 million
transactions I mean this thing is a
pretty remarkable Beast to be still
going so uh some really really fun stats
exist out there on just how far Bitcoin
has come um so there is a Twitter thread
that you'll find in the description
below where I kind of covered some of
the different uh you know just
interesting Network statistics to really
reflect on but anyway what we're going
to look at today is a topic that
generally speaking is a very very hard
one to analyze properly it is a very
nuanced and very complex topic um so we
are going to be touching on whale
watching and whale watching generally
speaking there's lots of people who like
to track addresses and you know try and
track what the big money is doing the
challenge is that quite often we get
confused between which addresses are
whales which ones are exchanges which
ones are ETF products and as the market
matures and those types of things ETFs
and and the like expand this is only
going to become more Dynamic and more
challenging so it is a very nuanced
topic but we are going to touch on some
really interesting and bizarre things
that are going on within this cohort
which kind of necessitates a bit of a
view
so whale entities are often cited as the
big players moving around markets and
yes of course if you have a large stack
um there is going to be a degree to
which you can influence the market more
than the plan but what we are going to
be looking at today is just kind of
unpacking the information taking in a
lot of the data that we see and just
trying to distill down some simple tools
because the thing is there's so many
parts of this puzzle that are very
complex and very nuanced and quite often
people get caught up tracking individual
transactions and you know sometimes the
market reacts to it but quite often they
turn out to not really have much
relevance at all so what we're really
going to focus on doing is building out
a couple of tools particularly using
correlations to try and identify more or
less like a filtering device when do we
actually need to pay more attention and
look into it a bit deeper so it's more
about looking for those areas where it
really does show up and say okay maybe
something interesting is happening and
on the other instances perhaps we can
use that as a bit of a filter to say
well maybe we don't really need to pay
attention to that headline about whales
you know doing whatever whales are doing
so anyway before we do get started
please do give us a rate a share and a
subscribe it does help this channel as
always let me know if you've got any
questions comments or thoughts always
happy to answer those and let's get
stuck right into the analysis
okay so we are going to start up in the
glass node engine room and in fact
because we're really looking at entities
whales exchanges almost every metric we
look at today will be focused on our T3
plan for professionals
um so this is really some of our most
nuanced data some of the stuff that
really gets down in the weeds trying to
track entities to exchanges and really
taking the maximum advantage of our
clustering and all the labels that we've
got that our data science team is
building up in the background
so we're going to start in the glass
note engine room which is one of our
dashboards that has a lot of quite
bespoke and metrics that are really
quite challenging to either compute or
to get into a into studio and actually
chart these things
um so so engine room's kind of an area
we do a lot of these exploratory metrics
and kind of building up these ideas
fairly early on
so this is the trend accumulation score
and a very very high level we've got the
smallest wallets 1 10 100 Bitcoin down
the bottom and all the way up to 10 000
plus so these are kind of our entity
groupings what we're looking at is over
the last 30 days that's an important
note over the last 30 days how much of
the group's balance increased going blue
or decreased going red so it is all a
relative it's relative to the last
30-day period what is the net change of
these different wallets now the reason
why this is an interesting way to study
the market is because there are well at
the moment 19.4 million Bitcoin but at
the end of the day there'll be 21
million and a coin is either in a whale
balance or it's not it's either in a
shrimp balance or it's not so these
things can I mean they're not binary
because there's more than one wallet
grouping but they're either in one set
or the other we're kind of got a closed
system and coins are moving around
between different entities and I'm quite
often by the way exchanges will sit in
the middle of this as kind of the the
area where these kind will pass through
certainly the way that our metrics are
constructed
now really we're going to be focusing
only on Wales here and that the
important part is you can see there's
this interesting Divergence this is kind
of the first thing that we noted that
set us off on this exploration our 1K to
10K has moved into what would be
presumed to be accumulation in this Blue
Zone but they're now greater than 10K is
seeing distribution so we're kind of in
this realm it's like okay hang on a
second we've got greater than 10K
wallets are Distributing and we've got
1K to 10K which are accumulating and you
can see that they've kind of got a
similar pattern they're almost operating
in tandem so this is kind of the first
Port of Call and really why we kind of
hone in on the on the whale cohort you
can also see that even in our current
environment they are the ones who are
kind of seeing the most volatility and
change it's very neutral across the
board for everybody else
so just to give you a bit of context and
I would recommend if you haven't read it
already we did a very very comprehensive
report on everything from shrimps all
the way to Wales a lot of the nuances we
captured in that report called the
shrimp Supply sink again you will find a
link in the description below and what
we really showed in that report is that
over the macro scale of bitcoin's
lifespan the whale cohort so to speak
being those with more than a thousand
Bitcoin they have seen their balance
decline year after year after year this
is a multi-year trend and this by the
way includes exchange addresses they are
built into this particular chart we're
looking at at the moment so you can see
we're looking at the entire Supply from
zero to a hundred percent how much is
held by these whale cohorts right and
just remember this particular data set
includes exchanges in this grouping so
it's all wallets with more than uh one
thousand Bitcoin so just for a quick
sense of scale it was about 73 back here
in the 2013 Peak we're just going to use
the market Peaks as our reference point
this whale grouping held around 73 of
the supply
when we got um debt by the time we got
down to the 2013 Market we had something
close to 62 percent
by the time we got to our 2017 Market it
was 52 and that was pretty much flat I
was about uh was it 53 in the 2021 Bull
and where we currently are we're down at
about 42 so the macro scale is that
these whale entities are actually Net
Distributors over the long Arc of time
now it is also quite important to
remember that this includes exchanges
ETF products lost coins satoshi's coins
are in here all of these entities that
have these large allotments so when you
really Factor those groupings out this
thing here is a and that's what we did
in the shrimp Supply sync report this
thing is a big macro decline so the
Bitcoin Supply as much as the critics
hate to hear this the facts of the
matter is that the coins are being
increasingly distributed over time so it
is kind of interesting when you put the
data versus The Narrative and it
certainly upsets many in the traditional
Finance space and but that's you know at
the end of the day it's kind of what
we're here for
so now what we're going to do we saw in
that first chart that we had a bit of a
Divergence between the let's call them
the small whales and the and the big
whales right so there's a bit of a
Divergence they kind of seem to be equal
and opposite if we look at their three
different balances right this is in BTC
denomination you can see back here that
we had a bit of a Divergence right these
very large whales 100 000 plus this was
kind of the gbtc era right lots of coins
flowing into ETF products and Michael
sailor and all of these elements are
playing into it but you can see that
really over the last little while there
hasn't been a great deal of Divergence
and even during recent weeks there's
been a little bit of a downtick about 40
000 Bitcoin a month I'm not mistaken in
this kind of middle cohort but we've
seen an equal and opposite uptick of
about 30 000 Bitcoin in the smaller
whale cohort so again we're kind of
seeing this very micro scale but equal
at opposite Divergence
now a nice way that we can actually plot
and chart this out is saying okay let's
use our net position change so the net
position changes we use this all the
time at glass node and by the way it's a
really really powerful metric we use it
all the time using the the diff function
and workbench it's fantastic when you're
looking at Supply based metrics so if we
want to look compare two different
groups of let's say whale Supply here
we're looking at 1K to 10K and then 10K
plus the same groupings that we saw back
in the in the first chart and we're just
looking at the 30-day change how much of
those aggregate suppliers of whales
change over the last month
now what we've essentially got here is
you can see that there's some periods of
time like where we currently are where
we have kind of an equal and opposite
where one group is declining the other
group is increasing
and what we've used down the bottom here
is a bar and we're basically looking at
this from a correlation standpoint
when there is a negative correlation of
minus 0.5 or less so really getting into
that kind of inverse relationship type
territory this thing here will show up
as a green level now what we've called
this metric is a whale reshuffling and
what we're kind of trying to assess is
are those whales actually just breaking
down their coins going from a 100 000
wallet or a 10 000 wallet into several
thousand wallets now the nice thing
about this is that our clustering
algorithm will pick these up so it's
going to be able to identify where these
different coins are going and if they're
all owned by the same person they're
just breaking them down what we're
looking for here is this kind of
um reshuffling type Behavior are they
really Distributing are they really
selling or buying or are we actually
just seeing coins kind of Shifting
around and moving around the network for
whatever purpose that may be and we have
to remember that exchange isn't often
the middleman for these transactions
coins will often flow into an exchange
and then out because they kind of act as
a little bit of an anonymizer because
coins can flow in but it's very hard to
then see it you know the same coin
doesn't flow through binance and then
come out the other side it comes from
the exchanges hot or cold wallet so what
we're kind of seeing is that exchanges
often get you used to kind of obfuscate
where these funds are going they're kind
of like a bit of a gray box that sits in
the middle
so um the the big takeaway from this is
that we can see that there is on net if
we look at overall in terms of these
groupings there appears to be a high
correlation a high inverse correlation
which suggests that there may be some
reshuffling that's going on right so
that's kind of a a first takeaway
now to try and address this exchange
problem and as I said at the start of
this session it's this is why whale
analysis is very very complex very very
nuanced what we're looking at here is
the whale volume this is a 30-day change
again we've got the net position change
here in purple really really powerful
tool but what we're looking at here is
only coins flowing in and out of
exchanges so we've essentially
calculated a balance that's what the
orange curve in the back here this is
basically all outflows to whales minus
all inflows right on a cumulative sum
bases so think about an outflow from an
exchange to a whale as an acquisition
and when a whale sends coins to an
exchange that's going to be a outflow
from the whale to The Exchange
so what we've then calculated is
essentially like imagine this is like a
purchased balance now you can see that
we have an extraordinarily large 30-day
change in this whale call it acquired
balance down 147
000 Bitcoin a month that's a significant
chunk of coin right we're talking about
an entire micro strategy here that is
essentially left whale wallets and gone
into exchanges so again we're starting
to get this thing with okay there's an
inverse correlation between these small
and large whales price I mean it's kind
of traded sideways and very very quiet
we've covered this over recent weeks
it's just so quiet out there so that
it's kind of interesting to see this
magnitude of coin volume moving around
right an entire micro strategy has
flowed into exchanges and yet the whale
balance hasn't really changed that much
it's kind of equal and opposite in two
different directions so it's starting to
get a little bit interesting right
there's a few pieces of the puzzle that
we can try and dig into here
now this metric is then looking at it in
terms of a total inflow so whales two
exchanges if whales are sending coins to
exchanges this thing here is going to be
green and if whales are withdrawing from
exchange it's going to be red right this
is kind of looking at it from the
whale's perspective in terms of an
inflow and an outflow sorry from the
exchanges perspective so inflow's a
green outflows are red now you know
again these charts can get quite noisy
you can obviously see that there's a lot
more volatility and activity around High
volatility sell-offs and Market tops and
all that kind of thing
but quite often there's there's things
that just stand out with this data and
you know I like to look for things that
just stand out and go oh that's a little
bit interesting and that's a little bit
different and to me the netflow line
this black curve that we've got here you
can see it has been elevated for about
two months it has sustained a higher
level of inflows for a substantial
period of time so again we're really
starting to piece together there is
something going on between the whales
and the exchanges and this is where we
ate and we also know that the exchange
is a kind of this this centerpiece where
coins are kind of flowing in and then
flowing out to go somewhere else
and this is probably the most intriguing
and again I'm not going to be out of all
the answers here we're certainly just
trying to look at some of these Dynamics
and just trying to set the stage for how
we can analyze these Market structures
this is one of the most interesting
charts I've seen in a very long time so
what we're looking at here is of all
this is like a dominance chart between
zero and 100 of all of the inflow volume
to exchanges so we only care about whale
deposits to exchanges
of all that volume that's flowing in
which exchange is it going to
well we know that binance is a dominant
force it is the largest exchange by
almost every metric whether it be by
coin balance whether it be by a trade
volume customer base all of these things
binance is the largest entity when it
comes to centralized exchanges in the
space
and what you can see here is that
binance currently accounts for about 82
percent of all inflows from Wales to
exchanges now we're not talking about 82
of all inflows we're talking about this
only from the whale cohort so whales are
primarily at an accelerating rate
depositing coins to binance coinbase is
here in blue that's kind of giving you a
sense of scale and magnitude so whereas
uh binance is 82 we're talking about
about seven percent going into coinbase
and the gray is pretty much everyone
else about 11 thereabouts my math is
correct so again we don't have all the
answers here but we're just trying to
piece together there is something really
interesting going on when it comes to
whales sending coins apparently largely
to binance right so we're kind of taking
advantage of all these different labels
and all these different clusters to just
try and paint a picture of what's going
on and meanwhile this is happening you
can actually see when this really starts
to spike higher this is happening when
price has basically done absolutely
nothing for a month so it's a really
interesting Dynamic
um but there is kind of the next layer
to this which is what does it really
mean when it comes to Market structure
what else can we really understand about
the profit and the loss and what's the
actual behavioral incentives that are
going on so that's where we're going to
leave in terms of the whale kind of
volume flows but what we're now going to
do is just assess this for a bit more of
a market structure perspective
so in our report last week what we
covered was the overall flow of coins in
and out of exchanges and how it was very
very interesting how short-term holders
here in red have seen a significant
uptick again we try to look for these
things that just stand out as being like
Oh that's a little bit different that
appears to be a bit of a shift or a
change in Market structure
so what this chart is looking at is all
exchange inflows right so the orange
curve up the top here is all exchange
inflows and then what we've done is
we've shown the breakdown the red is
then the component of that that's
short-term holders coins that are
younger than 155 days and again the
reason why we use this is because
statistically speaking that kind of age
threshold about five months a coin is
statistically much less likely to be
spent when it's it's survived or it's
been held for at least five months much
more likely to be spent when it's
younger than that and the younger a coin
is the more likely it is to be spent
this is like a very uh very consistent
curve it's been replicated by across
many different age groupings and by many
analysts so it's a kind of a common
thing that we see across the Bitcoin
Network
in the green we have inter-exchange
flows from binance to coinbase from
coinbase to okx these are kind of
inter-exchange flows and then down the
bottom here is our long-term holders
people who've crossed that kind of you
know hodler threshold and uh they are as
you can see a much much smaller
component so generally speaking a lot of
the day-to-day trade and spot markets is
driven by short-term holders and coins
flowing between exchanges which again is
going to be that Trader short-term
holder type cohort
but notable is this significant uptick
in short-term holders so again we've got
whales who are clearly sending a lot of
coins in and they also you can see very
very little uptick in long-term holders
so really the takeaway here is that this
appears to be short-term holder whales
right we're just trying to further
classify this problem
now this thing here is then looking at
of all the exchange inflows what is the
dominance of short-term holders and
what's fascinating again we're looking
for these big breaks in structure we
have seen in that basically since 2018
it's been between 55 and 65 of all
inflow volume has been by short-term
holders right this is a really stable
multi-year Baseline right of course day
to day that you can see in the
background there's a lot of volatility
but over some kind of meaningful moving
average it's pretty smooth except for
this significant break higher so again
something very intriguing is going on it
just kind of it helps us understand
where we can pay attention to these
things there is something going on in
terms of these flows they appear to be
large size they appear to be flowing
into exchanges and they appear to be
flowing into binets and of these coins
the vast majority of them last
transacted within the last 155 days
making them short-term holder coins so
there's something happening of late
that's that's really really kind of
getting our attention here
now there's another layer to all of this
and this is where we start moving into
kind of understanding a bit about how
Market structure works and how the
on-chain space can help inform what's
going on in spot markets
um so from my experience studying these
you know how these markets work and
really trying to assess how unchain data
helps us understand the mechanics you
will often I often turn to the the
profit and loss grouping realize profit
and loss in particular and the logic is
Right we've been in an uptrend in 2023
there are going to be people who invest
and take profits and what's really
interesting about profit and loss is
it's very much in the market psychology
camp and as someone who's kind of been
learning a lot about Market psychology
it's very much about knowing what the
smart money is doing which is typically
a smaller cohort and then you've got
what the rest of the people are doing
and quite often that tends to be what
the majority tend to do is be on the
wrong side of the boat they tend to do
the exact wrong thing at the exact wrong
time
so what we see during uptrends and it's
we kind of put this into the uptrend
type psychology we see this very
consistently and it's almost perfectly
reversed in a downtrend we see that
prophets this is only short-term holder
coins to exchanges note that our
short-term holder profits Spike higher
on the rally this is literally profit
taking coins get sent into exchanges and
that profit taking is actually what
establishes these local highs so we see
that there's kind of this trading cohort
that sends their coins in and actually
takes profits which is the thing that
puts these local tops in place
now the other thing is why short-term
holders are particularly interesting is
because we're now more than five months
into 2023 and if we consider this
particular part of the market
we still get short-term holder losses
and yet the only way you could hold your
coins for five months and be at a loss
as if you bought the local the local
highs so what we see here is that the
local high buyers actually sell at the
bottoms you see an uptick in losses by
the short-term holder cohort when we get
to kind of the worst part of the
correction so in many ways it starts to
fall into that almost contrarian style
thinking so you see the profit taking
that puts the local high in and then you
see a bit of a micro capitulation that
happens on the way back down and this is
where it really helps us understand
these kind of market dynamics and how
the marketers you know how investors are
moving their funds in and out of
exchanges in particular
so what we've just done there is
switched over to short-term holder sofa
and this is one of the most powerful
tools that we really have it certainly
when it comes to just kind of
understanding these market dynamics
um sopa is is it's a powerful metric
it's been around there's different
variants on it's been around for a
little while it's essentially not
looking at profit and loss in terms of
dollar terms which is what that previous
chart was looking at this one here is
really looking at it in terms of the uh
kind of like a profit multiple so it's
looking at the ratio of price of
disposal and price of acquisition and
it's taking an average across the
short-term holder cohort
now you'll often see when we're doing
our analysis that we apply a statistical
band so we just do a mean plus a
standard deviation right so it's kind of
just a typical one standard deviation
band here we're looking at on a 90-day
period And the reason why it's a 90-day
period is that if you do it on a longer
period of time yes it will be better for
that kind of long-term time Horizon but
I think we can all agree that the last
90 days has been quite different to the
90 days a year ago this was a
significant and fairly you know fairly
brutal downtrend it's 2023 has more or
less been an uptrend so in that sense
we're just going to look at this on a
shorter term time frame and what we're
looking for is periods of time when the
profit taking is larger than that 90 day
one standard deviation band we're
looking for periods of time when the
market takes a lot of profits relative
to the recent Market structure
likewise we can have one on the lower
side right one minus standard deviation
and we're looking for those periods
where the losses kind of exceed what
we've seen over the last 90 days
statistically meaningful
and you can use this Confluence let's
just flick back for one second you can
see that we've got our peaks in profit
near these local highs we get our Peaks
and losses near these local lows so now
let's switch again to our super metric
very very similar point in time when you
get sober pushing outside the standard
deviation bands on both directions so
again it's helping us just quantify what
is kind of typical Market Behavior
within whatever context we're looking at
in this case a 90-day period and just
looking for those statistically
meaningful Things That Go ah we should
pay attention to what's going on at this
point in time
and the last thing that we're going to
do is essentially distill both of those
two observations that first one we
looked at which was profit and loss in
terms of like dollar terminology we do a
bit of normalization but it's more or
less the same calculation and when Soper
is above that one standard deviation
band so we're only looking at things
that are in the profit-taking regime
here
but you can start to see that we can
look for Confluence we're looking for
two different sets of tools that are
saying that there is a significant
amount of profit that has been taken by
the short-term holder cohort so it's
trying to just contextualize and really
give us a bit of a you know a bit of a
tool set and a way to think about these
things how we can normalize the data how
we can look at statistical bands and
really pass these things into more
actionable information and really pull
insights and from what's going on in the
market
so kind of an interesting piece right
we're really looking at that Journey
from Wales something's going on in terms
of their balances okay now exchanges
appear to be some part of the mix
there's coins flowing in and out we can
then determine that they're short-term
holders because they're kind of
correlates between the short-term holder
behavior and what's going on with the
whale cohort and then from that from
that kind of strange and weird Journey
we finally end up with an indicator that
can help us spot when these events are
happening certainly when it comes to the
profit taking and naturally you could
look at this on both sides of the
equation
so thanks for tuning in for that session
folks as always let me know if you have
any comments or questions uh more than
happy to answer those
um so you know it's kind of an
interesting Dynamic um certainly
something to pay attention to hopefully
we've kind of given you a few more ideas
about how to think about these things
certainly we find looking for tools that
just help filter signal and noise and
quite often that will be you know
normalization techniques or standard
deviation bands or what we looked at
with the whale cohorts correlations just
bringing in these tools to help filter
out what is a meaningful piece of
information how to really distill it
down and actually turn it from a you
know set of data into something that's
really actionable insights so hopefully
you enjoyed that one let me know if
you've got any comments and I'll see you
in the next one cheers

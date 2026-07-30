# Supply Squeezes and The Bitcoin Halving - The Week On-chain 46, 2023 (Bitcoin Onchain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=BhJjhK4UoEk
**Publicado:** 20231113 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20231113-supply-squeezes-and-the-bitcoin-halving-the-week-on-chain-46-2023-bitc.md]`.

---

hello everyone and welcome to your
glasso video report for week 46
2023 so as I mentioned in last episode
we're going to be continuing with this
concept of Supply Dynamics and we're
going to be using the harving as our
reference point more so because it's
coming up and it obviously represents a
point of keen interest for investors so
what we're really going to be looking at
here is using a number of Supply metrics
different heuristics different ways to
measure the Bitcoin Supply and we're
really looking for that Confluence when
do we see multiple metrics telling us a
similar story which obviously builds up
conviction and confidence that it's
where starting to get close to some
semblance of
Truth so with the fourth Bitcoin harving
fast approaching it's expected to be in
April
2024 now the reason why this is an
important area for investors we will
look at the return profile that
typically happens following Haring
events and it is in in excess of 400%
now of course this doesn't mean that
that's what's going to happen in 2024
but it's certainly one of those things
with the few data points that we have
it's obviously a point for investor
Intrigue now rather than just saying
okay the price went up 400% in previous
Cycles what we're actually going to do
is explore the investor dynamics that
underpin those previous hars in many
ways looking at the realities on the
ground on what really drives at least in
part what is going on what is behind
that price performance rather than just
saying harving happens price goes up
we're going to actually look at the
supply dynamics that are an underpinning
driving Factor so we're going to do this
in a couple of different steps it's
really building on the uh on the report
we did last week we're going to start by
measuring what we're going to call
available Supply Supply that's kind of
freely circulating that investors today
can reasonably expect to change hands in
the near term when they going to compare
the rates of saving or the inverse
metrics of huddled or stored or saved
Supply and we're going to use issuance
as our Baseline simply because it's a
nice way to just frame things up and
normalize things right if we're
comparing the amount of saving relative
to issuance it's a nice grounding anchor
that obviously uh you know Compares
between these harving cycles and the
last thing we're going to close on is a
topic that we actually covered in our
realized cap video that we released a
couple of months back really looking at
the kind of the multiplier effect of
different periods of liquidity and we'll
explore that when we get there so as
always please do a rate a share and a
subscribe it does help the channel get
to more people and let's get stuck right
into the
analysis okay so here we are starting in
our week 46 dashboard and we're going to
start just with a very very simple
metric shows you a really cool workbench
construction that we worked on to
actually calculate how many days until
the harving So within this particular
function we actually input the block
interval because mining is a
probabilistic um event we don't actually
know there's going to be 144 blocks
mined on any particular day it
fluctuates with hash rate it fluctuates
with probability it's not a uniform
metric so as a result the actual number
of days that we would estimate when that
Haring event is there is no way we know
the block height when it will happen but
we cannot estimate the exact date and
time and what we really need to do is
look at in terms of probability
distribution so I won't go into the
details of this workbench but what you
can see is we've actually set up a
function that will reset at the point of
the harving and then go back to
recomputing so it's one of these
interesting workbenches where we have a
bit of a reset function that's looking
for the time when we hit a specific
block height which in this instance is
going to be every 210,000 blocks reset
back to zero and then start counting
down again taking into account the
variability of actual block timing so uh
that's a bit of a workbench there for
those who are not familiar the
magnifying glass in the top right of any
chart in a dashboard will expand either
the workbench or the dashboard so that
kind of gets you into the mix and you
can see how we've built the formulas uh
to construct these types of charts
okay so starting up with the actual
analysis of the piece um I mentioned at
the start that generally speaking we get
pretty impressive price performance
following uh the prior harving keeping
in mind that this is only three data
points right so we are in the process of
approaching that fourth data point and
of course we will see what happens from
there on so this particular chart again
is leveraging our workbench function
we're using the subset which basically
takes the first 365 days following a
Haring event and then indexes it so can
see the indexed price performance now in
previous Cycles we've got up to 400 600
and in the early Cycles which I think
are a little bit too old to be directly
comparable it was getting up into the
several thousands of percent increases
but obviously this chart at the very
least is why the harving creates a lot
of intrigue for investors so not only is
the harving a technical and you know in
some ways a philosophical Marvel of
Bitcoin it's just really it's really
fascinatingly simple and elegant concept
for investors it's obviously a point of
Intrigue now as I said we're really
going to explore the mechanics of what
drives this from a investor performance
rather than just looking and saying oh
look number go up we're going to try and
dive into the mechanics of what's going
on under the
surface so to just put some numbers on
the rate of issuance that's currently
coming into the market the blue curve
here is looking at the USD issued to
minor so this is basically the USD
reward um not including fees only the
block reward new issuance now just to
put things into perspective the blue
curve is the USD curve the purple line
here is the current year-to-date higher
it's approximately a billion dollars a
month that's coming out to miners so
most miners have to sell all of the
coins that they mine so just at a high
level that's a billion dollar headwind
per month in order to keep the Bitcoin
price stable that's just you know just
very very high level all things equal
now if we were to have that that
obviously goes down to half a billion or
500 million and this compares to the 450
million per month at the FTX lows so
obviously given Bitcoin is up you know
just over 100% the Haring essentially
takes us back down to the cycle lows so
just putting in a bit of perspective
we're talking about about half a million
dollar a month in sside pressure and
that's essentially going to be
alleviated from the market so that's
obviously the first part of this
equation but just put some dollar
numbers just for those who want to um
some quick back of the envelope
mathematics on the impact of the harving
from that
perspective okay so really getting into
the meat of this episode um here we're
looking at available suppli so part one
we're going to look at how many coins
can investors reasonably expect to
transact change hands you know that's
what we're going to classify as
available and there's a few different
charistics we can use here so obviously
the orange curve here is our circulating
Supply which is up at 15.5 million down
here this top surface of the red curve
is what we call short-term hold of
Supply now we use this as our top
surface here kind of the the maximum
amount of coins that we can expect to uh
to change hands these are coins that are
not on exchanges so long and shortterm
plus exchanges equals circulating so
this is exclusive of exchanges we have
different other measurements called what
we call Hot Supply or warm Supply these
are coins that transacted in the last
one month or one week and in the purple
we actually have down here is the open
interest in Futures markets there's also
trading volume there as well there's a
number of different ways we can measure
and which ones we can overlap and double
count and which ones are actually
exclusive but the concept that I really
want you to take away here is on any
particular period of time between 5 and
10% of the total Bitcoin circulating
Supply is either Futures open interest
or coins that moved in in the last one
month so we're kind of talking about in
terms of coins that really you know move
around on a weekly basis it's about 5 to
10% of the circulating Supply in and
kind of equivalent size so we're really
talking about 90 to 95% of the
circulating Supply is dormant um and it
really isn't participating week to week
it's that 5 to 10% that's really moving
around so we're starting to zoom in and
actually narrow down what's available
and again a lot of this is just about
putting things into
perspective now if we look at things in
terms of balances on exchanges now this
is a chart that gets circulated quite
often and I would I would strongly
encourage everybody to actually jump
across to the report for this particular
week because we actually explore not
only exchange balances in there in there
but also some of our estimated
calculations for and and balances for
coinbase including coinbase custody and
the gbtc so these are more of these
teristics that we're working on in the
background here at glass Noe now what I
really want to highlight cuz obviously
exchange balances are an obvious source
for coins that are likely to change
hands they are quite literally one red
button away from being sold and
purchased by somebody else now a really
important note one that's been widely
documented is this turning point in
March 2020 really the market went from a
net uptick in overall balances on
exchanges to a net down tick now as I
mentioned before and I strongly
recommend people check out the report
this week a lot of this is actually due
to both investors really acquiring and
pulling coins off exchanges that is most
certainly part of the equation but we
also saw an explosion in products like
collaborative custody coinbase custody
the gbtc product all of these things
which really do represent a demand level
but often from institutional level
clients these are talking about large
scale custodial relationships it's not
really the same you know buy and
withdraw this is a different cohort of
investors who really entered the Bitcoin
market around 2020 and onwards and we
are talking about a different audience
who expresses their or or their data
regarding their custody is actually
expressed differently to what you would
otherwise look at for other investors so
again I would encourage you to check
that out and what I'm just going to jump
across and look at is another heuristic
that we developed which was our liquid
and our highly liquid Supply and what
you can see is that the shape of this
pattern is very similar to our exchange
balances and that's because quite often
exchanges are liquid and highly liquid
balances so what do I mean when when I
say liquid and highly liquid well
theistic that we developed here there
there's a number of different ways we
can measure Supply in the previous one
we were looking at available Supply
short-term holders one week one month
that uses holding time as theistic how
long has it been since a coin last
transacted the reason we do that is that
when a coin transacts it is highly
likely to transact again this this kind
of probability that the more a coin is
dormant the more likely it is to stay
dormant for liquid and highly liquid
this is a different framework this is
how often that particular entity spends
so if you're an exchange you have lots
of deposits lots of inflows and lots of
outflows so your spending behavior is
quite liquid the other side of that
equation is the illiquid supply where
coins pull out of an exchange into an
Investor's wallet and they stay there
that's what we would classify as IR
liquid so that particular entity doesn't
spend a lot but they do receive an
exchange which is why we have a very
very similar pattern with March 2020
being that Pivot Point we saw more coins
flowing out of Highly liquid and liquid
wallets which by default means they're
heading towards illiquid wallets so what
we are seeing is a dramatic uptick in
our illiquid wallets over time now what
do you can also see is that illiquid
wallers represent the vast majority of
the Bitcoin Supply so again it makes it
one of these interesting elements but
the right way to think about this is
It's kind of the inverse of those
exchange um type products when you see
uh coin going into some kind of custody
solution for example yes they may be
held by coinbase but they are still
owned in terms of their ownership
Arrangement some entity be an
Institutional or gbtc or an ETF or
whatever it is is essentially the owner
of those coins held at a custodian so
again it's why we use multiple
heuristics to try and look for patterns
that really match across the
board so what I really want to highlight
just closing out this section on a
available Supply what we've plotted here
is exchange balances in Orange
short-term holder Supply stacked on top
of that because they're ex they do not
overlap we're talking about two separate
groups here and then we also have this
curve in the middle here is the percent
of circulating so let's sum those two
together shortterm plus exchange
balances both of them are about 2.3
million Bitcoin so they're actually
equivalent in size take both of those
volumes divided by the circulating we
are at alltime lows relative to
circulating of 24% so we really have the
smallest amount of all Bitcoin in really
the history of measurement and again
this comes back to how we're measuring
our different heuristics and we're not
looking for the precise number here
we're looking for what is the general
Trend and the shape and where we're at
based on all those charistics of the
best of our estimate 24% of the
circulating Supply is a reasonable
estimate for how much can reasonably be
expected to transact and remember that
on a weekly basis we're talking about 5
to 10% that is usually moving that's
kind of your BAS B Lo so we really have
a very very small amount of inverted
commas available Supply just by these
different
metrics now let's compare that to the
inverse which is our stored or our saved
Supply that's obviously the inverse of
the metrics we've just looked at and
what we can see we've plotted a bunch of
these um together red and orange being
the warmer colors are available Supply
measures and the cooler colors of greens
and blues are saved or stored measures
now what we can see is that since really
the uh since 2021 we've seen a widening
out or an opening up of this Divergence
there's a bit of an alligator jaws going
on so I'm just going to zoom in on a
5year basis to really look at this in a
bit more detail and what we can see is
this Divergence is actually getting
pretty Stark if we look at things like
liquid and highly liquid and orange it
is trending lower if we look at
short-term Supply Plus exchanges it is
trending lower if we look at IL liquid
Supply and long-term holder supplyer
they are both trending higher and we
also have in here voltage supplyer which
comes from our coin time economics
framework that is also trending higher
now these are all on different axes so I
encourage people to actually jump in
here and have a look and and test out
where these things lie more for
visualization that's why they've been
put on separate axes just to make it a
little bit cleaner to see but the
important thing here is the trend and
these are diverging we have more coins
going into stored saved and you know IL
liquid wallets and more coming out of
mobile highly liquid and exchange type
wallets so moving into part two this
this uh episode we're looking at the
rates of that storage so we're now
looking at the saved or the stored side
of the equation so in Orange we've got
our month in this case we're looking at
a 90day so quarterly issuance um and
we're comparing or overlapping the rate
of change of illiquid Supply over that
90 days so the other way to think about
this when coins come out of an exchange
they're leaving a highly liquid and
going into an illiquid wallet right so
they come from a high degree of
liquidity exchange balances and the like
towards what we could otherwise let's
just call it a accumulated or a hled or
a wallet that has less history of
spending now what we can see on the
previous Haring note that the illiquid
supply change is substantially higher
than it is from I mean actually from the
issuance before the harving but most
certainly on the issuance after the
harving the key Point here is this
really demonstrates an invest demand
profile people seem to buy and
accumulate into and through the Haring
and you can actually see that really
since February 21 we've seen significant
accumulation that has more than the
issuance for pretty much that entire
period of time so we've almost had 18
months maybe 25 month 24 months of
fullscale accumulation where every
single coin that's mined is essentially
going into some form of illiquid wallet
so when we have the Haring this is
already substantially higher than where
we are and again this is only one
heuristic we're going to explore this
this is why we look for Confluence
because one metric is not going to tell
us all the answer but we can see that
investor accumulation patterns have
actually been quite substantial um
despite the fact that the market went
through a significant bare draw down in
2022 now coming across to those timebase
heuristics this is long-term holder
Supply in the blue and voled Supply
which is the much a very very dense
heavy form it's kind of the the heaviest
component of that HED Supply we can see
three interesting waves in in all
previous Cycles actually so let's look
at 2015 we had our first wave of
accumulation following the first selloff
this is when the bare Market has kicked
in the all-time high is now well and
truly taken out and we are some distance
below that first wave of investors we
see it here in 2018 step in and actually
buy that oh look it's no longer 20,000
it's now 6,000 or it's no longer 13,000
it's now um 1300 it's now 600 it's kind
of that first wave of and we see it here
again in 29,000 that first wave of buy
side the second wave typically comes in
towards the the late stage bear we see
it through 2015 we see it through much
of 2019 into 2020 and you could argue
we've seen this through most of 2023
that really put in that floor from about
mid 2022 when three arrows blew up we
got down to 17,000 all the way through
to
FTX and the third wave actually comes
into and through the harving we see it
here in 2016 we see it here again in uh
in 2020 following the co event and
obviously that's it's not just the har
there's also all the other macroeconomic
events but we are seeing that similar
rate of accumulation that is well and
truly in excess of issuance well and
truly before the harving so again we've
got this very very robust and resilient
hodler accumulation at this point in
time and given that issuance is lower
and lower that is why we're seeing
available Supply reaching these kind of
relative lows because the only other
place coins can come from is from
existing holders who are actually
selling and distributing their coins so
there is quite a bit of buide coming in
by these
metrics now we can compare this to
another met I mean there's different
ways we can measure Supply and I think
what I really want to highlight here is
we can use time we can use spending
heuristics here we're using shrimp to
fish so how big the entities are and we
can see that shrimp to fish right these
are wallets under 100 BTC they are also
accumulating at a rate that is
equivalent issuance naturally there's
going to be overlaps between e but they
they're different heuristics different
ways we can slice and dice the supply um
so you can see that essentially You
could argue that you know um in terms of
the issuance that's currently being uh
brought on online for miners the shrimp
and fish are essentially accumulating
all of it so then we could also look at
the other cohorts to get a bit of a full
picture but this is just trying to show
how different juristic can uh can assess
this
mechanic and as a nice summary of all
these things this is another way we can
use workbench I've reset the circulating
supply to the 1st of January 2022 so
we're looking at basically the last two
years not quite two years but close to
it it the Orange is how much the
circulating supply has
increased the green curve here is how
much voltage Supply again that heaviest
densest form of huddled coins it's 1.1
times larger than circulating so pretty
much every coin that's been mined plus
10% has gone into that volted category
those fish to shrimp is then getting up
to about 1.8 times the circulating if we
go to long-term and illiquid Supply
we're getting up to 2.4 2.5 times the
issuant so it just shows you that we're
seeing more than all the issuant Mind
Over That 2-year period is going into
one of these forms of
storage so with all that as context the
next thing that we're going to cover is
what is the actual impact that this may
have on the market so again let me just
highlight and go back to that report
that I mentioned about the realized cap
which we did released both a video and a
written report to really explore the
realized cap it's a really really
powerful metric that all analysts in
this space should really become quite
familiar with the big highlight is that
what generally happens Market cycle
after market cycle is we see coins that
are accumulated during the lows right
what we see during bare markets let me
just turn off my tool tip here um during
bare markets and these big long sideways
accumulations that we have like 2018
through to 2020 and 2015 and 2016 and
indeed 2022 and 2023 is the realized cap
tends to trade sideway to slightly down
this is because losses dominate but
generally speaking investors leave the
market there's a lower attention and
what happens is that Things become less
liquid we see more price swings more
volatility on small capital inflows and
outflows during bull markets on the
other hand we see an explosion of profit
taking as coins accumulated in the
previous cycle are transferred to new
investors at higher prices realizing
profits pushing the realized cap to
higher levels and essentially getting to
this point where the market expands we
see Capital flowing into the industry
now during these periods of capital
inflows as anyone who's been through a
Bitcoin bull market probably knows
things can get pretty wild But
ultimately the bull market comes to an
end that profit taking overs saturates
the inflowing demand and the concept
we're trying to explore here is given
all of the supply Dynamics we've just
looked at how can we essentially measure
assess gauge how many capital how much
capital inflow or outflow in the
realized cap produces a $1 change in the
market cap so another way to think about
this what is the the leverage ratio so
to speak how many dollars have to go in
to create a $1 change in the market cap
so this I won't go through the Full
Construction of this but what we're
basically looking at is how many dollars
does the realized cap change up or down
to produce a $1 change in the market
market cap up or down this is a
non-directional basis it's really
looking at that almost liquidity ratio
the gearing ratio of dollars in equals
what out the other side so the gray
curve down the bottom here is that on a
90-day basis a 90-day median just really
trying to pick the big picture here
we're not looking for overly precise you
could obviously go down to smaller time
frames to look at this on a much more
precise and granular level but what I
want to highlight the orange zones here
is when you need more than 75 cents and
bull market Peaks it's over 80 cents 85
a doar
a150 a150 needs to go in to produce a $1
change in the market cap that's when we
start to get to fairly overheated
oversaturated let's call it
unsustainable
levels and the converse during those
bare Market accumulations 2018 2019 2022
we get down to Capital ratios of
sometimes less than 10 cents so 10 cents
of capital inflow or outflow creates
more than a dollar or or $1 of market
cap change now as I mentioned this is
directionless so you can see here during
the low liquidity periods of 2022 a
10cent outflow created a $1 draw down so
that's why you get these really violent
sell-offs during those late stage bare
markets because there's just not enough
liquidity in there to support the market
um and it works in both directions right
so where we currently are is in one of
those periods of relatively low
liquidity this red curve here is the
4year median and it's basically traded
about 25 cent so right now where the
market is on a long-term median 25 cents
coming in or out of Bitcoin it's
creating about a $1 equivalent move in
the market cap and actually if we look
at where we currently are it's back down
towards about 15 cents on the gray curve
so it's just one of those kind of
Concepts or Frameworks you can take away
with you to really study how the the
supply dynamics that we've looked at can
then translate across to what's going on
with capital change how many dollars are
flowing in or out but really using the
realized cap and merging it with our
supply metrics to get a really complete
picture and I think the the story I want
you to take away from all this if we go
back up to our harving uh sorry to our
um long-term holder Supply whilst the
harving certainly harves the issuance
it's really the investor Behavior
leading into the through the bare Market
putting in the floor and then through
the Haring itself that actually creates
these Dynamics so in many ways we're
describing the investor Behavior now
whether it's a self-fulfilling prophecy
that the reason the market goes up is
because the harving happens and that
brings people in or whether it's the
people who know about the harving that
actually put in the floor buy those
levels during the bare market and then
acquire during the the uh the Haring
event itself that creates that upwards
momentum all of these mechanics what
we're trying to do is describe the
investor Behavior rather than just
saying number go up putting some actual
mechanics and investor Dynamics behind
the whole thing so thanks everyone for
tuning in for that session hope you
found both this week and last week
useful as a kind of overall view of how
we can use many different Supply metrics
many different heuristics different ways
of measuring Supply and really using the
harving as a bit of a you know an excuse
to go through and look at this um what
really drives the behavior is investors
and what onchain analytics is really
giving us is a lens to actually
observing this investor behavior that
quite frankly is very very hard to do in
many other assets uh if if at all so it
gives us a really really unique lens um
and Hope hope you enjoy kind of
exploring these these Dynamics from a
more fundamental perspective so until
the next one thanks for tuning in I'll
catch you then
cheers

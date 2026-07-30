# The Week On-chain: Evaluating Exchange Risks - Week 35, 2023 (Bitcoin Onchain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=B2aWvbiwOTo
**Publicado:** 20230829 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20230829-the-week-on-chain-evaluating-exchange-risks-week-35-2023-bitcoin-oncha.md]`.

---

foreign
and welcome to your Glasgow video report
for week 35 2023 today we are doing a
deep dive on Exchange risk and really
this is kind of coming off the back of
many of the lessons learned and kind of
time we've spent studying the FTX event
where really the digital asset Market
learned in a very very painful lesson
that counterparty risk remains
now for many of our clients you know
when we're trading and using these
exchanges there is always going to be
that counterparty risk and in many ways
we've got lots of tools to help
understand when there may be kind of
things that just look a little bit out
of balance potentially times where risk
mitigation strategies and capital
preservation may need to step in
so what we're going to do is explore
this through the lens of you know using
FTX and a couple of other exchanges as
case studies just to really understand a
couple of these different metrics a
couple of Frameworks for how we can
think about exchange and counterparty
risk and really what we can do to try
and just identify and spot those
particular uh kind of events that are
just out of the ordinary
so counterparty risk and when exchanges
you know the the hard reality of this
industry is that assets need to be held
at some kind of a custodian and
obviously these custodians come in
varying degrees of quality as we found
out with FTX uh unfortunately things do
go wrong
um and this is a lesson that has been
learned many times you know the mount
gox event back in 2013
um and you know there's been many of
those such events since
so what we're going to look at today
we're going to start off with a bit of a
general View and just get a bit of a
sense of scale for how large exchanges
are and really just paint the pictures
that they really do Remain the
centerpiece of liquidity for this Market
and what we're then going to do is we're
going to introduce three different
metrics or three different ratios or
indicators across the four top assets
Bitcoin ethereum usdt and usdc this is
really where the primary majority of the
capital in this space really exists and
just look for some of these indicators
across four exchanges Finance coinbase
who OB and FTX essentially just selected
so we can get a bit of a view of
different types of exchanges and what
some of these indicators may tell us
some of them have some nuances and we're
just going to bounce around these ideas
and just kind of talk it through
so as always please do give us a rate a
share and a subscribe it does help this
channel get to more people really do
appreciate it um let me know if you have
any comments and just as a reminder
these particular metrics will be
available because we're looking at the
actual exchanges themselves and this is
really taking advantage of you know kind
of the top level of uh of glass nodes
labeling and entity analysis we're going
to be looking at internal exchange
transactions exchange to exchange really
leveraging all of the benefits of our
entity adjustment and our exchange
wallet clusters so uh really getting
into some uh some some pretty impressive
work that the data science team is
consistently building so uh we'll be
building on top of those
now just before we get stuck into the
analysis if you did miss it we released
a video last week
um uh covering that kind of an initial
introduction to coin time economics this
is a white paper that was developed
between myself and Dave puel from Arc
investor I was a joint venture between
glasnode and Arc and this really is I
mean this has been about 18 months worth
of work so if you haven't seen the the
coin time economics piece please do jump
across to our landing page you'll find a
link in the description below and this
is really a new economic framework for
Bitcoin it is kind of the amalgamation
of lots of interesting work kind of
lateral thinking and really correcting
many of the on-chain metrics that have
been drifting over time it really is a
bit of a an Insight from a new lens that
links the dimension of investor holding
time to the coin Supply so really quite
something coming quite interesting
certainly something out of left field
but I do recommend if you haven't had a
chance um please do jump across and
download the report uh PDF and as always
looking forward to hearing your comments
feedback
okay so getting stuck into the analysis
that we're all here for as I mentioned
we're going to start with the macro
picture and I just want to paint the
picture of how significant and you know
meaningful exchanges really are
so quite often people will look at the
balance that is on exchanges and here
we've essentially got the breakdown of
overall exchange balances
um broken up by all the different
exchanges themselves
now in terms of the general magnitude
right overall the trend has been since
March 2020 we have seen a net downtrend
overall but really what I want to draw
your attention to is that we see with
exchanges as with many things when it
comes to supply in markets and
populations and all the rest of it we
have a Pareto distribution you can see
down the bottom here this is binance
which has the largest balance of the
exchange component and just as a quick
reminder exchange balances do not
include things like custodians right the
likes of holding gbtc and these other
ETF products those kind of institutional
custodians they are a separate set of
entities this is really looking at the
exchange the actual exchange where you
can actually you know where the trading
is actually taking place that's really
the what we're trying to capture here
um so buy nets down the bottom here
we've then got coinbase sitting on top
as the second highest and then bitfinex
and then it's essentially a very rapid
grading down so really a huge proportion
of the overall kind of balance on
Exchange liquidity is generally centered
around a handful of exchanges it tends
to be a relatively small cohort where
most of the capital exists
um now this is kind of an interesting
chart again just just trying to put
things into a little bit of perspective
um what we've got shown here I might
just go on an old time zoom because it's
a it is a nice chart to look at
um what we've got here is just kind of
showing you a bit of a relative scale
just to get some ideas into your mind so
down the bottom in the gray this is the
circulating Supply obviously and you can
see down the bottom in Gray This is the
probably lost supplier the supply that
is highly probable lost
um coins that haven't moved since we've
had an exchange traded price back here
in 2010 so you can kind of get a bit of
a center scale it's about 1.45 million
BTC
now sitting on top of that in the yellow
this is the exchange balance so you can
see it's a it's a meaningful component
but a much much larger component is
essentially held off exchanges noting
that again custodians and gbtcs will
also be inside the orange but you can
get a bit of a sense of scale we're
talking about one and a half million
Bitcoin that are currently sitting on
exchanges it's around about 12 or 11 of
the overall circulating Supply
now if you can squint hard enough you
can see that little purple layer sitting
on top that is the entity adjusted
volume that's sitting on top of that
exchange layer and this is again just
put a bit of a sense of scale that's the
amount of volume that's transacted every
single day now just to be really um uh
conscious here
when we talk about transaction volume
like last year we've got a couple of
different versions we've got our kind of
total volume or change adjusted these
metrics are looking at the aggregate
looking at all of the transaction
activity change adjuster will remove
some kind of industry standard
heuristics but for the most part it's
going to capture all of the transaction
volume going on
our entity adjusted volume is really
going to move it's going to ignore and
filter out all of the binance internals
the coinbase internals kind of self
spends it's going to work out when
transaction volume is non-economical and
when we're looking at exchange related
data we're going to be using our entity
adjusted volume because it's going to be
filtering out all of that noise and
we're going to be comparing apples with
apples we'll talk about this in just a
second but you can kind of see the scale
of this we're talking about a very very
small fraction about 0.2 percent of the
overall volume and again this could
include the same coin spending twice if
it's going between two different parties
a deposit and then someone else
withdraws it but about point two percent
of the supply moves around on a daily
basis just for a bit of a sense of scale
now this here is our entity adjusted
volume in Orange plotted out in BTC
denomination and down the bottom here in
a stacked form we've got our exchange
withdrawals in red and our exchanged
deposits in green so just to put a bit
of a sense of scale you can see that if
we take the total height of our entity
adjusted volume about 50 percent it's
actually 55 as of right now 55 of all
transaction volume
economical volume that's occurring on
bitcoin is either to or from an exchange
and just uh to really put a pin on this
this is really why on-chain data is so
information dense because more than half
of all economical flows are people
sending to or withdrawing from an
exchange and each time those
transactions take place all of the
on-chain data that we look at whether
it's the age of the coins that are spent
the profit or loss that is realized all
of these components are telling us
something about Market sentiment so it
really goes to show just how significant
exchange flows actually are to the
industry
this year we've essentially done the
same chart we've combined it so the blue
is now total just gluing together a
deposit and withdrawal volume and then
here we've got our actual dominance and
you can see that we're about 54 or 55
dominance right now which is not too far
from the all-time highs you can also see
that exchange related flows is in a very
long term macro uptrend it goes through
its cyclical behaviors but overall the
amount of transaction volume going in
and out of exchanges it's it's more than
half of all economic flows so it just
puts this thing into perspective that
these exchanges really are the
centerpiece of the industry when it
comes to liquidity and trade volume and
furthermore this is why on-chain data
has such an impressive footprint in
terms of the amount of data and
information we can extract out of it
because it dominates so many of these
coins are people buying selling trading
moving coins around and again all of
this is going to exist within that you
know we talk call it hot Supply or
short-term holder Supply a lot of that
exists Within in those buckets until it
goes to a hodler's wallet and migrates
and matures and becomes that long-term
holder so again just kind of putting a
bit of a bit of a perspective on all
these things
um and the last thing we're going to
look at is in terms of the overall fund
flow breakdown so again in Orange this
is basically a dominance chart in the
orange we're looking at total entity
adjusted volume and again you can see
here in the blue this is our exchange
related at about 55 54
down the bottom here in purple
we have flows that are associated with
whale entities so we're talking about
entities with more than 1 000 BTC
um in terms of their overall kind of
entity adjusted volume so that's looking
at how much of the flows going in and
out of exchanges are actually dominated
by whales and it sits around 25 if
memory serves correctly and then down
the bottom here in red we have inter
exchange flows this is binance to
coinbase or binance to buy a bit or buy
a bit to who OB whatever that exchange
may be the red here is actually showing
us how much of that volume is actually
dominated by inter exchange flows so you
can see that the overall picture of flow
funds flowing in and out of exchanges is
quite Dynamic and we're going to use
this initial breakdown and now step in
and look at some potential indicators we
can use to try and spot exchange risk
now what we're going to do in this next
section is really just highlight the
concepts and this can be applied to any
exchange we've used binance coinbase who
OB and FTX just as you know a different
um kind of case studies to understand
the mechanics and each one of those
exchanges has a unique characteristic
just to help put this into a bit of
context so what we're looking for here
is things that just may look a little
bit bizarre right when something looks a
little bit out of whack and we're going
to use fgx as an example where pretty
much everything was out of whack and
almost the the perfect case study for
what not to do or at least what to look
out for
so the first thing we're going to look
at is called out internal reshuffling
ratio and what we're looking at here is
let's just take an exchange exchange a
if they are turning over internally lots
and lots of coins let's say for example
they've got a thousand Bitcoin just
argument's sake and they churn over 800
Bitcoin every day right they're doing
some kind of internal wallet management
well in the case of FTX it turns out
this was actually Alameda
misappropriating customer funds so that
kind of internal churn of lots of their
balance is something to just pay
attention to so what we look at is the
total internal transacted volume by
their balance it's basically how much of
their overall balance are they churning
over
um on a seven day moving average basis
so if we look at the and we're going to
look at this from four different Assets
in all of these metrics we're going to
look at binance top left coinbase top
right FTX bottom left and who OB bottom
right and we're going to look at always
Bitcoin ethereum usdc and usdt with the
color traces being their token now
there's a lot of lines here let me step
through each one
so what this is going to tell us if we
get a high value that's close to one all
of these are capped between zero and one
if we get a high value of one right in
the case of binance here we get these
spikes of orange spikes of green this
means that 100 of the Bitcoin balance
has turned over over the last seven days
likewise here we're getting lots of
turnover of tether
um if we get a low value basically means
that it's a very small percentage is
turning over
now if we look at the FTX case their
Bitcoin balance was essentially churning
for a period of about 14 months they
were spending more than their entire
balance over and over and over again
internally and this turns out it was
actually Alameda misappropriating funds
so we're looking for that kind of
strange Behavior
so let's go top to left let's start with
binance you can see that typically
speaking we get churn on a couple of
assets typically around volatility big
sell-offs big sell-offs large Market
rallies and if we kind of think about
this there's always going to be some
some kind of nuance here
You could argue that this is essentially
Market volatility lots of people deposit
lots of people withdraw there's going to
be a period where these assets need to
be kind of recombined with their car
wallets their hot wallets need to be
sorted out deposits all get Consolidated
during these Market volatility events
because there is more Market activity it
actually makes sense for this to happen
so it's something to just pay attention
to particularly if it's over a sustained
basis but there are also very legitimate
reasons why this may happen
now if we look at coinbase we can see
there's very very little going on except
for usdc and then we go okay well Circle
and coinbase have a partnership coinbase
is a primary onboarding venue for usdc
so in many ways what we're seeing here
is that that internal churn is very very
likely going to be part of that
partnership it's essentially usdc on and
off-boarding so in that instance it
actually does make quite a bit of sense
for FTX and again a lot of this is
leveraging the Lessons Learned right
we've seen what the disaster that FTX
was and we're just trying to propose
some different ideas to help spot it to
make sure that doesn't happen again
if we look at it from the case of FTX
they were churning their entire Bitcoin
balance for about 14 months and note how
it stops when the exchange stops because
the coins were gone right this is just a
very unfortunate reality but gives us
something to pay attention to moving
forward
so now if we move across and look at how
OB we can see similar to binance we have
these volatility linked events right
where we get these kind of wallet
churning so far we haven't had any
sustained periods of uptick
however what we will note is that it's a
little bit more elevated over recent
months we've just seen a few more as not
just Bitcoin we're seeing it across a
couple of assets you'll see here for
binance we kind of get these spikes
where a bunch of assets churn and then
it dies off for huobi it's just a little
bit larger at the moment so it's just
something to just be aware of and pay
attention to but we have to remember for
all of these metrics when it comes to
who OB we are looking at the the
denominator which is their exchange
balance for the asset that is in the
bottom of the all of these terms and as
a result as the denominator gets smaller
any churn that's going on in the top
level is going to be larger but that in
itself you can see that overall in terms
of the proof of reserves on who OB it's
just something to pay attention to that
there is in fact a declining overall
number of assets available on the
exchange itself so it's just one of
those things to keep in the back of the
mind because you'll see that very
similar theme where it looks quite
similar to binance volatility linked but
at the same time that is partially
because their balance has actually been
in a fairly long-term decline
now the second one we're going to be
looking at is the exchange Reliance
ratio and the concept here is funds we
saw that inter-exchange flow well let's
say you're a very large exchange and
someone deposits you know a thousand
Bitcoin and you've got one million
Bitcoin well that thousand Bitcoin is
kind of small relative to your balance
and if more funds flow from your
exchange to somebody else's it's all
relatively small compared to your
balance nothing to really you know kind
of be concerned about if on the other
hand on a regular basis a significant
chunk of your balance is going to and
from other exchanges it kind of
indicates there might be a Reliance
right a smaller exchange if there's lots
of funds flowing to and from a bigger
exchange and it's a significant portion
of the small exchanges balanced that may
indicate there's a Reliance of the
liquidity between these two entities it
may suggest that even that exchange has
a better counterparty risk going on
so what we look at is the 30-day net
flow of the total amount of coins
flowing in or out from an exchange and
compare it to its balance now this one
can trade between positive one meaning
that we've got overall net inflows or
negative one meaning that there's net
outflows
so again we've got our same grouping for
binance we can see that there's periods
of time where tether flows in and tether
flows out we can see that usdc
interestingly note that usdc tends to be
deposited to binance really over the
last 12 months and it's actually a very
similar magnitude to usdc being
withdrawn from coinbase so what this is
actually telling us is there is likely a
flow of funds of usdc from coinbase to
finance
now the other thing to note is that most
of the other traces tend to oscillate
around zero right for both finance and
coinbase and really what this reflects
is that these two exchanges are so large
and their balances are so big that
they're not really reliant on any other
exchange that's really what this is kind
of pointing out to there is a relatively
low degree of Reliance on the liquidity
on binance to the liquidity of other
exchanges and same for coinbase
now for FTX we have this very very angry
looking Red Zone this is because lots
and lots of coins and you can see this
really started up when three arrows blew
up back in June 2022 almost all assets
started flowing out and in the wrong
direction so in many ways this is
essentially telling us that there were
warning signs as far back as June which
is really when most analysts would say
that FTX probably actually blew up or
Alameda blew up and it was just a a very
painful process till the final unwind
um now again if we look at who OB we can
see there has been for a sustained
period of time a relatively significant
amount of fund flow we can see Ethan the
background here in purple are starting
to see significant outflows
um towards other exchanges likewise for
usdc periods of usdt so again it's just
one of those things to just be a little
bit aware of that there is in fact
relative to who obese balance which we
saw before is declining there is a
relative amount of funds flowing towards
other exchanges out of who OB and
towards other exchanges and again this
is just one of those things just be
aware of and just kind of consider it
when it comes to counterparty risk
now the last one we're going to look at
is the whale withdrawal ratio again
we're going to put the exchange balance
in the denominator and what we're going
to look at is the seven day flow of
funds to whale addresses so this is
looking at whales people who have more
than 1000 BTC this is typically trading
desks larger entities withdrawing funds
out of an exchange to their wallet and
let's again just have a look at FTX as a
case study the red curve here is the
long term average because naturally
every exchange is going to have its kind
of natural heartbeat whale's going to be
depositing and withdrawing all the time
so we've kind of got this long term
average as a bit of a you know what is
typical and normal
now you can see we've got our Gray Line
up the top here this is kind of when we
start getting into extreme risk
territory for binance you can see that
you know it's got a kind of a bit of a
heartbeat but it generally trades well
and truly below the long term average
for coinbase it's no I mean both of
these exchanges are just simply nowhere
near that level so what we're seeing is
that relative to the balance of coins on
coinbase and binance the amount of whale
withdrawals are relatively small there's
nothing really that kind of sends up any
kind of major red flags again none of
this is is um comprehensive this is just
a couple of metrics
um there can still be risks out there
that we don't cover here all we're doing
is looking at some of the lessons
learned from FTX and trying to just
paint a picture and turn these into some
metrics we can assess engage
now when we look at FTX you can see
again here's that June event when the
three arrows blew up and the whale
outflows blew well and truly above that
long-term mean and obviously ended when
the exchange collapsed so we can see
there is a non-trivial amount of of
whale outflows going from FTX
and lastly just to close out again
looking at who OB we can see that over
recent months we have seen a little bit
of an uptick a notable uptick in terms
of whale outflow volumes it is clearly a
break from what we've seen for really
since
um mid-2019 it is not unheard of we have
seen this level before however it is
just one to be aware of let's just
quickly Zoom back up so we're looking
here at uh around mid 2019 during the
rally so we can see here that we have a
net decline but we know that our balance
is in the process of declining
if we go back to 2019 we can see a
similar level right in terms of overall
volume or balance held on who OB we can
see that there was a similarly small
balance at that point in time so again a
lot of these things come back to the
fact that the denominator for who OB is
quite low which is the exchange balance
but that that in itself is kind of just
something to be aware of and and
cognizant of as we move forward
so thank you for tuning in for that
session hopefully you found that useful
um you know exchanges are the
centerpiece of this market and uh just
you know keeping an eye on these things
and understanding exchange and
counterparty risk um can be useful right
it's a it's a powerful tool when it
comes to risk management risk mitigation
and what we propose here is just a
handful of tools more of a framework a
way to think about it and really
leveraging some of the examples from FTX
you could really see that FTX stood out
across all three of those metrics and
really what we're looking for is just
things that warrant that kind of second
look right it's just a bit of an
indicator to show us that something is
just a little bit off and therefore we
can just have that extra you know extra
kind of uh scope around it
um now if you haven't checked out coin
time economics please do please do
review our white paper again there's a
part one primer by the arc side which is
a bit more of a general overview and
then part two is a much much deeper dive
really going for on-chain Specialists
and analysts
um really giving you the full picture
right stepping through all of the
metrics all of the constructions and all
of the findings
um so as always I look forward to
hearing your feedback hope you have a
great week and I'll see you in the next
one cheers

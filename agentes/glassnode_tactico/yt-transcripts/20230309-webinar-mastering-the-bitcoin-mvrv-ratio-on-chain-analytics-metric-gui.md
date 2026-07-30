# Webinar: Mastering the Bitcoin MVRV Ratio (On-chain Analytics Metric Guide)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=MKIMYbalO4w
**Publicado:** 20230309 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20230309-webinar-mastering-the-bitcoin-mvrv-ratio-on-chain-analytics-metric-gui.md]`.

---

so for this particular session uh we're
going to be actually focusing on one
single metric it's a crowd favorite the
mvrv ratio this is a tool that has been
around really since the origins of
on-chain analysis you know it kind of
comes from the realized price and the
realized cap which really are some of
the most foundational metrics and to
this day carry some of the most
significance the mvrv ratio is then a
derivative of that um originally
developed by Murad marmadov and Dave
puel so this is something that's kind of
been around for a long time but at least
in my experience as an analyst is
massively underexplored and
underappreciated in many regards
so what we're going to look at today is
kind of a bit of a snapshot and a deep
dive into the mvrv really exploring some
of the different profiles of what we can
do with it we will do about 30 minutes
of content
um and then we'll uh we'll close out
with a session of q a
so uh if you do have any questions there
is a a question form uh in this Zoom
call so do feel free to put those
questions in and we will come through
and get to them at the end all right
let's get stuck into it
so the The Humble mvrv ratio so this is
one of the most popular metrics as I
mentioned it's been around for uh pretty
much as long as on-chan analysis as a
discipline has been itself
um and really lots of people look at it
as a macro oscillator which it of course
is but under the surface when we
actually digest and understand what
exactly the mvrv ratio is doing what is
it presenting us what does up mean and
down mean and high values and low values
when you actually look at the underlying
bones of what this thing is doing it is
providing us a view on the unrealized
profit and loss held within the entire
Bitcoin Network
so the way to think about this and and
for any of you who've been uh kind of
absorbing our video content or our
webinars in the past you'll know that I
love to bring in the layer of
um human psychology
so if the mvrv ratio is basically
charting out current price which is
market value spot price market cap
divided by realized price which we often
consider to be the acquisition price so
the current value divided by the
acquisition value that will give you a
profit multiple when it's above one it's
going to give you a we are in profit
when it's below one it's going to give
you we are in loss on average and the
psychological concept here is that at
some point in time everybody sees an a
green enough number in their portfolio
that they feel motivated to sell and
likewise at the very very bottom of bear
markets there's only so much pain that
the human can take and when we look at
our financial portfolio and it's just
red red at some point in time that
elicits the same response of people
flushing out their coins so that's why
it tends to work on these extremes we're
looking at points in time when people
become exceedingly likely to distribute
their coins and that generally triggers
some kind of cycle change
so what we're going to do in this
particular session is focus on that kind
of core properties we'll explore just
the vanilla mvrv itself we're going to
look at some probabilistic Frameworks
and some tooling and just kind of ways
that I think about these types of
metrics we can look at how we can
actually identify Market extremes and
actually convert that into pricing
levels right which just makes it a bit
easier it's the same data but presented
in a different way
and we'll also look at market trends and
divergences so there's a lot going on in
terms of what the mvrb is capable of
more than just an oscillator that goes
up in balls and down in Bears so let's
get into a glass note studio and we will
start this thing off
so all of the charts that you'll see
today we do have a dashboard here we
actually have one for both Bitcoin and
ethereum you'll find it in our dashboard
Suite under uh profit and loss for both
of those assets and there is actually a
report here mastering the mvrb ratio
which will take you through those
elements but obviously you know it's a
bit more fun to do it live live in the
session
so let's jump into Studio itself this is
the humble MV RV ratio you'll see that
we do have a dashed line down here and a
value of one that is essentially the
break-even level so I mentioned that
mvrv is an unrealized profit and loss
multiple and look at all of the coins in
the market how much profit is the system
in if it's above one and how much loss
is it in if it's below one
um and as I said it does Trend right
obviously between bull markets and bear
markets but really for most people when
we look at this kind of thing if we just
bring into that frame of reference of a
macro oscillator what we're really
looking for is Extreme values what do we
actually consider to be a blow off top
type territory and what do we consider
to be undervalued right now some of
these when you kind of eyeball things in
you can say well okay if it's below one
it's probably and we typically see it
down near cycle lows
um 2018 and 2015. and when it gets above
maybe 2.4 or 3 that's typically getting
into some overheated territory but what
I want to do is bring this a step
forward and apply some kind of a
framework to actually measuring that
right because it's all well and good to
eyeball in a number and say yeah it's
it's it's high but what does that
actually mean from a you know a more
mechanical and systematic perspective
so there's another thing we can do here
with the mvrv this is kind of the first
you know just a very very simple model
that we can use to actually track Trends
right so we can take this thing and look
at extremes we can also look at Trends
so this here is just plotting uh the
mvrv ratio against this one year moving
average and you will notice that in in
the week on chain and in many of our
reports we will do this we call this
momentum typically where we're looking
at a faster moving average maybe a
monthly or in this case just the raw
metric itself and it's one year moving
average because that's kind of the
longer term Baseline
um so what we're doing here is measuring
when do we get these periods where the
cycle has changed now why this is really
important you'll notice here in 2017 and
in May 2021 and even back here in 2013
note that we drop very very quickly and
it typically breaks through that one
year moving average with some conviction
and this is after spending a significant
amount of time above it the reason why
is that remember this is a unrealized
profit multiple we're coming off a level
where the market is extremely in profit
but then suddenly is extremely not in
profit and remember in this market cycle
up here we actually I mean here was the
previous correction um up here about six
thousand seven thousand before the final
parabolic run we traded down to that
same level but you can see that the
profitability of the entire Market
absolutely collapsed so if you think
about that price has gone up gone to a
very high profit multiple but then
collapsed well and truly below where it
came from so there is much less
significantly less profit in the system
following that event
this can only happen when there's been a
lot of redistribution coins have been
transferred on this final parabolic run
many coins have gone from a cost basis
of 200 300 500 a thousand three thousand
dollars up to a cost basis of twenty
thousand so now that you have coins at a
much higher cost basis the mvrv ratio
this momentum break to the downside is
signaling that we probably have a
significant Trend shift underway
the same is true when we come to these
upside moves in 2019 was a great example
2015 another great example
typically when it breaks above that one
year moving average it is generally
because there's a whole lot of people
who've just capitulated out their coins
have been distributed to the lows
somebody else has come in and actually
acquired those coins has been a changing
of hands and you know you'll often hear
me say that it is much easier to hold a
coin when you're in the green than it is
when you're deep in the red what we're
seeing is that switching over of
psychology there's new buyers new
holders the market has essentially
re-established a new equilibrium so what
we get is these very very sharp breaks
to the upside actually creates a degree
of profitability that we haven't seen
for a long time it's a trend shift so in
a really really simple mechanic we're
actually looking for those sharp moves
that typically signal a bit of a trend
shift in the overall Market but at the
in the underlying fundamentals it's
actually a whole bunch of people who
were in profit suddenly are in a loss or
at bottoms it's a whole lot of people
who are in a loss capitulating out and
then returning to a profit so we're
seeing this kind of changing of hands
showing up in the mvrv ratio
now the other thing I want to touch on
just quickly before we get into some of
the uh the statistics is a bit of the
mechanics so we just understand what's
going on here that concept that we just
talked about in terms of Shifting
profitability this happens on both a
macro and a micro time scale so this
chart here we've got two traces we've
got the realized cap itself which is
obviously what the mvrv is derived from
it's kind of the on-chain cost basis is
the right way to think about this it's
the
um valuing every coin at the price when
it last moved and then in the green
we've got realized profit
now what that means is if a coin was
bought at five thousand it spent at ten
thousand there's a five thousand dollar
profit times the coin size right 0.5 BTC
or whatever it is that's on the move
now what you'll see is that during
periods of heavy profit taking
this realized cap will climb because
people are revaluing cheap coins to
expensive coins quite often selling to a
buyer who it's their first coin bull
markets are very common for the smart
money from the previous bear Market to
have very cheap coins basically doing
the exact opposite of what the market
should be doing which is the new money
coming in and saying hey I love this
sixty thousand dollar Bitcoin despite
the fact that in many instances it's the
exact wrong time
now you can see that there was this
second leg we had this second Rally from
August through to November 2021 and
we've covered this quite a bit this is a
bit of a funny rally it didn't really
have the momentum behind it and we're
going to discuss why what what was going
on there but you can see that we had
this second rally these extra profits
were taken and we had a second push
higher
the 2022 bear Market we then essentially
flushed out all of that capital and we
returned we essentially flushed out all
that excess speculative premium got
removed from the market but the
important thing to note is that the peak
profits were occurring at the exact top
which is literally profit taking and
that's those coins getting transferred
up to a higher level higher cost basis
more price sensitive
so we can look at that concept and the
signals that the mvrb is telling us on a
macro and a micro scale so on the left
hand side here this is the macro scale
what we're looking at here is mvrv
between the two 2021 Peaks now price was
at a higher level in October and
November
but there was less profit you can see
this big negative Divergence that's in
play there is less profit in the system
despite price being higher and you have
to wonder how does that happen because
the average cost basis of the market was
much higher there was literally less
profit in the system because the average
cost basis was up at a higher level and
the reason why that cost basis was at a
higher level is because a whole stack of
people took profits on one and then two
peaks so what this is really describing
this big negative Divergence here is
describing a top heavy Market you're
seeing in a situation where price is
higher because less profit you've got a
top heavy Market there's lots of coins
located up in that 50 60 000 realm
um and then you can basically when price
Falls below that you have a much more
sensitive Market any kind of price below
suddenly people start going hang on a
second I'm no longer in the green and uh
people start to get panicky and then the
bear Market ensues and naturally these
things all happen within the context of
everything else right you've got macro
and various other indicators but
essentially this is providing you a nice
framework to say well at the very least
within the context of Bitcoin I know
that this Market is far more sensitive
right now at this all-time high than we
were at the previous one so it gives you
a bit of a context now let's flip that
around let's just imagine in 12 months
18 months two years time we're back up
at all-time high right 70 000. because
there's going to be a whole lot of those
coins bought at 50 60 000 that have been
reallocated down here at 20 or 30 or 40.
this mvrv ratio in theory should be much
higher if on the other hand we get up to
that all-time high if price gets back to
70 000 and we have yet again another
very low mvrv ratio you start saying
hang on a second there's and we've also
got profits being taken you start to
think maybe this team doesn't quite have
the legs yet because you're seeing
people Distributing and basically taking
uh taking those profits
now that same concept applies at a micro
scale as well you can see here in the in
the um April uh to May 2021 Peak higher
and higher highers in price but decaying
profitability this is literally the
process of distribution taking place
which you can see distribution taking
place as profits were taken all the way
through this topping pattern which as we
all know how that story played out
and we can actually see this in our 2013
uh 2017 cycle as well in 2013 price
actually rallied between the two peaks
it was up 392 percent and yet mvrv at
the at the all-time highs was actually
lower so even though price was up 392
percent the amount of unrealized profit
in the system was much less
2017 very very similar story we got up
to these levels and we started seeing a
decaying or a weakening of our overall
mvrv despite price being up 65 56 and
then blow off top
um and actually you can see at the
all-time high itself we also had a
negative Divergence so the mbrv can be
used and to try and gauge risk in this
market as things are starting to devolve
and you're seeing coins transferring
around the system this is kind of about
a macro and a micro scale you can start
to observe whereabouts the system is in
terms of uh that profit taking when
you've got risk in the market top heavy
and obviously you can then break this
down into various cohorts and look at
this in even more detail
okay so that's kind of the the concept
and the structure and what the mvrv and
a big picture just some you know some of
the use cases that certainly I pay
attention to
um what we're going to do now is a bit
of an exercise to show you how I think
about probability right how do we make
this a more actionable tool because it's
all well and good to be looking at it
divergences and getting really in the
weeds but for for many people we're just
looking for what classifiers as an
extreme value
now the first approach that I mentioned
before is just to eyeball in some levels
so here I've put in some levels here at
3.2 at the top 2.4 right two levels that
kind of represent like super overheated
and hot and I've also got levels here at
one which is actually Break Even price
or at the mvrv and then 0.8 which is a
20 discount now these are just eyeballed
in right I've just kind of picked
numbers that seem to catch you know oh
that looks about right but obviously the
market can change and evolve over time
so it's not the most robust system but
the concept will still carry forward
so now that we've got these levels how
do we actually assign a probability
framework how do I give some kind of
robust level to say well maybe that will
work and with what kind of percentage
probability
so a tool that I like to use
um yeah this is in workbench we're using
an if statement here what I'm basically
saying is that let's just take the level
of 3.2 which is our red curve if price
is if sorry if mvrv is above that level
return one if mvrv is below that level
return zero so for every trading day and
I'm going to do a cumulative sum so for
every trading day let's say there's been
300 days out of the 6000 that bitcoin's
been trading that we've been above it
I've got a ratio of 300 days above 6 000
below give me that as a percentage
that's essentially what this metric is
doing for those four different levels so
the way to think about this um let's
take our red curve here at our current
level we're somewhere between six and a
half seven kind of in that ballpark you
can see it's actually been quite stable
for more than five years now so we're
talking about somewhere between let's
just say five and seven percent of all
trading days have been above that level
well that means that 95 of all trading
days have been below it
so if I see an mvrv that's above 3.2 I
know that there's only five percent of
all history and the the logic here only
five percent of the time have investors
been willing to sit there and go I love
this green portfolio and not put a top
in so when I'm above that level we're
talking about a fairly improbable
scenario when I'm below that level
that's kind of the mean that's the norm
95 of the time we're below that so
therefore human behavior is probably
going to start stepping in when you get
above that level
likewise for the blue curve this is the
one 20 below
um uh the markets are 20 loss this one
here we're talking about 3.9 percent
four percent five percent so similar
ballpark for round number let's just say
five percent 95 of the time mvrv is
greater than 0.8 so therefore if we
reach a number that's at 0.8 it's an
improbable scenario we can start to
assign probabilities to these things
and you will see here that yes I
eyeballed in those horizontal levels but
they're also rough you know there's a
bit of logic and thought behind it our
our very extreme both to the upside and
downside level about five percent
meaning 95 probability that we're
outside those bounds
for the other two somewhere between
about 15 and 20 right so I'm looking for
things that represent extremely
overheated with five percent probability
and stuff that's starting to get hot or
cold
um which is in that 15 to 20 type range
but this is just a really simple
framework to understand How likely is it
that this level is going to be hit or
tagged
so what we can then do is use the if
statement to essentially put some really
nice color bands onto this thing and we
can start to identify periods where we
are in heated and overheated territory
or we are in cool and extremely cool
territory so we can use that tool to
then say if
um if prior or mvrv is below 0.8 it
means that I have a 95 probability that
it wants to be higher than 0.4 than 0.8
over any kind of long term now naturally
this this all of this assumes that mvrv
continues to do what it does but the
nice thing about it is we're essentially
basing it in one of the most fundamental
metrics which is the realized price and
the realized price is going to react to
every single transaction on chain so
therefore your assumptions boil down to
if people continue to move coins around
on chain at a meaningful level then we
can expect that this thing will continue
to represent some kind of unrealized
profit and loss ratio so we're trying to
simplify a nullify risks to this thing
deviating over the long term
but the other assumption we've got here
is we've just eyeballed in horizontal
levels well what happens if Bitcoin
really does grow and we end up at a 10
trillion or you know 100 trillion dollar
asset and volatility squeezes out and
profit multiples of 320 no longer really
matter what happens if our base
assumption here is that those horizontal
levels is actually that's kind of the
weakest point in this analysis
um because we've eyeballed it in and
we're just kind of hoping that those
horizontal levels remain uh long term
so we'll come back to that in a second
um the last thing that we can do is
because all the mvrv is just a ratio
between spot price and the realized
price well if we've got an mvrv of two
that means that price is trading at two
times the realized price
so you can actually multiply we've now
got our four extreme levels 3.2 2.4 1
and 0.8 let's multiply the realized
price by that to develop pricing levels
so what this is essentially capturing
and you can actually see these levels
where things got really heated in 2017
things with things got really heated in
this is the price level
where there's only a five percent chance
that we've ever been above it it's
basically saying that when you're if you
reach that kind of pricing level that's
where the human behavior that we've been
talking about the I'm in so much profit
I need to take it or I'm in so much loss
I need to get out of this thing we're
looking at the pricing levels where we
would typically see that type of
behavior kick into gear so it's just
giving us a bit of a frame of reference
on where we sit within the market and
what I like I mean you can see here that
during the bear Market we tend to sit
between these two Behavior levels and
then we go through this long process of
transitioning up to the heated Zone and
once we break into this heated Zone
typically speaking here we are in
December 2020
um here we are back here in the early
2017 we're typically breaking the
previous all-time high so generally
speaking we see lots of things kick into
gear Bitcoin is just surprisingly
cyclical as we break the previous
all-time highs smart money start to
distribute in larger size that it starts
showing up in headlines new buyers come
in and you go through this extreme it's
like this big um uh big kind of tick
tock that goes back to back to front
where you see all of the the bull market
Mania shows up and then you cool down
and you have all the bear Market
catastrophe and these things tend to
show up in a very very similar cyclical
patterns
so in order to address the horizontal
level problem which is basically the
most arbitrary part of what we've got
here
we can actually use a bit more robust
and meaningful methodology
so the blue curve that I've got here and
again I'm using workbench to calculate
this I'm just doing a cumulative mean
this is basically calculating the
all-time average what is the all-time
average of mvrv and this is essentially
going to follow as mvrv evolves you can
see it's actually quite stable over time
but as mvrv evolves and changes and
moves over time this thing will follow
and adjust you can also set this to like
a four year basis so I've got some ghost
traces here to show you what we do if we
do a four year average there's all sorts
of things we can do but for the sake of
Simplicity we're just going to do an
all-time average
now for those who are familiar with
Statistics we can also then measure how
many standard deviations above in this
instance one above in the red or one
standard deviation Below in the green
you can start to set up okay show me a
statistically meaningful deviation when
are we actually well and truly outside
those boundaries now of course there's a
little bit of arbitrary what classifiers
as significant one standard deviation to
half
that that kind of number then comes into
it but very typically if we're looking
at plus or minus one standard deviation
it will give us a reasonable bound and
that's that's we're going to keep it
simple here
um but we're essentially it's a bit more
of a statistical framework rather than
just a horizontal level and kind of
finger in the air measuring days and
things like that
so what we can then do is calculate via
that exact same methodology let's just
use our mean plus one standard deviation
in the red mean minus one standard
deviation in a blue and again you can
start to identify periods in time where
the mvrv is extremely hot we're seeing
there's a lot of profit in the system
people are more likely to start spending
likewise during our bottoms we're seeing
that point in time when there's so much
red that people start flushing out you
get a changing of hands and that
typically puts in a cycle change in both
directions now naturally you can compare
this to that momentum oscillator we
looked at at the start and you can start
seeing how mvrv just by itself gives us
a really really nice framework for
what's going on across the market you
start getting Confluence across many of
these elements have we seen a trend
shift have we seen a bunch of
profitability drop out of the market
have we seen that we're at a one well
1.2 or 1.5 standard deviation
um from the mean you can start gluing
these pieces together and saying do we
have all of these divergences in play
and thus a cycle change May well be
underway and again it's based in that
human human behavior pattern
and we can also calculate via the exact
same mean a series of pricing bands
right plus or minus whatever standard
deviation level we want to look at here
I've just plotted out minus 1 minus 0.5
plus 0.5 plus 1 but you can see we
essentially achieve a very very similar
result where you can start looking for
periods in time when the market is just
well and truly out of bounds and it's
time to just start saying yeah this is
this is getting pretty heated start
looking for those divergences right
we're above this red band you can see in
2017 for example we were Above This
level for some time so we can persist in
an overheated state for some time
likewise at the bear Market we can beat
down here for several months six months
eight months these are not short-term
things but it's a signal to start maybe
looking for those divergences in the
opposite direction right so it gives you
a bit of a framework to say all right
now I can start thinking about are we in
superheated territory and what are the
metrics I need to then look at from that
point onwards and likewise when you're
up loads of bears you can start changing
that framework and saying all right
start looking for that capitulation
Behavior start looking for that changing
of hands sharp moves in percent Supply
and profit things like that so it just
helps you Orient yourself within the the
Maze of markets
so that framework that I just walked you
through that concept of taking standard
deviation bands and you know different
levels in terms of what we're looking at
in terms of statistical levels
we can apply that not only to mvrv we
can also apply that to many other
oscillators with a little bit of work
here and there but the other day we
started we actually released this
dashboard which glues together that
exact same framework using the
cumulative mean and the standard
deviations for four four crowd favorite
metrics mvrv ratio which is unrealized
profit and loss we're trying to capture
different segments of the market so is
the market in an extreme level of profit
or loss on paper
sopa which is saying is the market
locking in extreme profit or loss on
both sides
the pure multiple which is then saying
are minor revenues at some kind of
extreme are the production side
typically miners are operating at the
extremes at the bottom of a bear Market
they're selling into an already weak
Market they're capitulating they have to
empty their balance sheets um they're
under extraordinary stress and in a bull
market they're mining coins typically at
a power price that's much lower than the
current price and as price goes higher
those 900 BTC become an increasingly
large USD sell side so we're looking at
the mining perspective or the production
side
and the last one is the reserve risk
which is capturing the amount of hodling
that's taking place so essentially we
can start to distill all four of these
to say do we have all four of them out
of bounds and that's what this signal is
trying to capture is trying to pick up
points in time when we have Miners and
an extreme amount of profit we have the
markets in an extreme amount of profit
people are taking extreme profits and
the amount of hodling is pretty much at
an all-time low pushing reservers higher
so when you have all of those conditions
it starts looking like you have some
kind of Market cycle Peak when you have
all four of those conditions in the
exact opposite everybody's underwater
everybody who's selling is doing so at a
significant loss the miners are under
extraordinary pressure and their
revenues are wrecked and then the last
component is is huddling at all time
high because the hardlers are the ones
willing to step in during the most
bearish price action so this tool which
you'll find under our signal section
again this is all available for our
Advanced members
um is essentially distilling down those
concepts for each of these four metrics
using our main and plus or minus
standard deviation bands and then just
simply aggregating them together
so that's the uh that's the snapshot of
the run through of just some of the many
things you can do with the mvrv ratio
let me just jump back to my cover slide
because we will start to move into some
uh some questions
um so as I mentioned everything that we
just went through in that session is
contained within that mvrv report and
you will also suggest the live dashboard
for both Bitcoin and ethereum covering
every single step of that process and
then that signals dashboard is also now
live for all advanced members so you can
there's a free trial to get you started
with Advanced
um but really that's what we're trying
to do is break down these Concepts help
apply a bit of a probability framework
to things help people use these tools to
navigate Market extremes and there's
lots of ways you can use it you can use
it for just spotting Market extremes you
can use it for trying to just change
your ball versus bear Market thinking
you can use it as a bit of a compass to
try and just work out whereabouts we are
in the cycle but really if end of the
day it comes down to at what level do we
engage and kind of fire up people to
make the same decisions and this is the
thing I I try to impress upon people for
entree analysis is just a beautiful tool
for visualizing human behavior and while
the asset may change the Year may change
the market may change Jay Pal's comments
may change all these things in the world
will change but the reason we can still
chart price action back in the 1920s and
it looks exactly the same as today is
essentially because the human behavior
pattern our response to fear and greed
and profit and loss are pretty much the
same right the human ape brain doesn't
change despite the fact that the uh the
asset and everything else does so
on-train analysis is just the first time
we can actually see this
um printed out block by block
for these assets which are just
incredibly emotive right that's that's
kind of the uh part of the nature of
these things
so with that said um let's move across
to uh question and answer and uh see if
there's any uh queries that have come up
let me find the Q a tab
okay
okay so first question here um can you
please explain Young Supply realize
price and old Supply realized price in
the last research report
um great question so what we're looking
at here is
um when you so let's start with old
Supply when we look at old Supply and
Young Supply or long-term and short-term
Supply what we're really doing is trying
to understand the different components
of the market and if we did some
research um uh some time back now
actually I think 2020
and that that was kind of associated
with our long-term short-term Supply
um and the concept here is that when we
look at statistically speaking when you
look at all of the coins within the
Bitcoin Network generally speaking
um those that are older than five or six
months somewhere around the threshold
about 150 155 days the probability that
they get spent is significantly lower it
declines below one percent it's like a
very rapid decay
so any coin that's older than five or
six months it's very improbable similar
concept we just looked at in terms of
probabilities it is unlikely on a
relative basis they get spent conversely
the young supplier the coins that are
younger than that um that five six month
threshold those those coins make up the
vast majority like 99 point something
so what you're basically looking at
there is that the young suppliers I you
can also think about like the liquid or
the active or the mobile young supplies
the stuff that's always churning and if
you if you think about from from this
perspective
I don't particularly care as a Trader or
an analyst I don't particularly care
that the guy who bought yesterday sold
today or the guy that bought two days
ago sold sold today because it's all
just kind of part of the mix right it's
part of the daily trade volume what
actually matters is is the guy who
bought his coins five months six months
one year five years what happens if a
bunch of those old Supply starts
spending
so when we're looking at their realized
price what we're doing is breaking these
out into age base and therefore
probability based cohorts and what we've
seen historically through bitcoin's
Market cycle is that those old Supply
the older hands the people who
essentially have held their coins for a
long period of time generally speaking
they start Distributing and spending
their coins on mass during two's
particular events one when we break
above the previous all-time high
generally speaking those longer term
holders start spending on mass because
they see that Bitcoin is getting
expensive they bought their coins much
cheaper and they start realizing profits
into the Raging Bull Market
the other place that we see in the
spending is actually well maybe not
quite so much right now but certainly a
couple of months ago
um we see them at the very very bottom
why because bear markets typically last
for longer than five to six months in
this case and by my account
um I believe that the bear Market
started in May 2021 that's kind of when
the psychology shifted which what MVR
they also showed us as well that
psychology changed those old hands five
to six months are actually top buyers at
that point in time people who bought
during the 2020-21 cycle or 22 cycle
they typically become the old the old
hands the old Supply and you can see
that they're realized price will go up
and up and up and the higher it goes
it's showing you that the average
acquisition price of those buyers is
substantially higher so what we're
looking for there is that Young Supply
typically follows the price it's much
more responsive because it's daily churn
the old Supply realize price is trying
to capture those folks who essentially
are either the smart money who bought in
the bear and are selling in the bull or
the people who were bought at the top
and have finally just seen enough they
often drive that price action at the
extremes whereas the Young Supply kind
of picks up all the the
um the daily trade and the daily
momentum
um uh how that works out
okay
um so question here um uh which exchange
is used to calculate BTC prices and
volumes and what percent of transactions
do I believe are captured by the above
um and are these all on-chain transfers
so um for what we're doing we use an
aggregated
um price so in terms of what the spot
price is
um generally speaking I mean Bitcoin is
a bit of a unique asset because
generally a stock trades on the New York
Stock Exchange and that's kind of it's
home that's where it lives that's where
it's price action happens Bitcoin is
unique in this well this this industry
digital assets are unique and that they
train all over the place in different
places
um around the world so we use an
aggregator price to try and map out
where that is
um in many instances it's kind of you
know plus or minus it doesn't you know
the actual Delta in terms of what the
precise price is
um as long as you're not looking at
exchange it's got extraordinarily High
spreads we typically see that between
the major exchanges which form the bulk
of the uh of the pricing
um you typically get Arbitrage that
keeps them very very close together over
time the realized price is then looking
at the price at the point when each coin
moved so at a block by Block Level we
look at each utxo and we assign the
price when it was transacted because
each transaction has a time stamp
um well the block that that transaction
is in has a time stamp so we take that
time stamp we assess what the price was
at that time and we assign it to that
utxo and from that point when it's spent
again and mined into a block we can
measure the price Delta and therefore
the value Delta so it is the mvrv spot
price market cap off chain
realize price realized cap in the
denominator on chain and we're gluing
those two together so it's a bit of a a
meld between those two
foreign
the other way actually just one final
point on that to think about this um for
mvrv you've got market value which is
basically the price that everybody sees
right and then you've got the realized
price which is actually individual what
we do is we aggregate it to be an a
holistic view of the whole Market but my
realized price is different to your
realized price because you and I are
quiet our coins at different times so
the realized price is actually it's it's
much more Divergent if it actually every
single coin has its own realized price
what we're doing with mvrv is gluing
these things all together and just
looking at an average across the whole
market and bring it back to that
previous point we can do short-term
holder mvrv only looking at the profit
and loss held by recently moved Supply
or we can do long-term holder mvrv only
looking at the overall behavior of coins
that are held by older hands so you can
actually break that down even further
okay how would I classify mvrv
divergences for daily analysis and swing
trades is it a leading or a lagging
indicator it can actually be both so um
and again it kind of depends where you
sit in the cycle
um you can see that those divergences
basically what you're looking at is that
these Peaks it's about relative levels
right are we seeing more profit into the
system as price goes higher as we come
out of bear markets small price changes
and you'll see this in things like
percent Supply and profit as well as you
start to come off the lows a very small
price change 10 can create 13 14 15 20
increases in the amount of supply and
profit so during those transition points
typically mvrb is very very responsive
right the amount of movement is very
responsive over the macro scale that's
where you look for these just much
larger Divergence so it does actually
work as you bring it down to finer time
frames you will see these things like
does the change of mvrv match the
percent change of price so you can go
down to actually quite fine detail and
even within micro peaks and things like
that so certainly it will tell you
what's going on in those certain levels
but remember the underlying basis is
we're looking at changes in coin
distribution small changes in coin
distribution may not change the the
market very much but at Market cycle
tops you get the most extreme changes
you get very very large sums being
distributed near the top so it kind of
scales alongside the market when we're
just kind of day-to-day chop mbrv will
be less responsive because the
difference between the market being and
130 profit 140 profit yeah but the
difference between being in 240 and 320
percent that's a very significant change
that typically happens over a very very
short time scale so it does kind of
change
okay so a question here on the link
between mvrv Zed score and the
probability lines so the Z score is
literally plotting out how many standard
deviations we are so that second version
where I have the cumulative mean and the
cumulative mean plus or minus one
standard deviation mvrv Z score is
literally plotting out how many standard
deviations we are away so if mvrv Z is
at one that means we are at that top
plus one standard deviation band if
we're if mvrbz is at minus one it means
we're at that lower level that blue band
so it's actually plotting this out in a
pure statistical framework that's
exactly what mvrvz is doing
is there a way to use mvrv to spot the
picotop of the cycle uh it seems price
keeps going up even when it's in red
territory so the answer is there is no
metric tool answer to the picotop
um and looking for one is generally uh
the problem is if you look for too many
of these things try and look for the
picotop the reality is the market could
do something completely different right
and if there was a perfect answer to
these things
um everybody would be rich and we
wouldn't have to sit here in a webinar
um the the concept here you're
absolutely right it will break above
that red band remember
the the selection of that plus one
standard deviation that's the arbitrary
decision that we made for this and the
reason why is you just do plus or minus
one and we're trying to spot just
overheated conditions you could refine
that you could use MVR v z score and you
could look for levels
um you could look for levels that are
within your framework right you could
actually have a level for plus one plus
one point five plus two and you can
establish like the higher this thing
goes remember that probability framework
95 percent of the time we're below it
but they're still five percent we're
above and sometimes we're much above
what if that was two percent or one
percent or 0.5 percent
the thing what you're doing there is you
will start getting into picotop
territory so to speak if you keep
incrementing up how high how high do you
want to go the trade-off is that the
more your percentage goes down to one
percent zero point five percent you may
not hit it so if that makes sense you
may actually not get to that level
um because the market just happens to be
different that particular cycle so the
answer is you can do that
um but the challenge is you're then
reducing the probability of that event
happens in the first place so you know
there's no Solutions only trade-offs it
certainly falls into that bucket
okay
um uh great question here can you unpack
the realized price calculation given how
much of the Acquisitions
um uh BTC take place off chain fantastic
question
um there is a workbench chart or a
couple of workbench charts in our
presets under the exchanges category
um and they are designed to answer this
very question
um a lot of people don't realize this
but every single day hundreds of
millions to billions of dollars of
Bitcoin Flows In and Out both directions
so when you look at exchange netflow
it's like you know 3 000 Bitcoin 4 000
Bitcoin 10 000 Bitcoins a big day but
that's net that's inflows minus outflows
inflows are typically like
50 60 80 a hundred thousand BTC and
outflows are 50 60 80 100 000 BTC
so this is actually a question that I
contended with quite a bit in the
2021-22 cycle as I'm kind of I mean I
myself am growing as an analyst I was
trying to understand this question
because I saw lots of people saying you
know oh all the trading happens off
chain well that's true but the inflows
and outflows is typically somewhere
between like 30 and sometimes 70 percent
of spot volume
it's huge so there is a stack of volume
flowing in and out
um the other thing with Bitcoin um is
that the data is quite clean in the
sense that there's not that many dexes
certainly not ones with any kind of
significant volume on bitcoin so when
people are buying and selling those
coins are still going in and out of
exchange so the way to think about this
the realized price if you look at the
realized price on an individual basis I
may buy my coins at thirty thousand and
then I may withdraw them at forty
thousand so the on-chain transaction
will pick up a ten thousand dollar
difference
but I still made a decision to withdraw
at forty thousand I didn't sell I chose
to withdraw it and then when I send it
back I kind of don't have a choice right
you can see it because it's on chain so
in many ways when you look at an
individual level yeah there's some error
bars but when you look at it in scale
over time in aggregate you still see
these patterns play out time and time
again and a lot of this is driven by the
fact that the coin volume flowing in and
out is just truly extraordinary so if
you do want to have a look at this
there's a USD and a BTC version of this
go and look at on on workbench under
exchanges look at how small net flow is
and this tiny little black squiggly line
compared to the green and red which is
just enormous on both sides so that's uh
that's generally how I would answer that
question
uh would I combine in vrv with a
momentum based oscillator
um yeah apps just fine support and
resistance absolutely um mvrv is one of
these really nice things to help you
Orient yourself are we in market
conditions that look like we're in a
more constructive environment are we
seeing sharp changes so in many ways
mvrv is great to actually assess and and
help Orient yourself larger and like you
know for many people help you get your
longer term time frames in check and
then you can go look at all your other
indicators within that framework
um for some of you who are actually in
really in the weeds and looking at those
micro divergences it can then also be
part of that internal framework but
um really if there's kind of a takeaway
I think for most advanced members having
this tool is kind of that that grounding
anchor to just understand where we are
in the cycle of things is probably a
nice a nice way to go about it
uh we've got another question here in
terms of self-transfers and
consolidations
um yes in terms of self-transfers and
things there will be some
um that's again some signal loss there
that said we also have um our entity
adjusted variance which will account for
internal wallet transfers so you can
compare your
um uh standard mvrv
um to your entity adjusted mvrv and that
will clean up a lot of that um a lot of
those internal transfers and things like
that and also exchanges and the like but
generally speaking
um with exchanges if you're looking at
their hot wallets because they're always
on the move they just kind of track
price so the way that mvrv like the
realized price for an exchange hot
wallet is one because it's just like 1.1
1.2 because it's just kind of moving
with price so in a way it actually
self-nullifies because it's kind of just
moving around and not doing much
um it's it's kind of the extremes that
really make the mvrv sing so in many
ways it's actually self-correcting which
is kind of
um great question I get this all the
time how does tax loss harvesting affect
mvrv
tax loss harvesting will show up as a
sale right because somebody's moving
their coins from a high price to a low
price
but the other thing to think about that
is that people always tax loss Harvest
we're seeing the exact same behavior
playing out time and time and time again
human beings are making the same
decisions collectively at the same time
going gee it's a bear Market I'm very
very underwater some guys say I'm going
to harvest that tax at the exact same
time that some other guy goes that's it
I hate this asset get me out of this
thing I'm done I'm tired of seeing this
red the same behaviors show up with each
cycle so the answer is tax lost
harvesting will show up
um and and respond to this or so mvrv
will respond to that
but it always responds to that and human
beings make the same decision every
single time so again it's kind of one of
these neat little self-correcting
phenomena that um yeah it happens but it
happens every cycle so we're comparing
apples and apples
okay uh underlying assumption here of
realized price uh is that it's
essentially an acquisition
um I think I kind of covered this the
answer is yes on an individual basis
your error bars are a bit larger but in
aggregate we continue to see that people
tend to behave the same way over and
over again so uh it's kind of a funny uh
funny uh situation can I calculate mvrv
based on the API data use you can it's
literally spot price divided by realized
price or market cap divider by realized
cat the only difference there is
circulating supplyable nullify and
cancel each other out
okay what else do we have just trying to
go through and find
questions here that are separate what is
the name of the indicator and workbench
with the only two bands of mvrv um it's
called Uh deviation bands um you'll find
it under market indicators I believe if
not if you can't find anything that I
went through in this presentation
dashboards Bitcoin or ethereum profit
and loss and mvrv it'll be sitting in
there
okay let's keep going
I'm just trying to see if there's any
more questions here that are kind of uh
unique and different
yeah there's a point here about um
short-term and long-term holders this is
where if you look at in fact in in
workbench as well
um uh you will find long-term and
short-term or old and young Supply mvrvs
which is just to take the ratio between
their realized prices you can use those
to kind of segment the markets that hot
money cold money and you can actually
see these patterns play out time and
time again so you can compare standard
mvrv which is everybody Young Supply
mvrv which is the fast bot money and old
Supply mvrv which is going to give you
the older hands and you'll you'll see
that during some periods of time their
behaviors are very similar typically
during Market extremes they diverge
significantly because the old suppliers
and huge profit the young supplies at
they're at profit but they're pretty
much buying the top so you'll see these
things diverge and then they'll also
diverge in the opposite direction near
Market bottoms because the old money is
the ones from the previous cycle all the
smart old monies got out and those old
money who are left the kind of people
who are holding the bag and you know
very very red in their portfolio and
when you start to see them recover which
we're in the process of trying to get
above that's what we covered in the week
on chain that's the general framework
for those
okay I think that's pretty much uh
pretty much all the questions there's
one here on Sovereign Roll-Ups which I
wish that I could answer
um I don't have I actually haven't
looked into it enough uh so I can't give
you any kind of uh a proper response on
this one
um but uh one thing I am very excited
about and you know we've seen this
ordinals and inscriptions start to play
out at least from my personal
perspective the most exciting thing for
me is that we have a wave of innovation
that has come back to bitcoin
um and this is very exciting to see and
you know I fall into the camp where
Bitcoin is a pretty resilient and hard
to kill animal and uh if you know
inscriptions or Sovereign Roll-Ups or
any of these things kill Bitcoin then it
was destined to die
um I believe that the the amount of
innovation and interest and renewed kind
of uh engagement that's coming to both
the development but also the adoption
space is very very exciting I think that
uh Bitcoin will you know I think it will
Thrive through this it's gonna we're
gonna learn a lot and we're going to
build some cool things and uh you know
the network will expand and grow from
there and it's a resilient Beast so so
these things aren't going to kill it
so thank you everyone for tuning in
hopefully you found that uh to be a
useful session
um we are looking forward to doing more
of these we'll try and get at least one
more done
um uh for for the month of March if you
do have any feedback or comments or
questions following this we will
actually post this video
um and uh and get it live for you all so
if you have any questions at all either
jump into Forum glass note forum and uh
and ping us there
um or feel free to uh to send us a send
us comment but uh thank you for tuning
in and we will see you in the next one
cheers

# Product Release: Backtesting Strategies and Performance in Workbench

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=h1QOdZXbIps
**Publicado:** 20230329 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20230329-product-release-backtesting-strategies-and-performance-in-workbench.md]`.

---

hello everyone and welcome to a glass
load product video where we're looking
at the back testing tool which we've
just released it's come into workbench
itself this is a really powerful tool
that allows you to test strategies and
portfolios using a whole series of input
data and really it's been distilled down
to a fairly simple format of just an
individual input signal which can be a
combination of essentially any metrics
that are available in the workbench tool
so in terms of back testing a workbench
we're going to explore just a couple of
different examples some of these really
kind of build up the story over time so
you can see how this function actually
works so we'll give a bit of an overview
of the actual function itself and what
the inputs are we'll then go over
everything ranging from a hoddle only
strategy is kind of like a baseline
input we'll then move on to doing a long
only strategy just using simple moving
averages as a crossover
we'll then look at a long and short
strategy using on-chain data in this
case we're going to be using sopa and
then we're going to look at a combined
signal which actually says do we have a
crossover and do we have a super signal
so you can kind of see how a couple of
these constructions get put together
which should open up the the door for
you know other things to start
experimenting playing with
so the actual function itself that
you'll find inside workbench is fairly
simply back test now it takes five
different inputs the first one is the
simulated price so if you're looking at
Bitcoin for example this would be the
Bitcoin price if you're trading ethereum
or even the eth BTC ratio this metric
here would be input as whatever the
price you're looking to trade off
now the first function this one here is
the input signal we'll spend a lot of
time in the examples exploring this but
essentially this is a function that I'm
at zero indicates in fully cash at one
it would indicate 100 long and at minus
one it would indicate 100 short now we
also can apply leverage in this instance
if you were to do it by two or three
essentially this input signal is it's a
multiplier on the simulator price so in
the instance where the simulation is
saying a value of one the overall
portfolio value which we'll touch on in
a second will essentially follow price
one to one at two it will follow price
two to one at negative two it will be
inverse at two hundred percent of the
current price movements so it's
essentially taking the simulated price
and multiplying it by the input signal
relative to the account size
now we also have a starting timestamp in
this format you will find this in the in
the function guide which you'll see in
the description below we then also have
the account size so this is essentially
the portfolio value that will be traded
along the multiplication of that
simulator price so this is the base
account size if this value was a
thousand dollars that one thousand
dollars will fluctuate via the multiple
of this price according to the input
signal
and there is also a relative fee per
trade so each time the volume changes
there will be a fee and they can
essentially be simulated this can
obviously be set to zero if you want to
simulate just the the raw performance
but for strategies that are jumping in
and out of positions then this will
start to build up so we do have a tool
in here to actually monitor and and
regulate those fees
so let's get stuck into workbench and
we'll step through an example going all
the way from a hot simple huddle only
strategy all the way through to a
combined on-chain and off-chain strategy
so the simplest format of a back test
here is purely looking at a Buy and Hold
type setup and really what I want to
explore here because it's it's obviously
fairly uh fairly rudimentary how this is
set up is a bit about the construction
of these workbenches and certainly some
tips that I find uh work quite well
so there's a couple of traces here
obviously we've got our price chart here
in Gray but importantly down the bottom
here you'll see we have what we're
calling our hoddle signal this is the
input value that's going to that second
parameter of our workbench function for
back testing so we've essentially put in
a formula here which is just price over
price which is obviously going to return
a Time series of one that is the same
length and duration as our price chart
we're essentially saying that when the
back test is running we will be fully
allocated at that time
now you'll also note here that I've got
this bar which is set to one and it's
squeezed quite far down on the chart
you'll find this useful if you want to
plot out where your signal is we often
do this where we have a second formula
also assigned to Y2 the same y-axis as
our signal this one here is set to a
value of 10. if for example we wanted to
change this to a value of five you would
see that we can essentially change the
height of where we want that signal to
sit so this is a trick that we'll often
use you'll often see workbench charts
that we build with a dash parameter this
is essentially going to squeeze down
your signal and get into a nice visual
format the trick is just making sure
it's on the same y-axis
so moving on to the actual back test
function itself you can see that the
input function here is M1 which is going
to follow our price our F1 is going to
follow the hoddle signal which is
essentially one at all times
we can see that we're starting this
simulation at the 1st of January 2022 oh
sorry 2020 and our portfolio size is one
thousand dollars and we have that same
trading fee so as you can see here this
is essentially going to simulate a one
thousand dollar position how it
essentially performs over the course of
that time so over this process that one
thousand dollar account size will follow
price at a one to one ratio essentially
it will uh it will move with that um
with prices and we've also got a model
here showing the amount of BTC held
right the the Bitcoin size of the actual
position which is simply the back test
divided by price and it's showing us the
initial buy value
um was about 13.8 million sets so we can
see that this is essentially our BTC
value which is flat and it is simply
following the price chart all the way
through
so setting up for a our first kind of
strategy this is the input structure
just so you can see what we're doing
here we're using just a very simple 20
50 day moving average crossover strategy
so we have here we're using our simple
moving average formula on price
um for 20 days we have a second one here
at f2 which is our simple moving average
for 50 days now what we've got set up
here is that same we've got one two
three formulas which are all capturing
the different scenarios we've got our
20-day moving average is above our 50 so
you can see periods where the red curve
is above the blue curve we've
essentially got an if statement if F1
which is our 20-day moving average is
greater than F2 our 50-day moving
average return a value of 1 else return
a value of zero now we do have a second
Trace here this is actually not going to
be used in our next simulation it's more
so just to visualize what's going on we
essentially have the inverse if it is
less than or equal to then return a
value of one so we can essentially see
when the in a long only strategy when it
would be fully invested during these
green bars and when it would be in cash
during these red bars so it's more for a
visualization tool there
so bringing that across into an actual
back test scenario now we will use in
the orange curve the hoddle only
basically that same buying location that
we had back on the 1st of January 2020
this is essentially this orange curve
down here you can see at the top
um I don't have the bar chart turned on
but this is essentially saying for the
hot lonely strategy it's going to be one
for the entirety of this back test and
this is here huddleback test set to F1
which is our hot oil signal
now in instances when our 20-day moving
average is above our 50 we've
essentially got the if then statement
we've nested it here so rather than
having the 50 and the 20 as an
individual formula we've actually put in
here if the 20-day moving average is
greater than the 50-day moving average
return one else return a value of zero
so for our simple moving average back
back test we're taking the same input of
price M1 F3 is then our simple moving
average crossover signal which will only
be one during periods where this is
green and zero otherwise same starting
date same one thousand dollar account
size same trading fees and you can see
periods during these major sell-offs
where the 20 moves below the 50 that it
essentially moves to a position of cash
and the back test scenario essentially
is keeping the portfolio value higher
during those drawdown periods so it's a
very very simple strategy but really
trying to show how this system actually
works
now of course things get a little bit
more exciting than just doing Simple
moving average crossovers so here what
we've got is brought in a crowd favorite
unchain metric which is SOPA which is
effectively the amount of profit being
realized by all the coins spent that day
so values greater than one is indicating
that the market is realizing a profit
and if it's below one it means it's
realizing a loss now just to clean up
the signal a little bit we've actually
put this onto a seven day exponential
moving average just to make it a little
bit cleaner but what we can essentially
see here is our super signal is looking
at when super on a seven day moving
average is greater than one return a
value of one when it's Below return a
value of zero so we can see that
typically speaking during late stage
Bears we get these periods where the
market is essentially puking out we've
got many investors that bought coins
much higher in the cycle and most of
that transaction activities at a loss so
we typically see that soap will go down
below one particularly on a moving
average basis for extended periods of
time during Bear markers so we can see
here that our super back test which is
again taking F3 as our input formula is
essentially getting into cash as those
losses start to get realized on chain
and it's essentially picking up a
majority of the positive price
performance and looking for when that
strategy actually blows up and soaper
heads below one
now what we want to do here is
essentially look at that from both sides
so I have two different signals here
this is an example of a little bit more
complex but basically a long or short at
no point in this strategy is it supposed
to be in cash it's purely looking at if
Soper is above one then long if soap is
below one then short just trying to
demonstrate how the back testing tool
Works in both directions
so we have all the same inputs that we
had before this orange Trace here is our
huddle curve as our reference now we
have a long signal if super is greater
than one return one we have a short
signal if sopa is less than one return
negative one note that the negative here
is going to pick up a short signal
we then have our long only so this is
purely looking at the previous chart
that we had here's our long only super
back test from the previous uh previous
chart and we can also introduce a long
and short so what we're doing here is
for the input formula now there's two
ways that we could do this we could say
F3 plus F4 which is the long signal plus
the short signal it will either be one
or minus one because at no point in time
is when it's above one it's going to be
either it's a binary signal it's going
to be zero otherwise so we can add them
together inside the actual function
itself we could also have another
function f8 that summed these together
and then the Longshore just to am
ingested that FH signal so it kind of
depends on user preference but the back
test can take an actual formula inside
as the as the input signal
so we can see this red curve here is
fully invested at all times and we can
see that there are periods of time where
it's going to outperform the long only
because you're essentially short during
the worst phases of the bear but you can
also see that sometimes that signal
takes a bit of time to actually adjust
and it can underperform as well but it
really shows how we can have both of
these signals essentially operating at
the same time in a long and a short
Direction
now it is important to note here that
there can actually be leverage applied
here if you were to simulate leverage
one of these signals could say go to -2
and that would be essentially a 2X short
it would multiply the downside
performance and obviously anything
within those those boundaries so you can
test both long short and leverage within
that framework
so the last one I'm going to look at is
actually a combination so we have our
on-chain signal with sopa we're going to
go back to just the long only position
here we're also going to look at the
simple moving average crossover
so here we're going to do it with that
other format we have two different
signals one is the super signal we're
looking at is
um is super on a moving average greater
than one if so return one so that's our
super signal here in Orange we can see
the blue curve here is looking at is our
20-day greater than our 50-day moving
average that's going to return a blue
curve now we can also then establish our
combined signal strategy so I'm going to
turn both of those off
and the combined strategy is essentially
looking at if you have one of those
conditions met 50 and if we have both of
those conditions Matt it's going to
return a value of one so you can see
here that our combined strategy
is actually summing F1 which is our
simple moving average crossover plus F2
F3 which is our super signal and
dividing it by two so it's simply taking
the average between both of those
different conditions and thus will
return a fully invested scenario when
both of them are in positive territory
and it will return a 50 value when only
one of them is and when both are zero it
will essentially move directly out into
Cash
so with that as context we can then see
a orange curve here which is looking at
our super only back test we've got our
simple moving average only back test and
we also have our combined strategy back
test here we're looking at that same
signal summing these two together
dividing by two and we essentially
combine both an on-chain and an
off-chain strategy
so thanks for tuning in for that session
hopefully you found that useful you will
find all of these examples as well as
the charts inside a dashboard under
tutorials in our dashboard section
you'll also find some workbench examples
inside workbench itself and we do have a
fully written write-up and a dashboard
that has all of the documentation and
all the breakdown of these different
case studies so if you do have any
questions please feel free to reach out
for us and we'll see you in the next one
which is

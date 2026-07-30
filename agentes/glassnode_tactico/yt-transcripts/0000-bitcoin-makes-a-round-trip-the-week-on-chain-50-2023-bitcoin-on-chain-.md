# Bitcoin Makes a Round Trip - The Week On-chain 50, 2023 (Bitcoin On-chain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=iqk7Glm9T6o
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-bitcoin-makes-a-round-trip-the-week-on-chain-50-2023-bitcoin-on-chain-.md]`.

---

hello everyone and welcome to your
glasto video report for week 50
2023 so today we are talking about a
series of trading indicators and various
ways that we can actually design and
construct this be a bit more time inside
workbench today designing constructing
tools that can help us spot local
periods of overheated and underheated
because it's one thing to look at macro
tops and bottoms but there are a lot of
tools that we can use to really track
those kind of overheated and underheated
within the context of a macro uptrend or
downtrend for that matter but obviously
we're going focusing on an uptrend for
now now you'll see that this episode is
called round trip because we opened at
about 40,200 at the start of this week
we rallied to a new yearly high of about
just shy of 45,000 and we had a very
very rapid selloff back down to 40,000
1200 where it pretty much closed it's a
little bit up from there now 41 A2 um
but we have seen this kind of overall
round trip and this is kind of a good
opportunity for us to talk about what
does over and underhead look like from
an onchain perspective so really really
cool piece of analysis today a lot more
technical inside workbench but the focus
is going to be building out trading
indicators that's really the uh the
concept here and a couple of Frameworks
to take
forward so as I mentioned bitcoin's had
a pretty spectacular year and what we
really explore during I mean you've
probably seen over the course of this
season if we go all the way back to the
start of the Year bitcoin's trading at
16,000 there was no volatility
everything was quiet we spent a lot of
time looking at what the long-term
holders were doing kind of that big
macro view capitulations that generally
speaking long-term holders are active
around cycle bottoms when we break to
new all-time highs and all the way
through to cycle tops in between all of
those patches short-term holders are
much much more important and you will
notice here we're going to be spending a
lot of time on two very important
Concepts they go together really nicely
the first one is this notion of profit
and loss you'll hear me talk about this
all the time because this really is what
makes onchain analysis just so
unbelievably powerful we'll talk about
two different versions of profit and
loss and cohorts primarily looking at
short-term holders that hot ball of
money that is essentially the most
sensitive to price and tends to react as
a buyer and a seller as the market
jostles around so we're going to start
with a few different levels here we're
going to start with some cost basis
models just to kind of set the scene on
where we currently are and then we're
really going to Deep dive on short-term
holders profit and loss with the
objective here what we are going to try
and design again there's many ways that
we can do this is just one framework or
a way to think about it we're going to
help illustrate how we can design some
trading style indicators using this
concept of short-term holders that hot
ball of money following price and profit
and loss metrics on an unrealized and a
realized basis and we'll talk more about
that in a second before we do get
started please do give us a rate a share
and a subscribe it does help this
channel get to more people let's get
stuck right into the analysis okay so as
I mentioned we're going to just set the
scene we're going to start with some
pricing models and just kind of
understanding where we are in the
broader context of things now what we
can see here this is our daily price
performance now as I mentioned we're
going to be spending more time in
workbench today because I mean this is
essentially where I spend all day every
day um just an absolutely fantastic tool
so much that we can do with it so what
is workbench workbench is essentially a
tool where you can see here I've pulled
in a metric which is just price in this
particular instance and we've
constructed a series of formulas now you
can do all sorts of stuff everything
from complex models to back tests here
we're just doing some very very simple
visualization techniques so what I've
essentially calculated is the percent
change this one here is looking at
essentially how much is the Bitcoin
price changed over each daily period so
literally how much do the price change
in a closing basis um over a period of
one day what I've then done is just use
an if then statement to say I only want
to see green bars when it's positive up
dayss and I only want to see red bars
when it's negative and I've also put
over the top here some plus or minus one
standard deviation bands because really
what I'm looking for is when do we get a
big move right because price obviously
moves every day but show me when the
moves are statistically meaningful and
we can see here that this is actually
the third largest selloff um of 2023
I've got it on the zoom here year to
date this is the third largest sell of
5.7% I believe on a closing basis um so
we did come off quite quickly and quite
rapidly um it did stand out as a as a
sell-off event but as you can see we've
had one two different selloff events
that have been much much steeper than
this this one back here in August we
profiled quite a bit I forget which week
number it was um but this would have
been somewhere in August we looked at it
uh it was called exhaustion and apathy
and volatility Crush as we headed into
it very very quiet market and then a
very very sharp explosion of volatility
that followed so if you are looking at
volatility trading strongly recommend
going out and checking out those
newsletters and videos um because they
really are a great example of using
derivatives and onchain to predict
volatility so where we are at the moment
let's jump across to the next chart I
want to use some onchain pricing models
as well as technical just to kind of
position where we are at the moment so
many of you who watched this channel
will know what the realized price is
down here in blue the realized price is
the average cost basis of every coin in
the supply that includes lost coins and
all that kind of stuff now for those who
read our coin time Economics Report
which again you'll find in the
description below coin time economics
was this framework where we used how
long coins have been dormant to
calculate what we think is a much better
estimate of the active investor cost
bases and that's what's going on here
with this um orange curve I'm just going
to quickly turn off my tool tip so we
can actually see what's going on so this
orange version is actually just the
realized price divided by liveliness I
won go into the technical details
suffice to say this is capturing all of
the active investors we don't care about
all the Lost coins and the early Miners
and the Satoshi of the world let's
exclude them I only care about people
who are active in the market cycle now
this is currently trading about 36,000
this is best thought of as a bit of a
fair value model the market tends to
oscillate around it particularly in 2016
it kind of approached it and as we get
above it we start to move into a bit of
an acceleration phase back here 20 19 we
poked our head above it we spent some
time oscillating around it and really as
we broke through in October this was the
first time that we now got a significant
portion of the market back into profit
so that shifts investor psychology
that's why this really matters because
you now have a super majority of
investors who are active back in profit
so behaviors start to shift we move from
a I bought the bottom and I'm hanging on
we start to move into well 150% isn't
that bad maybe I'll take a little bit
off the table some profits start to get
taken investor psychology shifts but
that's also met by hey prices at $44,000
and demand starts to flow in so this is
what kind of makes for that um shift
from the recovery the uncertain recovery
phase into what we've been calling a bit
of an enthusiastic bull right so we're
now up into that zone where things are
probably going to get a little bit more
spicy now how do you actually measure
what that looks like well we've used
another series of uh of workbench
functions here which we call subset um
so the subset is essentially taking just
a slice of price action between two
starting and end dates and all we want
to see is how much does price oscillate
around this fair value model so you can
see here that 2019 was super choppy plus
or minus um about 50% in either
direction we traded above and below that
level with March 2020 obviously standing
out likewise back here we traded from a
low of about minus 50% below it all the
way up to Breaking Above This was kind
of the start of the Euphoria back here
in 2017 and we've seen here that we've
started from about minus 40% if I
remember reserves um to breaking up to
about 38% above so we're staying to get
this this chop we can see that there's
this choppiness that tends to happen
around this fair value model um we've
broken up from that realized price that
very floor kind of you know all coins
considered we're now up slightly above
that fair value model and if 2019 is any
kind of model there could be some chop
to go along with this now one last um
sector here between there and breaking
the pre the next all-time high which is
where we curtail these this was
somewhere between uh I think it was uh
14 months from memory 2019 was about 20
months we have been about 11 months
since breaking the realized price and
we're obviously not at all-time high
just yet so that would tell us and again
history is obviously just an indicative
but history would tell us that
previously it's been 14 and 20 months
and we're about 11 months into that
Journey so if history is a guide we may
have some choppy volatility and some
sideways and some kind of not going
anywhere ahead of us again none of us
actually know what will happen but just
kind of looking at how the market played
out in the
past now another great model this is a
this is a crowd favorite the mayor
multiple the trusty mayor multiple which
is just a fancy word for a ratio between
price and the 200 day moving average um
yes it's just the 200 day moving average
but why does this matter well the 200
day moving average is important because
every Trader Under the Sun knows what it
is and many of them from capital alloc
Traders all the way through to day
Traders treats it as a bull bear bias
it's kind of one of these models that
because so many people look at it it
reacts because people look at the 200
day and they say well I want to see the
reaction at the 200 day so when
something happens at the 200 day you
know it's kind of a self-fulfilling
prophecy now what's quite interesting is
that where we currently are we haven't
actually got anywhere close to this
level about 1.5 uh I'm actually just
going to show you how I would stick a
new Trace here I want to look at a model
about 1.5 which is where um we tend to
find bit of resistance um for this
particular model now importantly all of
these oscillators you can see here these
oscillator levels um I'm going to go to
the May multiple this one here is
currently located on y4 now when I add a
new formula it's going to assign itself
to a brand new y AIS I want to
immediately change that across to y4 I'm
going to make this particular line
purple because I want it to stand out
and I'm going to set this up at 1.5 and
evaluate so what you're going to see is
a purple line is now going to appear on
our mayor multiple now why did I pick
1.5 because historically this means
we're trading at a 50% premium to the
200 day moving average and during
uptrends we often find some level of
resistance at this point right 50%
premium to the 200 day think about all
those traders who maybe bought the 200
day moving average and they're now at a
50% profit these aren't too bad right
these are numbers where people start to
take some kind of action now we are
currently poking our head up against it
and we actually found resistance on this
level again now you'll also notice this
is obviously just one this is just
eyeballing in numbers right but you'll
often see and we've got a paper called
mastering
mvrv where we do the same exercise but
for the mvrv ratio one of these onchain
models and we put a little bit more
rigor to it right let's actually find a
statistically meaningful level you can
obviously then derive pricing models
from this as well to try and look for
where those areas of you know likely
intersection are but really this tells
that we've bumped our head as we kind of
rally up to 44 and then sold back off it
hit the level where lots of investors
like to take profit and this is the
concept we're going to explore in the
short-term holder front in uh in short
course now the last Model I just want to
quickly touch on pricing model um is the
nvt price Model now this one here is
basically a Fair Value Estimate
obviously all these things are always
models they're estimates they're never
perfect but the idea is that Bitcoin is
obviously settling transaction volume so
let me just leave you with a very simple
concept here
if nobody's moving money around the
system is it really worth that much it's
it's harder to argue that if lots of
people are moving value around the
system it's staying to show that hey
Network effect you've got actual value
being settled so what the nvt price
Model which was developed originally by
Wily Woo is one of these models where we
take in fact we're looking at the
formula here what we're looking at is
the ratio between the market cap or more
correctly the 90-day median of the
market cap circulating Supply and price
divided by
the 90day median of our transaction
volume so um what we're basically saying
is how big is Bitcoin and how much value
is it settling now notice here that
we're using entity adjusted data now
this is actually really really important
because there's lots of transaction
volume that occurs inside exchanges
custodians doing self- consolidation
even investors moving wallets between
themselves or coins between themselves
glass noes entity adjusted data cleans
all of that really really nicely so what
we end up with is a really high signal I
only want to see coins that are
economically meaningful so what this
particular model is doing is saying show
me all the economically meaningful
transaction volume compare it to the
market cap price time circulating Supply
with a couple of medians and averages
and stuff applied and then return it to
the price domain right so what we're
doing is we're saying what is our
current what what is the relationship
between those two what is the current
transaction volume and then equate that
back to the market cap um which you can
obviously then derive as a price now
we've got a 28 day in green and a 90day
here in purple um that quite often
during these uptrends let's look at 2019
and 2020 the 28 day tends to respond
much faster and when it breaks down
below it's actually a negative signal so
you've got this momentum type signal
between the crossover of these two do we
have growing transaction activity over
the fast and longterm but simultaneously
they kind of relate back how much
transaction activity is going on and you
can see we're only just getting the
90-day pickup and the 28 day has only
really broken above in that October
rally so what that really tells us is
that there's a couple of observations
one transaction volume hasn't yet caught
up to the price so you could argue that
price may have run just a little bit too
far too fast the other Insight is that
we've really only seen volume pick up
from October onwards meaning most of
2023 nobody even knew that Bitcoin was
up over 100% very very quiet kind of
shows just how under the radar this year
actually has been in the wake of FTX um
you can really see that following
October we've covered this over recent
weeks in our Capital rotation um kind of
focus we've seen that it's only seen new
money starting to flow back into this
ecosystem after that October rally and
when we broke that $30,000 level which
we spent quite a bit of time talking
about okay so all of that is our context
so that the takeaway message there where
we're setting the scene mayor multiple
got to a level or the 200 day got to a
level where people probably start to
take profits pricing models are kind of
suggesting we we're just a little bit
over stretch there's a lot of people who
are in profit so that the thesis that
we're running with here is that people
are likely to start taking profit now we
know that long-term holders are pretty
dormant until we get to alltime High um
so let's just put them in a bucket for
now we won't worry about those we're
going to look at only the short-term
holders these are people who bought
recently and therefore are the most
likely to start spending now this funky
looking retro chart is again I want to
introduce this we've got our short-term
holder cohort for those who are new and
maybe not heard this before short-term
holders are all coins that have that
moved within the last five months right
they've been mobile within the last 5
months we use this threshold 155 days
because statistically speaking they are
the most likely to spend again most
coins moving around the Bitcoin system
were spent within the last 155 days and
the vast majority of them were actually
spent within the last day so there's
like this massive logarithmic Decay or
an exponential decay of um how How
likely it is for a coin to be spent
based on how long it's been dormant
for so the other concept is profit and
loss so think about this on the rally
where we broke from 30k or above 30k we
had about 5 months oscillating between
26,000 and let's just say 31,000 for
easy math all 5 months people will kind
of accumulate and buying their coins in
that zone when the price broke out this
green line is showing us all the coins
that went into profit in fact I'm going
to zoom in on a slightly smaller time
frame and we will come back out again so
what we're seeing here is the amount of
short-term holder coins that have gone
from in loss meaning their cost basis
was higher than the current price to in
profit now we've also got two curves
here in the yellow we've got like the
30-day low of that particular model so
the other way to think about this show
me all the short-term holder coins that
have been in profit for at least 30 days
that's what the yellow is showing us and
the brown is at least 90 days so let's
just kind of back out and think about
what this means the more of this brown
color that we have this is basically
saying that lots of short-term holders
acquired their coins during a long
consolidation period it's kind of a
robust for um Foundation being ped coins
are changing hands inv are stepping in
and we really traded sideways for 5
months yes it was volatile and it was
choppy but lots of coins changed hands
up here and more and more of these coins
suddenly went into profit because they
built that Foundation that essentially
enabled the rally higher because all
these coins were reaccumulated new
holders in a very quiet period as we
mentioned before and you can see here
that this growing um Foundation actually
supports these uptrends in Bulls notice
also when the bare Market kicked in here
and I believe that the bare Market
really started following the coinbase
direct listing here in April look how
brutal the short-term holders I mean
when the coins in profit are going down
that means that they're now in loss we
had five months of accumulation up here
a massive Foundation this is also a
sensitive point this is showing us we
have a topheavy market lots of
short-term holders are trapped up here
to the tune of almost five in fact 5
million BTC got trapped up here and then
all of them fell into a loss in a very
very short order so again there's lots
of great stuff we can pull out of this
and for those who are into you know
building systematic models and these
types of things it's these inflection
points when these types of models shift
very quickly because you're looking at
lots of people going from profit to loss
or from loss to profit you've also got
these different time elements how long
have they been in profit or loss it
tells you something about their
sensitivity and the robustness of the
foundation that's getting built there's
a whole bunch of things that we can pull
out of this but this is the concept
right I wanted to use this model it's a
really really cool model that uh um that
we've kind of developed just to help
visualize some of these mechanics what
is actually going on under the surface
and how can we visualize this Supply
moving around the system changing hands
and having different cost
bases okay so sticking with our thesis
that people start to take profit what
we're looking at here is for short-term
holders we're looking at the ratio of
how much of their supply is in profit to
loss now the reason why I like you'll
often see me talk about profit loss
ratios sometimes I'll do realized profit
and loss this one here is a Supply in
profit or loss remember that that
inflection point just go back here lots
of people are in profit and then
suddenly they're not you go from very
very few at all-time high nobody is in
loss so you go from nothing to something
very quickly and that nothing to
something is an exponential move because
you're going from zero to anything right
so the concept is profit and loss ratios
are really really good at looking for
inflection points when does the market
change State and what you can see here
bare Market state where the losses
exceed The Profit tends to sustain
itself and we find resistance all the
way through until we get an inflection
point and note that this inflection
point here in 2018 happened very very
close to the bottom because we went from
something to nothing how do you get from
something to nothing lots of people
capitulate those coins go from just
slightly in loss to just slightly in
profit at scale likewise when you get to
these Market tops 2019 lots and lots of
people are in profit and then suddenly
they're not right this thing will start
to trigger an inflection point very very
early in the trend because it's looking
for trapped Traders let's go back and
have a look at this over a one-ear
period just to see how this performed
you can see back here in fact I'll Give
It 2 years just to be a little bit
clearer um we can see that this thing
flipped over before the rally even
started and we can actually see here's a
positive Divergence back here post FDX
because coins are getting transferred
from up here all these buyers all the
way down they Panic sell and they all
wash out so suddenly all these coins
that used to have a 40 50 60 $30,000
cost bases are capitulated out at 15K
and then price goes to 15,000 and 1 cent
and they suddenly go from in loss to in
profit at massive scale and this thing
here flips over so it's a really nice
indicator to look for inflection points
right when do things really start to
transition and shift you can see that
lots of Traders got trapped up here and
this thing indicated that we were and
exhaustion apathy I again recommend you
go back and check out that report we
covered a lot of indicators that were
saying that a big move was coming and
you can start to look at these
indicators and say hey lots of people
are trapped up here the risk is now
elevated now what we can see is that
lots of people are now in profit and we
have hit this level this is the highest
level of profit we've had through the
entire of 2023 so it aligns with the
fact that people are likely to start
spending now remember this is Supply in
profit unrealized coins that aren't
moving coins that are held by short-term
holders so we're really starting to
narrow in our thesis the thesis is
people are probably going to start
selling because we've got to that um you
know we're in a decent enough amount of
profit coming into year close nvt is a
little bit slower we've got mayor
multiple hitting that critical level and
their supply is now heavily in profit
the final question to answer did they
actually spend did we actually get sells
because it's one thing to say hey the
incentive is to sell they're at a lot of
profit but did they actually sell which
is the thing that overwhelms the
inflowing
demand now this is where we move and we
look at a couple of different metrics
we're looking for Confluence two
indicators that tell us the same story
what I've got plotted out here in green
is short-term holder volume going to
exchanges that is in profit right so the
green level here has been ticking higher
since that October rally and actually
peaked as we got to 44,000 the amount of
coins that short-term holders were
sending to exchanges that were in profit
started to tick higher now the blue
curve is showing us the realized profit
so this is the amount of coins in profit
doesn't matter if they're one cent or a
million dollars in profit it's
irrelevant how were they in profit
binary yes no blue is then calculating
the dollar Delta between the acquisition
price and the disposal price when both
of these start to tick higher now you're
starting to say okay profits are being
taken not only is coin volume flowing in
because that's obviously the thing that
needs to be purchased but also the
amount of profit taking is going up so
both of these are telling us profit
taking
events now of course we can also do the
same for losses right and as you can
imagine these tend to move inversely to
each other capitulation events really
start to show up when you get these big
sell-side events and if we just jump
this onto a 2-year
view uh and I'm going to turn off my
green and blue just to simplify things
you can start to see that local lows
when we get these Corrections people
panic this is kind of the nature of
markets people tend to panic and they
sell coins to exchanges in loss and they
take the L even though bitcoin's up 150%
some people sold the exact bottom down
here at 20,000 19,000 some people sold
the exact bottom here at 25,000 before
we rallied some people sold at 26 before
we went to 44 right this is the nature
of markets you know they they move
towards where people are in maximum pain
this is kind of the nature of the Beast
and generally speaking we're looking for
these periods where both the realized
loss or profit and the amount of coins
in profit or loss start to TI higher so
the last I'm going to do is turn these
insights into an actual trading
indicator just try and highlight where
these things show
up okay so all of that was I mean
there's a lot in here right and this may
be one of the videos that uh that you go
back and you rewatch a couple of times
what we like to do here at glasso is
just show you simple Frameworks which
you can obviously refine and build in
and really trying to find maximum value
from data that quite frankly just
doesn't exist in the traditional Finance
world so all of that said we're only
looking at the profit side of the
equation here so again we've got our
volume to exchanges in blue and we've
got our realized profit in green what
we've done here is convert them to a
very very simple Z score so all we're
looking for is how many standard
deviations above the mean are we and the
mean is right here at this red line well
actually sorry this is plus two standard
deviation so I uh forgive me for that
we're looking for periods when both of
those metrics are plus two standard
deviations above their Meme and when we
actually highlight those these are
picking up periods of high profit
realization now again we could refine
this to be 2.6 2.5 three whatever our
particular threshold is but starting to
see when profit taking and the volume
flowing into exchanges is starting to
tick higher we're looking for that
Confluence of both events and as you can
see it typically picks up the rallies
cuz that's naturally where profit taking
tends to occur but it also in bare
markets can help pick up these periods
of elevated risk right right before when
when Profit start getting taken right
before the market needs to actually
flush out now as you can imagine we can
do very very similar mechanic for
realized losses right we're looking for
periods when we've got plus two standard
deviation on the volume and the realized
loss right and again flowing into
exchanges and what we're going to do
here is we can start to see these points
in in time where people are selling the
local lows now of course this thing
doesn't flag every single level no
trading indicator ever does what we're
trying to impress across here is just
where we're getting this Confluence
between two different indicators saying
that people are selling at the top and
selling at the bottom now naturally at
some point that overwhelms demand but in
an uptrend that can often Mark the low
this is that kind of micro capitulation
these are really some of these
Frameworks we can use to track the
market Trend with then a trend right not
just looking for these macro tops and
bottoms we got plenty of tools for that
but we can actually explore these with
very very simple Frameworks within the
trends as well and this is really what
kind of brings some of this stuff to
light um and you know as you can see we
start picking up these areas where it's
just statistically meaningful the amount
of people getting flushed out and quite
often these levels align with short-term
holder cost bases and all this other fun
stuff right so it really does show how
exciting some of these analysis
techniques are because they often tell
and this is my experience onchain data
very often tells a consistent and
cohesive story right just putting all
the pieces together can be a bit of a
challenge but they are always telling
you a very consistent
story and just to bring all of this back
actually let me just shift back a couple
more because you've probably forgotten
the chart about to refer to this is the
chart I'm referring to now we're talking
about a Supply in profit and loss ratio
so this one here I have brought this
across and plotted out periods of where
it drops down below that 20 um 05 level
above the 20 Level and just overlaid it
with our statistical model that we just
covered and you can see that profits
right tend to mark local tops losses
tend to mark local bottoms these are
those inflection points I was talking
about coupled with the actual spending
so let's bring this back to the very
very simple level short-term holder
cohort the hot ball of money that
follows the market around what we're
looking at here is are they in profit
the purple line are they in profit are
they in loss are we seeing inflection
points in their profit and loss on the
coins they hold and then the green and
the red is saying now that they're in
profit did they actually take them and
the answer is yes are they in loss and
did they actually bail out at the bottom
yes you start looking for this
Confluence between these metrics is the
incentive there to do it do they
actually do it now we start talking
about an actual model where people start
spending at the top that profit taking
is what saturates the demand and causes
the correction and at some point in time
people sell the bottom and panic people
who buy the local top they sell the
bottom and the market then just seems to
go up in the other direction this is
just the way that markets work we just
happen to be able to visualize it here
in a very new and unique way so thanks
for tuning in for that session folks
again I know there was a lot in there um
these are some of these more complex and
but this the thing right for for the
last 3 years we've really explored a lot
of the macro side and many of you have
probably learned along with us right and
in many ways I'm a student of this as we
go um so we're kind of learning what
these tools do and we've really explored
a lot of the macro side of the equation
what we're now starting to really
explore is where are these inflection
points where are these zones within a
trend right these more micro type views
how do we actually use this for a little
bit more actionable uh actionable
behavior and try and I mean again we're
just using very simple um simple
statistics here there's obviously people
who can do far more complex models what
we're trying to do is just get across
the framework for how we can use these
models to actually look for Trends
within Trends and get down to finer and
finer resolutions and really taking
maximum advantage of things like our
entity adjustment really cleaning and
getting that economical data profit and
loss metrics which really just are the
be's needs as far as I'm concerned um
and short-term holder cohorts using
these different cohorts to identify
periods where people go from in profit
to in loss and vice versa and thus are
trapped and those people who are trapped
they tend to make rash decisions and
quite often that's what creates this
volatility and really What markets are
all about so anyway hopefully you found
that useful let me know if you have any
questions at all I'll catch you then and
I'll see you next week for our final
report for the year thanks have a good
one
cheers

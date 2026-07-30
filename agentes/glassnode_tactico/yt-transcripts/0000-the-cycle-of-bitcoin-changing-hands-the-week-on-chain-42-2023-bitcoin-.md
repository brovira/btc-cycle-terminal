# The Cycle of Bitcoin Changing Hands - The Week On-chain 42, 2023 (Bitcoin Onchain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=RRmpPN4d-v8
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-the-cycle-of-bitcoin-changing-hands-the-week-on-chain-42-2023-bitcoin-.md]`.

---

hello everyone and welcome to your
glasto video report for week 42
2023 So today we're going to be
expanding our study of capital rotation
last week we really looked at on a macro
view how funds actually transfer and
flow from Bitcoin down to ethereum and
then down to the long taale of assets uh
which we modeled through coins here
we're actually going to go internally
and we're going to look at the capital
rotation that occurs within Bitcoin
itself and this is really describing how
coins change hands they're moving from
one investor to another and with that
and the most important thing to
recognize there is that the owner
changes that means they may go from a
hodler to a Speculator but so too does
their cost bases and the cost Bas is
changing is really what changes the
Dynamics of the market because it's much
easier to hold a coin that's in a
significant ific profit with a low cost
basis than it is to buy the top and see
the market fall out from under you
especially if you are also a Speculator
or a new investor versus a high
conviction hodler so that's really what
we're going to be exploring today the
cycle of Bitcoin changing
hands so Capital rotation is a really
interesting Dynamic it happens across
all assets and all markets it just
happens to be that when we're looking at
the onchain data we essentially get
10-minute resolution for Bitcoin to see
how those Mac flows are starting to
change now obviously these things play
out over different cycle lengths when
you get to bull market tops there's a
very very significant distribution
pressure from those long-term hodlers
the same time when we get down to Market
cycle lows these price insensitive folks
are the ones that establish the floor
but in between those two extremes we
have the short-term holders who tend to
be this kind of hot ball of money that
follows the price around and what we're
going to try and do here is actually
model this out look at this distri
distribution how wealth moves from one
party to the other so we're going to
come with this approach really coming
back to the realized cap you've probably
heard me talking about this uh this
particular metric several times uh in
recent videos the realized cap is just
such an important foundational metric we
have a whole video and a report titled
as such and what we're going to do here
is take two different pieces or two
different models um using nupal which is
one uh kind of crowd favorite metric
looking at the net unrealized profit and
loss in the system and we're also going
to look at it from the perspective of
the realized cap hle waves so taking two
different instances of realized cap and
showing you how we can develop two
indicators that actually monitor the
progress of this cycle so as always
please do give us a rate a share and a
subscribe it does help this channel get
to more people and let's get stuck right
into the
analysis okay so here we are starting in
our week on chain 42 dashboard now we're
going to start just again Coming Back to
Basics what is the realized cap well the
realized cap which you can see here in
Orange is essentially the onchain market
cap what it's describing is the value of
every coin at the price when it last
moved now you can see here we have the
market cap in white and you can see that
the market cap um typically through most
of History trades some distance above
the realized cap the realized cap tends
to be a bit a lot slower but it's much
more representative of the capital
invested in Bitcoin because if you
withdraw your at $10,000 and it then
moves again at 50,000 somebody else had
to come in with that additional $40,000
times you know whatever the Bitcoin
value was so it really represents the
amount of invested wealth so one way to
think about it it is the onchain cost
basis it is the onchain market cap and
is the total wealth stored in Bitcoin
saved at the price when it last
transacted so it does have a bit of a
liquidity element if the coin doesn't
move it's kind of trading around on an
exchange and until until it really gets
withdrawn there's that extra layer of a
decision to say this coin is now self-
custodies it's one extra step or two
extra steps away from just hitting the
big red button that says sell or buy so
in that way it's a much more accurate
and liquidity adjusted measure of
valuation now the realized cap hodle
waves are for me personally one of my
favorite metrics they're really really
powerful you may have seen the hudle
waves before the Huddle waves in their
standard format look at the total Supply
breaken down by age bands now in the
warmer colors down the bottom here these
are very young coins coins that
transacted in the last day week month 3
months that's the story in the
traditional Hollow waves we're looking
at on a BTC denomination so of the total
Supply how many of the coins themselves
are actually in those buckets now
generally speaking some people obviously
think about things in terms of BTC value
but the problem with the original hdle
waves that satoshi's coins for for
example so there's 1.1 million Bitcoin
which are over 10 years old they would
otherwise be in the purple Zone which as
you can see in the realized cap hotle
waves is extremely small basically
non-existent so why is this well
satoshi's coins whilst they may
represent 1.1 million BTC they are
significant in terms of the coin volume
what was the price when they last
transacted it's effectively zero now
most people think about their investment
in terms of the dollar value value this
is how most people make their decisions
in markets and with Bitcoin it makes
sense to at the very least conceptualize
things with that price element in mind
so what the realized cap huddle waves
are they are more or less the USD
invested hudle waves this is showing the
distribution of wealth invested in
Bitcoin so let's just think about this
from a very very high level and we'll
get down into the into the details
during bull markets we obviously see the
media pick up people start to tell that
friends about it what generally happens
is the pool of investors increases the
capital inflow increases but the
characteristics of those investors moves
away from the hodlers the people who
study this thing in the deepest darkest
bare markets and know why they own it
and the wealth transitions as you can
see with these warm colors towards new
brand new speculators this was me back
here in 2018 very very first thing I
ever bought in my life was Bitcoin at
the absolute top of the bull so I was a
very unsophisticated uneducated
unknowing investor thinking I was doing
the exact right thing when it was the
exact wrong thing now what happens
during bare markets you get the exact
opposite the price insensitive hodlers
slowly but surely the speculators leave
the incentive hodlers just slowly
accumulate take those coins off it's a
long slow gradual boring painful process
but these cooler colors those older
coins swell in scale so that's the macro
view but obviously this happens at all
time frames you get these bursts when
you get these um older coins get spent
remember coins can be binary they're
either old or young they can't be both
so for young coins to increase it means
your old coins were spent and vice versa
this is where we can see the capital
rotation occurring now just as a quick
hint we've actually recently rolled out
so you can pull the realiz cap hudle
waves into workbench now and that's
actually what we're about to explore a
series of charts where we actually look
at each of these individual components
so we've been experimenting a lot with
these you can Calculate cost bases
models and capital rotation and all
sorts of things so if you are playing
around with workbench um be sure to pull
this in and have a bit of a
test okay so what I want to explore is
this idea of macro Capital rotation what
we're trying to look at is which cohorts
of investors describe the smart money
those longer term investors and which
ones are more more the hot money the
speculators the hot ball of money that's
uh you know more price sensitive but
typically kind of swells up during
periods of demand one represents Supply
the existing holders tend to provide the
supply because they buy it all in the
bear and they distribute it in the bull
in the bull market the demand is much
better represented by that hot ball of
money so that's the the concept we're
trying to go with here so first things
first we're going to look at all of the
wealth helding coins older than 3 years
why did we choose older than 3 years
well there's a couple of reasons one
Bitcoin has historically not necessarily
forever but has historically had about a
4year cycle 3 years really captures the
the last cycle now what we can also see
is that um this is in percent percent of
the wealth held or in other words um
percent of the realized cap held by
these age bands you can see that we're
getting up to about 4 32% by these two
older age BS this is the um 3 to 5 years
sorry this is 3 to 5 years in green and
5 to 7 in blue so even if we add these
together we're talking about sub 10% of
the total wealth held is by these groups
now you can also see they don't
necessarily exhibit an overly cyclical
behavior when you've held your coins for
more than 3 years you become much less
price sensitive you're more likely to
have this kind of long-term investment
and whether you're buying or selling
based on Price is potentially even less
important than if you're just buying or
selling based on your lifestyle if you
hold your coins for seven years for
example for at least in Bitcoin sake
there's a very good potential that you
know if you're buying back here in
hundreds of dollars sitting up here at
26,000 or 27,000 is kind of it's less
important to these people so these
long-term not only are they small in
total wealth but they also aren't overly
cyclical so what we're going to do is
just to simplify this model we're
actually just going to Discount these
people and we're only looking at the
Active investors we really care about
what happened in the last cycle because
they're the most likely people to
actually respond as the market
develops so what we've got here is 6
months up to 3 years in the orange we've
got our 6 months to one year in the
green we've got 1 to 2 year and in the
blue we've got two to three year and you
can see that the people who bought here
held and became the green here who then
some of those held and became the blue
this is this um maturing this maturation
of supply and note not all of the supply
makes it to the other side right some of
these people actually sell and spend so
there's a much smaller distribution that
actually makes it to the Blue Zone which
is that three to sorry um 2 to threee
bucket now as we mentioned at the start
the swelling of this kind of aggregate
group tends to occur during bare markets
and note that the one to twoe typically
Peaks maximum wealth is held by these
people around the bottom of the bear we
can see it here again in 2018 and we can
see it again as FTX blew up we had the
maximum wealth held by the 1 to 2year
Old cohort so what we're going to just
do is simplify this model and say let's
just take this one to two year it
appears to be roughly around the middle
and by definition It's the middle of
these groups it's a fairly good
representation of when that wealth has
saturated the hodlers the probability of
a bare Market floor has increased and we
therefore start looking at what comes
next so let's take the one to two year
as that smart ball of money right that
hodler kind of cohort they're willing to
buy during the bear weather all of the
downturn and survive to the other
side so then we look at the younger
groups we're looking at all of the
groups under 6 months and we can see the
exact opposite this will obviously Peak
during the bull market and when the when
nobody is talking about Bitcoin this is
when the hodlers get to work actually
establishing a market floor and again
this is not a property that is unique to
bitcoin gold has this cycle Commodities
have this cycle stocks have this cycle
it just happens to be we can see these
investor patterns playing out at
10-minute resolution using onchain data
so when the asset is at its most hated
and nobody is talking about it the media
hype has died down and nobody wants to
tell their friends about how much money
they lost in the bare Market um these
things are much less common this is
usually when the hodlers are seeing
their maximum wealth uh distribution and
the fast hot ball of money is at its
minimum and like likewise in the exact
opposite the hot ball of money is
investing the most when we hit the cycle
Peak this is again people buying at the
exact wrong time when the smart money is
spending and the new money is buying the
top now what we're going to do here I
won't go through the actual uh uh
construction but we're going to take the
coins less than one month cuz that
really represents similar to how the one
to two year was kind of this like nice
middle ground that just tells us the
story coins less than one month is
approximately the same for this younger
cohort and if we plot these two out next
to each other you can see the capital
rotation this is Peak hodlers when the
blue shows up and then the transfer back
to Peak Speculator at Peak Speculator we
have the lowest amount of hodlers when
we have the lowest amount of speculators
we have Peak hodlers this is the Bitcoin
internal Market cycle plotted out using
those less than one month the hot
Speculator money and the hodlers the 1
to 2 years now naturally we can break
this down and look at all different
groups in fact if you really think about
this there's a bit of a curve here that
shows how the average age of coins moves
this is what the Huddle waves are really
telling us there's this average wave
speed as things move through and coins
change from hodler to Speculator and
then from Speculator back to hodler this
is the process of capital rotation and
as you can imagine there's these spikes
here and there that occur so internally
on Market rallies during Bulls there is
also these details in terms of how coins
go between these different age
buckets so what we're going to do now is
actually distill this down into an
indicator now you can see here that we
get basically their local Maxima local
Minima they essentially move inversely
to each other and what we're going to do
is just take the difference between the
two and actually look at when do we have
Peak hodler and in the purple ratio
we've got down the bottom here that's
going to be high positive values and
when we have Peak Speculator large
negative values so you can basically
plot out and map out the overall Capital
rotation through the Bitcoin Network as
it plays out using these tools now some
of you who've been around the onchain
space for a while May recognize this
concept because this is actually what we
look at um when Philip Swift came up
with the r hodle ratio it's essentially
coming off the exact same logic we're
looking at that one to twoyear age
bracket and for memory he uses the one
we old as the uh kind of hot ball of
money um and you could really play
around with all these different Dynamics
and the more we've looked at these
different uh you know combinations of
you know do you do one to two year or
six month the 3E when you look at these
different combinations you can find all
sorts of different insights but here
we've simplified it just down to that
one to two year versus younger than one
month so that's the first approach and
again that's all based on the realized
cap there we're looking at the
proportion by age bands now what we're
going to do is go through a very very
similar exercise except I mentioned at
the start about cost bases models and
where your cost basis is is typically
what drives investor Behavior because
why well profit and loss is what drives
markets people generally speaking come
into these assets they buy and they sell
because they see some kind of profit or
loss if you see your coins go to a
profit you're more likely to hold them
but eventually people like to take those
profits likewise there's only so much of
a draw down that people can handle it's
only the price insensitive hodlers that
actually make it to the other side of a
bare market so you'll all obviously be
familiar with our shortterm long-term
and realized cap these are the cost
bases for long-term holders short-term
holders and the market by and large now
in purple this basically highlights when
the spot price is below all three of
them meaning it really doesn't matter
when you came into this Market you're
essentially underwater on your position
now one thing I really want to highlight
here we're going to focus on this purple
Zone that the short-term holder cost
basis which typically trades much higher
than both of them tends to descend below
both towards that late stage bear what
this is actually telling you is that
these long-term holders who weathered
all the volatility they made it all the
way to the other side of the bear they
reached their long-term holder status
and they still underperform the guy who
bought yesterday that is a really really
brutal reality of the Bitcoin Market
this is what these these 75% draw down
people buy all the way up and all the
way down and their cost basis gets
higher and higher until those people who
actually had the patience to wait until
the final capitulation level which again
onchain data helps us identify we can
start to see that this is where these
flaws get put in now remember the
short-term holders who are actually
buying down here we covered this back in
January I believe these are actually
long-term holders by definition of who
they are as a person to have the higher
conviction to buyer when FTX had blown
up and Bitcoin was dead for 10 years yes
they're a short-term holder because
their coins recently transacted but
think about the level of conviction you
need to have to be this person so down
here at these cycle lows even though
they are a short-term holder by
technical definition because their coins
recently moved we can layer on our
analyst perspective and go well what
kind of properties would this investor
have to have a fairly robust case for
why you want to own Bitcoin is probably
one of them so again we can look at
these from a technical perspective but
you can always overly that that you know
analytical perspective just to add that
extra color so really at the bottom of a
bare Market is really that only time
when the short-term holders are actually
some of the highest conviction in the
market and we are now starting to move
to this realm where that is less true
we've now got speculators who've seen
the market rally in pretty much 100%
since the lows and has been tussling
around this $28,000 level ever since now
the last thing I just want to touch on
kind of an adjacent point we are in the
process as we speak of retesting the
short-term holder cost bases from the
undersides at about 28,000 so that is a
key psychological level to pay attention
to if we get above and hold that $28,000
level those short-term holders who've
been underwater for a couple of weeks
since uh what was it in uh late early
September or late August they are now
back into profit on average and that
could potentially be a strong uh
indicator for Market sentiment a
rejection from there obviously would
tell us the
inverse now we're going to take those
cost basis models and we can either
develop something like mvrv which just
takes the ratio with price or we can do
nle which is net unrealized profit and
loss it's essentially mvrv but
transformed in a slightly different
manner we're looking at What proportion
of the Holdings of those different
cohorts are in profit or loss now what
you can see is that long-term holders
are in the max maximum profit at bull
market tops they're also as we said
before they move into the largest
unrealized loss because they buy and
hold at high prices and carry that the
whole way through the be so the blue
actually tends to hyperextend on both
extremes certainly relative to the
short-term holders you can see at these
bare Market flaws when the short-term
holders get in they actually have a very
favorable cost basis because by
definition they bought the bottom
whereas long-term holders typically sell
the top but also hold too long on the
downside so you can see we've got a very
similar pattern there kind of extremes
when the longterm and the short term
start to deviate at large magnitudes
from each other towards Market cycle
extremes well we're going to take the
exact same model and take a difference
between those two nupal curves and you
can see that we get maximum levels
during the bottom of bear Cycles this is
when long-term holders have actually
weathered the whole bear and they still
underperform the guy who just bought and
conversely when long-term holders have
the maximum profits this is when the
market is super overheated there's a lot
of people carrying lots of profit and
what typically happens when people have
lots of profit someone starts to spend
and that spending typically ramps up
until the point that it overwhelms the
supply so the new demand coming in this
is a really important point the
long-term holders are the ones that
actually stop the bull market from
progressing because they sell so many
coins that they overwhelm demand so
whilst the market is the most exciting
the media is the most hyped up at that
point in time that is actually when the
maximum profits are being taken
long-term holders are exiting the market
they're going to oversaturate the the
demand at some point and you have let's
just go back and close this thing out
with our realiz cap hotle waves you have
the maximum saturation by brand new
investors who've only heard about
Bitcoin yesterday today and they've just
bought their first coin and they are
going to be the most price sensitive
they also have a high cost basis they
become very sensitive and that is
essentially what terminates the bull at
the end of the day so thanks for tuning
in for that session folks hopefully you
found that useful a little bit of an
exploration about how coins move around
between different investors and really
just bring it back to just how powerful
the realized cap really is it is a
foundational tool that we build a great
many of these metrics and tools off the
back of um and really it comes down to
the very simple concept of capital
inflows and outflows and profit and loss
which are the motivating factors that
cause investors to make decisions so
until the next one I'll see you then
cheers

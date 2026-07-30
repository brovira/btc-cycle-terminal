# New Metric: Bitcoin Accumulation Trend Score for tracking Whale Buyers (On-chain 101)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=2Ix0yYpaaLk
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-new-metric-bitcoin-accumulation-trend-score-for-tracking-whale-buyers-.md]`.

---

hello everyone and welcome to your glass
node on chain 101 where today we're
looking at a brand new metric that's
just come out today called the
accumulation Trend score now this is a
metric that boils down a number of
Concepts including the size of entities
that are accumulating coins as well as
whether there's a large portion of the
market that are currently adding to
their balance so let's get
started so what the accumulation Trend
score tries to address is the nuance and
the complexity of trying to track when
accumulation is happening and what it
does is it boils it down to two
different concepts the first one is what
we call the participation score which is
thinking about how big an entity is are
they a whale right now are they a very
very small shrimp and overall how large
is the entity relative to all of the
wallets that are out there now the
second thing we include is what we call
Wallet balance change which is looking
at each of those entities if you're a
whale with 10,000 coins and you add one
coin it's not a very very large
accumulation amount however if you're a
whale with 10,000 coins and you're
rating 5,000 coins that's a large
balance change so it combines not only
the size of the entity but also how many
coins they're adding relative to their
current Holdings and it tries to Ste
this down into a fairly simplistic
colorful chart and the idea here is
we're trying to look at where we're
getting zones of accumulation zones of
distribution and really boil down all of
the complexity into a relatively simply
digestible metric so what we're going to
look at is a analysis of the bull and
bare Market structure how this metric's
performed we're going to spend a bit of
time up front to actually look at how it
was constructed using glass note Academy
and this particular session is for
advanced members and you'll find that
this metric is available for our tier 2
members so it's really trying to provide
that additional tool to just understand
what's going on in the
picture now before we get started please
do give this channel a like and a
subscribe it really does help us along
and do leave us a comment and let me
know what you think about this metric if
you've started looking at it um and if
you do have any questions about it as
you get started so as I mentioned we're
going to start here in glass note
Academy and we're looking at the
accumulation Trend score so as I
mentioned it's indicator which tries to
reflect the relative size of entities
that's how much they currently own in
terms of coin Supply and it also tries
to assess whether they're accumulating
or Distributing their coins so as an
indicator overview when we look at this
thing what it's trying to capture is for
a score that's closer to one which if we
see down here is more of these purple
darker colors that's showing when that
over the last month over the last 30
days these larger participants so
remember this is talking about whales
and larger accumulators or remember one
whale could also be met by the same
Force as lots of lots of small of
holders so when we see a large part of
the network or a number of large
participants in aggregate when we look
across the entire network are most of
the coin holders currently accumulating
that will return a value closer to one
now the other side of that these yellow
colors these warmer oranges this is
showing a score closer to zero which is
the opposite of that which is showing
that over the last month larger
participants are not accumulating as
many coins it doesn't necessarily mean
distribution what it does mean is that
their balances are not changing we're
not seeing accumulation so this
particular metric is looking at the
accumulation side of the equation it is
the inverse of if we were looking at a
distribution case but generally it will
return a score closer to zero when they
are not accumulating or when they're
Distributing so when they're balance
change is negative or when there's
simply not much going
on so to try and understand a bit more
about how this thing is actually
measured we're going to break it down to
the two key components so for each day
we look at each entity's participation
score now this is looking at let's say
we have an entity that owns 10 coins and
if we have a coin supply of 100 coins
that would mean that they currently have
a participation score of 10% in other
words if we look at all of the coins in
the supply and there's one entity with
10% of them then their participation
score is that amount it's 10% now bear
in mind that we are excluding exchanges
and miners here so we're only looking at
individual entity wallets we're actually
removing all of those exchangers and
miners who are more or less going to
skew the data if we look at those
otherwise now for each of those entities
now that we understand how big they are
relative to the current coin Supply we
then have to look at how much of their
balance are they accumulating so if we
think about it that's really limited we
have up to 100% have they have they
doubled their total allocation or in the
other hand are they selling 100% of
their allocation so we look at their
current balance and are they adding to
it up to a limit of 100% or are they
Distributing the entire amount which
again is bounded at a total of negative
100% And then what we do is we combine
those two concepts across the entire
network for every entity that's in the
system we look at their total balance
change we look at how large they are and
then we do a number of computations that
normalize the data and turn it into
something that is a distilled Market
wide metric so now we've jumped across
into glass node studio and we are
looking at the accumulation Trend score
metric now you can see here that we've
got these darker colors which is showing
that large scale accumulation values
closer to one and we've got these yellow
zones which is more of a Distributive or
lack of accumulation that's going on now
the way they want to explore this we're
going to start with the first half of
bitcoin's Life all the way up to 2016
because we have to remember that
bitcoin's gone through a number of
different life cycles and the different
participants had different Behavior
patterns at different times now I
typically use that 2016 period to kind
of to break apart the prehistory of
Bitcoin or the early phases and the
later stages where we have more of the
more Market participants more awareness
uh more derivative markets it's a
slightly different Market structure
following that 201617 bull run and
certainly from that point onwards so
I'll normally split it at around the
2016 level now what we can see is that
during the very early phase of bitcoin's
life we can see that there were many
folks who were buying all the way into
the top this is showing that there was
this kind of excitement bitcoin's got
this first price and remember we're
going from 10 cents up to $100 at this
point in time which if you can imagine
being there would have been a pretty
exciting time and this is before trading
view had any kind of implementation
there was no price charts people were
really trading on some you know fairly
interesting and dynamic exchanges at
this point in time it wasn't the same
infrastructure that we're all used to
today now following that you can see
that during these bearish periods it
really quietened off we move into this
yellow and orange phase but note how it
really starts to heat up when investors
see value and it's typically down near
the bottom and we see a large amount of
accumulation go on and then we move back
into the next Trend and we can see this
played out throughout 2013 we had
another rally of large accumulation into
the top this is when mount g exploded
back in 2013 and then went in solvent
and we can see that we started to move
back into that lack of accumulation or
dist distribution phase now what's quite
interesting you can see these folks here
back here in uh in early 2014 where they
actually bought the dip and
interestingly you may have seen this
before over the last 12 months it didn't
turn out to be the dip it was simply a
dip and you can see that we then went
back into a distribution phase which
then eventually came down and created
the macro Bottom now this macro bottom
in 2015 was about a year long and you
can see it went through periods of
accumulation inter distribution
accumulation this is really the Crux of
a bare Market this is where participants
are seeing it rally they think it's the
bull and then they get flushed out again
and there the yearlong of pain of trying
to work out is a bottom in or is it not
lots of people come in and they just get
bored and then we get other people who
are stepping and going I see value so
it's this kind of tussling between the
Bulls and the bears that develops this
long-term sideways consolidation range
which in many ways is a little bit
similar to what we're seeing in the
current market
structure so let's jump across to our
more modern history and again this is
picking up the back end of the 2017 run
and we can see through all of 2017 that
we have these large accumulation phases
into a correction now there is a way to
interpret this we can look and see that
this accumulation typically does carry
on for a period of time until it hits
the tops but then also signals that
people are in fact buying the top so
it's almost got a bit of a lifespan
there's only so long that these Trends
can carry on before things get too hot
and they have to blow off so we can see
that this actually moved particularly in
the 2018 Market we can see a very
distinct change between consistent
buying power all the way through the
bull note how it absolutely dried up in
2018 we went into a full zone of yellow
and orange and really it didn't recover
until we had our capitulation event in
November in December so we can see a
very very cool Market this is distinctly
a be lasted for a long period of time we
didn't get these intermittent bursts of
demand and then putting in a bottom and
then away we went again in a bull this
was very much a cool period very very
few people found demand for Bitcoin
during that
time now note that the November and
December we can actually see why this
bottom got put in there was a huge
amount of accumulation even though this
was a large scale selloff and we look at
a number of metrics whether it's
lifespan or transaction volume there was
a huge amount of capitulation going on
during this period of time and we can
see that we had we return to this bull
market this consistent demand through
2019 we had this miniature this
miniature bare phase but what I do want
to highlight see the difference in color
between 2019 and 2018 2019 is very much
an intermix some people are buying some
people are selling but it's certainly
got a lot more accumulation going on
even into the March 2020 event which
again was very similar to this November
December period so 2019 even though it
was a miniature bear there was a lot
more accumulation going on even though
it went on and off and hot and cold at
different times there was far more
observable accumulation than anything we
saw in 2018 so it showed that maybe the
tides were starting to turn now
following the March 2020 event there's a
very significant amount of accumulation
you can see that we really there was
strength all the way up similar to 2019
there was still uncertainty it wasn't
quite full purple full Trend score of
one but it was certainly nothing like
2018 which was basically a full Trend
score of zero and we can see the early
bull market buying there was a huge
amount of demand all the way into the
January Peak but note also that our
topping pattern here was very very soft
we can see the top pattern and actually
most of 2021 was actually quite soft in
terms of net accumulation it looks much
the same as what we saw back here in
2018 so interestingly even though we set
the bull market highs up here in April
and then we return to them again in
October and November note how that
period looks very similar to 2018 when
we look at this you could almost argue
that this bare Market maybe even started
as far back as February and this is in
terms of overall accumulation behavior
and remember if you've watched some of
our videos in the past you'll see that
onchain activity absolutely collapsed
following that may period and actually
really peaked here in January so we can
see that not only is onchan activity but
also now the accumulation volumes were
peaked in January and really slowed down
from there so now let's actually return
to our current market structure what I
want to highlight note how we've
actually been in accumulation for some
time and we're kind of in this 2019 in
between phase where it's certainly not
the coolness of 2018 where we are at the
moment is kind of a balance almost
there's a bit of accumulation there's
also a little bit of distribution feels
like that 2015 style bottom it feels a
little bit like 2019 and really we're
trading sideways so it shows that
there's this kind of balance at the
moment this equilibrium of bulls and
bears and we've seen this accumulation
that happened following the October high
now remember all of the folks who got
flushed out during this may period back
in 2021 it really has been a hodler
market ever since so many of this much
of this accumulation that we're looking
at and we've covered this in our week on
chain videos are more than likely the
hodler class they're people who are much
less price sensitive there's always
going to be people in the mix who are
going to be price sensitive but hodlers
are typically less so so it makes sense
that we're seeing a stronger
accumulation Behavior it's still not
full bull mode where we see these
massive spikes of overall accumulation
into a selloff and then we rally higher
again we're not there yet but what we
are seeing is more of a 2019 style
pattern more of a 2015 style pattern and
quite often the real deciding factor in
all of this is time it takes time for
the market to digest these moves it
takes time for it to to work out what's
going on and then also overlaying all of
the macro and geopolitical that's going
on at the moment but certainly this
metric is there to try and just unpick
and understand what the market is doing
what the accumulation style looks like
and who is participating in it so thanks
for tuning in for this session do be
sure to check out the accumulation Trend
score in glass node Studio you will find
the link to this in the description
below and just to really summarize this
this metric is trying to distill the
complex and nuanced analysis of
accumulation and it tries to capture
whether they're whales or whether it's a
large portion of the market looking at
that participation score and combining
it with the overall Wallet balance
change and what it's trying to do is
distill all of these entities across the
entire Market to try and identify where
we actually have these characteristics
of accumulation which will give a score
of one it'll be those Purple colors or
when we're seeing not necessarily
distribution but a Slowdown of
accumulation it can be either
distribution or it can be a slow down of
accumulation we Trend closer towards
that value of zero so thanks for tuning
in please do give us a like let us know
what you what you enjoyed in the
comments below and I will see you in the
next video cheers

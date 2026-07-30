# The Week On-chain: The Ethereum Merge - Is ETH Supply Deflationary? (Ethereum Onchain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=2-d2_1NQH2M
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-the-week-on-chain-the-ethereum-merge-is-eth-supply-deflationary-ethere.md]`.

---

foreign
video update for week 38 2022
so this week we are going to be covering
the ethereum merge we're going to be
looking at what really is a feat of
Engineering in the blockchain space a
truly remarkable development and
something that should be really
congratulated and celebrated considering
the scale of it and how many years this
has been underway
so what we're going to explore today is
some of these new proof of stake metrics
we can understand how they actually
operate how it describes consensus what
the validated distribution looks like
and we're going to look at the reality
of the supply Dynamics there's been a
lot of talk about ethereum going
deflationary and we're going to actually
look at the data and say what has
happened since the merge
so as I mentioned this was a successful
deployment of a long-standing
engineering project this has essentially
been a transition that's been underway
for ethereum for many many years and
that is the switch from proof of work to
proof of stake so what we now have are
two ex very large projects Bitcoin being
proof of work and really one of the last
ones standing at any kind of meaningful
scale and ethereum which has now
switched over to proof of stake which
really provides us an alternative option
in terms of these different on-chain
metrics and just exploring and
understanding how these two different
systems work
so we're going to explore these new
on-chain metrics related to proof of
State because there are a lot of
differences it does operate in a very
different Manner and it does have very
different properties to proof of work
we're going to look at the movement of
validate Us in and out of the consensus
pool as well as some of the the Nuance
relating to what that means in terms of
issuance because issuance actually goes
up when you have more validators coming
in and vice versa
we're going to look at the current East
stake Supply and the distribution of
stakers looking at how much of it is
actually held on certain staking
providers versus solo staking
and then we're going to look at the
realities of the deflationary supply
Dynamics there's a lot of talk about EIP
1559 and the effect that the burn will
have whereas what we've seen over recent
weeks has not quite aligned with that
deflational reality that many were
expecting so we'll look at some of those
realities and I'll present a series of
models that we've launched in workbench
that can actually help you track the
real factual performance of this network
and the supply Dynamics
so as always please do give us a write
and share and a subscribe hopefully you
enjoy this particular content but we are
going to be doing a deep dive on the
merge and understanding a bit more about
ethereum proof of stake so the first
chart that I wanted to start off with is
actually an interesting one really just
to show how dramatic and different the
reality is between proof of work and
proof of stake now remember there are
two diff these two different mechanisms
are entirely different systems what they
are doing is keeping the consensus of
the blockchain but what you can see here
is that the this is the mean and the
median block time so with a proof of
work system it's far more probabilistic
we essentially have miners who are
attempting to solve a puzzle the target
block time which for Bitcoin is 10
minutes and for ethereum was 13 seconds
that's essentially demonstrating where
the average time should be and the
difficulty adjustment winds up and down
the puzzle according to the actual
observed block time
so on the left hand side we can see this
natural variability this is the time the
randomized time in some sense around
that Target interval of miners actually
finding blocks so you can see that we
get up here around 16 seconds it gets
down here as low as eight seconds you
can see it's quite variable this is the
probabilistic nature of proof of work
now once we transitioned you can see
where the merge happened this merge
essentially that's immediate swap over
difficulty instantaneously went to zero
there was no difficulty wind down
essentially all proof of work blocks
stopped and we transitioned onto proof
of stake
now the difference with proof of stake
is it uses a system called slots and
epochs and we'll talk about this in a
bit more detail but essentially the
slots are pre-programmed they will come
every 12 seconds so it's more of a
defined interval there's not really that
random probability there's not the the
competitive nature so to speak the
protocol selects a validator and says
here is a slot would you like to fill it
with a block now for the most part they
generally do and we'll explore those
parameters later on
but you can see the difference between
what is closer to a commodity style
mining operation that we see in proof of
work versus essentially a system where
the slots are pre-allocated and
invalidated is selected to propose a
block within that system so two very
very different models two very very
different consensus mechanisms and you
can see the transition clear as day in
this chart
now we're going to start we're going to
run through two dashboards today and
these are both now within our ethereum
preset so you'll see proof of State
consensus where we'll start this is
looking at all of the raw consensus
parameters and the behavior types and
then we'll go to the post merge Supply
Dynamics so actually understand what is
going on with the burn the deflation the
inflation and what is the reality of
that situation
so starting with proof of State
consensus you'll see in this text block
here I won't go through all of these
points but it essentially outlines what
a slot is what an Epoch is and the
intervals that these come in
so generally speaking slots are
essentially pre-allocated there's a
series of slots that are going to come
in and each time a slot comes in there's
about 128 validators who are selected in
a committee to actually essentially
manage that particular Epoch so an Epoch
is 32 slots and 128 validators are
selected to look after that epoch so for
each slot one of those nowadays is opted
to actually build the block so the slot
think about that as an opportunity to
build a block sometimes they miss it if
a validator is offline or unreachable
for any reason you'll have a missed
block so this missed block here is
essentially a slot that was offered but
the validator didn't respond so we have
the slot height we have the number of
missed blocks occasionally we get
moments in time you can see that after
an upgrade that happened somewhere in
late 2021 we've essentially had very
very few orphaned blocks and orphan
block is essentially two blocks that
will produce at the same time by two
different validators but only one of
them could be selected as the chain tip
so it's essentially a block that was
produced but was rejected by the network
kind of a history that could have been
that didn't happen
so then we have the epoch height which
is then how many times we had those 32
groupings of slots and for each of those
epochs we'll have a new Committee of
validators you can see there's quite a
lot more going on in the proof of stake
system we'll touch through this as we go
but there is a lot more Dynamic a lot
more moving pieces than proof of work
which is generally speaking a relatively
simple consensus mechanism with a
problem that needs to be solved by
miners in order to find that next block
so it's a little bit more complicated
and nuanced in terms of how it works
there's a lot more pre-programmed
systems like Committee of validators and
pre-selected algorithmic choices and
Slot Heights so it is slightly different
there are more moving pieces but we'll
step through it one by one
so when we move on to look at things
like Network stability as we saw above
these missed blocks these are
essentially slots that did not get
filled with a block for whatever reason
the validator was offline or simply
didn't respond
so if we look at how many blocks were
actually filled versus how many slots
were offered we get the participation
rate and you can see that we typically
oscillate between 98 to 99 for the most
part we've been in the 99 realm so this
is basically saying that more than 99 of
all blocks were filled they're all slots
were filled with the block and we had
very very few missed blocks
so a lower value on participation rate
essentially means that we may be getting
some set of validators maybe a large
staking provider is having issues with
their node perhaps a client was having a
bug there's been a few of these
instances where we saw these drop-offs
although we really have stayed above 97
for pretty much the entirety of the
beacon Chain's existence so really we
see these in a very um a very short-term
events but if we ever do see
participation rate drops significantly
it may signify a client bug or a large
staking provider is having issues
now I mentioned before that there's 128
uh validators that essentially work on
each Epoch one of them proposes the
block and the other 27 attest to it and
they say yes this follows all the
consensus rules
so if we multiply that out we have an
Epoch is about 6.4 minutes over the
course of a day if all 127 of those
validos are voting yes on that chain tip
we should get somewhere between about
800 and 700 000 attestation votes every
single day and we can see that this is
essentially where the network has
stabilized up in the 700 to 800 000
Realm
alongside this drop in participation Ray
we also saw a brief drop in attestations
so again this gives us a bit of
indication that perhaps there was some
form of bug across one of the clients or
a staking provider that was of a
reasonable enough scale that it had a
noticeable impact but overall we have
seen both of these metrics recover back
into their expected ranges so so far
Network stability seems to be fine but
you can see that we can use these two to
really assess how many validators are
actually online and responsive in the
participation rate and then look at the
attestation count to see how many of
those validators actually saying yes
this is the correct chain tip and I'm
voting to approve this particular block
now when we talk about validators moving
in and out of the proof of State
consensus there is in fact a queue you
can't have too many validators coming in
at once and you also can't have too many
leaving there is an entry and an exit
queue and this is really to keep the
overall Network stable when you have too
many validators trying to come in it's
essentially a door that can only fit so
many in per epoch
so that's what this chart here is
showing you can see here in red this is
our active validators which you can see
has been more or less up and to the
right through most of the beacon chains
history
this blue curve at the top here is
essentially the imposed cap which you
can see it here the churn limit it's the
it's a maximum of four per Epoch but it
does increase the more active validators
on the network so essentially the more
validators that are online the more are
allowed to come through the door
and you can see that there's periods of
time we've got these large bursts of new
validators this chart down here is the
actual number of new validates you can
see that these are line very closely you
get lots of validators trying to enter
the protocol we essentially hit the
queue cap and it has to take some time
to actually process all of those
entrants you see that active validators
climbs at the same time and then you see
there's other periods where there's
marginally fewer we don't quite hit the
cap there's all of this white space it's
essentially showing that we have far
fewer validators trying to come on board
and thus our gradient here the number of
active validators slows down a bit so
this is essentially looking at the Cure
validators trying to come in and this
chart down here is plotting out the
actual number of new validators who are
entering this the network
and we also have those that are exiting
the queue now this is a fairly small
number we're talking about less than 500
have been slashed less than 500 have
voluntarily exited we're talking about a
relatively small number of validators
who have left the space now remember
that when it when a validate actually
leaves whether by voluntarily or by
slashing at the moment they still can't
withdraw they're waiting for the
Shanghai Fork to actually do withdrawals
of the eighth so at the moment the
eighth stays there but you can exit your
validator from the pool so it no longer
participates in consensus there's no
reward but there's also no more
penalties
now as to what these slashing events are
it remains to be seen whether these were
actually devs testing to see where the
slashing mechanism Works whether it was
just some kind of malicious behavior
whether it was some kind of client bug
it would require a bit more further
detail to understand that but we have
only seen today 175 slashing events and
only 677 validators have opted to leave
the network so really it's been more or
less inflows only for the most part
so now we're going to look at a little
bit of a nuanced topic which is called
total staked balance versus effective
stake balance now when every validator
enters the queue they must deposit at
least 32 each now from that point in
time they may earn some revenue from
issuance and fees they also may have an
inactivity leak which will cause their
balance to go down and they also may be
slashed so there's a few ways that their
balance can go up and down from that 32e
that's kind of the starting point and it
will deviate from there so the total
amount staked includes all of those
deposits plus all of the revenue minus
any of the slashing and inactivity
penalties that's the total amount that
has been deposited
however each validator can only have
what's called an effective balance that
is capped at 32 eighth and it goes down
in one eighth increment so if they have
31.5 for example that means they have a
effective balance of 31. there's a few
more details here I'll leave you to read
through the actual specifics
but in general the effective balance
think about this as the actual total eat
stake that's participating in consensus
because each validator can't have more
than 32 that's active any Revenue that's
earned on top of that think about like a
buffer if they had a little bit of an
activity leak their effective balance
would stay at 32 so it's trying to keep
the network nice and stable in terms of
the amount of stake that is actually
there
so if we look at these in combination
the red curve here is our total balance
and you can see that over time as
revenue is earned the green balance
underneath it which is the effective
balance which is that it's actually
participating in consensus starts to
deviate there's this is essentially
capturing the revenue and all of the the
Delta that goes beyond that initial 32
each state so you can see it does start
to climb higher and then this purple
curve is showing the percentage of how
much is effective versus the total and
where we are at the moment is down here
at about 94.6 percent which means about
5.4 percent is sitting there as bonus
Revenue essentially a buffer over and
above the amount that is actually
actively participating
now moving on to our last two charts for
this section we're looking at the total
eth staked by service providers now
we've continued to profile here at
Glasgow quite a number we've added a
number of different staking providers
and where we currently are by looking at
all of the staking providers that we're
currently looking at there's a just over
10 million each and it represents about
69 of the total stake
so what that essentially means is that
the total stake is captured by the 69 of
all steak teeth is hosted on these
providers that we've got tracked here
and we can see Lido down the bottom here
in green is the largest about 30 31
percent of all stake we then have
binance Kraken and coinbase and between
these top three we're talking about
about 59 of the total stake so a very
very large amount and there's a lot of
reasons why people will do this we see
that there's a technical overhead to
running a validator there's convenience
and just delegation of risk there's
those investors who just simply have
less than 32 eth and need some kind of
pooling solution
and there's also the ability to tokenize
stake and we're seeing this in Lido
we're seeing it in rocket pool and we're
also seeing it recently in coinbase
where they release their CBE product
which is essentially a liquid staking
derivative of coinbase staked eth so
there's a lot of reasons why we're
seeing this behavior um it's one of
these things that's been talked about
for a long time but now we're actually
seeing the full numbers that we're
talking about at 69 of the stake is
hosted on those those staking providers
some of them are more decentralized than
others there is a bit of a spread there
but there are logical reasons as to why
customers are choosing to use these
products rather than stake on their own
and the last chart that we're going to
look at is the staked realized price now
what we're looking at here this again
really shows you why a lot of people
move towards Lido and these liquid
staking derivative tokens
this red curve here shows the average
price of all staked deposits
and the average price of all staking is
about 2 2 340 which is obviously quite a
bit lower than where we currently are
trading down here about thirteen hundred
so this yellow curve here is showing the
amount of unrealized loss essentially
how much have investors deposited and by
holding that staked eth based on the
price when they deposited essentially
how much are they underwater an
unrealized loss and at the moment
there's about 12 billion dollars of
unrealized losses in that in the staking
pool
so if you compare that to the broader
Market here in blue that's sitting down
here at about 1600 so there's quite a
big difference between uh 2 300 and 1600
in terms of the realized price and that
cost basis so really the ability to
actually sell and hedge and
collateralize that those State eth
tokens it does make sense why we've seen
this explosion in momentum towards
liquid staking derivatives why Queen
bases launched theirs because it gives
people more options so really the
explosion and growth of these particular
Services shouldn't really come as too
much of a surprise being that it solves
these problems and it also allows
investors to hedge and sell their risk
so just before we get started on the
second dashboard I just want to give you
a quick update on what we've been doing
over at glass in terms of new content
and again this is for our Advanced and
our professional members so we have a
new market Polson Forum this one here we
actually built up and showed you step by
step how we constructed a dashboard that
can identify periods of tops and bottoms
essentially using a concept borrowed
from drilling techniques what we're
looking for is when a huge portion of
the market is entering to that
profitability realm and when we see
correlations break down because either
everybody is in profit or we've seen at
the top or we've seen a transition in
investor sentiment and behavior back
towards that hodler status near bottoms
so really building up a dashboard for a
workbench from first principles using
interestingly concept borrowed from
physics into the drilling world to
construct these metrics so a really
really interesting and fascinating study
and we've also recently released a
series of workbench presets So within
those we've got everything from Market
indicate haters Supply Dynamics proof of
stake pricing models and we're building
out these all the time we're really
rolling out quite a number of these new
workbench presets so do jump in to check
those out
so moving into the second part of this
video and we are now going to focus on
the supply Dynamics as well a lot of
people have been talking about with the
drop-in issuance from proof of proof of
work to proof of stake and then also
looking at the EIP 1559 burn
so we're going to start this analysis by
looking at each Supply and we're looking
at where are the large clusters of this
Supply different categories of Supply
Dynamics so in the yellow key we have
the supply held on exchanges in the red
we have the supply held in smart
contracts and at the top here you can
see that growing meaningfully we have
the supply held on the beacon chain so
you can see that the stake Supply it's
not quite as large as smart contracts or
as large as exchanges but it is
continuing to grow and becoming a
significant proportion of the supply I
think we're over 12 percent of ethereum
suppliers in the beacon chain so it
shows just the magnitude of how much
this is growing and now that the merge
has been de-risked to some extent it is
very very likely we'll start to see this
actually climb and continue to grow
especially with these liquid staking
derivative tokens it's likely we'll see
this Dynamic continue to play out
now stepping into some validated
economics looking at how does the
issuance rate and the return for a
validator differ based on how many
people are participating
so in the ethereum protocol we have two
calculations here so the annual return
on investment per validator so
essentially if it's four percent you're
earning four percent in eth on your 32
East deposit that's what this is mapping
out and you can see here that we've
actually got a formula that is dependent
on the number of validators so your Roi
the return on investment actually
declines the more validators enter the
pool and when you have a very large set
of validates we push above a million or
even 1.2 million validators currently
about 430
000 so imagine a doubling or a tripling
of the validator pool this starts to
stabilize we're at 4.8 at the moment
this will start to stabilize closer to
around three to two and a half percent
once we get to those large validator
sets this will continue to decline so
that return on investment does decrease
and simultaneously the actual issuance
or the estimated annual issuance at the
proof of stake layer is also a function
of validate account except instead of
being in the denominator where it
decreases so the return on investment
goes down the more people are staking
the issuance actually goes up the more
people are stating so we can see that
the overall annualized issuance
continues to climb as more validators
enter the network so back when it was
the Genesis block we saw 155 000 Heath
being minted per year on the proof of
work on the proof of stake chain sorry
and here we are at 671
000 so this will continue to increase as
more validators enter the mix so we can
see that there's this interesting
dynamic between validate account and the
higher that the yield is the more
validators start to come in and that
compresses down the yields and in that
way we have this almost fluid Bond like
mechanic where the more people are the
more demand there is for something the
lower the yield goes down
we can then also calculate the estimated
nominal inflation rate so this is not
looking at the EIP 1559 burn this is
purely what is the issuance rate so
pretend that there was no burn how much
Supply is being minted onto the market
and at the moment we can see that this
is 0.56 percent which is much lower than
the 4.3 percent
thereabouts was for the the proof of
work issuance so here is essentially
that first idea about the the supply
decline we've gone from over four
percent issuance to down to 0.56 percent
but remember this will climb as more
validators enter the pool and until the
Shanghai Fork that can only go up we can
only have more validators come in or it
stagnates because we actually can't have
that withdrawal as you get
so now adding on that next layer we've
got our nominal issuance here in blue
and this is the nominal issuance here in
blue at the top and you can see it's
much smaller relative to the red area
which is the EIP 1559 burn
now what this model here is looking at
is essentially a simulated reality
because remember that over the last
couple of months to until the merge we
had proof of work issuance we had proof
of stake issuance and we had the EIP
1559 burn we actually had two sources of
issuance which need to be accounted for
so we're going to build up this model so
up here we have our proof of stake only
issuance no burn
here we have that same curve and then
the red is the simulated 1559 burn so
let's imagine that the merge went live
at the same time as EIP 1559 back here
in August 2021. if that was the case
this purple curve shows you that we
would have been in deflationary
territory through most of the bull run
but remember this doesn't factor in the
proof of work issuance which was
happening at the same time
now even so you can see here that the
purple curve is now trading above the
Blue Line This is indicating that the
burn is currently less than the proof of
stake issuance even after the merge we
are currently in an inflationary regime
so it's just important to kind of map
out these things and understand the real
dynamics of what is going on so at the
moment even post merge we are still in
an inflationary eth regime but rather
than it being 0.56 percent the burn is
essentially halving that so it's 0.25 so
we've more or less halved it the burn is
taking up about 50 of the proof of stake
issue so still obviously a massive
decline from proof of work it's about a
92 percent the clients are quite
dramatic but we are still on that
inflationary regime
and this is primarily being driven by
the low gas fees by the way we're seeing
gas fees return to actually almost
pre-2020 bull market level so very very
light congestion on the ethereum chain
at the moment which is the primary
reason why the burn is so small
historically
so now we have a combined model this
proof of stake net Supply chains this is
at another one of these workbenches that
we've recently released so you will find
this as a preset and workbench you can
always access these charts from the
dashboard which is in the description
below and you can hit this little
magnifying glass at the top here to
actually view the full scale chart
so let's step through what this model is
looking at
the orange curve here is proof of work
so imagine we only had proof of work
with EIP 1559
and you can see it's much much higher
and anything that's above this middle
line is inflationary anything below it
is deflationary
the blue curve is only proof of stake so
modeling this purple curve so the blue
curve is looking at the only proof of
stake with EIP 1559 you can see the
dramatic difference between these two
now the green curve is the actual
reality this is the fact of what
actually happened for ethereum because
we have proof of work plus proof of
stake issuance minus the burn so this
green curve you can see is actually
higher than the proof of work issuance
and that is because there's an extra
layer of proof of stake issuing on top
of it however it has now collapsed down
to the blue curve so this blue curve is
now the reality everything that's in the
history is kind of a simulation but post
merge this purple curve and this blue
curve which are the same is the real
reality of how much coin is being issued
on net and we can see here that we're
currently issuing about 871 each per day
during the proof of work phase or the
actual reality phase we're issuing
closer to 13
000. so we're talking about 700 versus
13 000 a dramatic decline in Daily
issuance you can kind of see the scale
of that
and just to really close out we're going
to look at the very very zoomed in we're
looking at the one hour chart here this
is the event of the merge we have the
proof of stake issuance here in green we
have the EIP 1559 burn in red you can
see that the green is larger than the
red in scale and that leads us to this
blue curve where you can see this
initial deflationary period there's
about 12 hours of deflation post merge
higher Network congestion lots of people
trying to transact you know be um one of
the first transactors post merge but we
have since migrated back into a
inflationary regime nevertheless the
actual supply distribution is about 92
percent lower than what it was during
proof of work so it gives you a bit of a
sense of scale of just how significant
the merge effect was
so thank you for tuning in for that
hopefully you found that useful please
let me know in the comments whether you
enjoyed this type of content
um it is a very very new system there
are a lot more moving Parts but really
on those dashboards we've tried to
document them and give you enough
information to really digest and
understand these tools and make them
easy to actually deploy so do let me
know if you enjoy using those let me
know if you have any comments or
questions and I will see you in the next
one cheers

# The Week On-chain: Bitcoin Fee Pressure Explodes Higher - Week 19, 2023 (Bitcoin Onchain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=m8s2MefLBgY
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-the-week-on-chain-bitcoin-fee-pressure-explodes-higher-week-19-2023-bi.md]`.

---

foreign
and welcome to your glass node video
report for week 19 2023 so Bitcoin has
seen a enormous influx of demand for
Block space and this is really created
quite a bit of congestion actually and
push fees to uh really quite quite high
levels we've actually seen that the
total fee inside some of these blocks is
more than the 6.25 BTC block reward so
very very significant influx of demand
it is associated with inscriptions and
you know the brc20 token standard and
some of these different concepts which
uh may be a flash in the pan they may be
here to stay but today we're really
going to explore this look at a series
of metrics that help us understand a bit
more about what is going on
so congestion and fee pressure are one
of these things it's always been a bit
of a debate because on one side you have
the Bitcoin security system which
eventually will transition to a fee only
model and likewise it moves towards
being a global Reserve asset we can
expect fees to rise and likely stay
there now the other one is that having
high fees makes it more expensive to
transact and this generally creates more
incentive for people to move towards
things like lightning network and to
build them out in the first place so
these incentives will play out and it is
going to be a multi-year process as the
lightning Network expands as different
layered scaling Solutions evolve but
what we're going to be looking at today
is kind of what's Happening Here and Now
and a lot of this has been driven by
ordinal Theory and inscription so in
case you uh you missed our report on
ordinal Theory you will find it in the
description below
um but ordinal theory is essentially a
protocol that sits on top of Bitcoin
Bitcoin doesn't know anything about
satoshi's all it sees is utxos and
volumes of Bitcoin transacting and
obviously addresses and and blocks and
the like
um ordinal theory is essentially a
protocol that sits on top of that and
provides a serial number for each
Satoshi so these inscriptions are indeed
put onto the chain but actually
assigning an inscription to a particular
Satoshi is actually an external protocol
to bitcoin Bitcoin has no idea that this
link between individual satoshi's and
inscriptions is taking place so it's
kind of an interesting experiment it's
one of these things that is playing out
there's a lot of debate and discussion
um that's that's going on around it but
we're we're really going to zoom in and
look at this from an on-chain activity
lens and we are going to be focusing on
a series of dashboards that we've rolled
out on this topic this is essentially
why you would pull these tools out to
understand the difference between
on-chain activity and in particular
concept that I'm going to call payload
because in this instance we don't have a
lot of volume there's not a lot of BTC
flowing around despite the fact that
transactions are at an all-time high so
we're looking at that that Divergence so
anyway that's what we're going to get
stuck into as always give a rate a share
and a subscribe before we get started
and let's jump right into the analysis
okay so the first dashboard we're going
to start with all of these are presets
and available inside studio
um so the first one we're going to look
at is called the utxo set and you'll
find all of these underneath the
on-chain activity category for Bitcoin
so if the utxo set is a really cool
dashboard it's available for everybody
on all plans including free plans this
is really looking at the the underlying
Bones the utxos are the accounting
system that Bitcoin utilizes they're
kind of the base building block for all
of the metrics that we design in on-chan
Analytics
so the first one we're looking at here
is the number of utxos which are created
in green spent in red and total in blue
now what you can see let's actually just
zoom this one in on let's just go on a
two-year time frame
you can see here that the number
destroyed is actually I mean it's kind
of flat it's within our typical range
but the number of utxos created is
absolutely tearing higher so obviously
the blue being the total is the net of
created and destroyed and what we're
seeing is that the utxo set in terms of
the number of utxos on bitcoin is
exploding higher this is an enormous
uplift
um so we've seen a lot of activity
creating a lot of new utxos now for
anybody who's not familiar with the term
utxo you will find a link in the
description below we have a analogy or a
description of what they are comparing
them to a gold coin which is a really
really nice analogy a really nice way to
just kind of wrap your head around what
exactly this you know strange
abbreviation actually is
so what we're looking at is here is the
30-day growth in the number of utxos and
this you can see is the second largest
Spike we've ever had there was an
appreciable one back here at the 2017
top you'll see a bit of a theme across
many metrics we look at today and back
here in 2015 there was a huge cluster
but really short of this this is the
second largest growth in the utxo set
we've ever seen so it is a significant
demand inflow
now I mentioned before that we're
talking about the concept of when we're
talking about on-chain activity we're
looking at how alive the Bitcoin network
is how much transactions are taking
place how many blocks and how full are
they these things like this
now I'll talk about the concept of
payload if you've got an active address
but it's only sending 15 cents worth of
BTC it's kind of less meaningful in many
ways than a address that's moving a
thousand Bitcoin so the volume is what
I'm referring to as the payload how much
weight does that utxo have because a
single utxo can hold a billion dollars
worth of bitcoin or 10 cents worth of
bitcoin it could actually hold both
right so we're looking at how much
volume is there
so what we're looking at here is just
the role settled transaction volume in
BTC terms and you can see we've barely
got any uplift so whilst we have the
number of utxos and as you'll soon see
the number of transactions ripping
higher the amount of volume remains
historically low so there's not a lot
inside these utxos
as a percent of the circulating Supply
we can also see a very very small amount
of volume there's just not that many
coins actually moving around the chain
so moving on to the second dashboard and
this is probably the more important one
to pay attention to for the moment this
has got a lot of great tools
um this is called the on-chan activity
dashboard because that is essentially
the problem it's trying to solve we are
looking at this from two lenses activity
with no payload active addresses
transaction counts things like that and
we're looking at it from the payload
perspective which is how much weight
does it carry or the transaction volume
side of the equation
now what is quite interesting you can
see here this is our active addresses
I'm just going to put this onto a
five-year basis
um you can see the active addresses is
actually falling off so despite the fact
that there's lots of utxos we're
actually seeing that the number of
addresses that are active at the moment
is collapsing lower kind of a strange
phenomena
if we look at it on the new address
momentum remember this is where we
compare the monthly moving average in
pink versus the yearly Baseline in blue
you can see that we're coming back down
towards the yearly Baseline we're not in
negative momentum territory but we are
pulling back quite substantially in many
instances this will be something you say
uh it's probably not actually the best
thing to see it's not quite as positive
as a nice healthy uptrend in both we are
seeing a reduction in the amount of
addresses
now similar to our utxo chart the number
of addresses with a non-zero balance is
pushing higher so what we're seeing is
that there is activity happening and
it's creating lots of utxos it's
creating lots of new addresses but it's
in terms of the amount of activity and
how many addresses are actually
participating this is actually being
driven by the fact that Within These
brc20 token standards and we'll talk
about a bit more about this as we get to
get through this session but essentially
people are using the same address and
they're not using many addresses now
this is quite an interesting filament
something in the order about 60 to 70
percent of these transactions are
actually using the same address now
typically speaking wallet software
doesn't do this we normally see that
wallet software would generate a new
address for every Bitcoin transaction
it's very different to to account based
chains like ethereum or Solana where
they use a single address and that is
kind of your account in Bitcoin
addresses are essentially disposable and
really people rarely use and you
actually shouldn't reuse addresses for
both security and privacy reasons so
this is kind of an interesting phenomena
and it may actually speak to the fact
that there's you know the people who are
transacting or a large portion of people
who are transacting these brc20s may
actually be coming in with an ethereum
or a Salata mindset and reusing the same
address which really isn't the right way
to do things certainly from a security
and a stability standpoint privacy
standpoint
so what we can then see is and this is
really important when we look at metrics
here we're looking at our relative
activity as small and large entities so
this tool was designed to track large
entities which is looking at the red
small entities in the Blue by comparing
the mean and the median of the amount of
volume that's moving around so the mean
is typically weighted more towards
whales so we typically see this red
Curve will show when whales are more
active and when we're looking at more
retail dominated markets the blue will
be more dominant being in the median
which is typically a smaller value
there's a lot more shrimp relative to
whales
note that both are collapsing off a
cliff and this is because these
transactions that are on the Move have
such a tiny payload typically we see
with inscriptions they're like 10 000
sets so whilst there's lots of them
they're moving around very very little
BTC volume so it's just one of these
things we're trying to really frame up
the problem
so now we move on to the transaction
space and transaction counts are at a
tearing all-time high over 440
000 transactions a day I mean it leaves
the 2017 peak in the dust so this is by
far and away the largest transaction
we've ever seen in terms of number mine
we're actually seeing blocks that have
over 4 000 transactions each so just an
unbelievable uptick in transactions and
really what this shows us is that blocks
are being filled with lots of very small
transactions in terms of their data
footprint basically packing as many
high-paying fees into a very into that
constrained block space as possible and
they're all paying extraordinary fees
which means it's crowding out any of the
larger size transactions and it's really
all these small blc20 inscriptions
now if we look at on a momentum
standpoint right that this is a nice way
to just kind of ground it because you
can look at transaction counts so it's
up is that good I don't know if that's
good we can use momentum tools right
which is again just looking at the
monthly versus the yearly average to
compare these things and you can see
that I mean in terms of momentum it's
just extraordinary how much this thing
is pushing higher so there is a stack of
activity but it's not moving around on a
BTC it's created creating a lot of utxos
but it's not using a lot of addresses
it's kind of a funky problem and to be
honest we haven't actually seen this
before this is quite a unique setup for
Bitcoin but it's one of these things
that just requires us to understand the
mechanics so we can really interpret
these things properly
so now moving into the volume space
right we touched on this earlier with
the utxo dashboard but here we are
volume is just not picking up at all
right really confirming what we've seen
um we've got two metrics here this is
looking at our transfer volume momentum
this is looking at change adjusted now
it's important to note that this heavily
inflated volume is largely driven by
sadly the uh misbehavior by the FTX
Alameda entity so really this metric is
still recovering our yearly is very high
because of all those inflated volumes
you can see here that the volume
collapsed the day that that particular
Edge see well stop transacting because
they blew up so we are still in the
process of repairing this chart on an
entity adjusted basis you can see we had
volume pick up but it hasn't quite
broken above the yearly average so we're
just not there yet in terms of the
amount of transaction volume
and we can see a very similar Thing by
looking at exchange related volume this
is only inflows and outflows to
exchanges typically this is where people
are changing hands right people are
buying and selling exchanges are kind of
the centerpiece of that we had a bit of
an uptick we got above the yearly but we
haven't really stuck The Landing yet and
you've seen this in a couple of
different instances so this is just
something to be aware of right we have
activity we've got adoption but it's not
carrying much volume so you can kind of
weight that as uh you know it may not be
as positive as if all of these things
were firing at the same time
so now moving into I mean the one party
who is having an absolutely fantastic
week are the miners
so the total transaction fees I mean
this thing here is screaming higher
625 BTC in fees per day happening at the
moment just an unbelievable amount
remember six I'm 900 is what's coming
out the block reward so and this is
obviously at average over the course of
the day but 620 or 630 BTC per day is
just incredible in terms of the amount
that's actually being paid out and
really you can see that this has
happened overnight a true explosion has
happened overnight the mean and the
median fee has ripped higher so we've
seen an explosion in the actual amount
of fees being paid per transaction
and if we look at it from a zed School
perspective so for those who aren't
familiar a zed score is basically a tool
that we can normalize things so
obviously the behavior in Bitcoin back
in 2013 was somewhat different to today
how do we normalize that across Cycles
well a z-score is a nice way to do that
what it's doing is saying how far have
we deviated away from the mean
so the question is well which mean which
average do we care about because you
could do a four-year average a two-year
average an all-time average and the
answer is all of those are applicable
um and actually up here this is our fee
Revenue Z score ribbon which is looking
at the one the two the three and the
four year
um that's a bit complex for today um
I'll leave the uh the viewers to come
back and have a look at that we're going
to focus on these two and the reason why
I focus on these two is they're really
going to help us understand why we would
care about this particular metric
so the first one is that this is the
two-year mining Revenue Z score so what
we're looking at is how much are miners
making from fees it's a nice that is
already kind of averaged out because
you've got the block subsidy that will
decline with halvings and we're just
comparing the fees to that particular
environment now why do I pick a two-year
well a two-year if we're let's just free
you know again we don't know if we're at
the end of a bear Market let's just for
argument's sake say that we are then the
last two years is probably bear Market
Behavior so what do I want to look for
show me when bear Market Behavior
doesn't really look like bear Market
Behavior anymore so you'll get these
very violent moves right as we kind of
come out of that regime the two-year
will fire off now you may get some false
signals like we did here in 2019. well I
mean it was it was still a powerful
rally but this is comparing to the last
two years which was predominantly bear
market so show me when the fees are
different to the last two years
the four year is obviously going to
account for the classical Bitcoin um
four-year halving cycle show me a bit of
bull show me a better bear market and
now show me when we're statistically
above that average right so the average
is what's being captured here by the two
year and the four year they're both
useful depending on what you're trying
to solve in this instance we can see the
two-year is just screaming higher and
the four year is also ripping higher
back to bull market territory so the
amount of fees being paid is
extraordinary it is Meaningful and it is
very very significant so you know
whether This truly does lead to some
kind of momentum or it's just a flash in
the pan that's what we're waiting to see
nevertheless it is a fairly substantial
and uh and worth observing a moment in
time that's playing at the moment
now just to put a little bit of this
into perspective
um this particular chart is just a very
simple model we're looking at the
average fee paid per block so every
block that gets mined how many fees are
in there what's the BTC payment worth of
fees
now I've also used workbench here using
a clever rounding function what I've
essentially put in here this here is the
formula that Satoshi encoded into
Bitcoin to define the block subsidy so
you can see in the early days it's 50
BTC per block then it drops down the
first halving to 25 then it drops down
to 12 and a half and now we're at 6.25
and in just over or actually just under
a year now it will be 3.125 so this is
actually the Satoshi block reward
formula and in the orange we can see the
average fees paid per block in aggregate
right how much was the fee reward per
block so obviously when the orange is
spiking above the Blue Line showing that
the miners got paid more in fees than
they did From the Block subsidy and you
can also see that there's one two three
2017 four and here we are right now this
is only the fifth time in history where
we have seen a period of time where fees
inside the block were above that block
subsidy now whilst that's very
impressive here's the thing to just kept
bear in mind the first thing is it's
remarkable that this has happened right
this is significant and if this turns
into a trend that really sticks the
landing and we actually see that this is
kind of a new normal then many of the
concerns about the security budget will
essentially disappear right it'd be very
hard to argue it when the fees are
already outpacing the block subsidy
the second take here is that it's only
happened one two three four five and in
the last four note that this didn't
stick around this didn't stick around
nor did this noted this so historically
we have not seen this High fee pressure
stick around for very long now that
doesn't mean that we're not going to be
in a higher fee regime than if these
things weren't taking place but it also
stands that typically speaking we see
this kind of influx of demand and then
things cool down so given that we're
kind of in such an extraordinary period
of time the higher probability that this
will cool down and then over the course
of the coming months six months maybe
years we will see whether this
particular Trend really does have
staying power
so the last thing I want to close out on
is our ordinals and inscriptions
dashboard now this one here is
essentially trying to understand okay
we've established that there's lots of
uh activity going on it's not using very
many addresses and it's not moving a lot
of BTC around but it's creating stacks
of utxos and lots of transactions and
paying huge fees to do so
so if we look at the inscriptions the
number of new ones which are coming in
Orange uh jpegs and these this
previously dominated right this whole
screen was orange when we looked at this
when it first came out or in the
descriptions first launched look at all
these text files these BRC 20 tokens are
essentially text-based inscriptions and
what we're seeing is this is just
dominating by Far and Away you can't
even see jpegs taking place anymore
because at these fee levels it's just
non-economical for people to uh to
inscribe images they're just too big on
the data footprint and whilst text files
are much much smaller in terms of their
data footprint they can therefore pay a
much much higher fee rate
um you can see there were over 400 or
sorry no 4.5 million total inscriptions
and you can see that the blue is
actually starting to crowd out the
amount of tax inscriptions is now
crowding out in fact in terms of total
volume tax inscriptions now 3.87 million
out of that total 4.5 so tax has now
surpassed jpegs in terms of the primary
inscription type
um so truly quite extraordinary all of
these inscriptions have added 9.4
gigabytes to the vectone blockchain
since uh since this whole protocol
launched
um and if we move down into transaction
counts similar similar chart I mean
transaction counts you can see that
these things are dominating over 50
percent of all transfers happening right
now in the Bitcoin ledger so I'm just
extraordinary growth again it remains to
be seen if this is a long-term event
um or if it actually uh you know sticks
a landing and is it a flash of the pan
or something that's going to stick
around
we can see that the average transaction
size it ticked much higher when they
were jpegs the inscriptions were jpegs
which makes sense it has fallen
significantly now that these are text
files so basically because the data
footprint is so small we can fit more of
these into blocks or miners can fit them
more of them into blocks so the average
size of a transaction is actually
falling off a cliff we're down here at
near multi-year lows right so it's kind
of showing that the blocks are extremely
dense full of very small high paying fee
transactions so again it kind of speaks
to a serious hype that's happening at
the moment
um and the last one that I wanted to
jump on to we talked about uh these
moving on to transaction fees so you can
see here this is looking at transaction
fees or the total amount paid all
inscriptions since the protocol Came
live has been 653 BTC and you can see I
mean we were at 200 just a couple of
weeks ago look how much the fees have I
mean 400 something BTC
um or you know whatever that is uh
two-thirds has been paid by these text
inscriptions and with the most of it
actually happening in the last week or
so so truly extraordinary stuff miners
are really I mean they're having a great
time at the moment because they've seen
their revenues not quite double but get
pretty close to it and I mean it remains
to be seen whether this really sticks to
Landing or if there's a bit of a flash
in the pan
so thanks for tuning in for that session
folks hopefully you enjoyed uh actually
and analyzing things from a on-chain
activity standpoint
um I will often use this and I like to
split it into the non-payload addresses
transaction counts utxos and then the
volume and you can also put realized
value in there we often talk about
realized profit and loss that's kind of
are the transactions that are on the
Move carrying a lot of volume weight if
they're not it just helps us color and
understand that this looks a little bit
different to our classic bull market
where you've got high fees lots of
exchange volume lots of people trading
in and out at the moment we have a lot
of those things except we don't have the
volume we don't have the exchange
activity we don't have the coins moving
around it's being driven a lot by these
inscriptions so it's kind of one of
these things we have to start thinking
about this from a little bit more of a
dynamic lens it's not quite as binary as
it as it first seems but hopefully today
gave you a bit of an insight into how we
can analyze this so anyway thanks for
tuning in if you've got any questions
you can reach me in the comments and I
will see you in the next one
cheers

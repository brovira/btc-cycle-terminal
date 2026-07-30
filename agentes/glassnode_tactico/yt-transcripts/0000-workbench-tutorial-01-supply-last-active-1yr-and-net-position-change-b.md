# Workbench Tutorial 01: Supply Last Active 1yr+ and Net Position Change (Bitcoin On-chain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=neKODeE01Jk
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-workbench-tutorial-01-supply-last-active-1yr-and-net-position-change-b.md]`.

---

hello everyone and welcome to your first
workbench tutorial where we're going to
be exploring the supply last active
one-year metric we're going to use this
as a base because it provides us with a
very very big picture macro cyclical
behavior in terms of supply but we can
also really understand what's going on
with the market sentiment by looking at
the change in this metric so there's a
few opportunities to really just
understand the fundamentals of workbench
and build a net position change using
this metric to fully understand what is
going on at a more granular level
so in this particular tutorial we're
going to explore this fundamental
toolkit on how we can actually use
workbench to create new metrics to
identify new insights and really try and
go a little bit deeper than just the
metrics themselves
so for this particular model we're going
to start with the supply last active one
year this is the total percentage of
circulating supply that is older than
one year now as you may be familiar when
we see these older coins it generally
shows that bitcoin has a stronger set of
hands it's generally a fairly
constructive sign when this metric is
high or increasing
and the converse of that meaning the
coin's younger than one year when that's
growing in population that's telling us
the other side of the equation that
those older hands are actually spending
their older coins and as a result we
have an influx of new buyers which
generally increases the probability of
some kind of market top
so during this process we're going to
step through and build our first set of
metrics we're going to add all of these
tools to our workbench put them onto the
correct axis and scale and just
understand what the fundamental tool set
is for workbench
we're then going to convert our supply
in percent which is what the base level
of supply loss active is in a percent of
circulating we're going to convert that
into a btc volume so we can see it and
compare it to things like our
circulating supply
and we're they're going to construct a
new metric called coins younger than one
year which is essentially the inverse or
the opposite side of the equation to our
supplier last active or in other words
supply older than one year
and then we're going to close out this
session by looking at the supply net
position change we're actually going to
calculate one of these there's a number
of these styler metrics inside glass
node suite themselves so this will give
you a bit of insight to how we actually
calculate those depending on the
different input metrics and it gives you
a bit more tools that you can go ahead
and actually build your own net position
changes when you find something that
might be interesting or a metric set
that may not have been explored yet
now for this particular session is
targeted at beginners so anybody with
any skill level will get something from
this this really is starting at ground
zero so i do hope you enjoy this this
workbench tutorial let's get started
okay so we're going to start off here
with a brand new workbench we don't have
any metrics applied and we really are
going to build this up from the ground
zero
so as you'll often do the first metric
that we're going to add is price and
this is really it's almost the calendar
of bitcoin we want to see whereabouts we
are in the cycle i will typically set
mine to some kind of medium gray and
turn it onto a log scale
now what you'll see is it's currently
assigned to y-axis y1 which is on the
left-hand side we can change this to a
bar chart if we want to find that area
kind of style but in this case we're
going to keep it as a line
and on these axes you'll note that over
time when we add more metrics let's add
our second metric here it will pop onto
y2 and the next one onto y3 so we do
have to adjust these as we go
so the first metric that we're going to
add is circulating supply now there's a
few reasons for this the first one is
obviously the circulating supply is the
maximum cap of coins and what we really
care about is how many of those are
older or younger than one year
so here i've set this on to y2 and i'm
going to keep all of my supply in btc
terms put onto the y2 axis so just
remember this our y2 axis which is on
the right hand side because it's an even
number that will always be our supply in
btc style metrics
now what you'll see is that we have
price here as m1 and circulating supply
is m2 and that will continue to tick
higher as we add more and more metrics
so the next one we're going to apply is
our one plus metric this is looking at
our supply last active one year ago now
just remember that this here is
presented as a percentage it is not in
terms of btc you'll see here if we hover
our cursor over it we can see that at
the top here it's about 60.7 percent and
that's saying it's a percentage of our
circulating supply so we know that we
can't actually map that if we put this
onto our y2 axis because our circulating
supply is just over 19 million at the
moment we can see that as a percentage
it disappears towards nothing because
it's less than one
so it can't really be compared directly
to our circulating supply
now this is where we're going to step in
and actually build our first formula and
the objective what we're trying to do
here is we're bringing this supply last
active which is a percent of circulating
we're going to bring that into the btc
supply realm so because we're putting it
onto the btc supply axis we're going to
go to y2 remember that's where we've got
circulating supply and our end result is
we want to compare supply last active to
circulating
so we're also going to change the color
of this to a blue color and i'm actually
going to just turn off the legend of the
percent sign and what i will first do is
often i'll rename this metric because
quite often when you start playing
around in workbench you add a bunch of
formulas and you forget what you're
trying to do
so the first thing i'm going to call
this is supply
older than one year
so what you'll see with formula editor
is up here we've got our m1 m2 and m3
which represents price circulating
supply and supply last active and
percent respectively
now what we want to do is take that
percentage of supply which is our m3
metric and we're going to multiply it by
m2 which is our circulating supply so if
we have say for example 60 of the supply
that is older than one year when we
multiply that by circulating it's going
to bring it into the btc realm
now we're going to keep all the rest of
the settings the same and hit evaluate
and draw
and what we can now see is that our
supply older than one year is now mapped
onto the same axis on the right hand
side here and is the same scale as our
circulating supply so we can actually
see that during those bearish markets
during the the market top sorry we see
this decline in circular in supply old
than one year this older hand spending
during bearish markets we see that
re-accumulation commence and those older
hands start accumulating and putting
those coins into cold storage until we
break the all-time high and they start
spending again so we can see this very
very cyclical behavior that we have
coming from the supply last active
so what we're going to do is add another
formula here and we're going to look at
the converse of that so the blue curve
is showing us the supply that's older
than one year we've taken our supply
last active one year ago multiplied it
by circulating and that gives us our
supply that is older than one year
now what we're going to do for this
metric is i'm going to turn this to a
ready pink color and i'm going to put it
also onto our y2 axis because again
we're bringing this into the supply
domain
and what we're going to do with this
metric is the opposite we're going to
say supply
younger
than one year
so what we're looking at here is
essentially you may have heard the term
long term holder and short term holder
we're essentially establishing something
that is very similar to this but using
only the supply last active at the one
year so that one year is the threshold
that we're selecting in this instance to
represent that long-term or short-term
type holder
so to calculate the coins younger than
one year we essentially take our
circulating supply which is all of the
coins in existence and we're simply
going to subtract in this instance f1
which is the calculation that we did for
the supply older then because if we have
our total circulating supply and we
subtract all the coins that are older
than one year then by default we are
left with only the coins that are
younger than one year
so here we can see we essentially have
the exact opposite during periods of
time when our supply older than one year
remember that generally speaking that
when we want have older coins there's a
lot more old coins in the system it's a
more bullish signal typically happens
during bear markets when that
accumulation is taking place but it does
tend to lead to a supply squeeze
eventually so you can see that the
supply younger than one year is equal
and opposite it will decline during
those bearish markets as old of people
with stronger hands come in and buy
coins off speculators people who are
just here for the hype and the
excitement and actually pull those coins
into cold storage where they start to
mature and conversely as we come into
the bull market here's a good example in
2017 we see the exact opposite where
young coin population explodes higher we
see more of that spending from those
older hands the market has to absorb
more and more coins and as a result we
eventually get a market top getting put
in
so you can see here that using a very
very simple set of tools we can actually
build up and understand what's going on
in the cyclical behavior in terms of
coins that are older than one year and
the converse of that which is coins that
are younger than one year
and what we're going to do just before
we move on to the net position change
we're going to hit save at the top here
now you can save it this is an existing
chart for me in my chart so if i hit
save it will save it as is you can also
hit save as so if you want to create a
new variant of this metric and keep your
current one you can essentially fork
that particular workbench and start
working on a new model you can also use
the save as function if you want to copy
somebody else's workbench if you see
someone who shared one of their
workbenches and you want to take it and
continue to innovate on it you can hit
save as and it will put it into your
library
so for the second part of this tutorial
you may see in glass node we have what
we call the net position change metric
now what this is trying to do the
metrics we were just looking at was the
total supply
but sometimes it's a bit hard to
actually observe and understand exactly
what's a good number what's a high
number what is low it takes a bit of
nuance to understand when we're looking
at these base metrics
now what's generally quite important
when it comes to the way bitcoin behaves
and the overall supply dynamics is the
rate of change are we seeing lots of
coins moving into the older realm are we
seeing lots of those coins being spent
back into a young age and this is really
where the net position change metrics
comes into it and the way to think about
it it's essentially a rate of change
over the last month over the last month
how many coins have moved into or out of
one year supply and when we compare that
over time we can see that we developed
this oscillator here in blue and we can
actually see relative to previous cycles
what is a higher level and what is a low
level so it almost brings it into a
domain that we can see it in an
oscillator format but also get good
information about how many btc are
moving between older and younger coins
so the function that we're going to use
here is called difference and it's
abbreviated inside workbench to diff we
open up the bracket and then we have the
particular metric that we want to look
at in terms of the net position change
in this instance m3 would be the supply
last active one year
plotted out in btc
now the second function that we have
here is the period so this is over what
time frame now we've set it here to 30
we can put it to whatever number that we
want but if you set this here to a
period of 30 it's going to say over the
last 30 days how much has this metric
changed so it will look at today's
current value it will look back 30 days
it will calculate the difference between
those two and then it will present you
with the amount of coins that have
changed over the last 30 days now if we
put this to 90 it would be more like a
quarterly change if we did 365 it will
be closer to an annual change so you can
tweak this and adjust it and sometimes
multiple periods are useful but this is
really what this metric is doing it's
taking the difference of a particular
metric over some period we input the
metric that we're looking at and then we
and the period that we select is that
time difference between when we're
looking at and when the what we want to
see the change over that period of time
so here we are back in workbench what
we're going to do is just purely look at
the supply older than one year so this
is the metric that we actually care
about now note that this is actually f1
so we're going to apply this particular
net position change to f1 which is a
function you can do this both to a
metric m3 or m2 or we can apply it
directly to a function so it provides us
with that optionality in terms of how we
want to build these tools
so let's turn this onto a blue metric
and we are going to have this on y6 this
will also show up on the right hand side
as a separate axis and for oscillators
like this i often like to use the bar
style chart it provides us just that
little bit of extra signal you can kind
of see it and differentiate it to our
curve chart so we have plotted up
so as i mentioned in the intro we're
going to say diff we're going to do f1
which is our supply older than one year
in btc terms
comma 30 days and we're going to hit
evaluate and draw
and just so we don't forget we are going
to rename this because often when you
build these formulas you can very very
quickly forget exactly what this is so
this is our supply
one year net
position
change
and you can see that we now have an
oscillator that is telling us on the
right hand axis 500 000 or negative 500
000 btc we can see that this metric goes
down into negative territory when our
supply last active in the background is
declining this is showing spending
behavior and we can see here back in
2013 in both of these different peaks we
had large amounts of spending that was
going on these negative values and
remember with supply older than one year
spending is instantaneous a coin when
it's spent from one year plus is
immediately going to become a zero age
coin
now on the flip side we see that these
metrics start to peak very very positive
during bear markets but remember they
must the coin must mature to the point
of being one year or older so generally
speaking the maturation process is much
later in the cycle it will typically
signal closer to the middle or the end
of a bear cycle once a great deal of
accumulation has taken place and has
been there unspent for over a year
so in this instance we can look at these
highly reactive negative prints as being
that's a point of higher spending it's
telling us that there are exiting there
are stronger hands that are exiting from
the system that creates overhead supply
that the market must overcome now
sometimes it can overcome as we saw in
2017 where we get these large prints for
extended periods of time but eventually
the probabilities of a top getting put
in does start to increase
so that's really a bit of an overview of
how we can use workbench to build out
some very very simple tools um but
really providing us with some very
powerful insights in terms of spending
behavior the balance of coins between
young and old and actually comparing
them to our circulating supply to give
us a bit of a view on just how much
supply is held by these different
cohorts
so thanks for tuning in for this session
you will find a copy of this particular
workbench in the description below for
this video so if you do want to go and
inspect it and save it into your own
library so you can start to play around
with it and see exactly how this was
calculated you are free to do that
i hope that you enjoyed this we're going
to be doing more of these workbench
tutorials and we're going to slowly
build up the complexity so we really do
want people to be studying this and
understanding a little bit more and
becoming a bit more confident with how
we can use these tools to construct even
more robust insights this is a very very
simple example but you can see it has
quite powerful results when used
correctly
so thanks for tuning in for this session
do let me know if you enjoyed it in the
comments and i will see you in the next
one
cheers

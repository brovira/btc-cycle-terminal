# Glassnode Tutorial: Workbench

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=bJs1PQslhRc
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-glassnode-tutorial-workbench.md]`.

---

hello everyone and welcome to a glass
node feature release where we're really
excited to present workbench
so workbench is a tool that we've
released to glassnode studio that really
opens the door to a whole suite of
creativity and innovation when it comes
to on-chain analysis and really is there
to empower our users to just find and
discover new metrics and new ideas and
really take their analysis to the next
level
so we'll start off with a very quick
overview of what workbench is and all
the features that are available and then
we'll actually jump in and build up some
live charts so you can see how the tools
are used in practice
so workbench is a tool that's been
really designed with flexibility and
creativity in mind really giving the
analysts the ability to combine compare
and contrast different metrics all
within a single chart interface
so the tool allows you to plot multiple
metrics available in glass node studio
into a single chart and you can also use
the formula editor to create ratios or
create unique metrics that combine any
of the tools available in glassnode
studio
and really it provides flexibility in
which scales we're using whether logo
linear it allows you to plot these on
different axes for each individual trace
you can select and customize the
different colors whether it be for the
individual metrics or for the formulas
that you create yourself
and within that you can apply all manner
of moving averages and moving medians to
really make sure that you're getting the
insights that you're looking for
and we've also included the ability to
save these chart layouts so you can come
back to it for future reference and
continue to track your analysis in real
time
let's jump across now to glass node
studio and we'll build up some of these
charts using workbench so you can see
how these features work in practice
so here we are in glass node studio
we're looking at our workbench feature
which is nested between dashboards and
our trading view features
on the left hand side we can create a
new chart preset and we can also access
our previously saved charts
and then we have our main viewing pane
where we can add metrics and start up
our analysis
so what we'll begin with is creating a
simple pricing model using the realize
price as our input
so we'll start with our price chart
initially and we'll also use our formula
bar to recreate the mvrv ratio
so by adding price we'll change our
color to a gray
we can see that we can select different
resolutions depending on which data set
we're looking at in this case we can
choose anything from one month down to
10 minutes we'll keep it on the daily
time frame
we can select whether we want to apply a
moving average with a simple exponential
or a moving median with some
pre-selected periods and also an option
to select our own
we're going to change our scale to log
and note how our y-axis is y1 which will
map onto the left hand side and each
time we add a new metric in this case
we'll add our realized price
when we add a new metric it will move on
to a separate axis so we'll see here
that realize price will automatically
snap to the y2 axis which is on the
right hand side and each
odd y axis will be on the left and our
even y axis will be on the right we can
change this to y one and we can see that
it immediately inherits and snaps onto
the log axis that is defined by our y1
axis so realize price is now mapped on
to that same access as price and we can
now see the two performing next to each
other
so the realized price provides an
on-chain cost basis so we can use this
to really estimate the bottom of bear
markets the floor price and then when
price falls below we have a capitulation
zone which generally is the signifies
the end of a bear market
and what we can then do is implement a
formula bar
so note here that our btc price is m1
and our realized price is m2 so if we
want to construct a topping model let's
make this a red color or an orange color
we'll map this also onto y1
and in this case we're going to take m2
and multiply by an arbitrary factor of
4.2
and evaluate and draw
and we can see here that we've now
modified our realized price by a factor
of 4.2 which provides us for a fairly
crude but effective topping model for
bitcoin cycle so we now have a top and
bottom price model using only the
realized price as our input
so if we now want to rename this so we
keep in mind for next time we can call
this the
realized top price
and then we can hit save and we can
either save this as the currently
defined uh pricing models chart or we
can save it as a new if you wanted to
take this iteration and move it into a
new form of analysis
so what we can now do is implement our
mv rv ratio so we'll put in a second
formula
we will call this our mv rv ratio and
the rv
ratio
we'll change our color to blue
and we will map this onto our y4 axis
which will be on the right hand side
actually we can do it onto our y2 axis
in this case
and what we'll set so we have our price
which is m1 and our realized price which
is m2 the mvrv ratio is defined as the
ratio between our spot and our realized
price so we can take m1 divided by m2
evaluate and draw
and we've now recreated the mvrv ratio
as an oscillator that measures the
distance of price away from the bottom
realized price so it's showing when we
have a large degree of unrealized gains
to the upside or unrealized losses to
the downside when it's below a value of
one and we can use this oscillator to
really identify those market tops
alongside reaching our top price model
so we can hit save
and then we can come back and view this
chart at a later time
so here we are in our second set of
analysis and in this case we're looking
at miners so we have price mapped onto
our y1 axis in grey
and we have hash rate mapped onto our y2
axis in orange so what i want to
recreate in this is a very simple
example of the hash rate ribbon
so we've got our zoom set to five years
so we can see this on a linear scale
we can apply a formula
and we have prices m1 and our hashrate
as m2
so in this instance if we want to create
a moving average of our hash rate you
can see here in grey that we have sma of
m1 by 7. so that's telling us creating a
simple moving average of m1 with a
period of 7. so in our case if we wanted
to construct for example a 90-day moving
average of our hash rate we could take
m2 and do sma m2
90.
we can evaluate and draw apply this to
our y2 axis and let's make this a blue
color
and give it a name hash 90 so we
remember it
90.
and now we have a 90-day moving average
of hashrate
and if we can then create a second
formula
we can do sma m2
this will also go onto our y2 axis we'll
leave it as green
evaluate and draw
and this will be our hash nine
so now we've created the two upper and
lower bounds of our hash ribbon let's
change this green so we can see it a
little bit clearer
so now we have our standard hash rate in
orange our nine day moving average of
hash rate in green and our 90 day moving
average of hash rate in blue and note
that when we have negative crossovers
when the nine-day falls down below the
90-day it generally correlates to
periods of minor capitulation so we saw
it in the march 2020 sell-off we saw it
following the actual halving in may
we saw it in the 2018 end of the bear
market and then we saw it again in 2021
when we had the great migration as
miners started moving out of china
so we can start to reconstruct and use
this sma feature and various moving
averages to reconstruct some of these
tools and then apply those to different
models
now one thing to note is that for
hashrate at the moment m2 this is our
standard metric now we note that m2 is
an input to both our hash 90 and our
hash 9 metrics now if we jump into m2
just so you can see the impact of this
and we apply for example a 14 day moving
median
we can see that that actually translates
so that 14 day moving median is now
applied in our hash 90 and in our hash 9
metric so it's actually taking m2
whatever is set on the presets of m2 and
then reapplying it across the entire
system so you can either use these
functions here to create nested systems
or you can actually create modified uh
metrics using our moving median
exponential moving average or standard
moving average and then apply that
across the board so this provides a bit
of flexibility and allows you to create
whatever unique analysis and really
delve into the data and pull out the
insights that you're looking for
so just to close on some final tips to
help you make the most out of workbench
the first is that you can turn off any
particular chart item using the legend
and this can really help to clean up any
of the input components if you have more
complex functions or you just want to
show a particular subset of the data
that you have within your chart
you can also use our information pane on
the right hand side which will show you
the various functions that are available
it will show you different examples
about how to construct different
formulas and also how you can nest
functions inside other functions to
construct more complex metrics
and lastly you can use the share
workbench function which will create a
unique url to your chart and you can
then share it in your various
newsletters or social media to allow
others to interact with your particular
insight

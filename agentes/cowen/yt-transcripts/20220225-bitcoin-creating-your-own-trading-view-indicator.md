# Bitcoin: Creating Your Own Trading View Indicator

**Fuente (VÍDEO):** cowen · YouTube — https://www.youtube.com/watch?v=cWPceZ-C5So
**Publicado:** 20220225 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20220225-bitcoin-creating-your-own-trading-view-indicator.md]`.

---

hey everyone and thanks for jumping back
into the cryptoverse
today we're going to talk about bitcoin
making your own trading view indicator
if you guys like the content make sure
you subscribe to the channel give the
video a thumbs up and also check out the
sale on the premium list which you can
find a link to in the description below
or go to into the cryptoverse.com
let's go ahead and jump in so
as you guys know we use all sorts of
indicators to better navigate the
cryptoverse things like the bull market
support band the regression bands the
fair value the corridor etc okay
all of these are indicators that i i
made using a programming language called
pinescript which is the native language
of trading view so this is not something
you'll have learned really anywhere else
it's just if you want to learn how to
make trading view indicators you have to
learn how to use pine scripts but if you
have any type of experience with things
like python or any programming languages
it should not be that difficult to pick
up
even if you do not have experience with
programming languages i do want to take
a few minutes to show you how how some
aspects of it are are relatively simple
and the goal of this video is to at
least get you to make one trading view
indicator and and then we will we'll
take it from there
so uh first of all if this tutorial is
helpful to you and you make an indicator
that that you like and you want people
to see then why don't you go on over to
the into the cryptoverse subreddit which
you can find a link to in the
description below as well and and you
can post you know your training
indicator over here and then maybe in a
week or something we'll go through all
the different ones that were created
okay so let's go back to the chart and
what we're going to do is we're just
going to briefly go through how to make
a fairly simple indicator all right so
all you need to do is you need to go
down to pine editor which is at the very
bottom of the page and you just click on
it and it'll pull up something that
looks like this
so
there's a few things here at the top
you'll have you know you'll have like
you know your username and whatever the
version the the title of the script and
then it'll it'll just say i mean you
don't need you don't need the to plot
the close because we're gonna we're
gonna make our own now first of all i
think version five is relatively new and
i haven't actually fully gotten well
versed on all of the new syntax i
believe there are some changes to the
syntax so i'm going to go ahead and
change that to version 4.
i don't think they're that different but
i know there are some differences and so
i'm just going to go ahead and change it
to version 4 and i know that i need to
i'm going to change this to study so
we're going to create a new indicator
and we are going to
call this
dubious speculation all right
now
as you guys know in trading view it is
fairly easy to pull up a moving average
you just go on go on over to indicators
at the top and then you type in moving
average and you can see there's a moving
average right here and moving average
will pop up and you can click on this
moving average and you can go to inputs
you can change the length to you know a
longer term moving average let's say 100
weeks you can change the style to you
know whatever you want and you can get a
nice moving average to to
maybe give you a better understanding of
where the price of bitcoin is with
respect to prior prior price action
now you can also create this in pine
script okay and actually you can you can
have a little bit more flexibility with
it if you if you if you know what you're
doing so what we're going to do is we're
going to remove this and we're just
going to create it okay so we're just
going to type in a variable we're going
to say a equals okay and here we're
going to type in sma now sma
if you guessed it right just simple
moving average so this is part of the of
the programming language just the simple
moving average and in parentheses we're
going to be taking the simple moving
average
of the close so we're actually going to
be taking the closing price each you
know each each candle over a certain
time period and we're going to say 100
weeks all right so if we do that and
then we just say plot a we're basically
plotting the 100 week moving average add
to chart
now
what happened here
it didn't put it on the actual chart up
here but it created another box with a
100 week moving average this isn't as
helpful right you want to see it with
the chart so where did we go where did
we go wrong
all you need to do is you need to
understand that the default is to not
overlay the indicator over the price
over the price chart but all you need to
do to fix it is you go on over to the
study you type in
comma overlay
equals true
if you do that and you click add to
chart
it puts the 100 week moving average up
here
so
if you type in overlay equals false
which is also the default
it'll put it back down here okay and you
could even very quickly put up a lot of
moving averages if you wanted to you
could type in the 20 week you could put
that up there and then you could just um
let me change this back to true but you
could you know you could easily add many
different moving average
moving averages fairly quickly just by
just by doing something like that but
let's say you want to manipulate these
moving averages to some degree right you
don't just want to pull up a moving
average because that's boring you can
easily do that just by going on up to
the indicators you want to provide you
know perform some type of analysis okay
what you can do
is you know let's say we want to one
thing i've said before is that bitcoin
experiences diminishing volatility over
time and and and one of the ways you can
look at that is you can look at the
extension from various moving averages
various long-term moving averages so
let's put that theory to the test so
we're going to do is we're just going to
create a new variable and we're just
going to call it b we're going to set it
equal to the price so we're going to set
it equals to the close divided by a
and we're going to go edit a and make
this the 100 period moving average this
is on the weekly time frame so b equals
the closing price divided by a which is
the 100 week moving average now if we're
going to plot b
let's go ahead and do that
and we want to go back over to overlay
equals true and change that to false
because we don't want it to we don't
want it to be over the price we want it
to be a separate a separate chart so
then we're just going to go over here
and we're going to type in add the chart
and you can see it puts it down here
and if you zoom out what do you notice
you notice that you get diminished
volatility over time and that over time
you know the extension from say
the the
100 week moving average diminishes
okay it diminishes over time but this is
the expectation right so the next time
it comes back up to this level we might
say all right well hey guys this is
getting pretty far extended now might be
time to take some profits but i think
this is i'm not all right this is not
financial advice of course i'm just
giving giving um
uh um just my perspective on the market
so then you know you can see how quickly
it would be to you know to perform all
sorts of analysis on this um you can
even do things like
we could even change the variable b
uh and actually you could actually
change a really quick you could change
it to a different moving average you
could change it to the 200 week moving
average then check that out and see how
that one looks as well um but then
furthermore you could do something like
take the
100 week moving average and divide it
by the 200 week moving average so we're
going to set a equal to the 100 week b
equal to the 200 period and then we're
going to set c
equal
to a divided by b
add to chart
then you get something that looks like
or yeah then you get something that
looks like this
okay
now what's interesting is in this in
this case you're basically just taking
um
the the 100 week divided by the oh sorry
we're plotting the wrong thing we're
plotting we're plotting the 200 week
moving average that's why it looks weird
we need to plot c okay so we're this is
just the 200 week moving average that's
why it looks weird if we plot c
this is what you get right you're
plotting the 100 week estimate divided
by the 200 week estimate and then you
could even further analyze this and say
all right well you know are there any
are there any useful parts of this
indicator and i mean yeah i think there
there could be right if i can if i can
fix this so if you first of all if you
look at say
the you know the the peaks
uh in in the um in this concave convex
structure you'll notice that do they do
they tell a story at all
not really right not really because the
bottom tends to be well after the actual
bottom the top tends to be well after
the actual top what could be more
interesting is to potentially look at
changes in concavity okay so like from
going from you know going from um you
know being concave up basically we're
looking at at the um the convexity of of
this of this function and so when you
when you see this change in concavity
here
what you notice is the change in
concavity actually does get close to a
peak right
and the change in concavity here while
it doesn't get you you know it doesn't
get you
right at the bottom
but it does tell you you know it does
more or less get you in in the ballpark
right i mean this this was the actual
bottom over here but this one was pretty
close same thing over here right this
was the actual bottom but there was sort
of like a a proxy bottom that took us
down to 3 800 which wasn't that far off
and it was fairly close to that change
in concavity so
this is just something you can use to
you know to better navigate the
cryptoverse and then you know you spend
a few minutes looking into this stuff
you could find all sorts of things that
you maybe wouldn't have found before
just with the basic tools that
tradingview has to offer so
let me know what you guys think about
this you can also do things like plot
plotted in a different color if you want
i mean i don't know why you would
necessarily want to but if if you want
to you can um you just type in uh color
equals color
i don't know dot lime i believe that's
the right syntax when using version four
you type add to chart yeah you change it
to a different color
you could then say plot something else
right you could i don't know plot plot a
different function if you want to um
maybe maybe this time we'll plot
um
uh let's let's plot a new variable and
call it d and we'll say that d
is equal to a
divided by b divided by b so now we're
taking the 100 week moving average
divided by the 200 week moving average
squared and then we're gonna we're going
to plot that one
in in red and if we do that what do you
get you get this
uh well no i'm plotting i'm plotting c
again let's plot d let's see what let's
see what happens when we plot d
you get something that looks like you
get you get this okay so and we're
plotting two things here we're plotting
c and d
um so that's why it doesn't really
that's why you can see one and not
really the other
but if you just plot one of them that's
what you get okay so
all sorts of different types of analysis
you could do with this stuff if you just
take you know take some time to
to go through it and and to explore
various things obviously we're just
scratching the surface of what you could
look at um
so many more things you could you could
dive into but i just wanted to put a
video out there and show you that you
know making trading view indicators
isn't that challenging and i you know i
think anyone could do it if you just
take a few minutes to to try to learn
some of it and if you do make something
that's cool and you want to show people
then go on and over go on over to the
into the crypto subreddit post it there
um
maybe maybe title it like you know like
into the cryptoverse
uh tradingview indicator or something
just so it easily catches my attention
and and then maybe in a week or so we'll
we'll go through all the different ones
that were submitted and and you know see
how they are so hopefully you guys like
the content let me know what you guys
think about this in the comments below
make sure you subscribe to the channel
we also the premium list into the
cryptoverse.com we have a sale going on
right now so if you want to lock in the
lower rate go ahead and do so that's
going to end here probably in about a
week so make sure you do that before it
ends and i will see you guys next time
bye

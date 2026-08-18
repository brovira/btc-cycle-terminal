# Precious Metals: Portfolio Optimization (Gold, Silver, Platinum, and Palladium)

**Fuente (VÍDEO):** cowen · YouTube — https://www.youtube.com/watch?v=2tyzFiHfZSA
**Publicado:** 20200630 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20200630-precious-metals-portfolio-optimization-gold-silver-platinum-and-pallad.md]`.

---

hey everyone and thanks for jumping back
into the precious metal verse today
we're going to be talking about
optimizing your precious metal portfolio
based on modern portfolio theory so if
you guys liked the content please go
ahead and subscribe to the channel give
the video a thumbs up and also let me
know what you guys think about the
content in the comment section below and
if you want to discuss these charts you
can check out my telegram channel as
well which you can find in the
description below so let's go ahead and
jump in so we're going to be looking at
four different precious metals in this
video and how you can use historical
data to potentially optimize your
portfolio based on your expected returns
and the volatility or the risk so the
four the four metals that were looking
at are gold silver platinum and
palladium and we're gonna Fort we're
gonna start with a brute force approach
so Monte Carlo method to obtain the
portfolio with the highest risk adjusted
returns okay this is the Sharpe ratio
and then we're also gonna look at the
portfolio with the lowest volatility so
maybe you're a little bit more
risk-averse than you know most people
and you would rather sit on a portfolio
where the where the volatility would be
lower but your expected returns would
also be lower we're then going to finish
the video with you know using quadratic
programming to just solve for the
portfolio waves which maximize your risk
adjusted return so we're gonna
systematically go through the process so
I hope it's informative to you guys and
then you can always leave me a note down
in the description or in the comments
section below telling me what you want
to see in the future you know there are
other precious metals we certainly cover
a lot of different assets asset classes
on the channel so just let me know what
you guys think so to begin with the
first thing we're gonna look at is we I
ran a hundred portfolios so I just
looked at a hundred different portfolios
so there's really no initial pattern
emerging here and you can see that what
we're looking at is the expected return
and this expected return is based on
historical data for these for precious
metals going back to the 1990s the early
1990s you obviously you could change
your expected return to be what you
project out for the next decade to be
and use that and feed that in and we're
probably gonna do that in a future video
but for this video we're just looking at
historical returns I mean I even got the
daily timeframes so we have the daily
timeframe but its annualized so you know
if you see say 0.06 then for annual list
I mean 6% annual versus volatility and
this this is what a lot of people would
consider say your risk level now it's
color coded by the Sharpe ratio and the
Sharpe ratio is your expected it's your
it's essentially your you know your
excess return over your your volatility
level and you can see that it goes from
around point one to two point four which
by other asset class standards is not
that great but we'll talk about we'll
talk a little bit more about that at the
end of the video so in terms of 100
portfolios so we just ran a hundred
different completely rendom portfolios
we plotted the expected return versus
the volatility it turns out that the
portfolio that maximizes your Sharpe
ratio or your risk adjusted returns is
the green star and you can see that for
that the portfolio would be weighted
around 44% gold point six percent silver
seven and a half percent platinum and 48
percent palladium now is this important
it's not important at all we only ran a
hundred portfolios when you have four
different assets only running a hundred
different portfolios is essentially
nothing and it's meaningless but I just
want to get you guys accustomed to the
approach if you wanted to minimize your
volatility so you don't want to maximize
your Sharpe ratio but you'd prefer to
minimize your volatility you could you
know you could come over on into this
level over here and by the way I mean
this is this red star here you can see
it's as far left on the curve as you can
go and to do this you'd be you'd be
looking at around fifty eight percent
gold
six percent silver 27% platinum and nine
percent palladium now let's run let's
run more portfolios because 100
portfolios isn't a whole lot but I just
want you guys to see the the
bullet-shaped develop of the efficient
frontier you know using this
portfolio theory so running a thousand
portfolios you can see that our gold has
gone from 43% it found a much better
portfolio to maximize the Sharpe I found
67% gold 2.2 percent silver one point
nine percent platinum and 28 percent
palladium would maximize your Sharpe
ratio given a thousand random portfolios
to minimize your volatility you can see
the gold is a lot higher so you would be
eighty-one percent gold one and a half
percent silver 16.6% platinum and point
six percent palladium this is again is
with a thousand portfolios now again you
shouldn't dwell on these numbers I'm
just showing you how they converge and
then we're gonna use a little bit of
quadratic programming at the end to just
solve for the best portfolio but if you
if you ran it for say ten thousand
portfolios you can see that we're
starting to hone in things aren't
changing quite as much it would be
around 64 percent gold 0.7 percent
silver 0.3 percent platinum and 34
percent palladium and then to minimize
your volatility so at the leftmost point
on this curve so this would basically be
the beginning of the efficient frontier
because down here would essentially be
the inefficient frontier you wouldn't
want to be down here at a portfolio
because well for the same risk level you
could be all the way up here with a much
higher expected return based on
historical data so with that said to
minimize your volatility give them ten
thousand random portfolios it found that
the portfolio consisting of 72 percent
gold one percent silver 22 percent
platinum and four and a half percent
palladium minimized your volatility now
the largest amount of cases I ran for
this before I just you know went
switched over to quadratic programming
just to get a nice looking bullet shape
here was a hundred thousand portfolios
and you can see that the weight isn't
really changing you know as much now but
it is still changing some so in order to
maximize your portfolio here it ended up
being around 73 percent gold and 26
percent palladium with small portions of
silver and platinum and then to minimize
your volatility it was mainly just 77
percent gold and 21 percent platinum
with a little bit of silver and
palladium mixed in
okay so this covers it for just looking
at say a hundred thousand portfolios and
going to Monte Carlo approach now before
we get into the quadratic programming
portion of the video I wanted to show
one more thing what if you wanted to or
a couple more things what if you just
wanted to you don't care about the
Sharpe ratio you don't care about the
minimum volatility ratio all you care
about is you want to look at your
expected returns of the past so or look
at annualized returns historically and
then use that to project what would be
you know essentially this data point way
up here that maximizes your expected
returns you don't even care that it
gives you a volatility level of 30%
which would mean by the way if your
expected return is 8% and your
volatility is say 30% then to a 68
percent confidence level so one standard
deviation your expected return would be
8% plus or minus 30% which means you
could easily see a negative return but
you know an expected annual return does
not mean you have to see 8% it just
means that within one standard deviation
your expected return would be say 8%
plus or minus 30% which is a lot higher
than say your expected return being say
6% plus or minus 17% if that makes sense
for the lowest volatility level so for
the highest expected return based off
the hundred thousand portfolios that I
ran it turns out that it would have been
five and a half percent gold two point
four percent silver 91 92 percent
platinum and point three percent
palladium so this would be to maximize
your expected return based on historical
data you know since the 1990s now
with all that said let's get into you
know the the other part but you know
before the quadratic programming of
looking at what what if you don't care
again about the Sharpe ratio you don't
care about minimizing your volatility
you just have a certain risk level
you're okay with and you apply this
across various asset classes if you're
if you're if your volatility that you're
okay with is 20% then your your in order
to go to 20% if you went up to the
efficient frontier so this curve up here
then
maximizing your expected return for a
risk level of 20% your weights would
have been around 44% gold and 50 55 %
palladium with a little bit of silver
and platinum this would have given you
an expected return of 7.2 percent okay
and I should note that I gave this a
little bit of Tolerance
so each percent here said 20 percent
it's plus or minus 1% and then 25
percent it's also plus or minus 1% so it
could be down to 23 percent or 24% and
could be as high as 26 percent so 20%
volatility it would correspond to you
know one of the data points right here
giving you an expected return of around
7.2 percent on this these would have
been the weights if you were to have a
little bit higher of a risk appetite
then maybe your your risk level is 25
percent and you know you came up here
you you found the portfolio that gave
you an expected return of 7.9 percent so
way up here that portfolio would have
consisted of 21 percent gold and 25
percent palladium and that's just a
random portfolio I mean that was what
maximized it at that level there's
obviously other portfolios around that
level that would have you know had very
either could have had very different
weights and then finally to to get the
highest expected return at a volatility
level of 30 percent then it would have
looked like basically hardly anything in
most of the assets and then most of it
94 percent in palladium so I hope that
makes sense at least in terms of these
fork for for precious metals this is
what the data suggests now what if we
just switch over to quadratic
programming
you know we map out our efficient
frontier and we find the best Sharpe
ratio well to find the best risk
adjusted returns based off historical
data for the last few decades it turns
out that your portfolio would
identically consists of 73.3% gold 26.7%
palladium and 0% silver and 0% platinum
so essentially what it's doing is it's
saying you know what
to maximize the Sharpe ratio you really
don't want any silver you real
don't want any platinum you just want
gold or palladium now I know this
doesn't necessarily please everyone I
get there's a lot of people that think
especially you know silver is very
undervalued and for all I know it could
be undervalued I'm just going off
historical data since the 1990s if I
were to change the data to maybe go to
you know start at some other timeframe
then maybe we get slightly different
results and maybe in a future video
we'll go through ok these would be the
results if you were looking at say
different time frames but for the
purposes of this video I just what I did
was I just went as far back that I could
find reliable data for for each asset so
of course I could find gold not a lot
further some of the other coin you know
some of the other currents are the
precious metals I could find back
further but in order to find daily data
for all four of them the best I could do
in about 30 minutes of searching was the
1990s and this is daily data okay so in
order you know again the best one in
terms of quadratic programming would be
around 73% gold and 27% palladium in
future videos we'll also again talk
about different time frames we'll also
talk about putting in maybe you know a
projected return and using that as our
expected return and you know that would
obviously take a lot of you know
additional research into you know into
each precious metal to identify you know
what do we think an expected return
could be over the next five to ten years
so if you guys liked the content please
go ahead and subscribe to the channel s
toric ly have spoken mostly about
cryptocurrency but it turns out you know
I find I find applying these these
methods to other asset classes are very
useful and you know and we can we can
systematically go through each asset
class and I and apply similar types of
analysis so we're gonna continue to
build this out I would encourage you to
subscribe to the channel give the video
a thumbs up share it with with a few
other people if you think it was if you
think it was worthwhile and then also
the last thing I wanted to talk about
was if the Sharpe ratio is so low is
there a reason to include precious
metals in your portfolio for instance
with cryptocurrency we found that the
Sharpe ratio given data from 2015 is
around 1 and with traditional markets -
you know it tends to be a round one I
mean it can obviously fluctuate around
that level but around 1 is a decent
Sharpe ratio so when the Sharpe ratio
precious metals being so low given
historical data going back a few decades
is this something you would want to
include in your portfolio and in order
to assess that we'd have to you know put
put in you know these precious metals
into a portfolio consisting of index
funds consisting of other asset classes
and while it might you might think well
why would it why would precious metals
be included in something at the Sharpe
ratio so low you have to remember that
including assets that are uncorrelated
to each other can help you know if
you're if you're including say gold and
the covariance between gold and another
asset you hold is low then when you're
when you're calculating your covariance
matrix and solving for you know solving
for your you know your your risk
adjusted returns having uncorrelated
assets is is useful because it overall
would reduce your volatility which
reduces your subsequent risk so that's
not to say you know one way or another
yet we're gonna we're gonna dive into it
if you want to make sure you see these
videos in the future be sure to
subscribe to the channel if you like the
content a lot and you want access to
some premium content I do have my own
website it's actually into the cliff
divers comm because I did launch this
channel primarily looking at
cryptocurrency so go check that out into
the cliff divers calm and you'll get
access to premium videos premium
newsletters dating back a little while
and also access to the Google sheets
dashboard where I have you know I'm
regression analysis on like you know
things like the total cryptocurrency
market cap we also have stuff on Tesla
we're gonna be putting more stuff on
precious metals so check it out I'd love
to have you guys join if you sign up you
can you know it's just a monthly
subscription so if you if you sign up
I'll see you in your inbox soon
otherwise please subscribe to the
channel and I will see you guys next
time bye

# Cryptocurrency Portfolio Construction

**Fuente (VÍDEO):** cowen · YouTube — https://www.youtube.com/watch?v=olyYMQEYwt8
**Publicado:** 20221209 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20221209-cryptocurrency-portfolio-construction.md]`.

---

hey everyone and thanks for jumping back
into the cryptiverse today we're going
to talk about cryptocurrency portfolio
construction using modern portfolio
theory if you guys like the content make
sure you subscribe to the channel give
the video a thumbs up and check out into
the cryptographers premium at into the
cryptiverse.com let's go ahead and jump
in so we do videos on Modern portfolio
Theory every few months and the reason
is because I want to show people various
ways that you can go about trying to
construct a cryptocurrency portfolio
there is a common misconception that
there exists a portfolio that is right
for everyone however there are
portfolios that suit various risk
tolerances so what I want to do in this
video is what we're going to start we're
going to start off by looking at the
sharp ratio and the sortino ratio for
Bitcoin and ethereum portfolios and
they're going to expand to a few other
altcoins and see how they would affect
your risk adjusted returns
to start I should I should probably
explain the the chart in in great detail
the expected return is the y-axis and
the volatility is the x-axis so if you
wanna if you want to see the expected
return as say 0.7 that means your
expected annual return would be 70
percent
based on historical returns now one
important thing to point out
as always is that historical returns are
not necessarily always a great predictor
of future Returns the secret sauce that
a lot of hedge funds might use rather
than using historical returns to project
out expected returns they would probably
make their own projected returns and use
that as the expected return for various
assets to try to figure out what
portfolio would then maximize their risk
adjusted returns so if you were looking
for say an expected return of 75
annually on average than you would based
on historical returns then you would
come over here to 75 percent go all the
way over until you find that portfolio
that matches that return which in this
case would be about 27.6 Bitcoin 72.4
percent ethereum now if you want to get
a sense of the volatility of a portfolio
like that if you go down you can see I
actually correspond to about one which
is about a hundred percent so the
expected return of that portfolio
specifically based on historical returns
would be approximately 75 percent plus
or minus a hundred percent meaning to
within one standard deviation or a 68
probability your expected return is
going to be between negative 25 up to
175 percent I know that sounds like a
lot
welcome to crypto right the volatility
is insane some you know some years these
assets can go up 10x and then other
years they can go 90 down so that's just
the nature of the asset class again
don't take it up with me taking up with
the data that's what the data puts it
out puts it out as so there's a few
different things you can look at so the
first thing you might want to do for is
figure out you know what volatility are
you comfortable with which is sort of
like thinking like what risk are you
okay taking on
if if you only want to take on a low
amount of risk with respect to this
portfolio so you're already taking on
some Risk by just being in crypto in the
first place but if you want to be say
like in Bitcoin and ethereum only
you need to figure out what type of
volatility are you okay with at the
lower end of the curve right you can see
that you would have more Bitcoin like
you can see over here it's like 92
Bitcoin or 93 Bitcoin seven percent eth
that gives you a relatively lower
expected return but it also gives you
lower volatility as well
if you go up the efficient frontier
meaning you're looking at higher
expected returns based on historical
returns you'll see that the amount of
Bitcoin as you go up becomes a less per
a lower percentage in the amount of
ethereum becomes a higher percentage so
if you go all the way up to the top you
can see that it would basically be about
you know 100 ethereum and and basically
zero percent Bitcoin if you wanted to
take on you know the essentially the
most amount of risk based on the
historical performance of just these two
assets okay
one Nuance I should mention are a couple
of them one is that we can only use data
going back to the youngest asset so in
this case ethereum has been around since
2015 so we can only really use price
data from Bitcoin that's since 2015 as
well we can't really use price data from
from prior years because we don't really
have anything with ethereum to compare
it to because it just simply was not
around then so that's an important thing
to remember as well the second Nuance
that I want to mention is that it says
we're displaying 5000 of 50 000
portfolio simulations so the way you can
think about this is some Monte Carlo
based approach to to helping people
visualize what the returns would be that
would probably cause you to question
well does it mean that if you were to
run another 50 000 simulations you would
come up with a different answer since
it's a Monte Carlo based approach and
normally the answer would be yes you
could come up with a different solution
however in order to figure out what
maximizes your risk adjuster returns in
this case a sharp ratio and sortino
ratio what I've done is we actually have
made it so that we we use some quadratic
programming to then actually solve for
the portfolio that maximizes your risk
adjust returns rather than having to go
a Monte Carlo approach and just brute
force it so there's two ways you can
look at the portfolio which maximizes
your risk of dose Returns the way to
think about that is for a given amount
of expected return You Wanna you wanna
basically maximize that per unit risk
that you take on
so if you do this over all portfolios
there exists one that provides the best
risk adjust return and we're going to
start with a sharp ratio and in the
sharp ratio the portfolio out of Bitcoin
and ethereum that maximize your risk of
dose return is actually 68 Bitcoin 32
percent eth so just over two-thirds
Bitcoin and just under one third each
seems somewhat reasonable right and and
maybe that's what your gut would tell
you that a majority of Bitcoin would
actually help maximize your risk advice
return because yes ethereum can give
oversized gains in in Bull markets but
it has also shown to at least
historically to drop more in Bear
markets now right now it it's actually
you know it's been holding the June lows
for a while but also recognized that
when I hit that June low it was actually
down 80 82 percent or something in
Bitcoin so far this bear Market has only
gone down about 77 at its low so that is
something to consider
however the the one of the issues with a
sharp ratio if you're unfamiliar with
what the sharp ratio is it's basically
just
um you know the return of the portfolio
you know based on what you're expecting
it to be minus the risk-free rates like
treasury yields divided by the standard
deviation of the portfolios excess
return the excess Returns the return you
know taking out the the return that you
could get just get from the risk-free
rate so thinking about it like that
it actually punishes positive volatility
which is not necessarily something that
a lot of people want to do if you're
trying to figure out what portfolio is
going to maximize your returns your risk
address returns you don't necessarily
want to punish positive volatility right
like are you gonna be upset if if
there's a lot of volatility because the
asset went up a lot probably not so you
can go with the sortino ratio which
maximizes your risk adjusted returns but
only punishes negative volatility and in
that case you can see there's a slightly
different answer in that in that
instance it actually comes out to be 67
Bitcoin 33 eth so about two-thirds
one-third in that situation what this
shows is really no matter how you
measure it you're essentially coming out
with two-thirds Bitcoin one-third each
to maximize your risk adjusted returns
whether you punish whether you punish
positive volatility or not
if you don't really care about
maximizing your risk adjusted returns
then you could say for a given
volatility what risk are you okay taking
on perhaps it's 85 percent
maybe 90 percent volatility 95 percent
whatever it is you know you you could
pick it and then come up here and then
figure out what portfolio that would
correspond to and then you just live
with the results and also recognizing
there's no sure thing past performance
is not necessarily an indication what's
going to happen in the future and and
furthermore
um
you know it's all the probability of
occurring even based on this chart would
be within one standard deviation or a 68
probability that would be that return
plus or minus the volatility that is
associated with it so just something to
consider and and you know I can just
sort of scroll through right here so you
can see the portfolios
um portfolio percentages that are on
that certain volatility level in case
you're interested in that now it becomes
a bit more interesting when you
add in a few other assets right so like
let's add in Litecoin and let's add in
Monero and let's add in
xrp and then recalculate it and see what
that gives us okay now if you do it like
this you'll see something that looks a
bit more aesthetically pleasing right
and the whole idea in this situation is
that now for a given volatility level
there's more than one portfolio that
would correspond to that because there's
so many different ways that you could
um run you know run these simulations
with various weightings of five
different assets and so the idea is that
for a given volatility level there
exists a single portfolio on the
efficient Frontier which is this green
line up here that maximizes your risk
adjusted returns so for instance if you
wanted to say take on about 90
annualized volatility and you you come
up here and you see this one of these
first portfolios it says 21 Bitcoin two
percent eth 29 Litecoin four percent
Monero and then 44 xrp but the problem
with that is the expected return for
that 90 volatility level is only about
50 and for the same type of volatility
based on historical returns you could
come up here to the efficient Frontier
okay so you're taking on basically the
same amount of risk based on the
volatility of it and the expected return
though would be much higher so in this
case it would be you know like 26
Bitcoin 51 percent eth one percent
Litecoin 15 Monero and seven percent xrp
okay
does that make sense right so in this
situation there there's there's multiple
portfolios which correspond to that
volatility level ideally I think it
would make sense to be on the efficient
Frontier which is maximizing your
expected return for that given
volatility level okay that is generally
the idea and in this case we can also go
over here and see what maximizes your
sharp Ratio or your risk adjust returns
punishing both positive and negative
volatility and would be 57 Bitcoin 28
eth zero percent Litecoin thirteen
percent Monero two percent xrp people
always get upset with me about the zero
percent Litecoin again that's just what
the data suggests if you are a Litecoin
fan
I will say the good news for you is that
one of the best times that Litecoin
typically has with respect to some of
the other assets like Bitcoin ethereum
is about half a year before it's having
and the next having for Litecoin is
coming up in about you know summer of
2023 or so so perhaps you will see it
slightly show some relative strength for
a little while but do note that relative
strength is usually short-lived sometime
after the having with respect to
ethereum and it's not that Litecoin
can't go up against its US dollar
valuation in a bull market it did in the
last bull market but it basically went
to the same level that it went in 2017.
it's just that the the opportunity costs
of not putting that of not putting those
dollars in say ethereum that did go and
put in new all-time highs and Bitcoin
that also went and put a new all-time
highs is actually quite high so again
it's not that you can't make money on it
in a bull market it's what's the
opportunity cost and is it worth having
in your portfolio during a bull market
if it means you're not seeing those same
types if it means your dollars are not
at work in other assets which tend to
give oversized gains with respect to
Litecoin but again that you know going
into Litecoin having it it can show a
bit a bit higher performance than it
typically does otherwise and the
portfolio that maximizes your sortino
ratio is 48 Bitcoin 36 ethereum zero
percent Litecoin again 15 Monero and one
percent xrp and then finally the
portfolio that minimizes your volatility
would be 80 Bitcoin six percent ethereum
one percent Litecoin five percent there
you go for the Litecoin fans five
percent Monero and eight percent xrp
so the whole idea is you know there's
not a portfolio that is going to rule
them all there's not a portfolio that is
going to necessarily make sense for
every single person there's a portfolio
that makes sense for you there's a
portfolio that makes sense for me okay
if someone's heavier Bitcoin it just
means they want to take on less risk if
someone's heavier eth it means they want
to take on more risk
there were the you know the expected
returns and the volatility levels are
there for you to see you understand what
it is you know what is the risk you're
taking on based on what we've
historically seen and then you just live
with what happens if if it does well
yeah you're what you don't think you're
lucky if I mean I said this back in 2019
right like if you pick a portfolio out
and you construct it and and you end up
making money on it yeah I don't I don't
think you're lucky it's just you took a
calculated risk and it paid off or it
did it right it's just it's just a risk
and you got to figure out what you're
willing to live with and what you're not
willing to live with and and
um and that's about I mean that's about
as much as you can say with regards to
portfolio construction using uh using
some of these tools I mean I hope you
guys find this helpful uh I do
understand that this can be very dry and
and not very exciting and there's
probably a lot of other videos that are
a lot more enticing and for the 10
people still watching I commend you uh
but these are the types of videos that
we we do a lot
um especially especially you know a year
or two but for hopefully another bull
market because spending time figuring
out the best way to construct a
portfolio it can make a huge difference
later on right like it doesn't really
seem like it in a bear Market
um but it can make a huge difference
later on small tweaks right small
percentage tweaks and various assets can
go a long way once you get out to the
bull market just kind of looking at
which ones are are fundamentally
stronger than the other ones which ones
have a track record of doing well which
ones do not and so on and so forth so
again the main takeaways from this are
using modern portfolio Theory to
construct cryptocurrency portfolios via
minimizing your volatility or maximizing
your sharp Ratio or sortino ratio in
order to
basically just maximize your risk
adjuster returns for a a given
volatility and and that's about it I
mean that this is this is why I've
created this tool on the website again
this is modern portfolio Theory it's not
something I created it's been been going
back decades but I put it on the website
and applied it to a few older
cryptocurrencies just so we kind of see
how it performs you might ask well why
don't you have any newer
cryptocurrencies again this stuff really
only works well if you have usually at
least a couple Market cycles of data
otherwise there's just not really a
whole lot to compare to if if an altcoin
that you're interested in has never
experienced the full brutality of a bear
market then it just simply cannot be
used I think in any effective way in
modern portfolio Theory just because you
don't really know the the drawdown now
again it could be used in more effective
way if you want to project out returns
rather than use historical returns but
if you're if you're just sort of taking
a more conservative approach and using
historical returns then it's not really
that that valid if it hasn't experienced
the full brutality of a bear Market
hopefully you guys like the content
remember to check out into the
cryptiverse premium if you do we do have
several different tiers so I know I know
some people were asking about that make
sure you check it out links in the
description below one of the tiers is
actually free so you can check that out
thank you guys for tuning in make sure
you subscribe I'll see you guys next
time bye

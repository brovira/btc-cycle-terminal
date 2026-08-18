# Bitcoin and Ethereum: The perfect portfolio balance

**Fuente (VÍDEO):** cowen · YouTube — https://www.youtube.com/watch?v=mHwXiGWNr1c
**Publicado:** 20201228 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20201228-bitcoin-and-ethereum-the-perfect-portfolio-balance.md]`.

---

hey everyone and thanks for jumping back
into the cryptoverse
today we're going to talk about bitcoin
and ethereum
and investigate ways that you can
balance your portfolio
based on historical data if you guys
like the content please subscribe to the
channel give the video a thumbs up and
also check out the telegram channel
which you can find a link to
in the description below so the purpose
of this video
is you know whenever the markets start
flying and bitcoin
goes up and ethereum goes up and the
markets start moving up
everyone will put out rate my portfolio
type post
and they'll want to say okay what is
what is a good a good portfolio to have
based on percentages
and they will seek the advice of
random people on the internet to give
them some validity
as to are they making a good choice well
my argument is that there's a much
better way to do it don't listen to
people's opinions
about things is my philosophy stick with
the data
right stick with the data what does the
data tell you
and go with that because to me that's
much more important than what anyone
any one specific person necessarily
thinks
everything's usually hidden or maybe not
so hidden
within the data so what we're going to
talk about here is something we've
talked about on the channel before
it has been a while though this is
modern portfolio
theory quantitative finance this is what
a lot of people use
in traditional banking and investing so
what it is we're plotting here only
bitcoin and ethereum
we're plotting the expected return
versus the volatility
now the expected return is the
return that we would expect annually
based off nothing more than historical
data
it is not projected returns projected
returns are often the secret sauce
that hedge funds might use to try to
figure out what
what investments they're going to take
so that's another step putting in
projected returns
this is just historical returns starting
from 2015.
you might say well why don't you go back
further well ethereum
launched in 2015 and in order for this
to make any sense at all you need to use
the same time date like the same time
series you can't use
data for bitcoin going back to like 2010
and
e38 going back to 2015 um it wouldn't
really make a whole lot of sense in
terms of like your covariance matrix and
a few other things so
you have to use it the same amount of
time same amount of days
so the expected return one
would be a hundred percent and you might
say well
hold up a second you mean to say that i
can expect a hundred percent return
i'm not saying that it's what the data
says right that's what the data says
is that you can expect a 100
return annually on average of course
there's going to be some years where you
would see an 80
drop there might be some years where you
see a 300
return or something like that if you
think about it the price of bitcoin
from the beginning of the year is up
several hundred percent so
just historical data expected return
annual expected return so one would be
1.1 110 volatility
is also the risk in a sense so if you
want to think about the risk that you're
taking on
you can think of it in terms of the
volatility
this would be 90 volatility 80
70 volatility what the hell does that
mean
right well what it means is if you say
had this
yellow portfolio it means that
your expected return would be 95
to within one standard deviation um
so your expected return would be 95
plus or minus 65
and the return on that would come
within one standard deviation so 68
probability
that your annual return by holding this
percentage of bitcoin and ethereum we'll
get to that in a minute
would give you would yield a 95 return
plus or minus 65 percent
so the lower bound on that would be 30
95 minus 65 so your annual your expected
annual return
lower bound would be 30 because we know
volatility is 65
and then the upper bound would be 95
plus 65 so that would be so if we
160 right um
so just something to keep in mind so
within one standard deviation
a 68 probability that your expected
return
would be between 30 and 160
that's a huge range it's not as bad it's
not as as
um drastic in a lot of other markets but
it's crypto and it's why we're here
so what's going on here these are 10
dots okay
and um they're color coded
by the sharp ratio so these are your
risk
adjusted returns okay there's i don't
actually
i forgot to put the equation on on the
slideshow
but the sharp ratio is is very well
known
in in quantitative finance as modern
portfolio theory
a lot of great papers written on the
sharpe ratio so it's your risk adjusted
returns
i've said before many times it's not
about your return
it's about your risk adjusted return
right i mean think about it like this
would you rather have like a 50
chance of making 5x or a 5
chance of making 10x or something like
that i think most people would choose
say 50
chance to make uh 5x because the odds
are a lot higher and you're still making
a lot of money
yes being very risky in your investments
can ultimately
could theoretically yield you a higher
return but there's many
scenarios where it wouldn't if you think
about it if we live in a multiverse
and there's several other identical
universes that have variations on what
actually happens in in each specific one
if you invest a lot of money into some
random altcoin that someone showed you
on twitter
there's so many different scenarios
where that does not go well
okay there's somewhere it does and a lot
of people can get rich doing it
but a lot of people bet the family farm
and lose it
on on um highly speculative assets and
to some degree bitcoin and ethereum are
highly speculative already
so getting too far down into the mud
with a lot of other coins can does carry
a lot of risk
so you're probably wondering you know
what is this right there's there's
ten dots well let's let's increase it
let's go to say a hundred
and a thousand and ten thousand and a
hundred thousand
simulations so monte carlo approach a
brute force
figuring out which portfolio gives you
the best risk adjusted returns
or the sharp ratio out of combinations
of
only bitcoin and ethereum so only
looking at bitcoin and ethereum
out of all the different portfolio
weightings what would give you the best
risk adjusted return
and you can do it by brute force monte
carlo
simulation where you just look at a
hundred thousand different ones you
could even go higher
and it turns out that you can also
solve for it right uh a bit of quadratic
programming
in in python simple enough right piece
of cake
solve for it figure out you know what it
what where does it
what is the the most optimal portfolio
so based on and the the thing i love
about this
is that it does not matter what my
opinion is right my opinion could be one
thing
the data could say another and so if you
don't like
the results of this don't take it up
with me take it up with the data right
i've said that before about other
projects right
we've looked at this type of analysis
with random all coins before
and it suggests zero percent of that
coin in your portfolio based on its
historical returns and historical
volatility
and that tends to rub people the wrong
way because it might be insulting
you know one of their projects that they
like to follow and my
my response is you know don't take it up
with me just take it up with the data
because the data is telling me what i
need to know
um not my emotions not not you know any
any fundamental factors not oh but the
community it's all about the community
and this community is so much better
blah blah blah right again as i said no
one cares about that stuff
this channel we're here to make money
that's my goal um but we want to do it
in the least risky way possible and not
concerned i don't really want to concern
myself with how
um you know how healthy a specific
community is
show me the data we'll show you the
portfolio
so the portfolio
of bitcoin and ethereum which maximizes
your sharpe ratio or your risk adjusted
returns
based on historical volatility and
historical returns
from 2015 is
74.4 percent bitcoin 25.6
ethereum okay simple as that
looking at historical data historical
volatility returns etc
that's the portfolio which maximizes
your sharp
ratio meaning this star
is the optimal portfolio on the
efficient frontier
this is known as the efficient frontier
you could maybe refer to this down here
as the
as you know the inefficient frontier
because you're you're taking on
the same amount of risk for a lower
expected return
okay and it looks it looks different
with only two coins and it would with
three we'll show you what three
coins looks like in a minute so
74.4 bitcoin 25.6 aetherium
this changes over time uh you know i
think about a year ago
it's it was suggesting 60 40 60
bitcoin 40 ethereum so one you know one
way to navigate the markets is just to
rerun this analysis
every every month or two and re-weight
it right reweight it and that doesn't
mean you need to sell bitcoin to
ethereum or sell ethereum to bitcoin
but maybe if you're focused on
accumulating you could use this type of
analysis to figure out which one to
continue accumulating to get to
that that ideal percentage again this is
not financial advice
this is just looking at historical data
looking at very specific
measurements uh using modern portfolio
theory and presenting the results
okay now some of you are probably
wondering
what if we throw a risk out the window
like you know who does this guy think he
is telling me
he knows what my risk tolerance should
be and
that's a fair point because everyone
has a different risk tolerance you know
if you're if you're
young and in your 20s you might have a
larger risk
appetite than someone who's nearing
retirement
someone who's nearing retirement they
might want exposure to crypto
but they also want to do it in a very
smart and as
risk averse as they can because they
don't want to watch
you know a lot of their savings go up
and then come straight back down
so what they want to do is be more risk
averse if you're younger
perhaps you could be riskier i prefer to
be more risk-averse
just because i've lived through
crypto bear markets and i can tell you
it's not fun
it's not fun if you're on the wrong side
of that and
and so i prefer to be more risk-averse
and there's times like this
the last few months where holding a
majority of bitcoin
was the right thing to do in hindsight
i mean of course ethereum has had a
better year overall
but there's certainly phases of it where
bitcoin outperforms and whenever bitcoin
gives the site slight hint that it's
going to drop
ether drops more i'm a big proponent of
ethereum i love holding ethereum
i expect to have higher returns from
ethereum but i'm paying for it with
higher levels of risk or volatility
so you're probably wondering what if i
throw risk out the window you're also
probably wondering why has been putting
an emoji
in his in his presentation well um
i don't really have a good answer for
that so the question then
becomes well what if we pick a portfolio
above this say this this line through it
right here so it was a circle it's not
quite showing up
but what if we pick a portfolio all the
way over here
at the very top meaning maybe our
expected return is higher
but we're paying for it with a lot more
risk so in this scenario
maybe your expected return is around
let's say a hundred and twenty percent
volatility is at 105 so
to within one standard deviation or 68
percent
your expected return might be 120
plus or minus 105. so all the way down
to 15
at the bottom or 100 or um 235
at the top so theoretically a higher
expected return
you're taking a lot more risk on and
it's possible you
you end up seeing a lower risk or a
lower return again it's not saying that
your your return at the
at the least will be 15 it's just saying
that to within one standard deviation or
a 68
probability that that is where your
return would be
of course there's going to be some years
where you would experience a loss
that's that's obvious okay now
you also might be wondering well what if
i want
less risk but i want to take on more
risk
than what maximizes the sharpe ratio
because this is what maximizes the
sharpe ratio
this would be the the least risky
portfolio in terms of maximizing your
risk adjusted returns
so what if you go somewhere in this
ballpark and you say you want to take on
eighty percent volatility in that
scenario
the portfolio which maximizes your
sharpe ratio
on the efficient frontier would actually
be 35
bitcoin 65 ethereum so
theoretically you would expect a higher
return you're paying for it with more
units of risk
okay if you if you're trying to figure
out ways to get higher returns
usually there's going to be some higher
level of risk associated with it
and you can see that in the volatility
so what if you are
very inefficient with your portfolio and
you just said you know what i want to be
on the inefficient frontier i can't
explain why someone would want to be
because you're taking on the same level
of risk for a theoretically lower
expected return
but again you do you for instance let's
say you wanted to be all the way down
here
it would imply 90 bitcoin 10 ethereum
so the reason why this gives you a lower
sharp ratio
is because you're not really holding a
lot of ethereum and ethereum tends to
outperform bitcoin
it does it in a manner that is more
risky because the volatility is higher
to the upside and the downside
but there's a certain level where it
balances out and it maximizes your shop
ratio and it's over here
if you're going to be all the way down
here at the same risk level more or less
but have a lower expected return then in
my opinion right you're doing something
wrong and the best part about it is it's
not even my opinion it's what the data
says
and that's that's what we want to focus
on you know i get a lot of people that
like to criticize
some of the stuff i present whether it
be diminishing returns
that type of stuff and and my general
response to all this
is it's not like this is just what i
feel is going to happen based on my
own emotions that morning it's just what
the data suggests and that's what i like
to stick to
just stick to the data if it turns out
that something drastically different
happens then so be it
but it doesn't change the fact that i'm
going to stick to the data
and go with the data as long as i can
and then just stick with that
i think it tends to work out better than
than just you know
going off whatever however you feel that
day
so what if we had a third coin okay
this is two coins when you have two
coins you just get a pretty simple line
what if you had a third coin ah
looks different now so this
you can clearly see this is your
efficient frontier okay
all the way up here below this point
i would call it your inefficient
frontier because you know let's say
you're
you pick a portfolio which lines up on
this level
and it gives you an expected return of
seventy percent with eighty percent
volatility
that means your expected return could be
as low as negative ten percent
and that would have a sixty eight
percent probability i mean it wouldn't
be it would be negative ten percent all
the way up to maybe like 150
or so but there would be a 68
probability that that would be your
return
um and so when you add a third coin
it changes the game right it creates
this um
a different a different type of map here
it's not just a line over here
you get all these different portfolios
this is a hundred thousand portfolios
a hundred a hundred thousand different
portfolio weightings
we simulated in python got the results
put them here for you guys to see
this is what pisses people off if you
add litecoin
zero percent well why is it zero percent
does it mean that litecoin can't go up
no it does not mean that litecoin can't
go up if bitcoin trends up litecoin will
trend up too
i actually just picked up some litecoin
a couple weeks ago because as i've said
before
when bitcoin gets to the prior all-time
high litecoin
does tend to do well so in that scenario
there's there's different ways you can
look at it right if if you want to try
to make key moves based on historical
patterns
you can do that i did pick up a little
bit of litecoin however
as i've said before there's a time to
hold litecoin and there's a time not to
and then like 90 over 90 of the time i
think it's not too
based on historical returns and
historical volatility
you can see the data doesn't lie
it suggests to maximize your sharpe
ratio it's the same thing as if you just
were choosing from bitcoin and ethereum
74.4 bitcoin 25.6
ethereum 0.0 percent litecoin
now this is subject to change i've run
this analysis in the past and there's
been phases where it might go up to
you know a couple of percentage points
or something
but generally speaking it tends to be
around
zero and the reason again is not because
it can't go up
it's just that the downside risk in
terms of its historical returns and
historical volatility
does not justify the upside potential
that's all it means
you also need to think of this in terms
of the opportunity cost
right if you're putting a dollar into
litecoin that's a dollar
not going into bitcoin where that's a
dollar not going into ethereum
so it's not so so essentially the
argument is that
adding litecoin to your portfolio does
not improve
your covariance matrix enough to justify
the downside risk associated with it
that's all it means
again if you don't like it take it up
with the data and
and if the price starts performing
better and there's lower volatility and
higher returns
then it'll start showing up right that's
then it'll start showing up but again
based on data from 2015 mixed in with
bitcoin and ethereum data from 2015
it shows that bitcoin and ethereum
yields the higher
sharpe ratio but as we said before if
you wanted to take on more risk
and come up here there probably are some
portfolios that have a little bit of
litecoin
as i said before i just picked up a
little bit of litecoin not that long ago
sometimes based on other factors like
where bitcoin is within the market cycle
maybe it's okay to justify taking on a
little bit more risk
here on the efficient frontier to you
taking on the you're taking on more risk
as you go up the volatility
axis but you're also going up the
expected return access as well so you're
saying okay
i'm going to take on a little bit more
risk hopefully it comes with a higher
return
i get it i'm out back out of it right
that's the idea
so hopefully this has been useful we
talk about modern portfolio theory on
the public channel occasionally
but we definitely talk about it on the
premium list
we've had a few weekly reports on it
i'll probably try to jump more into it
here over the next few weeks and months
as people really try to get gear up
their uh portfolios for the
you know for the bull market if if we
get one or a sustained one
again is it possible that the bull
market is just 20 21
one and done is possible do i think it's
likely
no i don't um and so i think it is
important to think about these things
because
it could i mean it could potentially be
uh make a huge difference in a few years
small
portfolio tweaks can make huge
differences
i mean absolutely enormous differences
later on
so if you guys like the content
subscribe
let's go for 80 000 subscribers we like
to present information here that you
probably won't find elsewhere
we also do have the premium list the
holiday sale make sure you check that
out before the prices go up
uh they'll probably go up early january
i'll try to get you guys a specific date
but they're gonna go up soon make sure
you sign up it's not gonna last forever
and um you get access to weekly reports
weekly videos the telegram alerts
channel the telegram chat room
the risk dashboard the trade view
indicators next year we're going to
start doing premium
list only live streams and a few other
things that we have planned so make sure
you guys check it out
uh and sign up before the prices go up
hope you guys enjoyed the analysis
subscribe give the video a thumbs up
turn on notifications
so you'll see future videos and i'll see
you next time
bye

# Gold Price Prediction using Logarithmic Regression

**Fuente (VÍDEO):** cowen · YouTube — https://www.youtube.com/watch?v=xJC-PRtoRXo
**Publicado:** 20200626 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20200626-gold-price-prediction-using-logarithmic-regression.md]`.

---

hey everyone and thanks for jumping back
into the precious metal verse today
we're gonna be talking about gold if you
guys liked the content please go ahead
and subscribe to the channel turn your
notifications on and like the video
while we normally jump into the crypto
verse and talk about crypto currencies
we're going to be providing some of our
data science models to other asset
classes as we've talked about and today
we're looking at precious metals notably
gold is what we're looking at so go
ahead and subscribe also check out the
telegram channel here you can find a
link to that in the description below as
well as the premium list if you want
access to exclusive content so let's
just go ahead and dive in so what we
have here is the price of gold which is
the white line and then the Green Line
is our logarithmic fit so first of all
look at the y axis the y axis is on a
logarithmic scale so it's going up 10 X
10 X + 10 X so each move from major tick
to major tick is a 10x increase this is
so we can capture you know the moves of
gold over a long period of time so that
you can you can see you know the what
it's doing over say a decade otherwise
anything that was going on in this
portion over here would be completely
dwarfed by the prices today this is why
we use a logarithmic scale so the idea
is can we can we identify you know a
fair value of gold and the way we did it
with the total cryptocurrency market cap
and the way we were applying the same
methodology here is we just took the the
percent difference between the price and
the regression the the logarithmic
difference between those those two and
minimize the sum over the entire price
history and when you do that and you fit
it to the equation 10 raised to the
power a times L of X minus B where X is
time and a and B are fitted coefficients
then this is the equation you get this
green line that you see here and the
idea of the Green Line is to provide
what so you know what is the quote
unquote fair value of gold
obviously it's somewhat you know it's
it's you know somewhat arbitrary I agree
but let's just let's just run with this
and say okay this is our fair valuation
price of gold if we're above it then we
tend to be in our you know our
overvalued territory when we're below it
we tend to be in our undervalued
territory right now you can see we're
basically on the line where it were just
slightly above the line now we've also
talked about that it's you know it's
good to add a general tolerance bandera
just because of small price fluctuations
on any on you know in any given year or
so could really impact it especially you
know some of the ones early on so we did
was we we just gave it our you know our
our tolerance band innocence to say okay
well in this band you know if it's above
it or overvalued if it's below it we're
undervalued and if we're in the middle
of the band and we could say we're
pretty much at our fair fair value price
of gold so our current fair value
according to this model is around $1400
now what if we were to look at you know
what if we take the percent difference
between the price and the regression
line so this is this is so we can
identify you know how it moves with
respect to the regression line this is
what you go now we have a data point for
every every single year or every single
month of every single year I should say
but note that on this chart we're
missing negative values and the reason
we're gonna fix that the minute the
reason is because we're looking at it on
a logarithmic scale and it only plots
positive values on a logarithmic scale
unless you you know unless you go in and
hack hack the code and and present it in
a different type of way then this is
what you get and we are gonna present it
in a different way in a minute so first
of all you can see we had a peak here
another peak and then the third peak so
you I mean you can see each of these
three triangles that form from 19 you
know the early 1970s out to 1990 and
then currently we are in the phase you
know starting a little bit before 2010
you can see the first triangle formed
and the idea is well what if we are
going to repeat what happened last time
remember these data points are not
prices they represent the percent
difference between price and the
regression line but remember the
regression line is monotonically
increasing
so it never goes down so over time you
know the price as long as it's you know
I mean even if it's even if the percent
difference between the price and the
regression line is not as much here as
it was say here because the regression
line is continuing to increase
monotonically then the price would still
be going up so here's our you know this
is our general our you know our three
triangles here this is just a basic
trend line that I drew connecting from
peak to peak and identifying that you
know maybe maybe we come back up to this
point which would be you know I mean
currently the value 8 that the
evaluation shows that we're a little bit
more than 20% overvalued in terms of our
our fair valuation
but that hasn't stopped us before from
going to an over valuation of you know
three hundred and fifty percent so you
have to take this into consideration
another thing is let's plot the negative
values so these are the negative so this
shows when when we're actually below the
band so the red data points and it's
interesting that if you just you know
you you can extend this out and
basically connecting I just drew up I
drew a pair a line from here to here and
then just do another parallel one
connecting this point here you can see
our you know our when we're undervalued
we don't really form that same type of
pattern it tends to be more of an you
know a concave down pattern so this one
you saw this small one over here we had
a larger concave down pattern from 19
you know the early nineteen hundred's al
to 2010 and now maybe we are interested
entering another you know another
long-term bull market
it's obviously unclear yet but with the
you know with the current economic
climate gold does tend to do well
especially when there's a lot of
uncertainty in traditional markets so it
would not surprise me if if it continued
to do well so let's plot it a little bit
more intuitively so here we're just
showing that if it's if it's a hunt if
it's at a hundred percent then this is
our fair valuation line if it's below a
hundred let's say it says so 40 percent
or 50 percent then it's that means it's
undervalued so this would be you know 50
or 60 percent
undervalued in the early 2000s and you
can see that you know since 2015 till
2019 or so we were at our fair valuation
line only recently going above our fair
valuation line so if you're not familiar
with this I just want to remind you that
this is the cryptocurrency market cap
regression line our fair valuation line
and I'm showing this so we can relate it
back to gold you can see we we draw
these bands up here to identify
speculative bubble Peaks and then the
lower band down here is to identify you
know our hopefully our absolute bottoms
which typically is around negative 40%
for the total cryptocurrency market cap
and if you draw the percent difference
between the price and the regression
line you see this trend line here where
you know each peak while it you know the
price is continuing to go up
but the volatility from the regression
line continues to get to get the
volatility continues to go down and this
is just a sign of the market maturing
and becoming more efficient so here you
can you can compare this peak here to
being overvalued here this peak to this
peak and then this peak to this peak so
currently we're around a thousand
percent overvalued if you want to see
more on the crypto stuff then I would
encourage you to subscribe to my channel
because we talked about crypto a lot on
my channel so going back to gold this is
our our percent valuation here and I
just drew you know a general trend line
from from this peak to this peak we
don't really have I mean because gold
tends to move a lot slower than the
cryptocurrency market we don't have a
ton of useful information in terms of
say drawing macroscopic moves like this
where we're drawing it from the
regression line to the price but you
know if we were to come back up to the
top here then this could correspond to
an over valuation of you know a
significant over valuation I mean this
is a hundred percent over valuation here
so it could correspond to getting up to
around the three hundred and fifty
percent over valuation again now bear
with me here because we're gonna go
through through a few different charts
so the first one is is we're just gonna
draw a trendline and I'm not a huge fan
of imaginary lines but I do find myself
tending to draw them
cuz I think they I think it's
interesting to look at macroscopic views
with them more the you know the smaller
timeframes I don't think they're as
useful but you know when we're looking
at longer time frames I do think they
can can provide some useful insights so
first we're gonna draw a trend line from
the lower the lower price down here so
you can't really see it because it's
masked by the it's masked by the
logarithmic regression line but if you
look here you can see we're drawing it
from our price the the price here
connecting it up to this peak over here
and the bottom we're drawing a parallel
line to this line you can see it's
connecting here so when we break below
and then it also connects up here at the
peak so this is the first one the second
one is drawing the peak here down
basically this channel that we were in
for you know a couple decades or so the
third one is drawing bottom to bottom to
then support the bottom support here and
then the last one is just drawing peak
to peak if we put all these together
this is what it looks like and because
it's kind of hard for me to I you know
with with all the dashes if it can be a
little bit hard to look at so I changed
it to just straight lines but typically
when I'm drawing things that are not
concrete and they're more you know a a
speculation I usually draw it as a
dashed line so here we are try to stare
at this chart for a minute without you
know just to try to get an idea of
what's going on but a slightly bullish
scenario for gold so if we were slightly
bullish maybe we would come back up to
the top of the purple band in the early
2020s so if we were to do that you can
see that it would put us at a price just
north of $2000 because this data point
or this line here corresponds to 2000
and we would be scoring slightly above
that and then that would be kind of
keeping in line with the peak here to
the peak here and then maybe drawing
another peak here and then maybe we
would return back down to our regression
line an even more bullish case that
we'll talk about again in another video
we'll look at trading view in another
video so again subscribe to the
if you if you want to follow along would
be moving up over the next say six or
seven years so the red line window so
you know you can see we were in this red
line down here again right here a third
time here maybe we come back up oh I
don't think you know I I think the
chances that we come all the way back up
here and in only six years are fairly
low but again you know the move that
took us from 2000 to 2010 was you know I
think you I mean it was it was a fairly
significant move like a six hundred
percent move and I mean you can see we
went from around you know $200 to over
over a thousand dollars during that
decade or you know Ron that decade or so
so don't discount the fact that that
could happen maybe we don't make it into
the band maybe it acts as resistance and
we come and we come back down to our
regression line later on but I I think
it's interesting to to you know to
overlay all these different trend lines
to try to get an idea of where the price
might you know may be going obviously
are more you know are more neutral
stance in terms of saying we're not
going to go up or down
would just be to say okay well maybe
we'll just continue chugging along in
our regression band which remember
currently were slightly above so maybe
we'll stay within the band for a few
more years or maybe we come back up to
you know this longer-term
purple trend line that connects this
peak to this peak so basically just
connecting peak to peak and then maybe
projecting that this could be the next
peak I know this would correspond to
just over two thousand dollars
so this is our slightly bullish case and
then remember our more bullish case so
you know the stars the line for gold and
and maybe maybe you know there's a lot
of uncertainty in the markets and
traditional markets for you know several
years and then people hedge their bets
on gold if that were the case then you
know maybe maybe we are able to revisit
our red line here in terms of sale
resistance so later on and if that were
the case you know this would correspond
to around say $6,000 per I'm free for
gold
so $6,000 I know it seems like a lot but
again it's actually fairly akin to the
move we saw from you know the early
2000s to approximately ten years later
so this is this is the point of the
video I want to show you guys I hope you
guys enjoyed the content I do try to
focus on creating graphs that you won't
find other places so that I can provide
something unique if you guys like the
content you want to see more of it you
want to see this applied to other asset
classes go ahead and subscribe to the
channel give the video a thumbs up let
me know what you think about it in the
comment section below and remember I
will provide some of these graphs if you
want to download them on my telegram
channel which you can find a link to in
the description below and if you want
access to a weekly newsletter a weekly
premium video and a Google sheets
dashboard with access to you know
information on crypto currencies
primarily right now we're going to be
expanding that all you know we've
started to expand it to other asset
classes so if you want to if you want to
check that out go to my website it into
the crypt offers.com I hope you guys
enjoyed the show and again subscribe and
I'll see you guys next time bye

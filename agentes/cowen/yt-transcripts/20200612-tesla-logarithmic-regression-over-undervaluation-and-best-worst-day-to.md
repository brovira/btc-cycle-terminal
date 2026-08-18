# Tesla: Logarithmic Regression, Over/Undervaluation, and Best/Worst Day to Buy

**Fuente (VÍDEO):** cowen · YouTube — https://www.youtube.com/watch?v=T57UMV56jdY
**Publicado:** 20200612 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20200612-tesla-logarithmic-regression-over-undervaluation-and-best-worst-day-to.md]`.

---

Hey everyone, and thanks for jumping
back into the
Wait, this isn't the cryptoverse. Today,
we're going to talk about Tesla. So, if
you guys like the content, please go
ahead and subscribe to the channel.
Would love to have you join. Uh we
typically talk about cryptocurrency like
Bitcoin and Ethereum using more of a
data science approach than you'll find
most other places. Uh but today we're
going to talk about Tesla. We're going
to be looking at logarithmic regression
and under and overvaluation of of the
Tesla stock. Um in addition to that,
we're going to be looking at various
uh you know, comparisons of price with
respect to say volume and percentage
changes of volume. And then finally,
we're going to look at, you know,
statistically speaking, is there a
better day to buy Tesla?
And is there in general a a worse day to
buy Tesla? So, we're just going to use
all sorts of uh models that that I've
developed, and we're going to just going
to go systematically through this. So,
again, please subscribe to the channel.
Would love to have you join. I'm going
to try to expand this from from just
looking at cryptocurrency into some uh
other stocks because or you know, or
stocks in general, precious metals, uh
commodities. I think it's important that
that people are are diversified. Um and
so, you know, we can mark this as as
near the beginning. We have done some
videos before, but this is one of the
first one of the first videos that we've
done um that we veer away from
cryptocurrency. So, check out the
Telegram channel if you guys want to
discuss this stuff and also the premium
list here if you if you want more
content. So, the first thing we have
here is just the logarithmic regression
um fit that I've done to the Tesla
price. So, we have daily price data
for Tesla going back to 2010.
And then our red line is our our you
know, our fair value regression fit. So,
you can think of this is, you know, if
it's if it's under it,
you you might say, "Okay, well, it's
it's undervalued." Or sorry, yeah, yeah,
it's undervalued. If it's over it,
overvalued. Um so, in a sense here we
were we were at our undervaluation
point. Here again,
we were overvalued in 2014 and 2015, and
now we're approaching that same
overvaluation point
um this year potentially. So, we would
only need to go up another few hundred
dollars to reach this um overvaluation
line. Uh the orange line you hear that
you see here is just the quarterly
revenue.
Now, I'm not plotting anything against
it. It's just it's overlaid on the
secondary Y axis so that you can see how
the price moves when the revenue moves.
Here's an example where the revenue
started to rapidly go up, and it was a
leading indicator before the price
really started to move up. Um
over here this is a it wasn't really the
case, but again we we were at that
undervaluation line, and this is
ultimately where we bounced off of. We
came back up almost to a thousand, back
down to being undervalued, and then and
then straight back up. So, in a sense if
you wanted to use this to try to time I
mean this is not financial advice by any
means, but if you wanted to try to you
know time your entry into the market, it
might be useful to say look at at what
number in our undervaluation phase or
our overvaluation phase. Or if you are
deciding to buy at this point, to just
know that based on historical data we
might be capped up in this region in the
short term. But again, the regression
equation is monotonically increasing, so
uh more than likely time is going to be
on our side. I I continue you know I
suspect that that Tesla will continue to
go up in price
um
over the next several years assuming I
mean this of course is assuming um
we don't just have a complete global
meltdown.
Uh but despite Elon Musk saying that
it's it's um overvalued, uh we've
continued to move on up. Now, one of the
things I want to I want you to note is
this red line here is our fair valuation
line. So, the idea is well, can we look
at say the percent difference between
the price and the fair valuation line?
And that's this line. So, at 100% this
means we're at our perfect our fair
valuation.
When we're down here, you know, around
say -50% or so, this tends to be the
local bottom. So, if you see us coming
back down to this region, uh it could
present a timely opportunity.
Um despite the fact that we've been
moving up significantly, we're only
about uh we're we're basically at 150%
uh
over. So, if well, I guess if you think
about it is if 100% is is our fair
valuation, then we're only, you know,
we're only about 50% above that. Uh but
note that last time we we really shot
shot up over back in in say 2014-2015,
we went up all the way to, you know,
250%
or so. So, there there still could be a
significant room to move up. Um I know a
lot of people are are very wary with the
economy and and where it may be headed,
but again, I don't think if you think of
it just say like it's Brownian motion in
a sense or a random walk, I don't really
necessarily think that anyone is capable
of predicting short-term price movements
consistently, and if they are, uh
they're probably not advertising it to
the world anyways. Um on this channel we
tend to look at macro level moves and
and to, you know, time key momentum
shifts in the market.
Um and we actually even made a video on
Tesla over here uh when it had come back
down to being undervalued.
Um if you go back and look a few months
ago.
So, this chart here shows our volume
differential versus the daily percentage
price change. So, I know that might be
kind of confusing, but it's just looking
at the difference in volume from day to
day, and then the percentage change of
price from day to day. So, each point
represents a day and they're color-coded
based on time. So, we're going from 2010
to 2020. So, I think it's interesting,
you know, you it makes sense. It makes
intuitive sense when you're seeing daily
percentage change changes that are
significant like 15, 20%. They're
basically always accompanied by a
commensurate increase in in volume.
Um the same thing when we see a negative
price movement. Uh it's also accompanied
by uh you know, a commensurate
um change in the daily volume.
But, of course, looking at just the
absolute value of the volume uh maybe
not doesn't make a whole lot of sense
because as, you know, as, you know, as
the price grows, there's going to be
more and more volume. Let's look at the
daily volume percentage change. This is
what it looks like. Uh but, the
unfortunate consequence of doing this is
that you get a few points up here that
are um that, you know, basically make it
hard to understand really what's going
on in this region.
Uh so, what we'll have to do is we take
the the
log we we plot this on a logarithmic
scale. So, we're looking at 10x, 10x,
10x, 10x. And we're just plotting the
absolute value of it. So, you can see
the kind of this triangle uh that it
forms. Um and ultimately speaking, you
know, when when you're seeing these uh
the the percent moves, you can see as we
as we go up. So, if as you go up from
say um 0 to 5 to 10 to 15 to 20,
you you see you have to see
um commensurate increases in volume.
Otherwise, you know, if you didn't and
you might just see a rectangle where it
just doesn't really matter. But, you can
see that as we as the price moves up on
a single day
or down on a single day, the volume is
also moving with it. So, if you see the
volume of of Tesla really moving uh one
day, then um you know, it's it's it's
it's more likely to be associated with a
significant price move. I mean, this is
not
um any any crazy insight. I mean, anyone
anyone knows that um price moves are
associated with um volume changes, but
I just thought it'd be kind of
interesting to visualize it.
Um this plot shows the price of Tesla
versus the daily volume. So, I thought
it was interesting because if you if you
kind of plot the trend line here, um you
can kind of see some zigzag patterns uh
basically on the move up, then you can
kind of see these lines that form. But,
if we were to stay within this uh you
know, this projection here,
10 to the 6th is an is a daily volume of
a million, so this would be 10 million,
100 million, maybe 2 300 million. And,
you know, if you see the daily volume
getting that high, then it could, you
know, it very well could get us to say
another 10x from here in terms of the
price. Talking about $10,000. Um but,
even just say getting to 100 million
might be what we need in order for the
price to reach say 3 or 4,000 dollars.
Um so, I think this is a pretty
interesting chart to to look at as well.
Now, this is great and all, right? We we
like looking at all these models, but is
there anything we can, you know, squeeze
out of this information and essentially,
you know, take it to the bank where we
can we can plan our moves in a way that
can um benefit us over the macro scale.
Um before we continue, I'll just remind
you to please subscribe to the channel
if you guys like the content. Uh we we
typically talk about cryptocurrency, but
we are going to be expanding the channel
to talk about other things like um
uh stocks, precious metals. If you guys
have any recommendations to what this
channel what you would like to see
covered, then leave it leave a note down
in the description or in the comments
section below. Um and definitely
subscribe so so we can continue to to
stay up-to-date. Um so, the question is
what is the best day to buy Tesla? So,
is there statistically speaking, can we
look back and see have you been buying
on a certain day, would you have been
better off than buying on, say, a
different day?
And the way we're just going to look at
it, uh it's it's pretty simple. It's uh
completely simplifying it to some
degree. I could certainly go into a lot
more detail, and I probably will in
future videos. But, let's just keep
this, you know, this one of the first
videos just super simple, so that I
think it's easy easy to follow along.
So, we're basically looking We're first
looking at 2010. If you break it down by
day of the week, what is the average
percent move? Okay, so this is a
percentage.
Um what is the average percent move from
open to close that day? Okay?
So, in 2010, the average percent move
on, say, a Monday was -0.25%.
On Tuesday, it was 0.4. Wednesday, 0.75.
And then Thursday and Friday, it was
negative. Um so, during this first year,
on average, you would have seen, you
know, had you been buying uh first thing
on Tuesday, then on average, the price
by closing time
would have been approximately 0.4%
higher. And on on Wednesdays, uh
0.75% higher. So, you could argue maybe
that Tuesday morning could have been a
decent time to buy or Monday at close.
And then um and then, you know,
Wednesday at close would essentially uh
mark a potential short-term move to the
downside, on average, of course.
If you look locally, you're you're going
to find times where the complete
opposite happens. Um this is just on
average. We're not even showing, say,
standard deviations or, you know, like
an error bar. We're just taking the the
pure numbers, um averaging them out, and
seeing what we get.
So, in 2011, uh this is what we had. Uh
I'm not going to go through every single
year. We're going to just get a general
synopsis of it. Um but, you can see we
more or less uh are fluctuating between
like -1 to 1.
Um,
and what you notice is as we, you know,
as we continue to march on, there's more
and more days where on average they're
positive,
um, especially as we get into these
later years. Now, is there anything we
can take from this
uh that can that can help us? Like, is
there any is there is there a way to
deduce, well, if this is negative and
negative and positive and positive?
Well, what's something we can we can
look at? Well, one of the things we can
look at is,
um,
Ferrocious highlighting what is, you
know, where where do where do we tend to
be positive? You can see that in the
last few years, the beginning of the
week,
um, tends to be a better time to to
purchase Tesla
uh than the end of the week. Because if
you're say purchasing it on Fridays, I
mean, Fridays is by far the worst day to
uh one of the worst days to to buy
Tesla, because you can see that on
average, most of the years, if you had
purchased it at open, then by close,
close of business, um, you would have
actually been sitting at a loss already.
And, you know, there's it's certainly
not a great feeling when you put money
into the market and then a few hours
later you're already, you know, you're
you already see a loss. I mean, no one
wants to see that. Um, but on average,
doing, you know, investing on say Monday
or Tuesday,
tends to be a lot better.
Now,
if we count them, so what are the best
and worst days if you count them by
year? So, out of the 11 years we have,
so 2010 to 2020,
the number, you know, the number of
years where Monday was the best day to
buy on average was four. And Tuesday was
four. So, eight out of the 11 years, the
best times to buy would have been Monday
or Tuesday. Um, Wednesday only coming in
at two, Thursday one, and Friday zero.
So, there was not a single year where
statistically speaking, um looking at,
you know, averaging it out over every
single uh day of the week over that
year, uh Friday was never the best day
to buy at open. Um
Now, what is the worst day? You can see
that Monday and Tuesday and Wednesday
all had a single year where they would
have been the worst day.
But Thursday and Friday were the worst
days eight of the 11 years. So, in terms
of buying Tesla at open, Monday and
Tuesday would have been your best bet
over the over the last 11 years, and
Thursday and Friday would have been your
your worst performers.
Um
so, I hope that makes sense. I I hope
I've explained that uh well enough uh
that it's it's useful. We know that, you
know, past results obviously don't care
guarantee anything uh regarding the
future.
Um but, you know, regardless, it's still
interesting to to look at this data,
and, you know, I can package the data
for you. It's, you know, I'm the data
messenger in a sense, and then you can
do whatever you wish with it. Maybe you
think, "Oh, well, since this has been
the trend so far, I'll take the, you
know, the contrarian view." Or or
something like that. Um so, you know,
there there's certainly a lot of
different ways you can look at the data,
um but ultimately speaking, I I I think
providing this type of data is useful.
Um and and if you, you know, if you
stick with it over the macro scale and
you're not a day trader, then I think it
really could it could benefit you.
So, just going back to the beginning,
remember this is our regression equation
uh looking at undervaluation versus
overvaluation in terms of, say, getting
to this overvaluation line,
uh we still have uh a ways to go, and it
might put us at around, say, uh $1,400,
$1,500 by the time we get there.
Um but I I I do think that that, you
know, we certainly can make it there.
Uh and again, if if stocks if stocks
really start to uh take a downturn later
this year, then obviously Tesla will
most likely be affected. Um but I hope
you guys enjoyed the content. Uh let me
know what you guys think about uh
covering other things on the channel
uh besides just cryptocurrency. If you
guys like the idea of of a more
diversified approach, which I think is
ultimately smart.
One of the reasons why I'm doing this is
in preparation for the fact that if, you
know, if if you are able to make a lot
of money in cryptocurrency over the next
several years during a potential uh bull
market, if we if we think that LinkedIn
cycle theory is true, then at some point
there's going to be come a there's going
to come a time where you're going to
want to, you know, withdraw money from
the crypto market and diversify it
elsewhere. And by learning about this
stuff now, if you're not already, you
know, informed of it, then when the time
that by the time that happens, you'll be
ready to go. You'll know, "Okay, the
money's coming out of crypto. I'm
putting it into into other markets." Um
I would recommend, you know, I mean, for
me personally, I'm investing in in a lot
of, you know, a lot of different
markets, not just crypto by any means.
Um but I do know a lot of people who
watch the channel are are mainly focused
on crypto. But again, I think it's
important to uh to diversify if you can
and uh reduce your overall risk in
exposure of a single market. It's It's a
lot better to, you know, to offset that
risk by looking at at several different
markets. Um so that if one market goes
down, like if you see a 10% drop in
crypto in a day, then maybe you're not
seeing an entire 10% drop in your, you
know, your overall net worth because
hopefully you don't have 100% of your
net worth
invested in crypto.
Um so I hope you guys like the content.
Again, if you do, please subscribe to
the channel, turn the notifications on,
like the video, um leave a comment down
below with what you think. If you want
to discuss the charts, maybe I'll post a
couple of them in my Telegram channel.
You can see it here and you can find a
link to it in the description below. And
if you want access to premium content
with this graph updated fairly often,
then check out my website at
intothecryptoverse.com.
I hope you guys enjoyed the content. I
will see you guys next time. Bye.

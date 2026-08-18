# Cryptocurrency Portfolio: An example of setting up logarithmic weights

**Fuente (VÍDEO):** cowen · YouTube — https://www.youtube.com/watch?v=PEQ-kDBvTkU
**Publicado:** 20191203 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20191203-cryptocurrency-portfolio-an-example-of-setting-up-logarithmic-weights.md]`.

---

hey guys thanks for coming back into the
cliff divers today we're gonna be going
over waiting your portfolio well we're
actually gonna show you exactly how I
did it and I'm gonna do it using
Microsoft Excel I thought about just
learning you like I throwing you guys
the Python script or you know maybe
making like a C++ correct or something
like that but I think most people the
majority of people are gonna know how to
use Excel and so we're just gonna show
you guys how to do that now if you guys
like this content please subscribe to
the channel and turn notifications on so
you know I made a couple videos in the
past that talked about waiting your
portfolio and just to recap if you had
put in say $1,000 into the top ten
crypto currencies on November 15th 2015
so about it about four years ago you
would have allocated them like this and
you're peaking around 92 thousand
dollars back in early 2018
now if you had waited them by the
square-root of market cap you would have
seen a much better return two hundred
thirty seven thousand dollars of the
peak now this back to the question well
what what power could we raise it to
which would have optimized our our ROI
and it turns out it would have been
point zero nine nine six or nine which
would have allocated it like this and
your peak would have been at three
hundred and thirty five thousand dollars
so still about a hundred thousand
dollars was better than waiting it by
the square-root now if you notice this
looks very similar to a hundred dollars
a coin so if you did a hundred dollars a
coin you would have seen a very similar
ROI and you would have maxed out at
around three hundred and thirty thousand
well it turns out that weighting it by
the logarithm of the market cap which is
not raising it to a power like you're
seeing over here but if you weight it by
the logarithm mobile market cap then
your ROI will actually live on would
have been around three hundred and
thirty eight thousand dollars so it'd
have been a little bit higher and you
know I showed that later in a different
video I'm just scrolling through these
because we've already covered these in
other videos you guys can go look at
them I'll link them at the end of the
video but let's just go go to where I
show waiting it by say the top ten coin
so this is just waiting it by market cap
top coin top two three four five you can
see there's no a huge
because most of it is going to Bitcoin
if you waited by the logarithm of the
market cow this is just if you just had
that coin here is if you allocate at the
top to the top three four you can see
with four I included it would have
included aetherium so your return would
have been really high and in fact let me
see so this would have been two hundred
three hundred four hundred actually it
would have been maybe over five hundred
grand
so actually would have been quite quite
good if you had just done it in the top
four and then you can see as you start
to include more and more coins it
actually reduces down because you're
allocating less to etherium likes to add
less to XRP which take quite well now I
should mention that this you know in
2015 November we were in a bull run we
were at the beginning of the bull run
Bitcoin was you know I don't remember if
it was holding a 20-week moving average
or it was about to but we were at the
beginning of a bull run now in a bear
market
it's obviously historically it's been
better it's a whole Bitcoin a majority
of your holdings in Bitcoin so where we
currently are is where you know we're
not holding the 20 week moving averages
support for Bitcoin so I don't think
it's fair to say that Bitcoin is in a
full swing bull market but at the same
time you know we're much higher than
where we were about a year ago or around
you know bitcoins around 2x where it was
or more so I don't really necessarily
think we're you know just in a an
extended bear market either but it is
possible we might see a lower low so um
assuming that risk assuming that we may
or may not be in the bull market or we
may or may not be in a bear market if
you if you wanted to start weighting
your portfolio using these types of
methods then how do you do it so a lot
of you guys are probably like oh my gosh
this is simple and you just you know
it's obviously you can take the
logarithmic of the market cap but for
those who don't I'm going to show you
and if you are still confused and you
can join my telegram channel or
discordant Channel and I will just I
will give you an Excel spreadsheet that
you can usually use yourself also I
wanted to tell you guys I am
in the description below I will set up a
place where you guys can tip me if you
if you want to obviously don't feel
compelled to if you're a college student
I would urge you not to I've been in
that position before but some people
have asked have been asking and that is
one way you guys can support what I'm
doing and maybe I can take that money
and go buy an actual microphone so you
guys don't have to listen to this audio
all the time now let me just show you so
I you know I debated say giving you guys
the Python code or some C++ code and the
more I thought about it I just thought
you know most people aren't gonna know
how to run this or they're not gonna
know how to compile it or whatever it
might be but I was like okay most people
know how to open an Excel spreadsheet or
how to work an Excel spreadsheet because
you would've learned it at some point in
middle school or high school or college
so for that reason I will just show you
an excel it's super simple so you would
just first get the coins you want to
invest in and put them in the first
column so here this is the top ten not a
not including tether now if you if there
say there's a specific coin that you
don't like over here and you think it
would be preposterous that you would
ever invest in that that's fine I'm I'm
not invested in all these coins on
invested in some of them but if you if
you did just want to weight it by the
top ten this is what you would do and
then if you wanted to say include a
different coin or different coins you
would just add in what they are and then
their market cap so let's take the
logarithmic of that market cap so you're
just gonna go in you can type in the
logarithmic logarithm of the market cap
and then you're gonna see what it gives
you it looks like that so it should not
be showing dollar signs because we're
currently just we're currently just
trying to trying to get our weights here
so the way we do that is we need to take
this number and then divide it by the
sum of the logarithmic or the logarithm
log of each coin their market cap so
what we're gonna do is we're gonna go
over here and we're gonna just say
equals and we're gonna go to see two
so we're gonna put dollar signs so we
can scroll it down and then we're gonna
go by the sum of c2 to say c11 okay so
sorry I'm I'm currently not working on a
desk right now so it's kind of hard to
type on this thing right so we're gonna
divide it by that and then we're gonna
scroll this down and you should not have
dollar signs next to them we're just
getting our wait so we're gonna go to
number we're gonna increase the
precision so you can see what they come
out to be and it's wrong because this
one should not have a dollar sign right
here and what we're gonna scroll that
down okay so this this is what it should
be so this this is still not right
because I need to fix here okay so here
we have the weights by market cap or by
the logarithmic of the market cap we
need to make sure that this adds to one
so we're gonna sum it up so one let's
see if it adds to one it does add to one
it needs to add to one if you're not
getting it to add to line then you've
done something wrong now our investment
let's say it's one thousand dollars and
we're just gonna come over here and
we're gonna multiply a thousand dollars
by the weight and that's what we go and
then we are going to put our dollar
signs so that it doesn't change and then
we're gonna scroll this down so if you
ever to weight it by the log of the
market cap this is what you get and then
if we wanted to we can sum that up and
we want to make sure it adds up to a
thousand dollars and it does so if you
wanted to weight your portfolio by the
logarithmic of the market cap this is
what you would do now I'm not saying you
should do this you can wait at however
you want to weight it if you wanted to
weight it by the market cap then instead
of taking this one you would just change
this to be - okay but first before we do
that let's change your investment let's
say you want to do five hundred dollars
then you guys can freeze
that and see what it would be allocated
to each coin if you wanted to do say
$2,500 that's where your allocation
would go you can freeze frame it if
that's how your if that's how you're
doing your investment at $2,500 let's
say we wanted to wait it not by the
logarithmic on the market cap adjust the
market cap so it's a more conservative
approach there's still a ton of risk
involved so we're just going to take
this and change C to B we're gonna
change that C to a B and not C to a B
and then we're gonna go here scroll it
down it still adds to one this still
adds $2,500 and you can see your
allocation towards Bitcoin would be
almost 2 grand
so this means that you're you're mainly
you know you're mainly indexing your
portfolio to match Bitcoin with a very
small amount going to theory um and XRP
and Bitcoin cash and then only say you
know a few dollars going to so the
numbers 9 and 10 so I hope this is
useful for you guys again this is a very
simple way to do it there's no
programming involved there's not even
any Visual Basic involved in in this on
Excel so you know you can easily write
something in Python or whatever Java
whatever you want to do to calculate all
this but I'm hoping that most people can
understand Excel and just see what I'm
doing so get your coins over here add
your market count put in whatever you
want to do over here however you want to
weight it if you want to weight it by
say you know squaring it or taking the
square root you can do that and then you
would get your weight and then you just
put in your investment amount and this
will show you how it would be allocated
okay now I have talked about you know
changing how things are allocated what's
Bitcoin holds a twenty week moving
average and what's Bitcoin gets to a
previous all-time high and then what's
Bitcoin is reaching that plateau point
where it's starting to come back down
and it's breaking the 20 week moving
average then you might want to
reallocate and I've talked about that a
little bit in another video if you guys
want me to continue to expand on this I
can just let me know in the comments
below
and I think that's it for this video now
remember if you guys like the content
subscribe if you guys need this workbook
I can send it to you just join the
telegram channel or the discord channel
that you can find in the description
below and I will see you next time
bye

# Inscriptions, Mempools and Miners - The Week On-chain 39, 2023 (Bitcoin Onchain Analysis)

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=-n73r-38-58
**Publicado:** 20230926 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20230926-inscriptions-mempools-and-miners-the-week-on-chain-39-2023-bitcoin-onc.md]`.

---

foreign
and welcome to a glassdo video report
for week 39 2023 so we're going to be
focusing on the mempool on inscriptions
and on the impact on miners today and
the reason that we've opted to look at
it today particularly is we've seen that
there's been a bunch of these BRC 20
text-based inscriptions and one of these
that goes by the ticker SATs has
essentially finished minting it's been
going since February and it's actually
finally uh closed out and and finished
that mint process so over the last seven
months we have seen inscriptions be a
significant buyer of block space and
what we're basically going to do is just
take a bit of a snapshot of where we are
at the end of that kind of period of
time arguably the end of what we're
going to call Wave 2 and then we can
really have a bit of a foundation to
assess what inscriptions mean for minor
revenue for block for Block rewards all
these things moving forward
so what we're going to be diving in
today is starting from the mempool which
is obviously the first time that the
network sees about a transaction we're
going to explore how descriptions
actually show up on chain and really
make a differentiation between data size
and transaction counts which is going to
be an interesting thing we'll explore
that in more detail
I'm going to help illustrate a bit of a
you know now that we've got seven months
of data we have a better view on how
inscriptions actually buy block space
one of a better term and we have a bit
of an analogy and a framework on how we
can think about them moving forward
and we're going to close out by how this
actually looks relative to miners now
why this is really important is
according to our latest hash rate
estimates and block time intervals the
halving is about 206 days away which
means that for you know for the Bitcoin
uh environment the halving is obviously
a significant milestone
but not so much if you're a miner and
your revenues are going to get cut in
half so really having a look and seeing
have you have inscriptions and this
extra fee Revenue actually done anything
to offset that so as always please do
give us a rate a share and a subscribers
helped this channel get to more people
and without further Ado let's get stuck
right into the analysis
okay so here we are in our week on chain
39 dashboard and as I said at the start
we are going to begin with the mempool
now it's really important to remember
that there is no single mempool in
Bitcoin the mempool is individual to
each node and each node has a particular
set of rules now this is the glass node
mempool and we have the default 300
megabytes total size there are other
mempools out there and other mentpool
explorers that will have a much larger
to capture more data in our instance
we're essentially capturing what is the
default mempool going to see
now there's another important thing to
start off with this first metric up the
top here is the total size of
transaction so this is that data
footprint when I talk about the word
size in this session think bytes how
many bytes of data are we talking about
and why this is important inscriptions
really came into the I mean they were
kind of started in February and this is
when it was mostly this is wave one and
it was mostly images files sound files
mostly it was images kind of that first
emergence of ordinals and nfts on
bitcoin
now as we came into May that actually
changed that footprint has largely
become text-based inscriptions we're
going to explore this in a lot more
detail but what you'll see is that note
that the data footprint our mempool was
full from a data perspective you know
arguably with one kind of clearing
moment but our mempool has essentially
been full from a data perspective since
February there has been enough data in
there but remember that images are a
larger file size to text
so if we now look at this is the same
mempool but it's looking at it in terms
of the number of transactions so just
for easy kind of computation here we
have a fixed 300 megabyte mempool now if
you have a bunch of image files which
are large you know a couple of hundred
kilobytes
um those image files are going to be
less you're going to have less of them
to fill up that same 300 megabytes
now what you can see is that in April
and May this is when text-based
inscriptions and these brc20 token
things showed up in May note that the
transactions we had a full mempool from
February in terms of data but it really
filled up in terms of transactions from
May onwards and it's essentially been
full ever since so what this is telling
us is that there are more transactions
per byte available in the mempool at the
current moment and it really tells you
that since May there's been a dominance
of very small transactions all packing
into that 300 megabytes
so this first chart here is looking at
the number of new inscriptions now back
here when these blew up this was
enormous we were looking at back at uh I
think when ordinals first came out we
did a report uh back in February and
back then it was just all images and
it's almost like the Bitcoin chart back
then this was significant and large well
text-based inscriptions have absolutely
blown it out of the water by Far and
Away text inscriptions in these BRC 20
tokens have been the most significant
buyer of block space certainly in terms
of transaction count now it gets really
interesting we're going to keep
exploring this but uh there's a lot of
interesting Dynamics coming up so you
can see here this is the percent of how
many transactions were confirmed now on
the axis here you can see at the top
we're talking about sixty percent fifty
percent forty percent so images were you
know let's say seven and a half five
percent right they were only buying a
small proportion of the overall
transactions the other 95 you know
thereabouts was the standard monetary
transfers that Bitcoin has historically
been used for
now these text-based inscriptions
remember they're much smaller in terms
of their data footprint so there's a lot
more of them per unit of data and they
have been hitting between 40 and 60
percent of blocks being full of these
transactions so and it gets even more
interesting than this remember this is
on a transaction count basis if you look
at the Block there's lots and lots and
lots of these transactions but as we can
see here they're significantly smaller
you can fit a lot more text-based
inscriptions in the same space as a
standard monetary or a standard or a
text image based inscription sorry so
there's kind of lots of these things but
they're really really small so a really
interesting Dynamic is starting to
emerge
now because of this data and there's
also there's a there's a layer that I
won't go into the full details of um
regarding segwit um segwit has a dual
data structure there's all the
transaction data you know where it's
going how many coins are being sent the
utxo and then there's the witness data
and this is where inscriptions are being
put inside of this is the signature side
of the equation now because for a long
story short those the data that's in
that segwit component the signature
component it gets a discount in terms of
how much you can put in there
essentially now if we go back to our
previous bull markets this is typically
when Bitcoin sees the maximum overall
demand
so this is the number of transactions
confirmed each day and because the block
is essentially capped in terms of its
size you can only fit so many
transactions in So at the bull market
Peaks and these periods of extreme
Euphoria and excitement and lots of
things happening the blocks are
essentially full and historically we're
getting somewhere let's just say 400 000
transactions was the maximum per day
well because we can pack so many of
these inscriptions in particularly the
text ones that has been blown out we got
to 550
000 a significant increase and we
punched another one this week so we have
managed to fit far more transactions and
you can see the magnitude of this right
this was kind of a law of physics until
we found another way to pack more and
more transactions into these blocks
now another way to visualize that same
concept is the average number of
transactions per block so back in the
day we could fit something like two and
a half thousand transactions per block
that's what would classify as a full
block and in segwit that's basically 4
000 weight units again I won't go into
the full details there because it's
probably a bit too nuanced but uh just
think about this in terms of the amount
of available space when a block was full
you had somewhere between two and a half
thousand and two thousand two two
hundred transactions well we've again
we've blown that up a more than 50
percent of memory serves over 3.2 we got
up to over four thousand so we're almost
doubling the amount of transactions it
can fit in but remember this is all
within the same Block it's the same
construction of the block but we can fit
more of these things in because of the
segwit data structure and the way that
these inscriptions are operating
now one Dynamic that still probably
needs a little bit of research and to
understand is the expansion of the utxo
set so remember utxos and we have a
great article which you'll find in the
description below about what utx are
utexos are if you're unfamiliar with
that term it is worth just brushing up
on it and basically we use a gold coin
analogy to help people understand but
the utxo is essentially think about like
a 50 bill or a twenty dollar bill and
every time you spend it that 50 bill is
destroyed and it can be converted into
however many bills of whatever
denomination you want from that point
onwards so what we've seen is a it's
massive expansion in the utxo set it's
added about 46 million new utxos which
is a significant increase and I
mentioned at the start of this session
that there was this brc20 token called
SATs now this thing is essentially
replicated so there's one sat for every
sat in the Bitcoin Supply which that
means that and for each mint you could
only Mint one BTC or 100 million SATs so
what that means is that now that this
thing has finished minting out 21
million of this 46 million new utxos is
associated with that single brc20 token
called SATs so it's going to be very
interesting to see where the mempools
actually start to clear now that this
this has been a major buy this one
inscription has been a major buyer of
block space since February more or less
so now that it's cooled off this is
where it kind of remains to be seen do
inscriptions really have that stickiness
now that I would say the Wave 2 isn't
now finished where all those original
brc20s have been minted we are now going
to see whether inscriptions are a
lasting phenomena or whether they were
indeed just a period of excitement that
disappears we're going to find that out
most likely in the coming months
now this is where things get really
interesting so just to summarize where
we're at these text-based inscriptions
or these BRC 20s in particular are very
very small in terms of their data
footprint we can fit lots of them in so
there's lots of them in the block but
they're kind of taking out the same
amount of space as all the other
transfers were prior to them existing
so in terms of the proportion of fees
being paid wave one when it was images
and Wave 2 when it's text by and large
have been capped out at paying about 20
of the fees so what that means is that
all the transaction fees that mine has
been earning about 20 of them have been
coming from inscriptions
now in terms of the overall size
remember the bytes in that block note
that images were quite significant let's
just recall if we go back to our
previous chart
in terms of the transaction count
five to seven percent were images and 40
to 60 percent were text right so just
invert that number in terms of the
overall size the actual bytes it's the
exact opposite images were taking up 40
to 60 60 of the block whereas text is
something like five to seven percent so
again it's really reinforcing the the
kind of smallness of these things in
terms of their overall weight
so one thing I just the analogy that I
want you to take away here what we're
really seeing is it looks as though
these inscriptions are fairly fee
sensitive they don't particularly want
to pay an overly High fee particularly
images because they're paying on a per
byte basis so because they're quite
large in terms of their size they have
to pay a large absolute fee
but what it really appears they are is
they're almost like imagine you've got a
moving crate and all of the monetary
transfers and all of the standard
Bitcoin transactions they are the thing
that's being shipped in the crate they
have the most value they sit inside that
crate
um in the in the take of the majority of
the volume so the majority the volume
and value is in the contents that's the
monetary transfers
these particularly text-based
inscriptions are a little bit like the
the paper packing that you had put
around the sides you kind of put it into
all of the remaining space anything
that's left over that just hasn't been
filled or there's a tiny little Nook
over there that we can stuff some of
this stuff into that is more or less
what these charts are telling me about
these text-based inscriptions they are
very much the buyer of Last Resort they
appear to be this kind of thing that you
can packing around that block that just
fills any final available space and in
many instances it has to fill that space
because you know all the contents
they're bulky they don't quite fit it's
a bit like Tetris you just need that
tiny little block to fill that final
space that's very much how from looking
at this data I am thinking about
particularly these test text-based
inscriptions so it's kind of an
interesting dynamic
now one way we can visualize this and it
may not be overly intuitive but um I
thought this was a nice way to frame it
up so when we look at means and medians
in the Bitcoin environment because of
its positive skewness and what I mean by
that most of the transactions that we
have in Bitcoin are small right they're
large in count but small much like these
text inscriptions and most of the large
you know 100
000 million multi-million dollar
transfers there's just not many of them
but they will represent the mean right
very large outliers on the upside will
drag the average or the mean up which is
in the red and very lots and lots of
like small typically retail all those
kind of daily transactions they're going
to really be reflected in medians
so if we look here this is the transfer
volume mean in red and median in blue so
the average transfer volume kind of
follows bitcoin's bear markets uh
Tendencies and this is in log scale so
at the bull market Peak we were
transferring over a million dollars on
average pretty wild stuff we're
currently transferring 36 000 on the
average transaction and you can see we
essentially put in higher lows and
higher highs cycle after cycle in many
ways the mean transaction size is more
or less I mean it's going to be a little
bit effective but not by a great deal by
all of these inscriptions
now for our medians it typically
oscillates at bull market Peaks it can
reach about a thousand dollars two
thousand dollars in Bears we get down to
100 200 things like that we're at 7.50
right now so what's going on here is
that these inscriptions are basically
carried on what we call postage it's
like 10 000 SATs sometimes it's a couple
hundred SATs we're moving around cents
and dollars for these inscriptions
because obviously people have a
perceived value of the thing that the
inscription is based on there is a value
that goes beyond the 500 SATs or the
5000 SATs that it's actually being moved
around on people perceive the value of
the nft for one of a better term or the
token or whatever it is
so we can actually see this in the fee
that's paid now the way that I've
calculated this if you're transferring a
hundred dollars and you pay a one dollar
fee that's going to be a one percent fee
so I'm looking in terms of the amount
that's sent and the percent fee of what
is being said
now the mean or the average typically
oscillates between 0.01 and a tenth of a
basis point we're talking about you know
these are the kind of numbers you would
actually expect right between one basis
point and a tenth of a basis point and
that has been constant for pretty much
all of bitcoin's history so that's well
within expected limits
in bull market Peaks we have seen that
typically it's been capped out at about
1.2 percent one percent in the median so
this is kind of the peak urgency people
aren't really thinking so much about
transaction fees they just want to get
their coins onto an exchange at times
like that we get to like one percent
most of the time it's around point one
percent that's kind of the typical level
well note that particularly on that fee
spike in March we got up over 50 and
we're currently at 10 so what we're
seeing is that people are willing to pay
extremely high fees because they're only
moving around 500 SATs but they believe
that the value of the inscription is
more than the SATs that it's attached to
it's this really interesting Dynamic
where we're seeing utxos have a value
that's actually not really measurable
because it's an nft or it's a token or
it's it's some more subjective component
so um just you know really what these
charts are doing is just helping present
this this kind of case that there is a
bit of a shift here we can certainly use
our means to really assess what's going
on in kind of the Bitcoin economy the
monetary transfers but when we're
thinking about inscriptions we probably
have to look a little bit more at the
median because it's going to be really
small but lots and lots of them
so shifting gears just to close this
piece out we're going to focus on the
miners because as we look at this what
we're basically seeing is that there is
a bit of an uptick in fees they're
taking they're paying about 20 of the
fees it's kind of like packing around
the edges of the box so now we really
truly have very very dense and full
blocks and it does remain to be seen now
that this SATs uh brc20 is minted out
does this actually stand the test of
time
now in terms of the actual impact on
mining revenues on the left here the
blue curve is the total amount of fees
and the Orange is the percent of the
revenue that comes from fees so high
level you can see that in Bear markets
the fee Market has historically gone to
sleep we're talking about something
around 20 12 to 20 Bitcoin per day
now we've seen it tick up to about 40 or
48 sometimes 50. so let's just say for
argument's sake it's roughly a doubling
so we've seen about a 2X
but it's still relatively small we're
still only talking about 40 to 50
Bitcoin per day which you know the block
rewards 6.25 so we're talking about
adding yeah what is it maybe six seven
eight blocks in terms of overall uh fee
Revenue
at the percent that's coming from fees
has historically bottomed around one
percent of the overall uh overall reward
that's now jumped to four percent so
look that's a meaningful uptick if you
look at it from you know comparing one
for one
but at the end of the day if we are
coming towards the end of the kind of
mania phase or at least wave two of
inscriptions what we've seen is that yes
they're adding positive free pressure so
it's a it's a thumbs up but it's not a
five thumbs up right it's not get the
crowd cheering it's telling us that
we've got a very very light base load
buyer of cheap block space
but it's not really going to turn the
tides in terms of minor Revenue
certainly not with a halving on the
horizon we have not doubled minor
revenues we haven't you know we've
literally put it up by a couple of
blocks per day
now the tough case when it comes to
miners is that in that time since
February when inscriptions came out hash
rate is up 50 so the competition
fighting over this tiny little uptick in
inscription Revenue has you know we've
added 50 to our overall mining uh mining
pressure
and if we look at it from a hash price
perspective this has to be the most
brutal chart in all of Bitcoin
um this is in Orange BTC reward per
extra hash and in blue US dollars per
extra hash
now this is in log scale and this thing
goes down and down and down and down and
we're in the process of breaking to new
all-time lows so essentially per extra
hash on the network miners are earning
the least they've ever earned on both
the USD and a BTC basis now where this
is really interesting and this is not
the the place we'll go into the security
budget but what is fascinating to me is
that our hash price the reward per extra
hash is the lowest it's ever been
but our hash rate is at all time high
and what this is telling us is that
miners still even though there's a lot
of concerns about the security budget
and people talk about these things the
reality of the situation is that miners
still have enough to both run their Rigs
and invest in more newer better better
infrastructure machines we are still
seeing capex investment in the mining
cycle which is driving that competition
up new rigs come online new research and
development for new A6 comes online now
we will again we will see how this plays
out because obviously with the halving
coming these Dynamics continue to shift
and certainly we can see that
inscriptions haven't really moved the
needle in a sustainable way in terms of
their fee Revenue but again all of these
things it's the free market trying to
work it out
so coming across and closing out with
minor pain points right now with the
halving the halving is about 206 days
away based on our current block
estimates
so how do we know where the stress
points are for miners
well we've got two models that we're
going to look at here the first one is a
simple log log regression between
difficulty and market cap why I like
this model is first of all the art that
the correlation is 95 in terms of the r
squared and really everything in the
mining World from you know from the
miners salary to the power contract to
the geographical location to you know
all of the information known about
mining is baked down to one one number
difficulty difficulty is the price to
mine Bitcoin and what we've essentially
done is say well let's correlate the
market cap which obviously is the USD
that's the perceived incentive for
miners by the difficulty which is how
hard it is to actually get it out of the
ground you know for one of a better turn
now that with that correlation we're
looking for what is kind of the average
what is the Middle where is the typical
minor what is that stress point of
balance and right now it's at twenty
four thousand so it's about a seven
percent premium where we currently are
meaning miners are probably on the edge
of their seats right now
we have another model which looks at it
from how much issuance do you earn per
unit of difficulty so it's kind of like
what is the cost versus the reward it's
kind of another way to think about it
now this model uses a simple curve fit
so the red curve down the bottom here is
the most efficient miners it's curve
fits are bear Market bottoms it's kind
of telling us where is the Survivor
level the miners that are super hardcore
have the absolute best balance sheet and
are ready to survive what's an
approximate cost for them well now that
we've got the most efficient Miner we
can add our purple curve which is the
post halving
most efficient minor well that's
currently down at 15 000 for the most
efficient miners which you know 26 000
happy days but that obviously jumps to
over 30 000 which we are underneath so
if the Bitcoin price doesn't get above
30 000 and probably with a better margin
to to boot we are most likely going to
see some real stress into the mining
industry as we get closer to the halving
and once we go through the halving there
will be a lot of minors as the price
hasn't appreciated that are probably
going to be under stress so uh just
putting a flag in it now depending on
how things are looking we will certainly
be revisiting this topic because I think
the the mining topic is certainly one a
lot of people have interest in
um so we will explore this in more
detail certainly as we get closer to the
halving because that's obviously where
these things really come to bear and you
can actually relate the middle the
geometric mean between these two is the
orange it actually trades very very
closely to our difficulty regression
model so you can almost use those two as
a as a bit of a balance
so thanks for tuning in for that session
folks hopefully you found that useful
and a little bit different my big
takeaway from inscriptions is that they
are net positive they're kind of a cheap
block space buyer of Last Resort they're
going to stuff around all the final
edges and just completely fill the
tetris block they appear to be willing
to buy cheap block space they're not
they don't appear to be displacing
monetary transfers so in that case
they're relatively benign the question
is have they really moved the needle
they're positive but have they really
moved the needle in terms of fees my
assessment is not yet and are they going
to be sustainable now that we've kind of
seen the end of wave two we will
probably find out over coming months so
uh something to think about something to
contemplate and hopefully have a great
week I'll see you in the next one cheers

# Glassnode Academy: CDD and Binary CDD

**Fuente (VÍDEO):** glassnode_tactico · YouTube — https://www.youtube.com/watch?v=81sdyHkXJr8
**Publicado:** 0000 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/0000-glassnode-academy-cdd-and-binary-cdd.md]`.

---

hello and welcome to glass note academy
today we're looking at the bitcoin
metric coin days destroyed and then
a derivative of that called binary coin
days destroyed
so what we'll look at today is the
concept of coin days and the concept of
coin days destroyed
we'll look at which segment of the
market this is providing us insight into
and we'll look at how we can actually
apply coin days destroyed and binary
coin days destroyed as part of our
market analysis
but the concept of a coin day is a a
volume of btc that's essentially been
dormant or it hasn't moved in a period
of time
so in this case we've got alice with two
btc she withdrew them from an exchange
for example 100 days ago
that has now accumulated 200 bitcoin
coin days
when she goes to spend that those 200
coin days will be reset to zero those
200 days are destroyed and then those
two btcs start re-accumulating new days
um similarly bob has half a bitcoin
that's at 60 days age so you've now got
30 coin days and carol's got 10 btc at
five days which gives us 50 coin days
and if all of these outputs happen to be
spent on the same day we would sum them
up and we would say that 280 coin days
have been destroyed on that particular
day
so coin days destroyed is very much a
it's a multiplication of
time as an input we're looking at the
lifespan of those utxos that were spent
on that particular day
and we're multiplying it by how much
volume was actually spent so we're
getting a view on both the amount of
coins that were moved as well as how old
they are
so what this is tracking in general is
when are we seeing older coins coming
back to life when a
older dormant maybe coins that were
purchased in the last market um coming
back onto the market
and becoming reactivated and a higher
coin days destroyed level
will essentially say that more of those
either higher volume
or older coins or a combination of both
are currently on the move
so high value is old coins moving and
low values tend to be
day-to-day traffic now what binary coin
day's destroyed is
it looks at the average coin days
destroyed over bitcoin's lifespan
looks at what is it what is an average
value what is considered normal in this
instance
and it will return a one or a zero
literally a binary number
whether the current day is more or less
than that average so it's giving us a
bit of an idea
compared to the historical performance
what is typical in the market are we
greater than average which will return a
value of 1
or less than average which will return a
value of 0.
so now let's jump into glass node studio
and we'll have a look at how we apply
these in our market analysis
but here we are in glass node studio
looking at the coin days destroyed
metric we've applied a 30-day moving
average to try and smooth out some of
the noise and get a bit more signal
and what we can see is we've almost got
two different characters we've got this
general trend line to the upside which
makes sense because the older bitcoin is
around the more coin days the more time
can actually be baked into these
utxos and we also see these periods of
high volatility and spikes and you can
see that these generally occur
around periods of volatility and then
particularly during bull markets we get
these strong uptrends so
what this is signifying is that older
coins are coming back into the
circulation there could be coins that
were purchased back at an earlier level
and in many instances what this is
really tracking is what is the smart
money doing are they selling into
strength
or during a bear market is it telling us
that there's a bit of panic selling
going on or
is there coins being re-released into
the market so it gives us a bit of an
idea about what the
both the volume and the time based
elements of those coins are
if we look at binary coin days destroyed
this barcode down the bottom here
is essentially signaling either a one
which is a colored bar or a zero which
is a
no colored bar and that's essentially
telling us is it more or less than
average during those particular periods
of time and you can see that
particularly during bullish markets we
get a lot of days where it's above
average meaning more coins are coming
into circulation or older coins are
being spent
and during bearish markets we tend to
get this more barcode type behavior
where there's more days where it's
actually below average and there's less
activity going on on chain
and a useful trick when using the binary
coin days destroyed is similarly to
apply some kind of moving average
and you can get a little bit of a view
on the trend so when it's hitting up to
one it means that there's 30 days of
consistent
old coins coming back into circulation
we're consistently above
uh the the average coin days destroyed
and you can start to see when it's
beginning to trend and move from this
particular baseline so providing a
moving average just gives you that
extra bit of signal as to what the trend
is when it comes to being above
or below average in coin days destroyed

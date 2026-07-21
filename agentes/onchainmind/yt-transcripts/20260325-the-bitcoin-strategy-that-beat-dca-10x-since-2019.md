# The Bitcoin Strategy That Beat DCA 10x Since 2019

**Fuente (VÍDEO):** onchainmind · YouTube — https://www.youtube.com/watch?v=s8R4b_V2BS0
**Publicado:** 20260325 · **Subtítulos:** en (pueden ser auto-generados)
**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). Cita como `[yt-transcripts/20260325-the-bitcoin-strategy-that-beat-dca-10x-since-2019.md]`.

---

What if I told you that a single
rule-based strategy returned over 3,800%
and delivered more than 10x the
performance of dollar cost averaging
since 2019? Well, that's exactly what
I'm going to show you today.
This is just one of countless fully
back-tested systems built to work across
all market conditions and also with any
indicator on my platform using a tool
I've been developing behind the scenes
for a while now called the strategy lab.
I'm excited to show you guys this one,
so let's get into it.
Today we're diving into something that
up until now has been running quietly in
the background, but it's about to become
one of the most powerful tools on my
entire platform and it's called the
strategy lab. And it's something I'm
going to be releasing within the next
few weeks or so.
And what you're looking at here is a
full backtesting engine built from the
ground up designed to take any metric on
a platform and turning it into something
that's actually actionable with just
about every tool under the sun to test
its robustness of your chosen strategy.
Because let's be honest, most
indicators, even the good ones, just sit
there. They give you a number, maybe a
signal, but they don't tell you actually
what to do in a structured and
repeatable way.
But the strategy lab here fixes that. It
takes those same indicators and asks a
much more important question. If you had
traded this properly with defined rules,
what would the outcome actually have
been no matter the time frame?
Now, this is going to be rolling out to
everyone very soon, but today I wanted
to give you a sneak peek and walk you
through one specific example using an
indicator that pretty much everybody
already knows, which is the Fear &amp; Greed
Index.
And more importantly, I'm going to show
you how taking a slightly different
approach to it doesn't just improve
performance, but it completely changes
the outcome.
We're talking about a strategy here that
has returned over 3,800%
over double a buy and hold strategy and
delivered over 10 times the performance
of DCA. So, if you've ever looked at
something like the Fear &amp; Greed Index
and thought, well, it's in extreme fear,
so I should probably just buy here.
Well, this is where things start to get
a little bit more nuanced.
Now, before we even touch on all of
this, right now the Fear &amp; Greed Index
has been sitting in extreme fear
territory for an extended period now.
And we're not just talking about a quick
dip. We're actually talking about
roughly 50 consecutive days in extreme
fear.
And this is exactly the kind of
environment where retail typically
panics and in general sells into
weakness. But historically, this is also
where the most sophisticated capital
starts to step in.
But here's the problem. Most people use
the Fear &amp; Greed Index as a static
number.
They look at today's extreme fear
reading and treat that as the signal.
And the issue is that a single number
doesn't tell you about the direction of
it. It doesn't tell you whether
sentiment is improving or deteriorating.
And it certainly doesn't tell you if
fear is peaking or if it's accelerating
lower.
And that's the gap we're trying to solve
today.
So, instead of looking at that level,
we're going to look at the change in
sentiment over time. And that's what
we're going to be calling the Fear &amp;
Greed Cadence.
So, conceptually it's simple. You take
today's Fear &amp; Greed reading and
subtract that value from a fixed period
ago. In this case, we're going to go
with 90 days. And what you get is a
measure of how sentiment is evolving
over that window.
But the key signal here, and the one
that actually drives the strategy, is
the zero cross.
When the Cadence moves from negative to
positive, that becomes your buy signal.
It tells you that sentiment has stopped
deteriorating and has started improving
again.
And when it moves positive back into
negative again, that's your sell signal.
Sentiment acceleration has turned down
again.
It sounds simple, and it actually
genuinely is. And that's the whole point
of this video, is not to try and
overcomplicate things. Sometimes the
ideas that are simplest, yet the most
structurally grounded, tend to generate
the best returns. But also, we can take
things a step further if you want to
build a more complex strategy.
And I've built one here that's called
the composite strategy, but it's
actually pretty simple. Instead of just
relying on the cadence zero cross alone,
it adds two extra conditions before
entering a trade.
First, it waits for the smooth cadence
to cross above zero.
But on top of that, Bitcoin's price has
to be trading above its 200-day moving
average, which just confirms that the
broader trend is intact. And then also
the Fear &amp; Greed Index itself has to be
above 20, which just filters out buying
into total capitulation when sentiment
hasn't even started to turn yet.
So, all three have to line up for a buy.
But for selling, I've just made it
immediate. The moment the cadence
crosses back below zero again, you get
out. No filters, no waiting, just a
swift exit. And the idea is
straightforward. Avoid the bear market
false rallies that trap the similar
strategies, while keeping the exit
responsive so you don't give back gains.
But anyway, it's not really that much of
a complex strategy when you break it
down. And it took me about 2 minutes to
think of this one, so I'm sure you could
come up with something way more
elaborate. But anyway, if we go over to
the summary tab here and look at the
best-performing version of the strategy,
which was the composite one, you'll see
that it's currently in cash, completely
out of the market. And the last signal
that it generated was a sell in
mid-September 2025,
when Bitcoin was trading at around
$111,000.
And since that signal, Bitcoin has
dropped roughly 40% in a drawdown from
that $111,000 mark. And this strategy
has sidestepped that entire move, simply
by stepping aside when sentiment rolled
over.
So, while most portfolios, including
most of my own, are sitting through that
drawdown, this one has effectively
preserved in cash, waiting for the next
confirmed shift back to positive
sentiment. Now, as you can see here, the
Strategy Lab is testing all these
different types of smoothing signals.
They all use the zero cross logic I just
explained, but they apply different
levels of smoothing, such as the raw
value, 30-day, 60-day, 90-day, and
180-day.
And the smoothing matters for this one
because the raw signals are noisy.
If you just used an unsmooth cadence or
even the fear and greed, it whips around
constantly and you'll get a lot of false
signals, especially in choppy
conditions. So, as you increase the
smoothing window, you kind of reduce
that noise. You get fewer trades, but
they're much higher quality ones. But,
the trade-off for too much smoothing is
lag.
The heavily smoothed signal, like the
180-day one, will react pretty slowly.
It will get you in later after the
bottoms and out later after the tops.
But, anyway, all of these here are
benchmarked against two baselines, buy
and hold and DCA.
And buy and hold starts in March 2019,
which is basically the beginning of any
reliable fear and greed data. It was
actually an incredibly favorable time to
enter Bitcoin at around $4,000.
And we're going to start with an initial
investment of $10,000.
Now, that buy and hold strategy grows to
about $173,000
today, which is a 1,600% return or 50%
compound annual growth rate. Not at all.
It was actually an exceptional entry.
And dollar cost averaging takes that
same $10,000 and spreads it evenly
across all the trading days.
And that ends up with around $33,000
or a 237% return.
And that might sound disappointing, but
that's still an 18% compound annual
growth rate, decent by TradFi standards.
And it's important to test DCA because
it's actually what most people actually
do. It's the realistic baseline.
Now, the results here in the overview
tab, we can clearly see that the best
performing strategy is the composite. It
delivers a return of over 3,800%
turning that 10 grand into roughly
$400,000.
And that's not marginal outperformance,
it's a completely different outcome.
It outperforms buy and hold by roughly
2,200%
whilst also reducing the maximum
drawdown from 76% to 56%. And when you
look at the equity curves here, you can
see that the top strategies consistently
pull away from buy and hold, and
definitely from DCA over time.
But, the raw returns only tell you part
of the story, and this is the key bit.
If you flip over to the risk-adjusted
view, this is where things start to get
genuinely institutional grade.
Metrics like the Sharpe ratio, Sortino
ratio, Calmar ratio, and profit factor,
they're not just academic. They're
actually how all these professional
capital allocators evaluate their
different strategies.
Now, if you're not aware, the Sharpe
ratio measures how much return you're
getting per unit of total risk that
you're taking on. And anything above one
is good, and above 1.3 is excellent.
And the Sortino ratio refines that by
only penalizing the downside volatility,
which is particularly relevant for
crypto, where upside vol is something
you actually want. And the Calmar ratio
is something less known, but it's just
as important. It compares your annual
return to your worst drawdown.
So, if it's above one, you're generating
more return per year than your worst
loss drawdown generated. And that's one
of the key institutional thresholds.
And the profit factor is probably more
known amongst you traders.
It looks at the total gains versus the
total losses, and anything above two is
considered very strong.
Now, you can see here that the composite
strategy clears all of those at an
exceptional level.
A Sharpe of 1.44, a Sortino of 2.2, a
Calmar above 1.2,
and a profit factor of 35.
And that last number is especially
telling. It means that for every unit of
loss, the strategy is essentially
generating 35 units of gain, which is
wild for a simple strategy that I came
up with in literally 2 minutes.
Now, compare that to buy and hold, which
has a Sharpe below one, and a Calmar of
just 0.65.
Or in other words, its worst drawdown is
larger than its annualized return.
Now, just let that sink in for a second.
This was one of the best entries that
you could have got in buy and hold. Yet,
it has these sort of risk-adjusted
ratios. And it's not a profile that
institutional capital typically accepts.
Yeah, just as we said before, we've been
more than happy with that level of
return. But, sometimes good returns
aren't actually good risk adjusted
plays. It's a nuanced concept, but it's
important if you're playing across
different timelines. Because although I
said this wasn't a particularly good
entry point, the strategy of buying hold
might not have played out well at
different entry point, and these metrics
prove that perfectly.
Now, let's look at the actual trading
behavior.
The composite strategy generated 13
trades over the entire period. So,
roughly about 1.8 trades per year. And
it had 86% win rate. And it's only in
the market about 39% of the time.
Now, contrast that with just a raw fear
and greed strategy which most people
incorporate. That generated about 183
trades, and it only had a 42% win rate.
And that even surprised me. So, more
activity, worse results. And that's the
key point I think most people are
missing here. Frequency does not equal
performance.
Now, let's quickly take it one level
deeper with the regime analysis. Here,
every single day is classified based on
the slope of the Bitcoin 200-day moving
average. So, if the 200-day moving
average is sloping upwards, it classes
it as a bull regime. Negative, it's a
bear. And flat, it's sideways. It's a
simple but pretty effective way to look
at the market.
About 67% of the time is actually spent
in bull markets, 25% in a bear, and the
rest, roughly 6%, is spent in sideways
choppy conditions.
Now, buy and hold performs as you'd
expect. Strong in bulls, but still
exposed during bear phases. And what's
interesting is that the top cadence
strategies don't just protect on the
downside. They actually outperform in
the bull markets as well, which again
surprised me.
And finally, let's go on to one of the
most interesting elements of this tool,
which is the Monte Carlo analysis. Now,
if you're not familiar with the concept
of Monte Carlo, this is essentially
where you test whether the results of
your strategy are robust or they're just
a product of lucky sequencing and
timing.
And I guarantee you that 99% of the
trading strategies that you see online
don't test for this, and this is why
they fall short.
Now, what it does this take all the
individual trades and reshuffles them
randomly across thousands of different
simulations. And for this one we're
running 5,000 simulations in this case.
And it essentially tries to see how
sensitive the outcome is to the order of
the trades.
And for the composite strategy, the
result actually sits comfortably within
the central distribution.
And that tells you that the performance
isn't dependent on perfect timing or
lucky sequencing, and that's what we're
looking for.
So, when you're testing different
strategies, this is exactly what you're
looking for. The edge is in the strategy
itself and not in randomness of the
timing.
So, bringing this back to where we are
today, we're sitting in an environment
of prolonged extreme fear. The kind of
environment where most people feel
compelled to act, either buying the dip
or selling into fear.
But, the strategies we've been looking
at today are actually sitting in cash,
and they have been for a while.
The portfolio is currently sitting at
400k, having avoided a 40% drawdown, and
it's waiting. So, zooming out, this
really isn't about the composite
strategy or the Fear &amp; Greed Index in
general. I actually really don't care
about it that much at all. It's a strong
result, but it's not the strategy. It's
just a very clear example of what
happens when you take a simple indicator
and actually play around with it
properly. Because the Fear &amp; Greed Index
is relatively basic. It's sentiment, and
even then, we've managed to turn it into
something that has significantly
outperformed buy and hold and DCA by a
very wide margin with better
risk-adjusted returns and fewer trades.
So, the real takeaway for me here is
this. What happens when you apply the
same work to a much stronger signal?
Well, that's exactly what I plan to roll
out for you guys. This whole strategy
lab thing is something I wanted to give
to you guys. It's built so that you can
define your approach. If you want to
catch the bottoms, you can optimize for
that. If you want confirmation and a
smoother equity curve, you can do that,
too.
And if you want something that trades
momentum like a maniac, then you can
also build that.
And more importantly, you can test it
properly. And this is what most tools
are missing. You've got to test it
across different simulated market
regimes with the full visibility of its
actual robustness and the risk adjusted
metrics that matter more than anything.
Because most strategies look good in
hindsight, but very few hold up when you
actually stress test them. So, as this
rolls out, don't just copy what you've
seen here. Use it as a starting point to
build your own strategy. Because the
edge isn't in one indicator. It's having
a repeatable process that keeps you on
the right side of the market over time.
So, anyway, I can't wait to share it
with you guys, and I hope you all found
this useful. So, thanks for watching,
and I'll catch you all in the next one.
Call me.

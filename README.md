# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** no fixed size. One `##` section = one chunk, with a 900-character
ceiling and a 150-character floor.
**Overlap:** none between sections. One sentence of overlap only when a single
section runs past 900 characters and has to be split.

The starter cut at 800 characters and gave me 51 chunks from 14 documents,
averaging 650 characters, with the shortest at 24 — the leftover tail of a
document that didn't divide evenly. It also sliced straight through my labelled
sections, so "Where to stay" ended up glued to the back half of "What to see".

My documents are markdown guides with a `# Town` title and seven `## ` sections
under it. A section is already the unit my questions map to — "what's parking
like in Halden Bay" is one section, not half of two — so I split there instead
of at a character count. Overlap between sections is zero on purpose: the
sections are about genuinely different things, and carrying the tail of "Eat and
drink" into "What to see" would just add noise.

The part that isn't obvious from the file: every chunk gets the document's `#`
title pasted back on top. All ten town guides use the same seven headings, so a
"Getting around" chunk on its own reads "flat and compact — 15 minutes end to
end" with nothing in it to say which of ten towns that is. The title costs about
15 characters per chunk and is what makes them answerable alone.

**I changed my mind partway through.** I set the merge floor at 250 characters
first, figuring anything shorter was too thin to stand alone. That merged 25
sections, including "Getting around" into "Eat and drink" — exactly the
multi-topic chunk I was trying to avoid. At 150 only one section in the corpus
merges (the accessibility guide's two-line preamble). The sections were already
the right size; I'd set the floor above them.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: guide_accessibility.md#0 `` — produced by: chunker.py::split_documents``

```
# Getting around the region with limited mobility
## Overview / Straightforward
An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines,
running every 8 minutes on weekdays. The city museum and covered market are both
step-free. The distances between districts are the main consideration.

**Brightwater** is level along the river and through the centre. The mill museum
is step-free. The station is a 15-minute walk from campus on flat ground, or the
shuttle meets the four busiest arrivals.
```

**Chunk 2** — source: guide_corry_vale.md#6 `` — produced by: chunker.py::split_documents``

```
# Corry Vale
## When to go
May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** — source: guide_givens_mill.md#3 `` — produced by: chunker.py::split_documents``

```
# Givens Mill
## Eat and drink
A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: guide_kestrelford.md#5 `` — produced by: chunker.py::split_documents``

```
# Kestrelford
## Where to stay
Two inns on the square and a handful of rooms above the pubs. Booking ahead matters between May and September and not at all otherwise. There is no accommodation of any kind within four miles of the town in either direction.
```

**Chunk 5** — source: guide_pellew_sands.md#7 `` — produced by: chunker.py::split_documents ``

```
# Pellew Sands
## Practical notes
Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.
```

## Sample Answer
**Question:**
"What are the three least approachable towns from an accessibility standpoint?"
  
**Answer:**

```
(best distance 0.559, cutoff 0.6)

Based on the documents, the three towns listed as difficult for limited mobility are **Kestrelford**, **Halden Bay**, and **Corry Vale** (along with **Elder Ness**, which is also listed in the same difficult section).

Source: `guide_accessibility.md`

Sources retrieved: guide_accessibility.md, guide_givens_mill.md, guide_kestrelford.md, guide_walking.md
```

**My relevance cutoff:**

**Why 0.6 and not something else.** The gap is wide enough that anything from
roughly 0.60 to 0.80 gives the same result on these ten questions: all five
in-corpus answered, all five out-of-scope refused. Since a whole range works
equally well on my test set, I kept 0.6 rather than moving it for no measurable
reason. I put it at the low end of the workable range on purpose — I'd rather
the system refuse a question it could have answered than answer one it
couldn't, because a refusal is visible and a wrong answer isn't.

**What I'd get wrong at this number.** I found this by accident. The first time
I asked my Sunday-evening question I pasted it with the quotation marks still
around it, and the identical question scored **0.642** instead of 0.552 — over
the cutoff, and refused. So the gap isn't as empty as the table makes it look:
a question that's worded awkwardly, or that carries stray punctuation, can land
in the middle of it. At 0.6 that gets refused. Raising the cutoff to 0.7 would
have caught it and still refused all five out-of-scope questions, which is the
argument for going higher. I stayed at 0.6 because the failure I saw was a
formatting mistake on my part rather than a real question, but it's the thing I
would watch first if the system starts refusing things it shouldn't.

| In-corpus question | Best distance | Gate |
|---|---|---|
| Sunday evening walk + meal | 0.552 | pass |
| Best Saturday market, when established | 0.360 | pass |
| Two best seasons to visit | 0.417 | pass |
| Easiest town for walking | 0.524 | pass |
| Three least accessible towns | 0.559 | pass |


| Out-of-scope question | Best distance | Gate |
|---|---|---|
| Capital of Mongolia | 0.811 | refuse |
| Changing diesel engine oil | 0.888 | refuse |
| 1994 World Cup | 0.964 | refuse |
| Ibuprofen dosage | 0.835 | refuse |
| For loop in Rust | 0.836 | refuse |

## How I Used AI



**1.**
**1. The chunker, and a floor that was set too high.**

I described my corpus and asked Claude to write a chunking strategy that fit
it, rather than the starter's 800-character windows. What came back was
section-based splitting — one `##` section per chunk, with the document's `#`
title pasted on top of each one — plus a floor that merged any section under
250 characters into its neighbour.

The title-repeating part I kept, because it solves a problem I'd already
spotted when I read my documents: all ten town guides use identical headings,
so a bare "Getting around" chunk doesn't say which town it's about.

**2. Criterion 4, which I sent back.**

I asked Claude to review my report and make sure I answered all the questions.
I removed the parts that were overly verbose.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | each text contains an answer that shows up in expected.
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET | all the answers can be traced back to their source documents
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | irrelevant questions are denied, rather than guessed at
| 4. Chunks reference towns  | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | when sampling chunks, there is a town name inside each chunk
| 5. Answers don't confuse towns (i.e. no hallucinations or conflating facts) | 5 of 5 | 5/5 | 5/5 | 5/5 | MET | wrong answers are not included with a correct answer.

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->


## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### If I wanted to go for an easy walk and a meal on a Sunday evening somewhere in the region, where should I look? — run 1

- Best distance: 0.5520 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md

```
Based on the documents, Marchwood and Thornby Wells are the best places to look for a meal on a Sunday evening. (Source: guide_eating.md)
```

### Which city has the best Saturday market, and when was it established? — run 1

- Best distance: 0.3596 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_kestrelford.md

```
Kestrelford has the region's best Saturday market, which has run since the 1400s. 

Sources: `guide_eating.md` and `guide_kestrelford.md`
```

### When are the two best seasons or months to visit the region? — run 1

- Best distance: 0.4175 (passed the gate)
- Sources retrieved: guide_halden_bay.md, guide_marchwood.md, guide_seasons.md, guide_thornby_wells.md

```
Based on the provided documents, June and September are noted as the "sweet spot" for Halden Bay (`guide_halden_bay.md`), and September is also highlighted as "the other sweet spot" for the region overall (`guide_seasons.md`). Additionally, May and June are the best months for the gardens at Thornby Wells (`guide_thornby_wells.md`), and late May is described as arguably the best week of the year in Brightwater (`guide_seasons.md`).
```


### Which town is the easiest for walking? — run 1

- Best distance: 0.5238 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
**Thornby Wells** is described as the region's most accessible town on foot (from `guide_walking.md`) and the easiest town in the region (from `guide_accessibility.md`).
```


### What are the three least approachable towns from an accessibility standpoint? — run 1

- Best distance: 0.5588 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md, guide_kestrelford.md, guide_walking.md

```
Based on the "Difficult" section of the document, the three least approachable towns from an accessibility standpoint are Kestrelford, Halden Bay, and Corry Vale (along with Elder Ness, which is also listed in that category). 

Source: `guide_accessibility.md`
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | each text contains an answer that shows up in expected.
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET | all the answers can be traced back to their source documents
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | irrelevant questions are denied, rather than guessed at
| 4. Chunks reference towns  | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | when sampling chunks, there is a town name inside each chunk
| 5. Answers don't confuse towns (i.e. no hallucinations or conflating facts) | 5 of 5 | 5/5 | 5/5 | 5/5 | MET | wrong answers are not included with a correct answer.

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

None of my runs produced misses. I don't think my targets were set low. 
I'd refine my criteria #5 to make grading more straightforward.

## The Improvement

**What I changed:**

**Revised Criteria #5 in unit 2:** For all 5 of my test questions, every fact in the
> answer passes two checks:
> 1. **Right town.** If the fact is about a town, the cited file says it about that
>    same town, not a different one.
> 2. **Right file.** I can find the fact by opening a file the answer cites
>    for it and searching. Any one of the listed files counts.

**Why I picked it:**

**Why revised:** The original says "the town I actually asked about," but
none of my five questions names a town. The check now
compares the town in the answer with the town the source file gives that
fact to. I also wrote down how to score answers that list their sources. 


### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | each text contains an answer that shows up in expected.
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET | all the answers can be traced back to their source documents
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | irrelevant questions are denied, rather than guessed at
| 4. Chunks reference towns  | 4 of 5 | 5/5 | 5/5 | 5/5 | MET | when sampling chunks, there is a town name inside each chunk
| 5. Answers can be looked up in the provided source  | 5 of 5 | 5/5 | 5/5 | 5/5 | MET | the provided fact was verified in the source document.

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

The revised criteria helped clarify with evalating MET vs. MISSED.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

The scorer could be more sophisticated and test more of the criterion. 

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

I made the desired changes to the criteria in this unit. Criteria 5 was ambiguous 
about how it would be evaluated--the revision clears that up.
# Run log — after_revised_criteria_5

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-27 15:10

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| If I wanted to go for an easy walk and a meal on a Sunday evening somewhere in the region, where should I look? | pass | pass | pass |
| Which city has the best Saturday market, and when was it established? | pass | pass | pass |
| When are the two best seasons or months to visit the region? | pass | pass | pass |
| Which town is the easiest for walking? | pass | pass | pass |
| What are the three least approachable towns from an accessibility standpoint? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.811 | refused |
| How do I change the oil in a diesel engine? | 0.888 | refused |
| Who won the 1994 World Cup? | 0.964 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.835 | refused |
| How do I write a for loop in Rust? | 0.836 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### If I wanted to go for an easy walk and a meal on a Sunday evening somewhere in the region, where should I look? — run 1

- Best distance: 0.5520 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md

```
According to the documents, Marchwood and Thornby Wells are the places where Sunday evening meals are easiest to find (guide_eating.md). Additionally, Kestrelford offers an "easy gradient" walk on the old trackbed (guide_kestrelford.md), though Kestrelford's pubs have strict serving windows and kitchens across the region outside Marchwood generally stop serving by 9pm or earlier (guide_eating.md).
```

### If I wanted to go for an easy walk and a meal on a Sunday evening somewhere in the region, where should I look? — run 2

- Best distance: 0.5520 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md

```
Based on the documents, Marchwood and Thornby Wells are the best places to look for a meal on a Sunday evening, as Sunday evening is the hardest meal to find anywhere else in the region. 

Source: `guide_eating.md`
```

### If I wanted to go for an easy walk and a meal on a Sunday evening somewhere in the region, where should I look? — run 3

- Best distance: 0.5520 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md

```
Based on the provided documents, Sunday evening is difficult for finding a meal across most of the region, but it is easier to find in Marchwood and Thornby Wells (`guide_eating.md`). For an easy walk, Kestrelford features the old trackbed walk running six miles to the next village along an easy gradient (`guide_kestrelford.md`). However, the documents do not mention a place that combines both an easy walk and a Sunday evening meal in the exact same location. Therefore, I do not have enough information to name a single location meeting both criteria.
```

### Which city has the best Saturday market, and when was it established? — run 1

- Best distance: 0.3596 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_kestrelford.md

```
Kestrelford has the region's best Saturday market, which has run since the 1400s. 

Sources: `guide_eating.md` and `guide_kestrelford.md`
```

### Which city has the best Saturday market, and when was it established? — run 2

- Best distance: 0.3596 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_kestrelford.md

```
Kestrelford has the region's best Saturday market, which has run since the 1400s. 

Source: guide_eating.md (and also mentioned in guide_kestrelford.md)
```

### Which city has the best Saturday market, and when was it established? — run 3

- Best distance: 0.3596 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_kestrelford.md

```
Kestrelford has the region's best Saturday market, which has run since the 1400s (or continuously since the 1400s). 

Sources: `guide_eating.md` and `guide_kestrelford.md`.
```

### When are the two best seasons or months to visit the region? — run 1

- Best distance: 0.4175 (passed the gate)
- Sources retrieved: guide_halden_bay.md, guide_marchwood.md, guide_seasons.md, guide_thornby_wells.md

```
Based on the provided documents, June and September are identified as the "sweet spot" for Halden Bay (from `guide_halden_bay.md`), and September is also noted as "the other sweet spot" for the region overall, with warm, quiet conditions and everything still open (from `guide_seasons.md`). Additionally, May and June are stated as the best months for the gardens in Thornby Wells (from `guide_thornby_wells.md`), and late May is described as arguably the best week of the year in Brightwater (from `guide_seasons.md`).
```

### When are the two best seasons or months to visit the region? — run 2

- Best distance: 0.4175 (passed the gate)
- Sources retrieved: guide_halden_bay.md, guide_marchwood.md, guide_seasons.md, guide_thornby_wells.md

```
Based on the provided documents, June and September are noted as the "sweet spot" for Halden Bay (`guide_halden_bay.md`), and May and June are the best times for the gardens at Thornby Wells (`guide_thornby_wells.md`). September is also described as "the other sweet spot" for the region (`guide_seasons.md`).
```

### When are the two best seasons or months to visit the region? — run 3

- Best distance: 0.4175 (passed the gate)
- Sources retrieved: guide_halden_bay.md, guide_marchwood.md, guide_seasons.md, guide_thornby_wells.md

```
Based on the provided documents, June and September are noted as the "sweet spot" to visit Halden Bay (guide_halden_bay.md), and September is also described as "the other sweet spot" for the region (guide_seasons.md). Additionally, May and June are stated as the best time for the gardens in Thornby Wells (guide_thornby_wells.md), and late May is arguably the best week of the year in Brightwater (guide_seasons.md). 

Sources: `guide_halden_bay.md`, `guide_seasons.md`, and `guide_thornby_wells.md`.
```

### Which town is the easiest for walking? — run 1

- Best distance: 0.5238 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
**Thornby Wells** is described as the most accessible town in the region on foot (*guide_walking.md*) and the easiest town in the region (*guide_accessibility.md*).
```

### Which town is the easiest for walking? — run 2

- Best distance: 0.5238 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the provided documents, Thornby Wells is described as the region's most accessible town on foot (`guide_walking.md`) and the easiest town in the region (`guide_accessibility.md`). 

Sources: `guide_walking.md` and `guide_accessibility.md`
```

### Which town is the easiest for walking? — run 3

- Best distance: 0.5238 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
**Thornby Wells** is described as the most accessible town in the region on foot (*guide_walking.md*) and the easiest town in the region (*guide_accessibility.md*).
```

### What are the three least approachable towns from an accessibility standpoint? — run 1

- Best distance: 0.5588 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md, guide_kestrelford.md, guide_walking.md

```
Based on the documents, the three towns listed under the "Difficult" category for limited mobility are **Kestrelford**, **Halden Bay**, **Corry Vale**, and **Elder Ness** (four towns are mentioned in total under this heading). 

Source: `guide_accessibility.md`
```

### What are the three least approachable towns from an accessibility standpoint? — run 2

- Best distance: 0.5588 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md, guide_kestrelford.md, guide_walking.md

```
Based on the "Difficult" section of the document, the three least approachable towns from an accessibility standpoint are Kestrelford, Halden Bay, and Corry Vale (along with Elder Ness, which is also listed in that section). 

Source: guide_accessibility.md
```

### What are the three least approachable towns from an accessibility standpoint? — run 3

- Best distance: 0.5588 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md, guide_kestrelford.md, guide_walking.md

```
Based on the "Difficult" section of the document, the three least approachable towns from an accessibility standpoint are Kestrelford, Halden Bay, Corry Vale, and Elder Ness (the document lists four towns under this heading). 

Source: guide_accessibility.md
```

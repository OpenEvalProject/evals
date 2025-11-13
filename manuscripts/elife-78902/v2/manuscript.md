# A timer gene network is spatially regulated by the terminal system in the Drosophila embryo

## Authors

- Erik Clark<sup>1</sup> ([ORCID: 0000-0002-5588-796X](https://orcid.org/0000-0002-5588-796X)) †
- Margherita Battistara<sup>1</sup>
- Matthew A Benton<sup>1</sup> ([ORCID: 0000-0001-7953-0765](https://orcid.org/0000-0001-7953-0765)) †

### Affiliations

1. Department of Zoology, University of Cambridge Cambridge United Kingdom ([ROR:013meh722](https://ror.org/013meh722))
2. Department of Systems Biology, Harvard Medical School Boston United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
3. Department of Genetics, University of Cambridge Cambridge United Kingdom ([ROR:013meh722](https://ror.org/013meh722))
4. Department of Physiology, Development and Neuroscience, University of Cambridge Cambridge United Kingdom ([ROR:013meh722](https://ror.org/013meh722))
5. Developmental Biology Unit, EMBL Heidelberg Germany ([ROR:03mstc592](https://ror.org/03mstc592))

† Corresponding author

## Abstract

In insect embryos, anteroposterior patterning is coordinated by the sequential expression of the ‘timer’ genes caudal, Dichaete, and odd-paired, whose expression dynamics correlate with the mode of segmentation. In Drosophila, the timer genes are expressed broadly across much of the blastoderm, which segments simultaneously, but their expression is delayed in a small ‘tail’ region, just anterior to the hindgut, which segments during germband extension. Specification of the tail and the hindgut depends on the terminal gap gene tailless, but beyond this the regulation of the timer genes is poorly understood. We used a combination of multiplexed imaging, mutant analysis, and gene network modelling to resolve the regulation of the timer genes, identifying 11 new regulatory interactions and clarifying the mechanism of posterior terminal patterning. We propose that a dynamic Tailless expression gradient modulates the intrinsic dynamics of a timer gene cross-regulatory module, delineating the tail region and delaying its developmental maturation.

## Introduction

Insect segments are patterned by a relatively conserved gene regulatory network, including gap genes, pair-rule genes, and segment-polarity genes (reviewed in Nasiadka et al., 2002; Hughes and Kaufman, 2002; Clark et al., 2019). Within and across species, embryonic development depends on these network components being activated at the right times and in the right places. Locally, the maturation of any given segment involves segmentation genes being activated in a conserved temporal sequence (e.g., primary pair-rule genes before secondary pair-rule genes and segment-polarity genes; Akam, 1987; Baumgartner and Noll, 1990; Schroeder et al., 2011; Clark and Akam, 2016). Globally, the relative timing of segmentation across the anteroposterior (AP) axis correlates with the specific developmental mode of each species, ranging from predominantly sequential, germband-based patterning in the cricket Gryllus bimaculatus or the beetle Tribolium castaneum, to more or less simultaneous, blastoderm-based patterning in the fruit fly Drosophila melanogaster (reviewed in Davis and Patel, 2002).

Previously, we have proposed that segment patterning is coordinated by an underlying framework of ‘timer gene’ (alternatively, ‘timing factor’) expression, which broadly regulates segmentation gene expression in time and space (Clark and Peel, 2018; Clark et al., 2019). We identified the timer genes (not necessarily exhaustively) as caudal (cad; Mlodzik et al., 1985; Macdonald and Struhl, 1986), Dichaete (D; Russell et al., 1996; Nambu and Nambu, 1996), and odd-paired (opa; Benedyk et al., 1994), all of which code for transcription factors. The expression dynamics of these genes correlate with the progression of segmentation: in Drosophila, they are expressed sequentially within the blastoderm, while in Tribolium the same expression sequence occurs in cells emerging from the segment addition zone into the segmented germ band (Schulz et al., 1998; Copf et al., 2004; El Sherif et al., 2014; Clark and Peel, 2018). In addition, the protein products of these genes are known to directly regulate many segmentation genes in Drosophila (Rivera-Pomar et al., 1995; Schulz and Tautz, 1995; La Rosée et al., 1997; Häder et al., 1998; Ma et al., 1998; Clark and Akam, 2016; Vincent et al., 2018; Soluri et al., 2020; Koromila et al., 2020).

However, we currently do not understand how the timer genes themselves are spatiotemporally regulated within the embryo. What accounts for their local sequential activation in segmenting tissues, and why are these dynamics so deeply conserved across species? How is their expression globally regulated along the AP axis, and why is this regulation so evolutionarily flexible?

Here, we investigate these issues in the Drosophila embryo, exploiting the fact that segmentation in this model species is not quite so simultaneous as it is often described. Although most of the Drosophila blastoderm is patterned simultaneously before gastrulation, the most posterior part of the segmental ectoderm is not patterned until germband extension (Kuhn et al., 2000). This ‘tail’ region (see Box 1) is located posterior to abdominal segment 8 (A8) and anterior to the prospective hindgut, and eventually gives rise to a set of ectodermal structures known as the embryonic terminalia (Turner and Mahowald, 1979; Sato and Denell, 1986; Jürgens, 1987). Consistent with the timer gene hypothesis, the tail exhibits cad, D, and opa expression dynamics which differ from those in the rest of the trunk (Macdonald and Struhl, 1986; Russell et al., 1996; Clark and Akam, 2016; Clark and Peel, 2018), correlating with the difference in segmentation dynamics.

![Figure 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig1-v2.jpg)

**Figure 1.:** (A) wg and en expression from gastrulation to extended germband. Left column shows merged maximum projections of wg, en, and DAPI (nuclei). Middle column shows merged wg and en expression, either maximum projections (stage 6, stage 11.2), or sagittal sections (stage 8.1 to stage 11.1). Enlarged close-ups of the boxed regions are shown in the right column. Key expression domains are annotated with labels; newly established domains are shown in large font; wgpost = wg posterior domain. Stages 6–11.1 show lateral views, stage 11.2 is a ‘dorsal’ view that actually mainly shows the ventral side of the posterior germband due to germband extension. (B) slp1 (slp) and eve expression during the division of mitotic domain 4 (stage 8.1) and at extended germband (stage 11.1). Both stages show dorsolateral views. Left column shows a merge with DAPI (nuclei); right column shows gene expression alone. Enlarged close-ups of the boxed regions are shown below the whole embryo views; see Appendix 2: ‘Embryo images’ for details of how the close-up for stage 11.1 was re-sliced. Key expression domains are annotated with labels. (C) Schematic diagram showing the expression of key segmentation genes before tail segmentation (stage 6) and after tail segmentation (stage 11). The tail region is shaded in grey; note the expansion of the region due to morphogenesis, and the refinement of the cad domain. PSB16 is shown as a dotted line due to its vestigial nature; en16 is also depicted as narrower than the other domains. Lighter shading for eve domains represents weaker or decaying expression. C1-3, gnathal segments; T1-3, thoracic segments; A1-10, abdominal segments; Ma, mandibular segment; Mx, maxillary segment; Lb, labial segment. All embryos are anterior left, dorsal up. Scale bars = 50 μm; grey lines show embryo outlines.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Individual wg, en, and DAPI (nuclei) channels from the two-channel and three-channel merges shown in Figure 1A, plus two additional embryos (stage 5.2 and stage 5.4) showing wg and en expression at earlier stages. (B) Individual slp, eve, and DAPI (nuclei) channels from the two-channel and three-channel merges shown in Figure 1B. Embryo orientations as described for Figure 1. Scale bars = 50 μm; grey lines show embryo outlines.

The patterning of the tail region is dependent on the posterior terminal system (reviewed in Perkins and Perrimon, 1991), and, in particular, on its downstream effector, Tailless (Tll; Strecker et al., 1986; Pignoni et al., 1990). Tll has well-characterised effects on gap gene expression (Jaeger, 2011; Janssens et al., 2013), but its contribution to timer gene regulation is relatively unexplored. As a consequence, the specific regulatory interactions that mediate tail patterning remain unknown (Casanova, 1990; Wu and Lengyel, 1998; Smits and Shvartsman, 2020).

In this study, we discover that Drosophila timer gene expression is shaped by a combination of cross-regulatory interactions and extrinsic spatiotemporal inputs. Using multiplexed hybridisation chain reaction in situ hybridisation (HCR ISH; Choi et al., 2016; Trivedi et al., 2018; Choi et al., 2018), we first show that the tail region gives rise to two sets of parasegment-like boundaries after gastrulation, clarifying its segmental nature. We then characterise timer gene expression in wild-type embryos, timer gene mutants, and terminal system mutants, uncovering 11 new regulatory interactions within the Drosophila AP patterning network. Using a simple logical model, we show that the revised network both explains wild-type patterning dynamics and recapitulates the mutant phenotypes we examined. We conclude by discussing which aspects of timer gene regulation are likely to be conserved or divergent across species.

## Results

### Two parasegment-like boundaries form sequentially from the Drosophila tail region after gastrulation

The Drosophila embryo is well-known for its simultaneous mode of segmentation, in which a segmental pattern is laid down at the end of the blastoderm stage, prior to significant morphogenetic movements. Fourteen prospective parasegment boundaries appear at this stage, marked by segmental stripes of segment-polarity gene expression (DiNardo et al., 1985; Baumgartner et al., 1987; Baker, 1988; Lee et al., 1992; Grossniklaus et al., 1992).

Sandwiched in between parasegment boundary 14 (PSB14; see Box 1) and the broad posterior domain of wg (thought to correspond to prospective hindgut; Baker, 1988) are about four cell rows of ectoderm that remain unpatterned by segment-polarity genes at the end of the blastoderm stage (Figure 1A, stage 6). This ‘tail’ region (see Box 1) goes on to form the most terminal structures of the larva (Turner and Mahowald, 1979; Jürgens, 1987), including a 15th parasegment boundary (Kuhn et al., 1995; Kuhn et al., 2000), various sensory organs (Sato and Denell, 1986; Jürgens, 1987; Kuhn et al., 1992), and the anal pads (external organs involved in ion transport; Jarial, 1987).

The segmental nature of the tail is unclear. The tissue just posterior to PSB15 is abdominal segment 10 (A10; Figure 1C). Some authors consider the region to contain a cryptic 11th abdominal segment as well (Jürgens, 1987; Baumgartner et al., 1987), but most do not (see Discussion: ‘The segmental character of the Drosophila tail’) and, to the best of our knowledge, a 16th parasegment boundary has not been described. To investigate this issue, we used multiplexed HCR ISH to re-examine the expression of the parasegment boundary markers wingless (wg; Baker, 1987; Rijsewijk et al., 1987), engrailed (en; Kornberg et al., 1985; Fjose et al., 1985), sloppy-paired (slp; Grossniklaus et al., 1992), and even-skipped (eve; Macdonald et al., 1986) during germband extension and extended germband stages (Figure 1; Figure 1—figure supplement 1).

#### wg and en expression in the tail

The wg and en stripes associated with PSB15 emerge during germband extension (Figure 1A, stages 8.3–8.4). In contrast to published descriptions of wg expression (Baker, 1987; Baker, 1988), we identified an additional wg stripe, wg15, which appeared after germband extension (Figure 1A, stage 11.1). During subsequent development, a medial patch of en expression appeared posteriorly adjacent to wg15 (Figure 1A, stage 11.2). This ‘en16’ domain is clearly not a full stripe as found in parasegment boundaries 1–15. However, the domain marks the median neuroblast lineage of abdominal segment 10 (Birkholz et al., 2013), and median neuroblasts always originate from posterior segment compartments (Bate, 1976; Doe, 1992; Biffar and Stollewerk, 2014). wg15 and en16 therefore seem to correspond to a vestigial 16th parasegment boundary within the Drosophila embryo (Figure 1C).

#### slp and eve expression in the tail

In the simultaneously segmenting region of the embryo (here, termed the ‘trunk’), segment-polarity domains are initially patterned by stripes of pair-rule gene expression (DiNardo and O’Farrell, 1987; Jaynes and Fujioka, 2004; Clark, 2017). In the tail, PSB15 is prefigured by pair-rule gene stripes slp14 and eve15, which appear after gastrulation (Macdonald et al., 1986; Grossniklaus et al., 1992; Kuhn et al., 2000). We found that slp14 and eve15 emerged simultaneously early in germband extension (Figure 1B, stage 8.1), at around the same time as the polarised cell divisions of mitotic domain 4 (Foe, 1989; da Silva and Vincent, 2007). At the end of germband extension, we were surprised to find that an additional set of abutting slp and eve stripes, slp15 and eve16, emerged posterior to PSB15 (Figure 1B, stage 11.1), in the same region as wg15 and en16. This finding supports our conclusion that wg15 and en16 are segmental in nature.

To the best of our knowledge, the slp15 domain has not been described previously. Persistent eve expression at the posterior of the embryo is well-known, although it has been described as a remnant of eve15 (Macdonald et al., 1986; Frasch et al., 1987; Sackerson et al., 1999; Kuhn et al., 2000) or the 7th eve pair-rule stripe (Singer et al., 1996) rather than a separate domain. (Note that eve15 is described by some authors [e.g., Sackerson et al., 1999] as the 8th stripe of eve, not counting the seven ‘minor’ eve stripes that appear at even-numbered parasegment boundaries just before gastrulation).

#### Summary

We propose that two parasegment-like boundaries form sequentially from the tail region of the Drosophila embryo after gastrulation (Figure 1C). In both cases, segment-polarity gene expression is preceded by a template of abutting slp and eve expression, similar to the odd-numbered parasegment boundaries of the trunk (Lawrence et al., 1987; Cadigan et al., 1994). Unlike in the trunk, however, the resolved segmental eve stripes appear de novo and are not preceded by a pair-rule phase of expression.

### Timer gene expression differs between the trunk and the tail

Given that Drosophila shows distinct segmentation dynamics in the trunk and the tail, we examined the expression of the timer genes (cad, D, and opa) in these regions during blastoderm stages and early germband extension (for an earlier survey using an inferior in situ hybridisation method, see Clark and Peel, 2018). To account for the movement of nuclei/cells during blastoderm (Keränen et al., 2006) and gastrulation stages, we co-stained the timer genes with wg and used the posterior wg domain as a fiducial marker. (The posterior wg domain appears to be stable relative to nuclei, as nuclear transcription foci are not offset anteriorly or posteriorly relative to cytoplasmic transcripts.) To aid with fine-scale staging of embryos, we have divided stage 5, which lasts ∼40 min at 25° C, into five timeclasses based on gene expression and morphology (see Appendix 1).

#### Timer gene expression in the trunk

In the trunk, cad, D, and opa transcripts are expressed sequentially over stages 4–6; first cad, then D, then opa (Figure 2; Figure 2—figure supplement 2). Despite some AP intensity modulation (presumably downstream of gap and pair-rule genes), similar temporal dynamics are present across the whole trunk region, consistent with its simultaneous mode of segmentation. cad, which is maternally deposited and then zygotically expressed, clears from the trunk by stage 5.4 (Levine et al., 1985; Mlodzik et al., 1985; Hoey et al., 1986; Macdonald and Struhl, 1986; Mlodzik and Gehring, 1987a; Schulz and Tautz, 1995). D, which is detectable from stage 4.1 (nuclear cycle 10), reaches appreciable levels at stage 4.4 (nuclear cycle 13), rapidly reaches a very high peak at stage 5.2, then declines sharply, with residual expression clearing by stage 6, replaced ventrally by persistent expression in the neuroectoderm (Russell et al., 1996; Nambu and Nambu, 1996). Finally, opa appears at stage 5.1, rapidly builds to high levels, then tapers off during germband extension (Benedyk et al., 1994; Clark and Akam, 2016).

![Figure 2.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig2-v2.jpg)

**Figure 2.:** Column 1 shows a two-channel wg and DAPI (nuclei) merge for embryos of gradually increasing age; columns 2–4 show cad, D, and opa channels from the same embryos; column 5 shows a three-channel cad/D/opa merge. The plots at the right show quantitative expression traces (67.5–97.5% AP axis; all measurements from the anterior pole) for all four genes, extracted from the embryos pictured to the left. The stage 4.3, stage 4.4, and stage 5.1 embryos are from a different scanning session compared to the rest of the figure. All embryos are anterior left, dorsal up. Stages 4.3–6 show lateral views; stage 8.2 is dorsolateral. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Individual DAPI (nuclei) and wg channels from the two-channel merges shown in the leftmost column of Figure 2. All embryos are anterior left, dorsal up. Stages 4.3–6 show lateral views, stage 8.2 is a dorsolateral view. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Timer gene expression and DAPI (nuclei) staining in young wild-type embryos; note the weak, patchy D expression at stage 4.2. All embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** As the D antibody gave high background staining in the yolk, the D protein channel shows a mean z-projection of a thin 3D ‘shell’ tracking the embryo surface (see Appendix 2—figure 1F–H), which significantly improved the signal:background ratio. All embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A–C) Quantitative expression traces (0–100% AP axis) from individual embryos of different ages, to convey the spatiotemporal dynamics of timer gene expression within the early embryo. The line colour of a given stage is the same across all plots (see legend at bottom left of figure). All traces in a given plot are from embryos from the same tube, imaged with the same microscope settings in the same imaging session. (A) Expression traces from a wg/cad/opa/D HCR (see example source embryos in Figure 2). (B) Expression traces from a wg/cad-Intron/opa/Opa combined HCR and antibody stain (see example source embryos in Figure 3). (C) Expression traces from a D antibody stain (see example source embryos in Figure 2—figure supplement 3). (D) A rough approximation of timer gene expression dynamics at 50–60% AP axis, using normalised intensity measurements from the traces in (A) (cad, D and opa transcripts), (B) (Opa protein), (C) (D protein), and Figure 2B from Surkova et al., 2008 (Cad protein). Note the transcript/protein time lags for expression peaks and troughs.

Cad, D, and Opa protein dynamics broadly match their respective transcript dynamics, albeit with time-lags for synthesis and decay (Figure 2—figure supplement 3; Figure 2—figure supplement 4). Cad levels decrease steadily in the trunk over stage 5 (see Figure 2B in Surkova et al., 2008). D levels rise and fall gradually from stage 4.4 to stage 6, peaking at mid stage 5 (Figure 2—figure supplement 3; Figure 2—figure supplement 4C). Finally, Opa levels increase throughout stage 5 and into stage 6 (Figure 2—figure supplement 4B; see also the live quantification of llama-tagged Opa in Soluri et al., 2020). Segmentation stages in the trunk are therefore characterised temporally by decreasing Cad levels, increasing Opa levels, and a pulse of D expression in between (Figure 2—figure supplement 4D).

#### Timer gene expression in the tail

In the tail, a similar cad/D/opa expression sequence is evident, but delayed with respect to the trunk (Figure 2). cad is expressed continuously in the tail region throughout stage 5 and into germband extension. In contrast, D and opa expression in the tail region remains either low (D) or absent (opa) through most of stage 5. At stage 5.4, a D tail domain emerges within the lateral part of the cad tail domain, rapidly strengthening and extending dorsoventrally. D protein becomes prominent in the tail domain at stage 6 (Figure 2—figure supplement 3; Figure 2—figure supplement 4C), again reflecting a modest time-lag for protein synthesis. Finally, opa expression expands into the tail region from late stage 5 (described below).

High-resolution close-ups of nascent transcripts, mature transcripts, and synthesised protein (Figure 3; Figure 3—figure supplement 1) reveal subtle posterior shifts. The cad tail domain is mostly anterior to the wg posterior domain, with an overlap of a single cell row (Figure 3A, cad/wg merge). At stage 5.4, cad is actively transcribed in a domain 3–4 cells wide, but this shrinks to 2–3 cells wide by stage 6, with transcription ceasing at the anterior edge (cad intronic probe, Figure 3B). Throughout this period, the domain of active opa transcription, marked by prominent intranuclear foci, extends about one cell row posterior to the Opa protein domain (Figure 3B, Opa/opa merge), and also overlaps the cad domain by about one cell row (Figure 3A, cad/opa merge; Figure 3B, opa/cad-Intron merge). This suggests that opa transcription gradually invades the cad tail domain from the anterior edge, with cad transcription then ceasing in these cells as Opa levels increase (Figure 3B, Opa/cad-intron merge). Supporting this interpretation, we confirmed that a posterior expansion of Opa expression is evident in published live-imaging data (Soluri et al., 2020).

![Figure 3.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig3-v2.jpg)

**Figure 3.:** (A, B) Leftmost column shows the posterior ends of the selected embryos, each with a boxed region of interest in the tail; middle columns show high-resolution close-ups of the boxed region without and with DAPI signal (‘-nuclei’ vs. ‘+nuclei’); rightmost column shows quantitative expression traces along the x-axis of the boxed region. (A) Timer gene expression, as in Figure 2. (B) wg and opa expression (as in A), combined with a cad intronic probe (cad-Intron, showing intranuclear transcription foci) and an antibody stain for Opa protein. Solid lines in the expression plots show the average intensity of wg, opa, and Opa protein; dashed lines show the normalised density of cad and opa transcription foci. Note the staggered AP distributions of Opa protein, opa transcript, and opa transcription foci, the shrinking gap between the posterior wg domain and the opa/Opa signal, and the refinement of the cad-Intron domain over time. All embryos are anterior left, dorsal up, lateral view. Scale bars = 50 μm (embryo posteriors), 20 μm (boxed close-ups). For the high-resolution close-ups, the curvature of the tissue was straightened prior to z-projection.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Individual channels from the two-channel and multi-channel merges shown in Figure 3. All embryos are anterior left, dorsal up, lateral view. Scale bars = 50 μm (embryo posteriors) or 20 μm (boxed close-ups); grey lines show embryo outlines.

#### Summary

We find that timer gene expression differs sharply between the trunk and the tail, although both regions express cad, D, and opa in the same temporal sequence. The difference in timer gene expression between the trunk and the tail correlates with the difference in simultaneous versus sequential segmentation dynamics described above.

### The timer genes are patterned by cross-regulation

The relative spatiotemporal expression dynamics of the timer genes are suggestive of cross-regulation. To investigate this possibility, we examined timer gene expression in opa-, D-, and cad- mutants (Figure 4; Figure 4—figure supplement 1) and discovered a variety of cross-regulatory effects. As cad is expressed maternally as well as zygotically, we examined cad maternal mutants (cadm-z+) and cad zygotic mutants (cadm+z-) in addition to cad null mutants (cadm-z-) in order to disentangle maternal and zygotic effects (Figure 4—figure supplement 3). We also examined timer gene expression in wg- mutants, but did not observe any aberrant expression in these embryos during our stages of interest (Figure 4—figure supplement 4).

![Figure 4.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig4-v2.jpg)

**Figure 4.:** (A) Timer gene expression in wild-type, opa- mutants, D- mutants, and cadm-z- mutants at stage 5.5. The leftmost column shows a four-channel merge and the other columns show individual channels. In the cadm-z- embryo, note the absence of the wg posterior domain (arrowhead in wg channel), the dorsal loss of the D tail domain (arrowhead in D channel), and the AP modulation of the opa trunk domain (arrowheads in opa channel). The brightness and contrast of the D channel were adjusted for the D- embryo to reveal the very weak residual signal. (B) Quantitative expression traces (67.5–97.5% AP axis) from the individual embryos in (A) (multi-channel traces in leftmost column) or multiple stage 5.5 embryos (single-channel traces in other columns). All traces are individually normalised; mutant traces are overlaid on wild-type traces (grey) for ease of comparison. (C) cad and D expression in wild-type and cadm-z- mutant embryos of gradually increasing age; leftmost columns show a two-channel merge. In the cadm-z- embryos, note that cad transcript takes longer to clear from the trunk, while D is initially expressed at lower intensity and its neuroectodermal expression domain emerges earlier. All embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A, B) Plots showing quantitative expression traces (67.5–97.5% AP axis) from multiple stage 5.5 embryos, individually normalised to the range 0–1. Leftmost column shows traces from wild-type embryos (coloured lines); remaining columns show traces from cadm-z-, D- or opa- mutants (coloured lines) overlaid on the same wild-type traces shown in the leftmost column (grey lines). (A) Traces without any alignment step; locations of borders/domains represent their absolute position along the AP axis. Note the loss of the wg posterior domain in cadm-z- mutants, the slight anterior shift and expansion of the fate map in D- mutants, and the stronger D tail domain in opa- mutants. (B) All traces have been aligned with each other so that the cad posterior border from each embryo lines up with the others. Note the broadened cad domain in D- mutants and the broadened D tail domain in opa- mutants. Note also the slightly increased distance between opa and wg in D- mutants. Source data is the same as Figure 4.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Plots showing quantitative expression traces (0–100% AP axis) from multiple stage 5.5 embryos, individually normalised to the range 0–1. Top-left plot shows opa expression in wild-type embryos (orange lines); other plots show opa expression from cadm-z-, D-, or opa- mutants (orange lines) overlaid on the same wild-type traces shown in the top-left plot (grey lines). Note the marked AP modulation of opa expression in the cadm-z- mutants, and the anteriorly shifted position of the opa posterior border in D- mutants. Source data is the same as Figure 4.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) wg, D, and msh expression in wild-type and cadm-z- mutants. Transmitted light images of a sagittal section through the dorsal membrane surface (used for embryo staging) are shown at top right; black arrowheads mark the invagination of the plasma membrane. Note the early/ectopic expression of msh in the cadm-z- mutants, especially in the posterior of the embryo. (B) wg, cad, and D expression in wild-type and cadm+z- (zygotic) mutants. Note the normal D expression in the cadm+z- mutant at stage 6 but the absence of the D tail domain in the cadm+z- mutant at stage 8 (white arrowheads). (C) wg, cad, and D expression in a cadm-z- mutant (top) compared to a paternally rescued cadm-z+ mutant (bottom, note the lacZ expression in the head from the hb-lacZ marked balancer). Note that the D tail domain is rescued in the cadm-z+ mutant (white arrowheads). The posterior wg expression domain is also partially rescued (white arrows), as is the segmental pattern. cad and D expression resembles the cadm-z- mutant. All embryos are anterior left, dorsal up. All embryos except the dorsolateral stage 8 wild-type embryo in (B) are lateral views. Scale bars = 50 μm (whole embryos) or 20 μm (membrane close-ups); grey lines show embryo outlines.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Left column shows a multi-channel merge; other columns show individual channels. (Note that the wg- embryo pictured is slightly younger than the wild-type embryo and so does not show the same pattern of weak pair-rule cad stripes in the trunk. Older wg- embryos express these stripes as normal.) Both embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** Individual cad, D, and opa channels are shown for each genotype, as well as two-channel merges with wg. Multi-channel merges with and without the DAPI (nuclei) channel are also shown in the left column. White arrowheads point to the D tail domain – note that it is expanded in the opa- mutant, absent in the tll- mutant, and ‘rescued’ (though posteriorly shifted) in the tll- opa- mutant. Note also that the cad tail domain is slightly broader than normal at this stage in the opa- mutant, weak/fading in the tll- mutant, and partially rescued (though again, posteriorly shifted) in the tll- opa- mutant. All embryos are anterior left, dorsal up, lateral or ventrolateral views. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig4-figsupp6-v2.jpg)

**Figure 4—figure supplement 6.:** (A) DAPI (nuclei) staining from a wild-type vs. a cadm-z- embryo. The cadm-z- embryo is bigger and broader in the xy maximum projection, and shows a dimple in the surface in the xy (frontal) and zy (transverse) sections. (B) Scatter plot showing the AP (x-axis) and DV (y-axis) lengths of the embryo masks for n=78 wild-type embryos and n=73 cadm-z- embryos; note that the cadm-z- measurements are on average larger, particularly in DV. (C) Violin plots comparing the AP length, DV length, and fineness ratio (AP length/DV length) for the embryos in (B). The rightmost violin plot compares the thickness in the z-axis (top surface of the embryo to mid-yolk) for a separate set of n=29 wild-type embryos and n=29 cadm-z- embryos. Horizontal lines on the violin plots mark minimum, mean, and maximum values. Measurements were taken from embryos sourced from a variety of different imaging sessions and there should be no systematic differences in mounting technique. The means of all measurements shown in the violin plots are significantly different (two-tailed t-test). AP length: wild-type mean 503.5 μm, cadm-z- mean 512.3 μm; t=−3.12, p=0.002. DV length: wild-type mean 217.9 μm, cadm-z- mean 244.8 μm; t=−9.76, p=1.0x10−17. Fineness ratio: wild-type mean 2.32, cadm-z- mean 2.10; t=8.11, p=1.7x10−13. Thickness in z: wild-type mean 72.8 μm, cadm-z- mean 65.0 μm; t=3.27, p=0.002. Scale bar = 50 μm.

#### Timer gene expression in opa- mutants

In opa- mutants, trunk expression of D persisted longer than usual, resulting in a more prominent stripy pair-rule pattern, while the tail domain was stronger and extended further anterior than normal (Figure 4A and B; Figure 4—figure supplement 1B; Figure 4—figure supplement 5). The cad tail domain looked similar to wild-type at stage 5.5 (Figure 4A and B; Figure 4—figure supplement 1B), but was broader at stage 6 (Figure 4—figure supplement 5), suggesting that it failed to retract posteriorly as in wild-type. opa transcription and the posterior wg domain looked normal.

#### Timer gene expression in D- mutants

In D- mutants, cad expression persisted abnormally in the trunk, with marked AP modulation, and the cad tail domain extended further anterior than normal (Figure 4A–C; Figure 4—figure supplement 1B). The D allele we used had very low transcript levels (presumably due to nonsense-mediated decay, S. Russell pers. comm.), but the residual expression indicated that both the clearance of D expression from the trunk and the appearance of the D tail domain may have been delayed. The posterior wg domain, the posterior border of the cad tail domain, and the posterior border of the opa domain were all modestly anteriorly shifted relative to wild-type (Figure 4B; Figure 4—figure supplement 1A; Figure 4—figure supplement 2); even after allowing for this shift, the gap between the wg domain and the opa domain was slightly larger in D- embryos than in wild-type (Figure 4—figure supplement 1B).

#### Timer gene expression in cadm-z- mutants

In cadm-z- mutants, cad expression persisted abnormally in the trunk (Figure 4A–C), though without the AP modulation seen in D- mutants. D expression levels were weaker than normal at early stage 5 (Figure 4C, stage 5.2), the D neuroectodermal expression domain appeared precociously (Figure 4C, stage 5.4), and the D tail domain was only expressed in the ventral half of the embryo (arrowhead in Figure 4A). The posterior wg domain was generally absent (arrowhead in Figure 4A; Wu and Lengyel, 1998), although weak expression was observed in some embryos, consistent with the variability of the cadm-z- larval phenotype (Macdonald and Struhl, 1986). The opa domain showed strong pair-rule modulation in the anterior trunk (arrowheads in Figure 4A; Figure 4—figure supplement 2).

#### Timer gene expression in cadm+z- and cadm-z+ mutants

One copy of maternal cad (cadm+z- embryos) largely rescued the cadm-z- phenotype, except that the D tail domain was lost prematurely, during germband extension (Figure 4—figure supplement 3B). The posterior wg domain was present, conflicting with a previous report (Wu and Lengyel, 1998).

One copy of zygotic cad (cadm-z+ embryos) rescued the D tail domain fully and partially rescued the wg posterior domain (Figure 4—figure supplement 3C), but the blastoderm dynamics of D and cad expression were still perturbed.

#### Other observations from cadm-z- mutants

We wondered whether the premature neuroectodermal expression of D in cadm-z- mutants might indicate a more general pattern of precocious neuroectoderm development. To investigate this, we examined the expression of muscle segment homeobox (msh, also known as Drop; Lord et al., 1995), a key neuroectoderm patterning gene expressed outside the D neuroectodermal domain. We found that msh was also expressed prematurely in cadm-z- mutants, particularly in posterior parts of the embryo (Figure 4—figure supplement 3A).

Fixed and mounted cadm-z- embryos had a different range of shapes and sizes compared to wild-type embryos (Figure 4—figure supplement 6). We did not investigate whether this was specifically due to the loss of Cad expression or an artefact of the ‘FLP-DFS’ technique for generating germline clones (Chou and Perrimon, 1996). Given the robustness of AP patterning to variation in embryonic geometry (Huang et al., 2020), this minor morphological effect is unlikely to be the cause of the gene expression changes we observed.

#### Summary

Our investigation of timer gene mutant phenotypes provides strong evidence for timer gene cross-regulation. cad is derepressed in D- mutants, and D is derepressed in opa- mutants. cadm-z- embryos have a complex phenotype in which the early expression of D is reduced, neuroectodermal gene expression is activated prematurely, the posterior wg domain is lost, and the D tail domain fails to activate dorsally. Finally, opa expression is fairly normal across all the mutants, except that its posterior border is anteriorly shifted in D- mutants.

These phenotypes, in combination with the expression dynamics described in the previous section, suggest that Opa represses D and cad, D represses cad, and Cad activates D (see Appendix 3—table 1 for detailed reasoning). In addition, Cad is required for the expression of posterior wg, and D has a modest but concerted effect on the entire posterior fate map. Finally, most of the cadm-z- phenotype is mediated by maternal Cad, but zygotic Cad has specific late effects on D in the tail.

### Tll and Hkb expression dynamics correlate with timer gene patterning in the posterior of the embryo

We next wanted to understand why timer gene expression differs between the trunk, tail, and prospective gut regions; i.e., how the timer gene network is spatially regulated. We therefore examined how timer gene expression relates to the expression domains of the zygotic terminal system genes tll (Jurgens et al., 1984; Strecker et al., 1986; Pignoni et al., 1990) and huckebein (hkb; Weigel et al., 1990; Brönner and Jäckle, 1991), the obvious candidates for providing this spatial information.

#### tll and hkb expression dynamics

tll and hkb, which both code for repressive transcription factors, are expressed in nested domains at the posterior pole, with tll expression extending further from the pole than hkb expression (Figure 5; Figure 5—figure supplement 1; Pignoni et al., 1990; Brönner and Jäckle, 1991). tll is transcribed at low levels from as early as nuclear cycle 9 (Pignoni et al., 1992), and we detected similar early transcription for hkb. Transcript levels in both domains peak at around stage 5.2 and then decline, with tll expression fading by stage 6 and hkb persisting at low levels after gastrulation (Figure 5; Figure 5—figure supplement 1; Figure 5—figure supplement 3). Previous studies (Pignoni et al., 1990; Pignoni et al., 1992) reported retraction of the tll border by about 5% egg length between stage 4.4 (nuclear cycle 13) and stage 5 (nuclear cycle 14); we noticed that this border also retracts by about 3–4 nuclear diameters over the course of stage 5 (Figure 5—source data 2). (Note that the absolute [% AP axis] shifts in Figure 5—figure supplement 3 appear smaller than this because the posterior retraction of gene expression across nuclei is partially cancelled out by the anterior flow of nuclei away from the pole; Keränen et al., 2006.)

![Figure 5.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig5-v2.jpg)

**Figure 5.:** (A, B) Timer and terminal gene expression in embryos of increasing age; only the posterior end of each embryo is shown. Left four columns show either three-channel or two-channel merges; right column shows quantitative expression traces (67.5–97.5% AP axis) of all four genes in the stain. (A) Timer gene expression relative to tll; note the posterior regression and changing intensity of the tll domain and the different spatial relationships with opa, D, and cad. (B) cad and wg expression relative to hkb and tll; note how the posterior wg domain emerges within the tll-positive gap that opens up between cad and hkb. All embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The adjusted (‘adj.’) images for the stage 2–4.3 embryos have altered brightness and contrast to better show the early expression of tll and hkb. All embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Individual channels from the two-channel and three-channel merges shown in Figure 5. All embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A, B) Quantitative expression traces (0–100% AP axis) from individual embryos of different ages, to convey the spatiotemporal dynamics of gene expression within the early embryo. All traces in a given plot are from embryos from the same tube imaged with the same microscope settings in the same imaging session. The stage corresponding to each line colour is shown in the legends below the plots (colours are consistent between plots). (A) Expression traces from a tll/cad/D/opa HCR (see example source embryos in Figure 5A). Note the posterior retraction of the tll boundary between stages as well as the rise and fall in tll expression levels. (B) Expression traces from a tll/cad/wg/hkb HCR (see example source embryos in Figure 5B). Note the greater posterior retraction of the tll border compared to hkb, and the more pronounced fall in expression levels over stage 5.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** (A, B) Quantitative expression traces (0–100% AP axis) from individual embryos of different ages, to convey the relative expression (A) or spatiotemporal dynamics (B) of gene expression within the early embryo (an example source embryo is shown in Figure 5—figure supplement 6A). All traces in a given plot are from embryos from the same tube imaged in the same imaging session with the same microscope settings. Legends for gene products (A) or embryo stages (B) are shown below the plots. (A) tll/Tll/eve traces from individual embryos of different ages; note the time lag for Tll protein levels compared to tll transcript, as well as the relative positions of their posterior domain borders at stages 5.4 and 5.5. (B) the same data as in (A), except that plots are grouped by gene product rather than by embryo. Note the different temporal dynamics of Tll protein compared to tll transcript, and the posterior retraction of both posterior domain borders. The eve channel was used for embryo staging; note that the stripes in older embryos are more refined and have shifted anteriorly across the blastoderm.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** (A, B) Quantitative expression traces (0–100% AP axis) from individual embryos of different ages, to convey the relative expression (A) or spatiotemporal dynamics (B) of Hkb, Tll, and Opa protein expression within the early embryo (an example source embryo is shown in Figure 5—figure supplement 6B). All traces in a given plot are from embryos from the same tube imaged in the same imaging session with the same microscope settings. Legends for gene products (A) or embryo stages (B) are shown below the plots. (A) Hkb/Tll/Opa expression from individual embryos of different ages; note the nested domain of Tll and Hkb and the correlation between the Tll and Opa borders. (B) The same data as in (A), except that plots are grouped by protein rather than by embryo. In all plots, the Opa channel has been linearly unmixed from the Hkb channel to remove bleedthrough signal from Hkb in the poles of the embryo.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig5-figsupp6-v2.jpg)

**Figure 5—figure supplement 6.:** (A, B) Examples of individual embryos from the imaging datasets used to extract the expression traces shown in Figure 5—figure supplement 4 (A) and Figure 5—figure supplement 5 (B). (A) Tll antibody/tll HCR/eve HCR. (B) Tll/Hkb/Opa antibody stain. Both embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines.

Tll and Hkb protein dynamics (Figure 5—figure supplement 4; Figure 5—figure supplement 5) are spatiotemporally similar to tll/hkb transcript dynamics, albeit with a slight time lag, with the Tll protein border therefore lying slightly anterior to the tll transcript border during the second half of stage 5 (Figure 5—figure supplement 4A). Our Tll antibody data closely resembles that collected by the Reinitz group, who noted that “in contrast to the posterior domains of the other gap genes, the [Tll] posterior domain does not shift position with time” (Surkova et al., 2008). We interpret the same data as providing evidence for a modest posterior retraction of the Tll domain over time, which does indeed contrast with the anterior shifts of the trunk gap genes, and is partially masked by anterior nuclear flow.

#### tll and hkb expression dynamics relative to the timer genes

The tll and hkb anterior borders correlate closely with the resolving expression boundaries of cad, D, opa, and wg (Figure 5). At stage 4.4 (nuclear cycle 13), the graded tll border overlaps the graded posterior edge of the D domain (Figure 5A, top row). By mid stage 5, a narrow gap of low expression opens between the tll domain and the trunk domains of D and opa (Figure 5A, middle row), which is then filled by the cad and D tail domains at late stage 5 (Figure 5A, bottom row). cad is expressed ubiquitously throughout the posterior of the embryo at stage 4.4 (Figure 5B, top row), then fades from the hkb domain by mid stage 5 (Figure 5B, middle row), with a narrow gap of low expression opening up between the cad and hkb domains by late stage 5 (Figure 5B, bottom row). The wg posterior domain initiates at the border between cad and hkb expression present at mid stage 5 (Figure 5B, middle row), and by late stage 5 the wg posterior domain neatly demarcates the strip of tll-positive hkb-negative cells (Figure 5B, bottom row).

#### Summary

The spatiotemporal expression dynamics of Tll and Hkb make them good candidates for patterning the timer gene boundaries and the posterior wg domain because they are differentially expressed across the various terminal regions. Specifically, from posterior to anterior, the prospective posterior midgut experiences strong expression of both Tll and Hkb, the prospective hindgut experiences strong expression of Tll but weak/transient expression of Hkb, the tail region experiences weak/transient expression of Tll, and the trunk is consistently free of Tll and Hkb expression.

### The terminal system interacts with the timer gene network to pattern the posterior of the embryo

To determine whether Hkb and Tll spatially regulate the timer genes, we investigated timer gene expression in hkb- mutants, tll- mutants, and torso (tor-) mutants (Figure 6). Tor (Klingler et al., 1988; Sprenger et al., 1989; Casanova and Struhl, 1989) is a maternally provided receptor necessary for transducing the extracellular signal-regulated kinase (ERK) signal that specifies the poles of the embryo (reviewed in Duffy and Perrimon, 1994; Li, 2005; Goyal et al., 2018), and therefore tor- mutants express neither hkb nor tll (Brönner and Jäckle, 1991; Pignoni et al., 1992).

![Figure 6.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig6-v2.jpg)

**Figure 6.:** (A–F) Gene expression in wild-type and mutant embryos of increasing ages. The leftmost column shows a four-channel merge; the middle columns show individual channels; the rightmost column shows quantitative expression traces (75–100% AP axis) from the embryos shown to the left. (A) Timer gene expression in wild-type. The AP axis is truncated in the expression plot for the stage 6 embryo (diagonally shaded area) due to proctodaeal invagination. (B) Timer gene expression in tor- mutants. Note how the timer gene expression expands all the way to the posterior pole (excluding the pole cells). The broad posterior wg domain seen at stage 5.4–5.5 is mispatterned segmental expression; the posterior wg domain seen in wild-type embryos is absent. (C) Timer gene expression in tll- mutants, relative to wg expression. Note that the cad, D, and opa domains share a similar posterior border, the cad domain fades over time, and the wg posterior domain is absent. (Some mispatterned segmental wg expression is seen near the posterior of the embryo, similar to tor- mutants.) (D) Timer gene expression in tll- mutants, relative to hkb expression. Note that the posterior borders of cad, D, and opa all abut the hkb expression domain. (E) Timer gene expression in hkb- mutants, relative to wg expression. Note that cad is not repressed from the posterior pole until stage 5.5, and the posterior wg domain extends to the posterior pole. (F) Timer gene expression in hkb- mutants, relative to tll expression. Note that the tll domain is small, and it preserves normal relationships with the cad, D, and opa domains. (G, H) Single-channel quantitative expression traces (75–100% AP axis) from multiple wild-type and mutant stage 5.5 embryos. Note the absence of spatial patterning in tor- mutants and the posteriorly shifted expression boundaries in tll- and hkb- mutants. In (A–F) all embryos are anterior left, dorsal up, lateral view; scale bar = 50 μm; grey lines show embryo outlines. In (G,H) all traces are individually normalised; mutant traces are overlaid on wild-type traces (grey) for ease of comparison.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A, B) Plots showing quantitative expression traces (75–100% AP axis) from multiple stage 5.5 embryos, individually normalised to the range 0–1. Leftmost column shows traces from wild-type embryos (coloured lines); remaining columns show traces from tor-, tll-, or hkb- mutants (coloured lines) overlaid on the same wild-type traces shown in the leftmost column (grey lines). (A) In tor- mutants, note the loss of spatial patterning. In tll- mutants, note the posterior shifts of the cad, D, and opa posterior boundaries and the loss of the posterior wg domain. In hkb- mutants, note the posterior shifts of all boundaries and the extension of the posterior wg domain to the posterior pole. (B) Note the posterior shift of the tll boundary in hkb- mutants, in addition to the posterior shifts of the cad, D, and opa boundaries also seen in for the hkb- mutants in (A). Source data is the same as Figure 6.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Note that the posterior domain persists for longer in the hkb- mutants, and ectopic expression appears at the anterior pole. All embryos are anterior left, dorsal up, lateral views. Scale bar = 50 μm; grey lines show embryo outlines.

#### Timer gene expression in tor- mutants

In tor- mutants (Figure 6B and G), all posterior spatial patterning of the timer genes was lost, and their temporal expression dynamics resembled those seen in the trunk of wild-type embryos. Thus cad, D, and opa were all expressed to the very posterior of the embryo at the beginning of stage 5, with first cad and then D expression turning off as stage 5 progressed. The posterior domain of wg was absent, and the region of segmental wg expression expanded posteriorly, as described previously (Mohler, 1995). Loss of the cad tail domain in tor- and torso-like (tsl-) mutants has also been described previously (Mlodzik and Gehring, 1987b; Schulz and Tautz, 1995).

#### Timer gene expression in tll- and tll- opa- mutants

In tll- mutants (Figure 6C, D and G; Figure 6—figure supplement 1A), the posterior wg domain was absent (Wu and Lengyel, 1998), and the cad, D, and opa domains were expanded posteriorly to abut the hkb domain, which looked similar to wild-type (Figure 7B). Normal expression of hkb in tll- mutants has been previously reported (Brönner and Jäckle, 1991; Brönner et al., 1994; Ashyraliyev et al., 2009).

![Figure 7.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig7-v2.jpg)

**Figure 7.:** (A, B) Terminal gene expression (wg, cad, fkh, and tll/hkb) in wild-type and mutant embryos. In cadm-z-, note the loss of wg and fkh expression. In hkb-, note the posterior fate map shift and the delayed repression of posterior cad. In tll-, note the loss of the posterior wg domain, the posteriorly shifted cad domain, and the reduced size of the fkh domain. (C, D) Timer gene expression in wild-type and fkh- mutant embryos. Note the extremely reduced posterior wg domain in fkh-. (A, C) Individual stage 5.4 (A) or stage 5.5 (C) embryos; the leftmost column shows a four-channel merge, other columns show individual channels. All embryos are anterior left, dorsal up, lateral view. Scale bar = 50 μm; grey lines show embryo outlines. (B, D) Quantitative expression traces (75–100% AP axis); the leftmost column shows multi-channel traces from the individual embryos in (A, C), other columns show single-channel traces from multiple stage 5.4–5 embryos (B) or stage 5.5 embryos (D). All traces are individually normalised; mutant traces are overlaid on wild-type traces (grey) for ease of comparison.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A, B) Plots showing quantitative expression traces (75–100% AP axis) from multiple stage 5.4 and stage 5.5 embryos, individually normalised to the range 0–1. Leftmost column shows traces from wild-type embryos (coloured lines); remaining columns show traces from cadm-z-, tll-, or hkb- mutants (coloured lines) overlaid on the same wild-type traces shown in the leftmost column (grey lines). (A) In cadm-z- mutants, note the severe reduction in fkh levels, the loss of the posterior wg domain, and the persistence of cad expression in the trunk. In tll- mutants, note the reduced size of the fkh domain and the posterior shift of the cad domain. In hkb- mutants, note the reduced sizes of the tll and fkh domains, the posterior shifts of the wg and cad domains, and the total (wg) or partial (cad) derepression of expression in the posterior of the embryo. (B) A similar combination of genes is shown, with hkb in place of cad. Note that the size of the hkb domain is unaffected in either cadm-z- or tll- mutants. The tll- traces in both (A) and (B) are taken from a single wg/cad/hkb/fkh stain. Source data is the same as Figure 7.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** Plots showing quantitative expression traces (67.5–97.5% AP axis) from multiple stage 5.5 embryos, individually normalised to the range 0–1. Left column shows traces from wild-type embryos (coloured lines); right column shows traces from fkh- mutants (coloured lines) overlaid on the same wild-type traces shown on the left (grey lines). Note the loss of the wg posterior domain in fkh- mutants. Source data is the same as Figure 7.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** Black arrowheads mark the posterior wg domain (severely reduced in fkh- mutants). White arrowheads mark the cad tail domain. In the stage 6 wild-type embryo, note the additional cad domain posteriorly abutting the posterior wg domain (white arrow). This domain (corresponding to presumptive Malpighian tubules and proximal posterior midgut; Harbecke and Janning, 1989) is absent in stage 6 fkh- mutants. In fkh- mutants, new cad expression instead appears later, at the posterior edge of the tail domain (white arrow in the stage 7 embryo, pointing at prominent transcriptional foci). MD1, mitotic domain 1 (used for embryo staging). All embryos are anterior left, dorsal up, lateral or ventrolateral views. Scale bar = 50 μm; grey lines show embryo outlines.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig7-figsupp4-v2.jpg)

**Figure 7—figure supplement 4.:** wg expression and DAPI (nuclei) staining from wild-type, cadm-z- mutant, and fkh- mutant embryos at stages 6, 7, and 8. Embryos were staged by the presence of mitotic domain 1 (MD1, stage 7) or mitotic domain 4 (MD4, stage 8). Note the delayed proctodaeal invagination seen in both cadm-z- and fkh- mutants relative to wild-type embryos. Note also the epithelial buckling in fkh- mutants (arrowheads at stages 6 and 7), reminiscent of folded gastrulation (fog-) mutants (Sweeton et al., 1991). Both cadm-z- and fkh- mutants also mostly lack the posterior wg domain (arrows). All embryos are anterior left, dorsal up, lateral or dorsolateral views. Scale bar = 50 μm; grey lines show embryo outlines.

A posteriorly shifted cad tail domain was transiently expressed (Figure 6C and G; Figure 4—figure supplement 5). This finding conflicts with previous reports that the cad tail domain was either unaffected (Reinitz and Levine, 1990) or completely absent (Mlodzik and Gehring, 1987b) in tll- mutants.

The pattern of D expression in the trunk was abnormal (presumably caused by feedback from the segmentation genes, which are misregulated in tll- mutants; Mahoney and Lengyel, 1987; Casanova, 1990; Janssens et al., 2013), and a persistent posterior D domain did not emerge (Figure 6C; Figure 4—figure supplement 5).

tll- opa- double mutants showed similar patterning dynamics to tll- single mutants, except that tail-like expression of D was rescued and persisted into germband extension (Figure 4—figure supplement 5).

#### Timer gene expression in hkb- mutants

In hkb- mutants (Figure 6E–H), the wg posterior stripe became a posterior cap (Mohler, 1995), and cad expression persisted longer than normal at the posterior pole. The relative phasing of the cad, D, opa, and wg domains was preserved, but the whole terminal pattern was posteriorly shifted/expanded into territory that would normally express hkb (Figure 6H).

In contrast to previous reports that tll expression is unaffected in hkb- mutants (Brönner and Jäckle, 1991; Brönner et al., 1994; Brönner and Jäckle, 1996), we found that the tll domain was smaller than normal, thereby preserving the correlation between tll levels and timer gene expression boundaries seen in wild-type embryos (Figure 6F and H; Figure 6—figure supplement 1B). Expression of tll persisted throughout stages 6 and 7, rather than fading at stage 6, and ectopic expression appeared at the anterior pole (Figure 6—figure supplement 2).

#### Summary

All posterior spatial patterning of the timer genes is dependent on the terminal system via tor. Expression boundaries associated with the tail and hindgut are perturbed in tll- mutants, while expression boundaries associated with the posterior midgut are perturbed in hkb- mutants. In addition, there is a concerted posterior shift of the fate map in hkb- mutants, which we attribute to the reduced size of the tll domain.

Our observations from this and the previous section suggest that Tll strongly represses D and opa and weakly represses cad, while Hkb represses wg, cad, D, and opa (see Appendix 3—table 1 for detailed reasoning). Hkb is also necessary for activation of tll at normal levels (an interaction that is presumably indirect since Hkb acts as a repressor; Goldstein et al., 1999), and for timely repression of tll after stage 5.

### Fkh demarcates the tail/hindgut border and activates posterior wg

Having found that Tll is necessary for patterning both the tail region and the posterior wg domain (prospective hindgut), we next asked how these regions are distinguished from each other. Forkhead (Fkh) is a zygotic transcription factor that is expressed in the posterior of the embryo from stage 4.4 (nuclear cycle 13) downstream of Tor (Weigel et al., 1989; Weigel et al., 1990) and is required for the specification of hindgut identity (Jürgens and Weigel, 1988; Weigel et al., 1989; Kuhn et al., 1995; Hoch and Pankratz, 1996).

#### fkh expression in cadm-z-, hkb-, and tll- mutants

We examined the expression of fkh relative to other terminal genes in wild-type embryos and in mutant genotypes in which tail or hindgut patterning is perturbed (Figure 7A and B).

In wild-type embryos at stage 5.4, the posterior fkh domain had a fairly sharp border, which lined up with the anterior border of the posterior wg domain and the posterior border of the cad tail domain.

In cadm-z- mutants, fkh expression was strongly reduced (Wu and Lengyel, 1998), contrasting with the tll and hkb domains in these embryos, which looked normal (Figure 7—figure supplement 1; Wu and Lengyel, 1998; Olesnicky et al., 2006).

In hkb- mutants, the fkh domain was reduced in size (Weigel et al., 1990; Gaul and Weigel, 1990), correlating with the reduced size of the tll domain and the posteriorly shifted wg and cad borders in this genotype.

The fkh domain was also reduced in tll- mutants (Weigel et al., 1990; Gaul and Weigel, 1990). The reduced domain was the same size as the hkb domain, and it abutted the posteriorly shifted cad tail domain.

#### Timer gene expression in fkh- mutants

In fkh- mutants (Figure 7C and D), the posterior wg domain was largely absent (Wu and Lengyel, 1998), although there was some residual posterior wg expression, particularly in ventral tissue. cad, D, and opa expression was essentially normal throughout stage 5, although the cad posterior border appeared to be slightly posteriorly expanded relative to the D tail domain.

A stronger effect on cad expression was seen after gastrulation, when new cad transcription appeared posteriorly abutting the cad tail domain, rather than several cells away (posterior to wg) as in wild-type embryos (Figure 7—figure supplement 3). Our findings contrast with a previous report, which described cad expression as being normal in fkh- mutants (Jürgens and Weigel, 1988).

#### Abnormal morphogenesis in fkh- and cadm-z- mutants

Morphogenesis was abnormal in fkh- mutants, in that proctodaeal invagination was delayed until after stage 7 (Figure 7—figure supplement 4). This finding contrasts with previous reports that morphogenesis in fkh- mutants is normal until the end of the extended germband stage (Weigel et al., 1989; Wu and Lengyel, 1998).

cadm-z- mutants (which have severely reduced fkh expression) show a similar morphogenetic delay (Figure 7—figure supplement 4) as well as other defects in posterior invagination (Wu and Lengyel, 1998). Posterior invagination is dependent on Fog signalling (Costa et al., 1994; Sweeton et al., 1991; Parks and Wieschaus, 1991), which is known to be reduced in cadm-z- mutants (Wu and Lengyel, 1998). As Fkh is known to activate Fog signalling in other developmental contexts (Chung et al., 2017), the reduction in Fog signalling may be mediated by the reduction in Fkh.

#### Summary

We found a consistent pattern across wild-type, cadm-z-, hkb-, and tll- genotypes, in which the fkh border abutted the posterior border of the cad tail domain, and posterior wg was only expressed in fkh-positive hkb-negative territory. Accordingly, in fkh- mutants, the posterior wg domain was largely lost.

These results are consistent with previously proposed regulatory interactions: that Fkh activates wg (Wu and Lengyel, 1998), that Cad activates fkh (Wu and Lengyel, 1998), and that Tll and Hkb indirectly enable fkh to be expressed (Weigel et al., 1990; Casanova, 1990; Goldstein et al., 1999; Morán and Jiménez, 2006). Accordingly, the activation of wg by Cad (Wu and Lengyel, 1998) appears to be indirect, via Fkh (see Appendix 3—table 1 for detailed reasoning). In addition, it is possible that Fkh represses cad, but current evidence is inconclusive (see Appendix 3—table 1).

### Inferred regulatory interactions collectively form a network that can be formalised and simulated

From looking at how gene expression is affected in various mutant genotypes, we have inferred a network of regulatory interactions between the timer genes and the posterior terminal genes (Figure 8A; Appendix 3—table 1). Most (11/18) of these proposed interactions originate from this study, although we also find support for previously proposed interactions related to the patterning of tll, hkb, fkh, and wg (Figure 8B). (For a recent quantitative model of posterior gut specification using a network similar to Figure 8B, see Keenan et al., 2022.)

![Figure 8.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig8-v2.jpg)

**Figure 8.:** (A) Arrow diagram showing the regulatory interactions we have inferred from the experiments described in this work. Pointed arrowheads indicate activation; flat arrowheads indicate repression. Solid lines indicate interactions that are presumed to be direct; dashed lines indicate interactions that are presumed to be indirect. The diagram is laid out so that the factors are arranged in approximately the same order left to right as their expression along the AP axis, and causation mainly flows from top to bottom (with exceptions for Opa and Cad). To avoid arrow crossovers, the repression of Opa, D, and Cad by Hkb is shown separately from the main network. (B) The same network as in (A), highlighting the interactions described in the existing literature. (C–K) Simulation output for a logical model of posterior terminal patterning, for wild-type and eight mutant genotypes (see main text for details). Each set of plots shows the expression patterns of the logical variables Tll, Hkb, Fkh, Wg, Cad, D, and Opa (y-axis) across AP regions 1–4 (x-axis), at timepoints t0–t3. For Tll, Hkb, D, and Opa, a light colour shade represents weak expression and a dark colour shade represents strong expression. Mutant genotypes never express the relevant protein; tor- mutants were simulated as tll- hkb- double mutants.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/78902/elife-78902-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A) Arrow diagram showing a hypothetical timer gene network for sequential segmentation. Pointed arrowheads represent activation; flat arrowheads represent repression. Solid arrows are interactions taken from the Drosophila timer gene network in Figure 8A; dotted arrows are two additional interactions that might be present in sequentially segmenting species. The arrow from Wg to Cad supposes that Wg signalling from a posterior signalling centre activates cad expression, even in the presence of D. (Note that both Sox and Zic transcription factors can have different regulatory effects in the presence or absence of Wnt signalling, via molecular interactions with β-catenin and TCF; Pourebrahim et al., 2011; Murgan et al., 2015; Mukherjee et al., 2022.) The arrow from Cad to Opa completes an ‘AC-DC circuit’ network motif (Panovska-Griffiths et al., 2013; Perez-Carrasco et al., 2018) between the timer genes. (B) Simulation output from a model of the network in (A) operating in a scenario of posterior Wg signalling and AP axial growth. Each plot shows axial expression of the logical variables Wg, Cad, D, and Opa at a different timepoint in the simulation (t0–t30). The position of the Wg signalling centre (dark yellow rectangle) marks the posterior of the elongating AP axis; the spatial extent of Wg signalling is also shown (light yellow rectangle). Close to the posterior Wg signalling centre, Cad is activated by Wg, in turn activating D and keeping Opa repressed. Further away from the signalling centre, repression of Cad by D kicks in. Cad turns off, repression of Opa is lifted, and Opa in turn represses both Cad and D. Combined with the axial elongation of the tissue, this scenario produces posteriorly shifting wavefront dynamics (the transition between Cad/D and Opa expression moves posteriorly across the axis over time), similar to those found in Tribolium (Clark and Peel, 2018).

We now formalise the regulatory network in Figure 8A as a logical model, and see whether it reproduces the patterning dynamics that we observed in the embryo. For the purposes of this study, we are aiming for a minimal, qualitative explanation of timer gene patterning, commensurable with the essentially qualitative developmental genetic paradigm we have been working within. We are interested in the relative ordering of gene expression domains in time and space, abstracted away from specific domain sizes, expression levels or expression kinetics. To the extent that the model is able to recapitulate the essential features of both wild-type and mutant genotypes, our confidence in the network will be increased.

The modelling framework we have chosen is very simple (for a full description, see Appendix 4). Briefly, Hkb and Tll are assumed to be extrinsic inputs to the system (we ignore the cross-regulation of tll by Hkb), and we model how Fkh, Wg, Cad, D, and Opa are expressed in response. Each of these seven factors is modelled as a logical variable, some of which (Hkb, Tll, D, Opa) may take one of three levels of expression (off/weak/strong), while the others (Fkh, Wg, Cad) may take only two (off/on). The AP axis is modelled as four discrete regions, 1–4 (corresponding to trunk, tail, hindgut, and posterior midgut, respectively), which differ in their hard-coded Hkb and Tll inputs over time. (Note that we do not include any dorsoventral input to the system, nor attempt to model the D neuroectodermal domain.) Each simulation consists of four time points, t0–t3 (corresponding to nuclear cycle 13, early stage 5, mid stage 5, and stage 6, respectively). At t0, Cad is on in all regions, and the other output factors are off. Expression at subsequent timepoints is computed from expression at t(n − 1), according to factor-specific logical rules (which remain the same for all timepoints). Mutants are simulated by keeping the relevant factor(s) turned off for all timepoints.

### The regulatory network explains the patterning dynamics of each genotype

We simulated the patterning model for the wild-type condition (Figure 8C) and eight mutant genotypes examined in this study (fkh-, cadm-z-, D-, opa-, tor-, hkb-, tll-, and tll- opa-; Figure 8D–K). A genotype-by-genotype explanation of the simulated expression dynamics is provided in Appendix 4, along with a table cross-referencing the simulated expression data with the corresponding observations from real embryos (Appendix 4—table 1). Allowing for the simple, qualitative nature of the model, the simulations were remarkably accurate at recapitulating the patterning dynamics of each genotype.

#### Recapitulation of wild-type patterning

Regions 1–4 generate different gene expression as a result of their different inputs from Tll and Hkb. Across regions 3 and 4, the nested domains of strong Tll and Hkb expression specify abutting domains of hindgut (Fkh and Wg) and posterior midgut (Fkh only) fates (Weigel et al., 1990; Casanova, 1990), specifically by repressing the timer genes (both regions), activating Fkh (both regions), and differentially regulating Wg (repressed by Hkb in region 4). In region 1 (trunk), where Tll and Hkb are not expressed, gene expression is shaped by the intrinsic dynamics of the timer gene network: as D is activated and the level of Opa builds up, first Cad and then D are repressed. Finally, in region 2 (tail), these dynamics are modulated by transient expression of Tll, which delays the activation of D and Opa, and thereby prolongs the expression of Cad. Crucially, this Tll expression is weaker than in region 3, and so does not activate Fkh and (therefore) Wg.

#### Recapitulation of mutant phenotypes

Simulated mutants of the ‘outputs’ Fkh, Cad, D, and Opa (Figure 8D–G) have perturbed gene expression within specific regions, but the overall spatial organisation of the tissue is unaffected. In the fkh- mutant, Wg is never activated in region 3. In the D- and opa- mutants, the turnover of timer gene expression in region 1 is perturbed: the repression of Cad is delayed in D-, and the repression of D is delayed in opa-. Finally, in the cadm-z- mutant, widespread effects on gene expression coexist with fairly normal spatial organisation: in regions 3 and 4, Fkh and (therefore) Wg are not expressed, while in regions 1 and 2 the activation of D is reduced. (Although we modelled mutants as deficiencies and therefore did not recapitulate the delayed cad repression seen in cadm-z- embryos [Figure 4A], we can interpret this delay as a knock-on effect of the reduced D expression, since D represses Cad.)

In contrast, simulated mutants involving the ‘inputs’ Tll and Hkb (tor-, hkb-, tll-, tll- opa-; Figure 8H–K) show more serious spatial effects, which tend to resemble homeotic transformations. The tor- mutant, which removes all expression of Tll and Hkb, transforms regions 2–4 into region 1. The hkb- mutant essentially transforms region 4 (posterior midgut) into region 3 (hindgut). The tll- mutant transforms region 2 into region 1 but produces novel expression dynamics in region 3: D expression is transiently repressed (as in wild-type region 2) but Opa is not, producing a posteriorly shifted, transient Cad stripe and precluding any late expression of D. Finally, in the tll- opa- mutant, the repression from Opa on D and Cad seen in the tll- mutant is removed, and region 3 is fully transformed into region 2.

#### Discrepancies with real embryos

The discrepancies with real patterning stem from the simple, qualitative nature of the model. The activation of Fkh and (therefore) Wg is spuriously delayed in the hkb- simulation (Figure 8I), owing to the discrete implementations of time, Tll expression, and Fkh regulation. The model cannot recapitulate the subtle shifting dynamics with the tail region (Figure 3) because the tail is modelled as a single, discrete block. Similarly, the model cannot recapitulate the concerted fate map shifts seen in hkb- and D- mutants (Figure 4B; Figure 6E–H) because there is no representation of region size. That said, if we extrapolate from the existing results, we can interpret the posterior shifting dynamics within the tail region as resulting from the posterior retraction of Tll expression over time (Figure 5—figure supplement 3; Figure 5—figure supplement 4), interpret the posterior fate map shift in hkb- mutants as resulting from (indirect) cross-activation of tll by Hkb (Figure 6H), and interpret the anterior fate map shift in D- mutants as resulting from potential cross-repression of tll by D.

#### Summary

The genetic interactions we uncovered in this study are able to explain the qualitative aspects of timer gene patterning in both wild-type and mutant genotypes. In particular, our model explains how a graded Tll domain delineates both the anterior and posterior boundaries of the tail region, and explains why transient expression of Tll within the tail region is important for producing its characteristic timer gene dynamics. The model also explains the posteriorly shifted tail-like expression domains seen in tll- and tll- opa- mutants as the result of graded and dynamic Hkb expression. For insight into quantitative phenomena such as the fate map shifts in hkb- and D- mutants, it will be necessary to analyse quantitative models incorporating zygotic cross-regulation of tll.

## Discussion

In this study, we have used mutants, multiplexed imaging, and modelling to elucidate how the blastoderm expression dynamics of the Drosophila timer genes cad, D, and opa arise from a combination of cross-regulatory interactions and spatially localised inputs from the posterior terminal system. This work has four main implications. First, we have demonstrated that timer gene expression is partially driven by intrinsic network dynamics. Second, we have uncovered more evidence that the timer genes have broad effects on developmental timing, through our discovery that cadm-z- embryos precociously express genes associated with neural differentiation. Third, we have produced a coherent model for the patterning of the posterior terminal region. Fourth, we have clarified the segmental nature of the Drosophila tail. These findings increase our understanding of Drosophila development and have evolutionary significance for the mechanisms of axial patterning in other species.

### Timer gene expression is regulated by intrinsic network dynamics and extrinsic spatiotemporal inputs

This work provides evidence for a set of cross-regulatory interactions between cad, D, and opa that helps generate dynamic, sequential expression. In particular, we find that Cad activates D (i.e., promotes the expression of the next gene in the sequence), while D represses cad and Opa represses cad and D (i.e., both inhibit the previous gene(s) in the sequence). opa is not cross-regulated, however, making it an ‘input-only’ component of the three gene network (at least in the blastoderm context).

Timer gene expression is also shaped by extrinsic spatiotemporal regulation. In this work, we show how the timer gene network interacts with the posterior terminal system: most notably, Tll differentially represses cad, D and opa in the tail region, indirectly allowing cad expression to be maintained. The localised inputs from the posterior terminal system are overlaid on global temporal regulation provided by the nuclear:cytoplasmic ratio (which is particularly important for regulating the onset of opa transcription; Lu et al., 2009) as well as the levels of maternal factors such as Tramtrack (Harrison and Travers, 1990; Brown et al., 1991; Read et al., 1992), Zelda (Liang et al., 2008; Harrison et al., 2011; Nien et al., 2011; McDaniel et al., 2019), Stat92e (Yan et al., 1996; Hou et al., 1996; Tsurumi et al., 2011), and GAGA Factor/Trithorax-like (Farkas et al., 1994; Bhat et al., 1996; Moshe and Kaplan, 2017; Gaskill et al., 2021). Ironically, precisely because these maternal factors are so crucial to development, their patterning roles remain less well understood than those of the zygotic patterning genes, which are less pleiotropic and therefore easier to study.

### Timer gene expression has broad effects on developmental timing

Recent work in the Drosophila blastoderm has demonstrated the extensive effects of timer genes on developmental gene expression. Opa has been shown to act as a pioneer factor, reshaping gene expression genome-wide by opening chromatin at hundreds of target enhancers (Soluri et al., 2020; Koromila et al., 2020). Cad and D are also known to regulate expression across the genome (Li et al., 2008; MacArthur et al., 2009; Aleksic et al., 2013). Here, we have found that early Cad expression appears to be necessary for the correct timing of later developmental events because neuroectodermal gene expression turns on precociously in cadm-z- embryos. The vertebrate Cad ortholog Cdx4 has also been shown to temporally regulate neural differentiation, in the developing spinal cord (Joshi et al., 2019), a tissue in which D and Opa orthologs play key developmental roles (reviewed in Graham et al., 2003; Merzdorf, 2007; Houtmeyers et al., 2013; Stevanovic et al., 2021). More generally, comparative evidence suggests that Cad/Cdx plays a deeply conserved role in the formation of the posterior body and the patterning of the posterior gut (Copf et al., 2004; Wu and Lengyel, 1998; van Rooijen et al., 2012; Zhong et al., 2020). In this context, Drosophila cadm-z- mutants offer a rare opportunity to study the genome-wide effects of a total loss of Cad/Cdx function without also catastrophically perturbing early developmental events.

### A revised picture of posterior terminal patterning in Drosophila

In this work, we have investigated blastoderm gene expression downstream of the posterior terminal system, revisiting a patterning network that was most intensely studied in the late 1980s and early 1990s (Strecker et al., 1986; Mahoney and Lengyel, 1987; Mlodzik and Gehring, 1987b; Strecker et al., 1988; Jürgens and Weigel, 1988; Weigel et al., 1990; Casanova, 1990; Brönner and Jäckle, 1991; Wu and Lengyel, 1998). The modern availability of marked balancers and multiplexed imaging techniques has allowed us to clarify the topology and spatiotemporal dynamics of the network, and incorporate genes (D and opa) that had not been cloned at the time most of the original work was completed. All told, we have identified 11 new regulatory interactions involved in Drosophila AP patterning, put forward the first formalised model (to our knowledge) for the patterning of the tail, and provided a solid foundation for future quantitative analyses of this system.

Although simple, our model provides new insights into how the tail and hindgut regions are specified in the early embryo. Both regions, along with segment A8, have long been known to depend on Tll expression (Strecker et al., 1986; Diaz et al., 1996). tll alleles can be arranged into a coherent phenotypic series in which the most posterior structures within the Tll-dependent region are the most sensitive to tll perturbation and the most anterior structures are the least (Strecker et al., 1986; Diaz et al., 1996), suggesting that this part of the blastoderm fate map is patterned by a gradient of Tll activity (Casanova, 1990). However, it has not been clear at the network level how graded Tll activity would be transduced into a specific series of boundaries and domains.

We found that tll expression was strong and persistent within the hindgut region, but weaker and transient in the tail region, with the anterior border of the expression domain retracting posteriorly across nuclei over time. We additionally found that Tll effectively patterned both the anterior and posterior boundaries of the tail region by differentially repressing D and opa relative to cad. Crucially, D and opa were repressed even where Tll expression was transient and weak, but cad was not repressed (and fkh was not activated) unless Tll expression was stronger, helping explain the transition from tail fate to hindgut fate as Tll levels increase. Furthermore, the retraction of the Tll domain over time explains the posterior shifting dynamics we found for the timer genes within the tail region, which contrasts with the anterior shifting dynamics previously described for the pair-rule and gap genes (Jaeger et al., 2004; Keränen et al., 2006; Surkova et al., 2008; Lim et al., 2018).

We also discovered, to our surprise, that there is a concerted posterior fate map shift in hkb- embryos, apparently mediated by a reduction in the size of the tll domain. (A subtle anterior fate map shift additionally occurs in D- embryos, which might also be mediated by Tll.) Although further research is necessary to determine the mechanism by which Hkb cross-regulates tll, the phenotype implies that the size of the tll domain is not an unmediated response to terminal signalling. (Indeed, there are hints in the existing literature that tll and hkb may be zygotically cross-regulated by other AP patterning genes as well; see Casanova et al., 1994; Greenwood and Struhl, 1997; de las Heras and Casanova, 2006.) These findings may complicate the interpretation of recent studies that have characterised the input:output relationships between terminal signalling and tll and hkb expression using optogenetics (Johnson and Toettcher, 2019; Johnson et al., 2020; Keenan et al., 2020).

### The segmental character of the Drosophila tail

The ancestral insect body plan has 11 true abdominal segments plus the periproct/telson, but this number has been reduced in many extant insect lineages (Snodgrass, 1935; Demerec, 1950; Matsuda, 1976; Chapman et al., 2013). In Drosophila, the most common view has been that the embryo makes 10 abdominal segments (i.e., 15 parasegment boundaries), with the anal pads located in PS15/A10 (Turner and Mahowald, 1979; DiNardo et al., 1985; Sato and Denell, 1986; Perkins and Perrimon, 1991; Kuhn et al., 1992; Schmidt-Ott et al., 1994). In particular, territories corresponding to A8, A9, and A10 are visible at the morphological level during embryogenesis (Turner and Mahowald, 1979), and surveys of en, wg, hh, and slp staining have found evidence for (at most) 15 parasegment boundaries (DiNardo et al., 1985; Baker, 1987; Baker, 1988; Kuhn et al., 1992; Grossniklaus et al., 1992; Mohler and Vani, 1992; Tabata et al., 1992; Lee et al., 1992; Tashiro et al., 1993; Kuhn et al., 1995). However, fate mapping experiments (Jürgens, 1987) and surveys of gooseberry expression (Baumgartner et al., 1987; Gutjahr et al., 1993) have suggested that the embryo makes 16 parasegment boundaries, with the anal pads located in PS16/A11. There is also some evidence for A11 from patterns of gene expression in adult genital discs (Freeland and Kuhn, 1996).

Given the small size of the tail region within the embryo, the fact that it is covered by amnioserosa during key stages of patterning, and the fact that it later undergoes complicated morphogenetic rearrangements and fusions that obscure its metameric nature, it is perhaps unsurprising that the number of Drosophila segments has not been unambiguously resolved. In this study, we present evidence for a vestigial 16th parasegment boundary in the embryo by identifying additional domains of slp and wg expression and reinterpreting previously described domains of eve and en. These observations suggest that the anal pads are located in PS16. (Whether the tissue between PSB16 and the anus should be classified as a true 11th abdominal segment or a non-segmental periproct/telson is beyond the scope of this article.) However, PSB16 appears extremely dorsoventrally restricted and may have little functional significance in the organism. As the number of abdominal segments varies across insects (Matsuda, 1976), the mechanistic basis of this evolutionary reduction would be interesting to study within a comparative developmental framework.

Our findings suggest that the Drosophila embryo sequentially patterns two parasegment boundaries after gastrulation, and that in both cases the new boundary is patterned by abutting stripes of slp and eve. In PS15 and PS16, the relative arrangement of slp, eve, wg, and en expressing cells is the same conserved pattern that is found at parasegment boundaries in the Drosophila trunk and throughout the arthropod phylum (reviewed in Clark et al., 2019). However, tail segmentation differs from trunk segmentation in that resolved, stable eve stripes emerge de novo and with single-segmental periodicity, rather than from a dynamic and double-segmental phase of pair-rule gene expression.

Intriguingly, a remarkably similar switch from double-segment to single-segment periodicity occurs towards the end of segmentation in the centipede Strigamia maritima, where stable, resolved eve stripes start appearing de novo in the anterior segmentation zone instead of emerging from posterior oscillatory expression (Brena and Akam, 2013). A possible switch from double-segmental to single-segmental patterning has also been reported for terminal segments in the beetle Tribolium (Janssen, 2014). These observations hint that terminal and trunk segments may be homonomous at the level of segment-polarity gene expression but derived from distinct ontogenetic programs. More work is needed to determine how such a developmental switch—if present—is controlled, as well as its relationship to the more general problem of terminating axial development.

### Comparative analysis and evolutionary implications

We end this study by assessing the relevance of our findings from Drosophila to the development of other insect species. Which aspects of the Drosophila network are likely to be conserved in other insect species that have been used to study segmentation, such as Tribolium, Nasonia vitripennis, and Oncopeltus fasciatus? And how might the Drosophila network differ from that of its sequentially segmenting ancestors?

The cross-regulatory interactions that we found between the timer genes might be quite widely conserved in insect segmentation. Activation of D by Cad, repression of cad by Opa, and repression of D by Opa are all consistent with a segment addition zone that is subdivided into a posterior region that expresses Cad and D and an anterior region that expresses Opa, as seen, for example, in Tribolium (Clark and Peel, 2018). However, repression of cad by D would need to be reconciled with the sustained expression of both cad and D in the posterior segment addition zone. Intriguingly, some of the timer gene cross-regulatory interactions may even be important for regulating expression dynamics in completely different developmental contexts, given that Opa has recently been found to repress D during the temporal patterning of Drosophila intermediate neural progenitors (Abdusselamoglu et al., 2019).

The different components of the Drosophila terminal system seem to have acquired their posterior patterning roles at different times: posterior tll expression is found across diverse holometabolan species (Schroder et al., 2000; Lynch et al., 2006; Wilson and Dearden, 2009; García-Solache et al., 2010; Lemke et al., 2010; Klomp et al., 2015) although not in hemipterans (Weisbrod et al., 2013; Bickel et al., 2013), whereas hkb and tor appear to have been recruited to terminal patterning roles more recently (García-Solache et al., 2010; Kittelmann et al., 2013; Duncan et al., 2013). In Tribolium, tll is expressed downstream of tor (as in Drosophila), and tor RNAi embryos fail to express cad and wg in the posterior of the embryo, resulting in AP truncation (Schoppmeier and Schröder, 2005). In Nasonia, tll RNAi results in a reduction of posterior cad, as well as in gap gene misregulation that disrupts much of abdominal segmentation (Lynch et al., 2006). It will be instructive to test whether these losses of cad expression in Tribolium and Nasonia are mediated by ectopic expression of Opa, as we found for tll- and tor- mutants in Drosophila. If so, it would suggest that the initial spatial regulation of the timer gene network by Tll in the posterior blastoderm might be conserved across holometabolan embryos, despite their varying modes of development.

So, how does timer gene regulation differ between sequentially segmenting embryos (which establish a persistent segment addition zone) and simultaneously segmenting embryos like Drosophila? One key difference is likely to be the role of a posterior Wnt signalling centre: there is evidence from many different sequentially segmenting species that Wnt signalling is important for activating cad expression and maintaining the segment addition zone (reviewed in Clark et al., 2019), whereas we found that timer gene expression was unaffected in Drosophila wg- mutants, at least during our stages of interest. In addition, it seems probable that timer gene cross-regulation of opa is important in sequentially segmenting species, with this having been lost from the Drosophila lineage during the evolution of simultaneous patterning.

If we modify the Drosophila timer gene network to incorporate these additional features (Appendix 4), we can see how appropriate segment addition zone dynamics might naturally emerge (Figure 8—figure supplement 1). It therefore seems plausible that the cross-regulatory interactions between the Drosophila timer genes may represent an evolutionary vestige of a ‘dynamical module’ that was originally involved in axial elongation (Clark and Peel, 2018; Clark, 2021). Functional experiments in sequentially segmenting species will be necessary to test this hypothesis.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>caudal (cad)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0000251</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>Dichaete (D)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0000411</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>engrailed (en)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0000577</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>even-skipped (eve)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0000606</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>forkhead (fkh)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0000659</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>huckebein (hkb)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0261434</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>muscle segment homeobox (msh)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0000492</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>odd-paired (opa)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0003002</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>sloppy-paired (slp)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0003430</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>tailless (tll)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0003720</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>torso (tor)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0003733</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (D. melanogaster)</td>
      <td>wingless (wg)</td>
      <td>FlyBase</td>
      <td>FLYB:FBgn0284084</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (D. melanogaster)</td>
      <td>Oregon-R</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:5; RRID:BDSC_5</td>
      <td>‘Wild-type’</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>One Shot BL21 Star (DE3)</td>
      <td>Thermo Fisher Scientific</td>
      <td>C601003</td>
      <td>Chemically competent cells</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>cad[3]</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:5316; FLYB:FBal0001531; RRID:BDSC_5316</td>
      <td>Gift from H. Skaer</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>cad[2] FRT40A</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:7091; FLYB:FBal0001530; FLYB:FBti0002071; RRID:BDSC_7091</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>D[r72]</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:8858 FLYB:FBal0086878; RRID:BDSC_8858</td>
      <td>Gift from S. Russell</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>fkh[6]</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:545; FLYB:FBal0004012; RRID:BDSC_545</td>
      <td>Gift from K. Roeper</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>hkb[A321R1]</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:2059; FLYB:FBal0031495; RRID:BDSC_2059</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>opa[8]</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:5335; FLYB:FBal0013272; RRID:BDSC_5335</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Df(3R)Exel6217</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:7695; FLYB:FBab0038272; RRID:BDSC_7695</td>
      <td>Deficiency covering the tll locus</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>tor[XR1]</td>
      <td>Sprenger et al., 1989</td>
      <td>FLYB:FBal0016988</td>
      <td>Gift from T. Johnson</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>wg[l-8]</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:5351; FLYB:FBal0018500; RRID:BDSC_5351</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>CyO, hb-lacZ</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:6650; FLYB:FBba0000025; FLYB:FBti0002621; RRID:BDSC_6650</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>TM6C, twi-lacZ</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:7251; FLYB:FBba0000071; FLYB:FBti0010595; RRID:BDSC_7251</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>TM3, hb-lacZ</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:78357; FLYB:FBba0000047; FLYB:FBti0010581; RRID:BDSC_78357</td>
      <td>Gift from S. Russell</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>hsFLP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:6; FLYB:FBti0002044; RRID:BDSC_6</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ovoD1 FRT40A</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BDSC:2121; FLYB:FBtp0000359; FLYB:FBti0002071; RRID:BDSC_2121</td>
      <td>No longer listed in BDSC</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-D (rabbit polyclonal)</td>
      <td>Soriano and Russell, 1998</td>
      <td></td>
      <td>(1:10)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Hkb (rat polyclonal)</td>
      <td>Ashyraliyev et al., 2009</td>
      <td></td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Opa (guinea-pig polyclonal)</td>
      <td>This paper</td>
      <td></td>
      <td>(1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Tll (rabbit polyclonal)</td>
      <td>Kosman et al., 1998</td>
      <td></td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-guinea pig Alexa Fluor 647 (goat polyclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#:A-21450; RRID:AB_2735091</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rabbit Alexa Fluor 488 (goat polyclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#:A-11034; RRID:AB_2576217</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rabbit Alexa Fluor 555 (goat polyclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#:A-21429; RRID:AB_2535850</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rat Alexa Fluor 488 (goat polyclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#:A-11006; RRID:AB_2534074</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>FI01113 (clone)</td>
      <td>Drosophila Genomics Resource Center</td>
      <td>DGRC:1623347; RRID:DGRC_1623347</td>
      <td>opa cDNA</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Gateway pDONR221 (plasmid)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:12536017</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Gateway pET-DEST42 (plasmid)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:12276010</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cad</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_134301.4</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cad-Intron</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NT_033779.5: 20771910–20781798</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_001274901.1</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>en</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_078976.4</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>eve</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_078946.4</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>fkh</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_001300645.1</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>hkb</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_079497.4</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>msh</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_057976.3</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>opa</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_079504.4</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>slp</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_057382.3</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>tll</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_079857.4</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>wg</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NM_078778.5</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>lacZ</td>
      <td>Molecular Instruments</td>
      <td>HCR v3.0 probes</td>
      <td>Designed to target NCBI:NC_000913.3: c366305-363231</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>B1-5 Alexa Fluor 488</td>
      <td>Molecular Instruments</td>
      <td>HCR amplifiers</td>
      <td>Amplifiers coordinated with probes</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>B1-5 Alexa Fluor 514</td>
      <td>Molecular Instruments</td>
      <td>HCR amplifiers</td>
      <td>Amplifiers coordinated with probes</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>B1-5 Alexa Fluor 546</td>
      <td>Molecular Instruments</td>
      <td>HCR amplifiers</td>
      <td>Amplifiers coordinated with probes</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>B1-5 Alexa Fluor 594</td>
      <td>Molecular Instruments</td>
      <td>HCR amplifiers</td>
      <td>Amplifiers coordinated with probes</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>B1-5 Alexa Fluor 647</td>
      <td>Molecular Instruments</td>
      <td>HCR amplifiers</td>
      <td>Amplifiers coordinated with probes</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>opaDM-F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AAAAAGCAGGCTTCGAAGGAGATAGAACCATGAACGCCTTCATTGAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>opaA-R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGAAAGCTGGGTTGTCGTAGCCGTGGGATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>attB1adap-F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GGGGACAAGTTTGTACAAAAAAGCAGGCT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>attB2adap-R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GGGGACCACTTTGTACAAGAAAGCTGGGT</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Gatweway BP Clonase II</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:11789020</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Gateway LR Clonase II</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:11791020</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Phusion Plus DNA Polymerase</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:F630S</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Overnight Express Instant TB Medium</td>
      <td>Novagen</td>
      <td>Cat#:71491-3</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ni-NTA Agarose</td>
      <td>QIAGEN</td>
      <td>Cat#:30210</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Normal Goat Serum blocking solution</td>
      <td>Vector Laboratories</td>
      <td>Cat#:S-1000-20</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DAPI stain</td>
      <td>Invitrogen Scientific</td>
      <td>Cat#:D1306</td>
      <td>(1 ng/μL)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>#1.5 coverslips</td>
      <td>Corning</td>
      <td>Cat#:2980-224</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>SlowFade Gold AntiFade Mountant</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#:S36940</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Drosophila husbandry and genetics

Stock maintenance and embryo fixation (20 min with 4% formaldehyde in PBS) was performed as described in Sullivan et al., 2000. ‘Wild-type’ flies were Oregon-R. The mutant alleles used were wgl-8 (Bloomington #5351), cad3 (gift from H. Skaer), cad2 (Bloomington #7091), Dr72 (gift from S. Russell), opa8 (Bloomington #5340), torXR1 (gift from T. Johnson), hkbA321R1 (Bloomington #2059), Df(3R)Exel6217 (Bloomington #7695, a deficiency covering the tll locus), and fkh6 (gift from K. Roeper). Mutant lines obtained from the Bloomington Drosophila Stock Centre were verified by cuticle preparations as described in Sullivan et al., 2000. The tll- opa- double mutant was generated by the Cambridge Fly Facility by recombining Df(3R)Exel6217 and opa8. Mutants were balanced over marked balancer chromosomes expressing lacZ during early embryogenesis: CyO, hb-lacZ (Bloomington #6650) for the second chromosome and TM6C, twi-lacZ Sb1Tb1 (Bloomington #7251) or TM3, hb-lacZ Sb1 (gift from S. Russell) for the third.

cad- germline clones were generated using the heatshock induced FLP/FRT system as described in Selva and Stronach, 2007. Briefly, eight vials of 30 cad2 FRT40A/CyO virgin females (Bloomington #7091) were each crossed with 10 hsFLP w; ovoD1 FRT40A/CyO males (constructed by crossing Bloomington #6 hsFLP w; Adv/CyO females with Bloomington #2121 ovoD1 FRT40A/CyO, but note that #2121 is no longer listed in Bloomington). Adults were flipped to new vials every 2 days, resulting in a total of ∼100 vials. When crawling L3 larvae were visible, vials were heatshocked at 37°C in a waterbath for 1 hr, allowed to recover at 25°C for 24 hr, then heatshocked again at 37°C for 1 hr. Approximately 600 non-CyO virgin females (some presumably with cad2/cad2 ovaries) were collected from the heatshocked vials and crossed with ∼300 cad3/CyO, hb-lacZ males. Resulting embryos without lacZ expression lacked both maternal and zygotic cad (cadm-z-), while embryos with lacZ expression were paternal rescues (cadm-z+). Zygotic cad mutants (cadm+z-) were offspring from cad3/CyO, hb-lacZ parents that lacked lacZ expression; note that this genotype is also heterozygous for maternal cad.

### Opa antibody generation

Clone FI01113 containing opa coding sequence was obtained from the Drosophila Genomics Resource Center. Gateway attB primers were designed to express 386 amino acids from the N-terminus of Opa (amino acids 3–389), spanning the zinc finger region in the centre of the protein. The forward primer included a Shine-Dalgarno sequence; the reverse primer was designed to be in-frame with the C-terminal fusion of the Gateway expression vector pET-DEST42 (Thermo Fisher Scientific). A two-stage PCR procedure was used to obtain a final amplicon carrying the attB-sequences at each end of the N-terminal opa sequence.

Primers for the first amplification were

paDM-F: AAAAAGCAGGCTTCGAAGGAGATAGAACCATGAACGCCTTCATTGAGC

paA-R: AGAAAGCTGGGTTGTCGTAGCCGTGGGATG

Overlapping primers for the second amplification to complete the attB regions were

attB1adap-F: GGGGACAAGTTTGTACAAAAAAGCAGGCT

attB2adap-R: GGGGACCACTTTGTACAAGAAAGCTGGGT

The attB-opa amplicon was obtained by PCR with Phusion proofreading polymerase (Thermo Fisher Scientific) using primers opaDM-F and opaA-R. This first amplicon was diluted 1000-fold, then Phusion PCR was repeated with primers attB1adap-F and attB2adap-R. This attB-opa amplicon was recombined into Gateway donor vector pDONR (Thermo Fisher Scientific) using the BP Clonase II kit (Thermo Fisher Scientific). Plasmid DNA from a sequence-verified clone was then recombined into pET-DEST42 using the LR Clonase II kit (Thermo Fisher Scientific).

For expression of the fusion protein, plasmid DNA was transformed into One Shot BL21 Star (DE3) chemically competent Escherichia coli (Thermo Fisher Scientific). Opa protein was expressed in two ways, firstly by IPTG induction of exponentially growing cells (0.75 mM IPTG for 2.75 hr), secondly by overnight culture in TB Overnight Express (Novagen). The Opa fusion protein in pET-DEST42 had a C-terminal 6-His tag. Protein was purified from bacterial pellets, each from 100 ml of cells induced in IPTG or TB Overnight Express. Purification was carried out using Ni-NTA Agarose (QIAGEN), under 8 M urea denaturing conditions according to the manufacturer’s protocol. Purified protein was dialysed against water, then concentrated using an Amicon Ultra-Ultracel 5 kDa centrifugal filter (Millipore). Antibodies were raised in two guinea pigs by Eurogentec. Aliquots are available from EC on request.

### HCR in situ hybridisation and antibody staining

Prior to staining, fixed embryos stored in methanol were put through a rehydration series of 5 min each at 75, 50, and 25% methanol in PBS + 0.1% Tween-20, then washed three times with PBS + 0.1% Tween-20.

HCR in situ hybridisation was performed using probes and hairpins produced by Molecular Instruments, following the protocol for whole-mount fruit fly embryos included in Choi et al., 2016, adapted for v3.0 probes as described in Choi et al., 2018, with the following changes. Treatment of fixed embryos with ethanol, xylene, and proteinase K was omitted. The percentage of dextran sulphate in the probe hybridisation and amplification buffers was reduced from 10% w/v to 5% w/v, to reduce viscosity and allow the embryos to settle more easily in the tube. A 20 min postfix step (4% formaldehyde in 5× SSC + 0.1% Tween-20) was added at the end of the protocol to stabilise the signal.

For antibody staining following HCR, embryos were incubated for 30 min in blocking solution (5% Normal Goat Serum [Vector Laboratories] in 5× SSC + 0.1% Triton X-100), at room temperature with rocking. Embryos were then incubated overnight in preabsorbed primary antibody diluted in blocking solution, at 4°C with rocking. Embryos were washed four times for 15 min in 5× SSC + 0.1% Triton X-100, at room temperature with rocking, then incubated for 30 min in blocking solution, at room temperature with rocking. Embryos were then incubated for 2 hr with fluorescently labelled secondary antibody diluted in blocking solution at room temperature with rocking. Embryos were washed four times for 15 min then one time for 30 min with 5× SSC + 0.1% Triton X-100 at room temperature with rocking. Antibody staining without prior HCR was performed as above with the exception that PBS was used instead of 5× SSC. Primary antibodies were guinea pig anti-Opa (this work) at 1:5000, rabbit anti-Dichaete (Soriano and Russell, 1998) at 1:10, rabbit anti-Tll (Kosman et al., 1998) at 1:100, and rat anti-Hkb (Ashyraliyev et al., 2009) at 1:100. Secondary antibodies were goat anti-guinea pig Alexa Fluor 647 (Invitrogen A-21450), goat anti-rabbit Alexa Fluor 488 (Invitrogen A-11034), goat anti-rabbit Alexa Fluor 555 (Invitrogen A-21429), and goat anti-rat Alexa Fluor 488 (Invitrogen A-11006), diluted 1:1 with 100% glycerol for storage and used at 1:500 (1:1000 overall).

Following HCR and/or antibody staining, embryos were incubated for 30 min with 1 ng/μL DAPI (Thermo Fisher Scientific) in 5× SSC + 0.1% Tween-20, at room temperature with rocking, then washed three times for 30 min in 5× SSC + 0.1% Tween-20, at room temperature with rocking. Prior to mounting, embryos were stored in 1.5 mL tubes in SlowFade Gold Antifade Mountant (Thermo Fisher Scientific).

### Microscopy

Embryos were mounted in SlowFade Gold Antifade Mountant (Thermo Fisher) on glass microscope slides (Thermo Scientific) with #1.5 coverslips (Corning). #1.5 coverslips were used as bridges to prevent embryos from being squashed. Clear nail varnish was used to seal the edges of the slide.

Microscopy was performed on an Olympus FV3000 confocal microscope at the Department of Zoology Imaging Facility (University of Cambridge). Acquired images were 12-bit, with a 1024 × 768 scan format and a 2 μs/pixel dwell time. Whole embryo images were acquired using an Olympus UPlanSApo 30 ×1.05 NA silicon immersion oil objective, a physical pixel size of 0.47 μm × 0.47 μm, and a z-stack step size of 1.5 μm. The close-ups in Figure 1 and Figure 3 were acquired using an Olympus UPlanSApo 60 × 1.3 NA silicon immersion oil objective, a physical pixel size of 0.21 μm × 0.21 μm, and a z-stack step size of 0.8 μm. Each z-stack was specified so as to span from just above the top surface of the focal embryo through to the middle of its yolk.

In each experiment, embryos had been stained for up to four transcripts and/or proteins of interest plus nuclei, generally using Alexa Fluor 488, Alexa Fluor 546, Alexa Fluor 594, Alexa Fluor 647, and DAPI. (For mutant experiments, a lacZ probe or a probe to a gene covered by a deficiency was additionally labelled with one of these same fluorophores, so that homozygous mutant embryos could be easily identified.) All imaging channels were acquired sequentially to minimise cross-talk. The laser lines and collection windows were: 405 laser and 443–472 nm window for DAPI; 488 laser and 500–536 nm window for Alexa Fluor 488; 561 laser and 566–584 nm window for Alexa Fluor 546 or Alexa Fluor 555; 594 laser and 610–631 nm window for Alexa Fluor 594; 640 laser and 663–713 nm window for Alexa Fluor 647. Alexa Fluor 514 (514 laser and 519–540 nm window) was used in place of Alexa Fluor 488 for a round of HCR experiments carried out when the 488 laser was awaiting repair. When necessary, a transmitted light channel was also collected to allow for embryo staging based on the progress of cellularisation.

### Image analysis and figure preparation

Embryo staging was based on Bownes stages (Bownes, 1975; Campos-Ortega and Hartenstein, 1997), with subdivision of particular stages into substages where necessary (details in Appendix 1). Fiji (Schindelin et al., 2012) was used for routine inspection of imaging data and certain image adjustments (details in Appendix 2). Image processing and analysis scripts were written in Python 3 (https://www.python.org) using the libraries NumPy (Harris et al., 2020), SciPy (Virtanen et al., 2020), scikit-image (van der Walt et al., 2014), and matplotlib (Hunter, 2007); see Appendix 2 for details. Figures were assembled in Affinity Designer (Serif Europe). Embryo outlines were drawn manually in Affinity. Image look-up tables (LUTs) were either chosen from the ‘ChrisLUTs’ LUT package for ImageJ (Christophe Leterrier and Scott Harden; https://github.com/cleterrier/ChrisLUTs; ‘NeuroCyto LUTs’ update site in Fiji) or generated for custom colours using a macro provided by Nicolás De Francesco (https://github.com/ndefrancesco).

### Models and simulations

Models were implemented in Python using NumPy (Harris et al., 2020), and outputs were plotted using matplotlib (Hunter, 2007). See Appendix 4 for details.

# Arabidopsis plants perform arithmetic division to prevent starvation at night

## Authors

- Antonio Scialdone<sup>1</sup>
- Sam T Mugford<sup>2</sup>
- Doreen Feike<sup>2</sup>
- Alastair Skeffington<sup>2</sup>
- Philippa Borrill<sup>2</sup>
- Alexander Graf<sup>2</sup>
- Alison M Smith<sup>2</sup> †
- Martin Howard<sup>1</sup> †

### Affiliations

1. Department of Computational and Systems Biology John Innes Centre Norwich United Kingdom
2. Department of Metabolic Biology John Innes Centre Norwich United Kingdom
3. Department of Crop Genetics John Innes Centre Norwich United Kingdom

† Corresponding author

## Abstract

Photosynthetic starch reserves that accumulate in Arabidopsis leaves during the day decrease approximately linearly with time at night to support metabolism and growth. We find that the rate of decrease is adjusted to accommodate variation in the time of onset of darkness and starch content, such that reserves last almost precisely until dawn. Generation of these dynamics therefore requires an arithmetic division computation between the starch content and expected time to dawn. We introduce two novel chemical kinetic models capable of implementing analog arithmetic division. Predictions from the models are successfully tested in plants perturbed by a night-time light period or by mutations in starch degradation pathways. Our experiments indicate which components of the starch degradation apparatus may be important for appropriate arithmetic division. Our results are potentially relevant for any biological system dependent on a food reserve for survival over a predictable time period.

## Introduction

Organisms must control the rate of consumption of their stored food reserves to prevent starvation during periods when food acquisition is not possible. A classic example of this requirement is provided by the response to the light/dark cycle in plants. During the day, plants utilize solar energy for carbon assimilation through photosynthesis. During the night, when solar energy is unavailable, plants utilize stored carbohydrate—usually starch—to allow continued metabolism and growth. In the model plant Arabidopsis thaliana this phenomenon is essential for productivity: mutants with defects in either the accumulation or the degradation of starch have reduced productivity and exhibit symptoms of starvation (Usadel et al., 2008; Yazdanbakhsh et al., 2011). The leaf starch content of Arabidopsis increases approximately linearly with time during the day: more than half of the carbon assimilated via photosynthesis may be stored as semi-crystalline starch granules inside chloroplasts. At night, starch content decreases approximately linearly with time such that 95% of starch is utilized by dawn (Gibon et al., 2004; Graf et al., 2010). This pattern of utilization is extremely robust, and is achieved even when darkness comes unexpectedly early (Graf et al., 2010). It is also likely to be optimal for the efficient utilization of carbohydrate over the light/dark cycle (Gibon et al., 2004; Smith and Stitt, 2007; Graf and Smith, 2011; Stitt and Zeeman, 2012; Feugier and Satake, 2013). However, despite the high importance for plant productivity of precise control of starch degradation, the way in which such dynamics are generated is very poorly understood. One intriguing possibility is the existence of a mechanism that dynamically measures the starch content and the expected time to dawn, then arithmetically divides these two quantities to compute the appropriate starch degradation rate. Such a mechanism could ensure complete utilization of available starch reserves at dawn despite variation in both the starch content at the onset of darkness and the subsequent duration of darkness. Consistent with this idea, we have recently shown that computation of the appropriate starch degradation rate in a normal night requires the circadian clock (Graf et al., 2010), which indicates how information about the expected time to dawn is obtained.

Although levels of transcripts for starch-degrading enzymes undergo large daily changes, levels of the enzymes themselves do not (Smith et al., 2004; Lu et al., 2005; Kötting et al., 2005; Yu et al., 2005; and our unpublished data). Therefore, it is likely that an arithmetic division mechanism would control flux through starch degradation at a post-translational level. Post-translational control would also permit swifter modulation of the catalytic capacity of these abundant proteins than would be possible via transcription/translation. Accordingly, in this paper we propose appropriate analog division mechanisms that operate through post-translational chemical kinetics. More generally, we also consider analog chemical kinetic schemes that generate addition, subtraction and multiplication operations. To the best of our knowledge the starch degradation system constitutes the first concrete realization of such arithmetic operations in biology. In this context, we therefore introduce two mathematical models which can both implement arithmetic division between the starch content and the expected time to dawn. We then successfully test predictions from the two models by examining the pattern of starch degradation in abnormal light/dark cycles and in a range of mutant plants defective in components of the starch degradation apparatus. Finally, our experiments also indicate which components of the starch degradation apparatus may be important for the appropriate implementation of arithmetic division.

## Results

We first investigated the robustness of a potential arithmetic division calculation to perturbations in both the numerator (starch content) and denominator (expected time to dawn). Previously, we showed that the rate of starch degradation is appropriately adjusted in response to an unexpectedly early night (imposition of darkness 8 hr after dawn on plants grown in 12-hr light/12-hr dark cycles) (Graf et al., 2010). We found that adjustment also occurs in response to an unexpectedly late night. Plants grown in 12-hr light/12-hr dark cycles were subjected to darkness at either 12 hr or 16 hr after dawn. In both cases starch content decreased approximately linearly with time during the night, but with different slopes such that starch reserves were almost exhausted by dawn (Figure 1A). We also found that similar adjustments could be performed in a cca1/lhy circadian clock mutant which has a free-running period of <24 hr (Alabadi et al., 2001). In 12-hr light/12-hr dark cycles, this mutant degrades its starch by approximately 21 hr after dawn, rather than the normal 24 hr (Graf et al., 2010; Figure 1B).When subjected to an unexpected early night, the starch degradation rate in the mutant was adjusted, such that starch reserves were again exhausted at around 21 hr after dawn (Figure 1B). Appropriate adjustments of the rate of starch degradation also occurred in wild-type plants in which environmental manipulations produced different starch contents at the end of the 12-hr light period. A subset of a uniform batch of plants was transferred to a reduced light level for a single light period, leading to a twofold reduction in the starch content at the onset of darkness. For these and control plants subjected to normal light levels, starch content decreased approximately linearly with time during the night, but with different slopes such that starch reserves were almost exhausted by dawn in both cases (Figure 1C). Appropriate adjustment of starch degradation also occurred in subsets of plants exposed to three different regimes of varying light intensity over a single light period that generated two different starch contents at the onset of darkness (Figure 1—figure supplement 1). To investigate whether this phenomenon is widespread among plants, we examined the model grass Brachypodium distachyon. Ancestors of Arabidopsis and Brachypodium diverged at least 140 Myr ago. Starch content in Brachypodium leaves increased through the light period. As in Arabidopsis, the approximately linear decrease of starch with time following either a normal night (12 hr after dawn) or an unexpectedly early night (8 hr after dawn) was such that starch reserves were almost depleted by dawn (Figure 1D).

![Figure 1.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig1-v1.jpg)

**Figure 1.:** (A) Starch turnover in Arabidopsis grown in 12-hr light/12-hr dark, then subject to unexpected early (8 hr, n = 6 individual rosettes, circles) normal (12 hr, n = 6, squares) or unexpected late (16 hr, n = 5, triangles) onset of darkness. (B) Starch turnover in Arabidopsis cca1/lhy mutant grown in 12-hr light/12-hr dark, then subject to unexpected early (9 hr, circles), or normal (12 hr, squares) onset of darkness (n = 6–10). (C) Starch turnover in Arabidopsis exposed to different daytime light levels: 90 µmol quanta m−2 s−1 (open squares) or 50 µmol quanta m−2 s−1 (filled squares) (both n = 5, previously all plants grown in 12-hr light/12-hr dark with 90 µmol quanta m−2 s−1). (D) Starch turnover in Brachypodium grown in 12-hr light/12-hr dark, then subject to unexpected early (8 hr, circles) or normal (12 hr, squares) onset of darkness (both n = 6). Error bars are standard error of the mean throughout.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Three sets of plants (each n = 5 individual rosettes) were grown in 12-hr light, 12-hr dark and were then subject to different light regimes during a single day. One set (squares) was exposed to normal light levels (180 μmol quanta m−2 s−1), the other two were shaded to about 55% of normal light level (100 μmol quanta m−2 s−1) for either the first 6 hr (circles) or the second 6 hr (triangles) of the 12-hr light period, with the normal light level for the other 6-hr period. Error bars are standard error of the mean.

Overall, these results demonstrate that the control of starch degradation at night to achieve almost complete consumption at the expected time of dawn can accommodate unexpected variation in the time of onset of darkness, starch content at the start of the night, and patterns of starch accumulation during the preceding day. Although the rate of degradation is different in a circadian clock mutant with an altered period from that in the wild-type, the capacity to adjust starch degradation in response to an unexpectedly early night is not compromised. It is also likely that the mechanism underlying this control is present in evolutionarily-distant species of plants.

Robust computation of the appropriate starch degradation rate in response to perturbations of both the expected time to dawn and starch content is clearly consistent with the implementation of arithmetic division. Since it is conceptually unclear how such a computation might be performed, we turned to mathematical modeling to generate possible mechanisms.

The fact that starch exists as large polymers that are mostly inaccessible within granule matrices means that a separate measure is likely required to provide information about the total amount of starch present at any given time. Hence, we assume the existence of a soluble molecule S whose concentration is proportional to the amount of starch in a granule. Since plants are able to adjust the rate of starch degradation according to variations in two independent quantities (the expected time to dawn and the amount of starch present), two separate species of molecule are clearly required. Therefore, we further assume the existence of a molecule T whose concentration encodes information about the expected time to dawn.

In our first model the T molecule concentration is proportional to the expected time to dawn, except during a period after dawn when its value must be reset (Figure 2B). To compute the appropriate degradation rate, the S and T molecule concentrations must therefore be arithmetically divided. We propose that computations of this form can be carried out most simply using analog chemical kinetics. As shown in Figure 2A, it is straightforward to perform addition, subtraction and multiplication operations. Subtraction can be implemented through efficient sequestration and multiplication by a two-species chemical reaction. Division is slightly more intricate, but can be implemented using the model introduced in Figure 2D (other conceptually similar models are discussed in the ‘Materials and methods’). Here, S molecules associate with the starch granule surface, where they permit starch degradation (presumably in combination with other elements, as shown in Figure 2D) and where the S molecules can also be degraded. T molecules inhibit S molecule and starch degradation by binding to S and causing its detachment from the granule surface. In this way, it can be seen intuitively that a division-like operation can be implemented (for rigorous calculations, see ‘Materials and methods’). In Figure 2F,H,J, we show the best fit of this model to the data from Figure 1A–C with good results.

![Figure 2.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig2-v1.jpg)

**Figure 2.:** (A) Pictorial summaries of schemes for analog implementation of addition, subtraction and multiplication between the concentrations of two molecules S and T. Square brackets indicate concentrations. (B) and (C) Schematic behavior of the stromal concentrations of S and T molecules ([SC] and [TC] respectively), in (B) first and (C) second arithmetic division models. In the first model, the T molecule tracks the time to expected dawn after a reset-time tr. In the second model the T molecule concentration increases with time proportionally to 1/(expected time to dawn) between tr1 and tr2. (D) and (E) Pictorial summaries of (D) first and (E) second analog arithmetic division models (not all reactions shown in pictures, for full details see ‘Materials and methods’). In the reaction schemes, molecules not attached to the starch granule surface have a ‘C’ subscript. The blue disk represents components of the starch degradation apparatus potentially activated by the S molecule in the first model, and by the ST complex in the second model. Best fits (full lines) of first (F), (H), and (J) and second (G), (I), and (K) arithmetic division models to Arabidopsis data from Figure 1A–C.

A second distinct possibility also exists for computing the appropriate degradation rate. We now assume that the T molecule concentration increases as the expected time of dawn approaches, before being reset. If this increase is such that the T molecule concentration is approximately proportional to 1/(expected time to dawn) (Figure 2C) then the appropriate degradation rate can be computed by multiplying the S and T concentrations. This is implemented by the reaction scheme shown in Figure 2E: S molecules associate with the starch granule surface, where they recruit T molecules from the stroma. The resulting molecular complex permits the degradation of starch (again presumably in combination with other elements, as shown in Figure 2E) and of the S molecule itself. The output of this second model is very similar to that of the first model (fits to data of Figure 1A–C shown in Figure 2G,I,K) in that a division computation is still performed, but now the timing information is encoded differently in the T molecule concentration. One potential difficulty is the need to pre-compute the reciprocal of the expected time to dawn. A simple possible scheme to achieve this goal is outlined in the ‘Materials and methods’. Of course, a combination of the two above models is also possible, involving both multiplication and division by factors dependent on the expected time to dawn, such that overall an appropriate division computation is still performed. However, the additional complexity required for such implementations makes such a combined model less likely.

Importantly we assume that the granule surface area does not limit the reaction rate as the granule shrinks, consistent with an approximately linear decrease of starch content with time. Accordingly, in both models the degradation reactions (for both the starch and the S molecules) occur only in region(s) of granule surface of overall fixed area as each granule shrinks. This would be the case if one or more of the additional components required for starch degradation (illustrated in Figure 2D,E) is present at a fixed number on the granule surface as the granule shrinks. Clearly the assumption of a non-limiting surface area cannot remain true if the granule shrinks to very small volumes, as could happen at the end of the night. However, our models still fit the experimental data well even at these times (see Figure 2F–K).

Taken together, our modeling results show that arithmetic division (as well as other arithmetic operations) can be implemented simply using analog post-translational chemical kinetics. Furthermore, output from both models fits our experimental data well. We note that there is some variation in the fitted parameters for both models (see Tables 3–6), which arises due to variation between experimental data sets even for a single genotype. Such variation is widely observed for measurements of primary metabolites over the light/dark cycle and could arise from batch to batch variation in expression levels of degradation or clock components.

As the fit of the two models to the data is equally good, distinguishing between them is currently challenging. However, we can test two critical predictions common to both models. The first prediction is that the degradation rate is continuously computed via arithmetic division during the night. Such a scheme clearly has advantages in its flexibility and potential to recover from unexpected perturbations. To test whether this prediction is correct, we interrupted a normal night with a period of light, ending 5 hr before the expected time of dawn. During this night-time light period starch accumulated to levels very similar to those present at the end of the day-time light period. Comparison of the rate of starch degradation following the night-time light period with the rate before this period, and with the rate that would have been expected over a normal 12-hr night, allowed a robust assessment of whether the degradation rate had been reset. We confirmed that the night-time light period did not re-entrain the circadian clock, by monitoring expression of the clock gene LHY (see ‘Materials and methods’ and Figure 3—figure supplement 1). For three independent experiments we found that the rates of starch degradation immediately following the night-time light period (between 19 hr and 21 hr after dawn) were significantly greater than both the corresponding actual rates before this period (between 12 hr and 14 hr after dawn) and the corresponding rates that would have been expected during a normal 12-hr night, see insets in Figure 3A–C (p = 1.6 × 10−3 and 3.8 × 10−5, respectively, details of the statistical analysis in the ‘Materials and methods’). The latter rates are those that would have ensured the complete depletion of the starch content measured at 12 hr at the expected time of dawn (24 hr). We obtained the same result by changing the duration and the starting time of the night-time light period (Figure 3D). This increase in starch degradation rate is consistent with our prediction that the rate is continuously computed during the night, rather than set only once at the first onset of darkness. In Figure 3 we show the best fits of the first model to the data, with good results. As before, the second model produced very similar fits (see Figure 3—figure supplement 2).

![Figure 3.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig3-v1.jpg)

**Figure 3.:** Arabidopsis plants grown in 12-hr light/12-hr dark were subjected to onset of darkness at 12 hr, followed by an unexpected period of light, followed by extended darkness. (A)–(C) Three data sets (n = 12 individual rosettes, except n = 10 for C), in which the unexpected period of light was between 14 hr and 19 hr after dawn. (D) In the fourth dataset (n = 12) the period of light was between 16 hr and 20 hr after dawn. Full lines are best fits to the first division model. The second model produces very similar fits (see Figure 3—figure supplement 2). The insets show the respective starch degradation rates computed from the 12-hr and 14-hr experimental time points (dark grey bars) compared to those computed from the 19-hr and 21-hr experimental time points in panels (A–C) or the 20-hr and 22-hr time points in panel (D) (light grey bars). The white bars are the expected starch degradation rates in a normal 12 hr night, that is rates that would have ensured the complete depletion of the starch content measured at 12 hr at the time of expected dawn (24 hr). Error bars are standard error of the mean throughout.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** LHY transcript levels (relative to ACT2) measured in Arabidopsis plants kept in continuous darkness after a normal night (squares), or subjected to a 5-hr night-time light period between 14 hr and 19 hr after dawn, and then kept in continuous darkness (circles), as in Figure 3A–C. Data for the night-time light period are from the same plants as in Figure 3B. n = 5 individual rosettes, error bars are standard error of the mean. The night-time light period is shown on top of graph.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Error bars are standard error of the mean throughout.

The second prediction from the models concerns the effects on starch degradation of perturbations in components of the arithmetic division or degradation apparatus. To reproduce the normal pattern—in which starch is almost completely degraded by the expected time of dawn—our models require that a factor involved in specifying the relative degradation rates of the starch and S molecules must be fine-tuned to one (see ‘Materials and methods’). If instead this factor is <1, so that the starch is degraded too slowly, then rather than complete degradation the models predict that only a certain percentage of the starch will be consumed during the night regardless of the starch content at the end of the preceding light period (for full calculations, see ‘Materials and methods’). Accordingly, we predict that perturbations to parts of the arithmetic division or degradation apparatus might result in degradation of only a fraction of starch during the night. Interestingly, several mutants defective in proteins involved in, or related to, starch degradation exhibit approximately linearly decreasing starch content with time during the night, but have an elevated starch content at the end of the night. These include beta-amylase mutants bam3 and bam4, the debranching enzyme mutant isa3, and mutants lacking phosphoglucan water dikinase (pwd, also called gwd3), a glucan phosphate phosphatase (sex4) and a glucan phosphate phosphatase-like protein (lsf1) (Smith, 2012). We showed previously that this abnormal pattern of starch turnover was rapidly regained in lsf1 mutants that were transferred to normal light/dark cycles after starch was reduced to very low levels by prolonged darkness (Comparot-Moss et al., 2010). We re-analyzed these data and also performed a similar experiment on the sex4 mutant. For both mutants, we found that the fraction of end-of-light period starch content degraded during the night was approximately the same on successive nights (around 30% for the sex4 mutant and 45% for the lsf1 mutant), regardless of the starch content at the end of the respective preceding light period. This resulted in a progressive increase in the end-of-night starch content to an approximately constant value over 3–4 days after return to normal light/dark cycles (Figure 4A,B). Thus the pattern of starch degradation in these mutants is as predicted from the models for a situation in which the above factor is incorrectly set to a value <1.

![Figure 4.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig4-v1.jpg)

**Figure 4.:** (A) Starch content in wild-type (WT) plants and lsf1 and sex4 mutant plants during four days of 12-hr light/12-hr dark following 5 days of continuous darkness, where plants were transferred back into the light (at time 0 hr on the x-axis) 132 hr after the end of the previous light period (n = 6 individual rosettes). Data for wild-type and lsf1 plants are from (Comparot-Moss et al., 2010). (B) The percentage of starch degraded during each of the four nights in (A). (C)–(E) Starch content in lsf1, sex4 and pwd mutant plants grown in 12-hr light/12-hr dark cycles then subject to unexpected early (8 hr, circles) or normal (12 hr, squares) onset of darkness (n = 5). The continuous and dashed lines are linear fits to the normal and early night datasets respectively. (F) For each of the labeled genotypes, R is the ratio between the starch degradation rates (each normalized by their respective end-of-light period starch content and as determined from the linear fits) during the normal and early nights. The dashed line shows the expected value of R for wild-type (WT) plants, that is, ratio of rates that would ensure the complete depletion of the starch content in all cases at the time of expected dawn (24 hr). See ‘Materials and methods’ for details about the linear fitting and the calculation of R. Error bars are standard error of the mean throughout. Figure 4—figure supplement 1 shows the datasets used to calculate R for WT, bam3, bam4 and isa3.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Starch content in wild-type (WT), bam3, bam4, isa3 mutant Arabidopsis plants grown in 12-hr light, 12-hr dark cycles then subject to unexpected early (8 hr, circles) or normal (12 hr, squares) onset of darkness (n = 6 individual rosettes for WT, n = 5 for mutants; the WT dataset analyzed here is the one already shown in Figure 1A). The continuous and dashed lines are linear fits to the normal and early night datasets respectively. Error bars are standard error of the mean throughout.

We next attempted to gain experimental insight into how the arithmetic division mechanism modulates flux through the starch degradation pathway. In our models the computation of the starch degradation rate is the result of interactions between the molecules encoding the information about starch content and time to dawn (S and T) and the starch degradation apparatus. If this idea is correct, we expect that mutants lacking components of the degradation apparatus involved in these interactions may also lack the ability to adjust the rate of starch degradation in response to variation in starch content or time of onset of darkness.

To look for a mutant in this category, we imposed an unexpectedly early night on six mutants, each lacking a protein involved in starch degradation (lsf1, sex4, bam3, bam4, isa3, pwd). All six mutants show approximately linear decreases in starch content with time during the night, but they have higher end-of-night starch contents than wild-type plants. This mutant collection covers the majority of currently-known components of the chloroplastic starch degradation apparatus. For five of the six mutants, the rates of starch degradation (as determined from linear fits) were lower during an unexpectedly early night (starting 8 hr after dawn) than in a normal night (starting 12 hr after dawn), as is the case in wild-type plants (Figure 4C,D and Figure 4—figure supplement 1). To quantify the adjustment of the starch degradation rates in the mutants, we calculated the ratio R between the degradation rates (normalized by the respective end-of-light period starch content) during the normal and the early night. For wild-type plants, the expected value of R is 16/12 ≈ 1.33, that is, the ratio between the expected lengths of the early and the normal night. In Figure 4F we show that the values of R for five of the six mutants are consistent with the wild-type value.

However for the sixth mutant, pwd, the rate of starch degradation was not adjusted in response to an unexpectedly early night (Figure 4E,F), as we found an R which was significantly different from the wild-type value (p = 0.01, details of the statistical analysis in the ‘Materials and methods’). This finding indicates that PWD—phosphoglucan, water dikinase—may be a node at which information about expected time to dawn and starch content is integrated to set an appropriate rate of starch degradation.

PWD contributes to a cycle of phosphorylation and dephosphorylation of glucosyl residues within starch polymers that is essential for normal starch degradation. Two enzymes—glucan water dikinase (GWD) and PWD—add phosphate groups to starch polymers at the granule surface, and two further enzymes SEX4 and LSF2—remove them. All four enzymes are necessary for normal rates of starch degradation, and loss of GWD almost completely prevents degradation at night (Smith, 2012). The phosphate groups are thought to disrupt the ordered packing of the starch molecules at the granule surface, allowing access to starch degrading enzymes (beta-amylases and isoamylase 3). Subsequent removal of the phosphate groups is essential for full degradation of the starch polymers because the phosphates block the action of the exo-acting beta-amylases (Baunsgaard et al., 2005; Kötting et al., 2005; Ritte et al., 2006; Hejazi et al., 2009). The cycle as a whole is thus an attractive candidate for integration of factors that modulate flux through starch degradation.

Because the phosphorylation/dephosphorylation cycle modifies the granule surface, it is a potential candidate not only for flux modulation but also for the storage of information about starch content. To discover whether phosphate groups may provide information about starch content, we measured the amount of granule-bound phosphate (on the 6-position of glucosyl residues, representing about 80% of the total phosphate) over the light/dark cycle. If phosphorylation simply tracks starch polymer synthesis during the day, phosphate levels per unit mass of starch will be constant and will thus contain no information about starch content. Surprisingly, however, we found a large increase/decrease in the level of phosphate per unit mass of starch over the light/dark cycle (Figure 5). This discovery implies that the S molecule may be a modulator of activities of enzymes of the phosphorylation/dephosphorylation cycle, thus generating a daily pattern of change in the accessibility of the granule surface to hydrolytic enzymes that approximately tracks starch content.

![Figure 5.](https://cdn.elifesciences.org/articles/00669/elife-00669-fig5-v1.jpg)

**Figure 5.:** Results are normalized by total amount of glucose (Glc) in starch at each time point. Starch was extracted from rosettes of 26-day-old plants. n = 3 pools of 10 rosettes except at 24 hr time point, with n = 2 pools of 15 rosettes. Error bars represent the range (i.e., error bar edges correspond to highest and lowest values measured).

## Discussion

Overall, our work provides a new framework and perspective for understanding the control of reserve utilization in plants at night. Our experiments provide strong support for an implementation of arithmetic division in night-time starch degradation. We used mathematical modeling to generate two simple mechanisms capable of analog implementation of such an operation. Predictions from the models were then verified and a potential point identified at which the division computation could be integrated into the starch degradation pathway. We also showed that the phosphorylation state of the starch granule surface could provide information about starch content through the day.

Our analysis may also be relevant to a broader class of biological processes, where food reserves accumulated in advance of periods of predictable length without further food intake are just sufficient to permit survival to the expected end of the period. For example, migrating little stints (Calidris minuta) arriving at their Arctic summer breeding grounds after a 5000-km journey have sufficient remaining lipid reserves for an average of only 0.6 days (Tulp et al., 2009). During the 4-month fast period of egg-incubating male emperor penguins (Aptenodytes forsteri), lipid reserves are used such that they reach a critical depletion level at approximately the point at which the females are expected to return. Unexpected extension of the fast period leads to catabolism of protein and abandonment of offspring in favor of hunting for food (Groscolas and Robin, 2001). As in Arabidopsis leaves, the rate of reserve utilization in these examples can potentially be computed by arithmetically dividing the reserve levels by the anticipated time of fasting.

It is a longstanding idea that cells are able to use proteins to store and process information through networks of interactions (Bray, 1995). Understanding how such biochemical networks work and what kind of computations they perform is an ongoing challenge (see Deckard and Sauro, 2004; Lim et al., 2013). Our analysis here has underlined the utility of analog chemical kinetics in performing arithmetic computations in biology. Importantly, we have for the first time provided a concrete example of a biological system where such a computation is of fundamental importance. This contrasts to previous work where elegant theoretical implementations of arithmetic operations lacked specific biological applications (Cory and Perkins, 2008; Buisman et al., 2009). Analog chemical kinetic approaches may potentially also be useful for calculations in synthetic biology applications (Benenson, 2012), where they are likely to prove much simpler to implement than alternative schemes based on much more complex digital circuitry.

## Materials and methods

### Plant material

Arabidopsis thaliana (in the Col0 background, except for cca1/lhy and its wild-type which were in the Ws background) and Brachypodium distachyon (Bd21) plants were grown as in Graf et al. (2010) on soil in 12-hr light/12-hr dark with 200 µmol quanta m−2 s−1 illumination at a constant temperature of 20°C for 21 days.

### Measurement of starch

Plants were harvested and extracted in dilute perchloric acid for analysis of starch, which was then quantified enzymatically as previously described (Graf et al., 2010).

### Transcript analysis

RNA was extracted from plant material and qPCR was performed as in Graf et al. (2010). Oligonucleotide primer sequences were as follows:

<table>
  <tbody>
    <tr>
      <td>Primer</td>
      <td>Sequence 5′ to 3′</td>
    </tr>
    <tr>
      <td>LHY-F AT1G01060</td>
      <td>GACTCAAACACTGCCCAGAAGA</td>
    </tr>
    <tr>
      <td>LHY-RAT1G01060</td>
      <td>CGTCACTCCCTGAAGGTGTATTT</td>
    </tr>
    <tr>
      <td>ACT2-F AT3G18780</td>
      <td>ACTTTCATCAGCCGTTTTGA</td>
    </tr>
    <tr>
      <td>ACT2-R AT3G18780</td>
      <td>ACGATTGGTTGAATATCATCAG</td>
    </tr>
  </tbody>
</table>

### Starch phosphate measurements

Starch granules were prepared as in Ritte et al. (2000) and used immediately without drying. Granules were resuspended in two pellet volumes of water and boiled for 15 min then digested with 20 U amylogucosidase (Roche) and 2 U α-amylase (Megazyme) in 100 mM Na acetate pH 4.8 for 9 hr at 37°C. Glucose was assayed enzymatically following (Hargreaves and ap Rees, 1988) and glucose 6-phosphate was measured enzymatically using the fluorimetric assay of (Zhu et al., 2009).

### Mathematical Modelling

#### Quantification of the starch content and the expected time to dawn

Starch is laid down as semi-crystalline granules in chloroplasts in the light. Granule surfaces are then subject to degradation during periods of darkness. We assume here that the computation of the degradation rate is performed autonomously inside each chloroplast. In order to correctly compute the appropriate starch degradation rate, knowledge of the total chloroplast starch content is required. We assume that there exists a molecule S whose number $N_{S}^{tot}$ is proportional to the total starch content ΔStot in a chloroplast at the end of a light period:

$$
ΔS^{tot}=\alphaN_{S}^{tot}.
$$

We also assume that the S molecule can exchange rapidly between the granule surfaces and the surrounding chloroplast compartment. Moreover, we propose the existence of a molecule T that encodes information about the expected time to dawn. The T molecule dynamics will presumably be controlled by the circadian clock and are assumed to be independent of the starch degradation process.

In the first model (Figure 2B,D), the T concentration in the compartment surrounding the granules, [TC], is proportional to the expected time to dawn Δt = tday − t during most of the light/dark cycle. Note, however, that this cannot be true at all times, as around the time of expected dawn, after [TC] has dropped to low levels, its value must be reset. So, if dawn occurs at t = 0, we assume that:

$$
[T_{C}]={\beta\frac{t_{day}−t_{r}}{t_{r}}t 0\leqt\leqt_{r}\beta(t_{day}−t) t_{r}\leqt\leqt_{day},
$$

where β is a constant, tday is the period of the light/dark cycle and tr is the reset-time after which [TC] starts tracking the time to expected dawn (see Figure 2B).

These dynamics could be the result of production of T at a constant rate, with a comparatively low degradation rate for 0 ≤ t ≤ tr. During tr ≤ t ≤ tday, [TC] is assumed to decrease linearly with time, with a rate β. This could happen through an efficient sequestration of TC by another molecule which is produced at a rate β and is degraded at a comparatively low rate for tr ≤ t ≤ tday. These simple [TC] dynamics can reproduce the available experimental data on starch degradation during the hours after dawn. Experimentally, if the onset of darkness unexpectedly occurs only 6 hr after the previous dawn in plants previously grown in 12-hr light/12-hr dark conditions, the starch is degraded too quickly, while for an unexpected onset of darkness at 8 hr, the starch degradation occurs at the appropriate rate (Lu et al., 2005; Graf et al., 2010). This can be explained by the above model, with the T dynamics given in Equation 1 and assuming a reset time tr ≳ 8 hr, as we have [TC] < βΔt during the resetting period, and hence the starch degradation rate will initially be too high.

Nevertheless, if the early night condition is maintained each day for a few days in succession, acclimation occurs: the appropriate starch degradation rate is computed even after a light period as short as 4 hr. This suggests that tr can be reduced, thereby resetting [TC] more quickly, and hence allowing the arithmetic division mechanism to work effectively under the new light/dark cycle conditions.

In the second model (Figure 2C,E), we assume that for most of the light/dark cycle [TC] is proportional to 1/(tday − t). Again, this cannot be true around dawn, where [TC ] must be reset. For the sake of simplicity, we assume that during the reset period [TC] has a linear profile with time:

$$
[T_{C}]={\frac{\beta}{t_{day}+t_{r1}−t_{r2}}(\frac{t+t_{day}−t_{r2}}{t_{day}−t_{r1}}+\frac{t_{r1}−t}{t_{day}−t_{r2}}) 0\leqt\leqt_{r1}\frac{\beta}{t_{day}−t} t_{r1}\leqt\leqt_{r2}\frac{\beta}{t_{day}+t_{r1}−t_{r2}}(\frac{t−t_{r2}}{t_{day}−t_{r1}}+\frac{t_{day}+t_{r1}−t}{t_{day}−t_{r2}}) t_{r2}\leqt\leqt_{day},
$$

where β is a constant, and tr1 and tr2 define the time interval in which [TC] is proportional to 1/Δt (see Figure 2C). In the second model, these dynamics can also explain why starch degradation is too rapid following a very early and unexpected onset of darkness. During the resetting period after dawn [TC] > β/Δt, and therefore the starch degradation rate will initially be too high.

One apparent difficulty with the second model is in finding a simple way to generate a T molecule concentration that scales as 1/Δt. In fact, kinetics of this kind are simple to produce. For example, if T promotes further production of the T molecule itself, with a quadratic nonlinearity, then, away from saturation, we have $\frac{d[T_{C}]}{dt}=η[T_{C}]^{2}$. It is straightforward to show that the solution to this equation is:

$$
[T_{C}](t)=\frac{[T_{C}](t_{r1})}{1−η(t−t_{r1})[T_{C}](t_{r1})}.
$$

For [TC](t) = β/Δt as required, we then find [TC](tr1) = β/(tday − tr1) and η = 1/β.

Of course, more complex schemes could also generate a similar behavior; we simply wish to point out here that a 1/Δt behavior for [TC] is a plausible assumption.

### Two models that appropriately calculate the starch degradation rate

We now describe in full mathematical detail the models introduced in the main text.

#### Model 1

In this model, division is implemented by dividing the S concentration by the T concentration, where the T molecule concentration is proportional to Δt for most of the light/dark cycle. Such a division can be implemented by the following set of reactions:

$$
r_{S}:S_{C}↔Sr_{ST1}:S+T_{C}→STr_{ST2}:ST→S_{C}+T_{C}r_{D1}:S→∅r_{D2}:S+Starch→S,
$$

where the subscript ‘C’ refers to molecules in the compartment surrounding the granules. The reversible rS reaction describes exchange of the S molecules between the granule surface and surrounding compartment, with forward reaction parameter fS and backward rate bS. The T molecules can be recruited by the S molecules on the granule surface (reaction rST1, reaction parameter fST1) and the resulting complex can then dissociate leading to the detachment of S and T from the granule surface (reaction rST2, rate fST2). The S molecule on the granule can be degraded (reaction rD1, reaction parameter fD1) or it can permit starch degradation (reaction rD2, reaction parameter fD2).

In all the calculations in this section, we assume that bS ≫ fD1 and that the dynamics of the S and T molecules can be taken to be in quasi-steady-state. As described in the main text, we assume that the degradation reactions (for both the starch and the S molecule) can only occur in a region of overall fixed area Ad as each granule shrinks. We also assume that all granules in a given chloroplast are approximately equal in area and volume. The differential equations describing the dynamics of the total number of S molecules, $N_{S}^{tot}$, and the total amount of starch in a chloroplast, ΔStot, are:

$$
\frac{dN_{S}^{tot}}{dt}=n\frac{dN_{S}}{dt}=−nf_{D1}[S]A_{d}\frac{dΔS^{tot}}{dt}=n\frac{dΔS}{dt}=−nm_{S}f_{D2}[S]A_{d}=−n\mu=−\mu^{tot},
$$

where mS is the amount of starch degraded by an S molecule in a single degradation reaction, n is the number of granules in the chloroplast, μ is the starch degradation rate for an individual granule and μtot is the total starch degradation rate.

Using Equation 4, we find that $\frac{dΔS^{tot}}{dt}=−\mu^{tot}=\frac{m_{S}f_{D2}}{f_{D1}}\frac{dN_{S}^{tot}}{dt}$. We assumed that at the beginning of the dark period $ΔS^{tot}=\alphaN_{S}^{tot}$. It is easy to show that, if $\alpha=m_{S}\frac{f_{D2}}{f_{D1}}$, such a proportionality between the starch content and the number of S molecules continues to hold true throughout the degradation process. The total number of S molecules is $N_{S}^{tot}=[S_{C}]V+n[S]A+n[ST]A,$ where V is the compartmental volume surrounding the granules, and A is the surface area of a granule. Using the above quasi-steady state assumption and the law of mass action, we obtain:

$$
[S]=\frac{k_{S}[S_{C}]}{1+k_{ST1}[T_{C}]},[ST]=\frac{f_{ST1}}{f_{ST2}}\frac{k_{S}[S_{C}][T_{C}]}{1+k_{ST1}[T_{C}]},
$$

with kS = fS/bS, kST1 = fST1/bS. Assuming that nkS A ≪ V, bS/fST2 ≲1, then n[S] A, n[ST]A ≪ [SC]V, and hence:

$$
[S_{C}]=\frac{N_{S}^{tot}}{V}=\frac{N_{S}^{tot}}{nV_{0}},
$$

where we used the observation that the number of starch granules per unit volume inside the chloroplast is approximately constant, that is, the number of granules n is proportional to the chloroplast volume V (Crumpton-Taylor et al., 2012). For the T molecule, assuming the concentration in the compartment surrounding the granules is regulated by the circadian clock, we have (for much of the light/dark cycle, see Equation 1):

$$
[T_{C}]=\betaΔt.
$$

The starch degradation rate for an individual granule is then:

$$
\mu=m_{S}f_{D2}[S]A_{d}=m_{S}f_{D2}A_{d}k_{S}\frac{[S_{C}]}{1+k_{ST1}[T_{C}]}.
$$

According to Equation 6, [SC] is proportional to the amount of starch in a granule, whereas from Equation 7, [TC] is proportional to the expected time to next dawn. Sufficiently far from the time of expected dawn when kST1 [TC] ≫ 1, we then have:

$$
\mu=m_{S}f_{D2}A_{d}k_{S}\frac{\frac{N_{S}^{tot}}{nV_{0}}}{k_{ST1}\betaΔt}.
$$

Hence, summing over all the granules, and using that $ΔS^{tot}=\alphaN_{S}^{tot}=\frac{m_{S}f_{D2}}{f_{D1}}N_{S}^{tot}$ (see above in this section), the total starch degradation rate is:

$$
\frac{dΔS^{tot}}{dt}=−\mu^{tot}=−\frac{f_{D1}A_{d}k_{S}}{k_{ST1}V_{0}\beta}\frac{ΔS^{tot}}{Δt}.
$$

According to this equation, starch contents are completely depleted by the time of expected dawn, and for a degradation rate $\mu^{tot}=\frac{ΔS^{tot}}{Δt}$ with normalization relation $\frac{f_{D1}A_{d}k_{S}}{k_{ST1}V_{0}\beta}=1$, starch contents decrease linearly with time.

#### Model 2

In this model, division is now implemented by multiplying the T concentration by the S concentration, where the T molecule concentration is proportional to 1/Δt for most of the light/dark cycle. Such a multiplication can be implemented by the following set of reactions:

$$
r_{S}:S_{C}↔Sr_{ST1}:S+T_{C}→STr_{ST2}:ST→S+T_{C}r_{D1}:ST→T_{C}r_{D2}:ST+Starch→ST.
$$

Reversible reaction rS again describes the exchange of S molecules between the surrounding compartment and the granule surface (forward reaction parameter fS and backward reaction parameter bS). S can recruit T molecules from the surrounding compartment and form the complex ST (reaction rST1, reaction parameter fST). As the ST complex dissociates, T is released back in the stroma, while S remains attached to the granule (reaction rST2, reaction parameter bST). The ST complex permits S degradation, with T released from the granule surface (reaction rD1, reaction parameter fD1), as well as starch degradation (reaction rD2, reaction parameter fD2). Similar to our assumptions for Model 1, we assume here that bST ≫ fD1, with a fixed degradation area Ad for the starch as well as for the S molecule as each granule shrinks. We also again assume that the dynamics of S and T can be taken to be in quasi-steady-state and that all granules in a given chloroplast have approximately equal areas and volumes.

The differential equations describing the dynamics of the total amount of starch in a chloroplast, ΔStot, and of the total number of S molecules, $N_{S}^{tot}$, are now:

$$
\frac{dN_{S}^{tot}}{dt}=n\frac{dN_{S}}{dt}=−nf_{D1}[ST]A_{d}\frac{dΔS^{tot}}{dt}=n\frac{dΔS}{dt}=−nm_{S}f_{D2}[ST]A_{d}=−n\mu=−\mu^{tot}.
$$

The above relations again ensure that if $\alpha=m_{S}\frac{f_{D2}}{f_{D1}}$, then $ΔS^{tot}=\alphaN_{S}^{tot}$ at all times during degradation. The total number of S molecules is $N_{S}^{tot}=[S_{C}]V+n[S]A+n[ST]A$, where V is the compartmental volume surrounding the granules, and where A is the surface area of a granule. Using the above quasi-steady state assumption and the law of mass action, we obtain:

$$
[S]=k_{S}[S_{C}],[ST]=k_{ST}k_{S}[S_{C}][T_{C}],
$$

with kS = fS/bS and kST = fST/bST. We assume that nkS A ≪ V, kST[TC] ≲ 1, giving n[S]A, n[ST]A ≪ [SC]V, and hence:

$$
[S_{C}]=\frac{N_{S}^{tot}}{V}=\frac{N_{S}^{tot}}{nV_{0}},
$$

where we again used the observation that the number of starch granules per unit volume inside the chloroplast is approximately constant, that is, the number of granules n is proportional to the volume V. For the T molecules, we have (for much of the light/dark cycle, see Equation 2):

$$
[T_{C}]=\beta/Δt.
$$

The starch degradation rate for an individual granule is therefore:

$$
\mu=m_{S}f_{D2}[ST]A_{d}= m_{S}f_{D2} A_{d}k_{ST}k_{S}[S_{C}][T_{C}].
$$

According to the above equation, [TC] is proportional to the reciprocal of the expected time to the next dawn. Thus, we have:

$$
\mu=m_{S}f_{D2} A_{d}k_{ST}k_{S}\beta\frac{\frac{N_{S}^{tot}}{nV_{0}}}{Δt}.
$$

Summing over all the granules, and using $ΔS^{tot}=\alphaN_{S}^{tot}=\frac{m_{S}f_{D2}}{f_{D1}}N_{S}^{tot}$, the total starch degradation rate is

$$
\frac{dΔS^{tot}}{dt}=−\mu^{tot}=−f_{D1}A_{d}\beta\frac{k_{ST}k_{S}}{V_{0}}\frac{ΔS^{tot}}{Δt}.
$$

According to this equation, starch contents are completely depleted by the time of expected dawn, and for a degradation rate $\mu^{tot}=\frac{ΔS^{tot}}{Δt}$ with normalization relation $f_{D1}A_{d}\beta\frac{k_{ST}k_{S}}{V_{0}}=1$, starch contents decrease linearly with time.

### Calculation of the starch content during the degradation process

In this section we describe how starch contents during the degradation process were calculated using the equations previously derived.

#### Model 1

The starch content as function of time is obtained by solving the equation $\frac{dΔS^{tot}}{dt}=−\mu^{tot}$. For Model 1, from the previous section, we have:

$$
\mu^{tot}=m_{S}f_{D2}A_{d}k_{S}n\frac{[S_{C}]}{1+k_{ST1}[T_{C}]}.
$$

As we showed, [SC] can, at all times, be approximated by $[S_{C}]=\frac{N_{S}^{tot}}{nV_{0}}=\frac{ΔS^{tot}}{\alphanV_{0}}=\frac{f_{D1}}{m_{S}f_{D2}nV_{0}}ΔS^{tot}$; therefore, we find:

$$
\frac{dΔS^{tot}}{dt}=−f_{D1}A_{d}\frac{k_{S}}{V_{0}}\frac{ΔS^{tot}}{1+k_{ST1}[T_{C}]}.
$$

If we put $\gamma=\frac{f_{D1}A_{d}k_{s}}{k_{ST1}V_{0}\beta}$, we then have

$$
\frac{dΔS^{tot}}{dt}=−\gamma\frac{\betak_{ST1}ΔS^{tot}}{1+k_{ST1}[T_{C}]}.
$$

To convert this equation into one for starch content ρS in mg g−1 FW, we use ρS = (ΔStot/n) ν, (ΔStot/n) being the amount of starch in a single granule in mg and ν the number of starch granules g−1 FW. This leads to

$$
\frac{dρ_{S}}{dt}=−\gamma\frac{ρ_{S}}{(\betak_{ST1})^{−1}+([T_{C}]/\beta)}.
$$

Given Equation 1 for [TC], the above differential equation can be exactly solved analytically. If we define the functions:

$$
f^{(1)}(x,y)=(\frac{(\betak_{ST1})^{−1}+\frac{t_{day}−t_{r}}{t_{r}}y}{(\betak_{ST1})^{−1}+\frac{t_{day}−t_{r}}{t_{r}}x})^{−\gamma\frac{t_{r}}{t_{day}−t_{r}}},f^{(2)}(x,y)=(\frac{(\betak_{ST1})^{−1}+t_{day}−y}{(\betak_{ST1})^{−1}+t_{day}−x})^{\gamma},
$$

and t* is the time at which degradation starts, with ρS(t*) = ρ0 the corresponding starch content, then, for $0\leqt^{∗}\leqt_{r}$, the solution is:

$$
ρ_{S}(t)={ρ_{0}f^{(1)}(t^{∗},t) t^{∗}\leqt\leqt_{r}ρ_{0}f^{(1)}(t^{∗},t_{r})f^{(2)}(t_{r},t) t_{r}\leqt\leqt_{day},
$$

while, for $t_{r}\leqt^{∗}\leqt_{day}$, the solution becomes:

$$
ρ_{S}(t)={ρ_{0}f^{(2)}(t^{∗},t) t^{∗}\leqt\leqt_{day}ρ_{0}f^{(2)}(t^{∗},t_{day})f^{(1)}(0,t−t_{day}) t_{day}\leqt\leqt_{day}+t_{r}.
$$

According to these equations, for (βkST1)−1 sufficiently small, starch contents are almost completely depleted by the time of expected dawn, and for γ = 1, starch contents decrease linearly with time for most of the dark period, except around the time of expected dawn, when [TC] is being reset (see Figure 2B).

#### Model 2

Similarly, for Model 2, we have:

$$
\frac{dρ_{S}}{dt}=−\gammaρ_{S}\frac{[T_{C}]}{\beta},
$$

where $\gamma=f_{D1}A_{d}\beta\frac{k_{ST}k_{S}}{V_{0}}$ and [Tc] is defined by Equation 2. Then, given the three functions:

$$
f^{(1)}(x,y)=exp{−\frac{\gamma}{2}(y−x)(\frac{2}{\tau_{2}}−\frac{y+x}{\tau_{1}^{2}})},f^{(2)}(x,y)=(\frac{t_{day}−y}{t_{day}−x})^{\gamma},f^{(3)}(x,y)=exp{−\frac{\gamma}{2}(y−x)(\frac{2}{\tau_{3}}−\frac{y+x}{\tau_{1}^{2}})},
$$

with

$$
\frac{1}{\tau_{1}^{2}}=\frac{t_{r2}−t_{r1}}{(t_{day}+t_{r1}−t_{r2})(t_{day}−t_{r1})(t_{day}−t_{r2})},\frac{1}{\tau_{2}}=\frac{1}{(t_{day}+t_{r1}−t_{r2})}(\frac{t_{day}−t_{r2}}{t_{day}−t_{r1}}+\frac{t_{r1}}{t_{day}−t_{r2}}),\frac{1}{\tau_{3}}=\frac{1}{(t_{day}+t_{r1}−t_{r2})}(\frac{t_{day}+t_{r1}}{t_{day}−t_{r2}}−\frac{t_{r2}}{t_{day}−t_{r1}}),
$$

if the initial condition is ρS(t*) = ρ0, and $0\leqt^{∗}\leqt_{r1}$, the exact solution is:

$$
ρ_{S}(t)={ρ_{0}f^{(1)}(t^{∗},t) t^{∗}\leqt\leqt_{r1}ρ_{0}f^{(1)}(t^{∗},t_{r1})f^{(2)}(t_{r1},t) t_{r1}<t\leqt_{r2}ρ_{0}f^{(1)}(t^{∗},t_{r1})f^{(2)}(t_{r1},t_{r2})f^{(3)}(t_{r2},t) t_{r2}<t\leqt_{day}.
$$

For $t_{r1}\leqt^{∗}\leqt_{r2}$, we have:

$$
ρ_{S}(t)={ρ_{0}f^{(2)}(t^{∗},t) t^{∗}\leqt\leqt_{r2}ρ_{0}f^{(2)}(t^{∗},t_{r2})f^{(3)}(t_{r2},t) t_{r2}\leqt\leqt_{day}ρ_{0}f^{(2)}(t^{∗},t_{r2})f^{(3)}(t_{r2},t_{day})f^{(1)}(0,t−t_{day}) t_{day}\leqt\leqt_{r1}+t_{day},
$$

and for $t_{r2}\leqt^{∗}\leqt_{day}$:

$$
ρ_{S}(t)={ρ_{0}f^{(3)}(t^{∗},t) t^{∗}\leqt\leqt_{day}ρ_{0}f^{(3)}(t^{∗},t_{day})f^{(1)}(0,t−t_{day}) t_{day}\leqt\leqt_{r1}+t_{day}ρ_{0}f^{(3)}(t^{∗},t_{day})f^{(1)}(0,t_{r1})f^{(2)}(t_{r1},t−t_{day}) t_{r1}+t_{day}\leqt\leqt_{r2}+t_{day}.
$$

From the previous equations, it is easily seen that for tr2 close to tday starch contents are almost completely depleted by the time of expected dawn, and for γ = 1, starch contents decrease linearly with time for $t_{r1}\leqt\leqt_{r2}$, although this linearity no longer holds around the time of expected dawn, when [TC] is being reset (see Figure 2C).

### Parameters

For Model 1, the values of the following parameters are required: γ, (βkST1)−1, ρ0, tr; and for Model 2: γ, ρ0, tr1 and tr2.

In order to fit the data from the night-time light period experiments, we also considered the possibility that the T dynamics given by Equations 1 and 2 (see also Figure 2B,C) can be phase shifted by a time t0. The addition of t0 as an extra fitting parameter for the night-time light period experiments was justified by our data on transcripts of the clock gene LHY (Figure 3—figure supplement 1), showing that the night-time light period may induce a phase shift in the expression of some genes.

The phase shift of the T dynamics determines a shift in the time of expected dawn, that, in Model 1, is defined as the time at which [TC] falls to zero (see Equation 1 and Figure 2B) and which in Model 2 is the time at which [TC] would diverge without a reset (see Equation 2 and Figure 2C). Therefore, if the T dynamics are phase shifted by t0, in our models the starch degradation rates are adjusted in such a way so as to deplete the starch reserves at (24 + t0) hr after the previous dawn, instead of the normal 24 hr. We found this phenotype in cca1/lhy plants, which run out of starch earlier than 24 hr after the previous dawn. Hence, to reproduce the phenotype of cca1/lhy in our models, t0 was also used as a fitting parameter. A more extensive discussion about cca1/lhy can be found below in the ‘Mutant phenotypes’ section.

A full list of the system parameters is shown in Tables 1 and 2.

**Table 1.**
 Full list of the system parameters for Model 1


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ρ0</td>
      <td>Starch content at the beginning of the dark period.</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>Normalization variable.</td>
    </tr>
    <tr>
      <td>(βkST1)−1</td>
      <td>kST1 is the ratio of the reaction parameter associated with reaction rST1 with the backward rate of reaction rS. β is the proportionality constant between [TC] and Δt.</td>
    </tr>
    <tr>
      <td>tr</td>
      <td>Time at which [TC] levels finish being reset at the beginning of the day (see Figure 2B).</td>
    </tr>
    <tr>
      <td>t0</td>
      <td>Phase shifting parameter of the [TC] dynamics given by Equation 1. The next dawn is expected to come (24 + t0) hr after the previous one.</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Full list of the system parameters for Model 2


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ρ0</td>
      <td>Starch content at the beginning of the dark period.</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>Normalization variable.</td>
    </tr>
    <tr>
      <td>tr1</td>
      <td>Time at which [TC] levels finish being reset at the beginning of the day (see Figure 2C).</td>
    </tr>
    <tr>
      <td>tr2</td>
      <td>Time at which [TC] levels start being reset at the end of the day (see Figure 2C).</td>
    </tr>
    <tr>
      <td>t0</td>
      <td>Phase shifting parameter of the [TC] dynamics given by Equation 2. The next dawn is expected to come (24 + t0) hr after the previous one.</td>
    </tr>
  </tbody>
</table>

### Data fitting

The best fit to a given dataset was found by minimizing the function:

$$
L(\theta→)=\sumi=1N(\frac{ρ_{S}^{theory}(t_{i},\theta→)−ρ_{S}^{exp}(t_{i})}{ρ_{S}^{exp}(t_{i})})^{2},
$$

where $ρ_{S}^{exp}(t_{i})$ are the N mean values of starch contents measured at times ti. $ρ_{S}^{theory}(t_{i},\theta→)$ is the starch value predicted by the model at time ti with parameter values $\theta→$. The set of parameters $\theta→$ that minimizes L corresponds to the maximum-likelihood estimates of the parameters under the assumption that the experimental measurements are normally distributed around the theoretical values with a constant relative error.

Note that, in the fits of the data from the cca1/lhy mutant plants for the early and the normal night, we did not consider the two data points closest in time to 24 hr from the datasets, as they are characterized by very low values of starch content and, therefore, are likely to be affected by higher relative errors compared to the other data points. For the same reason, for the linear fits shown in Figure 4—figure supplement 1A we did not consider the data point at t = 24 hr in the normal night datasets and the data points at t = 22 hr and t = 24 hr in the early night datasets.

A simulated annealing algorithm was used for the minimization of L(θ→). The parameter values of the best fits of the models are given in Tables 3–6, along with the ranges in which the parameters were allowed to vary.

**Table 3.**
 The values of the parameters of the Model 1 best fits shown in Figure 2


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="7">Model 1</th>
    </tr>
    <tr>
      <th>WT early night (panel F)</th>
      <th>WT normal night (panel F)</th>
      <th>WT late night(panel F)</th>
      <th>cca1/lhy early night (panel H)</th>
      <th>cca1/lhy normal night (panel H)</th>
      <th>WT low light level (panel J)</th>
      <th>WT normal light level (panel J)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ρ0 (mg g−1 FW) within 10% of the measured value</td>
      <td>8.5</td>
      <td>11.0</td>
      <td>11.7</td>
      <td>4.2</td>
      <td>5.1</td>
      <td>3.6</td>
      <td>6.1</td>
    </tr>
    <tr>
      <td>γ (0.7–3.0)</td>
      <td>1.8</td>
      <td>1.8</td>
      <td>1.9</td>
      <td>1.2</td>
      <td>1.2</td>
      <td>1.5</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>(βkST1)−1 (1.5–5.0) hr</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>1.6</td>
      <td>1.7</td>
      <td>2.1</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>tr (9.0–12.0) hr</td>
      <td>9.0</td>
      <td>Any value in the specified range</td>
      <td>Any value in the specified range</td>
      <td>11.7</td>
      <td>11.7</td>
      <td>Any value in the specified range</td>
      <td>Any value in the specified range</td>
    </tr>
    <tr>
      <td>t0 (−5.0–5.0) hr for the cca1/lhy data, t0 = 0 for WT</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>−4.2</td>
      <td>−2.5</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

_With each parameter the range used in the best fit search is indicated.WT: wild-type plants._

**Table 4.**
 The values of the parameters of the Model 2 best fits shown in Figure 2


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="7">Model 2</th>
    </tr>
    <tr>
      <th>WT early night (panel G)</th>
      <th>WT normal night (panel G)</th>
      <th>WT late night (panel G)</th>
      <th>cca1/lhy early night (panel I)</th>
      <th>cca1/lhy normal night (panel I)</th>
      <th>WT low light level (panel K)</th>
      <th>WT normal light level (panel K)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ρ0 (mg g−1 FW) within 10% of the measured value</td>
      <td>8.3</td>
      <td>11.0</td>
      <td>12.1</td>
      <td>4.2</td>
      <td>5.1</td>
      <td>3.5</td>
      <td>5.8</td>
    </tr>
    <tr>
      <td>γ (0.7–3.0)</td>
      <td>1.1</td>
      <td>1.0</td>
      <td>1.1</td>
      <td>1.3</td>
      <td>1.2</td>
      <td>1.2</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>tr1 (9.0–12.0) hr</td>
      <td>11.0</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>11.0</td>
      <td>11.4</td>
      <td>10.5</td>
      <td>10.2</td>
    </tr>
    <tr>
      <td>tr2 (20.0–23.0) hr</td>
      <td>20.1</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>21.8</td>
      <td>21.4</td>
      <td>21.4</td>
      <td>22.5</td>
    </tr>
    <tr>
      <td>t0 (−5.0–5.0) hr for the cca1/lhy data, t0 = 0 for WT</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>−2.4</td>
      <td>−1.3</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

_With each parameter the range used in the best fit search is indicated.WT: wild-type plants._

**Table 5.**
 The values of the parameters of the Model 1 best fits shown in Figure 3


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="4">Model 1</th>
    </tr>
    <tr>
      <th>Panel A</th>
      <th>Panel B</th>
      <th>Panel C</th>
      <th>Panel D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ρ0 (mg g−1 FW) within 10% of the measured value</td>
      <td>5.4</td>
      <td>9.0</td>
      <td>7.7</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td>γ (0.7–3.0)</td>
      <td>2.4</td>
      <td>1.4</td>
      <td>1.1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>(βkST1)−1 (1.5–5.0) hr</td>
      <td>5.0</td>
      <td>2.6</td>
      <td>2.1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>tr (9.0–12.0) hr</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>10.3</td>
      <td>12.0</td>
    </tr>
    <tr>
      <td>t0 (−5.0—5.0) hr</td>
      <td>4.3</td>
      <td>3.3</td>
      <td>2.4</td>
      <td>−0.5</td>
    </tr>
  </tbody>
</table>

_With each parameter the range used in the best fit search is indicated._

**Table 6.**
 The values of the parameters of the Model 2 best fits shown in Figure 3—figure supplement 2


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="4">Model 2</th>
    </tr>
    <tr>
      <th>Panel A</th>
      <th>Panel B</th>
      <th>Panel C</th>
      <th>Panel D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ρ0 (mg g−1 FW) within 10% of the measured value</td>
      <td>5.5</td>
      <td>9.1</td>
      <td>7.7</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td>γ (0.7–3.0)</td>
      <td>1.5</td>
      <td>1.3</td>
      <td>0.7</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>tr1 (9.0–12.0) hr</td>
      <td>12.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <td>tr2 (20.0–23.0) hr</td>
      <td>20.0</td>
      <td>20.9</td>
      <td>22.1</td>
      <td>22.1</td>
    </tr>
    <tr>
      <td>t0 (−5.0–5.0) hr</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>2.4</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

_With each parameter the range used in the best fit search is indicated._

### Recalculation of the starch degradation rate after the night-time light period

By combining our results from the night-time light period experiments shown in Figure 3A–C, we can show that the evidence in favor of a re-calculation of the starch degradation rate after the night-time light period is statistically significant. In the experiments shown in Figure 3A–C, plants were subjected to 5 hr of light in the middle of the night (between 14 hr and 19 hr after the previous dawn). The starch content at each time point was measured by averaging the starch content of n = 10–12 individual rosettes and the standard error of the mean was also calculated.

The starch degradation rate before the night-time light period in the i-th experiment was measured as:

$$
\mu_{B}^{i}=\frac{ρ_{S}^{i}(12 hr)−ρ_{S}^{i}(14 hr)}{14 hr−12 hr},
$$

that is, as the difference between the starch content at 12 hr and 14 hr divided by the time interval.

Similarly, the starch degradation rate after the night-time light period for the i-th experiment was:

$$
\mu_{A}^{i}=\frac{ρ_{S}^{i}(19 hr)−ρ_{S}^{i}(21 hr)}{21 hr−19 hr} ,
$$

These rates were averaged over the three experiments, and the difference between the two averages was calculated:

$$
\mu_{A}−\mu_{B}=\frac{1}{N}\sumi=1N(\mu_{A}^{i}−\mu_{B}^{i}),
$$

where N = 3 was the number of experiments. The error on this quantity was estimated by propagating standard errors of the mean. We found μA − μB = 0.43 ± 0.14 (mg g−1 FW)/hr which is significantly greater than 0 (one-tailed Welch’s t-test, p = 1.6 × 10−3).

We also calculated the average difference between $\mu_{A}^{i}$ and

$$
\mu_{normal}^{i}=\frac{ρ_{S}^{i}(12 hr)}{12 hr},
$$

where $\mu_{normal}^{i}$ is the rate that would have been expected over a normal 12-hr night. We found that this average is

$$
\mu_{A}−\mu_{normal}=\frac{1}{N}\sumi=1N(\mu_{A}^{i}−\mu_{normal}^{i})=0.48\pm0.11(mgg^{−1} FW)/hr,
$$

where the error was again estimated by propagating the standard errors of the mean.

This value is again significantly greater than 0 (one-tailed Welch’s t-test, p = 3.8 × 10−5).

These results provide strong evidence against the hypothesis that a fixed degradation rate is set only once at the first onset of darkness, and is instead compatible with our prediction that the rate is continuously re-computed throughout the night.

### Mutant phenotypes

In the following, we show how the models can explain the mutant phenotypes discussed in the main text (see Figures 1B and 4 and Figure 4—figure supplement 1).

### cca1/lhy

LHY and CCA1 are central components of the clock. The cca1/lhy mutant has a free-running period of significantly <24 hr under continuous light.

This mutant is characterized by too high a rate of starch degradation (see Figure 1B). Indeed, the starch reserve is exhausted around 21–22 hr after the previous dawn, instead of 24 hr as in the wild type. Interestingly, if these mutant plants are given an early night, the starch degradation rate is adjusted such that all the starch is again degraded around 21–22 hr after previous dawn (see Figure 1B).

The models we discussed previously can straightforwardly explain such a phenotype by assuming that in this mutant, the time of expected dawn is shifted to a time t < 24 hr after the previous dawn. There are different perturbations of the T dynamics that can produce this effect in our models, and still reproduce the data from cca1/lhy equally well. For instance, for cca1/lhy in Model 1, [TC] after being reset, could decrease more steeply than in the wild-type, and drop to zero at a time t < 24 hr after the previous dawn. Then [TC] could remain at low levels, before rising again around 24 hr. Another perturbation appropriate for both Models 1 and 2, would be to phase shift the T dynamics given by Equations 1 and 2, respectively by a time t0 < 0 hr, in such a way that the time of expected dawn becomes (24 + t0) hr < 24 hr, as discussed above in the ‘Parameters’ section. For the sake of simplicity, we fitted the cca1/lhy data by assuming that the latter perturbation takes place, and accordingly we used t0 as a fitting parameter.

### lsf1, sex4, bam3, bam4, isa3

lsf1 and sex4 mutant plants were kept in the dark for 132 hr after the end of the previous light period, then exposed to normal 12-hr light/12-hr dark cycles and the starch content measured. As Figure 4A shows, during the days following the prolonged dark period the mutant plants failed to degrade their entire starch reserve at night. Instead, the total starch content degraded by the end of each night, expressed as a percentage of the starch content at the end of the respective preceding light period, was approximately constant and much lower than that of wild-type plants (Figure 4B).

Interestingly, the same mutants could also adjust their starch degradation rate in response to an unexpected early night. In order to quantitatively verify this observation, we performed linear fits of the data from the unexpected early and normal nights:

$$
ρ_{S}^{early}(t)=−\mu^{early}⋅(t−t^{early})+ρ_{S,0}^{early},ρ_{S}^{normal}(t)=−\mu^{normal}⋅(t−t^{normal})+ρ_{S,0}^{normal},
$$

where ($\mu^{early},ρ_{S,0}^{early}$) and ($\mu^{normal},ρ_{S,0}^{normal}$) are the fitting parameters, with tearly = 8 hr, tnormal = 12 hr the times of onset of darkness respectively for the unexpected early and normal night. From these fits, we calculated the ratio R between the starch degradation rates in the normal and the unexpected early night, normalized by the respective starch content at the time of onset of darkness:

$$
R=\frac{\mu^{normal}/ρ_{S,0}^{normal}}{\mu^{early}/ρ_{S,0}^{early}}.
$$

If the degradation rate is adjusted as happens in wild-type plants, during the unexpected early night relative to a normal night, the same fraction f of the initial starch content should be degraded by the time of expected dawn. Therefore, $\mu^{normal}≈f\frac{ρ_{S,0}^{normal}}{t_{day}−t^{normal}}$ and $\mu^{early}≈f\frac{ρ_{S,0}^{early}}{t_{day}−t^{early}}$; hence, $R≈\frac{t_{day}−t^{early}}{t_{day}−t^{normal}}=\frac{16}{12}≈1.33$. As Figure 4F shows, the values of R found for lsf1 and sex4 are compatible with 1.33 (dashed line), therefore supporting the hypothesis that these mutants are able to appropriately adjust their starch degradation rate in response to an unexpected early night. We also found the same type of rate adjustment in bam3, bam4 and isa3 mutants (see Figure 4F and Figure 4—figure supplement 1), which also failed to exhaust their starch reserves by the end of the night.

The models make a precise prediction about how such a phenotype can be produced. We will focus on Model 1, but analogous arguments also hold true for Model 2. We showed that for Model 1, in order to obtain a linearly decreasing starch content with time, and with the appropriate degradation rate to ensure complete starch depletion at the time of expected dawn, two normalization conditions must hold:

$$
\frac{f_{D1}A_{d}k_{S}}{k_{ST1}V_{0}\beta}=\gamma=1,\frac{m_{S}f_{D2}}{\alpha f_{D1}}=χ=1.
$$

The first condition ensures that the number of S molecules, and therefore the starch content, decreases linearly with time during the night. The second condition is needed to keep the number of S molecules and the amount of starch strictly proportional, so that both these quantities are fully degraded by the end of the night. We now assume that the second of the two conditions is not valid, and, in particular, that χ < 1. In this case, the starch degradation proceeds at a slower rate, breaking the proportionality between the number of S molecules and the amount of starch. By using Equations 4 and 8, and the initial condition at the start of the dark period, $ΔS^{tot}=\alphaN_{S}^{tot}$, we find that a fraction of starch approximately equal to χ only is degraded by the time of expected dawn. Such a phenotype is clearly compatible with the disruptions caused by the above mutations. Indeed by assuming that the second condition above is not valid, our models can be well fit to the full night-time starch profiles in all the above mutants (data not shown).

One way to perturb only the second of the two normalization conditions shown above (and not the first), would be to alter fD2, which is the starch degradation reaction parameter. This reasoning fits well with the known functions of the above genes, all of which play roles, directly or indirectly, in starch degradation.

### pwd

The pwd mutant lacks the glucan water dikinase responsible for the addition of the phosphate groups to the 3-position of glucose moieties in starch. This mutation generated an approximately linear decrease of starch content with time during the night, but with a rate which was too low to ensure the complete utilization of the starch reserve by the time of expected dawn. Yet, as opposed to the previously discussed mutations, this mutant did not have the ability to adjust the starch degradation rate in response to an unexpected early night (see Figure 4E,F). Indeed, for this mutant we found that the ratio between the degradation rates (normalized by the respective end-of-light period starch content) during the normal and the early night was R = 1.10 ± 0.10, which is significantly less than the wild-type value (R = 16/12, one-tailed Z-test, p = 0.01).

This finding indicates that PWD is potentially a key node where information about starch content and expected time to dawn from the circadian clock are integrated to control starch degradation dynamics. This makes PWD an obvious target for future experiments that aim to elucidate the identities of the S and T molecules.

### Other examples of models implementing arithmetic division

The models detailed above use two distinctly different methods of implementing the division operation. In one case, exemplified by Model 1, the S and T molecule concentrations are divided, with the T molecule concentration tracking the time to expected dawn. In Model 2, the S and T concentrations are multiplied, with the T molecule concentration tracking the reciprocal of the time to expected dawn. The precise implementation of these two methods of performing arithmetic division could, however, vary, with slightly different reaction schemes but the same underlying principles. To illustrate this point, we briefly outline other models related to Model 1 above, where the TC molecule again has the behavior given in Equation 1. We first consider:

$$
r_{S}:S_{C}↔Sr_{T}:T_{C}↔Tr_{T_{2}}:T+T↔T_{2}r_{ST}:S+T↔STr_{ST_{2}}:S+T_{2}→ST_{2}r_{S_{C}T_{2}}:ST_{2}→S_{C}+T_{2}r_{D1}:ST→T r_{D2}:ST+Starch→ST.
$$

Here both S and T molecules can directly and reversibly associate to the granule surface (reactions rS and rT). Once bound to the surface, S and T can form a complex ST (reaction rST) that permits S molecule and starch degradation (through reactions rD1 and rD2 respectively). The T molecule can also hinder starch degradation by forming dimers (reaction $r_{T_{2}}$) that are able to associate with S molecules (reaction $r_{ST_{2}}$) and induce them to detach from the granule surface (reaction $r_{S_{C}T_{2}}$). By a similar analysis to that carried out for Model 1 and Model 2, and for similar reasons, it can be shown that this model can also implement arithmetic division between the S and T molecule concentrations.

More complex models can also easily accommodate additional molecules, which, for instance, could recruit S and T molecules to the granule surface and be part of the starch degradation apparatus. For example, in the set of reactions:

$$
r_{M}:M_{C}↔Mr_{S}:S_{C}+M→SMr_{T}:T_{C}+M→TMr_{SM}:SM→S_{C}+M_{C}r_{TM}:TM→T_{C}+M_{C}r_{D1}:SM→M_{C}r_{D2}:SM+Starch→SM,
$$

M molecules which reversibly bind to the granule surface (reaction rM), recruit the S and T molecules from the surrounding compartment (reactions rS and rT), to form the SM and TM complexes, which can then dissociate from the surface through the reactions rSM and rTM. The SM complex can permit S molecule and starch degradation (reactions rD1 and rD2). Since the T molecule hinders starch degradation by binding to M molecules and preventing them from binding to S, it can be shown that this model can also implement arithmetic division between the S and T molecule concentrations.

### Validation of the use of a night-time light period

Exposure of Arabidopsis plants to light during the normal night could potentially lead to the early, light-induced expression of clock genes, and under some circumstances might re-entrain the clock. Such re-entrainment might affect the level of the T molecule. To discover whether our experimental conditions gave rise to such problems, we investigated the behavior of transcript levels of LHY, a central clock gene, by qPCR analysis. For the experiment shown in Figure 3B, LHY transcript levels were slightly elevated during the night-time light period, then peaked about 2 hr later than in plants that were not exposed to the light period (Figure 3—figure supplement 1). This result indicates that the night-time light period has only minor effects on the clock, which is not re-entrained: if this were the case the peak of LHY expression observed with the night-time light period would not be expected to occur at around 24 hr after the previous dawn.

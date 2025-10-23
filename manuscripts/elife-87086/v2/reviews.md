# Peer review - Round 1

Editors:
- Wolf-Dietrich Heyer, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87086.sa0](https://doi.org/10.7554/eLife.87086.sa0)

This manuscript reports valuable tools and data to study DNA repair and its regulation in life cells by generating and validating cell lines with Halo-tag fusions to the chromosomal genes encoding ATM, NBS1, MDC1, RNF168, RNF169, 53BP1, RIF1, SHLD3, REV7, SHLD2, SHLD1, and DNA-PKcs. The data establish the utility of most of the tools but remain incomplete. Conclusions from the kinetic analysis would benefit from more validation by genetic experiments and the single particle tracking analysis offers more potential for analysis.


---

# Peer review - Round 1

Editors:
- Wolf-Dietrich Heyer, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87086.sa1](https://doi.org/10.7554/eLife.87086.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Systematic analysis of the molecular and biophysical properties of key DNA damage response factors" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Wolf-Dietrich Heyer as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Markus Löbrich (Reviewer #2); Judith Miné-Hattab (Reviewer #3).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

The reviewers and Reviewing Editor recognize the potential utility of the reported tools for the scientific community and appreciate that these tools can provide certain novel insights. However, the analysis is incomplete in several areas and the conclusions seem insufficiently supported by the experimental evidence. The potential revisions would be extensive and consume more time than compatible with eLife's editorial policy.

If you decide to address the extensive revisions requested, we would encourage resubmission as a new manuscript, and we would make an effort to recruit the same reviewers to assess the work, which would be treated as a new submission. The major issues are the functionality of the tagged proteins, especially MDC1 and SHLD1/2 for which major conclusions are reached (#3), completeness of the single particle tracking analysis (#5), and orthogonal genetic validation of the major conclusions from the kinetic analysis (#11, 13, 16).

Life cell imaging provides unprecedented insights into cellular processes, and advances in fluorescence and microscopy allow the identification and tracking of single protein particles in four dimensions. The manuscript reports the creation of a set of useful cell lines with Halotag fusions to 12 key proteins acting in the DNA damage response, namely ATM, NBS1, MDC1, RNF168, RNF169, 53BP1, RIF1, REV7, SHLD1/2/3, and DNA-PKcs. The fusions were carefully validated molecularly and functionally, leading to detectable expression of Halotagged proteins in protein gels. All proteins, with the exception of ATM-Halo, showed the expected cellular localization in undamaged cells and led to an increase in focus formation in response to DNA damage (Zeocin) with the exceptions of ATM and DNA PKcs. Clonogenic survival assays demonstrated the functionality of the fusion proteins, with the exception of Halo-ATM, which appeared similar to a loss of function for both a C- and an N-terminal fusion, and Halo-MDC1, Halo-SHLD1/2, and Halo-53BP1, which showed partial loss of function. Using flow cytometric and in-gel approaches, the steady protein level for all Halo fusions was determined with a good correlation between both methods. All experiments were conducted with two independent clones for each fusion (except NBS, SLD2, 53BP1). All cell lines were homozygous for the Halo tag, with the exception of Halo-SHLD2, where one allele was tagged and the other was a frameshift allele.

Kinetic recruitment experiments using the Halo-tagged proteins were conducted using laser microirradiation-induced DNA damage. The data for components of the Shieldin complex showed significantly different recruitment kinetics for SHLD2 and 3, suggesting that this protein complex assembles at the site of DNA damage rather than being pre-assembled. The kinetic resolution for the other proteins allowed the identification of additional differences in protein recruitment at laser-induced DNA damage. The caveat working with non-physiological laser-induced DNA damage could have been considered and potentially be selectively complemented with orthogonal ways to induce DNA damage such as Cas9-mediated DSBs.

Single particle tracking was used to determine the nuclear diffusion of the single proteins in the presence and absence of DNA damage (zeocin). It is unclear if the technology allows the tracking of a single molecule. The results identified significant differences between the Shieldin subunits 1, 2, and 3, corroborating the conclusion that they do not exist as a pre-assembled complex. The data for MDC1 and RIF1 suggest that both are largely chromatin-associated in undamaged cells, and follow-up experiments show that the MDC1 PST domain is responsible for this, whereas the BRCT domain of MDC1 is critical for DNA damage-induced chromatin association, as previously shown. The analysis of the MDC1 domains lacks experiments under DNA damage conditions (zeocin).

Overall, this manuscript is well-written and documented but the analysis remains incomplete in several instances.

Recommendations for the authors:

1) The ATRX mutation in U2OS cells affects DNA repair pathway choice (PMID: 29937341, PMID: 33431668). This caveat should be considered and discussed.

2) I do not understand the comment in lines 210/211: "Importantly, the differences in absolute protein number between independent genome-edited clones could be the consequence of a different number of alleles being modified with the HaloTag." It is stated in lines 115-117 that all lines are homozygously tagged except for one, where the other allele is a frameshift likely resulting in expressing an unstable truncation protein. There should be no variation in tagged alleles, or am I missing something?

3) The survival of cells expressing Halo-tagged version of ATM, MDC1, 53BP1, SHLD1, and SHLD2 is reduced after zeocin treatment compared to wild-type cells. Thus, the functionality of these tagged proteins is questionable. In particular, the analysis focuses on MDC1 although MDC1 is one of the less functional tagged proteins. For example, MDC1 is reported as less mobile than histones H2B: is this really possible? Could it be an effect of the partial loss of MDC1 functionality? If not, how can such slow mobility be explained? The manuscript also reports that the constitutive interaction between MDC1 and chromatin is mediated by the PST repeat domain of MDC1: again, it is necessary to be careful about this conclusion since the functionality is reduced in the Halo-tagged version.

We appreciate that fully functional fusions may be out of reach, but the limitations need to be acknowledged and discussed. Have alternative tag designs been tried?

4) In the section: Functional validation of HaloTagged DDR proteins:

In the absence of zeocin treatment, cells expressing Halo-MDC1 exhibit many spontaneous foci. Is it something known and if not, how can that be explained?

Cells expressing ATM-Halo do not form foci after zeocin treatment: please comment.

Concerning DNA-PK: this protein is highly abundant in the cell; however, it does not form foci after zeocin treatment. Is there an explanation? does it mean that even if the protein is very abundant, very few DNA-PK molecules are present within foci and sufficient for the next steps of NHEJ? Does it form a visible line after micro-irradiation?

5) Page 12, line 206: It is stated that MDC1 has a higher protein abundance than ATM, SHLD1, SHLD2, and SHLD3 but one of the two MDC1 clones analyzed has the lowest protein abundance of all clones analyzed in this study (2400 molecules per cell according to the text and table I). Why are the two MDC1 clones differ so drastically from each other? Confusingly, the big difference between the two clones is not seen in the bar chart in Figure 3B and is not measured by flow cytometry.

6) Page 12, line 231: It is stated that the adjustment factors for DNA-PKcs are 0.62 and 0.79 but the application of these factors increases the molecule number for clone 1 but decreases it for clone 2 (the latter seems wrong).

7) Single Particle Tracking analysis:

Using analysis of single particle tracking, the authors can measure the diffusive properties of repair proteins. Diffusion is estimated in the presence and in absence of zeocin treatment. Thus, the cells contain many foci: all the traces in the nucleus are analyzed at once, inside and outside foci. The authors then used a 2 population model to fit the distribution of protein displacements.

The SPT analysis allows the authors to give some interesting mechanistic insight but the authors could extract much more information from their data. Why are the values of Dslow not provided? The authors interpret the slow population as bound to damaged DNA. However, it is known that some proteins diffuse relatively fast inside repair foci, especially if they are able to form liquid-liquid phase separation. In addition, some proteins might diffuse slowly outside of foci, because of non-specific interactions (or even for MDC1 for example). Thus, it is possible that the slow molecules are a mixture of the molecules inside the foci with molecules exhibiting chromatin binding outside of the repair foci.

There is no visualization of the traces allowing us to see if the slow molecules are indeed inside foci and the fast ones are outside. It would be essential to be able to see this for at least 1 cell for each repair protein.

Are mixed traces observed, with a slow and a fast part?

Is it possible to estimate the residence time of each protein inside repair foci or on their substrate?

Are the proteins inside foci exchanging with the rest of the nucleus or are they stuck inside the focus during the entire trace?

Since you use bright JF, it should be possible to have long traces: the authors should show a distribution of the traces' length for each repair protein.

Do you see a change in protein diffusion in the absence of zeocin treatment and in the presence of zeocin treatment outside of foci?

The authors also use H2B and NLS as controls. The values obtained should be compared with values found in the literature.

Finally, it is not clear how the histones H2B are tagged in this study: is it also an endogenous H2B-Halo tag? Is it a stable cell line but not endogenous, or is it a transient transfection?

8) Laser micro-irradiation induces massive damage and may not be reflective of physiological encountered DNA damage. Have the authored considered using Cas9-induced DSBs as a defined and targeted DNA damage? I understand that adding such experiments for all proteins would be a massive endeavor, but maybe this could be done for MDC1 and/or the Shieldin complex. Regardless, the limitations of the laser micro-irradiation approach should be discussed.

9) Figure 6 lacks data for the analysis in the presence of zeocin, in the way it was done in the analysis for Figure 5. Such data will corroborate the foci analysis and potentially reveal differences in the recruitment of MDC1 to damaged sites.

10) What is the evidence that a single molecule can be tracked in Figures 5 and 6, as opposed to a single particle that may be composed of multiple proteins?

11) Page 13, line 256: It was surprisingly observed that REV7 and SHLD3 have vastly different recruitment times to laser-induced damage although both factors are known to interact. At the end of the Discussion section, it is speculated that this might reflect REV7's role in TLS but the reader would benefit if such an interpretation was offered earlier in the paper. Moreover, if this interpretation was correct, one would expect that REV7 was recruited to laser damage independently of SHLD3. This should be tested by siRNA-mediated depletion of SHLD3 (or other factors upstream of SHLD3).

12) Page 14, lines 260-263: It is observed that SHLD1 is not recruited to laser damage although it forms foci after zeocin treatment. The authors then speculate that this might suggest that SHLD1 recruitment is the key regulatory step for a fill-in reaction. This is not clear. Are the authors suggesting that fill-in takes place at zeocin-induced breaks but not at laser-induced breaks? Please clarify.

13) Page 14, line 266: The authors state that the measured recruitment kinetics provide insight into the interdependencies of the shieldin complex components. As evidenced by the very early recruitment kinetics of REV7 (possibly due to its role in TLS), this may not be true since the factors could have roles in other processes. Thus, the evaluation of interdependencies requires the measurement of the recruitment kinetics in situations when individual components of the shieldin complex are depleted by siRNA technology. Thus, the authors should assess the recruitment kinetics in cells depleted for SHLD2/3, REV7, or 53BP1/RIF1.

14) Page 17, line 319: SHLD1 is not recruited to chromatin after DSB induction despite its low abundance, and the authors state that this is consistent with its lack of recruitment to laser damage. However, it is clearly shown to form foci at DSB. Moreover, how does this finding fit the author's suggestion from above that SHLD1 is the key regulator of the fill-in reaction?

15) The authors try to address the unexpected findings for SHLD1 (no recruitment to laser damage and no increase in the chromatin-bound fraction after zeocin treatment) in the discussion on page 22, last paragraph, and suggest that SHLD1 may either not bind every DSB where SHLD2 is present or may reside at a DSB in lower copy numbers than SHLD2. Both explanations appear inconsistent with the robust formation of SHLD1 foci at zeocin-induced DSB, the first suggestion can easily be tested with co-localization experiments using HaloTag SHLD1 and SHLD2 ab or vice versa.

16) Page 21, line 390: The authors suggest the model that RNF169 delays 53BP1 recruitment to DSBs. Although this interpretation is consistent with the presented data, the model should be tested by 53BP1 recruitment measurements after siRNA-mediated depletion of RNF169.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Systematic analysis of the molecular and biophysical properties of key DNA damage response factors" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Life cell imaging provides unprecedented insights into cellular processes, and advances in fluorescence and microscopy allow the identification and tracking of single protein particles in four dimensions. The manuscript reports the creation of a set of useful cell lines with Halotag fusions to 12 key genes acting in the DNA damage response, namely ATM, NBS1, MDC1, RNF168, RNF169, 53BP1, RIF1, REV7, SHLD1/2/3, and DNA-PKcs. The fusions were carefully validated molecularly and functionally, leading to detectable expression of Halotagged proteins in protein gels. All proteins, with the exception of ATM-Halo, showed the expected cellular localization in undamaged cells and led to an increase in focus formation in response to DNA damage (Zeocin) with the exceptions of ATM and DNA PKcs. Clonogenic survival assays demonstrated the functionality of the fusion proteins, with the exception of Halo-ATM, which appeared similar to a loss of function for both a C- and an N-terminal fusion, and Halo-MDC1, Halo-SHLD1/2, and Halo-53BP1, which showed partial loss of function. Using flowcytometric and in gel approaches, the steady protein level for all Halo fusions was determined with good correlation between both methods. All experiments were conducted with two independent clones for each fusion (except NBS, SLD2, 53BP1). All cell lines were homozygous for the Halo tag, with the exception of Halo-SHLD2, where one allele was tagged and the other was a frameshift allele.

Kinetic recruitment experiments using the Halo-tagged proteins were conducting using laser microirradiation induced DNA damage. The data for components of the Shieldin complex showed significantly different recruitment kinetics for SHLD2 and 3, suggesting that this protein complex assembles at the site of DNA damage rather than being pre-assembled. The kinetic resolution for the other proteins allowed identification of additional differences in protein recruitment at laser-induced DNA damage. The caveat working with non-physiological laser-induced DNA damage could have been considered and potentially be selectively complemented with orthogonal ways to induce DNA damage such as Cas9-mediated DSBs.

Single particle tracking was used to determine the nuclear diffusion of the single proteins in the presence and absence of DNA damage (zeocine). It is unclear if the technology allows tracking of a single molecule. The results identified significant differences between the Shieldin subunits 1, 2, and 3, corroborating the conclusion that they do not exist as a preassembled complex. The data for MDC1 and RIF1 suggest that both are largely chromatin-associated in undamaged cells, and follow-up experiments show that the MDC1 PST domain is responsible for this, whereas the BRCT domain of MDC1 is critical for DNA damage-induced chromatin association, as previously shown. The analysis of the MDC1 domains lacks experiments under DNA damage conditions (zeocine).

The two main conclusions from the work are that (1) the individual subunits of the Shieldin complex are recruited independently to sites of DNA damage, and (2) MDC1 and RIF1 are bound constitutively to chromatin. Although these conclusions are supported by the data, some inconsistencies with the literature remain unresolved. For example, the authors report that SHLD2 is recruited to laser tracks before SHLD3, while previous work demonstrated a genetic requirement for SHLD3 to recruit SHLD2 to sites of DNA damage. Further, it remains an open question how and when MDC1 and RIF1 are recruited to sites of DNA damage if they are constitutively bound to chromatin.

The use of Halo ligands with different emission spectra to simultaneously monitor single-particles and DNA repair foci is very elegant and can potentially be used to distinguish the behavior of different subpopulations of a DNA repair factor.

The manuscript is well-written, but some literature reference and information in the methods section are missing.

In conclusion, this is an interesting study that applies novel microscopy techniques to DNA double-strand break repair proteins. However, the study remains somewhat descriptive, which limits the mechanistic insight gained from the study and the analysis remains incomplete in several instances for lack of genetic corroboration of the main conclusion about the Shieldin complex recruitment.

Recommendations for the authors

Essential revisions

1) Line 144: The authors conclude that "the HaloTag does not impact the proper cellular localization of these proteins" based on fluorescence microscopy of the Halo-tagged proteins after JF646 labeling. This conclusion cannot be made, because it would require examination of the localization of the untagged proteins under the same conditions. Please qualify your statement.

2) Line 146: The authors conclude that "HaloTagging ATM at the N-terminus led to nuclear exclusion". The authors cannot make this conclusion without imaging the untagged ATM under the same condition. Please qualify your statement.

3) Line 183: It cannot be concluded that "most possess full DNA repair functionality" unless the cell lines expressing Halo-tagged proteins are compared to their gene knockout counterparts. This was only performed for 53BP1 and MDC1, where partial functionality was observed. Please qualify your statement.

4) Page 13, line 256: It was surprisingly observed that REV7 and SHLD3 have vastly different recruitment times to laser-induced damage although both factors are known to interact. At the end of the Discussion section, it is speculated that this might reflect REV7's role in TLS but the reader would benefit if such an interpretation was offered earlier in the paper. Moreover, if this interpretation was correct, one would expect that REV7 was recruited to laser damage independently of SHLD3. This should have been tested by siRNA-mediated depletion of SHLD3 (or other factors upstream of SHLD3) and this limitation should be explicitly acknowledged in the text.

5) Page 14, line 266: The authors state that the measured recruitment kinetics provide insight into the interdependencies of the shieldin complex components. As evidenced by the very early recruitment kinetics of REV7 (possibly due to its role in TLS), this may not be true since the factors could have roles in other processes. Thus, the evaluation of interdependencies requires the measurement of the recruitment kinetics in situation when individual components of the shieldin complex are depleted by siRNA technology. Thus, the authors should assess the recruitment kinetics in cells depleted for SHLD2/3, REV7 or 53BP1/RIF1. The caveat of roles in independent processes should be explicitly mentioned.

6) Line 293: It is counter-intuitive that SHLD2 foci depends on SHLD3, which is recruited to foci significantly later than SHLD2. The two-step model suggested in the Discussion to explain this observation is not supported well by the data, because one would expect the initial (pre-SHLD2) step of SHLD3 to also be detected in the LMI experiments. Further, SHLD2 actually dissociates when SHLD3 associates with laser stripes, which is not discussed by the authors. It would strengthen the manuscript if the model could be tested experimentally by the authors.

7) A similar study was conducted previously (Aleksandrov et al. 2018), which reported recruitment half-times to laser stripes significantly different than the current study for some proteins and in other cases similar half-times. For example, the recruitment times for MDC1, RNF168, RNF169, and 53BP1 was reported by Aleksandrov to be 35s, 78s, 203s, and 307s, where the current study report 77s, 69s, 186s, 669s. It would be in place to reference the previous study and compare findings.

8) It is surprising that Halo-H2B only displays 66% chromatin binding. The assumption is that JF646 binds irreversibly to the Halo-tag, but is it possible that some free JF646 is present and gives rise to the "free" pool of fluorophores? This could easily be tested by formaldehyde fixation which should give 100% chromatin binding if no free JF646 is present.

9) Line 331: A two-state diffusion model is assumed where particles either freely diffuse or are chromatin bound. How would the conclusions be affected if a third state was allowed where a protein is part of a slow diffusing macromolecular complex.

10) Figure 5: The scatter plots should be displayed as "super plots" where data points for each of the 3-4 independent experiments are presented in different colors/symbols (Lord et al. 2020). This would reveal any systematic differences between experiments. For example, it looks like RNF169 data points can be divided into two populations.

11) Page 21, line 390: The authors suggest the model that RNF169 delays 53BP1 recruitment to DSBs. Although this interpretation is consistent with the presented data, the model could be tested by 53BP1 recruitment measurements after siRNA-mediated depletion of RNF169. This limitation should be explicitly acknowledged in the text.

12) The sources of several plasmids are missing e.g. pX330 in line 665.

13) A table with oligonucleotides and gRNAs used in the study should be included.

14) Line 511: Which data allow the authors to conclude that the PST domain of MDC1 "facilitates DDR signal amplification"?

15) The authors conclude that MDC1 and RIF1 are constitutively associated with chromatin. If this is the case then one might expect the localization of MDC1 and RIF1 to follow that of condensed chromosome when cells progress from interphase into mitosis. Indeed, there is evidence for this for RIF1 (Watts et al. 2020), but for MDC1 I could not find such evidence in the literature. However, I suspect that the authors in their data have images of mitotic cells that could answer this question.

16) To quantify the mobility inside foci versus outside foci, and the flux of proteins in and out of foci, would it be possible to make a density map of all the repair proteins in the nucleus? Using this density map, the foci appear clearly, and it is then possible to separate trajectories within foci from those outside foci.

17) Figure S5B: After zeocin treatment: is it possible that the lines between foci are misslinking?

References

Aleksandrov R, Dotchev A, Poser I, Krastev D, Georgiev G, Panova G, Babukov Y, Danovski G, Dyankova T, Hubatsch L et al. 2018. Protein Dynamics in Complex DNA Lesions. Mol Cell 69: 1046-1061 e1045.

Lord SJ, Velle KB, Mullins RD, Fritz-Laylin LK. 2020. SuperPlots: Communicating reproducibility and variability in cell biology. J Cell Biol 219.

Watts LP, Natsume T, Saito Y, Garzon J, Dong Q, Boteva L, Gilbert N, Kanemaki MT, Hiraga SI, Donaldson AD. 2020. The RIF1-long splice variant promotes G1 phase 53BP1 nuclear bodies to protect against replication stress. eLife 9.

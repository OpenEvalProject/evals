# Author response - Round 1

Authors:
- Marina Besprozvannaya ([ORCID: 0000-0001-5856-4130](https://orcid.org/0000-0001-5856-4130))
- Eamonn Dickson
- Hao Li ([ORCID: 0000-0001-5677-3377](https://orcid.org/0000-0001-5677-3377))
- Kenneth S Ginburg
- Donald M Bers
- Johan Auwerx
- Jodi Nunnari ([ORCID: 0000-0002-2249-8730](https://orcid.org/0000-0002-2249-8730))

## Response text

DOI: [10.7554/eLife.31019.034](https://doi.org/10.7554/eLife.31019.034)

Specific Revisions:

1) GRAMD2a KO cells need more characterization.

a) In Figure 7, the single clone could have reduced amount of STIM1 and rescue by GRAMD2a overexpression could result from expansion of MCSs, so please show images to demonstrate normal looking MCSs and document protein levels.

We examined endogenous STIM1 levels using Western analysis with an anti-STIM1 monoclonal antibody in control U2OS and GRAMD2a KO cells. This analysis showed that STIM1 levels are comparable in GRAMD2a KO cells and control wild type cells (Figure 7—figure supplement 1C). In addition, the STIM1 translocation experiments, shown in Figure 7A and 7B, were performed with transfected overexpressed mCherry-STIM1.

We used TIRF microscopy to quantify the total amount of ER-PM contact in U2OS wildtype and GRAMD2a KO cells. Using this analysis, the total area of cortical ER is comparable between control and GRAMD2a KO cells and these data are presented in Figure 7—figure supplement 1E.

b) Please measure SOCE responses in the KO cells compared to WT

We measured SOCE-specific calcium influx across the PM using a GECO- Orai1 and observed that there was a small, reproducible and significant reduction in Orai1-specific Ca2+ influx in GRAMD2a KO cells as compared to wildtype cells (Figure 7C). These findings are consistent with the defective STIM1 translocation observed in GRAMD2a KO cells and with our conclusion that GRAMD2a is a SOCE-specific ER-PM tether.

We also measured total calcium influx over the PM as well as total cytosolic calcium following TG treatment (Figure 7—figure supplement 1D). We observed that in contrast to Orai1, there was a significant TG-dependent increase in both total calcium influx over the PM and total cytosolic calcium in GRAMD2a KO cells as compared to control cells. This finding suggests that loss of GRAMD2a affects calcium homeostasis more generally, potentially via altered PIP lipid homeostasis and/or by alterations in the activity of other calcium regulatory networks that impinge on other Ca2+ channels, such as TRP. These observations are interesting and indicate a broader role for GRAMD2a; however, a detailed analysis of the mechanisms underlying these phenotypes is beyond the scope of the manuscript.

2) The claim that GRAMD2a facilitates or is required for STIM1 recruitment to contact sites seems premature. Please quantitate the analysis to show that most or all of the recruited STIM1 overlaps with GRAMD2a (using total pixel overlap) and provide proper statistical analysis throughout.

We have performed the requested quantification and it is now presented in a new Table 1 embedded in the revised manuscript. Proper statistical analysis is provided throughout the manuscript.

3) The localization patterns in Figure 2B and 2C need to be quantitated and additional quantitation is needed throughout (see point 2).

We performed the two-tailed t-test on localization of GRAMD1a/2a with E- Syt2/3 in Figure 2B and 2C. Co-localization quantification (total pixel overlap) of GRAMD2a with E-Syt2/3 shown was statistically different from GRAMD1a with E-Sty2/3.

4) Does GRAMD2a bind to the PM via a GRAM domain-PIP-lipid interaction? To address this they need to show that deleting or mutating the GRAM domain inhibits binding.

Our deletional analysis of GRAMD2a and GRAMD1a indicate that their predicted respective GRAM domains are necessary for targeting to the PM (Figure 1E and 1F), substantiating our conclusion that they are ER-PM tethers that, in the case of GRAMD2a, directly tethers to the PM via PIP lipids.

5) Please show something about how the STIM1 separates itself from GRAMD2a during its accumulation at the PM; i.e., are they really part of the same ER structure? Perhaps coexpressing Sec61 marker would suffice. Also, the criteria for judging that GRAM proteins were localized to MCSs was never explicitly stated. Some EM could help a lot here, though it would likely take more than 2 months. A fluorescent marker (MAPPER, or a luminal ER marker) to mark these sites should be tried.

Line-scan analysis of individual puncta of GRAMD2a indicates that GRAMD2a and STIM1 share a ER-PM contact site subsequent to their spatial resolution at later time points of TG treatment (Figure 5D).

Our most stringent data used to conclude that GRAMD2a and GRAMD1a are localized to ER-PM contacts was TIRF analysis, which is a standard analysis PM-linked events. All other data, including line scans demonstrating the co-localization of these components with both PM and ER are also consistent with this conclusion. In our hands, MAPPER expression perturbs/expands the cortical ER and thus is not suitable. EM analysis would indeed be time and resource consuming. We chose to use our resources to address questions that were completely unknown, such as calcium dynamics in GRAMD2a KO cells.

Points that could probably be handled by discussion in the text:

1) Please offer possible explanation as to why STIM1-deltaK forms puncta in cells not overexpressing Orai, contrary to previous studies. For someone in the field, this result will look very suspicious.

Many labs studying SOCE work with HeLa or Hek293 cell lines. Our analysis was performed using COS7 and U2OS cells. Our data demonstrate that in COS7 cells STIMΔK is capable of translocating to the PM after ER calcium depletion, while, as already reported in the field, STIM1ΔK does not translocate to the PM under similar conditions in HeLa cells. These data are now included as Figure 6—figure supplement 1A. We hypothesize that differences in the endogenous expression of STIM1 and Orai1 protein account for this apparent discrepancy between different cell lines.

2) They should also discuss why GRAMD2a KO does not reduce number of puncta if it acts as a tether.

We have included the following statements in our revised discussion in response:

“Although the kinetics and extent of STIM1 recruitment are altered in the absence of GRAMD2a, the number of STIM1 puncta is not affected in GRAMD2a KO cells. We speculate that this GRAMD2a-independent recruitment of STIM1 is a consequence of functional redundancy of additional independent ER-PM tethers, such as E-Syt1/2/3 and oxysterol- binding proteins (OSBP)/OSBP-related proteins (Saheki and De Camilli, 2017a).”

“The basis for the rapid and selective recruitment of STIM1 to GRAMD2a- marked contacts may lie in the geometry of the ER-PM contact site created by the GRAMD2a tether and/or its influence on PIP lipid dynamics/concentration. Specifically, given its small size and simple domain structure, GRAMD2a is likely to create a tight ER-PM junction, which may facilitate STIM1 recruitment, consistent with the observed preference of STIM1 for the relatively narrow junction created by E-Syt1 over E-Syt2/3 (Fernandez-Busnadiego et al., 2015).”

[Editors' note: further revisions were requested prior to acceptance, as described below.]

The reviewers discussed the reviews with one another and the Reviewing Editor drafted this decision in the hopes that you can prepare a revised submission. We hope you will be able to submit the revised version within two months that highlights the stronger aspects of the current story and addresses the comments here from Reviewer #1. We try hard not to support multiple rounds of reviews, but this expert referee's comments seemed serious enough that additional revision is required. Overall, this reviewer was less convinced now that GRAMD2a specifically marks ER-PM MCSs for SOCE, as the paper concludes. Specifically:

1) The first question was whether expression of the mCh-STIM1 (not endogenous STIM1 – subsection “GRAMD2a facilitates STIM1 recruitment during SOCE”, Figure 7—figure supplement 1C) was lower in the single GRAMD2a KO clone. It is not possible to judge this from Figure 7A because the data are all normalized to initial fluorescence. STIM1 overexpression increases the area of MCSs and this is seen in Figure 7—figure supplement 1B; reduced expression of mCh-STIM1 in the KO clone could potentially explain the decreased STIM1 puncta area.

Measuring endogenous STIM1 made a lot of sense to us and in fact there seems to be a slight elevation in the STIM1 levels in the GRAMD2a KO cells. Nevertheless, we performed Western blots on both endogenous and overexpressed mCherry-STIM1 extracts from wild type and GRAMD2a KO cells under conditions where we observed defective STIM1 translocation in the KO cells and did not observe any significant difference in the expression levels of mCherry-STIM1 (Figure 7—figure supplement 1D and E).

The second question was whether GRAMD1a overexpression could have increased the size of MCSs beyond control size, which might account for the increased recruitment of mCh-STIM1 to the PM. Please address these questions.

We selected cells that had apparently normal ER-PM contacts site density and area. This is documented in Figure 1D low expression (0.1 ug/dish) and Figure 5A high expression (1.0 ug). Under both these conditions we observe that GRAMD2a pre-marks contacts where STIM1 is recruited in cells. Also, Figure 5B documents that under resting conditions with GRAMD2a low expression (low expression was used in all experiments with the exception of Figure 5B) STIM1 is diffusely localized to the ER, indicating that overexpression of GRAMD2a is not sufficient for STIM1 recruitment.

2) The new calcium measurements have serious problems and overall the results are not consistent with the evidence that GRAMD2a knockout greatly inhibits STIM1 accumulation at ER-PM contact sites, and do not support the contention that GRAMD2a KO affects Ca2+ homeostasis more generally. The authors see a slight decrease in SOCE in GRAMD2a KO cells when measured by GECO-Orai1 (Figure 7C) and conclude this is consistent with the inhibition of STIM1 localization. There are a couple of problems here. First, the difference between control and KO is very slight. Given the profound inhibition of STIM1 translocation in 7A, and the fact that SOCE is a highly nonlinear function of STIM1 binding to Orai1, one would expect a nearly complete elimination of SOCE in KO cells. More importantly, overexpressing Orai1 without coexpressing STIM1 actually inhibits SOCE, presumably because an excess of Orai1 "dilutes" the pool of endogenous STIM1 and reduces the STIM1:Orai1 binding stoichiometry below the level needed to open the channel (see Hoover and Lewis, PNAS 108:13299, 2011; Li Z et al. J Biol Chem 282:29448, 2007; Soboloff et al. J Biol Chem 281:20661, 2006). Such a dilution effect would explain why Ca influx is slightly reduced with GECO-Orai1 overexpression, but not when Ca is measured by Lck-GCaMP or fluo-4 (and endogenous Orai and STIM levels are maintained). Thus, the slight inhibition of SOCE with GECO-Orai1 cannot be attributed to the absence of GRAMD2a.

[…]

Based on the evidence at this point, the reviewers felt that the conclusion that GRAMD2a really acts as a "master tether" that specifies a subset of E-syt MCSs for SOCE is overstated (Discussion section paragraph two). In the absence of GRAMD2a there are still many STIM1 puncta (Figure 7B and Figure 7—figure supplement 1B); apparently, GRAMD2a is not required for STIM1 recruitment, although it may help promote it in some way. The new Ca2+ imaging data do not show a strong inhibition of SOCE in the absence of GRAMD2a. Taken together, a role of GRAMD2a in specifying sites for SOCE seems questionable at this stage.

To address concerns that the system we used for measuring Ca2+ is somehow fundamentally flawed, we measured the SOCE response in the HEK293 cell line, in which the conical SOCE has been defined. As shown in Figure 7—figure supplement 1F, we can reproduce the stereotypical SOCE response in this line using our experimental conditions, which indicates that the trivial explanations provided above do not account for the different response observed in U2OS cells. As expressed in our rebuttal letter dated November 12th above, we are also willing to share all of our raw data, which is compiled in Figure 7B and Figure 7—figure supplement 1F. In the raw movies, it is apparent that there are no “bleaching, focus drift, movement, etc” issues. Also, the Ca2+ responses between wild type and GRAMD2a KO cells are significantly different (p values 10-5)-see Figure 7 legend for details, which indicates that our data are “solid”. We have also added a new experiment examining E-Syt1 localization, which represents an independent approach to test the validity of our Ca2+ measurement data. It has been documented that under resting conditions E-Syt1 is localized diffusely in the ER but upon elevated cytosolic Ca2+ (independent of SOCE) it translocates to ER-PM contacts (Idevall-Hagren et al. 2105). Figure 7C and Figure 7—figure supplement 1G shows that under resting conditions, in contrast to wild type cells, E-Syt1 is constitutively localized at ER-PM contacts in GRAMD2a KO cells in a Ca2+ dependent manner, further substantiating our Ca2+ measurements and indicating that loss of GRAMD2a significantly alters the composition of ER-PM contacts.

We removed the GECO-Orai data because of the complication in interpretation resulting from overexpression of Orai. As stated above, we have performed additional experiments to address the specificity of the STIM1 and Ca2+ phenotypes in GRAMD2a knockout cells. We observe an additional defect in E-Syt1 localization, consistent with abberant Ca2+ homeostasis but we did not observe any apparent differences in PM PIP or cholesterol lipids or in E-Syt2/3 localization. Together we feel these data are consistent with a model in which GRAD2a functions as a ER-PM tether that organizes a PM domain devoted to Ca2+ handling.

Subsection “GRAMD2a pre-marks ER-PM contacts specialized for SOCE”, final paragraph. Li et al. did not report TG-induced STIM1deltaK PM translocation in the absence of Orai1 overexpression. They overexpressed Orai1-mOrange.

We have removed the citation and note that in HeLa cells where most of the STIM1deltaK work has been performed, we do not observe TG-induced translocation in the absence of overexpressed Orai, consistent with published work. However, we do observe in COS7 cells (Figure 6A and Figure 6—figure supplement 1A). Thus, like the SOCE response in U2OS cells, our data indicate that different cell types are indeed different.

Subsection “ER Ca2+950 depletion and PI(4,5)P2 depletion experiments” second paragraph: Ca2+ concentrations should be mM, not µM.

Done.

Please specify which GECO-Orai1 construct was used (there are two in the Dynes et al. paper). Also, specify which GCaMP was used for the Lck-GCaMP experiments (there are many).

GECO-Orai data have been removed. We have clarified that we used Lck-GCaMP3G.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

First, the reviewers felt that you have responded in a satisfactory way to points 1 and 2.

Regarding Point 3: The scientific basis for rating the quality as low was Ca2+ below baseline even when Ca2+ is re-added to WT in Figure 7B left, and the lack of a steady Ca2+ baseline at the start of the experiment in Figure 7B right.

In the revision, the authors now conclude that Ca2+ homeostasis is somehow different in U2OS cells compared to other cells like HEK or HeLa. This is not justified based on the sparse data that are presented. U2OS cells show very similar TG responses to HEK and HeLa; see Chen et al., Sci. Reports 6:22142, 2016; Supplementary Figure S1B. So this is not a cell type difference, but more likely has something to do with the way the cells have been treated. In the experience of the expert reviewer with many different cell types, basal Ca2+ can become elevated simply by plating cells on polylysine-coated coverslips, or flowing solutions past them, and one has to be careful not to stimulate Ca2+ signaling through these manipulations. The new fluo-4 data from HEK293 cells look great, but they do not validate the aberrant U2OS responses in Figure 7B. Also, the low P values comparing responses in WT vs. KO cells do not indicate that the "data are solid"; they merely indicate the two response are significantly different, but not why they differ. If one set of measurements is flawed, significant differences can occur, but they do not necessarily result from the KO. So this is still a problem that needs to be fixed to enable a meaningful comparison of WT and KO responses.

We thank the expert reviewer for this full explanation and for pointing out published SOCE data in U2OS cells. Based on these comments and data, we recruited a collaborator to help us conduct the Fura-2 measurements as we do not have the appropriate instrumentation. In the course of the Fura-2 experiments, we determined that Fluo-4 and Llk-GcAMP3G data were indeed flawed as a consequence of technical issues and have been removed. As you will see in revised Figure 7B, using Fura-2, we did not observe a significant change in the SOCE response between WT and GRAMD2a KO cells.

The new E-syt1 experiment is interesting, and does suggest that Ca2+ may be elevated in KO cells in the resting state. A likely explanation for both the TG and E-syt1 results is that the Ca2+ stores in the U2OS cells after plating are relatively empty, which prevents TG from releasing any more Ca2+ from the ER while stimulating tonic influx through SOCE. This also explains why Ca2+ drops inside when Ca2+ is removed outside (Figure 7B). It is unfortunate the authors did not take the suggestion of recording Ca2+ responses using fura-2, which would have indicated any differences in basal Ca2+ and allowed them to compare resting Ca2+ in WT vs KO in a direct way. (An elevated basal Ca2+ is not detectable in Figure 7B because the data are all normalized to the initial fluorescence).

Our Fura-2 data (not normalized to initial fluorescence – only non-dye-loaded cell background subtracted) suggest that basal cytoplasmic Ca2+ is not significantly different between the WT and KO cells. The increased constitutive Ca2+-dependent ESyt1 PM localization in GRAMD2a KO cells suggest that Ca2+ may be altered proximal to the PM. This aberrant localization is likely a compensatory response to altered ER-PM contacts and may normalize Ca2+ homeostasis. At this point, we are hesitant to revisit Llk-GcAMP3G experiments given the general concern that the probe may not be a neutral reporter. Thus, the exact basis of the STIM1 and E-Syt-1 localization defects in GRAMD2a KO cells and their relationship to Ca2+ (and π (4,5)P2) homeostasis will require additional experimentation beyond the scope of the manuscript.

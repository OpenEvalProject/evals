# Peer review - Round 1

Editors:
- James M Berger, Johns Hopkins University School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21763.017](https://doi.org/10.7554/eLife.21763.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Frequent exchange of the DNA polymerase during bacterial chromosome replication" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. The reviewers have opted to remain anonymous.

Overall, the referees are in agreement that the work potentially represents an important advance in understanding the dynamics of the bacterial replisome in vivo. However, the referees also raised several questions regarding the experimental methods used and data interpretation. Before a decision can be made regarding publication, we ask that you submit a revised manuscript that addresses the comments below.

Essential Changes:

1) The model that the holoenzyme dissociates from DnaB as a single unit is based on the observation that tau, epsilon, α and δ have identical timescales of dissociation. There are large uncertainties in the DNA bound times and the data in its current form are not strong enough to make this point. In this regard, the authors should provide good characterizations of the fluorescence properties of Ypet and mMaple. Most fluorescent proteins blink (switching reversibly between a bright and dark state), and mMaple is in particular known for its blinking property (Wang, PNAS, 2014). Fluorescence recovery after photobleaching could be spontaneous instead of due to subunit exchange (which could explain the strange behavior of DnaB FRAP experiment – DnaB needed 2s exposure time to prevent diffusing molecules from detected, and hence the authors assign the ~7sec initial FRAP recovery for DnaB to diffusing molecules. Yet single molecule tracking showed DnaB diffuses much slower than that). The authors should conduct control experiments so that these effects could be subtracted (for example using fixed cells or no-exchanging proteins under all conditions used in the paper).

2) In general, one replication fork has two copies of active Pol III. If the two replication forks stay with each other that will give a maximum of four copies. Even with three copies of Pol III as the corresponding author previously published (Reyes-Lamothe, Science, 2012), there are only maximally six labeled copies for each subunit. As such, should the authors observe a stepwise increase of single molecule fluorescence after photobleaching (as in the previous paper) if there are new subunits coming in? The authors observed gradual fluorescence increase instead, which also raises the possibility that this could be due to spontaneous recovery of fluorescence as mentioned in point 2. Comment on point is needed in the text/Methods as appropriate.

3) Similar concern goes to the rebinding experiments. Can the authors conduct control experiments to show that this is not complicated by the blinking behaviors of mMaple?

4) The track duration fits in Figure 2C do not appear to fit the data very well and often only span a few bins. Related to this point, how did the authors determine the appropriate bin sizes to use in the histograms? In some cases, it seems as though relatively few bins were used to generate the distributions. For example, the distributions in Figure 2—figure supplement 3 are plotted with only 5 or 6 bins although (according to the values in Supplementary file 1B) they seem to represent several hundred molecules.

5) It is unclear how results from multiple experiments were combined. For example, the bound time for ε in Figure 2—figure supplement 3 for the 500 ms exposure seems to be the value given in Supplementary file 1B for the second of the three experiments listed under that condition. Likewise, the bound time for the 2s exposure seems to be from the second of the two experiments under that condition. Are the values given in the text and the main figures calculated from a single experiment?

6) The authors show that the bound lifetimes for components of the holoenzyme are much shorter than the lifetime of DnaB. The authors ascribe this difference to the holoenzyme dissociating frequently from DnaB. How do the authors know that the dynamics of the holoenzyme are not dominated by associations with the large number of clamps behind the replication fork? The same question applies to Figure 3 where the authors assume that DnaB is the platform for rebinding, alternatively epsilon could be associating with clamps near the replisome.

7) It is interesting that Pol III still turns over when there is no DNA synthesis. The authors proposed that frequent encounters with transcription or DNA binding proteins result the turnover. The authors may wish to inhibit transcription to test the hypothesis.

8) In the Discussion, the authors invoke dynamic processivity as a mechanism that could explain the relatively transient binding of the holoenzyme. Such models require that the competitor is at a high local concentration which is often generated by nearby binding. It is hard to imagine that a second holoenzyme is associating with DnaB prior to dissociation of the active holoenzyme. It seems a more likely model is that an obstacle that impedes Pol III triggers a conformational transition resulting in a decrease in affinity and release. Such models have been used to describe the recycling of Pol III upon collision with an Okazaki fragment.

9) For the FRAP experiment, Cephalexin treated cells were used and assumed to have the same replisome dynamics as untreated cells, this is mostly based on the similar ori1/SSB ratio (Figure 1—figure supplement 1). The increase in cell volume with drug treatment could potentially influence replisome dynamics (like that the authors later pointed out protein concentration matters). Although life-time of replisome components are similar when probed with sptPALM as described later in the article, it would be good to independently check if DNA/RNA synthesis is effected by Cephalexin perhaps via synthesis rate measurements, or at least provide control experiments to show how this looks like in WT, untreated cells.

10) A significant concern with the authors' model is that it is unclear why, if the holoenzyme were indeed dissociating so frequently, there wouldn't be a much higher copy number of holoenzyme components behind the fork. Leake and Reyes-Lamothe have previously argued for only three copies of pol III within replication foci. This leads to the question of which polymerase is filling in all of these gaps?

11) A general point regarding the Discussion is that the authors provide no potential alternative interpretations of their data.

Suggested changes:

1) In E. coli, the two replisomes from two forks overlap with each other for a significant portion of time (such as in Figure 1—figure supplement 2 panel C. 30min to 40 min to 50 min). All analyses are done under the assumption that a large fluorescence spot could contain either one or two replisomes (cannot be resolved visually due to short distance separation). Perhaps the authors should state this more explicitly in the text and analyses.

2) In discussing the FRAP results for DnaB, the authors attribute the incomplete fluorescence recovery to slow diffusion of DnaB. This logic isn't clear and should be explained in greater detail.

3) Figure 1D and 4A have three y-axes, and are difficult to comprehend. Separating all the measurements, or using broken bars will be easier for the readers.

4) The data plotted in Figure 2D might be better represented in a table. The bar graph doesn't add anything and could be slightly confusing because the y axes are scaled differently.

5) The authors mentioned using a reaction-diffusion model to analyze FRAP traces. There was no description anywhere in the manuscript about what the model is. It appears that the authors simply used an exponential fitting and extracted the half time. If so please state clearly and do not use the name of reaction-diffusion, which has a specific meaning.

6) There are typos in Figure 2C and Figure 2—figure supplement 3 ("Bleach time" legend).

7) Please provide n values (sample size) for all statistic measurements with error bars.

8) Regarding additional data files and statistical comments – the authors should provide n values for all measurements.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Frequent exchange of the DNA polymerase during bacterial chromosome replication" for further consideration at eLife. Your revised article has been favorably evaluated by Jessica Tyler (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are a few remaining issues that need to be addressed before acceptance, as outlined below:

Primary points:

1) Some concerns about the quality of the lifetime fits for the PALM data still exist. From the presentation of the data in the figures, it's very hard to assess the quality of the fits, and many of the conclusions of this paper (exchange of the entire Pol III holoenzyme, no evidence of distinct leading and lagging-strand polymerase dynamics, etc.) rely heavily on those lifetimes. The response raised in the previous version about the presentation of data in histograms and the number of bins used is not wholly clear. For example, the epsilon lifetime data in Figure 2—figure supplement 3D appear to include 143 molecules for the 500 ms exposure and 415 molecules for the 2s exposure. Yet the histograms appear to contain data in only 5 or 6 bins, which is not consistent with the square root of N binning claimed to be used. Even if the MLE fitting method is insensitive to the choice of bins, the current presentation of the data makes it difficult to see how well the data are fit by the resulting curves. Please resolve this issue.

2) Regardless of the exact timescales of exchange, it has not been shown that the timescales of the holoenzyme components are identical. The Discussion should be amended to discuss different scenarios for replisome dynamics, such as the possibility that individual components of the holoenzyme exchange relatively rapidly with free proteins in solution without the complex falling apart. The manuscript attempts to argue against this option by noting that epsilon dissociation and rebinding is observed more frequently than one would anticipate from the free pool of epsilon. This argument is tenuous, however, as no direct evidence is provided to show that these epsilon molecules are diffusing with the holoenzyme (to test this, for example, one could determine whether those epsilon molecules that dissociate and rebind have an anomalously slow diffusion constant consistent with the much larger holoenzyme). Please amend the discussion of the model to point out that the favored model is at best suggested by the data, and please also present some alternative interpretations.

Secondary comments:

1) Regarding the possibility of two timescales in the lifetime data, it would help the reader assess the quality of these fits by plotting the data on a semi-log axis, so that deviations from linearity are more apparent.

2) Concerning the section "DnaB is a stable platform upon which the PolIII holoenzyme exchanges": Measurement of DnaB's long bound lifetime demonstrates that it is a stable component of the replisome, but not necessarily a platform upon which PolII assembles; this latter claim is likely based on what is known about the replisome, by not experimentally tested here (e.g., a DnaB mutant that fails to interact with tau would need to be used to examine this hypothesis). The section title could be altered slightly to more accurately reflect the experimental results.

3) Figure 2—figure supplement 4G. The color of DnaB and epsilon appears to be switched. In panels E and F, there appeared to be negative bins of the apparent diffusion coefficients? Please fix.

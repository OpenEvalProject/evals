# Peer review - Round 1

Editors:
- Donald Hamelberg, https://ror.org/03qt6ba18 Georgia State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80140.sa0](https://doi.org/10.7554/eLife.80140.sa0)

This paper reports a fundamental set of results describing the activation of nuclear receptors. The evidence to support the relationship between function and ligand-induced shift in the conformational ensembles is based on a compelling combination of experimental and computational approaches. The manuscript has implications for fully understanding how perturbation of the conformational ensembles of proteins, in general, orchestrates function. The findings will be of interest to a broad audience in biochemistry and structural, molecular, and evolutionary biology.


---

# Peer review - Round 1

Editors:
- Donald Hamelberg, https://ror.org/03qt6ba18 Georgia State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80140.sa1](https://doi.org/10.7554/eLife.80140.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Ligand-induced shifts in conformational ensembles that predict transcriptional activation" for consideration by eLife. Your article has been evaluated by 3 peer reviewers, and this evaluation has been overseen by Donald Hamelberg as Reviewing Editor and José Faraldo-Gómez as Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Argyris Politis (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) M75I mutant. The authors' functional studies showing the M75I mutant does not bind ligand are presented after the authors present ligand-bound simulation analyses of M75I and the other mutants vs. WT AncSR2. The significance of the ligand-bound M75I computational simulations is unclear if the ligand does not bind experimentally.

2) Potential for correlation bias. It seems much of the computation-function correlation analyses are performed via visual inspection, which can lead to bias. Computation-activity correlation coefficients, e.g., by plotting the fraction of the simulation in cluster X (or Y or Z) vs. maximum activity of the receptor (without ligand or at 1 µM ligand), would help reduce bias and better support the conclusion that computation methods can predict ligand activity.

3) Computational analysis details and new extended analyses. There are a few points related to how the analyses were performed. It is not entirely clear which simulation figure panels correspond to the analysis of conventional vs. accelerated MD trajectories. The cluster analysis of the simulations in Figure 2 compares two states (e.g., WT vs. M75A; M75 apo vs. EST-bound; etc.). However, a more comprehensive cluster analysis-where WT and the four M75 mutants are all clustered together to discover conserved/unique clusters that are populated in all/some/unique conditions-may better inform computational-function correlations. In the cluster analyses in Figure 2D and E, there are conserved clusters but the fractional population sizes can differ (e.g., M75A in cluster 1 is 1/3 the size as WT); the significance of these differences is not clear. Other features of the plots are not well defined, including the fraction of the total frames represented by the plots that show only several clusters; and the underlying structural similarities and differences among the various clusters when comparing different mutants or liganded states. In Figure 6A and B, it is not clear how frequently interactions are populated in the WT vs. mutant simulations (some information is provided in the manuscript text, but a fractional occupancy plot would help).

4) Constitutive activity. Differences in luciferase transcriptional reporter data are described indicating two mutants (M75L and M75I) display constitutive activity, the structural basis of which is further suggested by MD simulation data. However, an alternative explanation could be the mutants display different expression or protein levels in cells.

5) Limitations. One limitation of the study is the assumption that the ligand-free LBD structural state is similar to the LBD conformation where the PROG-bound AncSR2 LBD was stripped of the ligand (perhaps with some additional simulation to relax the system). However, this may not be representative of the true ligand-free LBD conformational ensemble. Describing the ligand-stripped conformational analyses as inactive may therefore be better described as ligand-free. Related is the assumption that the other ligand-bound states (EST, etc.) are not significantly different from the PROG state or can be accessed after further accelerated MD, which may be more plausible.

6) With a relatively small set of information as presented in this manuscript, would it be better to state that the computational studies predict activity or describe the activity (because in some cases computation does not predict or describe activity; ligand-bound M75I mutant). To predict activity, it could be argued that a larger dataset would be needed perhaps with data training + machine learning.

7) Western blot analysis would inform whether mutant receptor activity differences are caused by differences in protein levels.

8) Manuscript organization. The manuscript story is framed to ask the question if ligand activity be predicted from an experiment with an early emphasis on simulation, then relating the observed/discovered simulation findings to the experiment, then back to simulation. One wonders if the data were presented in a different way and if additional correlation analyses were performed on the existing data if the resulting outcomes would seem less biased and more informed (along with additional analyses and clarification of current analyses described below).

9) The flow of the manuscript may be improved if the manuscript were reorganized to describe the luciferase assay data and ligand displacement data first, then the computational clustering and correlation to experiment-rather presenting the functional studies in between two different computational analyses. A reorganized flow may address a few unanswered questions or speculations made in the current manuscript:

10) If the manuscript was reorganized as described above, one might not choose to include the M75I simulation data or use it to determine if ligand affinity can be predicted from simulation (currently the manuscript only attempts to predict ligand efficacy).

11) On page 5, the authors speculate that H3-H5 distance might impact transcriptional activity but provide no underlying basis for this hypothesis. If this idea has been previously suggested and supported by data, citations should be added. However, presenting the functional data first, then describing these H3-H5 simulation distance findings, would provide an opportunity to state (whether) there is a correlation between this distance and transcriptional output.

12) Another speculative statement where the basis for the comment is not well supported includes: end of the Figure 2 legend, in that the new M75A/M75I ligand-bound conformational states would activate the receptor or not (how can this be inferred from simulation data alone?).

13) Previous work in other nuclear receptors has shown that decreased HDX in the coregulator binding region is associated with receptor activation; however, the authors see the opposite here. M75L has increased HDX compared to WT, apparently imparting constitutive activity. This should be at least pointed out and discussed in the paper.

14) Given the large reduction in Tm for some of the mutants, I am not sure that the Tm reductions are "reflective of local, structural effects". What evidence or rationale do you have that argues/shows that these Tm reductions are not reflective of global changes to the protein?

15) "M75F shows the largest H3-H5 distance (7.5-8.1 Å) while M75L and WT AncSR2 show intermediate distances (7.4-8.1 Å). Thus, we determined that while M75 mutations preserve the contact with hormones, they vastly modulate the H3-H5 interhelical distance which might impact transcriptional activity." The stated numbers don't indicate to me that M75F, M75L, and WT induce different H3-H5 distances.

16) "Strikingly, we note that the largest global changes in M75L coincide with the regions predicted by HDX-MS to be destabilized by the M75L mutation (Figure 5B)." Contrary to this statement, I can't see a significant correlation between Figure 5B (M75L), and Figure 6E (M75L). This calls into question the correlation between the presented HDX-MS and simulation data.

17) How was simulation convergence of the relevant structural states tested? Please include some measure of convergence.

18) Could you display the data differently for Figure 2 panels E and F? It is hard to understand the similarity or difference between apo or wt. Are the wt/apo stacked or overlayed on the mutant/ligand bars? Possible ways to improve clarity are to display the data separately, use unfilled bars, or explicitly show and state that the data are stacked or overlayed.

19) Why do WT, M75F, and M75A produce less luciferase than empty vector (Figure 3F)? The similar supplementary figure suggests that the Y-axis numbers are wrong in Figure 3F.

20) Inclusion of additional data where data not shown is specified, could help consolidate the text. It would have been interesting to include M75A and M75F mutants in the binding assay and HDX to further strengthen the conclusions.

21) Figure S1; the SEC profiles of the WT and the mutants could be included in the same figure (with SDS-PAGE) instead of data not shown. It would help to further strengthen the text.

22) Figure 1D; the decrease in thermal stability of M75I mutant may lead to increased aggregation. Again, it would be interesting to correlate with the SEC profile for a better understanding of the results.

23) Figure 2; the text in the results is difficult to correlate with figures 2C and 2D. Specifically, for M75A and M75I, the H3-H5 distance is specified to be 7-7.2 Å in the text, which is to be referred to in figure 2D, but in figure 2D it is different.

24) Figure 4; the legends C and D are substituted for D and E. Also, legend 'E' is not in bold.

25) No statement is made regarding data availability. The HDX and other data generated during this work are recommended to be made accessible to the public.

26) Amino acid residue callouts use a mixture of three- and one-letter residue callouts, e.g., Met75 and M75; one should be chosen, and if one-letter code is chosen, then helical callouts such as H7 should be renamed h7 or helix7 for clarity.

27) There may be an overuse of words such as "unexpectedly", "unexpected", "vastly", "strikingly", "dramatic", etc.

28) Figure 2B: what atom(s) were used to measure the distance between the ligand and res75-or was a centroid used?

29) In several places, references are needed to support statements such as "our previous work", etc.

30) Maybe instead of using the phrase "conformational shifts" the phrase "a shift of the conformational ensemble" would be more appropriate?

31) Statements such as "none of the hormones activated mutant X" should probably be clarified with an additional phrase like "with ligand treatment up to 1 µM".

32) Page 9, the first line of the paragraph: it may not be unexpected that receptor mutations might inhibit or change activity.

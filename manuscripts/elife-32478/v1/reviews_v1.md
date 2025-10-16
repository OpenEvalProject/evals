# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32478.027](https://doi.org/10.7554/eLife.32478.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Chemical-physical characterization of the hepatitis B virus capsid by all-atom molecular dynamics simulations" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wenhui Li as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: William Gelbart (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision. Major revisions are required in order to make this work potentially acceptable for eLife. A final decision will be made once we receive your revisions.

Summary:

In this work, the authors use unrestrained molecular dynamics simulations to characterize the structural dynamics of the icosahedral HBV capsid. This study extends both time sampling and level of detail for previous work at the coarse-grained level for the same system, and shows insights into the function of the capsid. In addition, they show that capsid dynamics limits achievable resolution in cryoEM data processing for this system.

Overall, in its current form, the paper reads like a long description of the simulation and its analyses, and the reader may miss the exciting bits along the way, especially if they are not experts in molecular dynamics simulations. The paper should be rearranged to present from the get go the most exciting findings. Even the title and Abstract fail to do so currently. The Results sections should have meaningful section titles announcing the main finding to be expected (not just a narration of the analysis and figures). The separation between the Results section and the Discussion renders the former very dry. I suggest that the main findings and their contextualization with other data is included in the Results, with a shorter Discussion section.

Moreover, the authors should relate their results in more detail to previous findings, and to elaborate on the idea of suggesting treatment for disease. A couple of specific testable predictions would be very useful.

Below are more specific major concerns about the work and the presentation of the results.

Essential revisions:

1) What are the biological / biochemical / biophysical implications for the capsid hexamers to be more flexible than pentamers? (Subsection “Capsid flexibility and dynamics”, fourth paragraph).

2) The determination of larger-scale collective modes still appears to be challenging for this system. The authors present a normal mode analysis in Figure 5, but as they state in the Discussion, the results are difficult to interpret. Have the authors considered a principal component analysis of the capsid dynamics? This could bring to light similar motions but with more clarity.

3) The exchange rates for the water molecules (subsection “Solvent exchange across the capsid”) of 4.7x10^6 / ns seem extremely high. Do these rates imply that there are a lot of water molecules moving in/out per nanosecond? Are these waters bouncing back and forth? How does this compare to other viruses (or to bulk water, if one was to define a surface)? The rates for the sodium ions are more reasonable. The authors should also show the channels or paths through which the water molecules flow. Are there channels that lead water molecules in, and others out? Or is the exchange happening both ways in a single channel? It could be interesting to know more of the detailed structure on what is happening with this process. This is something interesting that can only be seen or suggested based on their heroic calculations.

4) Regarding the ion location around the capsid, Figure 7A is not really clear enough to see the positioning of Asp78 and Glu77; could this be improved? Also, I do not understand the deltaG values presented along each panel in Figure 7. What are these values exactly? Is it the density / location of sodium ions at different delta-G cutoffs? More details should be given here.

5) It is questionable if molecular simulation / free energy calculations would yield meaningful delta-deltaG's even, for a range so small (within 1 kcal / mol over the set of 4 panels). Perhaps the authors could remove some of the cutoff analysis and instead focus on rationalizing the mechanism of action for the CpAM's (allosteric modulators), which somehow appear to be interacting with or modulated by the ion binding locations.

6) In the second paragraph of the subsection “Capsid flexibility and dynamics”, the authors refer to promoter chains C and D, but this is not introduced until Figure 3 (although they refer her only to Figure 2).

7) In Figure 3, it seems like the color scheme of the angles is related to the symmetry points, which is not the case. Also, the plots are a deviation from the angle, so they should be labeled deltaϴ.

8) Figure 4 seems to cover only (the last?) 1us of simulation (but says it's 1.1us). It is not evident at all to me that panels B and C show more symmetry breaking than others, e.g., why is C more dramatic than E?

9) In Figure 8—figure supplement 1, the authors should specify a little better what was done. The sentence: “Two average maps (…) were rendered to 1 ̊A resolution, with a pixel size of 0.25 ̊A.” Does this mean that they were low-pass filtered to 1 A (this would be better wording than "rendered to 1A") but then the correlation between the two maps was only 2.3? In that figure, the actual values of the FSC at 0.143 should be indicated for all curves (in A). Given the modes are not correlated, why would the authors think local resolution would be a valuable metric to use? Also, for panel D, it seems that they altered the sampling rate (pixel size), so two things are changing here, but no comment is done on either of them (whether there were expectations, etc.).

Essential revisions of the presentation:

10) Please simplify the rather extensive analysis into more digestible findings. Some figures could be moved to Supplementary Information (e.g. Figure 3) to help focus the big take-home messages. Along the same lines, Figure 1A should have a scale bar and the authors should discuss in the introduction how many MDa and/or atoms are in the system to quickly characterize the size of the capsid for those less familiar.

11) The findings relating to cryo-EM are interesting, they probably should not be the main message of the paper. In this part of their analysis, the authors should emphasize that in this new era of increasing resolution in cryo-EM, capsid flexibility might become the rate-limiting factor to achieving true atomic (1-2 A) resolution, and propose that symmetry relaxation methods are attempted.

12) While some references are cited (e.g., Tama and Brooks, May and Brooks), it would be helpful to have some discussion in the text of theoretical work that has been done on the collective (e.g., normal mode) motions of viral capsids and the extent to which the present all-atom simulations confirm and extend these earlier analyses.

13) There appear to be no references to recent work being done on asymmetric reconstructions of viral capsids [see, for example, the work on bacteriophage MS2: X. Dai, Z. Li, M. Lai, S. Shu, Y. Du, Z.H. Zhou and R. Sun. In situ structures of the genome and genome-delivery apparatus in a single-stranded RNA virus. Nature, 541 (7635), 112-116 (2017)]. It would be helpful to call the reader's attention to the fact that cryo-EM reconstructions of this kind have been carried out in which icosahedral symmetry is not assumed/imposed. Indeed, this new work is what makes the present manuscript even more interesting, and vice versa.

14) The title should capture the big discovery presented in the paper, to help funnel the readers to the findings and conclusions. It might be helpful to include explicit mention of the importance of dynamics and asymmetry. E.g., "Chemical-physical characterization of dynamics and asymmetry in the hepatitis B virus capsid, as determined by all -atom molecular dynamics simulations", or just "Dynamics and asymmetry in the hepatitis B virus capsid, as determined by all -atom molecular dynamics simulations".

Optional revision:

15) PCA analysis on the asymmetric unit or a subset of the entire system should be performed. Such an analysis may reveal clearer modes that could then be used as reduced variables back into the large simulation to find simpler motion correlations. For instance, perhaps showing the motions of the virus only as related to the previously suggested motions (expansion, twisting of Cps, etc.) and showing that they are not occurring (or at least not alone) may be informative.

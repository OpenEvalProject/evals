# Peer review - Round 1

Editors:
- Suzanne R Pfeffer, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04535.026](https://doi.org/10.7554/eLife.04535.026)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Visualizing the functional architecture of the endocytic machinery” for consideration at eLife. Your article has been favorably evaluated by Vivek Malhotra (Senior editor), a Reviewing editor, and 3 reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision. In summary, all the reviewers agree that you have taken the analysis of endocytosis to a new level. However, presentation in eLife requires that the work also advance our understanding of an important biological process. We would be happy to reconsider the work if it includes an advance in our knowledge, in addition to addressing the detailed comments that follow below. Please pay particular attention to the critique on the method description, accuracy and tests. (Because the reviews are lengthy, we include them all to help you.)

Reviewer #1

This manuscript presents a comprehensive analysis of the dynamics of components of the Clathrin-mediated endocytosis machinery in yeast Saccharomyces cerevisiae. The authors used a centroid-based estimation of localization. Since the number of molecules on the clathrin coated vesicles CCV is in the range of 50-100 and the CCV have a regular shape, the center of mass of molecules can be localized with a few nm accuracy. The authors used mCherry labeled Abp1 as a base line and aligned other components of the endocytic machinery relative to Abp1 in space and time. This approach yielded a comprehensive description of the primary events occurring during CME in yeast.

The idea of aligning proteins to the center of mass of other proteins and building a comprehensive description of the relative activity of the endocytic machinery in space and time is interesting and promising. Since the method provides the time resolved behavior of the center of mass, the more detailed spatial organization of molecules on CCV was studied by CLEM (correlation of light microscopy with EM) and super-resolution microscopy. Using this approach, the authors describe the order of assembly and movement of the CCV proteins during invagination. The FRAP experiments allowed them to discriminate between different models of actin polymerization.

The study is potentially interesting but there are two main problems, one is technical and the other conceptual. The accuracy of the results critically depends on the accuracy of the trajectory alignment procedure used. Unfortunately, the description of the alignment procedure is cryptic (see below). In addition, even with an accurate procedure, every computer-based procedure will in all likelihood contain some implementation bugs. Therefore, its accuracy has to be tested in well controlled experiments.

One additional problem is that the precise question addressed by this study is unclear. I do not wish to dispute the fact that the quantitative analysis of CCV assembly and invagination is an important contribution. However, such a thorough analysis should also translate into some significant conceptual advances to merit publication in eLife. This is not apparent from this study. There are a number of potentially interesting points that the authors make, such as the specific orientation of coat-associated proteins, the order of proteins (e.g. Sla1 and End3) assembly, the formation of a BAR domain lattice on the tubular part of the invagination, the predicted bending forces exerted on the membrane, the activation and termination of actin filaments nucleation prior to and following vesicle scission. My impression however is that these are only incremental advances more than a true discovery.

Technical comments:

1) The accuracy of correction of chromatic aberration was not estimated, but it is expected to be in the range of measurable values. The alignment to the Abp1-mCherry is valid, because the systematic shift is common for the same type of fluorescent protein. However, the comparisons of shifts are valid only between the same fluorophores, e.g., Sla1-GFP to End3-GFP, but they are not for GFP and mCherry without a quantification of chromatic correction uncertainty.

2) This work is critically dependent on the accuracy of trajectory alignment. Unfortunately the procedure of two color alignment is very hard to follow. For example, in the Materials and methods: “These trajectory pairs were then used to align the average trajectory of the protein of interest to the average trajectory of Abp1-GFP […] that aligned the Abp1-GFP average trajectory to the Abp1-mCherry trajectory in the trajectory pair.” I am confused about which average trajectory aligns to which and how they are averaged. Were the tracks of Abp1-mCherry and of the GFP-proteins aligned independently of each other? I do not find it logical that a two-step alignment has higher accuracy than a single step alignment, against what the authors claim. All additional procedures have to increase uncertainty. In the case of doubling the number of measurements, the uncertainty decreases only by a factor square root of 2. Without a detailed description and controlled test it is impossible to judge the real accuracy of the proposed procedures. The correctness of error propagation is critical for the conclusions, but it is not reported in detail.

3) The number of molecules was estimated by a two-step comparison of fluorescence of the kinetochore proteins Nuf2 and Cse4. Unfortunately, the authors did not estimate the increase of the uncertainty by the additional step, but just multiplied the uncertainty of the first step by a scale factor (see Methods “Quantification of the number of molecules”). As such, the accuracy of number of molecules is overstated.

4) In the chapter “Assembly of Rvs proteins at the neck of the invagination” the authors described fitting procedures and estimations that are supposed to be numerical. Unfortunately, they did not provide any quantitative data and fit uncertainty estimation, but only a cartoon on Figure 4C. The small Figure 4B just gives a crude value 100+-(?) molecules in the scission neck. The curve on Figure 4A raises the question of whether a fraction of Rvs has to be on the plasma membrane side of the scission neck. After cutting the neck the membranes with Rvs move to opposite directions, with the vesicular part moving towards the interior and the PM part moving retrogradely. One could expect that it will be reflected in an oscillatory behavior of centroid with mean position in the center of the neck and high level of uncertainty. Unfortunately, this process is below the time resolution of the authors' technique. The curve on Figure 4B shows a fast shift toward the vesicle. The authors commented that Rvs persists 2 sec longer on the vesicle than the plasma membrane. But another possible explanation is that a larger fraction of Rvs localized above the scission plane, something that would be inconsistent with the cartoon on Figure 4C. The spreads of red and green points on Figure 6F are clearly different, but the difference in SD is rather minor (15 and 18nm).

Figure 1–figure supplement 2A: units of Y-axis are neither on the figure nor in the legend.

Figure 1–figure supplement 2D has 3 mistakes:

1) The optical slice depth 400nm is an overestimation. A well aligned confocal microscope has f ∼ 750nm.

2) I suppose that the radius of a cell was taken equal 2.5 um, but it was not mentioned on the figure and in the legend.

3) In the formula on 2D there is a mistake: the square root is missing. It has to be sqrt(1-f^2/(4 * r ^2)) * I. The estimation of maximal error is done with an over-optimistic optical depth and by a wrong formula that result in a 0.6% value in the legend. Moreover, this value is inconsistent with the value in the main text where it was given as 10%.

On Figure 5A the color scheme is far from optimal. I could not figure out from the figure and legend which tracks belong to Abp1 and which to Myo5.

Movie 2 is packed with some uncommon codec, so I could not see it on two computers under 64bit Win7 and 32bit Win8 OS respectively.

Reviewer #2

Major novel findings are limited as no new concepts are discovered. The idea that actin polymerizes primarily at the base of the pits is not really new (due in part to work of Kaksonen himself; a google search for images of actin at yeast actin patches or clathrin coated pits reveals that most schematic cartoon place actin polymerization at the base of the invagination), although this is proved elegantly here. On the other hand, this study is highly quantitative, fluorescent proteins are expressed at endogenous levels and the findings are supported by a large number of controls.

Issues to be addressed with discussion or new experimentation:

A major open question in the field is whether the dynamin homologue, Vps1, participates in fission at yeast actin patches. The authors mention Vps1, but do not show any data. Given the focus of this study, it would be great if the authors could analyze Vps1 and make a conclusive statement on this highly controversial topic.

The experiments with photobleaching of actin do not go past the time of scission (time = 0s). Thus, it remains unclear whether actin polymerization continues after scission. In this connection, several studies carried out on mammalian cells have demonstrated the occurrence of actin tails propelling newly formed endocytic vesicles. While tails were first described at sites of non-clathrin-dependent endocytosis (Merriefield and Almers, PMID: 10559868), a recent eLife paper demonstrated that also clathrin coated vesicles nucleate actin tails when the dephosphorylation of PI(4,5)P2 is impaired (Nandez et al., PMID: 25107275). Thus, while the present study proves what had been implicit in previous studies, i.e. that actin nucleation occurs at the base of the invagination, could some actin eventually nucleate also from the newly formed vesicle (for example at the site of the scar left by the fission)? The authors show that a pool of Rvs remains partially associated with the vesicle and one wonders whether some actin nucleating factors may be present at the same site.

Concerning Rvs (the endophilin homologue): it was shown that endophilin deficiency at neuronal synapses results in a defect in uncoating, most likely due to a deficient recruitment of synaptojanin, a PI(4,5)P2 phosphatase (Milosevic et al., PMID: 22099461). The Rvs pool that remains associated with the endocytic vesicles may be needed for uncoating, as Rvs167 binds a yeast synaptojanin. The authors may want to comment on this.

The authors state that as the number of Las17 molecules start decreasing before fission, suggesting that fission may not be assisted by the force generated by actin polymerization. Yet, one cannot exclude that the remaining Las17 may still be needed to generate a force. Photobleaching experiments show continued actin nucleation at least until the time of fission. As tagged Las17 does not behave as wild type Las17, these experiments must be interpreted with caution.

Why is Las17 not drawn bound to the membrane in the cartoon of Figure 7B? Las17/nWASP are actin nucleators at the plasma membrane.

The authors state that the number of Sla2 molecules remains relatively constant prior to scission, yet this is contrary to the data provided (Figure 2B, 3C and 7A), which shows that the number of Sla2 molecules starts declining a few seconds before scission.

Despite the thorough analysis of the correlation between changes in membrane shape and the recruitment of endocytic components, it remains unclear what causes the initial buckling of the plasma membrane. This work favors the idea that the initial deformation coincides with the nucleation of actin (Figure 7B), in line with the view presented in Kukulski, et al. (2012). The stronger evidence in favor of this model is that in the presence of Latrunculin A, no invaginations are observed (Kukulski et al., 2012). Idrissi et al. (2012) however, shows that there is an initial deformation of the membrane even in the presence of Latrunculin A. An alternative model suggests that early endocytic proteins like Syp1, Ede1 and Ent1 may act as the initiators of membrane curvature. What does the recruitment of these early endocytic proteins look like in this model and how does it relate to changes in membrane shape? Is the initial deformation the result of early endocytic proteins like Syp1, Ede1 and Ent1 coupled with actin polymerization? I note that, as often pointed out by Tom Kirchhausen who has extensively studied the structure of the clathrin lattice, it is unlikely that a flat clathrin lattice may convert to a curved clathrin lattice without undergoing a complete disassembly. Thus, it would seem more likely that the initial coated patch may already be curved. I realize that a thorough analysis of the spatio-temporal localization of early endocytic factors may go beyond the goal of this study, but these considerations should be discussed.

Reviewer #3

This is rigorous, technically demanding work on an interesting biological process. I am generally enthusiastic about the work and the presentation, but think that the authors should have taken a broader perspective on their work, since their work confirms many of findings and ideas of others working on fission yeast. That previous work does not detract from the value of the present work, but it should not be ignored.

Scientific issues:

Results section: “We thus produced a dataset in which all average trajectories are aligned to Abp1.” I am not concerned that some information was lost during averaging. The individual tracks in Figure 1B and D average out all of the lateral motion of the patches, because the motions to the right and left of the normal (zero on the x-axis) to the plasma membrane cancel out. This representation may not give the casual reader the right impression about the patch motions, which would be more apparent with plots of the averages of the absolute values of the left and right positions.

In the first paragraphs of the Results section: It might be informative to compare the patch alignment method used here with that of Berro (MBoC, 2014). My impression is that the two methods work about equally well. Berro discusses the biological variability. Do you have any measure of the biological variability in your system, since you seem to assume none. You should state this assumption, if you made it.

In the subsection “Organization of coat associated proteins”, in Results: An average localization precision of approximately 10 nm is extremely good; what is the evidence that the resolution is actually 10 nm?

In the beginning of the subsection “Assembly of Rvs proteins at the neck of the invagination”, in Results: The approach to calculating the membrane area covered by the Rvs dimers is identical to Arasada (2011) in fission yeast. Comparing the results may be informative.

In the same section: Berro, MBoC (2014) has evidence that the movements of the actin-covered vesicle are diffusive in the cytoplasm.

In the beginning of the subsection “Assembly of the actin cytoskeleton”: “The Myo5 trajectory remained almost stationary during the invagination of the plasma membrane, whereas the Las17 trajectory moved inward, but much less than Abp1, Arc18 and Act1 trajectories.” The behavior is similar in fission yeast (Arasada, 2011).

In the same section of the text, you state: “Note that because GFP-Act1 was expressed in addition to untagged actin, we do not know the ratio between tagged and untagged molecules that are recruited to the endocytic site and we can only provide relative abundance estimates.” Rather than using arbitrary units for Act1, measure the ratio of GFP-Act1 and wild type Act1with an anti-actin immunoblot and give the numbers of GFP-Act1 and the fraction tagged, allowing for a calculation of the total actin. Wu (2005) and Sirotkin (2010) explain how to do this.

In the beginning of the subsection “Actin polymerizes at the base of the invagination”, in Results: The FRAP experiments are elegant and informative. Abp1 is a nice control. However the authors do not include the most obvious model in Figure 6A, namely that new branches are formed on pre-existing filaments in proportion to the local concentration of the NPFs and then grow in random directions. This is what is expected from the mechanism of branch formation and does not presuppose a mechanism to align the branches in a certain direction (which seems unlikely). Arasada (2011) uses this assumption and the data in Figure 6F strongly support it. My impression is that the FRAP data are consistent with this model with local nucleation and random elongation, which the authors could simulate knowing the local concentrations of the two NPFs as established in this paper. Capping may be favored near the membrane (as assumed by some models of leading edge motility) and may bias the direction of growth, but the authors do not consider capping or other mechanisms to bias growth.

In the subsection headed “The endocytic coat”, in the Discussion, you state: “The disassembly of Sla1 and End3 begins after membrane invagination has started, but several seconds before scission, suggesting that these proteins may be important during early stages of vesicle budding.” This supports the model of Chen (2013) with adaptor proteins binding actin filaments to provide mother filaments to start the branching process.

Still in the Discussion, the first paragraph of the subheading “Endocytic actin network”: Berro (2010) uses data similar to that in this paper to calculate the evolution of the rates of the main actin assembly reactions from the beginning to the end of the patch life, so one does not need to speculate about “these data suggest that the nucleation of new actin filaments stops before vesicle scission occurs.” Dissociation of the NPF's is enough to explain the slowing of the rate of branching.

Subsection headed “The functional organization of the endocytic machinery”: Figure 7 is the budding yeast version of fission yeast data in Figure 7 and Table 1 in Sirotkin et al. (2010). Arasada 2011 and Chen 2013 have additional quantitative data on other fission yeast actin patch proteins. The timing and numbers of molecules are remarkably similar in the two yeast in spite of >400 my of divergent evolution. This certainly deserves some discussion. The new data in this paper leads to conclusions similar to those in the fission yeast papers. Given this new data from budding yeast, it would be interesting to make a formal comparison with fission yeast actin patches, including the peak times, peak numbers and depth of penetration of each homologous molecule: actin, Arp2/3 complex, Wsp1 (Las17), Myo1 (Myo5), Cdc15 and Bzz1 (Rvs167) and End4 (Sla2).

Figure 7 legend: I would call the GFP-actin signal “polymerized actin” rather the “actin cytoskeleton,” since you use the latter term for actin filaments plus associated proteins. Since you can calculate the total numbers of polymerized actin molecules at each point along these curves and since you know the numbers of Arp2/3 complex, you should be able to make some simple calculations such as the lengths of the filaments and numbers of branches formed each second.

Figure 7B legend: “Time ≈ -8 s: actin polymerization starts.” This drawing is misleading, since it shows Sla2 binding a branch, whereas the biochemical evidence strongly shows that branching only occurs on the side of a pre-existing filament. Where do the pre-existing filaments come from? Chen (2013) has one possible source. The drawings of the later time points show that the network propagates correctly from mother filament to branch, but this is not obvious, so it would be helpful to have some clue showing that the first branches end up at the tip of the invagination.

The model considers the branches to be stable, but actually the branches and the filaments are actually turning over rapidly on the time scale of this figure (as shown by the simulations of Berro, 2010). It would be helpful if the figure or the text could indicate this turnover.

Note that Berro, MBoC, 2014, has more realistic scale drawings the filaments in slices through actin patches. If the actin numbers are similar in budding yeast actin patches, you could make less schematic drawing of the actin network base on his calculations.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Visualizing the functional architecture of the endocytic machinery” for further consideration at eLife. You will be pleased to learn that your revised article has been favorably evaluated by Vivek Malhotra (Senior editor) and Suzanne Pfeffer, a member of the Board of Reviewing Editors, and two reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance.

The referees were pleased that you took the reviewers' suggestions seriously. Nevertheless, Thomas Pollard (peer review) wrote: ”My main concern with the original paper was its narrow point of view. The presentation generally ignored highly relevant work on other organisms, especially fission yeast. The new work on budding yeast offers valuable, new insights, but much of the story is remarkably similar to what was found in fission yeast. Making this clear highlights the amazing conservation of the mechanisms over the hundreds of millions of years since these two yeast diverged. These comparisons detract in no way from the authors' accomplishments. Also, the authors seem to have misunderstood several suggestions to compare the data from the two yeasts. They declined to do so, saying that this would require new experiments. However, all they needed to do was to plot the published data on the same graphs as their new data and comment on what is the same and what is different.

Second, citations: The authors added citations to some of the work on fission yeast, but missed some opportunities to inform a reader about what was known. Here are two examples:

Counting total actin from the numbers of GFP-actin and the ratio of GFP-actin to untagged actin: the new data look good, but the method developed by Wu was not cited.

Idea that adaptor proteins bind actin filaments to provide mother filaments for Arp2/3 complex to start the branching process: The revised text makes this point and cites four papers, three dealing with the discovery of the adapter proteins, none of which mention Arp2/3 complex. This gives the impression that these early paper rather than the Chen paper came up with the idea.

Finally, (not essential) in terms of the idea that the dissociation of the NPF's is enough to explain the slowing of the rate of branching: I was hoping that they would use their data to calculate the rates of the reactions, as done before by others. This would be nice but is not essential.”

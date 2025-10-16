# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- Richard A Neher, University of Basel Switzerland
- Mark Zanin, St. Jude's Children's Hospital United States

## Review text

DOI: [10.7554/eLife.43764.027](https://doi.org/10.7554/eLife.43764.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Influenza A virus surface proteins are organized to help penetrate host mucus" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Richard A Neher as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Arup Chakraborty as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mark Zanin (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Vahey and Fletcher investigate the importance of the spatial organization of hemagglutinin and neuraminidase in facilitating the movement of influenza A viruses (IAVs) through mucus. They report that neuraminidase proteins cluster at one pole of the virus and this clustering asymmetrically frees the virion from tethering to sialic acid, thereby facilitating directed motion. This is an interesting novel finding that provides insights into outstanding questions in the field. However, a number of issues need to be addressed before we can recommend publication.

Essential revisions:

The issues raised during review and the ensuing discussion broadly fall into four categories concerning i) further quantification, ii) the theoretical model, iii) direct assays of infectivity, and (iv) availability of analysis code.

1) A number of statements would benefit from more quantitative analysis.

a) Figure 1 should show distributions of data rather than representative examples. Figure 1A could, for example, be backed up by two histograms showing NA/HA intensities in the first/last 20% of the virion. Or last/first 100nm or similar. Figure 1D needs a distribution of correlation coefficients of HA/NA. Showing one example is simply not enough. Figure 1E should show distributions as well. Bar graphs are not good.

b) Figure 3A-C: While the measurement of the persistence of orientation is useful and interesting, we would like to see a quantitative and direct assessment of diffusivity, for example by comparing MSD vs time for the deletion mutant and the WT NA. It should be quantified whether the morphology of the viruses change when the cytoplasmic tail of NA is deleted. If so, does this affect the ability to determine the orientation of the particles?

c) Figure 4C D: Again, you should try to find a meaningful quantitative comparison rather than just showing examples.

d) Other statements need more precision: E.g. Results section, paragraph one: How were polarized viruses selected? What fraction of particles were filamentous? etc.

2) The theoretical model should be explained more clearly and connected better to the experimental results.

a) We suggest moving some of the descriptions of the model into the main text and maybe include an illustration of the model, the sialic acid distribution along the particle, and the resulting directional motion. It would also help to discuss in more simple and explicit terms that how macroscopic diffusion increases with more directionally persistent microscopic motion.

b) When describing the different physical effects, you should be careful not to confuse the reader with diffusion constants of NA, receptors, and viruses all labeled D. Please differentiate them with different symbols or subscripts.

c) The model prediction that very slow sialic acid diffusion results in slow virus diffusion should be better explained. How does this prediction compare with the experiments in Figure 2 using coverslips functionalized with biotin-anchored (and presumably immobile) receptors?

d) Please point out that Figure 4—figure supplement 1 essentially only shows the first-passage probability calculated in the supplement (please number equations and refer to them directly). This figure could be improved by changing the x-scale seconds -> minutes and illustrating more generally how increasing virus diffusion increases the probability of reaching the epithelium. You could add several curves for different D, plot this on a log scale, and remove the 5000x.

e) The assumption of an absorbing boundary at the epithelium implies that binding is essentially instantaneous and irreversible. This should be discussed.

3) Additional infectivity and/or mobility assays.

a) Could infectivity be assessed directly using mucus-producing cells such as CaLu-3? Such data would considerably strengthen the claim that enhanced diffusion increased infectivity.

b) Enhanced diffusion in polarized filamentous virus compared to spherical viruses is counteracted by their larger size. Is there a head-to-head comparison?

c) The data in this paper was obtained using viruses containing fluorescent labels. Have the authors confirmed these observations using unlabeled viruses? Whilst obviously fluorescent microscopy could not be conducted with unlabeled viruses, the morphology of virions propagated in mucus-producing cells could be compared to those propagated in non-mucus producing cells and studies of their ECL tracks could possibly be conducted. This experiment could add further weight to their statement that filamentous morphologies are adaptations to replication in the presence of mucus.

4) Simulation code and analysis scripts need to be made available, preferably on a repository like GitHub with appropriate documentation.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Influenza A virus surface proteins are organized to help penetrate host mucus" for further consideration at eLife. Your revised article has been favorably evaluated by Arup Chakraborty (Senior Editor) and a Reviewing Editor.

By and large, the authors have presented a compelling revision. They have quantified a number of previously rather qualitative statements by showing distributions rather than representative examples, present additional data on virus mobility directly comparing NA and NA-DCT viruses, streamlined notation, and explained the theoretical model better. However, there are a number of remaining issues that we would like to have clarified/rectified.

Figure 1: the distributions are useful, but the alignment of the NA rich pole with NP seems rather imprecise. Reading the previous version of the manuscript, I was certainly expecting a more clear cut picture. The insets in Figure 1A also suggest a much more pronounced asymmetry. How closely is this more blurry picture accounted for in the simulation?

Figure 1E, Anticorrelation of HA and NA: This anticorrelation is pretty weak and the main take home message from the figure seems to be that HA and NA are clustered. Hence I think the statement "...NA clusters that appear to largely exclude HA" is too strong.

Figure 1G seems problematic. The caption states that p-values are calculated using a two-sample t-test. What enters as independent data point here? Strictly speaking, you have n=4 replicates and I doubt that this would support the conclusion that these cases are different. A paired test on +/- NAI samples from the same replicate would probably be more powerful. Generally, quantifying the difference (and confidence intervals) between two conditions is preferable to rejecting a null.

The addition to Figure 4E does not help. This figure shows that there is little evidence for variation of ECL intensity and HA-NA polarity. Making an arbitrary cut at 0.06 and fitting lines to points below and above is not appropriate. Furthermore, a correlation of ECL intensity and HA-NA polarity doesn't quantify the examples given in C or D. You could try to show ECL intensity distributions aligned with the NA polarity or similar. But as of now, panels C, D, and E are just examples.

The comparisons of diffusion with/without correlations make sense only when you specify the time interval over which the displacements are measured (paragraph three of subsection “Polarized viruses step persistently away from their NA-rich pole”). You do so later, but I'd suggest moving it forward.

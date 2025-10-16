# Peer review - Round 1

Editors:
- Merritt Maduke, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58100.sa1](https://doi.org/10.7554/eLife.58100.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript presents structures of two "CdiB" transporters, which serve as microbial defense systems, secreting substrate CdiA proteins to trigger toxic effects on competing microbes. To relate structure to function, the authors developed a functional assay and validated the role of the observed conformational change in the transport mechanism.

Decision letter after peer review:

Thank you for submitting your article "Structural insight into toxin secretion by contact dependent growth inhibition transporters" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Merritt Maduke as the Reviewing Editors, Reviewer #1, and the evaluation has been overseen by and Olga Boudker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Dukas Jurenas (Reviewer #3); Trevor Moraes (Reviewer #4).

The reviewers have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that if it is not feasible to do the experiments that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

In this manuscript, the authors report their findings on a type Vb two-partner secretion system, represented by CdIA and CdIB proteins from Acinetobacter baumannii and Escherichia coli. In this system, outer membrane protein CdIB is responsible for secretion of its substrate protein CdIA from periplasm to the extracellular environment, which then is delivered to a cell of a competing microbe, triggering its toxic effects on that cell. Thus, this system acts to inhibit growth of competing bacteria. Here, the structures of two CdiB transporters are presented. Previously, only one TpsB structure had been determined. The two new structures adopt two different conformations, one overlapping with that of the previous structure, and one new conformation involved a repositioning of a DxxG motif that is unique to the TpsB transporters. The writing in this manuscript is excellent; the Introduction clearly set up the background, original discovery of contact dependent inhibition, and the known biochemical/structural information about the type Vb secretion system. To test the functional relevance of predicted conformational change, the authors developed a secretion assay that measures secreted CdiA protein by Western blot, and they tested predictions via cross-linking, complementarity, and mutational analysis. The authors additionally perform MD simulations to evaluate energetics of removal of the H1 helix from the pore. The simulations support the main thrust of the paper, but there are major concerns that must be addressed. In summary, this manuscript presents the first structures of CdiB transporters, identifies conformational change in a critical structure motif, confirms the functional relevance of the observed conformational change, and uses MD simulations to lay groundwork for future experimental analysis of CdiB transport mechanism. Going forward, we look forward to follow-up work such as structures with bound substrates/substrate peptides, structures of mutants, and experimental (e.g. EPR/DEER) results on CdiB conformational dynamics. Overall, once issues with the MD simulations are addressed, the results presented in this manuscript will be of broad interest to scientists studying mechanisms of membrane proteins.

Revisions for this paper:

Experimental:

1) In Figure 6B, the authors show that the GGAG mutant increases apparent activity, which is ostensibly consistent with their model. However, it is feasible that the increase in CdiB(Ab) secretion is due to increased cell lysis (as occurs with the Ec homolog, Figure 4A) rather than to increased secretion activity. Therefore, it is important to show a control for this experiment. If an experiment is not possible at this time, then the paper should be revised to specify the caveat.

2) Figure 5B would benefit from having a WT CdIB protein as control (as was done in Figure 6A). Also, the statement that "CdiBAb was detected in the pellet after 20 minutes and remained at a constant level over the 100-minute time course, in the presence or absence of TCEP" does not seem correct, as the band intensity increased from 20min to 60min. Please correct this statement and if possible shown densitometry analysis on the bands to better quantify and describe the observed phenomenon.

Simulations:

The computational expert who reviewed the manuscript provided specific comments that we agree are essential to address. The reviewer's comments are as follows:

– Regarding the suggestion in subsection “Structural differences in helix H1” these two structures demonstrate mobility of the helix. How can we be certain that this difference in position is not a transporter dependent difference? This is exactly where the simulations could really help support this argument.

– Do the authors really see the CdiBAb simulation interconvert between the two beta1 configurations as stated in subsection “Link between DxxG conformation and position of H1 helix”, or do they only see one direction (unravelling)? I can't tell from the videos because it is too small. I would really like to see this analysis and any follow up, because while the removal of the helix in Figure 7 is very difficult to accurately capture, these changes are doable. Is there a lipid that plays a role in this happening? The authors do three simulations of each structure, is the lipid placement the same in each case or does that get reinitialized too?

– I want to give my general impressions of the helix removal simulations. I like that the authors used both umbrella sampling and SMD, but I must say that given the very large energies (and they may actually be very large) and significant contact between the helix and the barrel, I am completely unconvinced by this analysis as it stands. In agreement with the authors, I also worry about a number of things: the reaction coordinate, potential protein conformational changes in the barrel and loops, the action of other elements from the periplasm or extracellular spaces, and most importantly sampling. I am concerned that with a few microseconds of enhanced sampling, you are not going to answer this question adequately, and you may arrive at completely wrong conclusions. For instance, I am left with the impression that the authors believe that the helix unravels to exit, and while it may undergo conformational changes, I don't think it is going to look like your SMD where the entire thing is unravelled in the aqueous environment. My first reason to not think this is the case are the two structures – we see the helix move quite a bit, but it is a well-formed helix in both cases. Moreover, if you run the helix through DISOPRED, is there reason to think that it is marginally stable as an α-helix?

– Personally, I would really love to see a very careful PMF carried out between the two states that you currently have. Create a homology model of one structure using a template of the other, where needed, or do some other kind of targeting, and then really sample the move from one to the other. This alone would be really hard, and might take tens of microseconds, if not more, to get a converged data set, but there are some really good features of this approach:

– it is much more tractable,

– you have end points that you believe, and

– you will learn a lot about what it takes to move the helix in this barrel and how the helix and rest of the protein have to adapt to do it.

– With my 2 cents given, I am not opposed to including the current PMF and SMD (although, I wouldn't do it personally), but I really would like to see more simulations to feel better that you have reached some kind of convergence. This is outlined below. Moreover, I would include these as supplemental figures where I focused more on the very general big picture ideas of overall energies supporting one reaction coordinate/transformation over another, etc. But that is my opinion, and I don't want to tell you how to write your own paper (ok, I gave another 2 cents here).

PMF calculations

– How were the actual snapshots generated in the 50 windows? Did you use rigid rotation, or did you seed 1 window from the last? If you used rigid rotation/translation, what were the sterics like prior to each run? Did you minimize, etc? I think it would be most ideal to carry these windows out sequentially, where you start in the X-ray structure state, carry out a 20 ns simulation under restraints, and then pick back through the simulation to identify the snapshot that moved the farthest along your reaction coordinate to seed the next step.

– Figure 7C should have bootstrap error estimates, in my opinion. If it can't be done in Alan Grossfield's implementation (I can't remember) there are some Gromacs tools to do this and mBAR can do it too. It is important to down sample your data here in each bin, however, so that you don't use correlated snapshots. Given the complexity and size of this system, this is going to be very important to see. I would especially like to see in a reply the side by side comparisons of the figures here with any recalculated taking into account correlations.

– As far as I can tell, it looks like each PMF is made up of about 750-1,000 ns of aggregate data. While there are important questions about how this is seeded and the progress coordinate used, I would at least like to see 1 or 2 more of these PMF profiles for each of the two conditions generated using completely independent simulations to assess the role of sampling in the computed PMF values.

SMD simulations

– Two independent runs per each condition (each about 150-200 ns), but only 1 profile is plotted for each in Figure 7A and B. Did you plot the average of the two? Given the small amount of time used to generate these, I would certainly compute 3-5 more SMD runs per condition and make a plot with all of the runs so that we can assess the role of stochasticity and non-equilibrium pulling versus the differences in the protein and or mutation in the protein.

– Finally, do you see any correspondence between the structural conformations that come out of your PMF and the SMD? You might have mentioned this, but I didn't catch it. This kind of analysis would again make me feel better about the convergence, but since you don't seem to favor the helix exit as a helix, maybe you don't want to get into that.

The statistics on the simulations is inadequate.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for re-submitting your article "Structural insight into toxin secretion by contact dependent growth inhibition transporters" for consideration by eLife. Your article has been re-reviewed by two peer reviewers, including Merritt Maduke as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Olga Boudker as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Revisions:

It is great to see that PMF profile was extended and additional simulations run. The new PMF is very different from the previous ones. We would have liked to see more of an attempt to rationalize the distances and compare with this propertied structure. Are they at all close in a semiquantitative manner? For future studies, cross linking from this intermediate state would be ideal.

For the current study, the authors should qualify their PMF in the final text and include a statement noting that they got very different results for the same starting conditions, which highlights the high degree of uncertainty in these kinds of calculations, especially when the end point structures are not known.

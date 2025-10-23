# Peer review - Round 1

Editors:
- Irene E Chiolo, University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60577.sa1](https://doi.org/10.7554/eLife.60577.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The revised manuscript shows elegant and compelling evidence that the dynamics of Rad52 molecules inside repair foci are consistent with the existence of a liquid droplet surrounding repair sites. Using single particle tracking (SPT) and Photo-activatable Localization Microscopy (PALM), the study also reveal that the ssDNA-binding protein RPA display a different behavior from Rad52, being mostly chromatin associated. Together, this analysis and the related conclusions significantly advance the field of nuclear dynamics in the context of DNA repair.

Decision letter after peer review:

Thank you for submitting your article "Single molecule microscopy reveals key physical features of repair foci in living cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option.

Summary:

In this manuscript by Miné-Hattab and colleagues, the authors use single-molecule imaging approaches to investigate local dynamics of Rad52 foci at DSBs in budding yeast, which is an important area of investigation. They show that the dynamics of Rad52 molecules inside foci are consistent with protein movement within LLPS domains, while Rfa1 dynamics are not. Their data also provide supporting evidence to previous observations that repair sites cluster within the nuclei, and suggest that clustered foci behave as larger phase separated structures. While the idea that Rad52 and other repair proteins form phase separated domains is not novel, this study presents higher resolution data in support of this model. The reviewers generally agree that the study is interesting and well conducted, but the conceptual advancement is limited and a significant revision is needed for publication in eLife. Specifically, more convincing experiments demonstrating that the observed Rad52 dynamics reflect LLPS are required. Evidence that the dynamics are relevant for DNA repair and genome stability should also be provided. Additionally, the study should be better integrated with previous studies, statistical analyses need to be more rigorous/better presented, and a revisions of the text should include a clearer separation between observations and speculations.

The following is a summary of the main points brought up by the reviewers, including after consulting with each other.

Experimental revisions:

1) Additional data need to be provided to draw conclusions about whether or not the authors' observations are reflective of phase separation. Specifically, additional mobility studies in conditions that disrupt LLPS (chemical treatments and mutations) are needed, both for the individual protein and for the foci.

2) Regarding the possible categories of traces evaluated, one category is not included in the study. The surface tension that defines LLPS-dependent bodies is known to both help maintain focus integrity and partly counter LLPS body fusions. So if the foci represent true phase-separated bodies, have the authors then observed traces where Rad52 molecules interact with yet fail to enter the larger Rad52 foci?

3) How is it possible to distinguish a cluster of binding sites from liquid-liquid phase separation? In the absence of breaks, there are two Rad52 diffusion populations (D=1.2 and 0.3 um2/s), which the authors attribute to monomers and multimers. They don't verify these multimers by alternative approaches (say number and brightness analysis), but it seems like a reasonable possibility. After a break, a third component – slower than the previous two – becomes evident. This slow population coincides with the break. In the vicinity of the break, there is now only 1 component diffusion (D=0.03 um2/s). Also, the motion is now more confined, but not absolutely so. Also, Rad52 diffuses faster than Rfa1, which is bound to ssDNA. At this point, there is no data to distinguish between two possibilities: slow diffusion *or* diffusion + binding. Except, if it were diffusion + binding, one might perhaps expect to still see the free diffusion component.

The authors then turn to diffusion at the boundary (Figure 5), which I agree can be a more informative measure. Here, they see changes in the diffusion estimator for trajectories which cross the boundary, using displacement which they argue is more robust for slow diffusion. The problem is that the “boundary” is determined by the very thing they are trying to measure, not some independent marker of the compartment. In other words, Rad52 defines the compartment, unless I missed something fundamental in the experimental design. Ideally, the way such an experiment would be done to test the hypothesis that Rad52 is forming a LLPS compartment is to look at the diffusion of an inert tracer as it comes in and out of the compartment. As designed, I frankly do not see how the observation of different diffusivities in and out of the compartment distinguishes between a cluster of binding sites and an LLPS. If you accept that DNA-binding is in no way biasing the kinetics, then the authors' interpretation seems like the most sensible one. But the fact that Rad52 is involved in DNA repair makes that a hard assumption to swallow.

Furthermore, I'm not sure I entirely grasp the significance of Figure 6. Since Rad52 can easily escape one focus and enter another, regardless of whether it is a cluster of binding sites or a phase, I don't see how the radius of confinement measurement distinguishes between these two alternatives. The observation that the foci are 2x larger in diploids but at similar density is compelling, although recent data from the Brangwynne lab point out that conserved density need not be the case (PMID: 32405004).

4) In the syntax of this paper, Rad52 is a client in the LLPS, leaving the question of the scaffold unaddressed. After all, the Rad52 focus ultimately disappears, meaning that something caused this phase to be dispersed. So is RPA the scaffold? It might be possible to address both this point and point #3 knowing what is responsible for forming the LLPS in the first place.

Along the same lines, how do the authors reconcile previous findings indicating that recombinant DNA repair proteins phase separate in vitro with their claim that "Rad52 acts as a client of the LLPS but does not drive its formation"?

5) What is the evidence that the biophysical properties observed are of direct relevance to DNA repair? For example, is the mobility of Rad52 within the repair focus important for repair? Is the difference in diffusion kinetics within and outside of the repair focus important for genome stability? What could the authors do to alter that diffusion profile and what would be the consequence on repair? Also, addressing this point implies the need to use a more physiologically relevant system with repairable DSBs, and not the irreparable DSB system used here.

One should easily compare wild-type Rad52 to known Rad52 mutants (that partly or fully abrogate function) to see if there is any correlation between intra-focus mobility profiles and repair. In other words, experiments along these lines may indicate whether a particular intra-focus mobility profile consistently correlates with repair, while this profile is absent in non-functional mutants, or a particular type of mutant. These experiments should be very feasible.

6) Can the authors visualize the fusion of the Rad52 foci/DSBs in live cells within their experimental systems?

7) The statistical significance of most presented data is either lacking or unclear. This needs to be carefully addressed. Providing additional data files may also help the authors strengthen their findings.

Text revisions:

– Several statements made are not supported by the data and without clearly stating that the statements represent speculations. E.g. longer tail is due to Rad52 molecules diffusing slowly inside the focus; observing the 2 populations also in G1 does not necessarily mean that the 2 populations in S/G2 do not reflect replication forks at all. The authors need to carefully revise their claims/statements and consider alternative explanations. Also, the writing is often unclear or confusing and the authors should consider substantially revising it to clarify their claims, clearly indicate speculations that are not supported by the data, and make the text as accessible as possible to non-specialists.

– How was the cell cycle stage determined? This should be better explained.

– Figure 1—figure supplement 1 data appear to show the existence of a partial loss of Rad52 function in the Rad52-Halo cells. This should be clearly stated in the Results and consequent limitations/caveats discussed. Also, please clarify whether Figure 1—figure supplement 1 shows the viability of Rad52-Halo cells in the presence or absence of JF646.

– The authors present no direct evidence for an "attractive potential" that drives molecules towards the centre of the focus. For example, what if the “attractive potential” is simply the focus' boundary surface tension creating a barrier against which some of the molecules inside the focus bounce back towards the centre of the focus?

– The authors state that "Here, we found that upon different levels of Rad52 over-expression, the background concentration increases (Appendix 1—figure 1) suggesting that Rad52 might not be the driving molecule responsible for the LLPS formed at the damaged site." The logical transition here is unclear.

– It is difficult to judge the novelty of this work, as key papers that showed similar conclusions or datasets are not cited. Without direct comparison with other data sets, it is difficult to see exactly where this paper goes beyond published studies.

Here are a few key examples:

a) In the last year the Haber lab published a very similar study in Plos Genetics (Waterman et al., 2019). Although they tracked Ddc2 and Rad51, they also looked at the behavior of separate foci and this paper is not even cited. The data should be compared at the very least.

b) The characteristics of 53BP1 foci have been extensively studied by many labs including those of Altmeyer, Scherthan, DeLange and others, with very similar findings as Miné-Hattab reports for Rad52 (for example, Kilic et al., 2019; Sollazzo et al., 2018, as well as the single molecule work of the lab of Eric Greene). Moreover both rad52 and PCNA foci were studied by Essers et al. (Kanaar and Vermeulen) MCB 2005. 25(21): 9350-9359 and EMBO J. 2002 Apr 15. Comparisons with these studies needs to be made.

c) A number of earlier studies followed Rad52 foci in budding yeast on induced double strand breaks (even using the I-Sce1-cut system used here) that are not taken into consideration. The diffusion coefficients presented here have to be compared with these earlier studies and differences should be resolved by comparing techniques and conditions of imaging. For instance, Dion et al., 2012).

– It is unclear if the “absence of DNA damage” condition discussed in the first section of the Results is the non-induced version of the system described in the second section of the Results. Also regarding these sections, it seems that the “absence of DNA damage” control conditions were not conducted as part of the same experiments with the I-SceI DSB.

– Figure 2C is a little underwhelming. I would like to see one data panel in the main text with the cumulative distribution +/- DSB.

– "in the case of diffusion coefficients D<0.1 μm2/s, we use mean square displacement analysis allowing us to substrate the noise." Subtract the noise.

– One technical point. The fluorescence lifetime of a freely diffusing fluorophore (reported half-life of JF646 is 2.1 sec) is not the same as if it is bound to a protein; in the latter context the fluorophore would diffuse more slowly in the illumination path and be subjected to more rapid photobleaching, making 2.1 sec an overestimation of the half-life/underestimation of the decay rate. At a frame interval of 20ms, photobleaching may be a competitive rate for the disappearance of signal and I am not sure the lack of applying photobleaching correction or saying that the short tracks are not affected by that rate is properly justified.

# Peer review - Round 1

Editors:
- Robert H Singer, Albert Einstein College of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02230.027](https://doi.org/10.7554/eLife.02230.027)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Distinct target search modes for c-Myc and P-TEFb revealed by single molecule tracking in live cells” for consideration at eLife. Your article has been favorably evaluated by a Senior editor, a Reviewing editor, and 3 reviewers, one of whom, Leonid Mirny, has agreed to reveal his identity.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

All reviewers felt that the work was a significant contribution and was novel in its approach to the problem of target search. Yet the reviewers also felt that the work could be significantly improved in the clarity of the writing and in considering other models. In particular, Reviewer 3 had an alternative explanation for the data that needs to be considered. He states “To summarize, my recommendation to the authors is to revaluate their conclusions concerning anomalous diffusion and, at least, to consider intermittent binding as an alternative mechanism. Suggested analysis and simulation may allow estimating sizes of targets and dwell times for c-Myc and P-TEFb. I believe this analysis can only strengthen this solid and important paper.” We suggest you address the issues raised by this and the other reviewers by using the intermittent binding model in your simulations to determine the fit for the existing data on angular distribution.

Reviewer #1:

The manuscript presents interesting results regarding the random motion of two fluorescently-labeled transcription factors (TFs) in mammalian cells. The authors suggest that the different spatiotemporal dynamics exhibited by the TFs represent radically different ways in which they experience the geometry of the nucleus, and that this “protein-specific geometry of the nucleus” may have important consequences for transcriptional regulation.

The work is of significance to our physical, quantitative understanding of gene regulation. It is multidisciplinary in nature, involving state-of-the-art imaging methods, advance image analysis and insightful incorporation of ideas from condensed matter physics.

On the other hand, I think the manuscript can be significantly improved in terms of narrative flow and data presentation. Specifically:

1) I wish the key concept, of compact versus non-compact exploration of space, was introduced earlier and used to actively guide the narrative. As the text is currently written, the reader is exposed to a lot of data that is pretty standard – SPT trajectories and their analysis as diffusive motion – before he/she encounters the novel aspects of the work. This burying of the lead is against the authors' own interest, I think.

2) While an overabundance of optics and imaging details are provided in the main text, essential biological details are missing. For example, it is not satisfactorily described how the fusion TFs were expressed, and what evidence there is that the fusions behave like the unfused wild type. The authors “tested the functionality of c-Myc-Dendra2 by performing RT-qPCR on a set of active genes in our U2OS cell line”. Was the fusion expressed in the null background? From the endogenous promoter? Does the fusion protein rescue the null? And as for the other fusion, CycT1-Dendra2, we are pointed to a work “in preparation” and are thus unable to judge for ourselves the evidence for its functionality.

3) The presentation of experimental data is also less than optimal. Examples: (a) Sample sizes (# trajectories, # cells, etc.) need to be stated for each plot, but they are not. (b) The evidence for sub-diffusion (Figure 3D) is not convincing. The anomalous behavior of MSD should be demonstrated for individual trajectories, not for an ensemble average. (c) The evidence for time-evolution of angle preference (Figure 4B) is also unconvincing. A single parameter should be extracted from the plot at each time point, and the change of this parameter value over time should be examined to reveal whether the angle preference changes over time or not. This would allow direct comparison to theory (Figure 5).

Reviewer #2:

This manuscript presents an elegant work of imaging single molecules of transcription factors in the nucleus of living cells by single particle tracking photoactivation localization microscopy (sptPALM). They have performed elegant microscopy and data analysis to collect large data sets of individual proteins diffusing within the nuclear volume. High quality single molecule trajectories were acquired and reconstructed for as long as 60 consecutive translocations. Their work provides an experimental framework to study nuclear proteins with mobility ranging from chromatin-bound H2B molecules to diffusing Dendra2 molecules as a general method for studying nuclear dynamics at the single molecule level.

This manuscript has raised several interesting points on transcription imaging in living cells. The authors describe the concept of compact and non-compact exploration of transcription factors. The compact exploration modes suggest that strong binding is not required to ensure high occupancy and that compact exploration factors may be preferentially shared between proximal loci. They also suggest that spatial cooperation can be a mechanism that adds a level of control of rapid assembly of molecular complexes, reconciling weak and transient interactions with functional stability.

Specific points:

1) The actual data presenting the described results (diffusion coefficients, etc) cannot be found.

2) It is interesting that free Dendra2 and c-myc have several populations of very distinct diffusion coefficients. Stokes-Einstein equation states that distinct diffusing populations usually arise from distinct hydrodynamic radii of the molecule or distinct local viscosity. Is Dendra2 strictly monomeric in cells? If so, then the distinct local viscosity in the nucleus seems to be the cause of distinct diffusing populations.

3) Could the DNA-binding or protein-binding properties of c-myc contribute to their distinct diffusing populations (or the relative proportions of each population)? Can a c-myc mutant defective in DNA binding be examined to test these possibilities? C-myc forms heterodimer with Max through its leucine zipper domain. Can a c-myc mutant defective in Max binding be examined?

4) The authors observed that P-TEFb, but not c-myc or free Dendra2 has anomalous diffusive behavior. FRAP or FCS can rarely differentiate multiple diffusing populations versus anomalous subdiffusion. This is one of very few reports that successfully identified anomalous diffusive behavior using single molecule imaging. How is the anomalous diffusion related to other kinetic properties observed for P-TEFb, such as abrupt transitions and biased angular distribution between consecutive steps?

5) “the time needed to find a 10nm target at a distance of 250nm is 68 times longer for c-Myc compared to P-TEFb”. Does the search time also depend on the nuclear concentration of transcription factors?

Reviewer #3:

The manuscript by Izeddin, Recamier, et al. presents a thorough study of intra-nuclear protein diffusion and concludes that two studied proteins, c-Myc and P-TEFb, exhibit different types of diffusion with c-Myc showing normal and P-TEFb anomalous diffusion. The study is timely, important to the biophysics community and beyond, and presents exciting new data that are carefully analyzed. To my knowledge, this is one the first, if not the first, study to track intra-nuclear motion of proteins at such high space and time resolution.

However, I contest author's interpretation of their data and mostly their conclusion that P-TEFb exhibits an anomalous diffusion. Below I suggest several approaches how this mechanism can be tested by simulations and data analysis.

My specific points are as follows:

Let me start by proposing an alternative model to explain P-TEFb data: labeled Cyclin-T (in complex with CDK or without) is diffusing freely while intermittently binding its partners/targets and other nuclear structures such as Pol II clusters and nuclear speckles. While bound to the targets, P-TEFb continues diffusing either with them, but much slower due to their size, or on the surface/volume of immobile targets (e.g. hopping between CTD domains of Pol II). Thus P-TEFb alternates between rounds of fast free (normal) diffusion and periods of slow and possibly confined diffusion. My hypothesis is that such motion can leads to MSD vs t and angular distributions of steps that appearas anomalous diffusion, even when the dwell time is exponentially distributed (not power-law-CTRW). Moreover, heavy-tailed dwell times can lead to real subdiffusion (CTRW type) with inhomogeneous angular distributions due to trapping.

Distinction between intermittent binding and anomalous diffusion is more than semantic. Intermittent binding can slow-down diffusion, lead to confined motion of the bound protein, but does not lead to phenomena specific to anomalous diffusion such as local exploration and distance-dependent search time. Since some conclusion of the paper rely on the statement of anomalous diffusion, it should be critically evaluated against seemingly more plausible intermittent binding.

Intermittent binding, indeed, requires fewer assumptions that anomalous diffusion. Most of homogeneous or inhomogeneous distributions of immobile or slowly moving partners/targets can lead to intermittent binding. Anomalous diffusion, in contrast, requires presence of some self-similar fractal structure present on allsales, an assumption that, in my opinion, is hard to justify.

It is likely that c-Myc and P-TEFb show different characteristics of diffusion due to different size, spatial distribution and dwell time on their targets/traps. Below I argue that presented data on P-TEFb may very well agree with the intermittent binding and not with anomalous diffusion.

1) Authors note that “individual trajectories of P-TEFb molecules often showed abrupt transitions from slow to fast displacement modes within the same trajectory”, which is consistent with the intermittent binding mechanism. Moreover, they note that “P-TEFb, the typical translocation length and the translocation histograms were comparable to those obtained for c-Myc” again consistent with intermittent binding. My guess is that subdiffusion on a fractal (i.e in the presence of a fractal-distributed traps) leads to power-law distributed displacements. Authors can test this for their simulations of anomalous diffusion on a percolation cluster.

My suggestion is to develop simulations where a diffusing molecule moves freely and gets trapped into finite size traps (containers, e.g. speckles or Pol II clusters) inside which a molecule can also move and then escape after some dwell time.

2) Fit of t^a of the MSD vs t is not very convincing. (a) MSD/t curves for c-Myc or Dentra are not flat either. For c-Myc and t>0.03s MSD/t vs t points easily fall onto a straight line. This reflecta either some real biophysical effect that affect both c-Myc and P-TEFb or some issues with longer trajectories and/or trajectory selection biases. Either way, the only difference between c-Myc and P-TEFb curves are in the first three points. (b) Most importantly, intermittent binding may very well create such “anomalous-looking” MSD/t vs t plots. To test this, authors can use simulations of the intermittent binding I suggested above, simulate the same length and number of trajectories as in the experiment and test whether they indeed can produce such results. Sweeping parameters of the intermittent simulations to fit the data may be necessary. Such parameters include the mean size of a trap, the number of traps (assuming a homogeneous distribution), and the mean dwell time (assuming exp distribution).

Another way to test for anomalous diffusion vs intermittent binding would be to segment trajectory into fast and slow parts and analyze them separately, perhaps by collapsing slow parts into points. Some steps toward this have been done by removing immobile steps (Figure 4–figure supplement 1), but a more systematic segmentation can be done (e.g. by applying HHM to the time series of step sizes). My guess is that true anomalous diffusion should manifest itself in power-law distributed step sizes and the same MSD∼t scaling for all time scales. Intermittent binding, on the contrary is expected to show normal diffusion for fast phases and confined diffusion (MSD going into a plateau for larger t) for slow phases.

3) The angular distribution of consecutive steps observed for P-TEFb is not a very strong argument in support of anomalous diffusion. In fact, enrichment of trajectory reversals (90-180deg) can be observed for trapped particles. This is evident in the angle distribution of H2B, which is a mixture of trapped and freely moving proteins. As such, observed angular distribution for P-TEFb may very well reflect its trapping/confinement during which the protein either fluctuates at one place or moves within a small volume, thus making sharp reversals. Simulations and analysis of trajectories that I suggested above can help to answer test this possibility.

Angular distributions for steps separated by delta_t don't seem to support anomalous diffusion of P-TEFb either. Comparison on these distributions for experiments (Figure 3B) and simulated anomalous diffusion (Figure 4C) shows that H2B is in best agreement with simulated anomalous diffusion. This argument only reinforces my concern that these plots cannot distinguish anomalous diffusion and a mixture of immobilized and freely-diffusing trajectories.

Moreover, when immobile steps are removed (Figure 4–figure supplement 1), angular distributions for P-TEFb and c-Myc looks very much alike, with both proteins showing enrichment of reversals for delta_t > 40ms. Speaking of c-Myc, authors rightfully note that this may reflect “confinement to domains significantly smaller than the nucleus”. The same argument can be equally applied to P-TEFb. These distributions for c-Myc and P-TEFb differ for ∼10-20ms range, possibly reflecting differences in sizes of traps and dwell times. By sweeping parameters for simulations that I proposed above one can find size/dwell times consistent with the data for each protein.

4) In Discussion, authors mention some important experimental results that they plan to publish elsewhere. They mention that impediment of interactions between P-TEFb and Pol II leads to a change in P-TEFb diffusion from anomalous to normal. In my opinion, this is very important result and the paper would be much stronger if it were presented here. Authors further suggest that a matrix of Pol II-CTD repeats can lead to anomalous diffusion. This is a conceptually important point: a mesh of traps can lead to slow diffusion, diffusion with intermittent binding, but anomalous diffusion would further require such mesh of Pol II-CTDs to form a perfect fractal. Note that anomalous diffusion can be observed on the percolation cluster only right at the percolation threshold. Near-fractal clusters below or above the percolation point do not lead to anomalous diffusion. It is hard to imagine Pol II forming such perfect structures. Excellent recent data on Pol II localization (from the same group) would hardly support this notion.

5) As far as simulations are concerned, simulations used to test possible modes of diffusion are important and insightful. I wasn't however that much impressed by simulations of the search process by normal and anomalous diffusion (Figure 5). Very similar results for search by local vs non-local explorers can be found in other papers. I also found surprising the set-up of the simulations: one molecule looking for a single target in the nucleus. Given the number of molecules per nucleus the search can almost instantaneous.

Here is my argument. The number of molecules of c-Myc per cell is ∼10^5 (bionumbers.org), which exceeds ∼10^4 c-Myc targets. The number of active Pol II, i.e. those that have P-TEFb bound, can also be estimated as ∼10^5-10^6 per cell. Thus in 500um^3 of the nuclear volume the spacing between c-Myc molecules and the spacing between P-TEFb is of the order of ∼100nm, i.e. any target has a protein within 100nm. As evident from MSD data, the area of (100nm)^2 is swept by either protein in less than 10ms, suggesting that the search time should be of the order of ∼10ms, irrespective of the mode of diffusion.

To summarize, my recommendation to the authors is to revaluate their conclusions concerning anomalous diffusion and, at least, to consider intermittent binding as an alternative mechanism. Suggested analysis and simulation may allow to estimate sizes of targets and dwell times for c-Myc and P-TEFb. I believe this analysis can only strengthen this solid and important paper.

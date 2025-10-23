# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.46564.031](https://doi.org/10.7554/eLife.46564.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Self-organised segregation of bacterial chromosomal origins" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the manuscript "Self-organised segregation of bacterial chromosomal origins", the authors investigate the segregation of the chromosomal origins in Escherichia coli bacteria. They build on previously published work (Murray and Sourjik, 2017) about the dynamic and self-organized clustering of MukBEF proteins on the chromosome. To study the dynamics of the chromosomal origins they incorporate interactions between MukBEF and the origins into the model, as suggested by experimental findings. Their main result is that preferential loading of MukBEF at the origins and entropic repulsion of the origins can explain the experimentally observed ori dynamics. The presented work is an important contribution to quantitative cell biology because it gives new mechanistic insights into origin positioning in E. coli by integration of computational methods with experimental data.

The reviewers were supportive of the approach and the results, but have raised a number of issues that need to be addressed in a revised manuscript in order for the paper to be acceptable for publication in eLife. In particular, additional modeling work is requested, along with detailed, falsifiable predictions, and a discussion of the limitations of the current model.

Essential revisions:

1) Limitations of 1D modeling.

The authors' modeling is limited to 1D. While I appreciate the technical challenges, 3D modeling is a conceptual necessity. The population average aspect ratio of E. coli is typically length/width = 4, and treating an E. coli cell as a 1D space is really misleading for chromosome organization and segregation. Such an 1D approach was acceptable for Min oscillations some 20 years ago when physicists modeled them as a 1D reaction-diffusion problem; not only such approaches were new then, but also the nature of dynamics of Min allowed dimensional reduction as the Min proteins bind and unbind to the inner cell-wall membrane, which was key to Min oscillations. However, that is not the case for MukBEF. See also below the points on the polymeric nature of the chromosome.

2) 3D effects and robustness.

E. coli cells with mild inhibition of mreB expression become almost completely round, but they still grow at the same growth rate as wildtype showing multifork replication (e.g., PMID: 28416114). We are unsure how ori positioning (if at all) by MukBEF pattern formation is important for chromosome segregation in round cells. Please explain and make predictions.

3) Polymeric nature of the chromosome.

Another aspect of the chromosome the authors almost completely neglect is the polymeric nature of the problem. Ori, after all, is an extremely small fraction of the chromosome. How does the ori positioning explain the principal organization of the rest of the chromosome? The authors did add limited 3D polymeric simulations, but they are far from being sufficient to justify the main claim of the paper.

4) Ori dynamics during (non-overlapping) replication.

In the last part of the manuscript, the authors do consider the polymeric nature of the chromosome and model the gradient of MukBEF implicitly by dynamic looping model with only one ori. They show that the ori can have a directed motion towards the cell center where the looping probability is more, but it is not clear how the oris reach the quarter positions during replication using the dynamic looping model. How does the dynamic looping model explain the position of MukBEF at quarter positions?

5) Ori dynamics during multifork replication.

We cannot assess the robustness of preferential loading of MukBEF on ori segregation and positioning during multifork replications (when 2 or 3 replication cycles overlap with up to 8 oris). This must be one of the most straightforward predictions the authors should be able to make based on their model, and they should extend their work to multifork replication cases. To be clear, we are not asking for more experiments, just falsifiable predictions using their model for future experimental tests.

6) Predictions.

In our view, modeling would be far more informative when it makes falsifiable predictions, rather than when the ad-hoc assumptions can produce results that look like published data. We ask the authors make two predictions, and include them in their revised manuscript.

Prediction 1: what will happen to low-copy number plasmids without partitioning system, when they instead integrated the E. coli chromosome ori? We presume the authors would predict these plasmids would completely localize with MukBEF clusters given that entropic repulsion would be negligible. If validated, this prediction would significantly support both the authors MukBEF model as well as the role of entropic repulsion.

Prediction 2: what would happen to the ectopic ori in the chromosome, depending on its locus position in the chromosome? And what would happen to the ectopic ori during multifork replication? Such strains were constructed previously and tested in limited growth conditions (PMID:21670292), and it would be worthwhile to extend the authors work by making explicit predictions assuming various different locations of the ectopic ori under different growth conditions.

See also other suggested predictions above.

7) The model is based on the known flux-balance mechanism and extended to explain the movement of the chromosomal origins. With each experimental observation (separation of two oris, ori dynamics during growth) they add a new aspect to the model (preferential loading, repulsive interaction of oris), which then leads to good agreement of the simulation results with the data. This raises two important questions: a) Are there new insights the model provides beyond the data? b) Are the model assumptions justified? In particular, is a preferential loading ratio of six, which shows the smallest variance of the peaks, realistic? The authors refer to a measured preferential loading for SMC in B. subtilis. What is the preferential loading ratio here? Is it possible to get a measurement for MukBEF in E. coli? Furthermore, is the chosen repulsive interaction strength / range realistic? It might be that, although repulsion contributes to the dynamics of the origins in the in vivo system, it is not the main factor because it might not be strong enough. The values for the repulsive strength and range are obtained by fitting (Figure 4——figure supplement 2). Isn't it trivial that with this fitted choice of parameters the experimental observations are reproduced?

8) In the model, diffusion of the origins is biased by a gradient of MukBEF. This is an important assumption of the model, which raises several questions: What is the physics behind this assumption, i.e. where does the net force come from? What determines the strength of the bias? Can the strength be measured? Another assumption of the model is that only the concentration of the slow species (in blue in Figure 2A) is considered for the bias of the origins. Why are not both, the slow and the fast moving, nucleoid-bound species (in green in Figure 2A) considered for the bias? Couldn't the success of the model in explaining the data hinge to a large degree on all these assumptions?

9) The authors justify their assumption of a one-dimensional model with the fact that most of the foci are within 40% of cell width and "There are also technical reason inherent to the method that make nonlinear models in higher dimensions (and the corresponding lower voxel volumes) problematic." However, 40% of cell width is not a very confined region. Furthermore, could the authors state more clearly, which technical reasons they refer to? If it is the lower bound on the mesh size, there are generalized RDMEs that overcome this limit (Hellander and Petzold, 2016).

10) Most of the parameters for the MukBEF dynamics are chosen as previously described (Murray and Sourjik, 2017). This reference should be cited when the parameters are discussed (subsection “Parameters”). The only parameter that is chosen differently is the concentration of MukBEF, which is set to a larger value than the one used before. Why is this choice justified? Couldn't the concentration be measured experimentally? Since the strength of stochastic effects depends on the number of particles, it is crucial to choose realistic concentrations / number of particles as well as realistic rates in the model.

11) The authors did a number of experiments with E. coli cells, in which they imaged the ori location(s) and/or Muk-foci. Together with what is already known in the literature, these experiments constitute the empirical basis for the analysis of the authors. However, instead of presenting this empirical basis in a coherent fashion in the beginning of the Results section, the authors chose to present the results piecemeal. In particular, the results that we found most striking, the "restoring velocities" of Figure 5B and D, are shown very late in the paper and presented only as a confirmation of their hypothesis of preferential Muk-loading onto the ori locus. In our view, this data should be the motivation for the hypothesis – prior to seeing this data we kept wondering what the basis for the hypothesis was.

Then, after finally seeing the "restoring velocities" of Figure 5B and D, we thought that the most logical next step would be to repeat this analysis on different variants of the MukBEF-system, in order to test whether the higher restoring velocity towards MukB than to midcell is lost when the system is modified in one or the other way.

Instead, the authors continued by presenting computer simulations of chromosome dynamics within a dynamic loop model. The presentation was so brief and the analysis of the simulations so minimal that the conclusions from this part of the work remained obscure to us. We think these simulations were meant to explore whether the directed motion of ori (within their model) is due to a real mechanical force on ori (and, if so, where this force comes from), or whether it results from a ratchet-like mechanism. However, what is the conclusion on this question and how do the authors arrive at the conclusion? We think this part of the work should either be eliminated or should be elaborated on and presented much more clearly.

12) The logic underlying the simulations of the stochastic model of Figure 2C was much clearer. However, given that this model relies heavily on the prior work of Murray and Sourjik, 2017, it would be good to spell out more clearly what has already been established in that paper and what is added here. Furthermore, the way in which the comparison of these simulations with the experimental data is done is sometimes confusing, in the sense that we did not get a clear sense about "what is put in and what they got out". For instance, it says "… Note this was based on a direct comparison and not a fit to the experimental distribution.", while earlier, it says "… We found that by adjusting the diffusion and drift input parameters, we were able to obtain excellent agreement with the experimental results (Figure 2F)." (the latter indicates fitting)

In conclusion, we recommend that the authors rewrite their manuscript to present the data and the logic in a more coherent and stringent way. For instance, we think it is in the best interest of the authors to clearly point out what results of this paper remain true in case future studies should show that there is no preferential loading of Muk onto ori. Our impression is that the data of Figure 5B and D is an important part of what would survive in that case. It would be helpful, if the authors clearly spell out what can be concluded from this data independent of a specific modeling scenario. It would be even better to also add data that tests the restoring velocities of variants of the Muk system.

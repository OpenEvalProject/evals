# Peer review - Round 1

Editors:
- Yibing Shan, DE Shaw Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60434.sa1](https://doi.org/10.7554/eLife.60434.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using a Go ̄-like theoretical model Chu et al. explored the trade-off between strong intra- and inter-domain interactions of DPO4, a Y-family DNA polymerase, and showed that the system reflects a balance between expedient folding of individual domains and a stable inter-domain arrangement that also allows conformational flexibility required for the polymerase's DNA binding. The work represents an early theoretic analysis of folding of multi-domain proteins and their substrate binding.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "From "divide-and-conquer" to "speed-stability": A trade-off between folding and function in a multi-domain protein" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. While recognizing the merits and sophistication of this work as, some of the reviewers are concerned that it is, as is presented in the manuscript, difficult for the more biologically oriented readership both in terms of style and in terms of substance. These reviewers also feel that publishing this work in a more biophysics-centric journal may do it more justice than eLife. At the same time, we would be willing to reconsider our decision if the manuscript is substantially revised to motivate the discussions by more biologically relevant questions, to make it more readable for eLife readership, and to give a better description of the underlying models and the simulations.

Reviewer #1:

This work used a Go model combined with enhances sampling simulations to investigate the folding of DPO4, a multi-domain protein that binds DNA. The results suggest that the relative strength of the inter- and intra-domain interactions determines the folding process, stability of the protein, and its DNA binding kinetics and affinity.

One important weakness of this manuscript, which makes this reviewer's assessment difficult, is its readability. From the main text, it is not very clear to a general reader, even one knowledgeable to protein modelling, what is the underlying physical model and what were the specific simulations. Moreover, the conclusions are presented in a somewhat convoluted way, alien to biologist. At a high level many of the conclusions are intuitive, and perhaps even obvious, e.g. strong inter-domain interactions hinder folding at domain level and leads to occasional unfolding of the domains, thus the backtracking. Overall, I am concerned whether this paper is suitable for eLife.

Reviewer #2:

In this manuscript, the authors use structure-based models to simulate multi-domain protein folding, in order to explore the relationship between inter- and intra-domain interactions during protein folding. Folding of multi-domain proteins is extremely challenging, and has only been seriously studied with simulations in the last few years, which makes the study timely. However, there are some serious issues with the manuscript that need to be addressed before the manuscript could be suitable for publication.

1) The use of English is rather poor. As a result, there are many passages that I cannot understand, making it difficult/impossible to assess the scientific quality of the full study. It may be necessary to consult with a professional scientific writer. Also, there are many statements for which the precision of the phrasing should be improved, such as claims of "perfect" or "proof".

2) As a motivation for the study, the manuscript states that "Until now, the mechanisms and functions of domain interactions on multi-domain protein folding have not been reported yet." However, this is not a fair statement. Specifically, the recent study of Rao and Gosavi, 2018, investigated multi-domain folding with a very similar model.

3) The authors use a re-weighting scheme to study the influence of changes in contact strengths. If this is simply free-energy perturbation, then a single equation could be given, along with a few sentence description. Since all results are derived from free-energy calculations based on re-weighting, there should be a clear description of the method, precisely as employed, in order to fully interpret the results.

4) There are many claims of backtracking, but the figures are not convincing. Specifically, Figure 2C shows that the average number of formed contacts is non-monotonic. However, this could simply arise from there being parallel pathways for folding, and the apparent backtracking could be an artifact of the projection onto Q. Since the simulations are based on REMD simulations, it is not obvious how one could distinguish between pathways, since full folding events are not observed. Demonstrating backtracking requires some form of pathway identification.

5) The Results state "In practice, for all different p, we set the free energy of the state that has the minimally formed total native contacts (Q(Total~ 0:08) to be 0." It is not clear why it is necessary to make this assumption. Couldn't the non-monotonic stability of the native ensemble be an artifact, if this assumption were not valid? As the contact strengths change, if the chosen point were to become less stable, it would shift the entire curve in Figure 1B. If the effect were sufficiently large, then perhaps the native ensemble would not exhibit the U-shape stability.

Reviewer #3:

This manuscript describes molecular dynamics simulations with the so-called Gō-like models that aim to investigate the folding and binding mechanism of a multi-domain protein modulated by inter-domain interactions. Specifically, the study focuses on determining the protein folding and DNA-binding processes of a DNA polymerase IV (DPO4). They observed an optimal DPO4 folding kinetics could be reached as inter-domain interactions were modestly weakened and showed the interesting competition between the fast, stable folding and efficient DNA-binding. This is an excellent study that is well-constructed, precisely executed and nicely presented.

Technically, they built a single-basin Gō model for DPO4 folding and double-basin Gō model for DPO4 binding with a frozen short DNA fragment. They used the classical enhanced sampling techniques, including parallel temperature replica exchanged MD and umbrella sampling, to accelerate the sampling and obtain the free energy profiles for folding and binding process, separately. They played with different strengths of inter-domain interactions 𝜖𝐼𝑛𝑡er so as to modulate the ratio 𝜌 of 𝜖𝐼𝑛𝑡𝑟𝑎 to 𝜖𝐼𝑛𝑡𝑟𝑎 (the strengths of intra-domain interactions) to investigate the effects of the balance between inter-domain interactions and intra-domain interactions. To avoid extensive sampling of the free energy landscapes in different models, they employed a reweighting method to estimate the folding thermodynamics at a wide range of 𝜌 by only performing REMD simulation with the standard model (at 𝜌0=1.0). I appreciated the thoroughness and the technical sophistication to solidify the strength of the results. I have some questions and a few minor suggestions that they could consider to further strengthen the work.

1) About the modeling.

Given that they aimed to explore the trade-off between folding and function for the same protein, it seems reasonable to investigate both the folding and binding process under the same energy landscape framework. Any reasons for not using a uniform double-basin Gō model for DPO4 in both folding and binding simulations?

They introduced the Debye-Hückel potential to describe the electrostatic interactions between DPO4 and DNA. It is not clear to me that if they also introduced DH potential to describe the intra-DPO4 interactions at the same time. If not, I am a bit concerned this might occur: a few positively charged residues in DPO4 bind at the same time with one negatively charged DNA bead just because these residues in DPO4 cannot feel the charges of others. Please make sure this situation didn't occur in the simulations.

And they also used specific native contacts to model the DPO4-DNA attractive interactions. So, in this binding model they used a hybrid specific LJ potential and a non-specific DH potential to model the DPO4-DNA binding process. This is of course not how real physics works in nature. Would some of the observations in this work be dependent on the choice?

There are at least four free parameters on the interaction strengths in the DPO4-DNA binding models (Materials and methods). It is not clear how the strength of the DH term was determined. And would the change of 𝜖𝐼𝑛𝑡er break the balance with other interactions? And could this impact the conclusions? Please comment on this.

2) About the simulation temperatures.

They performed kinetic simulations of DPO4 folding at the pesudo room temperature 𝑇𝑟sim which was identified by rescaling with the ratio of simulated Tf to experimental Tf. Changing the Hamiltonian parameters could change the thermodynamic properties, as they already recognized that "𝑇𝑓 also changes with 𝜌". So 𝑇𝑟sim may also change with different 𝜌. It seems the kinetic simulations were performed at the corresponding 𝑇𝑟sim recalibrated by the temperature shift caused by 𝜌 change. But it is not clear if they did the same in the DPO4-DNA binding kinetic simulations. Please clarify it.

In addition, they compared the DPO4-DNA binding affinities at different 𝜌 with experimental Kd which. But again, the simulated Tf and Tr may shift due to the change of 𝜌. So, does it make sense to compare the 𝜌 or T-dependent affinities with the experimental Kd which was measured at a fixed temperature?

3) They stated that "Since direct simulations on the transition between the IS and BS are computationally impractical due to the high barrier between these two states, we instead tried to infer the kinetic rates from the barrier heights for different 𝜌." But they actually didn't show the inferred kinetic rates in this manuscript, but instead just show the barrier heights in Figure 4E. I understand that they used the barrier height as a proxy of the transition rate based on the Arrhenius equation with a uniform pre-exponential factor. To release the dependence on this assumption and further strengthen the work, they could consider using other enhanced sampling methods with relatively low computational cost, such as frequency-adaptive metadynamics (Wang et al., 2018) and weighted ensemble simulation (Annu Rev Biophys. 2017;46:43-57) etc., to obtain the transition rates.

4) They stated that "We found a monotonic increase of barrier height for both two transitions between the IS and BS as 𝜌 increases (Figure 4E)." Without error estimations, it is hard to judge if the trend for BS→IS barrier increase with 𝜌 is significant or just within the errors. I would strongly suggest they do error estimations and include error bars in the free energy profiles.

5) There is one experimental author involved in this manuscript, so I read this work as an experimental/simulation collaboration, in which the simulations provide valuable predictions for experimental tests and validations. Besides the comparison with experimental Kd, it will strengthen the work by more comparisons. I understand that it is always non-trivial to combine and compare experiments and simulations, but I will appreciate if they could discuss and suggest the possibilities that could be tested by further experiments.

6) Could the conclusions in this manuscript be extended for other multi-domain proteins? Or how general are the conclusions?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Investigating the trade-off between folding and function in a multidomain Y-family DNA polymerase" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Cynthia Wolberger as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Using a Go ̄-like theoretical model Chu et al. explored the trade-off between strong intra- and inter-domain interactions of DPO4, a Y-family DNA polymerase, and showed that the system reflects a balance between expedient folding of individual domains and a stable inter-domain arrangement that also allows conformational flexibility required for the polymerase's DNA binding. The work represents an early theoretic analysis of folding of multi-domain proteins and their substrate binding.

Revisions:

In comparison to the original submission, the reviewers agree that manuscript has been substantially improved in terms of both presentation and substance. The reviewers suggested several relatively minor revisions:

Results paragraph four indicates that the ratio of inter and intra-domain contacts was varied. How this was implemented was not clear from the text. For example, one could vary one weight, or the other, or one could modulate both, while keeping some other quantity (e.g. total stabilizing energy) constant. Without this clearly defined, it is difficult fully appreciate the potential significance of any trends based on this ratio.

The authors should expand the discussion on the potential experimental consequence of their conclusions. For example, what signature might single molecule force spectroscopy observe as an implication. What other experiments can be conducted in this regard.

The manuscript repeatedly describes effects, relative to the "default" parameterization of a structure-based model. It is not clear what significance the default parameters may have. That is, are the default parameters considered to be an accurate approximation to systems in the cell? If so, how, and to what extent? Perhaps the initial parameterization is far from appropriate for the current application, in which case variations in the ratio of different interactions may correspond to a regime that is not biologically relevant. It is important that the authors present these trends in terms of the physical insights into a biological process.

The authors may further revise their figures and make them even more intuitive. For example, rho could be labelled as relative strength of inter vs. interactions on the figure, so could MTCI. The labelling of Figure 2G is not very clear, and similar issues exist for some other figure panels.

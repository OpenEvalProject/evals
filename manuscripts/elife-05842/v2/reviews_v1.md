# Peer review - Round 1

Editors:
- Janet Rossant, University of Toronto, Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05842.020](https://doi.org/10.7554/eLife.05842.020)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “A balance of positive and negative regulators determines the pace of the segmentation clock” for consideration at eLife. Your article has been evaluated by Janet Rossant (Senior Editor) and three reviewers.

The reviewers all agreed that there was considerable merit in your study and that the concept of a positive regulator of the somite clock was an interesting one. However, there was one major concern. The experimental work demonstrates nicely a correlation between NICD levels and stability and period length. Nonetheless, all reviewers were concerned that you had not really proven a causal relationship between elevated NICD half-life and extension of the oscillation period.

There was a quite extensive discussion on this issue, and the reviewers were not sure exactly how you could prove your hypothesis. Some ideas were introducing a low level of RNAi to Notch1 to reduce Notch levels or treating with a gamma-secretase inhibitor to reduce NICD production or to increase FBXW7 levels. Alternately, another hypothesis discussed was to show that the clock period can be returned to normal by making NICD less stable (despite treating with a CDK or Tankyrase inhibitor). Other possibilities raised were locally raising NICD levels or changing half-life by removing the PEST domain. We realize that these are not necessarily the right experiments, and therefore would like to give you the option to respond to this criticism. Please take into account the major concerns raised by reviewers 1 and 2, appended below.

Reviewer 1:

1) The percentage of embryos where cLfng expression is delayed after (for example) Wnt inhibition is almost certainly statistically significant, but in the absence of data from control embryos (both halves cultured in DMSO) and some statistical comparison, this cannot be confirmed. The authors should already have this data.

2) For figures looking at NICD levels and half-life following drug treatment, it is not entirely clear to me that treatment with cycloheximide alone will prevent production of new NICD in explants. Given the delays inherent in Notch and DLL1 trafficking, cell surface presentation, and interactions, it seems possible that new NICD could be produced even in the presence of CHX, based on signaling through receptors that were made prior to initiation of CHX treatment. Thus, if any of the inhibitors increased the production of DLL1 or NOTCH1, for example, then the increases in NICD observed might be secondary to increased signaling, rather than a result of changes in protein turnover. Control experiments where inhibition of Notch signaling was initiated at the time of CHX treatment could address this concern, and provide additional support to the thesis that the effects the authors observe are due to changes in NICD half-life.

3) The use of p values in Figure 4 legend indicates that multiple pools were assessed and the Western Blot bands were quantified. The details of this process, as well as the averages and standard deviations of the values and the statistical analysis used should be described. Further, I don't find the phosphoserine 5 controls showing activity of CDK inhibitors in Figure 2–figure supplement 1B extremely convincing. Details of quantification of Western Blots might help here as well. The authors should have this data.

4) From the images provided in Figure 5, it is not clear how “normal” the longer somites formed in the presence of various inhibitors actually are. Given that changes in clock synchrony also can affect somite size and morphology, the reader needs to have a clear idea of how (if) somite production might be perturbed by these treatments. Images that focus more closely on the region of interest to let the reader interpret morphology, and perhaps in situ analysis with markers that would delineate somite compartments would lend support to the authors’ conclusions.

5) Data showing that MLN4924 increases phospho-β catenin are shown in Figure 6, but as far as I could tell, are not discussed? Since the authors claim that Wnt inhibition can on its own increase NICD levels and half-lives, this data should be at least acknowledged and put in some kind of context.

Reviewer 2:

1) The experimental work nicely shows a correlation between NICD levels and stability and period length. It is however not clear if there is a causal relationship between elevated NICD half-life and extension of the oscillation period. The last set of experiments presented (subsection “Inhibition of SCF (SKP1- CUL1-F-box protein) E3 ubiquitin ligase complexes results in delayed clock oscillations and higher levels of NICD”), aiming at inhibiting the SCF E3 ubiquitin ligase complex is extremely important to address this issue. However, it should be extended to show that the inhibitor does not work through inhibition of the Wnt pathway, as is the case of the previous inhibitors. Otherwise the order of events remains unclear. Related to this, the last panel of Figure 6D, which is not described in the Results section (and should be), suggests that levels of phosphorylated β catenin are elevated following MLN4924 treatment. This should be explained.

2) In many ways, Figure 1 is essential to this manuscript. We feel it could be enhanced to facilitate the reading of the manuscript and understanding of the model and predictions. Figure 1A and B are not visually explicit enough to understand: a) the relationship between the clock protein, NICD, the feedback loops and the output on the oscillation period; b) how this model differs from the previous ones (Figure A could be replaced by the previous models); c) what the assumptions underlying this new model are. In addition, and maybe in the Experimental Procedures section, a statement explaining how the model can fit both the chicken and mouse somitogenesis, which oscillations for instance have a different period, would be useful.

3) Figure 1C-H should be explained in a bit more detail, since this is the basis for understanding the rationale behind the experiments. The period on the top of the plots C-E correspond to what? In D and E how much are the half-lives of NICD and Hes7 increased? Maybe it should be stated clearly what the used values are and that the loss of oscillations in Figure 1D corresponds to red region in Figure 1F near the solid line that is the limit of oscillations.

4) The competition relationship between NICD and the inhibitory clock protein to activate and repress transcription of a clock gene respectively (what parameter/properties considered?) impinges on the predictions of the model and interpretation of Figure 1D, which postulates that elevated NICD half-life results in more clock protein, and should be better spelled out. In addition, depending on the ability of the clock protein to be a potent transcription inhibitor, having NICD longer around but not much more NICD protein may not have much of an impact. It would be useful to explicit which parameter(s) in the mathematical model reflect this aspect.

5) The description of the approach to measure the half-life is a bit confusing and hard to follow with regard to the equations. Ai(t) is the amount of NICD in both pools A and B. “t” is a free parameter. We suggest for the second equation in the subsection “Measuring the half-life of endogeneous NICD”: B_bar(τ)=A_bar(t+τ)=sum… and F(τ)=A_bar(t+τ)/A_bar(τ). This is more coherent with the integral form of F(τ) in the fourth equation.

Maybe it would be useful to have a profile sketch for A as a function of t. If we understand correctly, as long as τ<ts, A is equal to a constant value A0, then as we reach to ts, A(t) decays exponentially. Using this sketch, it will be easier to understand that for τ<=ts, A(t) = A(t+τ), else A(t+τ)=A(t)e–βτ). We also suggest that the first sentence of the second paragraph changes to “Letting Ai(t) be the amount of NICD in the ith tissue sample at time (t). We define the experimentally measurable sum in pool A as…”

6) What is T in the integral form of F(τ) in the subsection “Measuring the half-life of endogeneous NICD”, the clock period?

7) Figure 6A: It should be mentioned that the vertical axis is log F(τ), the units of the horizontal axis is minutes. The label seems to be “τ” and not “t”. It would be useful to add at the end of the legend (A) that the inverse of the slope gives the half-life (data presented in Figure 6B). I don't understand where does the 0.5C0=C0e-slope t relationship come from. In the main text, Log F(τ)=–β(Τ–ts). From the slopes of Figure 6A we get the values in Figure 6(B) and from the intercept we should be able to get ts (which seems to be of the order of 10 minutes). Can the authors comment on this (and why this has not been used to calculate ts?).

8) Figure 4D and Figure 6 seem to point to different values for NICD half-life. The 2nd lane in Figure 4D indicates that all NICD proteins are cleared in 3 hours; the 4th lane indicates that significant residual NICD remains 1h after its production has been blocked. Could the authors explicit how these experimental results fit with the calculated half-life indicated in the subsection “Exposure to XAV939, and the CDK inhibitors increases the half-life of cNICD in the PSM”?

In addition, it would be very informative to visualize (in embryos) if the NICD half-life is homogenously increased in the somites and presomitic mesoderm, as its impact on the oscillation period is expected in a very defined spatial window.

9) Impact of SHH inhibition on the oscillation. It is a bit unsettling to only find in the Discussion a reference to the 2010 PNAS paper claiming the opposite results, and not upfront in the Results section. In addition, one would have liked to read possible reasons for the discrepancy.

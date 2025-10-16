# Peer review - Round 1

Editors:
- Sarah A Teichmann, EMBL-European Bioinformatics Institute & Wellcome Trust Sanger Institute , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09652.020](https://doi.org/10.7554/eLife.09652.020)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Paracrine Communication Maximizes Cellular Response Fidelity in Wound Signaling" for peer review at eLife. Your submission has been favorably evaluated by Naama Barkai (Senior Editor), a Reviewing Editor, and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this report, Handly et al. analyzed the impact of paracrine communication on the cellular response fidelity in an epithelial cell line during wound healing. Through single cell live imaging they quantified signal and noise of Ca2+ and ERK responses following treatment with ATPs (which recapitulates an event happening in wound context). They first validated the system (paracrine activation of ERK by ATP) and then they analyzed the effect of differential spatial density of cell clusters on the responses. They identified that higher density correlates with lower response variability, suggesting that paracrine communication decreases cellular variability response. To quantify the observed benefit of paracrine communication they performed a computational analysis based on signal-to-noise ratio (SNR). This analysis showed that paracrine communication can increase the response SNR.

To measure the spatial wound response they developed and used a new microfluidics-based device. The single cell analysis of Ca2+ and ERK showed the importance of cellular position for the determination of cellular response. Applying the same computational strategy as before in a better-controlled environment, they showed again that the paracrine communication distance decreases the noise of the response. However they also identified a limit of paracrine communication, which consist in reducing the gradient magnitude.

To directly measure the paracrine communication, the authors used a co-culture system in which they can distinguish "sender" and "receiver" cells. They measured the ERK level in "receiver" cells in relation of the distance from a sender cell. The authors determined the paracrine communication distance and compared it with their predicted distance value that maximizes the SNR. Therefore they concluded that the distance between communicating cells maximize cellular response fidelity.

Essential revisions:

1) Although the new microfluidics-based device represents a great tool to study wound healing in vitro in a highly controlled manner and already provided intriguing results, it would be important to see if some of the principles of paracrine communication observed in a static media condition can also be identified in a non-static condition (Figure 2–figure supplement 1).

2) The data collected and the analysis are interesting, however they refer to an in vitro setting (this should be more clear in the Abstract). Please discuss these data in the light of in vivo data present in literature (i.e. ERK reporter has been used in vivo).

3) The analyses are largely described in the text without any equations; having the equations in the Methods or supplements would be much better, and several of the quantitative figures are described quite vaguely (Figure 1G, Figure 2H, I, J, and Figure 3F).

4) At a number of points, the meaning of error bars and p-values are not explicitly stated, and these need to be fixed.

5) Given the setup in Figure 1A, please show some quantification of ERK variability in Figures 1 and 2. This omission seems odd given that ERK is the signal that is ultimately being affected by the averaging, and which is being predicted by the analysis. Is it in fact less variable than the Ca2+ signal in these systems? There also seems to be a logical disconnect – the optimum communication distance shown in Figure 2J is calculated based on Ca2+ responses, but then compared to the ERK response in Figure 3.

6) In Figure 1F (and in general), what is the expected role of diffusion? The authors conclude that there is no upper bound on SNR as distance is increased, but their analysis doesn't appear to take diffusion into account, which would presumably limit the distance over which averaging could be effective. This should be clarified. It would also be helpful to comment on the role of the integration time over which the cellular response operates.

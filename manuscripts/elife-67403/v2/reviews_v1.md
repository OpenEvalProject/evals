# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67403.sa1](https://doi.org/10.7554/eLife.67403.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript will be of interest to geneticists seeking to establish rules that govern gene regulation. To explain why a sequence enhances, rather than silences, gene transcription the authors draw our attention away from the binding of a single transcription factor, to focus instead on the number and diversity of transcription factor molecules that bind to it. Using a relatively simple metric called sequence information content they appear to be able to improve the prediction of enhancer over silencer sequences. A concern is whether the silencers are true silencers, or whether they only act as such in this specific experimental paradigm.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Information content differentiates enhancers from silencers in mouse photoreceptors" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Chris P Ponting (Reviewer #1).

Based on the reviews we received, I am sorry that we cannot offer publication in eLife.

While one of the reviewers was very positive, the other reviewer pointed out substantial weaknesses. We acknowledge that your title clearly makes narrow claims, but for eLife we would have hoped that the findings could be generalized.

Reviewer #1:

Why can silencers be enhancers in other cell types? Why is it that active chromatin epigenetic marks or binding of a single transcription factor do not reliably predict active enhancers? These are thorny issues in genomics because they hinder our mechanistic understanding of gene transcription regulation.

In this well-written submission the authors go beyond their previous publications using the same experimental system (White et al., 2013, 2016). They use MPRA for the CRX transcription factor (TF) in explanted mouse retinas to show that epigenetically indistinguishable sequences are classified more accurately as enhancers or silencers by the number and diversity of lineage-specific transcription factor binding motifs that they contain. They separate enhancers from silencers by enhancers' more diverse collection of TF motifs. This distinction is captured in a metric called sequence information content calculated from both TF motif count and diversity. This single metric is slightly worse at predicting strong enhancers over silencers than a model considering the PWMs for 8 TFs.

1. Whether the authors observe a bias in the linear arrangement of these TFs' motifs that might assist in distinguishing enhancers from silencers?

2. p10 the choice of the 8 lineage-defining TFs was somewhat arbitrary because of the arbitrary nature of PWM significance thresholds. Please justify their choice and number, and comment on how well the model performs when this TF set is altered?

Does an evolutionary change in information content calculated between orthologous Mus musculus and, say, Mus spretus sequence help to separate active (enhancer/silencer) sequence from inactive sequence? (https://doi.org/10.1038/sdata.2016.75).

p9 please explain further "we chose to represent the zinc finger motif with MAZ based on the PWM qualities".

p21 why were different FIMO p-value thresholds applied?

p27 line 562 "silencers as negatives"?

line 132 "For motifs that matched multiple TFs, we selected one representative TF for downstream analysis (Figure 2—figure supplement 2, Methods)". Please explain further.

Reviewer #2:

The authors state that enhancers and silencers often have the same epigenomic profiles and attempt to identify sequence-based information to differentiate between the two types of elements. They use massively parallel reporter assays to test elements that bind CRX for activity in retinal explants. The authors then look for differences in motif content between the elements that act as silencers vs. those that act as enhancers of gene expression from a basal promoter. They find that although enhancers and silencers have motifs for the same transcription factor – CRX, the number of sites and diversity of other TF sites is greater within enhancers. They suggest motif content is a way to distinguish between the two types of elements. I'm not convinced that anything can be determined about silencers using this experimental design.

Strengths:

The authors test many putative enhancers in mouse retinas and identify elements whose function requires CRX sites.

Interestingly, different behaviors of functional elements could not be predicted based on differences in DNA accessibility or ATAC-seq peak or CRX occupancy. This is a nice systematic example of how difficult it is to predict an enhancer strength or activity based on differences in epigenomic data and highlights the need for sequence-based approaches to identify the specific activity of an element.

They do a nice analysis of the inert vs. weak and strong enhancers. The data and analysis of these experiments could be really informative for understanding why not all regions that bind CRX and are within open chromatin are active enhancers.

Weaknesses:

I'm concerned that the silencers they detect could be an artifact of the experimental design. The promoter contains CRX sites and NRL sites, so there is some level of basal expression; the silencers are enriched in repressors, so is it just that the elements containing a repressor are silencing the basal transcription? Moreover, what does this mean relative to the elements in the endogenous locus, if an endogenous promoter doesn't have CRX or NRL sites within its promoter or basal transcription does this mean the silencers as described in this assay are not really silencers within the genome. I don't think it is possible to make conclusions about a cis-reg element's silencer capacity based on these experiments.

In line with this, they find that the silencers bind CRX in combination with a repressive TF. Would they find that enhancers as they define them bind a combination of transcriptional activators and that silencers bind some activators such as CRX in combination with a transcriptional repressor expressed in the cell type where the element acts as a silencer?

I am also not convinced that silencers and enhancers are different things. If a genomic element controls the time and location of gene expression, then it is an enhancer – enhancers can bind activators and repressors and restrict expression to only particular cell types. I think trying to call things enhancers, and silencers makes things overly complex, especially considering the fact the authors point out that the same element can be an enhancer in one tissue type and a silencer in another. I am also concerned about this in relation to my previous comments on the experimental design and the issues demonstrating that a silencer really works this way within the genome.

As silencers are decreasing expression from a basal promoter and the whole paper is centered on this, I think the choice of promoter in this experiment is critical. I don't think one promoter can be used to draw such conclusions. The authors use a basal promoter for the Rho gene, which contains one NRL site and CRX sites, and these could work in combination with the sites within the elements being tested. I wonder if the elements they're testing would behave the same way with their endogenous promoters or with another promoter that does not contain CRX or NRL sites. Testing these elements with no promoter does not really address this question. It would be helpful to test these elements with the Rho promoter where you mutate the NRL and CRX sites. It would also be helpful to test these elements with a different promoter for another gene that is expressed in the retina, ideally on that doesn't contain CRX and NRL sites, to see if there are enhancer-promoter interactions that are influencing your results and thus your conclusions. If the endogenous promoters don't contain CRX or NRL sites or don't have a basal level of transcription, would your element really be a silencer? I don't think it would, and I'm concerned that the results you're seeing are an artifact of your experimental design.

The paper claims that information content can be used to distinguish between these two classes of element, I would like to see how this compares to prevalence to transcriptional repressors, and activators found in silencers and enhancers as the only TF mentioned to work with CRX in the silencer is a well-known repressor Snail. Would the presence of a repressive TF be a better predictor of silencer vs. enhancer activity?

I would like to see that the information content model performs better than measuring the prevalence of activator and repressor motifs.

In line with this, the difference in information content between a silencer and an enhancer is 3 motifs for 2 tfs vs. 3 motifs for 3 tfs or 4 motifs for 2 tfs. For the silencers and enhancers, what % of these TF motifs are repressors, and what % are activators.

In my opinion, the authors should focus on using their data to work out what makes regions under their genomic marks functional enhancers vs. inert elements.

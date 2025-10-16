# Peer review - Round 1

Editors:
- Timothy W Nilsen, Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75555.sa0](https://doi.org/10.7554/eLife.75555.sa0)

This manuscript provides a deep mutational scanning of the deaminase domain of human ADAR2 to provide a comprehensive assessment of amino acids that alter editing activity at a specific adenosine flanked by preferred nucleotides (UAG). The results are quite important in terms of impact on precision medicine.


---

# Peer review - Round 1

Editors:
- Timothy W Nilsen, Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75555.sa1](https://doi.org/10.7554/eLife.75555.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Comprehensive interrogation of the ADAR2 deaminase domain for engineering enhanced RNA editing activity and specificity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Timothy A Whitehead (Reviewer #2); Nina Papavasiliou (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

All three reviewers raised substantive concerns regarding description of the methods and statistical analyses. Given these concerns, we had no choice but to decline the paper, but encourage you to resubmit if and when you can address the points raised by the referees as thoroughly as possible. The issues are particularly concerning since this manuscript was submitted as a research method or tool paper.

Reviewer #1:

The authors aims to enhance efficiency and specificity of RNA engineering mediated by ADAR2 deaminase domain (ADAR2-DD) by three approaches. First, they interrogated the residues in a portion of ADAR2-DD by deep mutational scanning (DMS), providing comprehensive map of residues important for the core region of ADAR2-DD. Second, they identified a novel mutation N496F that increases editing efficiency for a 5'-GA-3' motif. Third, they showed the split ADAR2-DD design with good editing efficiency and specificity. This work provides deeper understanding of ADAR2 deaminase domain as a tool for RNA directed engineering. Although the work presents advances, I have several concerns that the authors need to address in more detailed analysis.

1) The DMS screen described in Figure 1a is not intuitive to understand. Where exactly are the editing sites in the ADAR2-DD? How many sites are there in total? How are the editing sites and mutations identified in the sequencing reads? A better drawing, explanation, figure legend and methods are needed.

2) For the DMS method, since the editing site is in ADAR2-DD itself, when making mutations the structure of the RNA substrate might change, especially the ones near the editing site. Then the effect might not be sole consequence of the protein mutant. If RNA substrate might change in structure, is the DMS result still consistent with the validation result using the cluc assays?

3) In addition to measuring the editing level of targeted sites, can the authors measure off target in the deep sequencing data? This would result in both editing efficiency and editing specificity measurement.

4) ADAR1 is perhaps expressed in the chosen human cells. Would any of the results from the DMS and the validation be complicated by the editing from endogenous ADAR1?

5) It is very interesting that many mutants showed equal or higher activity than the well-known E488Q mutant. What are the efficiency and specificity for these (at least for some representative ones from the validation)?

6) For the N496F mutant, what are the transcriptome wide off-targeting data? What about other non-GA sequences?

7) How was the split ADAR2-DD chosen? Current writing is very simple. It would be useful for the community if the authors provide more details of the reasoning.

8) What is the correlation of the luciferase assay signal to the actual editing level of the transcript? What if comparing all designs (mutations and split-ADAR2-DD) in the same assay so we can see direction comparison of the editing efficiency and specificity? Preferably, using editing level of a target site as a readout to compare all designs and the off-target analysis by RNA-seq.

9) To validate all the findings in this work, it would be desired to show how an engineered ADAR2 DD, in a split fashion, would edit an endogenous substrate with a non-UAG motif (such as GAC). What would be the editing efficiency (% editing level) and the transcriptome-wide specificity?

Reviewer #2:

Katrekar and colleagues developed a screen for deaminase acting on RNA (ADAR) and screened most single amino acid substitutions across the catalytically active domain for RNA editing and for activity at 5'-GA-3' motifs. Separately, they developed a split ADAR and evaluated specific and off-target RNA editing using whole transcriptomes. The paper does not read like a coherent story and instead is two separate papers: Figure 1 – 2 involve the screen and evaluation of single clones resulting from the screen, whereas Figure 3-4 involve the split ADAR. The strengths of the paper involve the novelty of the genetic screen and, separately, the development and validation of the split ADAR system. There exist major concerns about the representation of the results from the screen, along with minor suggestions on the split ADAR story.

1. The statistical underpinning of the validity of the screening results are unexplored in the main text and need to be described accurately. The authors split between Z scores (Figure 1), Fold change in DMS relatiive to ADAR2-DD (Figure 2), % edited (in supporting information files and Figure 1d), DMS log2 fold change (SI Figure 2). Each of these screening outputs (if all are included) need to be described in the main text and justified. My personal opinion is that one or at most two metrics can be used in the paper to avoid confusion. I have particular concerns in this section about the following:

a. Replicates for the screen. The paper only lists replicates in three places, and in no place was how this replicate performed. How were they performed? Biological replicates? Technical replicates? Different days? These experimental details need to be discussed explicitly.

b. Of concern for the replicates are the relatively low correlation between replicates (R2 = 0.48 by my calculation). The correlation is not discussed at all in the main text – this data needs to be explicit for the reader to judge for herself the validity of the data presented.

c. The replicate showed in SI Figure 1d has a correlation missing for the worst performing sample ("wt-X-TAG") and the meaning for wt-X, wt-Y, etc are not described.

d. The validation performed isogenically involves cherrypicked samples with low variance between them (R2 for the variants described in figure 2b are 0.87) and don't represent a fair comparison. The authors state that "We observed that a majority of the mutants (85%) followed the same trend in our arrayed validation as seen in the pooled screens" but the meaning behind the sentence is not clear. What does the same trend mean and how is it calculated? Determine the statistical significance using a t test and show comparisons between isogenic datasets using rank correlation or R2 correlation.

e. Points a-d lead to the following conclusion that the screen, while clever and well implemented, has relatively high error and the data should not be presented as a heat map as the authors present in Figure 1. Deep mutational scanning experiments where data is presented as heat maps typically have R2 values of 0.8 or higher. This data is useful – the data for conservation at each position should be relatively robust even with the error in the screen reported in the paper. This screen can also be used to identify 'hits'.

Reviewer #3:

The paper by Mali and colleagues is an interesting mix of experiments on ADAR2 functionality: on mutations that increase activity, on a split ADAR2 construct appears to decrease off target effects, and on a split RESCUE construct that is said to also increase the specificity of C to U editing.

The notion of a split ADAR is certainly novel (brought together by the binding in situ of two elements on the RNA – an MS2 and boxB element, plus a second pair). However the paper would really benefit from being more explicit on some of the results. For instance, the "decrease of off target effects" though apparently significant, would benefit from some nuance – for example are there commonalities to the off-target targets? (are there RAB7A-specific off-targets vs KRAS specific ones and what would that imply?) In other words how generalizable to other transcripts are these findings?

Continuing with the notion of tradeoffs, are GAC/GAG-focused mutants "worse" on other triplets? and which?

Finally, given how little has been published on targeted C to U editing (excepting RESCUE), it is important to treat figure 4d as a little more than an afterthought – with a comprehensive analysis equivalent to the treatment of A to I editing.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Comprehensive interrogation of the ADAR2 deaminase domain for engineering enhanced RNA editing activity and specificity" for further consideration by eLife. Your revised article has been evaluated by James Manley (Senior Editor) and Timothy Nilsen (Reviewing Editor).

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

While both reviewers were quite positive about your revised paper, they felt that additional textual changes and/or additions as outlined below would further improve the manuscript. Please address these comments as thoroughly as possible.

Reviewer #1:

The manuscript by Mali and colleagues is substantially improved from the earlier version. If I had a single comment to make on the revision (and only because they now have the data to look) is this. Normally, a guide RNA bound to the coding region (as will be the case for the cAg in Rab7a) would be expected to reduce transcript abundance (through RNAi like effects). In view of the data in figure 4a/4b, is this true? if so it would be important to point out, because this is not normally something that would be observed in a "restore of a stop codon" situation, but it is something we need to worry about in terms of therapeutic efficiency.

Reviewer #2:

This revised manuscript provides a deep mutational scanning of the deaminase domain of human ADAR2 to provide a comprehensive assessment of amino acids that alter editing activity at a specific adenosine flanked by preferred nucleotides (UAG). The author recover 33 individual mutations that either increase or decrease editing, including several mutations that were previously known to impact editing. The authors perform a second DMS starting with a known hyperactive mutant and seeking to obtain a mutant that has altered preferences for the nearest neighbors of the target adenosine. This second goal is quite important in terms of impact on precision medicine. The last goal of the paper is to develop a split ADAR method of editing target adenosines with the goal of reducing off target adenosines, again an important technological advancement for therapeutic use of ADARs. Overall, the revisions adequately address the concerns about clarity, experimental approaches and statistical analysis.

Two areas that need to be addressed are listed below.

1. It would be beneficial if the authors specifically identified the novel mutations identified in the deaminase domain determined from the initial DMS experiment on the UAG codon (SI Figure 2). Furthermore, the initial reviews noted that there were several mutations (ex. D419W, D362R, D365R, etc) that exhibit a similar elevated activity as the well-described E488Q hyperactive mutant on the UAG substrate. The authors were asked (by reviewer 1) whether these hyperactive mutants are specific to UAG or also behave similar to E488Q (exhibit increased editing at less preferred codons). This was not addressed in the revised manuscript.

2. The second DMS screen identified only one mutant, N496F, that could significantly enhance editing of a GAC codon. The authors did not recover this mutant in the initial screen, is that due to the lack of N496F affecting editing at UAG codons?

The abstract describes this mutant as "greatly increased enzymatic activity at 5' GAN-3' motifs". This language is overstated both in terms of the activity (which is simply 1.1-2 fold enhanced (Figure 1h)) and with regards to the specific motif. The comprehensive assessment of the specificity of this mutant (requested in the initial review, SI Figure 3c) indicates this mutant has enhanced activity not only for GAN motifs but also CAN motifs, with CAC being the second most edited codon after GAA (and above several other GAN codons).

The authors should both tone down the language in the abstract and discuss the lack of specificity of the E448Q, N486F mutant, especially in terms of what may occur with off-targets. The authors have already performed the experiment (Figure 3b and Figure 4b) but do not discuss the data in this regard, despite the initial request by Reviewer 1. This is particularly important as the authors stress that finding mutants with altered preference is important for precision medicine, but if these ADAR mutants also increase off-target editing, the findings are less exciting-albeit more rationale for using the split ADAR technology developed.

The methodology for the comprehensive analysis of editing preferences should be added to the manuscript.

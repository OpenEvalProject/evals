# Peer review - Round 1

Editors:
- Tony Yuen, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77976.sa0](https://doi.org/10.7554/eLife.77976.sa0)

The web-based software developed in this study will be of interest to researchers who develop CRISPR-based diagnostic methods. The use of CRISPR-Cas to rapidly identify specific mutations in both cancer and infection is an evolving field with good potential to play a role in future research and diagnostics. This software will facilitate the implementation of such technologies and is therefore useful.


---

# Peer review - Round 1

Editors:
- Tony Yuen, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77976.sa1](https://doi.org/10.7554/eLife.77976.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "CriSNPr: a single interface for the curated and de-novo design of gRNAs for CRISPR diagnostics using diverse Cas systems" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mone Zaidi as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Shruthi Sridhar Vembar (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the authors have provided a small set of data that validated the design of the software, more validation experiments will be needed to demonstrate how well the guide RNAs work, or which designs are predicted to work better than others. These additional data should further support the usability of the software.

1) Figure 4 gives one example with the detection of a short WT and mutated oligo from SARS-CoV-2 as the template. Similar experiments may be done with several SNVs in real cells, to also include the complexity of genomic DNA. For comparison, it would be elegant to include a gRNA also recognizing the WT sequence in some of the experiments, including in Figure 4.

2) The authors only test their system for a single mutation (E484K) with three CRISPR effector proteins (FnCas9 and LbCas12a). More extensive validation (multiple designs per mutation, many mutations examined) is crucial for sequence design methods like CriSNPr.

3) How well do the pre-designed gRNAs work for detecting human SNPs? The authors should compare their method with existing assays to detect human SNPs.

Reviewer #1 (Recommendations for the authors):

I congratulate the authors on a great piece of work. Here are some suggestions which could improve the manuscript:

1. The Yes/No options in the flowchart of Figure 3a were confusing. For example, for the Input SNP ID box, the first check is if it is valid or not. The flowchart uses 'Not Valid' instead of 'Valid', and hence there is a double negative which becomes a positive, and so on. My suggestion is to change 'Not Valid' to 'Valid or not': if the answer to this is 'Valid', the Python Flask is invoked; if it is 'Not valid', the program outputs an error message and exits. The same is true for the 'Not found' option. I am sorry if this point doesn't make sense, but if I could have included a figure here, it would have been easier to explain.

2. To improve the flow of the paper, figures 4 and 5 could be switched. Basically, the paper could end with the experimental detection of the SARS-CoV-2 variant, S gene containing E484K mutation, using CriSNPr-designed CRISPR RNAs and PCR primers.

3. Since page and line numbers were not included in the submitted manuscript, it is difficult for me to point out the sentences which could be reworded for clarity. There were also a few typos and phrase/word repetitions that should be addressed.

One last suggestion is to develop a stand-alone version of CriSNPr which researchers can download and work with locally.

For the online version, please include a form in the 'Contact us' section where researchers could write to the authors requesting their organism of choice to be included in CriSNPr.

Reviewer #2 (Recommendations for the authors):

Here follows some suggestions:

It makes the review process easier if the manuscript has line numbers. I suggest adding this in the future to any manuscripts.

I realize that this could be difficult, but is there anyway the user can be helped to prioritize which gRNAs to use? Is there any scoring system that could be used or developed? It would be useful to at least discuss this a bit in the manuscript.

As briefly stated above, the manuscript would benefit from more validation experiments, in a systematic way showing to what level the suggested guide RNAs work. Figure 4 gives one example with the detection of a short WT and mutated oligo from SARS-CoV-2 as the template. I would suggest doing similar experiments also with several SNVs in real cells, to also include the complexity of genomic DNA. For comparison, it would be elegant to include a gRNA also recognizing the WT sequence in some of the experiments, including in Figure 4.

The manuscript would benefit from more detailed information about the basis for the guide RNA design for the different Cas proteins, including highlighting references better in the methods part as well as elsewhere in the manuscript (e.g. on p. 5 "… and the required crRNA and primer design parameters based on gRNA design principles available in the literature for each Cas protein" would benefit from adding references).

I lack references on other places too:

On p. 20 "performed the diagnostic assays according to previously published protocols".

On p. 23 "In clinically relevant variations, G.C>A.T class is dominating the other mutation classes".

On several places in the manuscript, its stated that specific updates will be made to the software (e.g. page 26). On the one hand I appreciate the dedication, but it also begs the question if they really think the software is ready to be published already.

Figure 3 and Sup. figure 2, are of fairly low quality. I realize that this is because the figure has been copied from the webpage, but consider if you can make some changes so that the quality is higher.

Consider rearranging the first page of the web page. To me it doesn't make sense that the "Seq-CriSNPr" part is shifted to the right compared to the "human" part. It also looks a bit strange that the distance on the y-axis between the "Seq-CriSNPr" and "Human", is much longer than the distance between "CriSNPr" and "Human". I think the web page will look more professional if this is fixed.

Reviewer #3 (Recommendations for the authors):

1. The first three figures are essentially schematics. There isn't enough data in this paper to support the claims made by the authors. The authors should provide additional data showing how they tested their system (both computationally and experimentally).

2. The authors only test their system for a single mutation (E484K) with three CRISPR effector proteins (FnCas9 and LbCas12a). More extensive validation (multiple designs per mutation, many mutations examined) is crucial for sequence design methods like CriSNPr.

3. How well do the pre-designed gRNAs work for detecting human SNPs? The authors should compare their method with existing assays to detect human SNPs.

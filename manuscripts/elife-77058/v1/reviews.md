# Peer review - Round 1

Editors:
- Shozeb Haider, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77058.sa0](https://doi.org/10.7554/eLife.77058.sa0)

This is a valuable paper that discusses a holistic understanding of LCRs of not only individual proteins but also provides a broad perspective of proteomes across many species. The data presented provides solid evidence on how LCR organisation and assemblies may be shared between subcellular compartmentalisation and extracellular organismal structure.


---

# Peer review - Round 1

Editors:
- Shozeb Haider, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77058.sa1](https://doi.org/10.7554/eLife.77058.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "A unified view of LCRs across species" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sreenivas Chavali (Reviewer #2).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Specifically, the reviewers believe that current data needs to be reanalyzed and additional experimental data are requested. Usually, papers are rejected from eLife if a revision would take substantial experimental work. Detailed recommendations for authors are listed below.

Reviewer #1 (Recommendations for the authors):

The paper is extremely dense and difficult to read and appears focused on a relatively narrow question. One barrier is that it is poorly linked to both a clear biological background for LCRs and the linked references in the introduction don't clearly talk about the same phenomena. This needs to be expanded to help readers who are not familiar with LCRs understand why this study is important and would help establish that the work will have a deeper impact. It would also make clearer what this manuscript's novel findings are- at present, it is not clear if results add detail to existing views in the literature, or make new discoveries (for example, the arguments about LCRs and localisation/function). Additionally, terms that are not widely used, such as protein valence, need to be defined to be suitable for a broad audience.

A second issue in the writing is that the relationship between the Results sections is unclear. The broad flow of the paper as I read it is that the authors present the method, apply the method to proteomes, experimentally explore one protein, go back to considering proteomes, then compare different proteomes. Specifically, the experimental work is not well justified- it is not clear how that protein was chosen, and how the findings relate to the work presented specifically. It doesn't validate the other findings in a meaningful way and raises questions of valence that don't arise from the analysis. It should be better linked to the rest of the presented work or removed.

To test potential issues with the null the authors should repeat the testing with a null derived from the amino acid composition derived from the individual proteomes under study. This is particularly important in light of some residues apparently rarely appearing in LCRs (e.g. tryptophan).

In the comparisons of the dotplot based method with existing techniques the graphs presented in figure 1 supplement 3 are almost unreadable due to the choice of colours used, particularly in comparing SEG to dotplots (A).

To attempt to remedy issues around the link between LCR contents and function/localisation I recommend the authors:

– Include a justification for the choice of p-value, and confirm in the methods that multiple tests correct took into account both the number of amino acids and the number of function/localisation classes. A discussion of the effect size as well as the p-value would be helpful.

– Use chi-squared and/or permutation tests to test cluster membership (rather than frequency) is more than expected for random perturbation for different amino acids.

– Use a heatmap, possibly with KDEs, to plot the density of specific categories relative to the raw umap. This is particularly important for Figure 3 supp Figure 3 where the points in some categories are so sparse it is hard to see the point distribution. It may be the case that these new plots are quite flat; in this case, it may be better to limit the use of umap plots and focus more heavily on robust statistical tests as umap plots are fundamentally a visualisation technique.

Reviewer #2 (Recommendations for the authors):

Although the study presents a unique approach to identify LCRs and exciting insights into LCR sequence space, there are few issues that need to be addressed.

1. It is not clear how the FDR threshold of 0.002, to define the LCRs was chosen. While Figure 1 —figure supplement 2 presents the relevant statistics for different thresholds, it is not intuitive why 0.002 was selected. The authors may consider different representations (distinct colors or dotted vs solid lines) to differentiate the lines corresponding to the thresholds in the supplementary figure. Moreover, the thresholding appears a bit random, as the authors reset the FDR threshold to 0.05 for E. coli. Is the threshold species/clade-specific? If so, what factors determine the thresholding. This has to be explicitly discussed for the tool to be used by other researchers in the field.

2. Figure 1: Panels D and E shall be presented first, followed by panels A, B and C. Distinct annotations should be provided for SRRM2 and MUC5A and should be discussed in the figure legends. The authors might consider presenting distinct examples with bars highlighting the similar and distinct types of LCRs in the examples as shown in Figure 1 —figure supplement 4, to allow the readers to appreciate the Dot-plot approach, rightaway. Also, Figure 1 —figure supplement 1 appears to be redundant and can be removed.

3. The discussion on the comparison between SEG, fLPS and the Dot-plot methods is rather limited (lines 209-215). Does the Dot-plot method provide more false-negatives with respect to identifying LCRs?

4. LCRs have been annotated for single amino acids. What was the basis for determining the most prevalent amino acid? The annotation of LCR sequence-space by eye appears arbitrary, hampering reproducibility, should this approach be used by others. Also, the approach does not differentiate between repetitive and non-repetitive LCRs. This must be discussed as limitations in the discussion.

5. On similar lines, physicochemical properties of the amino acids in the LCRs are known to aid formation of higher order assemblies. This implies that though the type of amino acid may vary, but similar physicochemical properties across the LCRs can contribute to similar type of interactions (e.g. G3BP1). Such similarities in the physicochemical properties of the amino acid is not taken into account. Therefore, a protein with multiple LCRs composed of physicochemically similar amino acid types could be treated as "multi distinct" or "multi mixed" in the dot plot method, although the nature of the amino acid type and thereby its mode of function in terms of higher order assemblies, could fall under "multi same" category. The authors should at least discuss these limitations explicitly.

6. The authors may think of some in vitro experiments to test the biological importance of T/H LCRs in Teleosts. Looking into the functions of these proteins might provide insights for designing such experiments. The entire section, as provided, is a descriptive account of the observations, with limited biological insights.

Reviewer #3 (Recommendations for the authors):

1. I would like the authors to more fully compare and contrast their approach with a SEG-based approach that extracts LCRs and then compares their composition. I believe they already used SEG to find LCRs, so this should be pretty simple (i.e. generate UMAPS based on the composition of the LCRs identified by SEG vs. their dotplot matrix method).

2. I would like to see the role of codon bias and repeat expansions discussed (and ideally considered, perhaps as an explanation for the bridge sequences)

3. The manuscript felt rather long – I understand the desire to place as many interesting observations in as possible, but as mentioned these are unavoidably cherry-picked, inasmuch as they are interesting and compelling to the authors (and, to this reviewer, I should say – the cherry-picking is unavoidable and not a criticism!). Perhaps instead some of these could be summarized with a table that lists protein, function, LCR, and possible observation? This I think would help avoid readers needing to wade through lots of text to obtain what really amounts to very nice hypotheses, as opposed to specific observations that require open prose. The teleost-specific analysis felt sort of tacked on at the end, and I'm not sure added much (but am happy to be disagreed with). I would like to see the manuscript length reduced, ideally with some of the observations condensed into a table.

4. I would like to more concretely know what (specific) question(s) this work answers. "We don't know much about LCRs" is not a particularly specific motivation, so I'd like to better understand what are the knowledge gap(s) the authors are solving.

5. The authors should provide detailed annotations of all LCRs in an easy-to-access format (both Excel and text-based), and should also I think provide a way to access and make sense of the data shown in the UMAP plots (perhaps with LCRs divided by cluster).

6. Consideration of the papers mentioned on this topic by Eric Ross.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A unified view of low complexity regions (LCRs) across species" for further consideration by eLife. Your revised article has been evaluated by the original reviewwrs, Volker Dötsch (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #3 (Recommendations for the authors):

This revised version is much improved!

The focus on claiming the dot matrix approach lets one find functionally important LCRs.

Fundamentally, I think the authors are overselling their approach as a way to easily find functionally important subregions in proteins.

I think this method is one way to find amino-acid enriched LCRs. I fundamentally do not believe this approach is somehow magically different from finding low-complexity sequences and then categorizing based on composition after the fact (as one could do with SEG or some other composition-independent metric), or by defining one (or more) residue types to extract contiguous low-complexity subregions enriched for a specific residue (as done by Gutierrez et al).

However, I think this issue can be addressed simply by scaling back the language and making less strong claims regarding what can/cannot currently be done. I recognize these changes were made to address previous critiques, but on my reading of the current version the setup feels like a straw man.

I think the actual way the new intro sets things up is great – I just think the implication that dot matrices are essential for this investigation is unsupported.

To specifically support this suggestion, I have provided some analysis below.

G31BP focus

The initial example focusses on G3BP1, and highlights the fact that there are two flavors of LCRs in G3BP1. The authors then relate those different LCRs back to previously published work to make the point that the dot-plot method can identify functionally distinct subdomains. The authors then state,

"The presence of these compositionally distinct LCRs are critical for the ability of G3BP1 to form stress granules, as the acidic LCRs interact with and inhibit the RGG domain, preventing it from interacting with RNA, a necessary step of stress granule assembly. Thus, by highlighting the relationships between different LCRs, dot plots can provide key insights relevant to protein function."

But the functional insight here didn't come from the dotplots – the functional insight here came from prior work, in which acidic rich and arginine rich subregions were already identified and characterized. The dotplots didn't identify that these regions could interact, nor did it provide any inference regarding the putative functions of these regions. With this in mind I really find the logic here hard to follow; my reading is that the setup is:

1. LCRs are important for biology.

2. Here we provide a new way to find LCRs.

3. By highlighting the relationships between different LCRs, dotplots can provide key insights relevant to protein function.

But this last point really is not what happened – the fact these LCRs are 'different' was not what was used to highlight them as important – instead relating them to prior literature was used to highlight functional roles, and the fact they are 'different' comes from prior work. The chemical logical behind this difference is not explicitly encoded by the dotplot matrix, so (for example) and Arg-rich and Lys-rich LCR would appear equally different.

LCR3 (as the authors define it) is not even particularly arginine rich (4/23 Arg residues) (LRGPGGPRGGLGGGMRGPPRGGM), the RGG domain of G3BP1 contains 11 arginine residues, so most of the arginine's that drive RNA binding actually fall outside of the "arginine-rich LCR3".

In sum, it's unclear to me how the authors' approach relates to the functional investigation of proteins beyond highlighting the low complexity domains that have been previously shown to be important. Does this mean that all 37,342 LCRs in the human proteome should point to functionally-important features? And if not, how is one meant to discriminate between functional vs. non-functional LCRs?

Not to belabor a point, but later the authors then state:

"The examples of dot plots make clear that functional information about LCR type and copy number can be extracted from dot plot matrices "

I still feel like there is a critical step completely missing here; HOW do we extract "functional information" from the dotplots? Are the authors saying that every LCR is functionally important? If yes, in what way? How are we (readers/users) meant to use information for dotplots on previously unstudied proteins to infer functionally important features beyond "If there's an LCR remove it and see if it matters".

The authors go on to say:

"The examples of dot plots make clear that functional information about LCR type and copy number can be extracted from dot plot matrices. However, there currently is not an approach to globally assess these features of LCRs and their functions. While several methods exist for identifying LCRs these methods are unable to determine LCR relationships such as type and copy number"

The way one determines the type and copy number is looking at (1) the amino acid composition of LCRs identified by these other methods and (2) the number of LCRs identified. This is precisely what the authors are doing with their own method.

For example, using SEG on G3BP1 and setting an arbitrary threshold here of 0.45 we find 3 SEG-derived LCRs (highlighted in blue here) which correspond to 144-160 ('PQEESEEEVEEPEERQ'), 192-205 ('EPEPDPEPEPEQE'), and 430-448 ('PGGPRGGLGGGMRGPPRG').

The authors' approach identifies basically the same three regions:

SEG: PQEESEEEVEEPEERQ

DotMatrix: TEPQEESEEEVEEPEERQQ

SEG: EPEPDPEPEPEQE

DotMatrix: AEPEPDPEPEPEQEPVS

SEG: PGGPRGGLGGGMRGPPRG

DotMatrix: LRGPGGPRGGLGGGMRGPPRGGM

Now I want to be clear – I have no particular love for SEG, but my point is simply that to claim there is no way to characterize LCRs that takes type and copy number is demonstrably false.

I would encourage the authors to not oversell the method as some magic bullet, and not pretend one could not do what they have done here with another method. You could. The big difference is people haven't and the actual analysis of proteomes is interesting and I think well written and well-explored.

Codon bias remains undiscussed

When the authors discuss biases and bridging among distinct classes of LCRs, I would, again, STRONGLY encourage them to consider codon biases – can overlapping/related enrichments for specific residues be explained based on codon distance in repetitive and slippy sequences? I recognize the authors state that 'this is out of scope' but… it's not. If the authors are going to find LCRs with specific compositional biases and comment on bridges between distinct classes of LCRs, ignoring a codon-based explanation for these bridges is most definitely within scope.

LCRs are short

One thing I had not appreciated in the original manuscript is that the LCRs are short. In the human proteome, 87% of LCRs are 20 residues or shorter. This to me makes me wonder if LCR is really the right term. The LCRs identified previously have generally been large domains, while here LCRs are functionally of the same length as motifs, should these perhaps be defined as LCMs (low complexity motifs) more

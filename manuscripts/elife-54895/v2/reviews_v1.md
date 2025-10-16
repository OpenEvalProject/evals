# Peer review - Round 1

Editors:
- Dan Larhammar, Uppsala University Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54895.sa1](https://doi.org/10.7554/eLife.54895.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

A mutation scanning procedure for amino acid replacements in G protein-coupled receptors is described and the outcome detected with cAMP-induced transcription of a luciferase reporter. Using the human beta-2 adrenergic receptor as proof of principle, the authors have investigated almost every possible amino acid replacement throughout the sequence. One interesting new observation is a conserved 'latch' involving three highly conserved residues in the receptor's first extracellular loop.

Decision letter after peer review:

Thank you for submitting your article "Structural and Functional Characterization of G Protein-Coupled Receptors with Deep Mutational Scanning" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James S Fraser (Reviewer #1); Aashish Manglik (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

All three reviewers and myself agree that this manuscript describes an interesting and potentially very useful scanning procedure of amino acid replacements in G protein-coupled receptors, exemplified by an impressively extensive analysis of the human beta-2 adrenergic receptor. Almost all possible mutations were evaluated after agonist stimulation, measured as cAMP-induced transcription of a luciferase reporter. The application of the procedure on beta-2 confirms several previous observations and thereby serves as proof of concept for this approach. It adds a few new observations, especially the proposed conserved 'latch' involving three highly conserved residues in EL1.

Essential revisions:

Detailed conclusions about mutation outcomes are limited by the fact that the one and only assay measures functional response and hence cannot distinguish mutational impact on all the preceding steps including biosynthesis, folding, intracellular transport, ligand binding, conformational change, G protein coupling and receptor internalization. Mutations that affect the functional output in an indirect fashion are likely to occur and this possibility should be discussed further. Ideally, it would be desirable that the authors could present quantification of cell surface expression for at least a subset of the deleterious mutants. Hopefully, such data has been collected.

Another aspect that is (as noted) important is the level of noise in the system. For example, it is not at all clear why it was necessary to use on average 10 barcodes per mutant, when other studies employing DNA-level abundance of barcodes have gotten away with smaller numbers of barcodes per variant.

Do all pairwise combinations exhibit equal reproducibility, or is it possible to model measurement error (e.g., making use of the number of read counts) as other studies have done to estimate error in individual measurements? Perhaps then we can be confident in some subset of residue-level measurements. Error estimates could then be propagated to higher-level aggregate summaries, e.g., average score at each given position and for the various missense variant types (hydrophobic, polar etc). Representative scatterplots between barcode replicates for a subset would be informative (ideally, with and without forskolin normalization). In addition, it would be interesting to see if sequence content of barcodes correlate with error estimates (e.g. certain barcode sequences might destabilize the transcripts, resulting in artificially lowered scores for a given mutation and vice versa). Error estimates could also be useful, e.g., in ranking the most intolerant amino acids, where ranking is based on the estimate at the more conservative end of a confidence interval. Also, with error estimates, statements like "we obtained measurements for 99.6% (7,800/7,828) of possible missense variants" could be replaced with statements like "we obtained reliable measurements for X% of possible missense variants.

Considering that the output assay as mediated by cAMP, the authors might want to common if the approach is limited to receptors coupling via G-alpha-s.

When the authors discuss which positions are conserved and which are not, it is not always clear whether they mean among ADRB2 orthologs or perhaps across adrenergic receptor subtypes or perhaps for the entire GPCR class A. Which receptors and species are compared? It is also essential to describe the range of species. The authors refer in a couple of places to 55 ADRB2 orthologs (Figure 2 legend, Figure 3—figure supplement 1 legend, subsection “Conservation, EVMutation, and gnomAD”) but do not specify which range of species was included in this data set. For instance, it makes a huge difference if it's mammals or vertebrates.

One of the major findings is the identification of the conserved EL2 motif WxxGxxxC, proposed to work as a 'latch'. It would have been very interesting indeed to see this hypothesis tested in some way, but hopefully this will come in the near future.

Likewise, the observations that distal mutations in the N-terminus and C-terminus lead to constitutive activity invites further studies. Is it possible to say something about this based upon mutagenesis already reported in the literature for beta-2 or other class A receptors? It appears likely that especially the N-terminal mutations may compromise biosynthesis and handling in ER and Golgi, why the caveat should be mentioned early in the manuscript that differences in expression level may explain the observed output results.

The comparison of the latch with two receptors that are closely related to each other (opioid kappa and mu) seems a bit superfluous. It would be more interesting if a few completely different peptide receptors were included in the comparison.

The observation of the EL1 latch has some precedence, see review by Hulme in TIPS, 2013, Figure 3A. Please check if this should be cited.

ADRB2 variants were synthesized in oligonucleotide microarrays split into 8 segments and integrated into the cell line. Additional details on the scheme and numbers/statistics on coverage, library wt representation, and evenness would be important to discuss and show – especially for reproducibility. (Rubin et al., Genome Biology, 2017).

The authors conduct the DMS experiment under four different isoproterenol conditions and normalize measurements to forskolin treatments. Experimental details on the forskolin activation in their assay or reference for this treatment would aid in interpreting the normalization approach.

What exactly distinguishes the globally intolerant clusters (clusters 1 and 2) in Figure 4? It seems there is a tighter range of activity to isoproterenol in cluster 2 than in 1 for all mutations and chemical properties, but does this get ranked differently than cluster 1?

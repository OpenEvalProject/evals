# Peer review - Round 1

Editors:
- Arup K Chakraborty, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33050.014](https://doi.org/10.7554/eLife.33050.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Method for identification of condition-associated public antigen receptor sequences" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor/Senior Editor has drafted this decision to help you prepare a revised submission.

Your manuscript describes a computational pipeline that identifies particular TCR sequences that are over represented in groups of individuals. In effect, it identifies the outlier TCR sequences populations from a computationally determined normal distribution. You go on to show that, based on TCR deep sequencing datasets, this method can retrospectively identify TCRβ chains that are over represented following CMV infections, and TCRβ sequences that have reactivity to defined autoantigens in type 1 diabetes. The manuscript is theoretically interesting, useful, timely, and clearly written. However, we have some significant concerns about the general applicability of this tool and its value for prospective, rather than retrospective, studies. These concerns are listed below and need to be addressed in a revision.

1) Methods to identify outlier populations are understood and statistical approaches to achieve this goal are available. Indeed, a related approach to this question is the basis for lymphoid tumor diagnostic methodologies being pursued by several companies. In what ways is your tool different/better compared to the available methods?

2) Your work is based on small cohorts of patients. HCMV can be responsible for a disproportionate number of TCR clonotypes and can have a stable profile over many years, even by the standards of other chronic infections. So, we wonder whether an attractive feature of this tool, which is its ability to glean information from data on small cohorts will carry over beyond the HCMV setting. Would one need a larger cohort for most disease applications? Is there a theoretical way to estimate what part of the repertoire (in terms of unique clones and their frequencies) has to be devoted to an infectious disease in order for it to be resolved in a given cohort size (maybe a scaling rule)?

3) A general concern is whether this tool will have broad impact. You used TCR sequence data sets of HLA-matched patients, which had already been shown to have T cell expansion to a defined peptide/HLA combination. The approach works if one has HLA-matched subjects, because one would assume in general that different HLA alleles will present a different spectrum of peptides, and that TCR Vgene – HLA interactions impact ligand specificity. Further, a significant element to the approach only works retrospectively; without prior knowledge of the TCR specificity one does not know whether the identified outlier populations are disease-relevant. For example, in Figure 2, there are many outlier sequences (red), which may be noise, may be disease relevant or may be consequences of HLA-biased selection that was not accounted for by the authors computationally-defined normal TCRb distribution. Can the method be useful for prospective studies, or learn new biology in retrospective studies? Perhaps one way to address this question is the following:

Is there any other viral infection for which comparable data is available? For instance, it would be nice if data on viruses like HSV or EBV were available along with data related to acute infection or vaccination (where a method such as this, if applicable, would be incredibly valuable).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Method for identification of condition-associated public antigen receptor sequences" for further consideration at eLife. Your revised article has been favorably evaluated by Arup Chakraborty (Senior editor), a Reviewing editor, and 1 reviewer.

You present an important statistical tool for analyzing TCR sequence diversity. We will soon get to a point where entire human TCR repertoires will be sequenced and then the question is how do we understand this data to assess immune health – your method is an advance that allows us to take steps toward this goal, and is therefore a valuable resource/tool. However, you often confuse TCR with clonotype in the writing of your paper. A TCR β chain sequence is not a TCR clonotype. Throughout the manuscript, you describe what you are analyzing as TCR clonotypes when you are actually referring to independent TCR β sequences. An independent TCR α chain or a TCR β chain sequence is NOT a receptor. Once this point is consistently clarified in the manuscript, your paper will be accepted.

Reviewer #1:

Re-review:

The major concern I have with the method, writing and the inability of this platform to provide a framework for prospective studies is the author's miss-statements (I assume they know better) that a TCR β chain sequence is not a TCR clonotype. Throughout the manuscript, they authors describe what they are analyzing as TCR clonotypes when they are actually referring to independent TCR β sequences. An independent TCRa chain or a TCRb chain sequence is NOT a receptor. The CDR3beta sequence does not equal or even mark a particular T cell clone.

Problem statement that this creates:

Example in the Introduction: the authors argue that there are "Several mechanisms leading to the repertoire overlap. The first mechanism is convergent recombination[…]" This first statement or option is a product of sequencing just the TCRb chain, i.e., there are common rearrangements that occur do to V-J or V-D-J rearrangements that have no or few N-region additions. The second and third "options" are indeed TCRa + TCRb clonotypes, comparing the first possibility to 2 and 3 is comparing apples to oranges.

Due to biases in V(D)J recombination process, the probability of generation of some receptors is very high, making them appear in almost every individual multiple times and repeatedly sampled in repertoire profiling experiments Britanova et al., (2014). This sharing does not result from a common specificity or function of the shared clonotypes and may in fact correspond to cells from the naive compartment in both donors Quigley et al., (2010), or from functionally distinct subsets such as CD4 and CD8 T-cells.

The second possible reason for TCR sequence sharing is specific to identical twins, who may share T cell clones as a consequence of cord blood exchange in utero via a shared placenta Pogorelyy et al., (2017). The third and most interesting mechanism for sharing receptor sequences is convergent selection, in response to a common antigen.

- The terminology makes these types of statements nonsensical. Identical TCR clonotypes will absolutely have the identical antigen-specificity.

Issues that miss-representing TCRb sequences for TCR clonotypes in the general approach being promoted:

The incorrect use of TCR clonotype leads to some particularly difficult to imagine scenarios. For examples, in the reviewer response and within the manuscript, "our method can be used to narrow down the potential candidates for further experimental validation of responsive receptors." (i.e., identify the antigen being recognized). Their idea regarding this approach is to use: "Functional tests (like cultivation with peptides, or cytokine secretion assays) are the ultimate way to confirm specificity of these predicted clonotypes."

Within the cover letter: "We also are careful to note that this method should be used to identify antigen-specific candidates that need to be further verified by other methods. Nevertheless, we believe that identifying candidates for these experiments is extremely useful."

- However, the sequencing and analyses method of the manuscript does not identify the V α chain, with only half of the receptor there is nothing to study further. Thus, there is no method provided that one could identify interesting receptors for prospective studies.

In summary, this is a method to identify outlier populations, for which retrospective data can be superimposed to create a snapshot of an immune response that has already been described using for example pMHC tetramers or other methods.

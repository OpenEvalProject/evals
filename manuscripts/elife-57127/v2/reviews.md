# Peer review - Round 1

Editors:
- Philip A Cole, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57127.sa1](https://doi.org/10.7554/eLife.57127.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study reports a high resolution structure using CryoEM of a PIKK family kinase in complex with a peptide substrate and an ATP analog. It is the first member of this family of protein kinases to be captured at atomic resolution with a peptide substrate. The structural interactions between enzyme and substrate were corroborated with very solid biochemical analysis including a range of kinase assays with various peptides. This work will serve as a model for related kinases including ATM, ATR, DNAPK, and mTOR.

Decision letter after peer review:

Thank you for submitting your article "Structure of substrate-bound SMG1-8-9 kinase complex reveals molecular basis for phosphorylation specificity" for consideration by eLife. Your article has been reviewed by Reviewing/Senior Editor Philip Cole and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Nikolaus Grigorieff (Reviewer #1); Kacper Rogala (Reviewer #2); Michael B Yaffe (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below, although fairly numerous, are meant to address clarity and presentation.

Summary:

Langer et al. elucidate a cryo-EM structure of a human PIKK family member SMG-1-8-9 in complex with a short peptide substrate (from UPF1) and a non-hydrolyzable analog of ATP, AMPPNP. This is an extension of the cryo-EM work that they did in 2019 on apo SMG-1-8-9 (Gat et al., 2019). However, this study is in fact more interesting than the previous work because it captures the SMG1 kinase in a state with its substrate peptide bound, frozen in time just before the actual act of phosphorylation. Importantly, the authors do an extensive characterization of the peptide recognition sequence, and reveal the chemical compatibility of the LSQ sequence and its derivatives for phosphorylation by SMG1. They compare the binding site of SMG1 to other members of the PIKK family and explain the observed differences between them in terms of substrate recognition. Overall, we believe that this work is novel and interesting. In general, the claims are supported by solid data, and the structure is validated with substantial biochemical work. Although we do not think additional experimental work is needed, below we make the following suggestions for revisions to strengthen the manuscript.

Essential revisions:

-The structure and its interpretation seem plausible. However, we wonder if using an 11-amino acid peptide as a substrate captures all the contacts relevant for the kinase specificity that the authors are interested in. Is it possible that the full UPF1 molecule makes tertiary contacts with the kinase that are important for specificity? The authors should consider this possibility and explain why they can rule this out. Related to the above point, the authors state that "there are no extensive interactions between SMG1 and the residues preceding or following the LSQ motif in our structure." It is not clear how they can conclude this from their structure. If this is known from other work, they should cite it.

-The authors seem to have side-stepped the other 3D classes that were generated during data processing. There are at least two classes (center top and center bottom in Figure 1—figure supplement 3) that show extra density that is not present in the final reconstruction presented. That density appears to extend from SMG8's stalk and reach towards the FRB of SMG1. According to Li et al., 2019), this extra density is likely the kinase inhibitory domain (KID) of SMG8. This density also appeared in the authors' previous map of the apo SMG-1-8-9 complex (EMDB 10348), but they avoided discussing it in their previous manuscript (Gat et al., 2019). If the authors feel that delving into this would be too speculative, adding a label and a note to point out what they represent would be helpful.

-A discussion regarding nucleotide binding to SMG9 and its effects on SMG8 binding and SMG1 catalytic activity is lacking. The authors in their previous work revealed a GTP/GDP nucleotide binding pocket in C. elegans SMG1 (Li et al., 2017), and then realized that human SMG9 co-purifies with bound ATP instead of GTP (Gat et al., 2019). Can human SMG1 also associate with GTP/GDP? In Figure 1—figure supplement 4 of this manuscript, the authors talk extensively about the adaptations for adenine vs guanine binding. This topic appears to be rather confusing in the field, so please include a short discussion that deals with the nucleotide-binding matter, including the mutagenesis study from another SMG-1-8-9 structure paper by Li et al., 2019.

-The methods are not sufficiently detailed, and it would be challenging to reproduce the authors' work by simply following them.

-Figure 3A and Figure 3 legend, particularly the statement that sequence logo letter size reflects the frequency of occurrence is not technically correct. True sequence logos use bit scores that typically do not reflect the frequency of occurrence but rather indicate the information content (in bits) that is being provided by each residue in that position in terms of the informational entropy content in each position of a motif, at least as originally described by Tom Schneider and Mike Stephens in 1990. A good review of the concept is found in Crooks et al., 2004. (http://www.genome.org/cgi/doi/10.1101/gr.849004). The authors should clarify how they are using the sequence logos here.

-Regarding the data in Figure 3B described in subsection “Crucial recognition of a glutamine residue at +1 position of the UPF1 consensus motif”, the claims of "peptide library" and "systematically" in the text go a bit beyond the data, since they are really looking at a small series of peptides, not a complete library of all residues in that position. The data is solid, and there is no need to do anything more, other than tone down the claims of this being a 'library'. We think the use of the term 'library' in Figure 4 and its description is fine, since in that case the authors really are looking at the set of all possible X-SQ sites that exist in UPF1.

-The authors may want to expound a bit more on the similarity and differences in the hydrophobic cage between SMG1 and other PIKKs, particularly the Leu to Glu activation loop substitution seen in mTor (Figure 2—figure supplement 1B). This is important because the optimal kinase motif for mTor is NOT SQ as it is in ATM, ATR and DNA-PK, but rather more like SF or SP (see Figure 2 in Hsu et al., 2011).

-Subsection “Preferred recognition of a leucine residue at -1 position of the UPF1 consensus motif” and Figure 4C- presumably the point the authors are making is that C-terminal SQ motifs are better phosphorylated than the N-terminal ones because they are better matches to the hydrophocis-Ser-Gln motif. Perhaps they can state this conclusion a bit more clearly.

-Similarly, it appears from Figure 2C that the Gln side chain is actually helping stabilize the activation segment conformation. Is this correct, and if so, shouldn't this be alluded to somewhere in the Results section?

-Regarding the catalytic mechanism, as the authors have a (not so common) ternary complex protein kinase crystal structure containing both a peptide substrate and a nucleotide substrate, it would be nice to say a bit more about the relevance to potential phosphoryl transfer transition states. There has been a classical discussion in the field among physical organic chemists and enzymologists about whether phosphoryl transfers involving monoesters like the γ phosphate of ATP are more associative or dissociative. High resolution structures have been used to inform these discussions. For examples, please see: PMID:9408938, PMID:21513457, PMID:25399640

# Peer review - Round 1

Editors:
- Magnus Nordborg, Austrian Academy of Sciences Austria

Reviewers:
- Amy L Williams, Cornell University United States
- Shai Carmi, The Hebrew University of Jerusalem Israel

## Review text

DOI: [10.7554/eLife.51810.sa1](https://doi.org/10.7554/eLife.51810.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript shows that genetic databases, like other databases, are vulnerable to being (ab)used in a manner not foreseen by their owners. The presented scenarios are very realistic and I sincerely hope that this article will spur both genetic service firms and politics into action.

Decision letter after peer review:

Thank you for submitting your article "Attacks on genetic privacy via uploads to genealogical databases" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Magnus Nordborg as the Reviewing Editor and Mark McCarthy as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Amy L Williams (Reviewer #1); Shai Carmi (Reviewer #2). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Direct-to-consumer genetics services are increasingly popular for genetic genealogy, with millions of customers as of 2019. Several DTC genealogy services allow users to upload their own genetic data in order to search for genetic relatives. This paper demonstrates that such services can also be exploited to reveal much about the genome of individuals in the database, without their consent, and with potentially adversarial consequences.

Essential revisions:

A major concern was whether you intend this paper as a hypothetical discussion, or as a real-world demonstration. The latter would require real-world examples. Either way, it would be necessary to try to specify the conditions under which this work. For example, your IBD baiting method depends sensitively on the algorithms used by the provider. Thus, at a minimum, we would like to see a general discussion of the limitations of these exploits, and of the parameters that effect their efficacy.

Needless to say, you should also discuss the recent work of Ney et al., which you are aware of.

Reviewer #1:

Edge and Coop outline several means of inferring genotypes of individuals in genetic databases that allow users – specifically an attacker – to upload genetic data. There are three such attacks: (1) IBS tiling, wherein an attacker utilizes inferred IBS regions to N (known) samples to reconstruct the genotypes of others in the database in a genome-wide fashion. (2) IBS probing, with the aim of inferring genotypes at a specific locus (for example, the APOE locus). And (3) IBS baiting, with a more systematic form of probing that, given multiple uploads, may be able to collect enough genotypes to allow imputation of a person's common variants genome-wide.

The paper is of broad interest given the robust interest in direct-to-consumer genetic testing and the advent of long-range familial searches by law enforcement. The authors have responsibly handled their discoveries, notifying the various companies that host databases vulnerable to these attacks.

Before it can be published a few technical topics that should be addressed are:

1) To perform IBS baiting effectively, the (unphased) IBS detector would need to break segments at opposite homozygous genotypes. However, in practice most such detectors would likely be tolerant to errors, and therefore may not break the segments in the fashion the text assumes. This seems like it may pose a serious issue to such an attack, and this merits more careful consideration.

2) The Supplementary Figure 4 legend says, "All other arguments were kept at their default values. Calling IBS without respect to genotype phase returns many IBS segments, but less can be learned about each segment via tiling than if haplotype phase is respected." Note that services that I'm aware of do not provide phase to the users, nor allow users to upload phased data. (Please say if this is not the case.) Given this, it's hard to make use of the potential benefits of phased data. In general, this issue merits a more prominent mention – the fact that, if phase were known, the amount of information learned by an attacker is greater, and that (unless services give this information), it's hard to envision how an attacker could put this into practice.

3) "(We consider some alternative IBS reporting procedures in the supplement.)" Is this about the supplementary figures? If so, perhaps cite them. I wasn't sure if there was text that I missed?

4) Optionally, the Discussion may wish to expand on the proposals that inhibit genealogical research, which end users may prefer not to have implemented. Points 2, 4, and 5 (since inferring other relatives' relationships can be useful) fall in this category.

Reviewer #2:

Conflict of interest:

The authors have shared the manuscript with me a few weeks ago. I have discussed my thoughts with the authors and they have revised their manuscript according to some of my comments, acknowledging me at the end of the paper. The review below is a slightly edited and expanded version of the remaining comments.

General assessment:

Edge and Coop describe a method for breaching privacy of genomes deposited in genetic genealogy matching services. The key idea is that a genetic match between a (known) uploaded genome and a target genome reveals some DNA sequence of the target. This can be exploited to recover large proportions of the target's genome. This is a novel and innovative approach. The manuscript is very interesting and thought provoking and the results are important. The analysis is overall sound (but see the points below). I am certain that the results will have major implications on genetic genealogy, genetic privacy, and beyond.

1) A result I find intriguing is the high proportion of the genome that can be covered by IBS tiling, which is comparable only to what was previously seen in founder populations. I suggest the following. (All the requested data should be already available to the authors or require very quick experiments.)

a) Show a breakdown of the coverage by ethnicity (at least for the main ethnicities), to make the results a bit more comparable to previous studies.

b) Further emphasize the message that segments need not be IBD (identity-by-descent) to allow privacy breaching – rather, IBS (identity-by-state) is good enough. This explains to some extent why the proportions of genome covered are so high, even though these are (mostly) not founder populations.

c) I think the results of Figure 2—figure supplement 3 are important, and should perhaps be reported as the main results. The reason is that when running Germline in haploid mode with no errors allowed, we are guaranteed no mismatches between the target and the (known) uploaded genome. In other words, we have an exact match to at least one haplotype of the target. (The authors can even improve performance easily by using a diploid mode but allowing no errors. Germline would still require a perfect match, but would allow phasing errors if they happen between blocks.) If the authors choose not to change the order of figures, I would recommend to at least report the mismatch rate between the haplotypes that were found to be matching by RefinedIBD in the main analysis (Figure 2).

d) Regarding Supplementary Figure 4, I think this figure might be somewhat misleading. The problem with the approach taken to generate that figure (if I'm not mistaken) is that Germline will not try to match any sites where either the target or the uploaded genome are heterozygous. Thus, the coverage is likely inflated – there could be entire "covered" segments that provide very little information on the target. At the very least, the uploaded genome should be made artificially homozygous, so that we are guaranteed to have information on the homozygous genotypes of the target.

2) It will be important to evaluate the IBS tiling method against a very simple "null", in which each allele is predicted to be the major (more frequent) allele. In other words, the outcome would be not the proportion of the genome covered, but the proportion of alleles of the target correctly inferred, and this outcome should be compared between IBS tiling and just using the major allele. While this experiment may take a little time (but I believe no more than a few days), I believe it is essential, because otherwise it is difficult to evaluate the success of the proposed method.

3) I am not confident whether these very elegant results form a practical and immediate risk of privacy, or whether the paper is more of a proof of concept. The biggest problem is with IBS baiting. The success of this approach relies on an IBD detection algorithm that is very simple minded. It is not clear to me whether any of the companies is actually using such an algorithm. But more generally, the authors did not demonstrate an actual recovery of genomic material from a genetic genealogy service using any of their methods. Of course, they would not want, and should not, violate the terms and conditions of any company. But I think that if using research genomes (such as 1000 Genomes) or their own genomes, and limiting the experiment in duration and scale, this would be legitimate. Or the authors could even explicitly ask the companies' managements for permission.

This is not to say that the article is not worthwhile without such experiments. On the contrary, the paper describes a very novel approach, and it would be extremely important and urgent that the proposed techniques become known to all stakeholders in personal genomics, both from the industry and from the academia, as well as the actual participants. Also, additional experiments may take too much time or be outside the scope of the present paper.

But as happens frequently with this kind of papers, once they are published, the media and the general public cannot get to the bottom of such subtle nuances (even if authors do their very best). I expect the paper will be very widely covered, and with some likelihood, it could develop into a total media circus and trigger panic. I think that would be an unfortunate consequence, unless there is a real, tangible risk of privacy breaching. If the risk is more theoretical in nature, it will be important to say so explicitly (and possibly drop the part about the letters to the representatives of the companies, which is only going to amplify the drama).

Reviewer #3:

Edge and Coop describe a battery of methods that seek to recover parts of a personal genome through segment matching queries in a direct-to-consumer database that facilitates uploads. Specifically, the authors describe methods for tiling the hacked genome with matched segments, probing it for the genotype at a particular locus, or baiting it to match contrived genomes, designed to recover the genotype at a particular site.

The paper is technically sound. Methodologically, it puts together ideas that had been floated, and actually evaluates them rigorously. In the context of the genetic privacy field, this constitutes and advancement.

1) This reviewer believes that genetic privacy as a whole is overblown. The impacts of violating it are not substantial, and accepting such work in broadly read venues panders to irrational fears thus does science a disservice. While I don't fault the authors for pushing their work to a visible journal, making this more of a comment to the editor, I would nevertheless welcome the authors' rebuttal. Specifically, I would challenge the statements in the last paragraph of the Discussion regarding trait-predictability of traits. These are upper-bounded by the prediction accuracy implied by SNP heritability (accuracy which is markedly lower than the SNP heritability itself). More practically, the likely improvement in prediction does not mean convergence of prediction even to that bound. Worse, given the non-genetic data trace of individuals today, with more precious predictive value, genetic privacy is a distraction. An example ad absurdum, every street camera recovers my height better than my genome would.

2) The paper is somewhat thin in results (basically, Figures 2 and 3). In particular, Section 2.3 is falsely appearing under Results, whereas it only describes a method, without even applying it. This defeats the entire purpose of the manuscript, of actually demonstrating the attacks and quantifying their effectiveness. One quantitative question relevant to (defending against) the baiting attack has to do with feasibility of assembling all-het segments from naturally-occurring human haplotypes of chip SNPs. There are back-of-an-envelope reasons to assume those would not be long enough for the described attack, but actual data would be reassuring and consistent with the nature of contributions of this manuscript.

3) Relatedly, I am specifically concerned regarding the baiting security loophole being practical, as the authors' description of IBS baiting relies on a straw man IBS detector that they construct to have that weakness. As the authors point out, many actual detectors would not willy-nilly extend each segment till conflicting homozygous on both ends, or require some information content to seed a match between segments. Baiting may still be possible, but likely more complicated and potentially impractical.

4) The results reported are all w.r.t. the general European population. It is important to report the (different) results for other continental ancestries, and, on the other hand, in bottleneck populations.

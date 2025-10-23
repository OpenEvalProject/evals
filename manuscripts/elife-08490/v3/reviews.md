# Peer review - Round 1

Editors:
- Richard A Neher, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08490.022](https://doi.org/10.7554/eLife.08490.022)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for choosing to send your work entitled “Viral dark matter and virus-host interactions resolved from publicly available microbial genomes” for consideration at eLife. Your full submission has been evaluated by Diethard Tautz (Senior editor) and three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the decision was reached after discussions between the reviewers. One of the three reviewers, Ken Stedmann, has agreed to share his identity.

All reviewers agreed that virus diversity and ecology are very important topics that deserve more attention and new approaches. The large set of putative viral sequences is impressive and the patterns of host association are intriguing, but we felt that the analysis didn't deliver much novel insight into the evolution of “viral dark matter”. A more in depth analysis covering multiple scales of evolution would be necessary to make significant progress in this direction. As it stands, the manuscript describes in broad terms a data set generated with a tool that is supposed to be published elsewhere. The usefulness of the data set as a resource for others remains limited without a feature rich data base that allows convenient exploration and access. Hence we don't feel that your manuscript is appropriate for publication as a Research article in eLife.

Reviewer #1:

Roux and colleagues analyze a large set of putative viral sequences mined from published bacterial and archaeal genomes using a software that is described in a manuscript that is currently under review elsewhere (and provided to the reviewers). The method seems sound and I think the majority of the reported viral sequences are genuine. The authors use this large set (10 fold larger than existing data bases) to investigate patterns of host adaptation, host range, and virus taxonomy.

The main results reported are:

(i) > 12000 sequences fall into ∼600 clusters, half of which contain known viruses;

(ii) Viruses are well adapted to their hosts, across virus types and proteins;

(iii) Viruses are mostly host specific and virus/hosts define modules.

These results make sense and are mostly expected, the novel element here is to be able to do it on a massive scale. I have a couple of other comments/criticisms:

1) Only the more reliable predictions were used. How do things change when less stringent criteria are used?

2) Is there a sense of saturation: if one had done the study a few years ago with fewer genomes, how many clusters would have been found? Are some parts of the bacterial world exhausted, where do the new sequences come from?

3) What can be learned from this for future efforts to detect viruses? How should sequencing be targeted?

4) Coinfection: the number of viruses per genome seem compatible with random. What can really be learned from this? Does this reflect the number of concomitant infections, or the number of genomes deposited in this genome in the past (like endogenous retroviruses in mammals)?

5) How are others supposed to use this? A data set of this size needs tools to analyze. Are the authors going to develop a data base with interactive views etc?

6) This is a computational study. I expect the scripts and code to be deposited.

Reviewer #2:

In this manuscript the authors describe an approach to increase our knowledge about prokaryotic viruses (phages) by mining prokaryotic genomes available in public repositories. It is an excellent idea that makes a lot of sense and is badly needed to increase the knowledge about the sequence space of phages presently very biased and incomplete. It can also provide a great contribution into one of the conundrums of phage biology, the infection range without the bias of culture. However, I have mixed feelings about this manuscript. On the one hand it is very comprehensive including all genomes in repositories (including many draft genomes) but the results are a bit disappointing and provide very little novelty. That the pattern of infection at large phylogenetic scale will be modular was largely expected from classical work with cultures. But the most relevant question is whether at short phylogenetic distances is nested what is left unanswered. Maybe a problem that is general to these “big data” analysis is the gross level of detail. I wonder why the authors do not provide analysis at the fine resolution level i.e. phages detected within a single species or genus. At the broad level analysed here most of the results are very predictable from classic approaches. The use of draft genomes and the possibility of discriminating plasmids from phages is another question that is left untouched in both this manuscript and the previous submission. There is a gradient in nature between infective phages and conjugative elements and establishing the borderline might be risky.

In summary I missed some more fine grained analysis of examples in this big data approach.

Reviewer #3:

I find this to be a very well-written report of the application of a new bioinformatic tool (VirSorter) developed by some of the authors. This tool has been applied to data mining of the available and rapidly growing genomic datasets and thereby has increased the number of putative (mostly partial) viral genomes by ten-fold. Due to association with both known genomes and SAG genomes from known sources, the analysis allowed identification of potential viruses in hosts for which no known viruses are currently available. This is clearly a boon to researchers working on these organisms. I find the tetranucleotide analysis of viral genomes in order to possibly identify hosts for these viruses to be particularly attractive and plan on using it in my own research.

I am not convinced of the premise stated in the title and Abstract that this analysis provides much insight into viral dark matter or virus-host interactions. This tool enables further investigations that would allow that insight, which would otherwise be extremely difficult if not unfeasible.

I wonder if the manuscript describing the development and testing of the tool (which was submitted together with this manuscript) could be combined into one manuscript.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled “Viral dark matter and virus-host interactions resolved from publicly available microbial genomes” for further consideration as a Tools and resources article at eLife. Your revised article has been favorably evaluated by Diethard Tautz (Senior editor) and a Reviewing editor. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Data availability: given that this is now being considered as a Tools and resources article, we feel that the data availability section should be more prominent. We suggest to move the availability section up (possibly before the conclusions) and provide a little bit more detail. iVirus.us itself seems like a rather hollow shell – clicking on data access yields a 502 bad gateway error. As far as I can tell, everything happens within the discovery environment of iPlant for which registration is necessary. Please elaborate a little bit. The MetaVir environment seems useful, but some of the MetaVir analysis haven't completed yet. In addition, we think that the “richly annotated genbank files” (promised in the rebuttal letter) should be made available not only on the author's website but uploaded to a big-data repository such as data dryad.

2) It seems the authors have misunderstood the request for making the scripts available. We were not asking for the VirSorter scripts, but the scripts that analyze the VirSorter data set to produce figures and results of the paper. Those scripts provide the most accurate description of the methods, and in the interest of reproducibility, they should – whenever possible – be made available. The preferred place would be a separate GitHub repository.

3) Host association figure: We continue to be underwhelmed by this figure. There are lots of lines which clearly fall into a handful of modules, but within these modules it is pretty hard to see what is going on. Maybe a two-way clustering would be more insightful. Consider a distance matrix d_ij, where d_ij is the fraction of sequences in viral cluster (VC) i that come from genomes of host phylum j, maybe normalized for the abundance of genomes from phylum j. Then cluster this matrix both by VC and host, similar to RNA-seq being clustered by gene and tissue. The modules should show up as blocks on the diagonal, while promiscuous affiliations are off-diagonal terms. What exactly the distance matrix d_ij should be requires some thought and there are probably better choices then this proposal. But if something like this would work out, it could be more informative than the current figure. Keeping one as a supplement of the other could be a good solution.

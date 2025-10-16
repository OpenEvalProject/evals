# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90782.4.sa0](https://doi.org/10.7554/eLife.90782.4.sa0)

This study presents valuable data on the antigenic properties of neuraminidase proteins of human A/H3N2 influenza viruses sampled between 2009 and 2017. The antigenic properties are found to be generally concordant with genetic groups. Compared to a previous version, additional analyses have strengthened the work, with solid evidence supporting the claims of the authors.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90782.4.sa1](https://doi.org/10.7554/eLife.90782.4.sa1)

Summary

The authors investigated the antigenic diversity of recent (2009-2017) A/H3N2 influenza neuraminidases (NAs), the second major antigenic protein after haemagglutinin. They used 27 viruses and 43 ferret sera and performed NA inhibition. This work was supported by a subset of mouse sera. Clustering analysis determined 4 antigenic clusters, mostly in concordance with the genetic groupings. Association analysis was used to estimate important amino acid positions, which were shown to be more likely close to the catalytic site. Antigenic distances were calculated and a random forest model used to determine potential important sites.

This revision has addressed many of my concerns of inconsistencies in the methods, results and presentation. There are still some remaining weaknesses in the computational work.

Strengths

(1) The data cover recent NA evolution and a substantial number (43) of ferret (and mouse) sera were generated and titrated against 27 viruses. This is laborious experimental work and is the largest publicly available neuraminidase inhibition dataset that I am aware of. As such, it will prove a useful resource for the influenza community.

(2) A variety of computational methods were used to analyse the data, which give a rounded picture of the antigenic and genetic relationships and link between sequence, structure and phenotype.

(3) Issues raised in the previous review have been thoroughly addressed.

Weaknesses:

Some concerns regarding the robustness of the machine learning model and potential overfitting remain.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90782.4.sa2](https://doi.org/10.7554/eLife.90782.4.sa2)

Summary:

The authors characterized the antigenicity of N2 protein of 43 selected A(H3N2) influenza A viruses isolated from 2009-2017 using ferret and mice immune sera. Four antigenic groups were identified, which the authors claimed to be correlated with their respective phylogenic/ genetic groups. Among 102 amino acids differed by the 44 selected N2 proteins, the authors identified residues that differentiate the antigenicity of the four groups and constructed a machine-learning model that provides antigenic distance estimation. Three recent A(H3N2) vaccine strains were tested in the model but there was no experimental data to confirm the model prediction results.

Strengths:

This study used N2 protein of 44 selected A(H3N2) influenza A viruses isolated from 2009-2017 and generated corresponding panels of ferret and mouse sera to react with the selected strains. The amount of experimental data for N2 antigenicity characterization is large enough for model building.

Weaknesses:

One weakness is the use of double-immune ferret sera (post-infection plus immunization with recombinant NA protein) or mouse sera (immunized twice with recombinant NA protein) to characterize the antigenicity of the selected A(H3N2) viruses. Conventionally, NA antigenicity is characterized using ferret sera after a single infection. Repeated influenza exposure in ferrets has been shown to enhance antibody binding affinity and may affect the cross-reactivity to heterologous strains (PMID: 29672713). The increased cross-reactivity is supported by the NAI titers shown in Table S3, as many of the double immune ferret sera showed the highest reactivity not against its own homologous virus but to heterologous strains. In response to the reviewer's comment, the authors agreed the use of double-immune ferret sera may be a limitation of the study.

Another weakness is that the authors used the newly constructed a model to predict antigenic distance of three recent A(H3N2) viruses but there is no experimental data to validate their prediction (eg. if these viruses are indeed antigenically deviating from group 2 strains as concluded by the authors). Leaving out data from some strains for testing is a useful check, but due to phylogenetic correlations in the data the generalizability of the machine learning is not guaranteed.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90782.4.sa3](https://doi.org/10.7554/eLife.90782.4.sa3)

Summary:

This paper by Portela Catani et al examines the antigenic relationships (measured using monotypic ferret and mouse sera) across a panel of N2 genes from the past 14 years, along with the underlying sequence differences and phylogenetic relationships. This is a highly significant topic given the recent increased appreciation of the importance of NA as a vaccine target, and the relative lack of information about NA antigenic evolution compared with what is known about HA. Thus, these data will be of interest to those studying the antigenic evolution of influenza viruses. The methods used are generally quite sound, though there are a few addressable concerns that limit the confidence with which conclusions can be drawn from the data/analyses.

Strengths:

-The significance of the work, and the (general) soundness of the methods.

-Explicit comparison of results obtained with mouse and ferret sera

Weaknesses:

- Machine learning analyses neither experimentally validated nor shown to be better than simple, phylogenetic-based inference.

# Peer review - Round 1

Editors:
- Jennifer Flegg, The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90888.3.sa0](https://doi.org/10.7554/eLife.90888.3.sa0)

The study is an important advancement to the consideration of antimalarial drug resistance: the authors make use of both modeling results and supporting empirical evidence to demonstrate the role of malaria strain diversity in explaining biogeographic patterns of drug resistance. The theoretical methods and the corresponding results are compelling, with the novel model presented moving beyond existing models to incorporate malaria strain diversity and antigen-specific immunity. This work is likely to be interesting to malaria researchers and others working with antigenically diverse infectious diseases.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90888.3.sa1](https://doi.org/10.7554/eLife.90888.3.sa1)

Summary:

The paper is an attempt to explain a geographic paradox between infection prevalence and antimalarial resistance emergence. The authors developed a compartmental model that importantly contains antigenic strain diversity and in turn antigen-specific immunity. They find a negative correlation between parasite prevalence and the frequency of resistance emergence and validate this result using empirical data of chloroquine-resistance. Overall, the authors conclude that strain diversity is a key player in explaining observed patterns of resistance evolution across different geographic regions.

The authors pose and address the following specific questions:

1. Does strain diversity modulate the equilibrium resistance frequency given different transmission intensities?

2. Does strain diversity modulate the equilibrium resistance frequency and its changes following drug withdrawal?

3. Does the model explain biogeographic patterns of drug resistance evolution?

Strengths:

The model built by the authors is novel. As emphasized in the manuscript, many factors (e.g., drug usage, vectorial capacity, population immunity) have been explored in models attempting to explain resistance emergence, but strain diversity (and strain specific immunity) has not been explicitly included and thus explored. This is an interesting oversight in previous models, given the vast antigenic diversity of Plasmodium falciparum (the most common human malaria parasite) and its potential to "drive key differences in epidemiological features".

The model also accounts for multiple infections, which is a key feature of malarial infections, with individuals often infected with either multiple Plasmodium species or multiple strains of the same species. Accounting for multiple infections is critical when considering resistance emergence, as with multiple infections there is within-host competition which will mediate the fitness of resistant genotypes. Overall, the model is an interesting combination of a classic epidemiological model (e.g., SIR) and a population genetics model.

In terms of major model innovations, the model also directly links selection pressure via drug administration with local transmission dynamics. This is accomplished by the interaction between strain-specific immunity, generalized immunity and host immune response.

Weaknesses:

The authors emphasize several model limitations, including the specification of resistance by a single locus (thus not addressing the importance of recombination should resistance be specified by more than one locus); the assumption that parasites are independently and randomly distributed among hosts (contrary to empirical evidence); and the assumption of a random association between the resistant genotype and antigenic diversity. However, each of these limitations are addressed in the discussion.

Did the authors achieve their goals? Did the results support their conclusion?

Returning to the questions posed by the authors:

1. Does strain diversity modulate the equilibrium resistance frequency given different transmission intensities? Yes. The authors demonstrate a negative relationship between prevalence/strain diversity and resistance frequency (Figure 2).

2. Does strain diversity modulate the equilibrium resistance frequency and its changes following drug withdrawal? Yes. The authors find that, under resistance invasion and some level of drug treatment, resistance frequency decreased with the number of strains (Figure 4). The authors also find that lower strain diversity results in a slower decline in resistant genotypes after drug withdrawal and higher equilibrium resistance frequency (Figure 6).

3. Does the model explain biogeographic patterns of drug resistance evolution? Yes. The authors find that their full model (which includes strain-specific immunity) produces the empirically observed negative relationship between resistance and prevalence/strain diversity, while a model only incorporating generalised immunity does not (Figure 8).

Utility of work to others and relevance within and beyond the field?

This work is important because antimalarial drug resistance has been an ongoing issue of concern for much of the 20th century and now 21st century. Further, this resistance emergence is not equitably distributed across biogeographic regions, with South America and Southeast Asia experiencing much of the burden of this resistance emergence. Not only can widespread resistant strains be traced back to these two relatively low-transmission regions, but these strains remain at high frequency even after drug treatment ceases.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90888.3.sa2](https://doi.org/10.7554/eLife.90888.3.sa2)

Summary:

The evolution of resistance to antimalarial drugs follows a seemingly counterintuitive pattern, in which resistant strains typically originate in regions where malaria prevalence is relatively low. Previous investigations have suggested that frequent exposures in high-prevalence regions produce high levels of partial immunity in the host population, leading to subclinical infections that go untreated. These subclinical infections serve as refuges for sensitive strains, maintaining them in the population. Prior investigations have supported this hypothesis; however, many of them excluded important dynamics, and the results cannot be generalized. The authors have taken a novel approach using a deterministic model that includes both general and adaptive immunity. They find that high levels of population immunity produce refuges, maintaining the sensitive strains and allowing them to outcompete resistant strains. While general population immunity contributed, adaptive immunity is key to reproducing empirical patterns. These results are robust across a range of fitness costs, treatment rates, and resistance efficacies. Given sufficient antigenic diversity and high transmission, sensitive parasites remain in circulation even when there is no cost to resistance. This work demonstrates that future investigations cannot overlook adaptive immunity and antigenic diversity.

Strengths:

Overall, this is a very nice paper that makes a significant contribution to the field. It is well-framed within the body of literature and achieves its goal of providing a generalizable, unifying explanation for otherwise disparate investigations. The model is innovative. The approach is elegant and rigorous, with results that are supported across a broad range of parameters when considered within an equilibrium setting. Their exploration of geographical patterns of resistance makes the results of their simulations even more compelling. As such, this work will likely serve as a foundation for many future investigations.

Weaknesses:

Although the authors model resistance invasion, it does not align with empirical observations of the spread of resistance. For example, Plasmodium's mutation rate and population size mean that mutations providing chloroquine resistance should arise repeatedly even within a single infection. Nevertheless, Africa remained free of chloroquine resistant strains until a lineage was introduced from Asia. Upon introduction, it spread across the continent within ten years. The difference between the fate of chloroquine resistance originating in Africa versus chloroquine resistance originating in Asia cannot be attributed to changes in population immunity and treatment.

The source of this disparity may be in part attributable to the use of a deterministic, compartmental model, as the authors mention in the discussion. Strains are not explicitly modeled. This means that in terms of the distribution of strain diversity, the resistant and the sensitive compartments are identical, and the locus determining resistance is equally distributed across all strain backgrounds. However, substantial rates of linkage disequilibrium and clonal reproduction are found even in high transmission settings. The model assumptions may be met at equilibrium, but are not appropriate for most scenarios involving the invasion of a rare mutation.

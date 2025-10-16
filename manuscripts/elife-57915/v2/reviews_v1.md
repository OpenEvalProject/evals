# Peer review - Round 1

Editors:
- Eva Top, University of Idaho United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57915.sa1](https://doi.org/10.7554/eLife.57915.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Integrative Conjugative elements (ICEs) play an important role in bacterial adaptation as they can horizontally transfer phenotypic traits between bacteria, ranging from biodegradation of aromatic compounds to antibiotic resistance and virulence. Their low rate of excision from the chromosome and transfer to other cells has been attributed to the existence of two mutually exclusive stable states within the population: the transfer-competent and non-active state. For a particular family of these ICEs, ICEclc, the regulatory basis for the activation of this so-called bistable transfer competence pathway has remained largely elusive. This paper elegantly combines various genetic tools and stochastic modeling to identify these regulatory mechanisms, discovered a transcription factor that is part of a new regulator family, and showed that the feedback loop they described acts as a converter of a unimodal input to a bistable output. It will be interesting to learn from future studies how important biological bistability is in the horizontal transfer of genes via conjugation mediated by various plasmids and ICEs.

Decision letter after peer review:

Thank you for submitting your article "An analog to digital converter controls bistable transfer competence of a widespread integrative and conjugative element" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Eva Top as the Guest Editor and Reviewer #1, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Rafael Silva-Rocha (Reviewer #3).

The reviewers have discussed the reviews with one another and the Guest Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This is a very thorough and elegant study characterizing the different components of the regulatory cascade governing the bistable switch between non-active and transfer competent cells of Pseudomonasputida carrying the Integrative and Conjugative Element ICEclc. The authors used a number of promoter reporter constructions together with mathematical modeling to investigate the key regulatory components of the ICEclc conjugative element in P. putida. They developed an original conceptual mathematical model to test several hypotheses and then tested them experimentally. They demonstrated that the feedback loop regulating the third node of the cascade maintains production of the regulator during a longer period, which enables the activation of the transfer competence pathway (referred as an "analog to digital converter"). Such regulation is likely widespread in other gamma- and beta-proteobacteria.

Essential revisions:

1) Along with the description of the underlined mechanisms controlling this process, a novel transcription factor (BisR) was described. Perhaps the new regulator could be emphasized more in the Abstract. The work is very complete and well-performed. The authors do a nice job of walking the reader through the various genetic manipulations that were needed to draw the conclusions on a complex regulatory system, especially in the first part of the Results.

2) The manuscript could be improved as a publication for eLife if the authors argue more than they do now about the general interest of their work, the possible importance of these elements in pathogens, and respond to the few methodological issues raised. A few particular suggestions are made below.

3) Since the clc element transfers by conjugation much like conjugative plasmids, and several plasmids, like those of the IncF family, also seem to transfer only from a limited number of cells (or at least the rates of transfer are very low), is there any information on whether or not conjugation mediated by some groups of plasmids may also be controlled by such a complex system? Given the broad readership of eLife, it would be helpful to broaden the discussion to horizontal (or at least conjugative) transfer of other genetic elements.

4) Though the role of RpoS is intriguing, and suggests some kind of stress response. Can more be said about that in this study, even though it was not the focus but seems to be critical?

5) Subsection “A new regulator BisDC is the last step in the activation cascade”: I did not quite understand at first why complementation of a bisD deletion mutant with bisCD did not result in similar frequencies of transfer as in the wild-type or other deletion mutants. It would be helpful to elaborate a bit more on this concept of 'reinforcement' at this stage in the paper, more specifically how these findings led to that conclusion. Later on, when the positive feedback is demonstrated, it would be helpful to go back and explain this result.

6) The only place where I was a bit lost during the first read-through was the evidence of a bistable output (see below). I think the average reader will be puzzled by the fact that you equate bistable with 'digital' and a single signal with 'analog'. Some explanation is warranted here. Moreover, is this the only circuit working as analog-to-digital converter in bacteria? More comparison to other systems in bacteria was missing. Can you elaborate features that seem unique so far in ICEclc and those that are similar to other systems.

7) In general terms, the authors did not put much emphasis on the role of AlpA on the modulation of the circuit. What is this element? Which could be the potential mechanisms for its effect on PalpA? It is clear this element is relevant for the systems, but this has been only superficially mentioned in the work. It would strengthen the work if this gene would be investigated a bit more, at least by bioinformatics.

8) The authors exploit the phylogenetic distribution of ICEclc in several organisms. Have this element (or similar) been described associated with pathogenesis or antibiotic resistance? It was mentioned early at the Introduction the association of ICE elements with antibiotic elements, but has the key regulatory elements of ICEclc been identified in pathogenic bacteria or associated with virulence? This information would enhance the general interest of the work beyond environmental bacteria and biodegradation.

9) Why do the authors use 75th of relative fluorescence? What is the rational for that? What would happen if relative fluorescence for all cells were used?

10) The authors used different single-copy reporter systems to investigate promoter activity. For miniTn5, 3 independent clones were used. Yet, even in this case the system will not be isogenic. It would be better to have all reporter systems using the same insertion locus, such as miniTn7, to have a faithful composition between strains. In terms of methodology, for me it’s is the only concern that I have.

11) One concern is that the authors used two approaches to decipher the regulatory cascade of this ICE. The first one relied on the mutagenesis of putative regulator genes of ICEclc and complementation by genes cloned in plasmids. The second one consisted in the ectopic expression of individual and combinations of suspected regulatory elements in a host without ICEclc and study of the expression of single chromosomal copy of transcriptional fusions. Both methods rely on ectopic expression of the regulator genes and thus in an "off-ground" analysis, i.e. not in the in situ context of transcription of ICE genes. Thus potential regulation elements can be missed: secondary structures of long RNA transcripts, competition between regulators, dosage of regulators versus promoters etc.

12) The authors should give more explanations regarding their choices to feed the conceptual mathematical model: why choosing a mean of eight molecules for BisDC and TciR (is there a change if this value is changed)? Does it rely on particular biological data (level of production of proteins?)? Why choosing this particular binomial distribution for the other proteins? What does "bin size=1" (indicated on the figure) mean? What does the bracket indicate on panel 2? Why not feeding the model with real biological data in particular affinities of the regulator for the targeted promoters (to get values for A1/binding and A2/unbinding of regulators)?

13) Although key regulators of ICEclc have been characterized, the full cascade of regulation is not completely deciphered (as stated in the Discussion): role of AlpA, of RpoS, mechanism of reinforcement present in wild-type configuration of the ICE and not restored by in trans induction of plasmid-clones bisDC. The authors should make it clear to the reader that these are still outstanding issues that require future work.

14) Such regulation appears specific to ICEclc (even if such mobile elements can be found in several bacterial genus, not only in Pseudomonas). In addition, since the regulation cascade is complex and involves several regulators, the manuscript is quite long and requires considerable effort and concentration for the reader (even for a specialist). The authors should take a fresh look and try to really guide the reader through the steps, be as succinct as possible, and not make the manuscript any longer than it already is, in spite of all these suggestions for clarification.

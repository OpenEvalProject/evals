# Peer review - Round 1

Editors:
- Fernán Agüero, https://ror.org/02h7fsz12 Universidad Nacional de San Martín Argentina

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104547.2.sa0](https://doi.org/10.7554/eLife.104547.2.sa0)

This study presents an important methodological advance to improve the sensitivity of PCR for detecting Trypanosoma cruzi in blood, combining DNA fragmentation, deep sampling, and blood cell pellet analysis. The findings offer solid evidence of enhanced detection sensitivity and shed light on parasite load dynamics during chronic infection in mammalian reservoirs. The evidence is sound for macaques and the method shows promise in expanding detection limits, but there is some variability in the limits of detection and small sample size of human samples. This work will be of interest to parasitologists, epidemiologists, and clinicians using molecular diagnostics to monitor responses to etiological treatments for Chagas disease.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104547.2.sa1](https://doi.org/10.7554/eLife.104547.2.sa1)

This study presents a refined approach to enhance the sensitivity of PCR for detecting Trypanosoma cruzi in blood by employing DNA fragmentation and deep sampling, involving multiple replicate PCR reactions. Combined with serial blood sampling, these methods enabled consistent detection of the parasite in infected humans, non-human primates, and dogs, including hosts with very low parasitemia levels.

Inspired by earlier methods that cleaved kinetoplast DNA (kDNA) to improve target distribution, this study targets nuclear satellite DNA repeats, which are tandemly arranged in T. cruzi chromosomes. By fragmenting DNA prior to PCR, the authors reduced subsampling errors, breaking large fragments into smaller, evenly distributed units. This improved the frequency of positive reactions and reduced variability among replicate Cq values.

Using contrived blood samples, the study demonstrated that this approach significantly enhances PCR positivity. Moreover, the findings suggest that cell pellets from blood yield higher concentrations of parasite DNA compared to whole blood, prompting a reevaluation of current diagnostic practices, which predominantly use whole blood lysates.

The study also highlights the importance of deep sampling. Serial testing across multiple blood samples mitigated the variability in parasitemia, addressing challenges first noted in early xenodiagnosis studies (Cerisola et al., 1977).

The proposed DNA extraction and amplification procedures effectively captured parasitemia dynamics, achieving detection sensitivities with quantification limits as low as ~0.00025 parasite equivalents/mL, approaching the detection of a single target copy per reaction.

This work underscores the utility of deep-sampling PCR in monitoring parasitemia dynamics and guiding treatment strategies, especially in chronic infections. It also stresses the importance of treating individuals with low parasitic loads, as immune control may change over time.

Strengths:

The strategies used for increasing PCR sensitivity offer the potential for enhancing treatment monitoring and understanding the dynamics of parasite-host interactions in chronic Chagas disease.

Weaknesses:

While the study offers valuable insights for research in T.cruzi infection dynamics and monitoring of trypanocidal drugs efficacy, its broader adoption depends on the development of cost-effective and scalable alternatives to labor-intensive techniques such as sonication, currently required for DNA fragmentation. Additionally, the reliance on blood cell pellets and the DNA fragmentation protocol introduces extra processing steps, which may not be feasible for many clinical laboratories, particularly in resource-limited endemic areas that require simpler and more streamlined procedures.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104547.2.sa2](https://doi.org/10.7554/eLife.104547.2.sa2)

Summary:

This study introduces a valuable methodological innovation for detecting Trypanosoma cruzi, the causative agent of Chagas disease, using "deep-sampling PCR" which combines DNA fragmentation with multiple qPCR replications (>300 in some cases) on each sample. The authors aim to overcome the limitations of current qPCR methods by increasing the sensitivity of detection, which is fundamental for evaluating treatment responses in chronic Chagas disease patients. The work also evaluates the approach in multiple host species (macaques, humans, and dogs), at different times and across different sample types, including whole blood, blood cell pellets, plasma, and tissues.

Strengths:

The primary strength of this study lies in its methodological novelty, particularly the combination of multiple parallel PCR reactions and DNA fragmentation to enhance sensitivity. It is a sort of brute-force method for detecting the parasite. This approach promises the detection of parasitic DNA at levels significantly lower than those achievable with standard qPCR methods. Additionally, the authors demonstrate the utility of this method in tracking parasitemia dynamics and post-treatment responses in macaques and dogs, providing valuable insights for both research and clinical applications.

Weaknesses:

(1) Methodological Concerns on detection and quantification limits

Some methodological inconsistencies and limitations were observed that merit consideration. In Figure 1, there is a clear lack of consistency with theoretical expectations and with the trends observed in Figure 4A. Based on approximate calculations, having 10^-7 parasite equivalents with 100,000 target copies per parasite implies an average of 0.01 target copies per reaction. This would suggest an amplification rate of approximately 1 in 100 reactions, yet the observed 30% amplification appears disproportionately high. In addition, Figure 4A (not fragmented) shows lower values of positivity than Figure 1 for 10^-5 and 10^-6 dilutions showing this inconsistency among experiments. Some possible explanations could account for this inconsistency: (1) an inaccurate quantification of the starting number of parasites used for serial dilutions, or (2) random contamination not detected by negative controls, potentially due to a low number of template molecules.

Similarly, Figure 5B presents another inconsistency in theoretical expectations for amplification. The authors report detecting amplification in reactions containing 10^-9 parasites after DNA fragmentation. Based on the figure, at least 3 positives (as I can see because raw data is not available) out of 388 PCRs are observed at this dilution. Assuming 100,000 copies of satellite DNA per parasite, the probability of a single copy being present in a 10^-9 dilution is approximately 1/10,000. If we assume this as the probability of amplification of a PCR (an approximation), by using a simple binomial calculation, the probability of at least 3 positive reactions out of 388 is approximately 9.39 x 10^-6 (in ideal conditions, likely lower in real-world scenarios). This translates to a probability of about 1 in 100,000 to observe such frequency of positives, which is highly improbable and suggests either inaccuracies in the initial parasite quantification or issues with contamination. In addition, at 10^-6 PE/reactions (the proposed limit of quantification) it is observed that 40% of repetitions are amplified. The number of repetitions is not specified but probably more than 50 according to the graph. Such dilution implies 0.1 targets per reaction (assuming 100.000 copies divided by 10^6), which means a total of 5 target molecules to distribute among the reactions (0.1 targets multiplied by 50 reactions). It seems highly improbable that 40% of the reactions (20/50) would amplify under the described conditions. Even considering 200.000 target copies per parasite implies 0.2 targets per reaction and an average of 10 molecules to distribute among 50 reactions. The approximate probability of the observation of at least 20/50 positives can be calculated by determining the probability of a reaction to receive targets by assuming a random distribution of the targets among the tubes, p = 1 - (1 - 1/50)^10, and then by using a binomial distribution to determine the probability that at least 20 reactions receive at least one target copy. The probability of at least 20/50 positive reactions in a dilution of 10^-6 parasites (200.000 target copies per parasite) is 0.00028. Consequently, the observed result is highly unlikely.

1. Lack of details on contamination detection

Additionally, the manuscript does not provide enough details on how cross-contamination was detected or managed. It is unclear how the negative controls (NTCs) and no-template controls were distributed across plates, in terms of both quantity and placement. This omission is critical, as the low detection thresholds targeted in this study increase the risk of false positives by contamination. To ensure reliability and reproducibility, future uses of the technique would benefit from more standardized and clearly documented protocols for control placement and handling.

1. Unclear relevance for treatment monitoring in Humans

In Figure 7A, the results suggest that the deep-sampling PCR method does not provide a clearly significant improvement over conventional qPCR in humans. Of the 9 samples tested, 6 (56%) were consistently amplified in all or nearly all reactions, indicating these samples could also be reliably detected with standard PCR protocols. Two additional samples were detected only with the deep-sampling approach, increasing sensitivity to 78%; however, these detections might be attributable to random chance given the limited sample size. While the authors acknowledge the small sample size in the discussion, they do not address the fact that a similar increase in sensitivity was reported in citation 5, where only 3 samples were tested with 3 replicates each. This raises an important question: how many PCR reactions are needed in human samples to reach a plateau in detection rates? This issue should be further discussed to contextualize the results and their implications.

Despite these limitations, this work represents a promising step forward in the development of highly sensitive diagnostic tools for T. cruzi. It offers a novel foundation for advancing the detection and monitoring of parasitemia, which could significantly benefit Chagas disease research community and clinicians focused on neglected tropical diseases. While addressing the methodological inconsistencies and improving robustness will be critical, this study provides valuable insights and data that could lead to future innovations in parasitological research and diagnostics.

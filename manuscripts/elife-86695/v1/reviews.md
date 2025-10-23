# Peer review - Round 1

Editors:
- John Ewer, Universidad de Valparaiso Chile

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86695.3.sa0](https://doi.org/10.7554/eLife.86695.3.sa0)

This study presents an important open-source resource for high-throughput behavioral screening. The protocols employ inexpensive, off the shelf hardware, and allow real-time analysis of hundreds of behaving flies. Although these protocols were developed using Drosophila melanogaster, they could easily be applied to other models. The evidence in support of the conclusions is solid and the revisions carried out by the authors go a long way towards providing the user with an integrated system that is also more user-friendly.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86695.3.sa1](https://doi.org/10.7554/eLife.86695.3.sa1)

In the current paper, Jones et al. describe a new framework, named "coccinella", for real-time high-throughput behavioral analysis aimed at reducing the cost of analyzing behavior. In the setup used here each fly is confined to a small circular arena and able to walk around on an agar bed spiked with nutrients or pharmacological agents. The new framework, built on the researchers' previously developed platform Ethoscope, relies on relatively low-cost Raspberry Pi video cameras to acquire images at ~0.5 Hz and pull out, in real time, the maximal velocity (parameter extraction) during 10 second windows from each video. Thus, the program produces a text file, and not voluminous videos requiring storage facilities for large amounts of video data, a prohibitive step in many behavioral analyses. The maximal velocity time-series is then fed to an algorithm called Highly Comparative Time-Series Classification (HCTSA)(which itself is based on a large number of feature extraction algorithms) developed by other researchers. HCTSA identifies statistically salient features in the time-series which are then passed on to a type of linear classifier algorithm called support vector machines (SVM). In cases where such analyses are sufficient for characterizing the behaviors of interest this system performs as well as other state-of-the-art systems used in behavioral analysis (e.g., DeepLabCut)

In a pharmacobehavior paradigm testing different chemicals, the authors show that coccinella can identify specific compounds as effectively as other more time-consuming and resource-consuming systems.

The new paradigm should be of interest to researchers involved in drug screens, and more generally, in high-throughput analysis focused on gross locomotor defects in fruit flies such as identification of sleep phenotypes. By extracting/saving only the maximal velocity from video clips, the method is fast. However, the rapidity of the platform comes at a cost--loss of information on subtle but important behavioral alterations. When seeking subtle modifications in animal behavior, solutions like DeepLabCut, which are admittedly slower but far superior in terms of the level of details they yield, would be more appropriate.

The manuscript reads well, and it is scientifically solid. The comments listed below were directed to the original submission and were satisfactorily addressed in the revised version.

1- The fact that Coccinella runs on Ethoscopes, an open source hardware platform described by the same group, is very useful because the relevant publication describes Ethoscope in detail. However, the current version of the paper does not offer details or alternatives for users that would like to test the framework, but do not have an Ethoscope. Would it be possible to overcome this barrier and have coccinella run with any video data (and, thus, potentially be used to analyze data obtained from other animal models)?

2- Readers who want background on the analytical approaches that the platform relies on following maximal velocity extraction, will have to consult the original publications. In particular, the current manuscript does not provide much explanation on Highly Comparative Time-Series Classification (HCTSA) or SVM; this may be reasonable because the methods were developed earlier by others. While some readers may find that the lack of details increases the manuscript's readability, others may be left wanting to see more discussion on these not-so-trivial approaches. In addition, it is worth noting that the same authors that published the HCTSA method, also described a shorter version named catch22, that runs faster with a similar output. Thus, explaining in more detail how HCTSA operates, considering is a relatively new method, will make the method more convincing.

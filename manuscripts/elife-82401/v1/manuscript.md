# SIMMER employs similarity algorithms to accurately identify human gut microbiome species and enzymes capable of known chemical transformations

## Authors

- Annamarie E Bustion<sup>1</sup> ([ORCID: 0000-0002-7380-3619](https://orcid.org/0000-0002-7380-3619))
- Renuka R Nayak<sup>2</sup>
- Ayushi Agrawal<sup>3</sup> ([ORCID: 0000-0003-2940-8926](https://orcid.org/0000-0003-2940-8926))
- Peter J Turnbaugh<sup>4</sup> ([ORCID: 0000-0002-0888-2875](https://orcid.org/0000-0002-0888-2875))
- Katie S Pollard<sup>3</sup> ([ORCID: 0000-0002-9870-6196](https://orcid.org/0000-0002-9870-6196)) †

### Affiliations

1. Pharmaceutical Sciences and Pharmacogenomics Graduate Program University of California, San Francisco San Francisco United States
2. Department of Medicine University of California, San Francisco San Francisco United States
3. Institute of Data Science and Biotechnology Gladstone Institutes San Francisco United States
4. Department of Microbiology and Immunology University of California, San Francisco San Francisco United States

† Corresponding author

## Abstract

Bacteria within the gut microbiota possess the ability to metabolize a wide array of human drugs, foods, and toxins, but the responsible enzymes for these chemical events remain largely uncharacterized due to the time-consuming nature of current experimental approaches. Attempts have been made in the past to computationally predict which bacterial species and enzymes are responsible for chemical transformations in the gut environment, but with low accuracy due to minimal chemical representation and sequence similarity search schemes. Here, we present an in silico approach that employs chemical and protein Similarity algorithms that Identify MicrobioMe Enzymatic Reactions (SIMMER). We show that SIMMER accurately predicts the responsible species and enzymes for a queried reaction, unlike previous methods. We demonstrate SIMMER use cases in the context of drug metabolism by predicting previously uncharacterized enzymes for 88 drug transformations known to occur in the human gut. We validate these predictions on external datasets and provide an in vitro validation of SIMMER's predictions for metabolism of methotrexate, an anti-arthritic drug. After demonstrating its utility and accuracy, we made SIMMER available as both a command-line and web tool, with flexible input and output options for determining chemical transformations within the human gut. We present SIMMER as a computational addition to the microbiome researcher's toolbox, enabling them to make informed hypotheses before embarking on the lengthy laboratory experiments required to characterize novel bacterial enzymes that can alter human ingested compounds.

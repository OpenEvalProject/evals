# NetPyNE, a tool for data-driven multiscale modeling of brain circuits

## Authors

- Salvador Dura-Bernal<sup>1</sup> ([ORCID: 0000-0002-8561-5324](https://orcid.org/0000-0002-8561-5324)) †
- Benjamin A Suter<sup>2</sup> ([ORCID: 0000-0002-9885-6936](https://orcid.org/0000-0002-9885-6936))
- Padraig Gleeson<sup>3</sup> ([ORCID: 0000-0001-5963-8576](https://orcid.org/0000-0001-5963-8576))
- Matteo Cantarelli<sup>4</sup>
- Adrian Quintana<sup>5</sup>
- Facundo Rodriguez<sup>1</sup>
- David J Kedziora<sup>6</sup>
- George L Chadderdon<sup>1</sup>
- Cliff C Kerr<sup>6</sup>
- Samuel A Neymotin<sup>1</sup>
- Robert A McDougal<sup>7</sup>
- Michael Hines<sup>7</sup>
- Gordon M G Shepherd<sup>2</sup> ([ORCID: 0000-0002-1455-8262](https://orcid.org/0000-0002-1455-8262))
- William W Lytton<sup>1</sup>

### Affiliations

1. Department of Physiology and Pharmacology State University of New York Downstate Medical Center Brooklyn United States
2. Department of Physiology Northwestern University Chicago United States
3. Department of Neuroscience, Physiology and Pharmacology University College London London United Kingdom
4. Metacell LLC Boston United States
5. EyeSeeTea Ltd Cheltenham United Kingdom
6. Complex Systems Group, School of Physics University of Sydney Sydney Australia
7. Department of Neuroscience Yale University New Haven United States

† Corresponding author

## Abstract

Biophysical modeling of neuronal networks helps to integrate and interpret rapidly growing and disparate experimental datasets at multiple scales. The NetPyNE tool (www.netpyne.org) provides both programmatic and graphical interfaces to develop data-driven multiscale network models in NEURON. NetPyNE clearly separates model parameters from implementation code. Users provide specifications at a high level via a standardized declarative language, e.g. connectivity rules, to create millions of cell-to-cell connections. NetPyNE then enables users to generate the NEURON network, run efficiently parallelized simulations, optimize and explore network parameters through automated batch runs, and use built-in functions for visualization and analysis - connectivity matrices, voltage traces, spike raster plots, local field potentials, and information theoretic measures. NetPyNE also facilitates model sharing by exporting and importing standardized formats (NeuroML and SONATA). NetPyNE is already being used to teach computational neuroscience students and by modelers to investigate brain regions and phenomena.

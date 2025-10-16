# On the objectivity, reliability, and validity of deep learning enabled bioimage analyses

## Authors

- Dennis Segebarth<sup>1</sup> ([ORCID: 0000-0002-3806-9324](https://orcid.org/0000-0002-3806-9324))
- Matthias Griebel<sup>2</sup> ([ORCID: 0000-0003-1959-0242](https://orcid.org/0000-0003-1959-0242))
- Nikolai Stein<sup>2</sup>
- Cora R von Collenberg<sup>1</sup>
- Corinna Martin<sup>1</sup>
- Dominik Fiedler<sup>3</sup>
- Lucas B Comeras<sup>4</sup>
- Anupam Sah<sup>5</sup>
- Victoria Schoeffler<sup>6</sup>
- Teresa Lüffe<sup>6</sup>
- Alexander Dürr<sup>2</sup>
- Rohini Gupta<sup>1</sup>
- Manju Sasi<sup>1</sup>
- Christina Lillesaar<sup>6</sup> ([ORCID: 0000-0002-5166-2851](https://orcid.org/0000-0002-5166-2851))
- Maren D Lange<sup>3</sup>
- Ramon O Tasan<sup>7</sup>
- Nicolas Singewald<sup>5</sup> ([ORCID: 0000-0002-0166-3370](https://orcid.org/0000-0002-0166-3370))
- Hans-Christian Pape<sup>3</sup> ([ORCID: 0000-0001-6874-8224](https://orcid.org/0000-0001-6874-8224))
- Christoph M Flath<sup>2</sup> ([ORCID: 0000-0002-1761-9833](https://orcid.org/0000-0002-1761-9833)) †
- Robert Blum<sup>1</sup> ([ORCID: 0000-0002-5270-3854](https://orcid.org/0000-0002-5270-3854)) †

### Affiliations

1. Institute of Clinical Neurobiology University Hospital Würzburg Würzburg Germany
2. Department of Business and Economics University of Würzburg Würzburg Germany
3. Institute of Physiology Westfälische Wilhlems-Universität Münster Germany
4. Department of Pharmacology University of Innsbruck Innsbruck Austria
5. Department of Pharmacology and Toxicology University of Innsbruck Innsbruck Austria
6. Department of Child and Adolescent Psychiatry University Hospital Würzburg Würzburg Germany
7. Department of Pharmacology University of Inssbruck Innsbruck Austria

† Corresponding author

## Abstract

Bioimage analysis of fluorescent labels is widely used in the life sciences. Recent advances in deep learning (DL) allow automating time-consuming manual image analysis processes based on annotated training data. However, manual annotation of fluorescent features with a low signal-to-noise ratio is somewhat subjective. Training DL models on subjective annotations may be instable or yield biased models. In turn, these models may be unable to reliably detect biological effects. An analysis pipeline integrating data annotation, ground truth estimation, and model training can mitigate this risk. To evaluate this integrated process, we compared different DL-based analysis approaches. With data from two model organisms (mice, zebrafish) and five laboratories, we show that ground truth estimation from multiple human annotators helps to establish objectivity in fluorescent feature annotations. Furthermore, ensembles of multiple models trained on the estimated ground truth establish reliability and validity. Our research provides guidelines for reproducible DL-based bioimage analyses.

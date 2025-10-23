# Digital wearable insole-based identification of knee arthropathies and gait signatures using machine learning

## Authors

- Matthew F Wipperman<sup>1</sup> ([ORCID: 0000-0003-1436-3366](https://orcid.org/0000-0003-1436-3366)) †
- Allen Z Lin<sup>2</sup>
- Kaitlyn M Gayvert<sup>2</sup>
- Benjamin Lahner<sup>1</sup>
- Selin Somersan-Karakaya<sup>3</sup>
- Xuefang Wu<sup>4</sup>
- Joseph Im<sup>4</sup>
- Minji Lee<sup>2</sup>
- Bharatkumar Koyani<sup>4</sup>
- Ian Setliff<sup>2</sup>
- Malika Thakur<sup>4</sup>
- Daoyu Duan<sup>1</sup>
- Aurora Breazna<sup>5</sup>
- Fang Wang<sup>1</sup>
- Wei Keat Lim<sup>2</sup> ([ORCID: 0000-0002-6226-2570](https://orcid.org/0000-0002-6226-2570))
- Gabor Halasz<sup>2</sup>
- Jacek Urbanek<sup>5</sup>
- Yamini Patel<sup>6</sup>
- Gurinder S Atwal<sup>2</sup>
- Jennifer D Hamilton<sup>1</sup>
- Samuel Stuart<sup>1</sup>
- Oren Levy<sup>3</sup>
- Andreja Avbersek<sup>3</sup>
- Rinol Alaj<sup>4</sup> †
- Sara C Hamon<sup>1</sup> †
- Olivier Harari<sup>3</sup> †

### Affiliations

1. Precision Medicine Regeneron Tarrytown United States
2. Molecular Profiling and Data Science Regeneron Tarrytown United States
3. Early Clinical Development and Experimental Sciences Regeneron Tarrytown United States
4. Clinical Outcomes Assessment and Patient Innovation Regeneron Tarrytown United States
5. Biostatistics and Data Management Regeneron Tarrytown United States
6. General Medicine Regeneron Tarrytown United States

† Corresponding author

## Abstract

Gait is impaired in musculoskeletal conditions, such as knee arthropathy. Gait analysis is used in clinical practice to inform diagnosis and to monitor disease progression or intervention response. However, clinical gait analysis relies on subjective visual observation of walking, as objective gait analysis has not been possible within clinical settings due to the expensive equipment, large-scale facilities, and highly trained staff required. Relatively low-cost wearable digital insoles may offer a solution to these challenges. In this work, we demonstrate how a digital insole measuring osteoarthritis-specific gait signatures yields similar results to the clinical gait-lab standard. To achieve this, we constructed a machine learning model, trained on force plate data collected in participants with knee arthropathy and controls. This model was highly predictive of force plate data from a validation set (area under the receiver operating characteristics curve [auROC] = 0.86; area under the precision-recall curve [auPR] = 0.90) and of a separate, independent digital insole dataset containing control and knee osteoarthritis subjects (auROC = 0.83; auPR = 0.86). After showing that digital insole derived gait characteristics are comparable to traditional gait measurements, we next showed that a single stride of raw sensor time series data could be accurately assigned to each subject, highlighting that individuals using digital insoles can be identified by their gait characteristics. This work provides a framework for a promising alternative to traditional clinical gait analysis methods, adds to the growing body of knowledge regarding wearable technology analytical pipelines, and supports clinical development of at-home gait assessments, with the potential to improve the ease, frequency, and depth of patient monitoring.

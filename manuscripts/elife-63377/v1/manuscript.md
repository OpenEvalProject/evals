# DeepEthogram, a machine learning pipeline for supervised behavior classification from raw pixels

## Authors

- James P Bohnslav<sup>1</sup>
- Nivanthika K Wimalasena<sup>2</sup>
- Kelsey J Clausing<sup>3</sup>
- Yu Y Dai<sup>3</sup>
- David A Yarmolinsky<sup>2</sup>
- Tomás Cruz<sup>4</sup>
- Adam D Kashlan<sup>2</sup>
- M Eugenia Chiappe<sup>5</sup> ([ORCID: 0000-0003-1761-0457](https://orcid.org/0000-0003-1761-0457))
- Lauren L Orefice<sup>3</sup>
- Clifford J Woolf<sup>6</sup>
- Christopher D Harvey<sup>1</sup> ([ORCID: 0000-0001-9850-2268](https://orcid.org/0000-0001-9850-2268)) †

### Affiliations

1. Neurobiology Harvard Medical School Boston United States
2. F.M. Kirby Neurobiology Center Boston Children's Hospital Boston United States
3. Molecular Biology Massachusetts General Hospital Boston United States
4. Champalimaud Neuroscience Programme Champalimaud Center for the Unknown Lisbon Portugal
5. Champalimaud Neuroscience Porgramme Champalimaud Center for the Unknown Lisbon Portugal
6. Department of Neurobiology Harvard Medical School Boston United States

† Corresponding author

## Abstract

Videos of animal behavior are used to quantify researcher-defined behaviors-of-interest to study neural function, gene mutations, and pharmacological therapies. Behaviors-of-interest are often scored manually, which is time-consuming, limited to few behaviors, and variable across researchers. We created DeepEthogram: software that uses supervised machine learning to convert raw video pixels into an ethogram, the behaviors-of-interest present in each video frame. DeepEthogram is designed to be general-purpose and applicable across species, behaviors, and video-recording hardware. It uses convolutional neural networks to compute motion, extract features from motion and images, and classify features into behaviors. Behaviors are classified with above 90% accuracy on single frames in videos of mice and flies, matching expert-level human performance. DeepEthogram accurately predicts rare behaviors, requires little training data, and generalizes across subjects. A graphical interface allows beginning-to-end analysis without end-user programming. DeepEthogram's rapid, automatic, and reproducible labeling of researcher-defined behaviors-of-interest may accelerate and enhance supervised behavior analysis.

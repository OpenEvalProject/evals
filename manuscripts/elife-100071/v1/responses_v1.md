# Author response - Round 1

Authors:
- Quang Thinh Trac ([ORCID: 0000-0003-2429-0287](https://orcid.org/0000-0003-2429-0287))
- Yue Huang
- Tom Erkers
- Päivi Östling
- Anna Bohlin
- Albin Osterroos
- Mattias Vesterlund ([ORCID: 0000-0001-9471-6592](https://orcid.org/0000-0001-9471-6592))
- Rozbeh Jafari
- Ioannis Siavelis
- Helena Backvall
- Santeri Kiviluoto
- Lukas Orre
- Mattias Rantalainen
- Janne Lehtiö ([ORCID: 0000-0002-8100-9562](https://orcid.org/0000-0002-8100-9562))
- Soren Lehmann
- Olli Kallioniemi
- Yudi Pawitan
- Trung Nghia Vu ([ORCID: 0000-0001-7945-5750](https://orcid.org/0000-0001-7945-5750))

## Response text

DOI: [10.7554/eLife.100071.4.sa4](https://doi.org/10.7554/eLife.100071.4.sa4)

The following is the authors’ response to the previous reviews

We would like to respond to just one remaining concern from Reviewer 1 and Reviewer 2 regarding a potential overfitting in Test Set 1, which involves combinations already present in the training set. DIPx’s (and TAIJI’s) performance in Test Set 1 is better than in Test Set 2, which involves combinations not present in the training set. Let’s consider two general points to highlight why the improved performance is not the result of overfitting.

(1) Suppose we are testing the e ect of one drug D; the training may involve, for example, selecting an optimal dose. A validated e ect of D in an independent test set is not an overfit, even though we are using the same drug in the training and the test set. Testing one drug is an extreme case, but the same idea holds for any number of drugs. What matters is the independence of the test set.

(2) A prediction model P1 will legitimately perform better than model P2, if P1 uses better or more informative features than P2. The features could be those used directly in the model, but they could also be other observable characteristics not directly used in the model, such as optimal subregions of the feature space. DPIx or TAIJI results indicate that the identity of previously trained combinations is one such informative feature. The set of previously trained combinations corresponds to a subregion of the feature space. DIPx’s prediction performance for known combinations would be expected to follow the results from Test Set 1; we cannot expect that if there is an overfitting issue. Finally, we note that Test Set 1 was established and used in the AstraZeneca Dream Challenge for rigorously testing the prediction of known combinations.

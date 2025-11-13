# Rapid protein stability prediction using deep learning representations

## Authors

- Lasse M Blaabjerg<sup>1</sup> ([ORCID: 0000-0003-0720-8632](https://orcid.org/0000-0003-0720-8632))
- Maher M Kassem<sup>2</sup>
- Lydia L Good<sup>1</sup> ([ORCID: 0000-0001-5308-8542](https://orcid.org/0000-0001-5308-8542))
- Nicolas Jonsson<sup>1</sup> ([ORCID: 0000-0002-7838-1814](https://orcid.org/0000-0002-7838-1814))
- Matteo Cagiada<sup>1</sup>
- Kristoffer E Johansson<sup>1</sup> ([ORCID: 0000-0001-6054-0461](https://orcid.org/0000-0001-6054-0461))
- Wouter Boomsma<sup>2</sup> †
- Amelie Stein<sup>1</sup> ([ORCID: 0000-0002-5862-1681](https://orcid.org/0000-0002-5862-1681)) †
- Kresten Lindorff-Larsen<sup>1</sup> ([ORCID: 0000-0002-4750-6039](https://orcid.org/0000-0002-4750-6039)) †

### Affiliations

1. Linderstrøm-Lang Centre for Protein Science, Department of Biology, University of Copenhagen Copenhagen Denmark ([ROR:035b05819](https://ror.org/035b05819))
2. Center for Basic Machine Learning Research in Life Science, Department of Computer Science, University of Copenhagen Copenhagen Denmark ([ROR:035b05819](https://ror.org/035b05819))

† Corresponding author

## Abstract

Predicting the thermodynamic stability of proteins is a common and widely used step in protein engineering, and when elucidating the molecular mechanisms behind evolution and disease. Here, we present RaSP, a method for making rapid and accurate predictions of changes in protein stability by leveraging deep learning representations. RaSP performs on-par with biophysics-based methods and enables saturation mutagenesis stability predictions in less than a second per residue. We use RaSP to calculate ∼ 230 million stability changes for nearly all single amino acid changes in the human proteome, and examine variants observed in the human population. We find that variants that are common in the population are substantially depleted for severe destabilization, and that there are substantial differences between benign and pathogenic variants, highlighting the role of protein stability in genetic diseases. RaSP is freely available—including via a Web interface—and enables large-scale analyses of stability in experimental and predicted protein structures.

## Introduction

Protein stability, as measured by the thermodynamic free energy difference between the native and the unfolded state, is an important feature of protein structure and therefore function. Protein stability plays a critical role when trying to understand the molecular mechanisms of evolution and has been found to be an important driver of human disease (Casadio et al., 2011; Martelli et al., 2016; Nielsen et al., 2020). Furthermore, optimisation of protein stability is a fundamental part of protein engineering and design (Rocklin et al., 2017).

For a given protein, single amino acid substitutions can have substantial effects on protein stability depending on the particular substitution and the surrounding atomic environment. Assessing such variant effects can be done experimentally for example via thermal or chemical denaturation assays (Lindorff-Larsen and Teilum, 2021). This process, however, may be laborious and time-consuming for even a modest number of amino acid substitutions. In contrast, computational methods have been developed that can predict protein stability changes. Such methods include well-established energy-function-based methods such as for example FoldX (Schymkowitz et al., 2005) and Rosetta (Kellogg et al., 2011), or methods based on molecular dynamics simulations (Gapsys et al., 2016).

Machine learning models have also been developed to predict changes in protein stability and can roughly be split into two types: supervised and self-supervised models. In supervised models, experimental protein stability measurements are used as targets for model predictions (Li et al., 2020; Benevenuta et al., 2021; Pires et al., 2014; Chen et al., 2020). Supervised models are immediately appealing as they are trained directly on experimental data and are able to make predictions at the correct absolute scale. Supervised models may, however, suffer from systematic biases, which can be hard to overcome with limited experimental data. These biases relate to issues of model overfitting of the training data, biases present in the experimental data towards destabilising mutations, biases of the types of amino acid changes that have been probed experimentally, and a lack of self-consistency in model predictions (Yang et al., 2018; Pucci et al., 2018; Usmanova et al., 2018; Fang, 2019; Stein et al., 2019; Caldararu et al., 2020).

In contrast, self-supervised models can be trained without the use of experimental protein stability measurements. Typically, self-supervised models are trained to predict masked amino acid labels from structure or sequence information, thereby learning a likelihood distribution over possible amino acid types at a particular position. This learned likelihood distribution can subsequently be used directly to predict the effects of mutations on protein stability (Lui and Tiana, 2013; Boomsma and Frellsen, 2017; Riesselman et al., 2018; Shin et al., 2021; Elnaggar et al., 2021; Meier et al., 2021). Self-supervised models sidestep many of the challenges associated with training on experimental data and have shown impressive results in recent years. These models, however, often require substantial computational resources during training—and sometimes during evaluation—and generally do not make predictions at an absolute scale, which limits their practical application.

Due to the complementary strengths and weaknesses of supervised and self-supervised models, the two perspectives can often be fruitfully combined. Here we present such an approach for rapid protein stability-change predictions, combining pre-trained representations of molecular environments with supervised fine-tuning. Our method, RaSP (Rapid Stability Prediction) provides both fast and accurate predictions of protein stability changes and thus enables large-scale, proteome-wide applications.

## Results

### Development of the RaSP model

We trained the RaSP model in two steps (Figure 1). First, we trained a self-supervised representation model to learn an internal representation of protein structure. We selected a 3D convolutional neural network architecture for the representation model, as this has previously been shown to yield predictions that correlate well with changes in protein stability (Boomsma and Frellsen, 2017). Second, we trained a supervised downstream model using the learned structure representation as input to predict protein stability changes on an absolute scale. The task of the downstream model is therefore to re-scale and refine the input from the representation model. The supervised downstream model was trained on a set of calculated protein stability changes to enable the generation of a larger and more powerful training data set while minimizing the effects from experimental data biases. We chose to estimate protein variant stability values using the Rosetta ‘cartesian_ddg’ protocol, which has shown to be a reliable and well-established predictor of stability (Park et al., 2016; Frenz et al., 2020), and as shown below the model generalizes to a wide range of situations. We expect that similar results could have been obtained using other variant stability prediction methods such as FoldX.

![Figure 1.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig1-v2.jpg)

**Figure 1.:** We trained a self-supervised three-dimensional convolutional neural network (CNN) to learn internal representations of protein structures by predicting wild-type amino acid labels from protein structures. The representation model is trained to predict amino acid type based on the local atomic environment parameterized using a 3D sphere around the wild-type residue. Using the representations from the convolutional neural network as input, a second downstream and supervised fully connected neural network (FCNN) was trained to predict Rosetta $Δ⁢Δ⁢G$ values.

Building on earlier work (Boomsma and Frellsen, 2017), we first trained a self-supervised 3D convolutional neural network on a large, homology-reduced set of high-resolution structures. This model was trained to predict the wild type amino acid labels of a protein given its local atomic environment (see Methods and Figure 2—figure supplement 1 for further details). In the second step of developing RaSP, we trained a downstream supervised fully-connected neural network to predict stability changes; this model uses the internal representation of the 3D convolutional neural network as well as the corresponding wild type and mutant amino acid labels and frequencies as input. We trained this model on $Δ⁢Δ⁢G$ values generated by saturation mutagenesis using Rosetta to limit the effects of biases from experimental assays and amino acid compositions; as described further below we validated the model using a range of different experiments. In the training of the supervised model, we used a custom loss function to focus the model on $Δ⁢Δ⁢G$ values in the range from approximately -1 to 7 where Rosetta is known to be most accurate (Kellogg et al., 2011) and where many loss-of-function variants relevant for human disease can be identified (Casadio et al., 2011; Cagiada et al., 2021).

After training (Figure 2a), the downstream model achieves a Pearson correlation coefficient of 0.82 and a mean absolute error (MAE) of 0.73 kcal/mol on a test data set comprised of 10 proteins with full saturation mutagenesis which was not seen by the model until after it had been developed and trained (Figure 2b and Table 1). In practice, the downstream model predictions were made using the median of an ensemble of 10 model predictions with each model trained using different initialization seeds. The accuracy of the model is relatively uniform for the different types of amino acid substitutions, with bigger errors in particular when substituting glycine residues, or when changing residues to proline (Figure 2—figure supplement 2). In terms of location of the residue in the protein structure, the model accuracy is slightly better at exposed relative to buried residues (Figure 2—figure supplement 3), although we note also that the distribution of stability changes are different in the two different locations.

**Table 1.**
 Overview of RaSP model test set prediction results including benchmark comparison with the Rosetta protocol.When comparing RaSP to Rosetta (column: "Pearson |$ρ$| RaSP vs. Ros."), we only compute the Pearson correlation coefficients for variants with a Rosetta $Δ⁢Δ⁢G$ value in the range [–1;7] kcal/mol. Experimental data is from Kumar, 2006; Ó Conchúir et al., 2015; Nisthal et al., 2019; Matreyek et al., 2018; Suiter et al., 2020.


<table>
  <thead>
    <tr>
      <th>Data set</th>
      <th>Protein name</th>
      <th>PDB, chain</th>
      <th>Pearson |ρ|RaSP vs. Ros.</th>
      <th>Pearson |ρ|RaSP vs. Exp.</th>
      <th>Pearson |ρ|Ros. vs. Exp.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="10">RaSP test set</td>
      <td>MEN1</td>
      <td>3U84, A</td>
      <td>0.85</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>2R7E, A</td>
      <td>0.71</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ELANE</td>
      <td>4WVP, A</td>
      <td>0.81</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ADSL</td>
      <td>2J91, A</td>
      <td>0.84</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>GCK</td>
      <td>4DCH, A</td>
      <td>0.84</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>RPE65</td>
      <td>4RSC, A</td>
      <td>0.84</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>TTR</td>
      <td>1F41, A</td>
      <td>0.88</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ELOB</td>
      <td>4AJY, B</td>
      <td>0.87</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SOD1</td>
      <td>2CJS, A</td>
      <td>0.84</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>VANX</td>
      <td>1R44, A</td>
      <td>0.83</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="4">ProTherm test set</td>
      <td>Myoglobin</td>
      <td>1BVC, A</td>
      <td>0.91</td>
      <td>0.71</td>
      <td>0.76</td>
    </tr>
    <tr>
      <td>Lysozyme</td>
      <td>1LZ1, A</td>
      <td>0.80</td>
      <td>0.57</td>
      <td>0.65</td>
    </tr>
    <tr>
      <td>Chymotrypsin inhib.</td>
      <td>2CI2, I</td>
      <td>0.79</td>
      <td>0.65</td>
      <td>0.68</td>
    </tr>
    <tr>
      <td>RNAse H</td>
      <td>2RN2, A</td>
      <td>0.78</td>
      <td>0.79</td>
      <td>0.71</td>
    </tr>
    <tr>
      <td>Protein G</td>
      <td>Protein G</td>
      <td>1PGA, A</td>
      <td>0.90</td>
      <td>0.72</td>
      <td>0.72</td>
    </tr>
    <tr>
      <td rowspan="3">MAVE test set</td>
      <td>NUDT15</td>
      <td>5BON, A</td>
      <td>0.83</td>
      <td>0.50</td>
      <td>0.54</td>
    </tr>
    <tr>
      <td>TPMT</td>
      <td>2H11, A</td>
      <td>0.86</td>
      <td>0.48</td>
      <td>0.49</td>
    </tr>
    <tr>
      <td>PTEN</td>
      <td>1D5R, A</td>
      <td>0.87</td>
      <td>0.52</td>
      <td>0.53</td>
    </tr>
  </tbody>
</table>

![Figure 2.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig2-v2.jpg)

**Figure 2.:** (A) Learning curve for training of the RaSP downstream model, with Pearson correlation coefficients ($ρ$) and mean absolute error ($MAE_{F}$) of RaSP predictions. During training we transformed the target $Δ⁢Δ⁢G$ data using a switching (Fermi) function, and $MAE_{F}$ refers to this transformed data (see Methods for further details). Error bars represent the standard deviation of 10 independently trained models, that were subsequently used in ensemble averaging. Val: validation set; Train: training set. (B) After training, we applied the RaSP model to an independent test set to predict $Δ⁢Δ⁢G$ values for a full saturation mutagenesis of 10 proteins. Pearson correlation coefficients and mean absolute errors (MAE) were for this figure computed using only variants with Rosetta $Δ⁢Δ⁢G$ values in the range [–1;7] kcal/mol.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The model obtained at epoch 15 achieves a classification accuracy of 63% on the validation set.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Substitutions from glycine and cysteine as well as to proline generally have higher errors.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** RaSP versus Rosetta $Δ⁢Δ⁢G$ values for a full saturation mutagenesis of 10 test proteins separated into either exposed (A) or buried (B) residues.We speculate, that the RaSP prediction task is harder in the case of buried residues because Rosetta $Δ⁢Δ⁢G$ values generally have higher variance in those regions. Pearson correlation coefficients and mean absolute errors (MAE) were for this figure computed using only variants with Rosetta $Δ⁢Δ⁢G$ values in the range [–1;7] kcal/mol. Buried and exposed residue were classified based a relative surface accessible surface area (SASA) cut-off of 0.2.

### Validating RaSP using experimental data

After having shown that the RaSP model can successfully reproduce Rosetta $Δ⁢Δ⁢G$ values, we proceeded to test it on experimental measurements for five proteins. Specifically, we selected four proteins with stability measurements from ProTherm (Kumar, 2006; Ó Conchúir et al., 2015) and the B1 domain of protein G for which stability measurements are available for almost all possible single amino acid substitutions (Nisthal et al., 2019). We compared RaSP predictions for the five test proteins to Rosetta as a baseline (Figure 3, Figure 3—figure supplement 1). Pearson correlation coefficients of RaSP model predictions versus experimental stability measurements ranged from 0.79 (RNAse H, Rosetta baseline: 0.71)–0.57 (lysozyme, Rosetta baseline: 0.65). Although these correlations are not very high on an absolute scale, our results indicate that the RaSP model is approximately as accurate as the Rosetta protocol for predicting experimental $Δ⁢Δ⁢G$ values (Table 1). We also note that this accuracy is close to what is computationally achievable given the available data; it has been shown that there exists a natural upper bound on the achievable accuracy when predicting experimental $Δ⁢Δ⁢G$ values due to variations between experiments (Montanucci et al., 2019). Furthermore, we find the bias of the predictions (assessed via the mean error) is roughly the same between RaSP and Rosetta.

![Figure 3.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig3-v2.jpg)

**Figure 3.:** Predictions of changes in stability obtained using (A) RaSP and (B) Rosetta are compared to experimental data on five test proteins; myoglobin (1BVC), lysozyme (1LZ1), chymotrypsin inhibitor (2CI2), RNAse H (2RN2) and Protein G (1PGA) (Kumar, 2006; Ó Conchúir et al., 2015; Nisthal et al., 2019). Metrics used are Pearson correlation coefficient ($ρ$), mean absolute error (MAE) and mean error (ME). In the experimental study of Protein G, 105 variants were assigned a $Δ⁢Δ⁢G$ value of at least 4 kcal/mol due to low stability, presence of a folding intermediate, or lack expression (Nisthal et al., 2019).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Stability predictions obtained using (A–E) RaSP and (F–J) Rosetta are compared to experimental data for the five test proteins; myoglobin (1BVC), lysozyme (1LZ1), chymotrypsin inhibitor (2CI2), RNAse H (2RN2) and Protein G (1PGA) (Kumar, 2006; Ó Ó Conchúir et al., 2015; Nisthal et al., 2019). In the experimental study of Protein G, 105 variants were assigned a $Δ⁢Δ⁢G$ value of at least 4 kcal/mol due to low stability, presence of a folding intermediate, or lack expression (Nisthal et al., 2019).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig3-figsupp2-v2.jpg)

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The experimental data has been filtered to include only well-defined experimental $Δ⁢Δ⁢G$ values from single substitution mutations in natural protein domains (Tsuboyama et al., 2022). This filtered data set contains a total of 164,524 variants across 164 protein domain structures.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** We compare stability predictions with VAMP-seq scores for three test proteins (A) TPMT (PDB: 2H11) (Matreyek et al., 2018), (B) PTEN (PDB: 1D5R) (Matreyek et al., 2018) and (C) NUDT15 (PDB: 5BON) (Suiter et al., 2020).

In order to further validated RaSP, we compared its performance versus other methods on the recently published S669 experimental direct data set (Pancotti et al., 2022; Figure 3—figure supplement 2). The data set includes 669 variants and 94 experimental structures. We observe that RaSP performs as well as Rosetta in terms of Pearson correlation on this particular data set (Figure 3—figure supplement 2) and that RaSP performs relatively close to several of the best performing methods (Table 2). We also test the performance of RaSP on a high-accuracy version of the recently published experimental mega-scale data set from Rocklin and collaborators (Tsuboyama et al., 2022). We observe that RaSP achieves a zero-shot Pearson correlation coefficient of 0.62 and an MAE of 0.94 (Figure 3—figure supplement 3). Taken together, these results suggest the RaSP performs on-par with other computational methods although differences in training and parameterization makes direct comparison difficult. For example, a given method might have been parameterized either directly or independently from experimental data. In the case of RaSP, parameterization is made indirectly from experimental data since the Rosetta $Δ⁢Δ⁢G$ itself has been parameterized using a range of different types of experimental data (Park et al., 2016).

**Table 2.**
 Benchmark performance of RaSP versus other structure-based methods on the S669 direct experimental data set (Pancotti et al., 2022).Results for methods other than RaSP have been copied from Pancotti et al., 2022. We speculate that the higher RMSE and MAE values for Rosetta relative to RaSP are due to missing scaling of Rosetta output onto a scale similar to kcal/mol.


<table>
  <thead>
    <tr>
      <th rowspan="2">Method</th>
      <th colspan="3">S669, direct</th>
    </tr>
    <tr>
      <th>Pearson ρ</th>
      <th>RMSE [kcal/mol]</th>
      <th>MAE [kcal/mol]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Structure-based</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ACDC-NN</td>
      <td>0.46</td>
      <td>1.49</td>
      <td>1.05</td>
    </tr>
    <tr>
      <td>DDGun3D</td>
      <td>0.43</td>
      <td>1.60</td>
      <td>1.11</td>
    </tr>
    <tr>
      <td>PremPS</td>
      <td>0.41</td>
      <td>1.50</td>
      <td>1.08</td>
    </tr>
    <tr>
      <td>RaSP</td>
      <td>0.39</td>
      <td>1.63</td>
      <td>1.14</td>
    </tr>
    <tr>
      <td>ThermoNet</td>
      <td>0.39</td>
      <td>1.62</td>
      <td>1.17</td>
    </tr>
    <tr>
      <td>Rosetta</td>
      <td>0.39</td>
      <td>2.70</td>
      <td>2.08</td>
    </tr>
    <tr>
      <td>Dynamut</td>
      <td>0.41</td>
      <td>1.60</td>
      <td>1.19</td>
    </tr>
    <tr>
      <td>INPS3D</td>
      <td>0.43</td>
      <td>1.50</td>
      <td>1.07</td>
    </tr>
    <tr>
      <td>SDM</td>
      <td>0.41</td>
      <td>1.67</td>
      <td>1.26</td>
    </tr>
    <tr>
      <td>PoPMuSiC</td>
      <td>0.41</td>
      <td>1.51</td>
      <td>1.09</td>
    </tr>
    <tr>
      <td>MAESTRO</td>
      <td>0.50</td>
      <td>1.44</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td>FoldX</td>
      <td>0.22</td>
      <td>2.30</td>
      <td>1.56</td>
    </tr>
    <tr>
      <td>DUET</td>
      <td>0.41</td>
      <td>1.52</td>
      <td>1.10</td>
    </tr>
    <tr>
      <td>I-Mutant3.0</td>
      <td>0.36</td>
      <td>1.52</td>
      <td>1.12</td>
    </tr>
    <tr>
      <td>mCSM</td>
      <td>0.36</td>
      <td>1.54</td>
      <td>1.13</td>
    </tr>
    <tr>
      <td>Dynamut2</td>
      <td>0.34</td>
      <td>1.58</td>
      <td>1.15</td>
    </tr>
  </tbody>
</table>

A common challenge for many machine learning-based methods is the ability to satisfy the anti-symmetry condition, which states that the $Δ⁢Δ⁢G$ of a single point mutation must equal its reverse mutation with opposite sign (Pancotti et al., 2022). In order to assess this property, we tested RaSP on the Ssym+ data set, which includes both a direct and a reverse data set (Pancotti et al., 2022). The direct data set includes 352 variants and 19 experimental structures while the reverse data set includes 352 experimental structures for each of the corresponding reverse variants. RaSP achieves a Pearson correlation of 0.58 and a MAE of 1.01 kcal/mol on the direct data set, while it only achieves a Pearson correlation of 0.18 and a MAE of 1.82 kcal/mol on the reverse data set (Figure 3—figure supplement 2). The failure of RaSP to accurately capture anti-symmetric effects is expected following the one-sided training method and provides an interesting avenue for further method development.

Multiplexed assays of variant effects (MAVEs, also known as deep mutational scanning assays) leverage recent developments in high-throughput DNA synthesis and sequencing to probe large (e.g. thousands per protein) libraries of protein variants (Kinney and McCandlish, 2019). A particular type of MAVE termed ‘Variant Abundance by Massively Parallel sequencing’ (VAMP-seq) probes variant effects on cellular protein abundance (Matreyek et al., 2018), and correlates with both in vitro measurements (Matreyek et al., 2018; Suiter et al., 2020) and computational predictions (Cagiada et al., 2021) of protein stability. We therefore compared RaSP calculations with VAMP-seq data for three proteins and find that it correlates about as well as Rosetta calculations (Table 1 and Figure 3—figure supplement 4).

### Prediction of protein stability-change using computationally modelled structures

For maximal utility for proteome-wide stability predictions, our model should be generally robust to the quality of input protein structures (Caldararu et al., 2021). To test this, we used template-based (homology) modelling to generate structures of the four proteins selected from ProTherm that we analysed above. To minimize issues of leakage between training and testing data, we have recently used MODELLER (Martí-Renom et al., 2000; Webb and Sali, 2016) to construct models of the four proteins, using templates with decreasing sequence identities to the original structures (Valanciute et al., 2023). We used these structures as input to RaSP in order to calculate $Δ⁢Δ⁢G$ values to compare with experiments; we also performed similar tests using $Δ⁢Δ⁢G$ values calculated using Rosetta (Figure 4). Overall we find that both RaSP and Rosetta are relatively insensitive to the input models, with some decrease in accuracy for both methods when models are created using more distant homologues.

![Figure 4.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig4-v2.jpg)

**Figure 4.:** Pearson correlation coefficients ($ρ$) between experimental stability measurements and predictions using protein homology models with decreasing sequence identity to the target sequence. Pearson correlation coefficients were computed in the range of [–1;7] kcal/mol.

The development of AlphaFold 2 (Jumper et al., 2021) and other protein structure prediction algorithms has enabled large-scale generation of accurate structural models (Varadi et al., 2022). Recently, it has been shown that high-confidence models generated by AlphaFold 2 are sufficiently accurate to be used as input for protein stability predictions using for example FoldX and Rosetta (Akdel et al., 2022). We therefore tested whether AlphaFold 2 structures could similarly be used as input to RaSP. More specifically, we asked whether $Δ⁢Δ⁢G$ could be predicted as accurately from AlphaFold 2 structures as from crystal structures. We selected three proteins that each had two high-resolution crystal structures and used these as well as an AlphaFold 2 model to predict $Δ⁢Δ⁢G$. Overall we find a high correlation between the RaSP predictions from the pairs of crystal structures ($ρ¯=0.97$), only slightly greater than the correlation between values predicted from a crystal structure and an AlphaFold 2 structure ($ρ¯=0.94$) (Table 3). This correlation is highest in regions of the proteins where AlphaFold 2 is most confident about the structure prediction (i.e. residues with high pLDDT scores). Interpreting this observation is, however, complicated by the fact that low pLDDT scores are often found in loop regions that might have naturally lower $Δ⁢Δ⁢G$ scores, thus increasing the effects of noise and minor outliers on correlation scores. Overall, these results, together with those using the homology models above, indicate that RaSP can also deliver accurate predictions using computationally generated protein structures; we note that similar results have been obtained using other stability prediction methods (Akdel et al., 2022; Valanciute et al., 2023; Lihan et al., 2023; Keskin Karakoyun et al., 2023).

**Table 3.**
 Comparing RaSP predictions from crystal and AlphaFold 2 (AF2) structures.Pearson correlation coefficients ($ρ$) between RaSP $Δ⁢Δ⁢G$ predictions using either two different crystal structures or a crystal structure and an AlphaFold 2 structure for six test proteins: PRMT5 (X1: 6V0P_A, X2: 4GQB_A), PKM (X1: 6B6U_A, X2: 6NU5_A), FTH1 (X1: 4Y08_A, X2: 4OYN_A), FTL (X1: 5LG8_A, X2: 2FFX_J), PSMA2 (X1: 5LE5_A, X2: 5LE5_O) and GNB1 (X1: 6CRK_B, X2: 5UKL_B). We also divided the analysis into residues with high (pLDDT ≥ 0.9) and medium-low (pLDDT <0.9) pLDDT scores from AlphaFold 2.


<table>
  <thead>
    <tr>
      <th rowspan="2">Protein</th>
      <th colspan="3">All [ρ]</th>
      <th colspan="3">High AF2 pLDDT [ρ]</th>
      <th colspan="3">Medium-Low AF2 pLDDT [ρ]</th>
    </tr>
    <tr>
      <th>X1-X2</th>
      <th>X1-AF2</th>
      <th>X2-AF2</th>
      <th>X1-X2</th>
      <th>X1-AF2</th>
      <th>X2-AF2</th>
      <th>X1-X2</th>
      <th>X1-AF2</th>
      <th>X2-AF2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PRMT5</td>
      <td>0.93</td>
      <td>0.89</td>
      <td>0.95</td>
      <td>-</td>
      <td>0.90</td>
      <td>0.95</td>
      <td>-</td>
      <td>0.66</td>
      <td>0.89</td>
    </tr>
    <tr>
      <td>PKM</td>
      <td>0.99</td>
      <td>0.95</td>
      <td>0.95</td>
      <td>-</td>
      <td>0.95</td>
      <td>0.95</td>
      <td>-</td>
      <td>0.88</td>
      <td>0.89</td>
    </tr>
    <tr>
      <td>FTH1</td>
      <td>0.99</td>
      <td>0.97</td>
      <td>0.97</td>
      <td>-</td>
      <td>0.97</td>
      <td>0.97</td>
      <td>-</td>
      <td>0.92</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td>FTL</td>
      <td>0.97</td>
      <td>0.96</td>
      <td>0.97</td>
      <td>-</td>
      <td>0.96</td>
      <td>0.97</td>
      <td>-</td>
      <td>0.96</td>
      <td>0.94</td>
    </tr>
    <tr>
      <td>PSMA2</td>
      <td>0.99</td>
      <td>0.95</td>
      <td>0.95</td>
      <td>-</td>
      <td>0.96</td>
      <td>0.96</td>
      <td>-</td>
      <td>0.78</td>
      <td>0.80</td>
    </tr>
    <tr>
      <td>GNB1</td>
      <td>0.96</td>
      <td>0.94</td>
      <td>0.94</td>
      <td>-</td>
      <td>0.94</td>
      <td>0.94</td>
      <td>-</td>
      <td>0.93</td>
      <td>0.89</td>
    </tr>
  </tbody>
</table>

### Large-scale calculations of stability-changes and analysis of disease-causing missense variants

Protein stability has been shown to be an important driver of human disease (Casadio et al., 2011; Martelli et al., 2016; Nielsen et al., 2020) and knowledge about changes in protein stability can provide important mechanistic insights into the molecular origins of a disease (Abildgaard et al., 2023; Cagiada et al., 2021). In particular, predictions of changes in protein stability can help separate variants into mechanistic classes depending on how they affect protein function (Cagiada et al., 2022). In this light, developing accurate predictors of $Δ⁢Δ⁢G$ values is an important step in understanding the mechanisms behind human diseases.

Large-scale predictions often require models that are specifically suited for the task. As such, we designed RaSP to be fast, yet retain the accuracy of the Rosetta protocol. We benchmarked the speed of RaSP against both Rosetta and FoldX (well-established energy-function-based methods) (Kellogg et al., 2011; Schymkowitz et al., 2005) as well as two recent machine learning-based methods; ACDC-NN and ThermoNet (Benevenuta et al., 2021; Li et al., 2020; Table 4). We find that RaSP enables saturation mutagenesis $Δ⁢Δ⁢G$ calculations at a speed of ∼0.4 s per position—independent of total protein length—after pre-processing of the protein structure. At this speed, saturation mutagenesis scans are possible for most proteins in a few minutes—orders of magnitude faster than Rosetta (Table 4; note differences in hardware used for the two sets of calculations). Furthermore, we find that RaSP is also faster than the other machine learning-based methods that have not been optimized for large-scale applications. The ACDC-NN model is the closest performing model to RaSP in terms of speed, and ACDC-NN has also shown to have good predictive performance on experimental test data (Table 2). ACDC-NN is, however, somewhat slower than RaSP both in time for pre-processing and for computing $Δ⁢Δ⁢G$; it also uses information from multiple sequence alignments, which might not always be available.

**Table 4.**
 Run-time comparison of RaSP and four other methods for three test proteins ELOB (PDB: 4AJY_B, 107 residues), GCK (PBD: 4DCH_A, 434 residues) and F8 (PDB: 2R7E_A, 693 residues).The RaSP model is in total 480–1,036 times faster than Rosetta. RaSP, ACDC-NN and ThermoNet computations were performed using a single NVIDIA V100 16 GB GPU machine, while Rosetta and FoldX computations were parallelized and run on a server using 64 2.6 GHz AMD Opteron 6380 CPU cores. The number of $Δ⁢Δ⁢G$ computations per mutation was set to 3 for both Rosetta and FoldX. For ThermoNet, we expect that the pre-processing speed can be made comparable to Rosetta via parallelization.


<table>
  <thead>
    <tr>
      <th rowspan="2">Method</th>
      <th rowspan="2">Protein</th>
      <th colspan="3">Wall-clock time [s]</th>
    </tr>
    <tr>
      <th>Pre-processing</th>
      <th>Δ⁢Δ⁢G</th>
      <th>Δ⁢Δ⁢G/ residue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">RaSP</td>
      <td>ELOB</td>
      <td>7</td>
      <td>41</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>GCK</td>
      <td>11</td>
      <td>173</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>20</td>
      <td>270</td>
      <td>0.4</td>
    </tr>
    <tr>
      <td rowspan="3">Rosetta</td>
      <td>ELOB</td>
      <td>677</td>
      <td>44,324</td>
      <td>414.2</td>
    </tr>
    <tr>
      <td>GCK</td>
      <td>7,996</td>
      <td>118,361</td>
      <td>272.7</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>17,211</td>
      <td>133,178</td>
      <td>192.2</td>
    </tr>
    <tr>
      <td rowspan="3">FoldX</td>
      <td>ELOB</td>
      <td>78</td>
      <td>42,237</td>
      <td>394.7</td>
    </tr>
    <tr>
      <td>GCK</td>
      <td>728</td>
      <td>309,762</td>
      <td>713.7</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>1,306</td>
      <td>559,050</td>
      <td>806.7</td>
    </tr>
    <tr>
      <td rowspan="3">ACDC-NN</td>
      <td>ELOB</td>
      <td>81</td>
      <td>158</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>GCK</td>
      <td>169</td>
      <td>619</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>325</td>
      <td>1,080</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td rowspan="3">ThermoNet</td>
      <td>ELOB</td>
      <td>80,442</td>
      <td>884</td>
      <td>8.3</td>
    </tr>
    <tr>
      <td>GCK</td>
      <td>4,586,522</td>
      <td>4,227</td>
      <td>9.7</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>11,627,433</td>
      <td>8,732</td>
      <td>12.6</td>
    </tr>
  </tbody>
</table>

To demonstrate how the speed of RaSP enables large-scale applications, we used it to perform saturation scans for 1381 experimentally determined structures of human proteins or domains (see Methods for further details on selection criteria), yielding a data set of ∼ 8.8 million $Δ⁢Δ⁢G$ values. The $Δ⁢Δ⁢G$ values predicted by RaSP follow the expected distribution (Tokuriki et al., 2007; Nisthal et al., 2019) with a small number of stabilizing variants, a large number of slightly destabilizing variants and a long tail of very destabilizing variants (Figure 5—figure supplement 1).

As an example of the kinds of analyses that these large-scale calculations enable, we examined variants that have been observed in the human population. Specifically, we extracted validated disease-causing and benign variants from ClinVar (Landrum et al., 2018) and variants observed more broadly in the human population from the Genome Aggregation Database (gnomAD) (Karczewski et al., 2020), and annotated them with their predicted $Δ⁢Δ⁢G$ values (Figure 5). We find that benign variants generally only have a smaller effect on stability (median $Δ⁢Δ⁢G$ 0.54 kcal/mol, and 95% within the range –0.9–2.7 kcal/mol; Figure 5A) whereas many disease causing missense variants are predicted to be destabilizing (median $Δ⁢Δ⁢G$ 1.4 kcal/mol, and 95% within the range –1.4–6.7 kcal/mol; Figure 5A). Thus, a substantial fraction of the pathogenic variants are predicted to be destabilized to an extent that is likely to cause lowered abundance (Cagiada et al., 2021; Høie et al., 2022). We observe that this difference in median $Δ⁢Δ⁢G$ values between the benign and the pathogenic group is statistically significant using bootstrap sampling. We resample each of the pathogenic and benign distributions with replacement 104 times and compute the difference in medians between the two groups along with a 95% confidence interval (CI). Using this method, the difference in medians is estimated at 0.82 kcal/mol (CI: 0.73 kcal/mol – 0.93 kcal/mol).

![Figure 5.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig5-v2.jpg)

**Figure 5.:** The grey distribution shown in the background of all plots represents the distribution of $Δ⁢Δ⁢G$ values calculated using RaSP for all single amino acid changes in the 1,366 proteins that we analysed (15 of the 1381 proteins that we calculated $Δ⁢Δ⁢G$ for did not have variants in ClinVar or gnomAD and were therefore not included in this analysis). Each plot is also labelled with the median $Δ⁢Δ⁢G$ of the subset analysed as well as a range of $Δ⁢Δ⁢G$ values that cover 95% of the data in that subset (box plot shows median, quartiles and outliers). The plots only show values between –1 and 7 kcal/mol (for the full range see Figure 5—figure supplement 2). (A) Distribution of RaSP $Δ⁢Δ⁢G$ values for benign (blue) and pathogenic (tan) variants extracted from the ClinVar database (Landrum et al., 2018). We observe that the median RaSP $Δ⁢Δ⁢G$ value is significantly higher for pathogenic variants compared to benign variants using bootstrapping. (B) Distribution of RaSP $Δ⁢Δ⁢G$ values for variants with different allele frequencies (AF) extracted from the gnomAD database Karczewski et al., 2020 in the ranges (i) AF>10-2 (green), (ii) 10-2 > AF>10-4 (orange), and (iii) AF<10-4 (purple). We observe a gradual shift in the median RaSP $Δ⁢Δ⁢G$ going from common variants (AF>10-2) towards rarer ones (AF<10-4).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Histogram of $Δ⁢Δ⁢G$ values from saturation mutagenesis using RaSP on 1,366 PDB structures corresponding to ∼8.8 million predicted $Δ⁢Δ⁢G$ values.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** The grey distribution shown in the background of all plots represents the distribution of $Δ⁢Δ⁢G$ for all single amino acid changes in the 1366 proteins that we analysed. Each plot is also labelled with the median $Δ⁢Δ⁢G$ of the subset analysed as well as a range of $Δ⁢Δ⁢G$ values that cover 95% of the data in that subset (box plot shows median, quartiles and outliers). (A) Distribution of RaSP $Δ⁢Δ⁢G$ values for benign (blue) and pathogenic (tan) variants extracted from the ClinVar database (Landrum et al., 2018). We observe that the median RaSP $Δ⁢Δ⁢G$ value is higher for pathogenic variants compared to benign variants. (B) Distribution of RaSP $Δ⁢Δ⁢G$ values for variants with different allele frequencies (AF) extracted from the gnomAD database Karczewski et al., 2020 in the ranges (i) AF > 10-2 (green), (ii) 10-2 > AF > 10-4 (orange), (iii) AF < 10-4 (purple). We observe a gradual shift in the median RaSP $Δ⁢Δ⁢G$ going from common variants (AF> 10-2) towards rarer ones (AF< 10-4).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/82593/elife-82593-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Histogram of $Δ⁢Δ⁢G$ values from saturation mutagenesis using RaSP on predicted structures of the entire human proteome corresponding to ∼300 million predicted $Δ⁢Δ⁢G$ values predicted from 23,391 protein structures.

Similarly, variants that are common in the human population (i.e. with an allele frequency in gnomAD > 10-2) generally only have a small effect on the stability (median $Δ⁢Δ⁢G$ 0.41 kcal/mol), whereas rarer variants have a broader distribution including more destabilizing variants (Figure 5B). Thus, in line with previous observations (Casadio et al., 2011; Martelli et al., 2016; Stein et al., 2019) we find that loss of protein stability is likely to be the underlying cause for loss of function for a large fraction of pathogenic variants. Using the bootstrapping method described above, we observe that the difference in median $Δ⁢Δ⁢G$ values between the common (gnomAD > 10-2) and the rare (gnomAD < 10-4) variants is estimated at 0.35 kcal/mol (CI: 0.27 kcal/mol – 0.43 kcal/mol).

Following the prediction of ∼8.8 million RaSP $Δ⁢Δ⁢G$ values, we decided to expand our analysis to the entire human proteome corresponding to ∼ 300 million predicted RaSP $Δ⁢Δ⁢G$ values across 23,391 protein structures obtained from the AlphaFold2 database (Varadi et al., 2022; Figure 5—figure supplement 3); because of overlapping fragments in AlphaFold predictions for large proteins, this corresponds to ca. 230 million unique variants. We note that RaSP has only been trained and benchmarked on soluble, globular and folded proteins and may therefore not expected to perform equally well on proteins outside this category including e.g. membrane proteins and intrinsically disordered proteins. Furthermore, AlphaFold2 may not predict reliable structural models in regions that are highly flexible and disordered (Jumper et al., 2021; Varadi et al., 2022). For convenience, we however provide the data for all human proteins. Despite these caveats, we observe that the RaSP predictions follow the same expected distributional shape as described above. We believe that these predictions could serve as a fruitful starting point for large-scale studies of protein stability and have therefore made these RaSP predictions freely available online (see ‘Data and code availability’).

## Discussion

Here, we have presented a novel deep-learning-based model for making rapid predictions of protein stability changes using a combination of supervised and self-supervised methods. Our model uses the latent-space representation of a 3D convolutional neural network for protein structures as input to a supervised model to predict $Δ⁢Δ⁢G$. Our results show that the RaSP model performs on-par with the Rosetta protocol that we used as target for our optimization, but at a speed that is several orders of magnitude faster. We analysed RaSP’s sensitivity towards using predicted protein structures, and applied it to generate a unique and large set of stability-change predictions for 8.8 million variants of 1,381 human proteins. As an example of the kinds of applications that RaSP may enable, we analysed the role of protein stability for genetic diseases, and hope that this data and the RaSP model will be a broadly useful tool to study the effects of amino acid changes on protein stability.

## Methods

### A convolutional neural network for protein structures

We use a 3D convolutional neural network as a model to represent protein structures based on the architectures presented in Boomsma and Frellsen, 2017. During training, the model is tasked with predicting the amino acid type given its local 3D atomic environment. Specifically, for each residue in the polypeptide chain, the model aims to predict the amino acid type based on the local atomic environment lying inside a sphere centered on the $C_{\alpha}$ atom of the target residue to be predicted with a radius of 9 Å. Before prediction, all atoms in the target residue are removed from the environment. Each local spherical environment is parameterized using a Cartesian grid and so divided into multiple cubic voxels each with a volume of $(1A˚)^{3}$. Each cubic voxel has six input channels corresponding to the one-hot encoding of C, N, O, H, S, and P atoms. The model consists of a series of three 3D convolutional layers that is applied to the local spherical atomic environment. All convolutional filters have a size of $(3A˚)^{3}$ and the number of filters at each convolutional layer is 16, 32, and 64, respectively. The three 3D convolutional layers are connected using leaky ReLU activation (He et al., 2015), max pooling (Riesenhuber and Poggio, 1999) and batch normalization functions (Ioffe and Szegedy, 2015). We apply Gaussian blurring to the input local environment before the convolutional layers. After the convolutional layers, the output is flattened and the dimensionality is reduced by two fully connected layers with 100 and 20 nodes, respectively. Model predictions are optimized by minimizing the cross-entropy between the predicted 20-length vector and the one-hot encoded amino acid label.

We trained the above model on a data set of 2336 high resolution protein structures obtained using the PISCES server with maximal sequence identity set to 30% (Wang and Dunbrack, 2003). All structures were pre-processed using the Reduce program (Word et al., 1999) to add missing hydrogen atoms and OpenMM PDBFixer (Eastman et al., 2013) to correct for common PDB errors; during pre-processing, three proteins gave errors and were thus discarded. Out of the remaining 2333 proteins, 2099 proteins were used for training while 234 were withheld for validation. Optimization was performed using Adam (Kingma and Ba, 2014) with a learning rate of $3⋅10^{-4}$ and a batch size of 100 residues. After training, the representation model achieves a wild-type amino acid classification accuracy of 63% on a validation set (Figure 2—figure supplement 1).

### Downstream model architecture and training

We used the convolutional neural network described above to represent protein structures when predicting protein stability changes. Specifically, for each variant, the downstream model takes as input (i) a flattened 100-dimensional representation of the atomic environment extracted for the wild-type structure using the self-supervised model, (ii) one-hot encoded labels of the wild type and variant amino acid, and (iii) the amino acid frequencies of the wild type and variant amino acid in the PISCES set of proteins. These inputs are concatenated and passed through three fully connected layers with 128, 64, and 16 nodes, respectively, resulting in a scalar value. During training, this value is passed through a sigmoid function corresponding to the transformation of the target data described below. Between each layer, we apply batch normalization (Ioffe and Szegedy, 2015) and leaky ReLU activation (He et al., 2015). We train the model by minimizing the mean absolute error between the predicted values of the stability-change and Rosetta $Δ⁢Δ⁢G$ values, after being transformed using a switching function (see below).

We trained the downstream model using $Δ⁢Δ⁢G$ values from saturation mutagenesis of 35 training proteins and 10 validation proteins, and tested using 10 different proteins. Before training, we transformed all Rosetta $Δ⁢Δ⁢G$ values using a switching (Fermi) function to focus model training on the $Δ⁢Δ⁢G$ range from -1 to 7, as this is where Rosetta is expected to be most accurate (Kellogg et al., 2011), where most experimental values lie (Kumar, 2006; Ó Conchúir et al., 2015; Nisthal et al., 2019), and covering an important range for detecting missense variants that cause disease via loss of protein stability and abundance (Stein et al., 2019; Cagiada et al., 2021; Høie et al., 2022). The Fermi function was defined as:

$$
F(Δ⁢Δ⁢G)=\frac{1}{1+e^{-\beta⁢(Δ⁢Δ⁢G-\alpha)}}
$$

with $\beta=0.4$ and $\alpha=3.0$. Optimization was performed using Adam (Kingma and Ba, 2014) with a learning rate of $5⋅10^{-4}$ and a batch size of 40 variants. Stability changes for (disulfide-bonded) cystine residues were removed from the training, validation and test set as they are not predicted using our Rosetta protocol. In practice, this means that RaSP will tend to underestimate the magnitude of $Δ⁢Δ⁢G$ values for mutations at cysteine residues involved in disulfide-bonds and that these predicted $Δ⁢Δ⁢G$ values should therefore not be taken to be accurate.

### Rosetta protocol

We used Rosetta (GitHub SHA1 99d33ec59ce9fcecc5e4f3800c778a54afdf8504) and the the Cartesian $Δ⁢Δ⁢G$ protocol (Park et al., 2016) to predict $Δ⁢Δ⁢G$ values. Values from Rosetta values were divided by 2.9 to convert to a scale corresponding to kcal/mol (Park et al., 2016).

### Calculation of SASA

We analyse the differences in correlation between RaSP and Rosetta $Δ⁢Δ⁢G$ predictions at exposed and buried residues respectively (Figure 2—figure supplement 3). The solvent accessible surface area (SASA) was calculated using BioPython and default Sander and Rost values (Cock et al., 2009; Rost and Sander, 1994). The cut-off between exposed and buried residues was set at 0.2.

### Filtering of mega-scale data set

We tested the performance of RaSP on a recently published mega-scale folding stability experiment (Tsuboyama et al., 2022). We included variants with single amino acid substitutions with well-defined experimental $Δ⁢Δ⁢G$ values. As RaSP has only been trained on $Δ⁢Δ⁢G$ values from natural protein structures, we also decided to include only those in our test. Furthermore, we excluded any synonymous substitutions. The filtered data set contains a total of 164,524 variants across 164 protein domain structures.

### Speed test benchmarking

We compare the speed of RaSP to other predictors of $Δ⁢Δ⁢G$ namely Rosetta, FoldX, ACDC-NN and ThermoNet (Kellogg et al., 2011; Schymkowitz et al., 2005; Benevenuta et al., 2021; Li et al., 2020). The Rosetta protocol was implemented as described above. The FoldX protocol was implemented using FoldX version 5.0 with a custom script to enable full saturation mutagenesis calculations. ACDC-NN was implemented using the GitHub source code (https://github.com/compbiomed-unito/acdc-nn, Computational Biology and Medicine Group, 2023 accessed January 2023). ThermoNet was implemnted using the GitHub source code (https://github.com/gersteinlab/ThermoNet, Gerstein Lab, 2022 accessed January 2023).

### Selection of proteins and structures for large-scale analysis

Our selection of experimental structures was based on 5,557 human proteins annotated with cytosolic location. To make this list, we extracted UniProt identifiers from the human genome assembly GRCh38.p13 filtered for the Gene Ontology (Ashburner et al., 2000) term ‘cytosol’ (GO:0005829). We aligned the sequences of all chains of all PDB entries in the SIFTS map (Dana et al., 2019) (June 2021) to the UniProt sequences for the cytosolic proteins and calculated how much the protein structure in each PDB file covered the UniProt entries (explicitly considering mismatches, indels, residues that are not resolved in the structure, and modified residues). Based on these features, we calculated a score for each protein structure and the highest scoring structure was selected to represent a PDB entry. When calculating the score, we gave the highest priority to the coverage of the UniProt sequence and the experimental method. Specifically, given that RaSP was initially developed and benchmarked using crystal structures, we prioritized methods in the following order: (i) X-ray, (ii) cryo-electron microscopy, (iii) NMR. For our final selection, we chose 1,381 structures from the above selection, where the structure was of high quality in a canonical PDB format and where at least 50% of the UniProt sequence was covered by the structure.

### Benchmarking on the S669 dataset

We used RaSP to predict stability changes for 669 variants using 94 experimental structures from a recently described dataset (Pancotti et al., 2022). We note that one of the proteins in the S669 set (1XXN.pdb) is highly similar to one of the proteins we used to train our downstream model on (1C5H.pdb). We also used the Ssym+ data set (Pancotti et al., 2022), which includes 352 variants and 19 experimental structures for the ‘forward’ substitutions, and 352 experimental structures for each of the corresponding reverse variants.

### Selection of ClinVar and gnomAD variants

The extraction of variants from ClinVar and gnomAD is based on Tiemann et al., 2023. Briefly, we extracted data from gnomAD using an in-house database (scripts available at: https://github.com/KULL-Centre/PRISM/tree/main/software/make_prism_files, Linderstrøm-Lang Centre for Protein Science, University of Copenhagen, 2021 release-tag v0.1.1). This was constructed using exome data from gnomAD v2 and whole-genome data from gnomAD v3, selecting exome GRCh38 liftover for v2 and whole-genome files for v3, and annotated with Variant Effect Predictor with the GRCh38 release 100 human transcripts set from Ensembl. As previously described (Tiemann et al., 2023), we computed gnomAD allele frequencies for all protein variants from the extracted exome- and genome data combined (if present, otherwise solely for the exome- or genome allele frequencies). The reported allele frequencies are calculated as the sum of exome- and genome allele counts divided by the sum of total exome- and genome allele counts, and all DNA variants leading to the same protein-level variant were combined (Tiemann et al., 2023). Similarly, ClinVar data were extracted from an in-house database constructed using the NCBI data source: here (May 2021). For our analysis, only single nucleotide variants with a mapping to GRCh38 and with a rating of at least one star were used. We did not find any variants in gnomAD or ClinVar for 15 of the 1381 proteins that we calculated $Δ⁢Δ⁢G$ for; the data shown in Figure 5 thus refers only to 1366 proteins.

### Selection of data for human proteome analysis

The structures used for the human proteome analysis were obtained from the AlphaFold2 database UP000005640_9606_HUMAN_v2 (Varadi et al., 2022; Figure 5—figure supplement 3). The structures in the database were pre-processed following the RaSP protocol using Reduce and PDBFixer, but were otherwise unmodified so that each protein is defined by a single UniProt sequence and a single predicted structure. For longer proteins the AlphaFold2-predicted structures have been split into fragments; for those proteins we also split our RaSP predictions into corresponding fragments.

### Data and code availability

Scripts and data to repeat our analyses are available via: https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg/, where we also provide a link to run RaSP via resources at Google Colaboratory.

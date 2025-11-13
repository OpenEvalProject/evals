# Semantical and geometrical protein encoding toward enhanced bioactivity and thermostability

## Authors

- Yang Tan<sup>1</sup> ([ORCID: 0009-0004-7261-1705](https://orcid.org/0009-0004-7261-1705))
- Bingxin Zhou<sup>1</sup> ([ORCID: 0000-0002-3897-9766](https://orcid.org/0000-0002-3897-9766)) †
- Lirong Zheng<sup>5</sup> ([ORCID: 0000-0001-6803-5048](https://orcid.org/0000-0001-6803-5048))
- Guisheng Fan<sup>2</sup>
- Liang Hong<sup>1</sup> ([ORCID: 0000-0003-0107-336X](https://orcid.org/0000-0003-0107-336X)) †

### Affiliations

1. Shanghai-Chongqing Institute of Artificial Intelligence, Shanghai Jiao Tong University Chongqing China ([ROR:0220qvk04](https://ror.org/0220qvk04))
2. School of Information Science and Engineering, East China University of Science and Technology Shanghai China ([ROR:01vyrm377](https://ror.org/01vyrm377))
3. Zhangjiang Institute for Advanced Study, Shanghai Jiao Tong University Shanghai China ([ROR:0220qvk04](https://ror.org/0220qvk04))
4. Shanghai Artificial Intelligence Laboratory Shanghai China ([ROR:03wkvpx79](https://ror.org/03wkvpx79))
5. Shanghai Jiao Tong University, Institute of Natural Sciences Shanghai China ([ROR:0220qvk04](https://ror.org/0220qvk04))
6. Shanghai National Center for Applied Mathematics (SJTU Center), Shanghai Jiao Tong University Shanghai China ([ROR:0220qvk04](https://ror.org/0220qvk04))

† Corresponding author

## Abstract

Protein engineering is a pivotal aspect of synthetic biology, involving the modification of amino acids within existing protein sequences to achieve novel or enhanced functionalities and physical properties. Accurate prediction of protein variant effects requires a thorough understanding of protein sequence, structure, and function. Deep learning methods have demonstrated remarkable performance in guiding protein modification for improved functionality. However, existing approaches predominantly rely on protein sequences, which face challenges in efficiently encoding the geometric aspects of amino acids’ local environment and often fall short in capturing crucial details related to protein folding stability, internal molecular interactions, and bio-functions. Furthermore, there lacks a fundamental evaluation for developed methods in predicting protein thermostability, although it is a key physical property that is frequently investigated in practice. To address these challenges, this article introduces a novel pre-training framework that integrates sequential and geometric encoders for protein primary and tertiary structures. This framework guides mutation directions toward desired traits by simulating natural selection on wild-type proteins and evaluates variant effects based on their fitness to perform specific functions. We assess the proposed approach using three benchmarks comprising over 300 deep mutational scanning assays. The prediction results showcase exceptional performance across extensive experiments compared to other zero-shot learning methods, all while maintaining a minimal cost in terms of trainable parameters. This study not only proposes an effective framework for more accurate and comprehensive predictions to facilitate efficient protein engineering, but also enhances the in silico assessment system for future deep learning models to better align with empirical requirements. The PyTorch implementation is available at https://github.com/ai4protein/ProtSSN.

## Introduction

The diverse roles proteins play in nature necessitate their involvement in varied bio-functions, such as catalysis, binding, scaffolding, and transport. Advances in science and technology have positioned proteins, particularly those with desired catalytic and binding properties, to pivotal positions in medicine, biology, and scientific research (Zhou et al., 2024a). While wild-type proteins exhibit optimal bio-functionality in their native environments, industrial applications often demand adaptation to conditions such as high temperature, high pressure, strong acidity, and strong alkalinity. The constrained efficacy of proteins in meeting the stringent requirements of industrial functioning environments hinders their widespread applications (Woodley, 2013; Ismail et al., 2021; Jiang et al., 2023). Consequently, there arises a need to engineer these natural proteins to enhance their functionalities, aligning them with the demands of both industrial and scientific applications.

Analyzing the relationship between protein sequence and function yields valuable insights for engineering proteins with new or enhanced functions in synthetic biology. The intrinsic goal of protein engineering is to unveil highly functional sequences by navigating the intricate, high-dimensional surface of the fitness landscape (Yang et al., 2019), which delineates the relationship between amino acid (AA) sequences and the desired functional state. Predicting the effects of AA substitutions, insertions, and deletions (Riesselman et al., 2018; Gray et al., 2018; Notin et al., 2022a) in proteins, that is, mutation, thus allows researchers to dissect how changes in the AA sequence can impact the protein’s catalytic efficiency, stability, and binding affinity (Shin et al., 2021). However, the extensive, non-contiguous search space of AA combinations poses challenges for conventional methods, such as rational design (Aprile et al., 2020) or directed evolution (Wang et al., 2021), in efficiently and effectively identifying protein variants with desired properties. In response, deep learning has emerged as a promising solution that proposes favorable protein variants with high fitness.

Deep learning approaches have been instrumental in advancing scientific insights into proteins, predominantly categorized into sequence-based and structure-based methods. Autoregressive protein language models (Notin et al., 2022a; Madani et al., 2023) interpret AA sequences as raw text to generate with self-attention mechanisms (Vaswani et al., 2017). Alternatively, masked language modeling objectives develop attention patterns that correspond to the residue–residue contact map of the protein (Meier et al., 2021; Rao et al., 2021b; Rives et al., 2021; Vig et al., 2021; Brandes et al., 2022; Lin et al., 2023). Other methods start from a multiple sequence alignment, summarizing the evolutionary patterns in target proteins (Riesselman et al., 2018; Frazer et al., 2021; Rao et al., 2021a). These methods result in a strong capacity for discovering the hidden protein space. However, the many-to-one relationship of both sequence-to-structure and structure-to-function projections requires excessive training input or substantial learning resources, which raises concerns regarding the efficiency of these pathways when navigating the complexities of the vast sequence space associated with a target function. Moreover, the overlooked local environment of proteins hinders the model’s ability to capture structure-sensitive properties that impact protein’s thermostability, interaction with substrates, and catalytic process (Zhao et al., 2022; Koehler Leman et al., 2023). Alternatively, structure-based modeling methods serve as an effective enhancement to complement sequence-oriented inferences for proteins with their local environment (Tan et al., 2024e; Zhou et al., 2024c; Yi et al., 2024; Zhou et al., 2024b; Tan et al., 2024c). Given that core mutations often induce functional defects through subtle disruptions to structure or dynamics (Roscoe et al., 2013), incorporating protein geometry into the learning process can offer valuable insights into stabilizing protein functioning. Recent efforts have been made to encode geometric information of proteins for topology-sensitive tasks such as molecule binding (Jin et al., 2021; Myung et al., 2022; Kong et al., 2023) and protein properties prediction (Zhang et al., 2022; Tan et al., 2024d; Tan et al., 2024a). Nevertheless, structure encoders fall short in capturing non-local connections for AAs beyond their contact region and overlook correlations that do not conform to the ‘structure–function determination’ heuristic.

There is a pressing need to develop a novel framework that overcomes the limitations inherent in individual implementations of sequence or structure-based investigations. To this end, we introduce ProtSSN to assimilate the semantics and topology of Proteins from their Sequence and Structure with deep neural Networks. ProtSSN incorporates the intermediate state of protein structures and facilitates the discovery of an efficient and effective trajectory for mapping protein sequences to functionalities. The developed model extends the generalization and robustness of self-supervised protein language models while maintaining low computational costs, thereby facilitating self-supervised training and task-specific customization. A funnel-shaped learning pipeline, as depicted in Figure 1, is designed due to the limited availability of protein crystal structures compared to observed protein sequences. Initially, the linguistic embedding establishes the semantic and grammatical rules in AA chains by inspecting millions of protein sequences. The topological embedding then enhances the interactions among locally connected AAs. Since a geometry can be placed or observed by different angles and positions in space, we represent proteins’ topology by graphs and enhance the model’s robustness and efficiency with a rotation and translation equivariant graph representation learning scheme.

![Figure 1.](https://cdn.elifesciences.org/articles/98033/elife-98033-fig1-v1.jpg)

**Figure 1.:** The encoded hidden representation can be used for downstream tasks such as variants effect prediction that recognizes the impact of mutating a few sites of a protein on its functionality.

The pre-trained ProtSSN demonstrates its feasibility across a broad range of mutation effect prediction benchmarks covering catalysis, interaction, and thermostability. Mutation effects prediction serves as a common in silico assessment for evaluating the capability of an established deep learning framework in identifying favorable protein variants. With the continuous evolution of deep mutation scanning techniques and other high-throughput technologies, benchmark datasets have been curated to document fitness changes in mutants across diverse proteins with varying degrees of combinatorial and random modifications (Moal and Fernández-Recio, 2012; Nikam et al., 2021; Velecký et al., 2022). ProteinGym v1 (Notin et al., 2023) comprehends fitness scoring of mutants to catalytic activity and binding affinity across over 200 well-studied proteins of varying deep mutational scanning (DMS) assays and taxa. Each protein includes tens of thousands of mutants documented from high-throughput screening techniques. While ProteinGym v1 initiates the most comprehensive benchmark dataset for mutants toward different properties enhancement, these fitness scores are normalized and simplified into several classes without further specifications. For instance, a good portion of protein assays is scored by their stability, which, in practice, is further categorized into thermostability, photostability, pH-stability, etc. Moreover, these stability properties should be discussed under certain environmental conditions, such as pH and temperature. Unfortunately, these detailed attributes are excluded in ProteinGym v1. Since a trade-off relationship emerges between activity and thermostability (Zheng et al., 2022), protein engineering in practice extends beyond enhancing catalytic activities to maintaining or increasing thermostability for prolonged functional lifetimes and applications under elevated temperatures and chemical conditions (Liu et al., 2019). Consequently, there is a need to enrich mutation effect prediction benchmarks that evaluate the model’s efficacy in capturing variant effects concerning thermostability under distinct experimental conditions. In this study, we address the mutation effect prediction tasks on thermostability with DTm and DDG, two new single-site mutation benchmarks that measure thermostability using ΔTm and ΔΔG values, respectively. Both benchmarks group experimental assays based on the protein–condition combinations. These two datasets supplement the publicly available DMS assay benchmarks and facilitate ready-to-use assessment for future deep learning methods toward protein thermostability enhancement.

This work fulfills practical necessities in the development of deep learning methods for protein engineering from three distinct perspectives. Firstly, the developed ProtSSN employs self-supervised learning during training to obviate the necessity for additional supervision in downstream tasks. This zero-shot scenario is desirable due to the scarcity of experimental results, as well as the ‘cold-start’ situation common in many wet lab experiments. Secondly, the trained model furnishes robust and meaningful approximations to the joint distribution of the entire AA chain, thereby augmenting the epistatic effect (Sarkisyan et al., 2016; Khersonsky et al., 2018) in deep mutations. This augmentation stems from the model’s consideration of the nonlinear combinatorial effects of AA sites. Additionally, we complement the existing dataset of DMS assay with additional benchmark assays related to protein–environment interactions, specifically focusing on thermostability—an integral objective in numerous protein engineering projects.

## Results

### Variant effect prediction

We commence our investigation by assessing the predictive performance of ProtSSN on four benchmark datasets using state-of-the-art (SOTA) protein learning models. We deploy different versions of ProtSSN that learns kNN graphs with $k\in{10,20,30}$ and $h\in{512,768,1,280}$ hidden neurons in each of the six Equivariant Graph Neural Networks EGNN layers. For all baselines, their performance on DTm and DDG is reproduced with the official implementation listed in Table 5, and the scores on ProteinGym v1 are retrieved from https://proteingym.org/benchmarks by Notin et al., 2023. As visualized in Figure 2 and reported in Table 1, ProtSSN demonstrated exceptional predictive performance with a significantly smaller number of trainable parameters when predicting the function and thermostability of mutants.

![Figure 2.](https://cdn.elifesciences.org/articles/98033/elife-98033-fig2-v1.jpg)

**Figure 2.:** Number of trainable parameters and Spearman’s $ρ$ correlation on DTm, DDG, and ProteinGym v1, with the medium value located by the dashed lines.Dot, cross, and diamond markers represent sequence-based, structure-based, and sequence-structure models, respectively.

**Table 1.**
 Spearman’s $ρ$ correlation of variant effect prediction by with zero-shot methods on DTm, DDG, and ProteinGym v1.


<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th rowspan="2">Version</th>
      <th># Params</th>
      <th rowspan="2">DTm</th>
      <th rowspan="2">DDG</th>
      <th colspan="6">ProteinGym v1</th>
    </tr>
    <tr>
      <th>(million)</th>
      <th>Activity</th>
      <th>Binding</th>
      <th>Expression</th>
      <th>Organismal</th>
      <th>Stability</th>
      <th>Overall fitness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="11">Sequence encoder</td>
    </tr>
    <tr>
      <td rowspan="4">RITA</td>
      <td>Small</td>
      <td>30</td>
      <td>0.122</td>
      <td>0.143</td>
      <td>0.294</td>
      <td>0.275</td>
      <td>0.337</td>
      <td>0.327</td>
      <td>0.289</td>
      <td>0.304</td>
    </tr>
    <tr>
      <td>Medium</td>
      <td>300</td>
      <td>0.131</td>
      <td>0.188</td>
      <td>0.352</td>
      <td>0.274</td>
      <td>0.406</td>
      <td>0.371</td>
      <td>0.348</td>
      <td>0.350</td>
    </tr>
    <tr>
      <td>Large</td>
      <td>680</td>
      <td>0.213</td>
      <td>0.236</td>
      <td>0.359</td>
      <td>0.291</td>
      <td>0.422</td>
      <td>0.374</td>
      <td>0.383</td>
      <td>0.366</td>
    </tr>
    <tr>
      <td>xlarge</td>
      <td>1,200</td>
      <td>0.221</td>
      <td>0.264</td>
      <td>0.402</td>
      <td>0.302</td>
      <td>0.423</td>
      <td>0.387</td>
      <td>0.445</td>
      <td>0.373</td>
    </tr>
    <tr>
      <td rowspan="5">ProGen2</td>
      <td>Small</td>
      <td>151</td>
      <td>0.135</td>
      <td>0.194</td>
      <td>0.333</td>
      <td>0.275</td>
      <td>0.384</td>
      <td>0.337</td>
      <td>0.349</td>
      <td>0.336</td>
    </tr>
    <tr>
      <td>Medium</td>
      <td>764</td>
      <td>0.226</td>
      <td>0.214</td>
      <td>0.393</td>
      <td>0.296</td>
      <td>0.436</td>
      <td>0.381</td>
      <td>0.396</td>
      <td>0.380</td>
    </tr>
    <tr>
      <td>Base</td>
      <td>764</td>
      <td>0.197</td>
      <td>0.253</td>
      <td>0.396</td>
      <td>0.294</td>
      <td>0.444</td>
      <td>0.379</td>
      <td>0.383</td>
      <td>0.379</td>
    </tr>
    <tr>
      <td>Large</td>
      <td>2700</td>
      <td>0.181</td>
      <td>0.226</td>
      <td>0.406</td>
      <td>0.294</td>
      <td>0.429</td>
      <td>0.379</td>
      <td>0.396</td>
      <td>0.381</td>
    </tr>
    <tr>
      <td>xlarge</td>
      <td>6400</td>
      <td>0.232</td>
      <td>0.270</td>
      <td>0.402</td>
      <td>0.302</td>
      <td>0.423</td>
      <td>0.387</td>
      <td>0.445</td>
      <td>0.392</td>
    </tr>
    <tr>
      <td rowspan="4">ProtTrans</td>
      <td>bert</td>
      <td>420</td>
      <td>0.268</td>
      <td>0.313</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>bert_bfd</td>
      <td>420</td>
      <td>0.217</td>
      <td>0.293</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>t5_xl_uniref50</td>
      <td>3000</td>
      <td>0.310</td>
      <td>0.365</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>t5_xl_bfd</td>
      <td>3000</td>
      <td>0.239</td>
      <td>0.334</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="3">Tranception</td>
      <td>Small</td>
      <td>85</td>
      <td>0.119</td>
      <td>0.169</td>
      <td>0.287</td>
      <td>0.349</td>
      <td>0.319</td>
      <td>0.270</td>
      <td>0.258</td>
      <td>0.288</td>
    </tr>
    <tr>
      <td>Medium</td>
      <td>300</td>
      <td>0.189</td>
      <td>0.256</td>
      <td>0.349</td>
      <td>0.285</td>
      <td>0.409</td>
      <td>0.362</td>
      <td>0.342</td>
      <td>0.349</td>
    </tr>
    <tr>
      <td>Large</td>
      <td>700</td>
      <td>0.197</td>
      <td>0.284</td>
      <td>0.401</td>
      <td>0.289</td>
      <td>0.415</td>
      <td>0.389</td>
      <td>0.381</td>
      <td>0.375</td>
    </tr>
    <tr>
      <td>ESM-1v</td>
      <td>-</td>
      <td>650</td>
      <td>0.279</td>
      <td>0.266</td>
      <td>0.390</td>
      <td>0.268</td>
      <td>0.431</td>
      <td>0.362</td>
      <td>0.476</td>
      <td>0.385</td>
    </tr>
    <tr>
      <td>ESM-1b</td>
      <td>-</td>
      <td>650</td>
      <td>0.271</td>
      <td>0.343</td>
      <td>0.428</td>
      <td>0.289</td>
      <td>0.427</td>
      <td>0.351</td>
      <td>0.500</td>
      <td>0.399</td>
    </tr>
    <tr>
      <td rowspan="5">ESM2</td>
      <td>t12</td>
      <td>35</td>
      <td>0.214</td>
      <td>0.216</td>
      <td>0.314</td>
      <td>0.292</td>
      <td>0.364</td>
      <td>0.218</td>
      <td>0.439</td>
      <td>0.325</td>
    </tr>
    <tr>
      <td>t30</td>
      <td>150</td>
      <td>0.288</td>
      <td>0.317</td>
      <td>0.391</td>
      <td>0.328</td>
      <td>0.425</td>
      <td>0.305</td>
      <td>0.510</td>
      <td>0.392</td>
    </tr>
    <tr>
      <td>t33</td>
      <td>650</td>
      <td>0.330</td>
      <td>0.392</td>
      <td>0.425</td>
      <td>0.339</td>
      <td>0.415</td>
      <td>0.338</td>
      <td>0.523</td>
      <td>0.419</td>
    </tr>
    <tr>
      <td>t36</td>
      <td>3000</td>
      <td>0.327</td>
      <td>0.351</td>
      <td>0.417</td>
      <td>0.322</td>
      <td>0.425</td>
      <td>0.379</td>
      <td>0.509</td>
      <td>0.410</td>
    </tr>
    <tr>
      <td>t48</td>
      <td>15,000</td>
      <td>0.311</td>
      <td>0.252</td>
      <td>0.405</td>
      <td>0.318</td>
      <td>0.425</td>
      <td>0.388</td>
      <td>0.488</td>
      <td>0.405</td>
    </tr>
    <tr>
      <td>CARP</td>
      <td>-</td>
      <td>640</td>
      <td>0.288</td>
      <td>0.333</td>
      <td>0.395</td>
      <td>0.274</td>
      <td>0.419</td>
      <td>0.364</td>
      <td>0.414</td>
      <td>0.373</td>
    </tr>
    <tr>
      <td colspan="11">Structure encoder</td>
    </tr>
    <tr>
      <td>ESM-if1</td>
      <td>-</td>
      <td>142</td>
      <td>0.395</td>
      <td>0.409</td>
      <td>0.368</td>
      <td>0.392</td>
      <td>0.403</td>
      <td>0.324</td>
      <td>0.624</td>
      <td>0.422</td>
    </tr>
    <tr>
      <td colspan="11">Sequence + structure encoder</td>
    </tr>
    <tr>
      <td>MIF-ST</td>
      <td>-</td>
      <td>643</td>
      <td>0.400</td>
      <td>0.406</td>
      <td>0.390</td>
      <td>0.323</td>
      <td>0.432</td>
      <td>0.373</td>
      <td>0.486</td>
      <td>0.401</td>
    </tr>
    <tr>
      <td rowspan="2">SaProt</td>
      <td>Masked</td>
      <td>650</td>
      <td>0.382</td>
      <td>-</td>
      <td>0.459</td>
      <td>0.382</td>
      <td>0.485</td>
      <td>0.371</td>
      <td>0.583</td>
      <td>0.456</td>
    </tr>
    <tr>
      <td>Unmasked</td>
      <td>650</td>
      <td>0.376</td>
      <td>0.359</td>
      <td>0.450</td>
      <td>0.376</td>
      <td>0.460</td>
      <td>0.372</td>
      <td>0.577</td>
      <td>0.447</td>
    </tr>
    <tr>
      <td rowspan="2">ProtSSN (ours)</td>
      <td>k20_h512</td>
      <td>148</td>
      <td>0.419</td>
      <td>0.442</td>
      <td>0.458</td>
      <td>0.371</td>
      <td>0.436</td>
      <td>0.387</td>
      <td>0.566</td>
      <td>0.444</td>
    </tr>
    <tr>
      <td>Ensemble</td>
      <td>1467</td>
      <td>0.425</td>
      <td>0.440</td>
      <td>0.466</td>
      <td>0.371</td>
      <td>0.451</td>
      <td>0.398</td>
      <td>0.568</td>
      <td>0.451</td>
    </tr>
  </tbody>
</table>

_The top three are highlighted by first, second, and third._

Compared to protein language models (Figure 2, colored circles), ProtSSN benefits from abundant structure information to more accurately capture the overall protein characteristics, resulting in enhanced thermostability and thus achieving higher correlation scores on DTm and DDG. This is attributed to the compactness of the overall architecture as well as the presence of stable local structures such as alpha helices and beta sheets, both of which are crucial to protein thermostability by providing a framework that resists unfolding at elevated temperatures (Robinson-Rechavi et al., 2006). Consequently, the other two structures involved models, that is, ESM-if1 and MIF-ST, also exhibit higher performance on the two thermostability benchmarks.

On the other hand, although protein language models can typically increase their scale, that is, the number of trainable parameters, to capture more information from sequences, they cannot fully replace the role of the structure-based analysis. This observation aligns with the mechanism of protein functionality, where local structures (such as binding pockets and catalytic pockets) and the overall structure (such as conformational changes and allosteric effect) are both crucial for binding and catalysis (Sheng et al., 2014). Unlike the thermostability benchmarks, the discrepancies between structure-involved models and protein language models are mitigated in ProteinGym v1 by increasing the model scale. In summary, structure-based and sequence-based methods are suitable for different types of assays, but a comprehensive framework (such as ProtSSN) demonstrates superior overall performance compared to large-scale language models. Moreover, ProtSSN demonstrates consistency in providing high-quality fitness predictions of thermostability. We randomly bootstrap 50% of the samples from DTm and DDG for 10 independent runs, the results are reported In Table 3 for both the average performance and the standard deviation. ProtSSN achieves top performance with minimal variance.

### Ablation study

The effectiveness of ProtSSN with different modular designs is examined by its performance on the early released version ProteinGym v0 (Notin et al., 2022a) with 86 DMS assays. For the ablation study, the results are summarized in Figure 3a–d, where each record is subject to a combination of key arguments under investigation. For instance, in the top orange box of Figure 3a, we report all ablation results that utilize six EGNN layers for graph convolution, regardless of the different scales of ESM2 or the definitions of node attributes. For all modules investigated in this section, we separately discuss their influence on predicting mutation effects when modifying a single site or an arbitrary number of sites. The two cases are marked on the y-axis by ‘single’ and ‘all’, respectively.

![Figure 3.](https://cdn.elifesciences.org/articles/98033/elife-98033-fig3-v1.jpg)

**Figure 3.:** Each record represents the average Spearman’s correlation of all assays. (a) Performance using different structure encoders: Equivariant Graph Neural Networks (EGNN) (orange) versus GCN/GAT (purple). (b) Performance using different node attributes: ESM2-embedded hidden representation (orange) versus one-hot encoding (purple). (c) Performance with varying numbers of EGNN layers. (d) Performance with different versions of ESM2 for sequence encoding. (e) Performance using different amino acid perturbation strategies during pre-training.

#### Inclusion of roto-translation equivariance

We assess the effect of incorporating rotation and translation equivariance for protein geometric and topological encoding. Three types of graph convolutions are compared, including GCN (Kipf and Welling, 2017), GAT (Veličković et al., 2018), and EGNN (Satorras et al., 2021). The first two are classic non-equivariant graph convolutional methods, and the last one, which we apply in the main algorithm, preserves roto-translation equivariance. We fix the number of EGNN layers to 6 and examine the performance of the other two methods with either 4 or 6 layers. We find that integrating equivariance when embedding protein geometry would significantly improve prediction performance.

#### Sequence encoding

We next investigate the benefits of defining data-driven node attributes for protein representation learning. We compare the performance of models trained on two sets of graph inputs: the first set defines its AA node attributes through trained ESM2 (Lin et al., 2023), while the second set uses one-hot encoded AAs for each node. A clear advantage of using hidden representations by prefix models over hardcoded attributes is evident from the results presented in Figure 3b.

#### Depth of EGNN

Although graph neural networks can extract topological information from geometric inputs, it is vital to select an appropriate number of layers for the module to deliver the most expressive node representation without encountering the oversmoothing problem. We investigate a wide range of choices for the number of EGNN layers among ${6,12,18}$. As reported in Figure 3c, embedding graph topology with deeper networks does not lead to performance improvements. A moderate choice of six EGNN layers is sufficient for our learning task.

#### Scale of ESM

We also evaluate ProtSSN on different choices of language embedding dimensions to study the trade-off between computational cost and input richness. Various scales of prefix models, including ${8,150,650,3000}$ millions of parameters, have been applied to produce different sequential embeddings with ${320,640,1280,2560}$ dimensions, respectively. Figure 3d reveals a clear preference for ESM2-t33, which employs 650 million parameters to achieve optimal model performance with the best stability. Notably, a higher dimension and richer semantic expression do not always yield better performance. A performance degradation is observed at ESM2 with 3 billion parameters.

### AA perturbation strategies

ProtSSN utilizes noise sampling at each epoch on the node attributes to emulate random mutations in nature. This introduction of noise directly affects the node attribute input to the graphs. Alongside the ‘mutate-then-recode’ method we implemented in the main algorithm, we examined four additional strategies to perturb the input data during training. The construction of these additional strategies is detailed below, and their corresponding Spearman’s $ρ$ on ProteinGym v0 is given in Figure 3e.

#### Global average

Suppose the encoded sequential representation of a node is predominantly determined by its residue. In essence, the protein sequence encoder will return similar embeddings for nodes of the same residue, albeit at different positions within a protein. With this premise, the first strategy replaces the node embedding for perturbed nodes with the average representations of the same residues. For example, when perturbing an AA to glycine, an overall representation of glycine is assigned by extracting and average-pooling all glycine representations from the input sequence.

#### Sliding window

The presumption in the previous method neither aligns with the algorithmic design nor biological heuristics. Self-attention discerns the interaction of the central token with its neighbors across the entire document (protein). The representation of a residue is influenced by both its neighbors’ residues and locations. Thus, averaging embeddings of residues from varying positions is likely to forfeit positional information of the modified residue. For this purpose, we consider a sliding window of size 3 along the protein sequence.

#### Gaussian noise

The third option regards node embeddings of AA as hidden vectors and imposes white noise on the vector values. We define the mean = 0 and variance = 0.5 on the noise, making the revised node representation $𝒗~=𝒗+𝒩⁢(0,0.5)$.

#### Mask

Finally, we employ the masking technique prevalent in masked language modeling and substitute the perturbed residue token with a special <mask> token. The prefix language model will interpret it as a novel token and employ self-attention mechanisms to assign a new representation to it. We utilize the same hyperparameter settings as that of BERT (Devlin et al., 2018) and choose 15% of tokens per iteration as potentially influenced subjects. Specifically, 80% of these subjects are replaced with <mask>, 10% of them are replaced randomly (to other residues), and the remaining 10% stay unchanged.

### Folding methods

The analysis of protein structure through topological embeddings poses challenges due to the inherent difficulty in obtaining accurate structural observations through experimental techniques such as NMR (Wüthrich, 1990) and cryo-EM (Elmlund et al., 2017). As a substitution, we use in silico folding models such as AlphaFold2 (Jumper et al., 2021) and ESMFold (Lin et al., 2023). Although these folding methods may introduce additional errors due to the inherent uncertainty or inaccuracy in structural predictions, we investigate the robustness of our model in the face of potential inaccuracies introduced by these folding strategies.

Table 2 examines the impact of different folding strategies on the performance of DMS predictions for ESM-if1, MIF-ST, and ProtSSN. Although the performance based on ESMFold-derived protein structures generally lags behind structures folded by AlphaFold2, the minimal difference between the two strategies across all four benchmarks validates the robustness of our ProtSSN in response to variations in input protein structures. We deliberately divide the assays in ProteinGym v0 (Notin et al., 2022a) into two groups of interaction (e.g., binding and stability) and catalysis (e.g., activity), as the former is believed more sensitive to the structure of the protein (Robertson and Murphy, 1997).

**Table 2.**
 Influence of folding strategies (AlphaFold2 and ESMFold) on prediction performance for structure-involved models.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">DTm</th>
      <th colspan="3">DDG</th>
      <th colspan="3">ProteinGym-interaction</th>
      <th colspan="3">ProteinGym-catalysis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>AlphaFold2</td>
      <td>ESMFold</td>
      <td>diff ↓</td>
      <td>AlphaFold2</td>
      <td>ESMFold</td>
      <td>diff↓</td>
      <td>AlphaFold2</td>
      <td>ESMFold</td>
      <td>diff↓</td>
      <td>AlphaFold2</td>
      <td>ESMFold</td>
      <td>diff↓</td>
    </tr>
    <tr>
      <td>Avg. pLDDT</td>
      <td>90.86</td>
      <td>83.22</td>
      <td>-</td>
      <td>95.19</td>
      <td>86.03</td>
      <td>-</td>
      <td>82.86</td>
      <td>65.69</td>
      <td>-</td>
      <td>85.80</td>
      <td>73.45</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ESM-if1</td>
      <td>0.395</td>
      <td>0.371</td>
      <td>0.024</td>
      <td>0.457</td>
      <td>0.488</td>
      <td>–0.031</td>
      <td>0.351</td>
      <td>0.259</td>
      <td>0.092</td>
      <td>0.386</td>
      <td>0.368</td>
      <td>0.018</td>
    </tr>
    <tr>
      <td>MIF-ST</td>
      <td>0.400</td>
      <td>0.378</td>
      <td>0.022</td>
      <td>0.438</td>
      <td>0.423</td>
      <td>–0.015</td>
      <td>0.390</td>
      <td>0.327</td>
      <td>0.063</td>
      <td>0.408</td>
      <td>0.388</td>
      <td>0.020</td>
    </tr>
    <tr>
      <td>k30_h1280</td>
      <td>0.384</td>
      <td>0.370</td>
      <td>0.014</td>
      <td>0.396</td>
      <td>0.390</td>
      <td>0.006</td>
      <td>0.398</td>
      <td>0.373</td>
      <td>0.025</td>
      <td>0.443</td>
      <td>0.439</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>k30_h768</td>
      <td>0.359</td>
      <td>0.356</td>
      <td>0.003</td>
      <td>0.378</td>
      <td>0.366</td>
      <td>0.012</td>
      <td>0.400</td>
      <td>0.374</td>
      <td>0.026</td>
      <td>0.442</td>
      <td>0.436</td>
      <td>0.006</td>
    </tr>
    <tr>
      <td>k30_h512</td>
      <td>0.413</td>
      <td>0.399</td>
      <td>0.014</td>
      <td>0.408</td>
      <td>0.394</td>
      <td>0.014</td>
      <td>0.400</td>
      <td>0.372</td>
      <td>0.028</td>
      <td>0.447</td>
      <td>0.442</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>k20_h1280</td>
      <td>0.415</td>
      <td>0.391</td>
      <td>0.024</td>
      <td>0.429</td>
      <td>0.410</td>
      <td>0.019</td>
      <td>0.399</td>
      <td>0.365</td>
      <td>0.034</td>
      <td>0.446</td>
      <td>0.441</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>k20_h768</td>
      <td>0.415</td>
      <td>0.403</td>
      <td>0.012</td>
      <td>0.419</td>
      <td>0.397</td>
      <td>0.022</td>
      <td>0.401</td>
      <td>0.370</td>
      <td>0.031</td>
      <td>0.449</td>
      <td>0.442</td>
      <td>0.007</td>
    </tr>
    <tr>
      <td>k20_h512</td>
      <td>0.419</td>
      <td>0.395</td>
      <td>0.024</td>
      <td>0.441</td>
      <td>0.432</td>
      <td>0.009</td>
      <td>0.406</td>
      <td>0.371</td>
      <td>0.035</td>
      <td>0.449</td>
      <td>0.439</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>k10_h1280</td>
      <td>0.406</td>
      <td>0.391</td>
      <td>0.015</td>
      <td>0.426</td>
      <td>0.411</td>
      <td>0.015</td>
      <td>0.396</td>
      <td>0.365</td>
      <td>0.031</td>
      <td>0.440</td>
      <td>0.434</td>
      <td>0.006</td>
    </tr>
    <tr>
      <td>k10_h768</td>
      <td>0.400</td>
      <td>0.391</td>
      <td>0.009</td>
      <td>0.414</td>
      <td>0.400</td>
      <td>0.014</td>
      <td>0.379</td>
      <td>0.349</td>
      <td>0.030</td>
      <td>0.431</td>
      <td>0.421</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>k10_h512</td>
      <td>0.383</td>
      <td>0.364</td>
      <td>0.019</td>
      <td>0.424</td>
      <td>0.414</td>
      <td>0.010</td>
      <td>0.389</td>
      <td>0.364</td>
      <td>0.025</td>
      <td>0.440</td>
      <td>0.432</td>
      <td>0.008</td>
    </tr>
  </tbody>
</table>

_The top three are highlighted by first, second, and third._

ProtSSN emerges as the most robust method, maintaining consistent performance across different folding strategies, which underscores the importance of our model’s resilience to variations in input protein structures. The reported performance difference for both ESM-if1 and MIF-ST is 3–5 times higher than that of ProtSSN. The inconsistency between the optimal results for DDG and the scores reported in Table 1 comes from the utilization of crystal structures in the main results. Another noteworthy observation pertains to the performance of ESM-if1 and MIF-ST on DDG. In this case, predictions based on ESMFold surpass those based on AlphaFold2, even outperforming predictions derived from crystal structures. However, the superior performance of these methods with ESMFold hinges on inaccurate protein structures, rendering them less reliable.

### Performance enhancement with MSA and ensemble

We extend the evaluation on ProteinGym v0 to include a comparison of our individual-sequence-level, zero-shot ProtSSN with methods that include MSAs (which we consider here, ‘few-shot’ methods [Meier et al., 2021]). The details are reported in Table 3, where the performance of baseline methods is retrieved from https://github.com/OATML-Markslab/ProteinGym, copy archived at ProteinGym, 2024. For ProtSSN, we employ an ensemble of nine models with varying sizes of kNN graphs ($k\in{10,20,30}$) and EGNN hidden neurons (${512,768,1280}$), as discussed previously. The MSA depth reflects the number of MSA sequences that can be found for the protein, which influences the quality of MSA-based methods.

**Table 3.**
 Variant effect prediction on ProteinGym v0 with both zero-shot and few-shot methods.Results are retrieved from Notin et al., 2022a.


<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th rowspan="2">Type</th>
      <th># Params</th>
      <th colspan="3">ρ(by mutation depth)↑</th>
      <th colspan="3">ρ(by MSA depth)↑</th>
      <th colspan="4">ρ(by taxon)↑</th>
    </tr>
    <tr>
      <th>(million)</th>
      <th>Single</th>
      <th>Double</th>
      <th>All</th>
      <th>Low</th>
      <th>Medium</th>
      <th>High</th>
      <th>Prokaryote</th>
      <th>Human</th>
      <th>Eukaryote</th>
      <th>Virus</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="13">Few-shot methods</td>
    </tr>
    <tr>
      <td>SiteIndep</td>
      <td>Single</td>
      <td>-</td>
      <td>0.378</td>
      <td>0.322</td>
      <td>0.378</td>
      <td>0.431</td>
      <td>0.375</td>
      <td>0.342</td>
      <td>0.343</td>
      <td>0.375</td>
      <td>0.401</td>
      <td>0.406</td>
    </tr>
    <tr>
      <td>EVmutation</td>
      <td>Single</td>
      <td>-</td>
      <td>0.423</td>
      <td>0.401</td>
      <td>0.423</td>
      <td>0.406</td>
      <td>0.403</td>
      <td>0.484</td>
      <td>0.499</td>
      <td>0.396</td>
      <td>0.429</td>
      <td>0.381</td>
    </tr>
    <tr>
      <td>Wavenet</td>
      <td>Single</td>
      <td>-</td>
      <td>0.399</td>
      <td>0.344</td>
      <td>0.400</td>
      <td>0.286</td>
      <td>0.404</td>
      <td>0.489</td>
      <td>0.492</td>
      <td>0.373</td>
      <td>0.442</td>
      <td>0.321</td>
    </tr>
    <tr>
      <td>GEMME</td>
      <td>Single</td>
      <td>-</td>
      <td>0.460</td>
      <td>0.397</td>
      <td>0.463</td>
      <td>0.444</td>
      <td>0.446</td>
      <td>0.520</td>
      <td>0.505</td>
      <td>0.436</td>
      <td>0.479</td>
      <td>0.451</td>
    </tr>
    <tr>
      <td rowspan="2">DeepSequence</td>
      <td>Single</td>
      <td>-</td>
      <td>0.411</td>
      <td>0.358</td>
      <td>0.416</td>
      <td>0.386</td>
      <td>0.391</td>
      <td>0.505</td>
      <td>0.497</td>
      <td>0.396</td>
      <td>0.461</td>
      <td>0.332</td>
    </tr>
    <tr>
      <td>Ensemble</td>
      <td>-</td>
      <td>0.433</td>
      <td>0.394</td>
      <td>0.435</td>
      <td>0.386</td>
      <td>0.411</td>
      <td>0.534</td>
      <td>0.522</td>
      <td>0.405</td>
      <td>0.480</td>
      <td>0.361</td>
    </tr>
    <tr>
      <td rowspan="2">EVE</td>
      <td>Single</td>
      <td>-</td>
      <td>0.451</td>
      <td>0.406</td>
      <td>0.452</td>
      <td>0.417</td>
      <td>0.434</td>
      <td>0.525</td>
      <td>0.518</td>
      <td>0.411</td>
      <td>0.469</td>
      <td>0.436</td>
    </tr>
    <tr>
      <td>Ensemble</td>
      <td>-</td>
      <td>0.459</td>
      <td>0.409</td>
      <td>0.459</td>
      <td>0.424</td>
      <td>0.441</td>
      <td>0.532</td>
      <td>0.526</td>
      <td>0.419</td>
      <td>0.481</td>
      <td>0.437</td>
    </tr>
    <tr>
      <td rowspan="2">MSA-Transfomer</td>
      <td>Single</td>
      <td>100</td>
      <td>0.405</td>
      <td>0.358</td>
      <td>0.426</td>
      <td>0.372</td>
      <td>0.415</td>
      <td>0.500</td>
      <td>0.506</td>
      <td>0.387</td>
      <td>0.468</td>
      <td>0.379</td>
    </tr>
    <tr>
      <td>Ensemble</td>
      <td>500</td>
      <td>0.440</td>
      <td>0.374</td>
      <td>0.440</td>
      <td>0.387</td>
      <td>0.428</td>
      <td>0.513</td>
      <td>0.517</td>
      <td>0.398</td>
      <td>0.467</td>
      <td>0.406</td>
    </tr>
    <tr>
      <td>Tranception-R</td>
      <td>Single</td>
      <td>700</td>
      <td>0.450</td>
      <td>0.427</td>
      <td>0.453</td>
      <td>0.442</td>
      <td>0.438</td>
      <td>0.500</td>
      <td>0.495</td>
      <td>0.424</td>
      <td>0.485</td>
      <td>0.434</td>
    </tr>
    <tr>
      <td>TranceptEVE</td>
      <td>Single</td>
      <td>700</td>
      <td>0.481</td>
      <td>0.445</td>
      <td>0.481</td>
      <td>0.454</td>
      <td>0.465</td>
      <td>0.542</td>
      <td>0.539</td>
      <td>0.447</td>
      <td>0.498</td>
      <td>0.461</td>
    </tr>
    <tr>
      <td colspan="13">Zero-shot methods</td>
    </tr>
    <tr>
      <td>RITA</td>
      <td>Ensemble</td>
      <td>2,210</td>
      <td>0.393</td>
      <td>0.236</td>
      <td>0.399</td>
      <td>0.350</td>
      <td>0.414</td>
      <td>0.407</td>
      <td>0.391</td>
      <td>0.391</td>
      <td>0.405</td>
      <td>0.417</td>
    </tr>
    <tr>
      <td>ESM-1v</td>
      <td>Ensemble</td>
      <td>3,250</td>
      <td>0.416</td>
      <td>0.309</td>
      <td>0.417</td>
      <td>0.390</td>
      <td>0.378</td>
      <td>0.536</td>
      <td>0.521</td>
      <td>0.439</td>
      <td>0.423</td>
      <td>0.268</td>
    </tr>
    <tr>
      <td>ProGen2</td>
      <td>Ensemble</td>
      <td>10,779</td>
      <td>0.421</td>
      <td>0.312</td>
      <td>0.423</td>
      <td>0.384</td>
      <td>0.421</td>
      <td>0.467</td>
      <td>0.497</td>
      <td>0.412</td>
      <td>0.459</td>
      <td>0.373</td>
    </tr>
    <tr>
      <td>ProtTrans</td>
      <td>Ensemble</td>
      <td>6,840</td>
      <td>0.417</td>
      <td>0.360</td>
      <td>0.413</td>
      <td>0.372</td>
      <td>0.395</td>
      <td>0.492</td>
      <td>0.498</td>
      <td>0.419</td>
      <td>0.400</td>
      <td>0.322</td>
    </tr>
    <tr>
      <td>ESM2</td>
      <td>Ensemble</td>
      <td>18,843</td>
      <td>0.415</td>
      <td>0.316</td>
      <td>0.413</td>
      <td>0.391</td>
      <td>0.381</td>
      <td>0.509</td>
      <td>0.508</td>
      <td>0.456</td>
      <td>0.461</td>
      <td>0.213</td>
    </tr>
    <tr>
      <td>SaProt</td>
      <td>Ensemble</td>
      <td>1,285</td>
      <td>0.447</td>
      <td>0.368</td>
      <td>0.450</td>
      <td>0.456</td>
      <td>0.410</td>
      <td>0.544</td>
      <td>0.534</td>
      <td>0.464</td>
      <td>0.460</td>
      <td>0.334</td>
    </tr>
    <tr>
      <td>ProtSSN</td>
      <td>Ensemble</td>
      <td>1,476</td>
      <td>0.433</td>
      <td>0.381</td>
      <td>0.433</td>
      <td>0.406</td>
      <td>0.402</td>
      <td>0.532</td>
      <td>0.530</td>
      <td>0.436</td>
      <td>0.491</td>
      <td>0.290</td>
    </tr>
  </tbody>
</table>

_The top three are highlighted by first, second, and third._

ProtSSN demonstrates superior performance among non-MSA zero-shot methods in predicting both single-site and multi-site mutants, underscoring its pivotal role in guiding protein engineering toward deep mutation. Furthermore, ProtSSN outperforms MSA-based methods across taxa, except for viruses, where precise identification of conserved sites is crucial for positive mutations, especially in spike proteins (Katoh and Standley, 2021; Mercurio et al., 2021). In essence, ProtSSN provides an efficient and effective solution for variant effects prediction when compared to both non-MSA and MSA-based methods. Note that although MSA-based methods generally consume fewer trainable parameters than non-MSA methods, they incur significantly higher costs in terms of search time and memory usage. Moreover, the inference performance of MSA-based methods relies heavily on the quality of the input MSA, where the additionally involved variance makes impacts the stability of the model performance.

## Discussion

The development of modern computational methodologies for protein engineering is a crucial facet of in silico protein design. Effectively assessing the fitness of protein mutants not only supports cost-efficient experimental validations but also guides the modification of proteins toward enhanced or novel functions. Traditionally, computational methods rely on analyzing small sets of labeled data for specific protein assays, such as FLIP (Dallago et al., 2021), PEER (Xu et al., 2022), and PETA (Tan et al., 2024b). More recent work has also focused on examining the relationship between models and supervised fitness prediction (Li et al., 2024). However, obtaining experimental data is often infeasible in real-world scenarios, particularly for positive mutants, due to the cost and complexity of protein engineering. This limitation renders supervised learning methods impractical for many applications. As a result, it is crucial to develop solutions that can efficiently suggest site mutations for wet experiments, even when starting from scratch without prior knowledge. Recent deep learning solutions employ a common strategy that involves establishing a hidden protein representation and masking potential mutation sites to recommend plausible AAs. Previous research has primarily focused on extracting protein representations from either their sequential or structural modalities, with many treating the prediction of mutational effects merely as a secondary task following inverse folding or de novo protein design. These approaches often overlook the importance of comprehensive investigation on both global and local perspectives of AA interaction that are critical for featuring protein functions. Furthermore, these methods hardly tailored model designs for suggesting mutations, despite the significance of this type of task. In this work, we introduce ProtSSN, a denoising framework that effectively cascades protein sequence and structure embedding for predicting mutational effects. Both the protein language model and equivariant graph neural network are employed to encode the global interaction of AAs with geometry-aware local enhancements.

On the other hand, existing benchmarks for evaluating computational solutions mostly focus on assessing model generalization on large-scale datasets (e.g., over 2 million mutants in ProteinGym v1). However, such high-throughput datasets often lack accurate experimental measurements (Frazer et al., 2021), leading to significant noise in the labels. Furthermore, the larger data volumes typically do not include environmental labels for mutants (e.g., temperature, pH), despite the critical importance of these conditions for biologists. In response, we propose DTm and DDG. These low-throughput datasets, which we have collected, emphasize the consistency of experimental conditions and data accuracy. They are traceable and serve as valuable complements to ProteinGym, providing a more detailed and reliable evaluation of computational models. We have extensively validated the efficacy of ProtSSN across various protein function assays and taxa, including two thermostability datasets prepared by ourselves. Our approach consistently demonstrates substantial promise for protein engineering applications, such as facilitating the design of mutation sequences with enhanced interaction and enzymatic activity (Table 4).

**Table 4.**
 Average Spearman’s $ρ$ correlation of variant effect prediction on DTm and DDG for zero-shot methods with model ensemble.The values within () indicate the standard deviation of bootstrapping.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th># Params (million)</th>
      <th>DTm</th>
      <th>DDG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RITA</td>
      <td>2210</td>
      <td>0,195(0.045)</td>
      <td>0.255(0.061)</td>
    </tr>
    <tr>
      <td>ESM-1v</td>
      <td>3250</td>
      <td>0.300(0.036)</td>
      <td>0.310(0.054)</td>
    </tr>
    <tr>
      <td>Tranception</td>
      <td>1085</td>
      <td>0.202(0.039)</td>
      <td>0.277(0.062)</td>
    </tr>
    <tr>
      <td>ProGen2</td>
      <td>10,779</td>
      <td>0.293(0.042)</td>
      <td>0.282(0.063)</td>
    </tr>
    <tr>
      <td>ProtTrans</td>
      <td>6840</td>
      <td>0.323(0.039)</td>
      <td>0.389(0.059)</td>
    </tr>
    <tr>
      <td>ESM2</td>
      <td>18,843</td>
      <td>0.346(0.035)</td>
      <td>0.383(0.55)</td>
    </tr>
    <tr>
      <td>SaProt</td>
      <td>1285</td>
      <td>0.392(0.040)</td>
      <td>0.415(0.061)</td>
    </tr>
    <tr>
      <td>ProtSSN</td>
      <td>1476</td>
      <td>0.425(0.033)</td>
      <td>0.440(0.057)</td>
    </tr>
  </tbody>
</table>

## Materials and methods

This section starts by introducing the three mutational scanning benchmark datasets used in this study, including an open benchmark dataset ProteinGym v1 and two new datasets on protein thermostability, that is, DTm and DDG. We establish the proposed ProtSSN for protein sequences and structures encoding in the section ‘Proposed method’. The overall pipeline of model training and inference is presented in the section ‘Model pipeline’. The experimental setup for model evaluation is provided in the section ‘Experimantal protocol’.

### Dataset

To evaluate model performance in predicting mutation effects, we compare ProtSSN with SOTA baselines on ProteinGym v1, the largest open benchmark for DMS assays. We also introduce two novel benchmarks, DTm and DDG, for assessing protein thermostability under consistent control environments. Details of the new datasets are provided in Table 5. Considering the significant influence of experimental conditions on protein temperature, we explicitly note the pH environment in each assay. Refer to the following paragraphs for more details.

**Table 5.**
 Statistical summary of DTm and DDG.


<table>
  <thead>
    <tr>
      <th rowspan="2">pH range</th>
      <th colspan="3">DTm</th>
      <th colspan="3">DDG</th>
    </tr>
    <tr>
      <th># Assays</th>
      <th>Avg. # mut</th>
      <th>Avg. AA</th>
      <th># Assays</th>
      <th>Avg. # mut</th>
      <th>Avg.AA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Acid (pH &lt; 7)</td>
      <td>29</td>
      <td>29.1</td>
      <td>272.8</td>
      <td>21</td>
      <td>22.6</td>
      <td>125.3</td>
    </tr>
    <tr>
      <td>Neutral (pH = 7)</td>
      <td>14</td>
      <td>37.4</td>
      <td>221.2</td>
      <td>10</td>
      <td>23.1</td>
      <td>78.3</td>
    </tr>
    <tr>
      <td>Alkaline (pH &gt; 7)</td>
      <td>23</td>
      <td>50.1</td>
      <td>233.3</td>
      <td>5</td>
      <td>24.6</td>
      <td>101.4</td>
    </tr>
    <tr>
      <td>Sum</td>
      <td>66</td>
      <td>38.2</td>
      <td>221.2</td>
      <td>36</td>
      <td>23.0</td>
      <td>108.8</td>
    </tr>
  </tbody>
</table>

### ProteinGym

The assessment of ProtSSN for deep mutation effects prediction is conducted on ProteinGym v1 (Notin et al., 2023). It is the most extensive protein substitution benchmark comprising 217 assays and more than 2.5M mutants. These DMS assays cover a broad spectrum of functional properties (e.g., ligand binding, aggregation, viral replication, and drug resistance) and span various protein families (e.g., kinases, ion channel proteins, transcription factors, and tumor suppressors) across different taxa (e.g., humans, other eukaryotes, prokaryotes, and viruses) (Table 6).

**Table 6.**
 Details of zero-shot baseline models.


<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th colspan="2">Type</th>
      <th rowspan="2">Description</th>
      <th rowspan="2">Source code</th>
    </tr>
    <tr>
      <th>Seq</th>
      <th>Struct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RITA (Hesslow et al., 2022)</td>
      <td>✓</td>
      <td></td>
      <td>A generative protein language model with billion-level parameters</td>
      <td>https://github.com/lightonai/RITA (Hesslow and Poli, 2023)</td>
    </tr>
    <tr>
      <td>ProGen2 (Nijkamp et al., 2023)</td>
      <td>✓</td>
      <td></td>
      <td>A generative protein language model with billion-level parameters</td>
      <td>https://github.com/salesforce/progen (Nijkamp, 2022)</td>
    </tr>
    <tr>
      <td>ProtTrans (Elnaggar et al., 2021)</td>
      <td>✓</td>
      <td></td>
      <td>Transformer-based models trained on large protein sequence corpus</td>
      <td>https://github.com/agemagician/ProtTrans (Elnaggar and Heinzinger, 2025)</td>
    </tr>
    <tr>
      <td>Tranception (Notin et al., 2022a)</td>
      <td>✓</td>
      <td></td>
      <td>An autoregressive model for variant effect prediction with retrieve machine</td>
      <td>https://github.com/OATML-Markslab/Tranception (Notin, 2023)</td>
    </tr>
    <tr>
      <td>CARP (Yang et al., 2024)</td>
      <td>✓</td>
      <td></td>
      <td>Pretrained CNN protein sequence masked language models of various sizes</td>
      <td>https://github.com/microsoft/protein-sequence-models (microsoft, 2024)</td>
    </tr>
    <tr>
      <td>ESM-1b (Rives et al., 2021)</td>
      <td>✓</td>
      <td></td>
      <td rowspan="3">A masked language model-based pre-train method with various pre-trainingdataset and positional embedding strategies</td>
      <td rowspan="4">https://github.com/facebookresearch/esm (facebookresearch, 2023)</td>
    </tr>
    <tr>
      <td>ESM-1v (Meier et al., 2021)</td>
      <td>✓</td>
      <td></td>
    </tr>
    <tr>
      <td>ESM2 (Lin et al., 2023)</td>
      <td>✓</td>
      <td></td>
    </tr>
    <tr>
      <td>ESM-if1 (Hsu et al., 2022)</td>
      <td></td>
      <td>✓</td>
      <td>An inverse folding method with mask language modeling and geometricvector perception (Jing et al., 2020)</td>
    </tr>
    <tr>
      <td>MIF-ST (Yang et al., 2023)</td>
      <td>✓</td>
      <td>✓</td>
      <td>Pretrained masked inverse folding models with sequence pretraining transfer</td>
      <td>https://github.com/microsoft/protein-sequence-models</td>
    </tr>
    <tr>
      <td>SaProt (Su et al., 2023)</td>
      <td>✓</td>
      <td>✓</td>
      <td>Structure-aware vocabulary for protein language modeling with FoldSeek</td>
      <td>https://github.com/westlake-repl/SaProt (Su and fajieyuan, 2025)</td>
    </tr>
  </tbody>
</table>

### DTm

The assays in the first novel thermostability benchmark are sourced from single-site mutations in ProThermDB (Nikam et al., 2021). Each assay is named in the format ‘UniProt_ID-pH’. For instance, ‘O00095-8.0’ signifies mutations conducted and evaluated under pH 8.0 for protein O00095. The attributes include ‘mutant’, ‘score’, and ‘UniProt_ID’, with at least 10 mutants to ensure a meaningful evaluation. To concentrate on single-site mutations compared to wild-type proteins, we exclude records with continuous mutations. To avoid dealing with partial or misaligned protein structures resulting from incomplete wet experimental procedures, we employ UniProt ID to pair protein sequences with folded structures predicted by AlphaFold2 (Jumper et al., 2021) from https://alphafold.ebi.ac.uk. In total, DTm consists of 66 such protein–environment pairs and 2520 mutations.

### DDG

The second novel thermostability benchmark is sourced from DDMut (Zhou et al., 2023), where mutants are paired with their PDB documents. We thus employ crystal structures for proteins in DDG and conduct additional preprocessing steps for environmental consistency. In particular, we group mutants of the same protein under identical experimental conditions and examine the alignment between mutation sites and sequences extracted from crystal structures. We discard mutant records that cannot be aligned with the sequence loaded from the associated PDB document. After removing data points with fewer than 10 mutations, DDG comprises 36 data points and 829 mutations. As before, assays are named in the format ‘PDB_ID-pH-temperature’ to indicate the chemical condition (pH) and temperature (in Celsius) of the experiment on the protein. An example assay content is provided in Figure 4.

![Figure 4.](https://cdn.elifesciences.org/articles/98033/elife-98033-fig4-v1.jpg)

**Figure 4.:** The record is derived from DDG for the A chain of protein 1A7V, experimented at pH = 6.5 and degree at 25°C.

### Proposed method

Labeled data are usually scarce in biomolecule research, which demands designing a general self-supervised model for predicting variant effects on unknown proteins and protein functions. We propose ProtSSN with a pre-training scheme that recovers residues from a given protein backbone structure with noisy local environment observations.

### Multilevel protein representation

#### Protein primary structure (Noisy)

Denote a given observation with residue $𝒗~$. We assume this arbitrary observation is undergoing random mutation toward a stable state. The training objective is to learn a revised state $𝒗$ that is less likely to be eliminated by natural selection due to unfavorable properties such as instability or inability to fold. The perturbed observation is defined by a multinomial distribution.

$$
\pi(v~∣v)=pΘ(\pi_{1},\pi_{2},,\pi_{20})+(1−p)\delta(v~−v),
$$

where an AA in a protein chain has a chance of $p$ to mutate to one of 20 AAs (including itself) following a replacement distribution $𝚯⁢(⋅)$ and $(1−p)$ of remaining unchanged. We consider $p$ as a tunable parameter and define $𝚯⁢(⋅)$ by the frequency of residues observed in wild-type proteins.

#### Protein tertiary structure

The geometry of a protein is described by $𝒢=(𝒱,ℰ,𝑾_{V},𝑾_{E},𝑿_{V})$, which is a residue graph based on the k-nearest neighbor algorithm (kNN). Each node $v_{i}\inV$ represents an AA in the protein connected to up to k closest nodes within 30 Å. Node attributes $𝑾_{V}$ are hidden semantic embeddings of residues extracted by the semantic encoder (see the section ‘Semantic encoding of global AA contacts), and edge attributes $𝑾_{E}\inℝ^{93}$ feature relationships of connected nodes based on inter-atomic distances, local N-C positions, and sequential position encoding (Zhou et al., 2024b). Additionally, $𝑿_{V}$ records 3D coordinates of AAs in the Euclidean space, which plays a crucial role in the subsequent geometric embedding stage to preserve roto-translation equivariance.

### Semantic encoding of global AA contacts

Although it is generally believed by the community that a protein’s sequence determines its biological function via the folded structure, following strictly to this singular pathway risks overlooking other unobserved yet potentially influential inter-atomic communications impacting protein fitness. Our proposed ProtSSN thus includes pairwise relationships for residues through an analysis of proteins’ primary structure from $𝑽~$ and embeds them into hidden representations $𝑾_{V}$ for residues. At each iteration, the input sequences are modified randomly by Equation 3 and then embedded via an Evolutionary Scale Modeling method, ESM2 (Lin et al., 2023), which employs a BERT-style masked language modeling objective. This objective predicts the identity of randomly selected AAs in a protein sequence by observing their context within the remainder of the sequence. Alternative semantic encoding strategies are discussed in the section ‘AA perturbation strategies’.

### Geometrical encoding of local AA contacts

Proteins are structured in 3D space, which requires the geometric encoder to possess roto-translation equivariance to node positions as well as permutation invariant to node attributes. This design is vital to avoid the implementation of costly data augmentation strategies. We practice EGNN (Satorras et al., 2021) to acquire the hidden node representation $𝑾_{V}^{l+1}={𝒘_{v_{1}}^{l+1},,𝒘_{v_{n}}^{l+1}}$ and node coordinates $𝑿_{pos}^{l+1}={𝒙_{v_{1}}^{l+1},,𝒙_{v_{n}}^{l+1}}$ at the l+1th layer

$$
m_{ij}=ϕ_{e}(w_{v_{i}}^{l},w_{v_{j}}^{l},‖x_{v_{i}}^{l}−x_{v_{j}}^{l}‖^{2},w_{e_{ij}}),x_{v_{i}}^{l+1}=x_{v_{i}}^{l}+\frac{1}{n}\sumj\neqi(x_{v_{i}}^{l}−x_{v_{j}}^{l})ϕ_{x}(m_{ij}),w_{v_{i}}^{l+1}=ϕ_{v}(w_{i}^{l},\sumj\neqim_{ij}).
$$

In these equations, $𝒘_{e_{i⁢j}}$ represents the input edge attribute on $V_{ij}$, which is not updated by the network. The propagation rules $ϕ_{e},ϕ_{x}$, and $ϕ_{v}$ are defined by differentiable functions, for example, .multilayer perceptrons (MLPs). The final hidden representation on nodes $𝑾_{V}^{L}$ embeds the microenvironment and local topology of AAs, and it will be carried on by readout layers for label predictions.

### Model pipeline

ProtSSN is designed for protein engineering with a self-supervised learning scheme. The model is capable of conducting zero-shot variant effect prediction on an unknown protein, and it can generate the joint distribution for the residue of all AAs along the protein sequence of interest. This process accounts for the epistatic effect and concurrently returns all AA sites in a sequence. Below, we detail the workflow for training the zero-shot model and scoring the effect of a specific mutant.

#### Training

The fundamental model architecture cascades a frozen sequence encoding module and a trainable tertiary structure encoder. The protein is represented by its sequence and structure characteristics, where the former is treated as plain text and the latter is formalized as a kNN graph with model-encoded node attributes, handcrafted edge attributes, and 3D positions of the corresponding AAs. Each input sequence $𝑽$ are first one-hot encoded by 33 tokens, comprising both AA residues and special tokens (Lin et al., 2023). The ground truth sequences, during training, will be permuted into

$$
V~=Permute(V).
$$

Here, $𝑽~$ is the perturbed AA to be encoded by a protein language model, which analyses pairwise hidden relationships among AAs from the input protein sequence and produces a vector representation $𝒘_{v_{i}}\in𝑾_{V}$ for each AA, that is,

$$
𝑾_{V}=LM_{frozen}⁢(𝑽~)
$$

The language model $LM_{frozen}(⋅)$, ESM2 (Lin et al., 2023) for instance, has been pre-trained on a massive protein sequence database (e.g., UniRef50 [Suzek et al., 2015]) to understand the semantic and grammatical rules of wild-type proteins with high-dimensional AA-level long-short-range interactions. The independent perturbation on AA residues follows (Equation 1) operates in every epoch, which requires constant updates on the sequence embedding. To further enhance the interaction of locally connected AAs in the node representation, a stack of LEGNN layers is implemented on the input graph $G$ to yield

$$
𝑾_{V}^{L}=EGNN⁢(𝒢).
$$

During the pre-training phase for protein sequence recovery, the output layer $ϕ(⋅)$ provides the probability of tokens in one of 33 types, that is,

$$
𝒀=ϕ⁢(𝑾_{V}^{L})\inℝ^{n33}
$$

for a protein of $n$ AAs. The model’s learnable parameters are refined by minimizing the cross-entropy of the recovered AAs with respect to the ground-truth AAs in wild-type proteins:

$$
loss=−\sumn=1L\sumc=133V_{n,c}log⁡(softmax(Y_{n,c})),
$$

where $L$ is the length of the sequence, $n$ represents the position index within the sequence, and each $c$ corresponds to a potential type of token.

#### Inferencing

For a given wild-type protein and a set of mutants, the fitness scores of the mutants are derived from the joint distribution of the altered residues relative to the wild-type template. First, the wild-type protein sequence and structure are encoded into hidden representations following (Equations 4 and 5). Unlike the pre-training process, here the residue in the wild-type protein is considered as a reference state and is compared with the predicted probability of AAs at the mutated site. Next, for a mutant with mutated sites $T$ ($|T|\geq1$), we define its fitness score $F_{x}$ using the corresponding log-odds ratio, that is,

$$
F_{x}=\sumt\in𝒯log⁡p⁢(𝒚_{t})-log⁡p⁢(𝒗_{t}),
$$

where $𝒚_{t}$ and $𝒗_{t}$ denote the mutated and wild-type residue of the tth AA.

### Experimental protocol

We validate the efficacy of ProtSSN on zero-shot mutation effect prediction tasks. The performance is compared with other SOTA models of varying numbers of trainable parameters. The implementations are programmed with PyTorch-Geometric (ver 2.2.0) and PyTorch (ver 1.12.1) and executed on an NVIDIA Tesla A100 GPU with 6912 CUDA cores and 80GB HBM2 installed on an HPC cluster.

### Training setup

ProtSSN is pre-trained on a non-redundant subset of CATH v4.3.0 (Orengo et al., 1997) domains, which contains 30,948 experimental protein structures with less than 40% sequence identity. We remove proteins that exceed 2000 AAs in length for efficiency. For each kNN protein graph, node features are extracted and updated by a frozen ESM2-t33 prefix model (Lin et al., 2023). Protein topology is inferred by a six-layer EGNN (Satorras et al., 2021) with the hidden dimension tuned from ${512,768,1280}$. Adam (Kingma and Ba, 2015) is used for backpropagation with the learning rate set to 0.0001. To avoid training instability or CUDA out-of-memory, we limit the maximum input to 8192 AA tokens per batch, constituting approximately 32 graphs.

### Baseline methods

We undertake an extensive comparison with baseline methods of self-supervised sequence or structure-based models on the fitness of mutation effects prediction (Table 5). Sequence models employ position embedding strategies such as autoregression (RITA [Hesslow et al., 2022], Tranception [Notin et al., 2022a], TraceptEVE [Notin et al., 2022b], and ProGen2 [Nijkamp et al., 2023]), masked language modeling (ESM-1b [Rives et al., 2021], ESM-1v [Meier et al., 2021], and ESM2 [Lin et al., 2023]), a combination of both (ProtTrans [Elnaggar et al., 2021]), and convolutional modeling (CARP [Yang et al., 2024]). Additionally, we also compare with ESM-if1 (Hsu et al., 2022) which incorporates masked language modeling objectives with GVP (Jing et al., 2020), as well as MIF-ST (Yang et al., 2023) and SaProt (Su et al., 2023) with both sequence and structure encoding.

The majority of the performance comparison was conducted on zero-shot deep learning methods. However, for completeness, we also report a comparison with popular MSA-based methods, such as GEMME (Laine et al., 2019), Site-Independent (Hopf et al., 2017), EVmutation (Hopf et al., 2017), Wavenet (Shin et al., 2021), DeepSequence (Riesselman et al., 2018), and EVE (Frazer et al., 2021). Other deep learning methods use MSA for training or retrieval, including MSA-Transformer (Rao et al., 2021b), Tranception (Notin et al., 2022a), and TranceptEVE (Notin et al., 2022b).

### Scoring function

Following the convention, the fitness scores of the zero-shot models are calculated by the log-odds ratio in Equation 8 for encoder methods, such as the proposed ProtSSN and the ProtTrans series models. For autoregressive and inverse folding models (e.g., Tranception and ProGen2) that predict the next token $x_{i}$ based on the context of previous $x_{1:i−1}$ tokens, the fitness score $F_{x}$ of a mutated sequence $𝒚$ is computed via the log-likelihood ratio with the wild-type sequence $𝒗$, that is,

$$
F_{x}=log⁡\frac{P(y)}{P(v)}.
$$

### Benchmark datasets

We conduct a comprehensive comparison of deep learning predictions on hundreds of DMS assays concerning different protein types and biochemical assays. We prioritize experimentally measured properties that possess a monotonic relationship with protein fitness, such as catalytic activity, binding affinity, expression, and thermostability. In particular, ProteinGym v1 (Notin et al., 2023) groups five sets of protein properties from 217 assays. Two new datasets named DTm and DDG examine 102 environment-specific assays with thermostability scores. In total, 319 assays with around 2.5 million mutants are scored. To better understand the novelty of the proposed ProtSSN, we designed additional investigations on ProteinGym v0 (Notin et al., 2022a), an early-release version of ProteinGym with 1.5M missense variants across 86 assays (excluding one assay that failed to be folded by both AlphaFold2 and ESMFold, that is, A0A140D2T1_ZIKV_Sourisseau_growth_2019).

### Evaluation metric

We evaluate the performance of pre-trained models on a diverse set of proteins and protein functions using Spearman’s $ρ$ correlation that measures the strength and direction of the monotonic relationship between two ranked sequences, that is, experimentally evaluated mutants and model-inferred mutants (Meier et al., 2021; Notin et al., 2022a; Frazer et al., 2021; Zhou et al., 2024b). This non-parametric rank measure is robust to outliers and asymmetry in mutation scores, and it does not assume any specific distribution of mutation fitness scores. The scale of $ρ$ ranges from -1 to 1, indicating the negative or positive correlation of the predicted sequence to the ground truth. The prediction is preferred if its $ρ$ to the experimentally examined ground truth is close to 1.

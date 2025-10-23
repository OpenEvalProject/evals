# Peer review - Round 1

Editors:
- Shozeb Haider, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90061.3.sa0](https://doi.org/10.7554/eLife.90061.3.sa0)

The study presents a valuable tool for searching molecular dynamics simulation data, making such datasets accessible for open science. The authors provide convincing evidence that it is possible to identify noteworthy molecular dynamics simulation datasets and that their analysis can produce information of value to the community.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90061.3.sa1](https://doi.org/10.7554/eLife.90061.3.sa1)

Summary:

Tiemann et al. have undertaken an original study on the availability of molecular dynamics (MD) simulation datasets across the Internet. There is a widespread belief that extensive, well-curated MD datasets would enable the development of novel classes of AI models for structural biology. However, currently, there is no standard for sharing MD datasets. As generating MD datasets is energy-intensive, it is also important to facilitate the reuse of MD datasets to minimize energy consumption. Developing a universally accepted standard for depositing and curating MD datasets is a huge undertaking. The study by Tiemann et al. will be very valuable in informing policy developments toward this goal.

Strengths:

The study presents an original approach to addressing a growing concern in the field. It is clear that adopting a more collaborative approach could significantly enhance the impact of MD simulations in modern molecular sciences.

The timing of the work is appropriate, given the current interest in developing AI models for describing biomolecular dynamics.

Weaknesses:

The study primarily focuses on one major MD engine (GROMACS), although this limitation is not significant considering the proof-of-concept nature of the study.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90061.3.sa2](https://doi.org/10.7554/eLife.90061.3.sa2)

Summary:

Molecular dynamics (MD) data is deposited in public, non-specialist repositories. This work starts from the premise that these data are a valuable resource as they could be used by other researchers to extract additional insights from these simulations; it could also potentially be used as training data for ML/AI approaches. The problem is that mining these data is difficult because they are not easy to find and work with. The primary goal of the authors was to discover and index these difficult-to-find MD datasets, which they call the "dark matter of the MD universe" (in contrast to data sets held in specialist databases).

The authors developed a search strategy that avoided the use of ill-defined metadata but instead relied on the knowledge of the restricted set of file formats used in MD simulations as a true marker for the data they were looking for. Detection of MD data marked a data set as relevant with a follow-up indexing strategy of all associated content. This "explore-and-expand" strategy allowed the authors for the first time to provide a realistic census of the MD data in non-specialist repositories.

As a proof of principle, they analyzed a subset of the data (primarily related to simulations with the popular Gromacs MD package) to summarize the types of simulated systems (primarily biomolecular systems) and commonly used simulation settings.

Based on their experience they propose best practices for metadata provision to make MD data FAIR (findable, accessible, interoperable, reusable).

A prototype search engine that works on the indexed datasets is made publicly available. All data and code are made freely available as open source/open data.

Strengths:

- The novel search strategy is based on relevant data to identify full datasets instead of relying on metadata and thus is likely to have many true positives and few false positives.

- The paper provides a first glimpse at the potential hidden treasures of MD simulations and force field parametrizations of molecules.

- Analysis of parameter settings of MD simulations from how researchers *actually* run simulations can provide valuable feedback to MD code developers for how to document/educate users. This approach is much better than analyzing what authors write in the Methods sections.

- The authors make a prototype search engine available.

- The guidelines for FAIR MD data are based on experience gained from trying to make sense of the data.

Weaknesses:

- So far the work is a proof-of-concept that focuses on MD data produced by Gromacs (which was prevalent under all indexed and identified packages).

As discussed in the manuscript, some types of biomolecules are likely underrepresented because different communities have different preferences for force fields/MD codes (for example: carbohydrates with AMBER/GLYCAM using AMBER MD instead of Gromacs).

- Materials sciences seem to be severely under-represented - commonly used codes in this area such as LAMMPS are not even detected, and only very few examples could be identified. As it is, the paper primarily provides an insight into the *biomolecular* MD simulation world.

The authors succeed in providing a first realistic view on what MD data is available in public repositories. In particular, their explore-expand approach has the potential to be customized for all kinds of specialist simulation data, whereby specific artifacts are

used as fiducial markers instead of metadata. The more detailed analysis is limited to Gromacs simulations and primarily biomolecular simulations (even though MD is also widely used in other fields such as the materials sciences). This restricted view may simply be correlated with the user community of Gromacs and hopefully, follow-up studies from this work will shed more light on this shortcoming.

The study quantified the number of trajectories currently held in structured databases as ~10k vs ~30k in generalist repositories. To go beyond the proof-of-principle analysis it would be interesting to analyze the data in specialist repositories in the same way as the one in the generalist ones, especially as there are now efforts underway to create a database for MD simulations (Grant 'Molecular dynamics simulation for biology and chemistry research' to establish MDDB' DOI 10.3030/101094651). One should note that structured databases do not invalidate the approach pioneered in this work; if anything they are orthogonal to each other and both will likely play an important role in growing the usefulness of MD simulations in the future.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90061.3.sa3](https://doi.org/10.7554/eLife.90061.3.sa3)

Molecular dynamics (MD) simulations nowadays are an essential element of structural biology investigations, complementing experiments and aiding their interpretation by revealing transient processes or details (such as the effects of glycosylation on the SARS-CoV-2 spike protein, for example Casalino et al. ACS Cent. Sci. 2020; 6, 10, 1722-1734 https://doi.org/10.1021/acscentsci.0c01056) that cannot be observed directly. MD simulations can allow for the calculation of thermodynamic, kinetic, and other properties and the prediction of biological or chemical activity. MD simulations can now serve as "computational assays" (Huggins et al. WIREs Comput Mol Sci. 2019; 9:e1393. https://doi.org/10.1002/wcms.1393). Conceptually, MD simulations have played a crucial role in developing the understanding that the dynamics and conformational behaviour of biological macromolecules are essential to their function, and are shaped by evolution. Atomistic simulations range up to the billion atom scale with exascale resources (e.g. simulations of SARS-CoV-2 in a respiratory aerosol. Dommer et al. The International Journal of High Performance Computing Applications. 2023; 37:28-44. doi:10.1177/10943420221128233), while coarse-grained models allow simulations on even larger length- and timescales. Simulations with combined quantum mechanics/molecular mechanics (QM/MM) methods can investigate biochemical reactivity, and overcome limitations of empirical forcefields (Cui et al. J. Phys. Chem. B 2021; 125, 689 https://doi.org/10.1021/acs.jpcb.0c09898).

MD simulations generate large amounts of data (e.g. structures along the MD trajectory) and increasingly, e.g. because of funder mandates for open science, these data are deposited in publicly accessible repositories. There is real potential to learn from these data en masse, not only to understand biomolecular dynamics but also to explore methodological issues. Deposition of data is haphazard and lags far behind experimental structural biology, however, and it is also hard to answer the apparently simple question of "what is out there?". This is the question that Tiemann et al explore in this nice and important work, focusing on simulations run with the widely used GROMACS package. They develop a search strategy and identify almost 2,000 datasets from Zenodo, Figshare and Open Science Framework. This provides a very useful resource. For these datasets, they analyse features of the simulations (e.g. atomistic or coarse-grained), which provides a useful snapshot of current simulation approaches. The analysis is presented clearly and discussed insightfully. They also present a search engine to explore MD data, the MDverse data explorer, which promises to be a very useful tool.

As the authors state: "Eventually, front-end solutions such as the MDverse data explorer tool can evolve being more user-friendly by interfacing the structures and dynamics with interactive 3D molecular viewers". This will make MD simulations accessible to non-specialists and researchers in other areas. I would envisage that this will also include approaches using interactive virtual reality for an immersive exploration of structure and dynamics, and virtual collaboration (e.g. O'Connor et al., Sci. Adv.4, eaat2731 (2018). DOI:10.1126/sciadv.aat2731)

The need to share data effectively, and to compare simulations and test models, was illustrated clearly in the COVID-19 pandemic, which also demonstrated a willingness and commitment to data sharing across the international community (e.g. Amaro and Mulholland, J. Chem. Inf. Model. 2020, 60, 6, 2653-2656 https://doi.org/10.1021/acs.jcim.0c00319; Computing in Science & Engineering 2020, 22, 30-36 doi: 10.1109/MCSE.2020.3024155). There are important lessons to learn here, for simulations to be reproducible and reliable, for rapid testing, for exploiting data with machine learning, and for linking to data from other approaches. Tiemann et al. discuss how to develop these links, providing good perspectives and suggestions.

I agree completely with the statement of the authors that "Even if MD data represents only 1 % of the total volume of data stored in Zenodo, we believe it is our responsibility, as a community, to develop a better sharing and reuse of MD simulation files - and it will neither have to be particularly cumbersome nor expensive. To this end, we are proposing two solutions. First, improve practices for sharing and depositing MD data in data repositories. Second, improve the FAIRness of already available MD data notably by improving the quality of the current metadata."

This nicely states the challenge to the biomolecular simulation community. There is a clear need for standards for MD data and associated metadata. This will also help with the development of standards of best practice in simulations. The authors provide useful and detailed recommendations for MD metadata. These recommendations should contribute to discussions on the development of standards by researchers, funders, and publishers. Community organizations (such as CCP-BioSim and HECBioSim in the UK, BioExcel, CECAM, MolSSI, learned societies etc) have an important part to play in these developments, which are vital for the future of biomolecular simulation.

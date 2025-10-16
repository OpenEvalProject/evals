# Author response - Round 1

Authors:
- Gregory M Noetscher ([ORCID: 0000-0001-9786-7206](https://orcid.org/0000-0001-9786-7206))
- Peter J Serano
- Marc Horner ([ORCID: 0000-0002-2483-5796](https://orcid.org/0000-0002-2483-5796))
- Alexander Prokop
- Jonathan Hanson
- Kyoko Fujimoto
- James Brown
- Ara Nazarian
- Jerome Ackerman ([ORCID: 0000-0001-5176-7496](https://orcid.org/0000-0001-5176-7496))
- Sergey N Makaroff

## Response text

DOI: [10.7554/eLife.90440.3.sa3](https://doi.org/10.7554/eLife.90440.3.sa3)

The following is the authors’ response to the original reviews.

The Authors wish to thank the Reviewers for their detailed and insightful comments. By properly addressing these critiques, we sincerely believe our finished product will be substantially improved and provide greater insight to the academic community.

Both Reviewers noted the importance of identifying the limitations of our study with particular emphasis on embedded implant heating due to switching gradient coils. Understanding the limitations of any model and/or simulation process is critical when adopting its use, especially when estimating the safety of embedded devices. For this reason, we have included the following text and corresponding references in our Discussion section:

While the workflow presented herein establishes a validated approach to estimate RF heating due to the presence of a passive implant within a human subject undergoing an MR procedure, certain limitations and proper use stipulations of this methodology should be identified. These include:

1. The approach of embedding a given passive implant must be carefully considered and supervised by an orthopaedic subject matter expert, preferably an orthopaedic surgeon. While the procedures described above focus on insertion and registration of an implant to make it numerically suitable for simulation, relevant anatomic and physiological considerations must also be addressed to ensure a physically realistic and appropriate result. This will enable a proper simulated fit and no empty spaces or unintended tissue deformations.

2. Temperature changes presented are due only to RF energy deposition. The results do not take into account the impact of low-frequency induction heating of metallic implants naturally caused by the switching gradient coils. Important work on this subject matter has recently been reported in [21],[22],[23],[24],[25],[26],[27]. Unless an orthopaedic implant has a loop path, heating due to gradient fields is typically less than heating due to RF energy deposition. The present testbed would be applicable to the induction heating of implants (and the expected temperature rise of nearby tissues), after switching from Ansys HFSS (the full wave electromagnetic FEM solver) to Ansys Maxwell (the eddy current FEM solver). Two examples of this kind have already been considered in [25],[45].

3. The procedures presented in this work have been based on the response of a single human model of advanced age and high morbidity.

4. Finally, validation was achieved using available published data [42]-[44] and relies upon the legitimacy and veracity of that data. Coil geometry, power settings, and other relevant parameters were taken explicitly from these sources and modeled to enable a faithful comparison.

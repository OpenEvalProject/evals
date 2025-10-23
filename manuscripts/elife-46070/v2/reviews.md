# Peer review - Round 1

Editors:
- Werner Kühlbrandt, Max Planck Institute of Biophysics Germany

Reviewers:
- Robert Crichton, Catholic University Louvain Belgium

## Review text

DOI: [10.7554/eLife.46070.031](https://doi.org/10.7554/eLife.46070.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Large protein organelles form a new iron sequestration system with high storage capacity" for consideration by eLife. Your article has been reviewed by Gisela Storz as the Senior Editor, a Reviewing Editor, and three reviewers. The following individual involved in review of your submission has agreed to reveal his identity: Robert Crichton (Reviewer #1).

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript presents a structural and mechanistic description of a recently discovered bacterial iron storage system based on a T4 icosahedral encapsulin shell carrying an iron-mineralising protein cargo of the iron mineralizing encapsulin-associated firmicute (IMEF) family. The study is sound and well communicated, and the findings are significant. The authors present a single-particle cryo-EM study of the encapsulin shell, and an X-ray crystal structure of the IMEF protein, which forms a ferroxidase center at its dimeric interface. A target peptide of the IMEF protein is shown to be essential to incorporation of the IMEF cargo into the encapsulin shell. The chemical composition of heterologously-expressed Enc-IMEF is analysed by EDS and EELS, and the ferroxidase activity is analysed to indicate that iron mineralisation by the full complex is limited by the rate of iron entry to the encapsulin shell.

Essential revisions:

Most of the comments pertain to improving the presentation and discussion of the work.

1) There seems to be a systemic problem with not introducing or explaining key ideas and relationships early enough. Some of the confusing points become partly clarified in the end after multiple readings. But for someone not well-acquainted with these systems, and frankly even for those closer to the subject, one is left without a clear sense of how different the findings and the specific structure should be considered compared to other studies on triangulated encapsulins and even HK97 phage capsids. The function, composition, equivalence or distinction compared to various encapsulins, is hard to absorb; could other encapsulins be doing this and it just hasn't been shown.

2) The authors state that 'A newly discovered class of protein organelles called encapsulin nanocompartments are implicated in microbial iron and redox metabolism and have so far only been shown to be involved in oxidative stress response (Giessen and Silver, 2017; He et al., 2016; McHugh et al., 2014; Sutter et al., 2008).', but cite a paper (McHugh, 2014) in which iron storage by an encapsulin is well documented. The authors' own work (Giessen and Silver, 2017) has previously shown that IMEF-Enc mineralises iron in vivo. I would therefore consider it established that encapsulins can function in iron storage.

3) Other issues related to clarity:

- Is IMEF a system or is IMEF a cargo protein?

-Retention of the 'cargo protein' name instead of a protein name based on homology and presumptive function allows questions to linger unnecessarily.

- The main statement about what protein construct/assembly is produced for study is (subsection “Overall structure of the cargo-loaded IMEF encapsulin”) "we produced homogeneous IMEF cargo-loaded encapsulins". What does that mean? What proteins were expressed?

- Subsection “Overall structure of the cargo-loaded IMEF encapsulin”: "as evidenced by comparison of the IMEF T =4 monomer with T = 1, T = 3 and T = 7 capsid proteins." What capsid proteins? Is this referring to all encapsulin and HK97 proteins or something else?

- There are places where "the" should probably be "a" instead, where a new idea hasn't been introduced previously. [subsection “Overall structure of the cargo-loaded IMEF encapsulin” on the flexibility of a linker in the cargo protein].

- Subsection “Structure and analysis of the IMEF cargo protein” says that a phylogeny analysis shows IMEF is a member of the Flp superfamily, but could not be detected as the sequence level. What is meant here? That the IMEF protein has sequence similarity to other proteins whose structures were known and could be assigned to the Flp superfamily despite not being able to detect sequence similarity to other Flp members?

A few technical issues also need to be addressed:

4) The following points can be addressed changes to the text:

- The issue of symmetry averaging and its presumptive effects on certain parts of the structure like the cargo are not handled cleanly (See subsection “Overall structure of the cargo-loaded IMEF encapsulin”; subsection “TP-mediated cargo-shell co-assembly”). The authors infer flexibility in some cases where lack of icosahedral symmetry in the presence of averaging would likely have the same effect. How would the cargo protein survive averaging if it sits as a single dimer bound to a pentamer at an icosahedral vertex?

- In subsection “Iron mineralization and storage by the IMEF system”, the logic about the shell permeability and kinetic curve shapes is unclear.

- In subsection “Iron mineralization and storage by the IMEF system”, the idea of being "channeled to pores" is contrasted with diffusion in the next phrase. But presumptive pore transport here is presumably diffusive. The physical ideas need to be spelled out more carefully.

- Grounds are lacking for the assertion in subsection “Overall structure of the cargo-loaded IMEF encapsulin” about the observed conformational diversity being important for pore function.

- In subsection “Non-covalent chainmail and thermal stability of the IMEF system”, the absence of a patent pore is not evidence for a gated pore.

- More caution is required on the claim of ions and density in the central regions of the capsid oligomers. For one, averaging often accentuates noise on symmetry axes. But further the identities/charge of any molecules there are entirely unknown; the densities could be water for example.

5) The authors discuss the probability that features of the cryo-EM map, including the IMEF densities, are artifacts of averaging, which is almost certainly the case. This could be mitigated by symmetry expansion (relion_particle_symmetry_expand) and focussed classification/refinement for a clearer picture of the IMEF protein within the encapsulin shell. This is not essential, but would strengthen the paper considerably.

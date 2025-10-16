# Peer review - Round 1

Editors:
- Timothy E Behrens, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101642.3.sa0](https://doi.org/10.7554/eLife.101642.3.sa0)

The authors show MRI relaxation time changes that are claimed to originate from cell membrane potential changes. This would be a substantial contribution if true because it may provide a mechanism whereby membrane potential changes could be inferred noninvasively. However, the membrane potential manipulations applied here are performed on a slow time scale and are known to induce cell swelling. Cell swelling has been previously shown to affect relaxation time. Experiments could be performed to rule out this hypothesis, but the authors have chosen not to perform these experiments. The study is therefore useful, but the evidence is incomplete.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101642.3.sa1](https://doi.org/10.7554/eLife.101642.3.sa1)

Summary:

This paper examines changes in relaxation time (T1 and T2) and magnetization transfer parameters that occur in a model system and in vivo when cells or tissue are depolarized using an equimolar extracellular solution with different concentrations of the depolarizing ion K+. The motivation has been revised to state that the results suggest a potential approach to non-invasively detect changes in membrane potential using MRI.

Strengths:

The authors argue that the use of various concentrations of KCL in the extracellular fluid depolarize or hyperpolarize the cell pellets used, and that this change in membrane potential is the driving force for the T2 (and T1-supplementary material) changes observed. In particular, they report an increase in T2 with increasing KCL concentration in the extracellular fluid (ECF) of pellets of SH-SY5Y cells. To offset the increasing osmolarity of the ECF due to the increase in KCL, the NaCL molarity of the ECF is proportionally reduced. The authors measure the intracellular voltage using patch clamp recordings, which is a gold standard. With 80 mM of KCL in the ECF, a change in T2 of the cell pellets of ~10 ms is observed with the intracellular potential recorded as about -6 mv. A very large T1 increase of ~90 ms is reported under the same conditions. The PSR (ratio of hydrogen protons on macromolecules to free water) decreases by about 10% at this 80 mM KCL concentration. Similar results are seen in a Jurkat cell line and similar, but far smaller changes are observed in vivo, for a variety of reasons discussed. As a final control, T1 and T2 values are measured in the various equimolar KCL solutions. As expected, no significant changes in T1 and T2 of the ECF were observed for these concentrations.

Weaknesses:

While the concepts presented are interesting, and the actual experimental methods seem to be nicely executed, the conclusions are not supported by the data for a number of reasons. This is not to say that the data isn't consistent with the conclusions, but there are other controls not included that would be necessary to draw the conclusion that it is membrane potential that is driving these T1 and T2 changes. The results are consistent with Stroman et al. Magn. Reson. in Med. 59:700-706 (increased T2 with KCL) as well as some other cited work. However all those authors emphasize that cell swelling is the mechanism, not cell membrane potentials.

It is well established that cells swell/shrink upon depolarization/hyperpolarization. Cell swelling is accompanied by increased light transmittance in vivo, and this should be true in the pellet system as well. In a beautiful series of experiments, Stroman et al. (2008) showed in perfused brain slices that the cells swell upon equimolar KCL depolarization and the light transmittance increases. The time course of these changes is quite slow, of the order of many minutes, both for the T2-weighted MRI signal and for the light transmittance. Stroman et al. also show that hypoosmotic changes produce the exact same timecourse as the KCL depolarization changes (and vice versa for the hyperosmotic changes - which cause cell shrinkage). Their conclusion therefore, was that cell swelling (not membrane potential) was the cause of the T2-weighted changes observed, and that these were relatively slow (on the scale of many minutes).

What are the implications for the current study? Well, for one, the authors cannot exclude cell swelling as the mechanism for T2 changes, as they have not measured that. It is however well established that cell swelling occurs during depolarization, so this is not in question. Water in the pelletized cells is in slow/intermediate exchange with the ECF, and the solutions for the two compartment relaxation model for this are well established see Menon and Allen, Magn. Reson. in Med. 20:214-227, 1991. The T2 relaxation times should be multiexponential (see point (3) further below). The current work cannot exclude cell swelling as the mechanism for T2 changes (it is mentioned in the paper, but not dealt with). Water entering cells dilutes the protein structures, changes rotational correlation times of the proteins in the cell and is known to increase T2. The PSR confirms that this is indeed happening, so the data in this work is completely consistent with the Stroman work and completely consistent with cell swelling associated with depolarization. The authors should have performed light scattering studies to demonstrate the degree cell swelling or shrinkage. Measuring intracellular potential is not enough to clarify the mechanism.

So why does it matter whether the mechanism is cell swelling or membrane potential? The reason is response time. Cell swelling due to depolarization is a slow process, slower than hemodynamic responses that characterize BOLD. And in fact, cell swelling under normal homeostatic conditions in vivo is virtually non-existent. Only sustained depolarization events typically associated with non-naturalistic stimuli or brain dysfunction produce cell swelling. Membrane potential changes associated with neural activity, on the other hand, are very fast. In this manuscript, the authors have convincingly shown a signal change that is virtually the same as what was seem in the Stroman publication, but they have not shown that there is a response that can be detected with anything approaching the timescale of an action potential. So one cannot definitely say that the changes observed are due to membrane potential. One can only say they are consistent with cell swelling, regardless of what causes the cell swelling. The First line of the discussion still claims that T2 relaxation time and pool size ratio (PSR) can detect responses to membrane potential changes modulated by ionic solutions. However, in the absence of cell swelling controls, this cannot be stated.

For this mechanism to be relevant to measuring neuronal activity directly or explaining techniques such DIANA, one needs to show that the cell swelling changes occur within a millisecond, which has never been reported. If one knows the populations of ECF and pellet, the T2s of the ECF and pellet and the volume change of the cells in the pellet, one can model any expected T2 changes due to neuronal activity. I think one would find that these are minuscule within the context of an action potential, or even bulk action potentials.

Comments on revisions:

The manuscript is well written and my previous methodological concerns have been clarified as well. There are no flaws in the experiments, but the interpretation really depends on simultaneous measurements of cell volume and membrane potential, which have yet to be done.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101642.3.sa2](https://doi.org/10.7554/eLife.101642.3.sa2)

Summary:

Min et al. attempt to demonstrate a mechanism whereby magnetic resonance imaging (MRI) can reflect changes in neuronal membrane potentials. They approach this goal by studying how MRI contrast and cellular potentials together respond to treatment of cultured cells with ionic solutions that are known to depolarize or hyperpolarize excitable cells. The authors specifically examine two MRI-based measurements: (A) the transverse (T2) relaxation rate, which reflects microscopic magnetic fields caused by solutes and biological structures; and (B) the fraction or "pool size ratio" (PSR) of water molecules estimated to be bound to macromolecules, using an MRI technique called magnetization transfer (MT) imaging. They see that depolarizing K+ and Ba2+ concentrations lead to T2 increases and PSR decreases that vary approximately linearly with parallel measurements of voltage in a neuroblastoma cell line and that change similarly in a second cell type. They also show that depolarizing potassium concentrations evoke T2 increases in rat brains, and that these changes are reversed when potassium is renormalized. Min et al. argue that their results suggest a basis for noninvasive functional imaging of cellular voltage signals. If this were true, it would help validate a recent paper published by some of the authors (Toi et al., Science 378:160-8, 2022), in which they claimed to be able to detect millisecond-scale neuronal responses by MRI.

Strengths:

The discovery of a mechanism for relating cellular membrane potential to MRI contrast could yield an important means for studying functions of the nervous system. Achieving this has been a longstanding goal in the MRI community, but previous strategies have proven insufficient for neuroscientific or clinical applications. The current paper suggests that one of the simplest and most widely used MRI contrast mechanisms-T2 weighted imaging-may indicate correlates of membrane potential if measured in the absence of the hemodynamic signals that most functional MRI (fMRI) experiments rely on. The authors make their case using quantitative tests that include some controls for ion and cell type-specificity of their in vitro results and reversibility of MRI changes observed in vivo.

Weaknesses:

The major weakness of the paper is that it uses only slow correlational experiments to probe the relationship between MRI contrast and membrane potential. The authors do not examine effects on the subsecond time scale that is of greatest interest, and they do not adequately consider how biophysical factors with only loose relationship to electrophysiological variables could explain their imaging results. Notably, depolarizing ionic solutions that perturb membrane potential can also induce changes in cellular volume and tissue structure that in turn alter MRI contrast properties similarly to the results shown here. For example, a study by Stroman et al. (Magn Reson Med 59:700-6, 2008) reported reversible potassium-dependent T2 increases in neural tissue that correlate closely with light scattering-based indications of cell swelling. Phi Van et al. (Sci Adv 10:eadl2034, 2024) showed that potassium addition to one of the cell lines used here likewise leads to cell size increases and T2 increases. In their revised manuscript, the authors acknowledge that cell swelling might contribute to the MRI signals they report, but they do nothing to probe the contributions or characteristics of such effects. If cell swelling accounted for the author's MRI results, it would likely operate on a time scale far too slow to yield useful indications of membrane potential. Given these considerations and the absence of data demonstrating correspondence of electrophysiological measures with MRI readouts on a fast time scale, the paper fails to provide evidence that membrane potential changes can be meaningfully detected by MRI.

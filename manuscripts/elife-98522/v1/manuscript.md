# An adaptable, reusable, and light implant for chronic Neuropixels probes

## Authors

- Célian Bimbard<sup>1</sup> ([ORCID: 0000-0002-6380-5856](https://orcid.org/0000-0002-6380-5856)) †
- Flóra Takács<sup>2</sup>
- Joana A Catarino<sup>3</sup>
- Julie MJ Fabre<sup>4</sup>
- Sukriti Gupta<sup>5</sup> ([ORCID: 0009-0004-5222-4775](https://orcid.org/0009-0004-5222-4775))
- Stephen C Lenzi<sup>2</sup>
- Maxwell D Melin<sup>6</sup>
- Nathanael O'Neill<sup>4</sup>
- Ivana Orsolic<sup>2</sup>
- Magdalena Robacha<sup>1</sup>
- James S Street<sup>4</sup>
- José M Gomes Teixeira<sup>3</sup> ([ORCID: 0000-0003-1787-1809](https://orcid.org/0000-0003-1787-1809))
- Simon Townsend<sup>7</sup>
- Enny H van Beest<sup>1</sup> ([ORCID: 0000-0002-2454-0445](https://orcid.org/0000-0002-2454-0445))
- Arthur M Zhang<sup>8</sup>
- Anne K Churchland<sup>6</sup> ([ORCID: 0000-0002-3205-3794](https://orcid.org/0000-0002-3205-3794))
- Chunyu A Duan<sup>2</sup>
- Kenneth D Harris<sup>4</sup> ([ORCID: 0000-0002-5930-6456](https://orcid.org/0000-0002-5930-6456))
- Dimitri Michael Kullmann<sup>4</sup> ([ORCID: 0000-0001-6696-3545](https://orcid.org/0000-0001-6696-3545))
- Gabriele Lignani<sup>4</sup> ([ORCID: 0000-0002-3963-9296](https://orcid.org/0000-0002-3963-9296))
- Zachary F Mainen<sup>3</sup> ([ORCID: 0000-0001-7913-9109](https://orcid.org/0000-0001-7913-9109))
- Troy W Margrie<sup>2</sup> ([ORCID: 0000-0002-5526-4578](https://orcid.org/0000-0002-5526-4578))
- Nathalie L Rochefort<sup>8</sup> ([ORCID: 0000-0002-3498-6221](https://orcid.org/0000-0002-3498-6221))
- Andrew Wikenheiser<sup>5</sup>
- Matteo Carandini<sup>1</sup> ([ORCID: 0000-0003-4880-7682](https://orcid.org/0000-0003-4880-7682))
- Philip Coen<sup>1</sup> ([ORCID: 0000-0003-1495-1061](https://orcid.org/0000-0003-1495-1061)) †

### Affiliations

1. UCL Institute of Ophthalmology, University College London London United Kingdom ([ROR:02jx3x895](https://ror.org/02jx3x895))
2. Sainsbury Wellcome Centre for Neural Circuits and Behaviour, University College London London United Kingdom ([ROR:04kjqkz56](https://ror.org/04kjqkz56))
3. Champalimaud Research, Champalimaud Centre for the Unknown Lisbon Portugal
4. UCL Queen Square Institute of Neurology, University College London London United Kingdom ([ROR:02jx3x895](https://ror.org/02jx3x895))
5. Department of Psychology, University of California, Los Angeles Los Angeles United States ([ROR:046rm7j60](https://ror.org/046rm7j60))
6. Department of Neurobiology, University of California, Los Angeles Los Angeles United States ([ROR:046rm7j60](https://ror.org/046rm7j60))
7. The FabLab, Sainsbury Wellcome Centre for Neural Circuits and Behaviour, University College London London United Kingdom ([ROR:04kjqkz56](https://ror.org/04kjqkz56))
8. Centre for Discovery Brain Sciences, School of Biomedical Sciences, University of Edinburgh Edinburgh United Kingdom ([ROR:01nrxwf90](https://ror.org/01nrxwf90))
9. Simons Initiative for the Developing Brain, University of Edinburgh Edinburgh United Kingdom ([ROR:01gghaa40](https://ror.org/01gghaa40))
10. Department of Cell and Developmental Biology, University College London London United Kingdom ([ROR:02jx3x895](https://ror.org/02jx3x895))

† Corresponding author

## Abstract

Electrophysiology has proven invaluable to record neural activity, and the development of Neuropixels probes dramatically increased the number of recorded neurons. These probes are often implanted acutely, but acute recordings cannot be performed in freely moving animals and the recorded neurons cannot be tracked across days. To study key behaviors such as navigation, learning, and memory formation, the probes must be implanted chronically. An ideal chronic implant should (1) allow stable recordings of neurons for weeks; (2) allow reuse of the probes after explantation; (3) be light enough for use in mice. Here, we present the ‘Apollo Implant’, an open-source and editable device that meets these criteria and accommodates up to two Neuropixels 1.0 or 2.0 probes. The implant comprises a ‘payload’ module which is attached to the probe and is recoverable, and a ‘docking’ module which is cemented to the skull. The design is adjustable, making it easy to change the distance between probes, the angle of insertion, and the depth of insertion. We tested the implant across eight labs in head-fixed mice, freely moving mice, and freely moving rats. The number of neurons recorded across days was stable, even after repeated implantations of the same probe. The Apollo implant provides an inexpensive, lightweight, and flexible solution for reusable chronic Neuropixels recordings.

## Introduction

Some fundamental cognitive processes develop across days (e.g. learning) and are best studied in naturalistic environments (e.g. navigation). To gain insights into these processes, it is necessary to record brain activity chronically and to be able to do so in freely moving animals. Chronic recordings in freely moving animals are possible with calcium imaging (Ghosh et al., 2011; Zong et al., 2022). However, accessing deep brain regions can require invasive surgery and fails to capture fast neural dynamics. Electrophysiology overcomes these issues: the temporal resolution is higher, deeper regions are readily accessible, and recordings can be made in freely moving animals. Substantial effort has thus been dedicated to developing devices for chronic electrophysiology recordings (Berényi et al., 2014; Chung et al., 2017; Chung et al., 2019; Ferguson et al., 2009; Ferreira-Fernandes et al., 2023; Newman et al., 2023; Okun et al., 2016; Schoonover et al., 2021; Shobe et al., 2015). But these devices are typically non-recoverable, are too heavy for use in smaller animals like mice, or record relatively few neurons.

With Neuropixels probes, many hundreds of neurons can be recorded in a single insertion (Jun et al., 2017; Steinmetz et al., 2021). These probes allow experimenters to produce brain-wide maps of neural activity in head-restrained mice using acute recordings (Allen et al., 2019; Benson et al., 2023; Steinmetz et al., 2019; Stringer et al., 2019). To track neurons across days, and to use freely moving animals, the probes can be implanted chronically, with procedures that are permanent (Jun et al., 2017; Steinmetz et al., 2021) or recoverable (Ghestem et al., 2023; Horan et al., 2024; Juavinett et al., 2019; Luo et al., 2020; Song et al., 2024; Steinmetz et al., 2021; van Daal et al., 2021; Vöröslakos et al., 2021). Permanent implants are lightweight and stable, but their use at scale is not financially feasible. Conversely, recoverable implants can be reused, but solutions need to be cheaper, lighter, more flexible, and easier to implant and explant. In particular, the only published recoverable implants for Neuropixels 2.0 probes may be too heavy for use with typical mice, and cannot be adjusted for different implantation trajectories (Steinmetz et al., 2021; van Daal et al., 2021).

To address these issues, we developed the ‘Apollo implant’ for the reversible chronic implantation of Neuropixels probes. The implant is named for its lunar module design: a recoverable payload module accommodates up to two Neuropixels probes and is reused across animals, and a docking module is permanently cemented to the skull during implantation. The design is open source and can be readily adjusted with editable parameters to change distance between probes, implantation depth, or angle of insertion.

Our eight independent laboratories have performed successful recordings with the Apollo implant in mice and rats, supporting the flexibility and simplicity of the design. The same Neuropixels probes have been reimplanted up to six times with no significant change in recording quality. Recordings were stable across weeks and sometimes months. This allows for recordings to cover the entirety of the probes (by recording from different sections across days), while minimizing setup time, and could facilitate the tracking of neurons across days. The design has been independently printed, adjusted, and implanted across labs, and implanted subjects included freely behaving mice and rats and head-fixed mice, with Neuropixels 1.0, 2.0α (a pre-release version), and 2.0 probes.

## Results

### Flexible design

The Apollo implant consists of two parts, the payload and the docking modules, inspired by previous designs (van Daal et al., 2021; Figure 1). Both parts can be 3D-printed in a variety of materials, although we typically used a combination of Nylon PA12 and Formlabs Rigid Resin. The Neuropixels 1.0, 2.0α, and 2.0 implants weigh 1.7, 1.3, and 0.9 g (Table 1). Payload modules can accommodate up to two parallel probes, with the second probe adding a further 0.4, 0.2, and 0.2 g. The Apollo implant is therefore 40% lighter than the only published Neuropixels 2.0α solution, which recommends animals are at least 25 g (van Daal et al., 2021; Steinmetz et al., 2021). This allows for use in smaller animals (e.g. female and water-restricted mice). The electronics are protected by lids with slots to accommodate the flex cables when not connected to the headstage (Figure 1A). To ensure the implant is maximally compact, flex cables can be folded into the cavity beneath the lids (Figure 1B). This minimizes implant height (29, 21, and 17 mm for a Neuropixels 1.0, 2.0α, and 2.0), reducing the moment of inertia above the head. The implant can be 3D-printed for $10 ($3 for each disposable module).

![Figure 1.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig1-v1.jpg)

**Figure 1.:** (A) Exploded view of the implant showing the two modules: the payload module, which accommodates up to two Neuropixels probes (protected by two lids), and the docking module. Zoom-in: scaled illustration of the tip of a 4-shank Neuropixels 2.0α probe. Each shank is 75 μm wide, with 250 μm center–center distance between shanks and 15/32 μm vertical/horizonal distance between electrode sites on each shank. (B) Assembled view of the implant, for 2.0α and 2.0 (top) and 1.0 (bottom) probes. (C) Illustration of implant flexibility. Compared with the standard model (left), the length of exposed probes (middle-left), spacing between probes (middle-right), and implantation angle (right) can all be adjusted with preset parameter changes in the software files (Video 1). (D) Constructor for the assembly of the payload and docking modules. The docking holder slides along the posts of the constructor, and optimally aligns with the payload module being held by the payload holder. This effectively eliminates the risk of breaking the shanks when combining modules.

**Table 1.**
 Implant weight depends on probe version and material.The weight for each implant version. We find these to vary with each print (5%), and with different services (10–15%). For consistency, these weights are calculated from part volume and the material density. The ‘Standard’ implant comprises PA12-Lids and Rigid4000-Payload/Docking modules. This is the most common implant used by experimenters, but the PA12-only implant has been used to reduce weight further. The total weights do not include the cement (0.2 g) to fix the probes to the payload module.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="6">Weights of implants (g)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td colspan="2">NP 1.0</td>
      <td colspan="2">NP 2.0-Alpha</td>
      <td colspan="2">NP 2.0-Commercial</td>
    </tr>
    <tr>
      <td></td>
      <td>Nylon PA12</td>
      <td>Rigid4000 Resin</td>
      <td>Nylon PA12</td>
      <td>Rigid4000 Resin</td>
      <td>Nylon PA12</td>
      <td>Rigid4000 Resin</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>0.36</td>
      <td>0.46</td>
      <td>0.29</td>
      <td>0.38</td>
      <td>0.18</td>
      <td>0.23</td>
    </tr>
    <tr>
      <td>Docking</td>
      <td>0.35</td>
      <td>0.45</td>
      <td>0.26</td>
      <td>0.34</td>
      <td>0.22</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>Lid (x2)</td>
      <td>0.61</td>
      <td>0.79</td>
      <td>0.41</td>
      <td>0.52</td>
      <td>0.25</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>Probe (x2)</td>
      <td colspan="2">0.80</td>
      <td colspan="2">0.38</td>
      <td colspan="2">0.33</td>
    </tr>
    <tr>
      <td>Screws (x4)</td>
      <td colspan="2">0.09</td>
      <td colspan="2">0.09</td>
      <td colspan="2">0.09</td>
    </tr>
    <tr>
      <td>Threads (x4)</td>
      <td colspan="2">0.08</td>
      <td colspan="2">0.08</td>
      <td colspan="2">0.08</td>
    </tr>
    <tr>
      <td>PA12 total</td>
      <td colspan="2">2.29</td>
      <td colspan="2">1.51</td>
      <td colspan="2">1.15</td>
    </tr>
    <tr>
      <td>Standard total</td>
      <td colspan="2">2.50</td>
      <td colspan="2">1.67</td>
      <td colspan="2">1.26</td>
    </tr>
  </tbody>
</table>

The implant is flexible and recoverable, allowing for different configurations, and the same Neuropixels probe(s) to be used multiple times (Figure 1C). Once the payload module is constructed, the distance between the two probes remains fixed. The docking module is connected to the payload module via small screws, which makes it easy to assemble, and disassemble upon explantation. Only the docking module is cemented to the animal’s skull, and it is covered with merlons to increase contact with the cement and therefore the stability of the implant. To facilitate different implantation depths and angles with the same payload module, both the length and base-angle of the docking module can be adjusted. The base of the implant thus remains parallel to the skull (Figure 1C) which improves stability and reduces weight by minimizing implant height and the quantity of cement required. All adjustments can be achieved by inexpert CAD users with preset parameters supplied in the editable files to change distance between probes (1.8–6.5 mm—beyond 6.5 mm, two implants can be used), implantation depth (2–6.5 mm), or angle of insertion (up to 20 degrees) (Video 1). As the fully editable files are provided, users can (and have) adjusted the implants to exceed these default boundaries, or create their own custom modifications which are also available online (see Methods).

![Video 1.](https://cdn.elifesciences.org/articles/98522/elife-98522-video1.mp4.jpg)

**Video 1.:** This video guide demonstrates how to change the shape of the implant using parameters in Autodesk Inventor software—facilitating changes in inter-probe distance, penetration depth, and angle of implantation.

To help combine the payload and docking modules, we designed a dedicated constructor (Figure 1D). The docking holder, containing a new docking module, slides onto the constructor posts, and the payload holder, containing the payload module, is fixed to the end. The two modules are thus coaxial, and the docking module can slide into position and be secured to the payload module without risk of damaging the probes. The constructor comprises 3D-printed parts and Thorlabs 6 mm poles for a one-time cost of $25.

### Assembly and implantation

A comprehensive protocol for assembly and implantation, including variations employed across labs, is provided in Methods. Payload modules are assembled with one or two Neuropixels probes. After probe-sharpening (see Methods, Figure 2—figure supplement 1A), an empty payload module was positioned on adhesive putty and coated with a thin layer of epoxy. The probe(s) can then be affixed and aligned to the payload module, either by eye or using graph paper, before covering the base and electronics with epoxy or dental cement (Figure 2A). The flex cable was folded and inserted into the lid and lids were then glued to the payload module (Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig2-v1.jpg)

**Figure 2.:** (A) Initial stage of payload assembly. The payload module is stabilized on Blue Tack while the first (top) and second (bottom, optional) probes are secured with epoxy. (B) Each flex cable is first folded into a cavity in the lid (top) before the lid is glued in place (bottom). (C) The completed payload module fixed in its holder before being attached to the constructor. (D) The combination of payload and docking modules in the constructor. Inset: after the screws have been added to combine the modules. (E) Before (left) and after (right) residual gaps were filled with Kwik-Cast. (F) Example of dual craniotomies performed with a drill (top – premotor cortex and striatum) or biopsy punch (bottom – bilateral superior colliculus). (G) Dual 4-shank probes at the initial stage of insertion into craniotomies performed with drill (top) or biopsy punch (bottom). (H) Finalized implant in anesthetized animal, after the docking module has been cemented to the skull.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Probes were sharpened before assembling the implant using a microgrinder (Narishige EG-45). (B) Before most implantations, probes were coated with a fluorescent marker (Vybrant V22888 or V22885, Thermo Fisher) by dipping them directly into the solution. (C) Example of detritus that can adhere to the probe shanks during explantation. This should be cleaned before reusing the implant (see Methods).

The payload module (new or previously used) was combined with a new docking module for each experiment. Docking modules were adjusted to match experimental requirements (e.g. insertion depth, angle, etc.). The docking module was secured in its holder and slid onto the arms of the constructor. The payload module was secured in its holder and attached to the end of the constructor (Figure 2C, D). The docking module holder was then slid along the constructor arms, and the two modules were secured with screws (Figure 2D). Before each experiment, any gaps in the assembled implant were filled (Figure 2E). Prior to each implantation, probes were typically coated with fluorescent dye for post-experiment trajectory tracking (Figure 2—figure supplement 1B).

Craniotomies were performed on the same day as the implantation, but this could be any time after assembly (Figure 2F). The implant was held using the 3D-printed payload holder and positioned using a micromanipulator. The eight shanks (in the case of a dual 4-shank implant) are positioned at the surface of the brain (Figure 2G). Care is taken to avoid large blood vessels, and the implant can be rotated and repositioned. If the vessel is not completely avoidable, the shanks can be positioned on each side of the blood vessel. Probes were inserted to the desired depth at a slow speed (3–5 µm/s). Finally, to complete the implantation, the docking module was cemented to the skull (Figure 2H).

### Explantation

Explantations were performed with a payload holder attached to a micromanipulator. The holder was aligned to the payload module, slid into place, and secured with a screw. The screws between the payload and the docking modules were then removed, and the payload module extracted (Figure 2—figure supplement 1B). Probes were cleaned with a Tergazyme solution, occasionally followed by a silicone cleaning solvent if Dural-Gel stuck to the probe. The payload module was combined with a new docking module for subsequent experiments.

Across laboratories, 97% of probes were recovered without any broken shanks (61/63 explanted probes, Supplementary file 1). In only two cases were probes damaged, and in one of those cases the skull integrity was compromised by infection (a rare occurrence) and the probe was likely broken before explantation. On six further occasions, probes stopped working due to connection errors (typically revealed by a ‘shift register’ error in SpikeGLX). The recovery rate is therefore 86% when including all connection errors. However, as this type of error is also observed with acute probe use, and there was no observable damage to the chronic probes, these failures may reflect long-term wear rather than any issue with the implant. Consistent with this, probes that failed with this error had typically been used for several months (Supplementary file 1). Outside of the originating laboratory (UCL), 95% of probes (19/20) were recovered without any broken shanks (90% when including all connection errors) demonstrating the ease with which new users adopt this design.

### Stability

We tested the stability of the Apollo implant with Neuropixels 1.0, 2.0α, and 2.0 probes (Figure 3). We implanted 48 mice using 4-shank Neuropixels 2.0α implants (20 mice with a single-probe implant and 13 mice with a dual implant), single-probe Neuropixels 2.0 implants (7 mice), and Neuropixels 1.0 implants (7 mice with a single-probe implant and one mouse with a dual), as well as 3 rats with a single Neuropixels 1.0 implant (Supplementary file 1). In many cases, the same implants were reused (up to six times) and remained fully functional across different animals (Supplementary file 1). Recordings were performed over a period of days to months. The probes were typically inserted 5–6 mm inside the brain, traversing multiple brain regions (Figure 3A, B). Because only 384 of the 5120 channels, termed a ‘bank’ of channels, can be recorded simultaneously on each 4-shank 2.0 probe, multiple recording sessions were often used to cover all recording sites located in the brain. Compared with acute recordings, this strategy dramatically reduces experimental setup time and complexity, and is especially beneficial for whole brain approaches. The raw signal quality did not seem to change across days (Figure 3C, D), allowing us to identify single spikes reliably for months. The spiking patterns on each probe were similar across days (Figure 3E, F), suggesting that the same populations of neurons were being tracked.

![Figure 3.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig3-v1.jpg)

**Figure 3.:** (A, B) Insertion trajectories of two simultaneously implanted 4-shank Neuropixels 2.0α probes, with respect to brain anatomy (Allen Mouse Brain Atlas, Wang et al., 2020). (C, D) Raw signal (bandpass filtered between 400 Hz and 9 kHz) across six channels, on day 16 and 88 post-implantation. (E, F) Number of spikes per second versus depth along the probe (y-axis) and days from implantation (x-axis) for the same implantation shown in A–D. The total number of spikes per second (across all detected units) is binned across depths for each day (20 µm bins). This mouse was recorded while head-fixed.

The number of recorded neurons was reasonably stable across weeks (Figure 4, Figure 4—figure supplements 1–3). For each session, we quantified the number of well-isolated single units for each individual channel bank (Figure 4A). Units were selected based on stringent criteria including amplitude, percentage of missing spikes, and refractory period violations (Fabre et al., 2023; van Beest et al., 2024). The number of single units for each probe is the sum of units across all banks within the brain (Figure 4A). Unit numbers could remain stable for more than 50 days, and we observed comparable stability in most of mice (Figure 4B). As previously described (Luo et al., 2020), we often observed an initial fast decrease in the number of units, but this was not systematic. Indeed, in some animals, unit number increased slowly across days until reaching a peak. The mean decrease in unit count per day was 3% (median 2%), within the range previously observed for chronic Neuropixels implants (Steinmetz et al., 2021). Although implants with more rapid unit loss were not suited for long-term recordings, others remained stable for months. Across all banks, the average number of recorded neurons on each bank was 85 ± 6 during the first 10 days (n = 59 probes, mean ± SEM), 65 ± 7 during days 10–50 (n = 50 probes), 54 ± 15 during days 50–100 (n = 6 probes), and 44 ± 25 beyond (n = 2 probes) (Figure 4—figure supplement 2). The initial number of units did not depend on the number of times the probe was reimplanted (p > 0.25, linear mixed-effects model, Figure 4C) or the insertion coordinates of the probe (p > 0.94, linear mixed-effects model, Figure 4D). The rate of unit loss was also independent of these two variables (p > 0.29 and p > 0.31 for probe reuse and AP position, linear mixed-effects model, Figure 4E, F). However, implant quality was more variable in posterior brain regions, with instances of rapidly decreasing neuron counts, as previously described (Luo et al., 2020). Stability was qualitatively similar across different laboratories (Figure 4—figure supplement 1). Surgical optimizations are ongoing, and protecting the craniotomy with silicon may significantly increase recording stability (Figure 4—figure supplement 3, Melin et al., 2024).

![Figure 4.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig4-v1.jpg)

**Figure 4.:** (A) Total number of recorded units across days for individual channel banks (thin lines), and across each probe (thick lines), for the same implantation as in Figure 3. Lines: logarithmic fits. (B) Logarithmic fits across all implantations where a full survey of the probe was regularly performed (orange, implantation from Figure 3). Full probe surveys were performed only in the primary lab (head-fixed conditions). (C) Unit count versus number of implantations. Connected dots represent single probes, reused up to six times. No criteria were used to select probes for reuse, and this decision was based solely on probe availability and experimental need. Slopes were quantified on individual banks and averaged for each probe before applying a linear mixed-effects model (thick line). (D) Unit count versus antero-posterior position of the insertion, relative to bregma. (E, F) Same as (C, D) but for the slope of the unit count decay. (G–L) Same as (A–F) but for the root-mean-square (RMS) value of the raw signal. For C–F and I–L, all mice are used and shown (head-fixed and freely moving conditions). Rats were excluded because their insertion coordinates cannot be matched with the mice, but their individual results are shown in Figure 4—figure supplement 1. All p-values shown come from a linear mixed-effects model.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Number of recorded units as a function of days from implantation, for all the secondary labs. Each color corresponds to a different lab, and each line is a different bank for a specific probe and animal. (B) Root-mean-square (RMS) values as a function of days from implantation, for all the secondary labs. (C) Median unit amplitude as a function of days from implantation, for all the secondary labs. The high amplitude values (yellow) come from the recordings in rats. All secondary labs used this implant as part of their own study, explaining the diversity of length and types of protocols.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Number of recorded units per bank as a function of days, averaged across all banks for each animal (gray) or averaged across animals (black, mean ± SEM, n changing across bins).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** As in Melin et al., 2024, a drop of silicon (Kwik-Sil) was added to cover the craniotomy before closing the implant with cement. Although anecdotal, the stability of recorded units in this mouse was excellent, suggesting that silicon may improve implant stability.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** (A) Median unit amplitude across days for individual channel banks (thin lines), and across each probe (thick lines), for the same implantation as in Figure 3. Lines: logarithmic fits. (B) Logarithmic fits across all implantations where a full survey of the probe was regularly performed (orange, implantation from Figure 4). (C) Median unit amplitude versus number of implantations. Connected dots represent single probes, reused up to six times. The slope is quantified with a linear mixed-effects model (thick line). (D) Median unit amplitude versus antero-posterior position of the insertion, relative to bregma. (E, F) Same as (C, D) but for the change in amplitude over days.

The overall quality of the signal remained high throughout days and probe reuses. We quantified the overall noise present in the recordings by computing the root-mean-square (RMS) value of the raw signal (Figure 4G–L). The RMS values were stable across days, across all mice (Figure 4G, H). Both the average RMS value and its changes over time were independent of the number of times the probe had been used (Figure 4I, K). We observed a significant effect of AP position on the RMS value, but not on its changes over time (Figure 4J, L). Similarly, the median unit amplitude was stable and unaffected by probe reuse (Figure 4—figure supplement 4).

Individual neurons could be tracked across days and months (Figure 5). We used the tracking software UnitMatch to track the same units across days, based on their waveforms (van Beest et al., 2024). In a mouse recorded for 100 days, a significant fraction of units could be tracked for months (Figure 5A, B). Tracked neurons had stable waveforms over days, as expected from the matching procedure, but also stable inter-spike intervals histograms (ISIHs) (Figure 5C, D). These ISIHs were not used to match neurons across days, and their stability therefore strongly suggests the same units were tracked over months. The proportion of units tracked between two recordings decreased as a function of time between the recordings (Figure 5E). For two recordings on the same day, 50% of neurons were matched, suggesting an upper limit in neuron tracking with the method we used, likely due to variability in neural activity or conservative choices in software parameters. The proportion of tracked neurons typically decreased to 10% after 32 days, but the rate of decay varied across recordings: with some cases where 20% of neurons were tracked for 64 days, and others dropping to 0% after a week. In all cases, tracked units had consistent ISIHs, as measured by the area under the receiver operating characteristic curve (AUC)—comparing the similarity of ISIHs for tracked versus different units (Figure 5F). This indicates the tracking algorithm remains accurate for large intervals between recordings.

![Figure 5.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig5-v1.jpg)

**Figure 5.:** (A) Unit presence across all recordings (left). Only the units present in at least one of the first 3 days are shown for ease of visualization. Units are ordered by the number of recordings in which their presence was detected (right). (B) Spatial layout of the population of neurons tracked across days. In this example, the recording sites were spanning two shanks of a 4-shank 2.0α probe (green rectangle in Figure 3E). (C) Average waveforms of four example tracked units, computed for 7 days across a 13-week period. (D) As in C, but showing the inter-spike interval (ISI) histogram of each unit on each day. (E) Probability of tracking a unit as a function of days between recordings, for individual mice (gray), including example from A to D (orange), or the average across all mice (black, mean ± SEM across datasets). (F) The average AUC values when comparing the ISI histogram correlations of tracked versus non-tracked neurons. Colors same as (E).

### Freely behaving animals

To test whether the Apollo implant could be used in more naturalistic conditions, we recorded from freely behaving mice and rats in various configurations (Figure 6). First, to minimize the weight, we recorded from two freely moving mice using either a dual Neuropixels 2.0α implant or a Neuropixels 1.0 implant, with the headstage suspended by its connection cable (Figure 6A, B). The mice explored their home cage and exhibited normal behaviors, such as grooming, running, and sleeping, suggesting that the implant did not impair basic movements. The recordings yielded high-quality, well-isolated single units for weeks (Figure 6C, Figure 4—figure supplement 1). The distributions of the RMS values (Figure 6D) and spike amplitudes (Figure 6E) were similar to the head-fixed conditions, suggesting an equivalent quality of recording despite differences in conditions, and labs. It can also be more convenient to secure the position of the headstage in each recording, or permanently attach the headstage to the implant. We thus designed a headstage holder, which we tested with Neuropixels 1.0 (Figure 6F–J). To further reduce the weight on the mouse, we also designed a 1-probe version of the implant for Neuropixels 2.0, with a minimal headstage holder (Figure 6K–O), inserted at an angle (16 or 25 degrees), at the back of the brain. In rats (Figure 6P–T), the implant was inserted in the center of a 3D casing, that afforded extra protection, and neural data was recorded wirelessly using SpikeGadgets.

![Figure 6.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig6-v1.jpg)

**Figure 6.:** (A) Neuropixels 1.0 and 2.0α were used with freely moving mice. The headstage was suspended by the wire above the implant. (B) Animal freely moving with the 1.0 version of the implant, with headstage attached. (C) Raw signal (bandpass filtered between 400 Hz and 9 kHz) across multiple channels of increasing depth, on 2 days post-implantation. (D) Mean distribution of the root-mean-square (RMS) value across channels, averaged across all recordings in head-fixed mice (black, n = 2 mice) and freely moving (cyan, n = 35 mice). (E) Same as (D), but for the distribution of the units’ amplitude. (F) As in (A), but with an additional headstage holder for Neuropixels 1.0 (n = 4 mice). (G–J) As in (B–E) but for recordings with the headstage holder from (D). (K) Miniature, 1-probe implant for Neuropixels 2.0, with a headstage holder (n = 8 mice with both 2.0 and 2.0α probes). (L–O) As in (B–E) but using the modified design from (G). (P) Configuration for rats, with a casing to protect the implant (SpikeGadgets – without the lid, n = 3 rats). The final configuration comprises the wireless recording system. (Q–T) As in (B–E) but with the apparatus from (P), recorded in rats. Not that the reference head-fixed data is from mice.

To quantify the effect of implantation on behavior, we compared the performance of mice on a complex behavioral task before and after implantation with a Neuropixels 1.0 probe—the heaviest version of the Apollo Implant (Table 1). This implant was modified to allow the headstage to be permanently attached from the first recording session (see Methods). Mice were placed in a large octagonal arena (80 cm diameter). On each trial, mice were required to respond to visual stimuli projected onto the floor of the chamber and perform a nose poke in one of the ports located around the perimeter of the chamber. Thus, during a typical session of 100 trials, mice typically traversed tens of meters (Figure 7A). We compared mouse hit rate, trial number, and reaction times in sessions before implantation (when the mouse moved entirely freely) and after implantation (when the mouse was tethered). After implantation, mice continued to perform trials and fully explore the chamber (Figure 7B). We observed an initial reduction in hit rate and trial number, and an increase in reaction time immediately after implantation (Figure 7C–E). The first two measures recovered within five sessions (Figure 7C, D), but reaction times did not recover to pre-implantation levels, indicating that implantation may impact mobility in physically demanding tasks. Although we cannot disambiguate whether these changes are due to tethering, or the implant, it represents the maximal impact of the implantation, particularly as the heaviest Apollo implant was used. Therefore, the consistent hit rate and trial number, in a complex task requiring exploration in a large arena, demonstrates that the implant is well-suited to extended recordings from freely moving mice.

![Figure 7.](https://cdn.elifesciences.org/articles/98522/elife-98522-fig7-v1.jpg)

**Figure 7.:** (A) Trajectories (gray) of single mouse in an example session prior to implantation. Blue and red dots indicate mouse position at the start and end of each trial. (B) As in (A), but for an example session post-implantation. (C) The hit rate (percentage of correctly completed choices) made by two mice (magenta and brown) in the four sessions immediately before implantation (Pre), immediately after implantation (Recovery), and the subsequent four sessions after this recovery period (Post). n = 2 mice, 4 sessions per mouse at each time period. (D) As in (C), but for the number of trials per session. (E) The probability of each reaction time for the same sessions in A and B, separated by mouse.

## Discussion

To record large populations of neurons across days and during freely moving behaviors we developed the ‘Apollo implant’: a chronic implant for Neuropixels 1.0 and 2.0 probes. This solution is easily implanted and recovered, inexpensive, lightweight, flexible, and stable. We successfully tested the implant across multiple labs, setups (head-fixed or freely moving), and species (mice and rats), recording neural populations across weeks and even months.

The design of the Apollo implant builds upon past advances in chronic devices for Neuropixels probes (Juavinett et al., 2019; Luo et al., 2020; Steinmetz et al., 2021; van Daal et al., 2021; Vöröslakos et al., 2021) to improve on several aspects: weight, price, flexibility, and ease of use. The implant is optimized for animals that cannot carry heavy loads, like mice and especially female and water-controlled mice, which have lower body weight. Because the headstage is not permanently fixed to the implant, the animal carries less weight outside of recordings, and a single headstage can be used with multiple animals in sequence. However, the flexible design allows for the headstage to be permanently attached to an implant, which increases experimental ease at the expense of some additional implant weight. The implant is strong enough to be carried by rats with the addition of a protective 3D outer casing (see Methods), but its use in stronger animals, like ferrets or primates, remains untested. For applications requiring even lighter implants, such as birds, printing materials can be selected to further reduce weight. The lightweight design enables animals to perform complex and demanding freely moving tasks, but also allows experimenters to implant female and water-restricted mice while respecting animal welfare weight limitations.

The Apollo implant is more flexible than previously published solutions. A unique aspect of our modular design is that different docking modules can be used when reimplanting the same payload module, which enables a variety of recording configurations (brain regions, animals, and experimental setups) that would not have been possible with previous designs. The provided CAD files are fully editable and open source, allowing experienced users to modify the parts as needed. For inexpert users, the files are populated with predefined key dimensions that can be easily adjusted to accommodate changes in several features, including inter-probe distance, angle of implantation, and the length of exposed probes. This ensures the implant remains close to the skull for each experiment, minimizing surgical complications, implant weight (less bonding agent is needed), and moment of inertia (height is minimized). Indeed, even with the heavier Neuropixels 1.0 implants, freely moving mice maintained consistent performance on a complex task after implantation.

Although adapting the design to other commercially available silicon probes is beyond the scope of this study, the flexible design paves the way for future adaptations by individual groups. Because of the low component-cost ($3 per docking module), testing custom modifications is also more cost-effective than with previous solutions. This combination of flexibility and affordability is exemplified by the modifications already used across the eight labs providing data for this manuscript.

With the Apollo implant, the number of recorded neurons exhibited good stability across days, regardless of the number of times the probe had been reimplanted. To provide a realistic estimate for the number of high-quality units that could be recorded across days, we used stringent quality metrics based on unit waveform and spiking properties. Predicting the stability of an implantation was difficult and did not seem to correlate strongly with the quality of surgery (e.g. a small bleed during craniotomy, or ease of probe insertion). We observed more variable stability at the back of the brain, especially in superior colliculus, possibly due to the mechanical constraints imposed during head movements.

The Apollo implant allows for the insertion of up to two parallel probes simultaneously. This can be advantageous: it simplifies surgeries by reducing insertion time and allows probes to be placed in close proximity. However, some users may need to insert multiple probes at different angles. In this case, we are aware of two implant solutions in development that could be better suited, although to our knowledge these remain untested outside the authors’ own groups and have only been used in mice (A Aery Jones, 2023; Melin et al., 2024).

We have demonstrated that neurons recorded with the Apollo implant can be effectively tracked across days, consistent with previous characterizations of chronic Neuropixels implants (Steinmetz et al., 2021; van Beest et al., 2024). van Beest et al. provide further evidence of neurons tracked with the Apollo implant, and a rigorous quantification of the number of neurons that one can expect to track with these methods. We expect the success of these methods to vary across model systems due to differences in waveform properties—for example, we observed qualitatively higher unit amplitudes in rats in this study. The ability to track neurons across these timescales promises to enhance our understanding of cognitive processes that evolve over long timescales, such as learning or aging.

Overall, the Apollo implant fills an important need to facilitate chronic electrophysiology with Neuropixels probes, particularly in small animals. The simplicity and flexibility of its design are exemplified by the eight independent groups that have successfully used the implant and contributed data to this manuscript.

## Methods

Experimental procedures at UCL and University of Edinburgh were conducted according to the UK Animals Scientific Procedures Act (1986), the European Directives 86/609/EEC and 2010/63/EU on the protection of animals used for experimental purposes, and the Animal Welfare and Ethical Review Body (AWERB). Procedures were conducted under personal and project licenses released by the Home Office following appropriate ethics review.

Experimental procedures at UCLA conformed to the guidelines established by the National Institutes of Health and were approved by the Institutional Animal Care and Use Committee of the University of California, Los Angeles David Geffen School of Medicine.

Experimental procedures at Champalimaud were approved and performed in accordance with the Champalimaud Centre for the Unknown Ethics Committee guidelines and by the Portuguese Veterinary General Board (Direção-Geral de Veterinária, approval 0412/2022).

### Implant design and materials

All parts of the implant (except the constructor probes, Thorlabs) were designed using Autodesk Inventor Professional 2023 software, acquired free of charge through the renewable education plan. Parts were 3D-printed by external companies (primarily SGD 3D, https://sgd3d.co.uk/), or at the SWC FabLab. Stereolithography (SLA, using Rigid4000 resin, Formlabs) was typically used for the payload and docking modules, the docking holder, and the constructor head. Selective laser sintering (using Nylon PA12) was typically used for the payload module lids and payload holder. Brass threaded inserts were manually added to the payload module, payload holder, and docking holder using a soldering iron after printing. For parts (e.g. the payload and docking modules) where strength and inflexibility were advantageous, we used Rigid4000 resin, although this material is denser than Nylon PA12. With this combination, the Neuropixels 1.0, 2.0α, and 2.0 implants weigh 1.7, 1.3, and 0.9 g. The weight of the implants can be further reduced to 1.5, 1.1, and 0.8 g if all parts are printed with Nylon PA12. The full-PA12 implants have been successfully used with 1.0 probes, but remains untested with the 2.0 versions. The miniaturized Neuropixels 2.0 implant with headstage holder weighed 0.6 g by itself or 1.1 g with the probe epoxied and ground attached. All probes used, and any resulting issues/breakages are detailed in Supplementary file 1. Damage resulting from historical procedural steps that are no-longer used (e.g. manually separating the shanks of a 4-shank probe with a needle, now achieved by de-ionized water or strong solvant) or carelessness during probe handling outside of mounting, implantation and explantation are not indicated in the table as they are independent of the implant itself.

In addition to the 3D-printed implant, the following materials are required (due to variable supply, up-to-date links are provided in the GitHub repository):

### Implant assembly, implantation, and explantation protocol

What follows is the protocol used by the originating laboratory with some minor variants. This is the most thoroughly tested and recommended approach. Methods employed by each individual lab are detailed in a later section.

#### Payload module assembly—once per Apollo implant

The payload modules were assembled with either one or two Neuropixels probes. First, all parts were assembled by hand without the probes to ensure a good fit first before fixing the probes permanently to the holder.

#### Combining payload and docking modules

For each implantation, a new or previously used payload module was combined with a new docking module. The docking module could be varied between experiments to adjust for variables including insertion depth, angle, or headplate-compatibility.

#### Implantation

Craniotomies were performed on the day of the implantation, under isoflurane (1–3% in O2) anesthesia, and after injection of appropriate analgesia and anti-inflammatory drugs (usually Colvasone and Carprofren). Headplate surgery was performed in most cases, either days before or on the same day. The eyes of the animal were protected throughout surgery using eye lubricant.

#### Explantation

Explantations were performed under light isoflurane anesthesia (1–3% in O2).

### Lab-specific methods

#### Payload module assembly

##### Carandini-Harris laboratory

##### Churchland laboratory

##### Duan laboratory

##### Kullman/Lignani laboratories

##### Mainen laboratory

##### Margrie laboratory

##### Rochefort laboratory

##### Wikenheiser laboratory

### Implantation

#### Carandini-Harris laboratory

#### Churchland laboratory

#### Duan laboratory

#### Kullman/Lignani laboratories

#### Mainen laboratory

#### Margrie laboratory

#### Rochefort laboratory

#### Wikenheiser laboratory

### Data acquisition

#### Carandini-Harris laboratory

#### Churchland laboratory

Grounding: Bone screw.

#### Duan laboratory

#### Kullman/Lignani laboratories

#### Mainen laboratory

#### Margrie laboratory

#### Rochefort laboratory

#### Wikenheiser laboratory

### Data processing

Sessions were automatically spike-sorted using pyKilosort (Banga et al., 2022), python port of Kilosort (Pachitariu et al., 2016; version 2.0), and automatically curated using Bombcell (Fabre et al., 2023). One mouse (GB012) was spike-sorted using Kilosort 4 (Pachitariu et al., 2024).

A variety of parameters were used to select high-quality units, based either on their waveform and their spiking properties.

The template waveform-based criteria were: (1) a maximum of two peaks and one trough, (2) a spatial decay slope below −3 µV·µm−1, defined as the slope of a linear fit (using the MATLAB polyfit function) between the maximum absolute amplitude of the peak channel and nearest five channels along the length of the probe (i.e. 75 µm away for Neuropixels 2.0), (3) a duration between 0.1 and 0.8 ms (Deligkaris et al., 2016), and (4) fluctuations during baseline not exceeding 30% of the peak amplitude. The raw waveform-based criteria, computed using at least 1000 randomly sampled spikes, were: (1) a minimum mean amplitude of 20 µV (only 1% of units had amplitudes below 30 µV, and increasing this threshold to 50 µV did not affect the results), and (2) a minimum mean signal-to-noise ratio of 0.1, defined as the absolute maximum value divided by the baseline variance. Both somatic and non-somatic spikes (Deligkaris et al., 2016) were kept.

The spiking properties-based criteria were: (1) a minimum of 300 spikes, (2) less than 20% of spikes missing, estimated by fitting a Gaussian to the spike amplitude distribution with an additional cut-off parameter below which no spikes are present, (3) a maximum of 10% refractory period violations, using a previously published approach (Hill et al., 2011), defining the censored period as 0.1 ms and estimating the refractory period using a window between 0.5 and 10 ms, and (4) a minimum presence ratio of 0.2, defined as the fraction of 1 min bins with at least one spike.

### Data analysis

Raw traces (Figures 3C, D, 6C) were obtained by bandpass filtering each channel from spikeGLX between 400 and 9000 Hz (using the MATLAB bandpass function) and subtracting the median across channels. The RMS value was computed on the processed signal, and the median across all channels was used to summarize each recording.

To obtain the total number of spikes per second at each depth along the probe (Figure 3E, F), we summed spikes across all units present within each 20 µm depth bin.

In the case of 4-shank probes, we estimated the number of recorded units for a probe on a given day (Figure 4A, B) by summing units from a complete set of independently recorded banks—a set of channel banks that tiled the entirety of the implanted probe—when available. Because each such set was recorded across at least 2 days, we used the closest recordings within a window of 5 days, centered on the day of interest. Days were excluded if it was not possible to form a complete set of banks within a 5-day window.

To obtain $P$ the percentage change in unit count $N_{d}$ across days $d$ (4C–F), we fit an exponential decay function to the number of units detected on each bank across days and extracted the decay parameter $\tau$:

$$
N_{d}=N_{0}10^{\taud}
$$

$P$ was defined as:

$$
P=100\times(\frac{N_{d+1}}{N_{d}}−1)=100\times(10^{\tau}−1)
$$

$P$ was averaged across all longitudinally recorded banks from each implantation to obtain a single value. Only banks with at least three recordings were included.

The median of the units’ amplitude and the median RMS values were fitted using a linear fit. Similarly, a single value for each implantation was obtained by taking the variable’s mean value across all banks.

To estimate the effect of repeated probe use, $U$, and antero-posterior and medio-lateral insertion coordinates ($Y$ and $X$) on a variable of interest (e.g. the percentage change in unit count, or the RMS values) across days, we used a linear mixed-effects model (using the MATLAB fitlme function):

$$
P∼1+Y+X+U+(1|probeID)+(U−1|probeID)
$$

Here, $P$ is the response variable, $Y,X,$ and $U$ are fixed effect terms, and $probeID$ (the probe identity) is the single grouping variable. We then assessed whether $Y,X,$ or $U$ had a significant effect on the response variable.

To track neurons across days (Figure 5), we used UnitMatch, which uses only the neurons’ waveform (van Beest et al., 2024). We identified cell presence across days using the intermediate algorithms, which have been shown to maximize the probability of tracking neurons while preserving a low false-positive rate. We then identified the neurons that were tracked across 6 arbitrary days spanning the whole recording period. The inter-spike intervals were computed as the distribution of the times between consecutive spikes, binned on a logarithmic scale from 0 to 5 s. As in van Beest et al., 2024, to compute the probability of a unit being tracked, we looked at each unit across all recordings and computed the probability of this unit being tracked in previous or subsequent recordings. These probabilities were then averaged across all the units from each animal, and averaged across animals.

To quantify the amount of information present in the distributions of the correlations of the fingerprints, we computed the ROC curve for different populations of pairs (from putative matched units or nonmatched units) across days. We then computed the area under the ROC curve (AUC) to quantify this difference between distributions. Only sessions with at least 20 matched units were considered. Units that had a match within recordings were excluded from this analysis. For each mouse, the AUCs were then averaged across recording locations.

To compute the distributions of RMS values and unit amplitudes (Figure 6), we computed these distributions first for single sessions (across channels and units, respectively), and then computed the average distribution across sessions and animals.

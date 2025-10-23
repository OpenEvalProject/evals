# Two-subunit DNA escort mechanism and inactive subunit bypass in an ultra-fast ring ATPase

## Authors

- Ninning Liu<sup>1</sup>
- Gheorghe Chistol<sup>1</sup>
- Carlos Bustamante<sup>1</sup> †

### Affiliations

1. Jason L. Choy Laboratory of Single Molecule Biophysics University of California Berkeley United States
2. Department of Molecular and Cell Biology University of California Berkeley United States
3. Department of Physics University of California Berkeley United States
4. California Institute for Quantitative Biosciences Berkeley United States
5. Department of Chemistry Howard Hughes Medical Institute, University of California Berkeley United States
6. Physical Biosciences Division Lawrence Berkeley National Laboratory Berkeley United States
7. Kavli Energy NanoSciences Institute at the University of California, Berkeley and the Lawrence Berkeley National Laboratory Berkeley United States

† Corresponding author

## Abstract

10.7554/eLife.09224.001 SpoIIIE is a homo-hexameric dsDNA translocase responsible for completing chromosome segregation in . Here, we use a single-molecule approach to monitor SpoIIIE translocation when challenged with neutral-backbone DNA and non-hydrolyzable ATP analogs. We show that SpoIIIE makes multiple essential contacts with phosphates on the 5'→3' strand in the direction of translocation. Using DNA constructs with two neutral-backbone segments separated by a single charged base pair, we deduce that SpoIIIE’s step size is 2 bp. Finally, experiments with non-hydrolyzable ATP analogs suggest that SpoIIIE can operate with non-consecutive inactive subunits. We propose a two-subunit escort translocation mechanism that is strict enough to enable SpoIIIE to track one DNA strand, yet sufficiently compliant to permit the motor to bypass inactive subunits without arrest. We speculate that such a flexible mechanism arose for motors that, like SpoIIIE, constitute functional bottlenecks where the inactivation of even a single motor can be lethal for the cell. Bacillus subtilis DOI: http://dx.doi.org/10.7554/eLife.09224.001

## Introduction

The ASCE [Additional Strand Conserved E (glutamate)] division of oligomeric, ring-shaped NTPases encompasses a diverse range of enzymes that function as molecular motors (Lyubimov et al., 2011). Within the ASCE division, the FtsK/SpoIIIE family of motors is involved in the fundamental process of DNA segregation prior to cell division. During the Bacillus subtilis sporulation lifecycle, an asymmetric division septum closes around one of the sister chromatids before complete chromosome segregation, trapping about two-thirds of the chromosome in the mother cell compartment (Burton et al., 2007; Wu and Errington, 1994). To complete chromosome segregation, SpoIIIE must translocate the DNA from the mother cell into the forespore. SpoIIIE and its closely related Escherichia coli homologue FtsK, contain an N-terminal transmembrane domain that anchors the protein to the division septum, a long unstructured polypeptide linker and a C-terminal-soluble motor domain consisting of subdomains α, β, and γ (Barre, 2007). Subdomains α and β adopt a RecA-like fold containing ATP binding and hydrolysis motifs (Massey et al., 2006), while subdomain γ imparts translocation directionality to the motor (sequence dependence) (Besprozvannaya et al., 2013; Lee et al., 2012; Löwe et al., 2008; Ptacin et al., 2006; 2008). Crystallography and electron microscopy studies indicate that both FtsK and SpoIIIE form homo-hexameric rings, and that double-stranded DNA (dsDNA) is threaded through their central pore (Cattoni, et al., 2014; Cattoni et al., 2013; Massey et al., 2006).

A distinguishing characteristic of SpoIIIE/FtsK is their enormous translocation velocity (∼5 kbp/s) and their ability to work against high forces (Ptacin et al., 2008; Saleh et al., 2004). Previous single-molecule studies of these motors focused primarily on investigating the mechanism of sequence recognition and translocation direction reversal (Lee et al., 2012; Pease et al., 2005; Ptacin et al., 2006; 2008; Saleh et al., 2004), studying how they strip off DNA-bound proteins (Lee et al., 2014; Marquis et al., 2008), and determining the amount of supercoils introduced in the DNA during translocation (Saleh et al., 2005). However, many fundamental aspects of these motors’ operation remain poorly understood: How does the motor interact with its DNA track during translocation? What is the motor step size? How does the motor coordinate the activity of its individual subunits? How is the subunit coordination mechanism optimized for the motor’s specific biological task?

To answer these questions, we used single-molecule manipulation and measurement techniques. Using modified DNA with a neutral backbone, we show that SpoIIIE makes critical electrostatic contacts with the phosphate backbone on the 5'→3' strand in the direction of translocation. This observation indicates that the individual subunits operate in a well-defined sequential order around the ring. To determine the SpoIIIE step size, we challenged the motor to translocate a DNA molecule containing two neutral segments of variable lengths separated by a charged base pair. This hybrid construct revealed the periodicity of motor–DNA interactions, suggesting that each SpoIIIE subunit takes a 2-bp step per ATP hydrolyzed. Experiments where non-hydrolyzable nucleotides were used to probe the intersubunit coordination within the motor suggest that SpoIIIE can tolerate non-consecutive inactive subunits, implying a degree of flexibility in the sequential operation of the motor. Finally, we propose a two-subunit DNA escort model that can rationalize all these data and that correctly predicts the degree of supercoiling introduced by SpoIIIE during translocation.

## Results

To monitor DNA translocation by SpoIIIE, we used a single-molecule assay developed previously (

![Figure 1.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig1-v3.jpg)

**Figure 1.:** (a) Experimental geometry of the optical tweezers assay. Neutral MeP DNA (red) was placed roughly 4 kb away from the end of the dsDNA tether (blue) that is attached to the optically trapped bead. (b) Sample traces of individual SpoIIIE motors translocating on DNA with a 30-bp dsMeP insert (magenta). Control experiments with DNA containing no MeP inserts are shown in green. Inset: detailed view of motor’s attempts to cross the neutral insert. All experiments were conducted at 3 mM ATP and a constant force of 5 pN. Traces were offset vertically to line-up the pause-like regions. Phosphate and MeP groups are represented as blue and red circles respectively.DOI: http://dx.doi.org/10.7554/eLife.09224.003

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** We performed control experiments in 'passive mode' where the optical trap position is fixed. As SpoIIIE translocates the DNA tether, it pulls the bead away from the trap, causing the tension in the DNA to increase. Upon reaching a certain force, SpoIIIE loses its grip on DNA and slips (red arrows), then resumes translocation from zero force. The fact that each slip occurs in a single, nearly instantaneous step indicates that a single SpoIIIE ring is translocating the DNA. Unfiltered 1-kHz data is shown.DOI: http://dx.doi.org/10.7554/eLife.09224.004

## SpoIIIE makes critical contacts with the DNA phosphate backbone during translocation

Modified inserts such as ssDNA, dsDNA with interstrand cross-links, dsDNA with abasic sites, and so on, have been previously used in single-molecule experiments to probe how dsDNA translocases interact with their nucleic-acid track (Aathavan et al., 2009; Stanley et al., 2006). To investigate how SpoIIIE interacts with its substrate, we designed DNA constructs containing a modified insert with a methyl-phosphonate (MeP) backbone (Figure 1b), which preserves the base pairing and overall structure of B-form DNA (Strauss and Maher, 1994). We first monitored SpoIIIE translocation along a substrate containing a 30-bp double-stranded MeP (dsMeP) insert, several times longer than the expected step size of the motor. Upon reaching the insert, SpoIIIE undergoes multiple slips followed by translocation recoveries (Figure 1b inset), revealing that it makes several attempts to cross the neutral segment. Despite these attempts, SpoIIIE failed to traverse the 30-bp dsMeP segment (Figure 1b), indicating that motor interactions with the negatively charged phosphates are critical for translocation.

Depending on the step size of the motor, and the manner in which it interacts with the DNA, the motor should be able to easily traverse short dsMeP inserts up to some critical length. To determine this length, we designed dsMeP inserts of varying size and recorded the motor’s ability to cross each insert (

![Figure 2.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig2-v3.jpg)

**Figure 2.:** (a) Sample traces of SpoIIIE translocating on DNA with dsMeP inserts of 2 bp (blue), 3 bp (green), 4 bp (magenta), and 5 bp (black). (b) Traversal probability for dsMeP inserts of various length. Note the sharp decrease in traversal probability between 4-bp and 5-bp inserts. Error-bars represent the 68% CI estimated via bootstrapping. (c) Mean traversal time for dsMeP inserts of various length. Note the large increase in traversal time between 4-bp and 5-bp inserts. Error-bars represent the SEM. P values calculated with a two-tailed Fisher exact test.DOI: http://dx.doi.org/10.7554/eLife.09224.005

Note that in rare instances (1 out of 32 molecules, Table 1), SpoIIIE managed to traverse the 30-bp dsMeP insert, albeit after several seconds of repeated crossing attempts (Figure 1b). A slightly higher traversal probability (∼8%) was recorded for the 10-bp dsMeP insert (Figure 2b). The dynamics of slipping and re-translocation (Figure 1b, inset) at the neutral insert and the lengthy traversal times for dsMeP inserts of 5 bp or longer (Figure 2c) suggest that, given a sufficient number of traversal attempts, SpoIIIE can cross even relatively long stretches of dsMeP (10–30 bp). The drop in traversal probability for longer dsMeP inserts suggests that the motor can hold onto MeP DNA for a short amount of time during which it can either step forward, or lose its grip on the neutral DNA. In other words, forward translocation along the MeP insert is in kinetic competition with backward slipping (Aathavan et al., 2009). As a result, to traverse longer MeP inserts, the motor must execute a correspondingly larger number of consecutive productive power-strokes. We hypothesize that other types of motor–DNA interactions (e.g. steric) enable the motor to traverse the neutral insert given an arbitrarily large number of crossing attempts. In support of this idea, the φ29 ring ATPase has been shown to require electrostatic contacts with the DNA every 10 phosphates, but relies on steric, non-specific interactions to exert force and translocate the DNA in-between those electrostatic contacts (Aathavan et al., 2009).10.7554/eLife.09224.006Table 1.MeP traversal statistics. DOI: http://dx.doi.org/10.7554/eLife.09224.006DNA constructSuccessful crossingsFailed crossingsTotal tracesssMeP modification30 base 3'→5' MeP2312430 base 5'→3' MeP62228dsMeP Modification2 bp dsMeP211223 bp dsMeP160164 bp dsMeP213245 bp dsMeP1313267 bp dsMeP391210 bp dsMeP1192030 bp dsMeP13132Length of MeP Probe Segment*4 bp dsMeP probe716233 bp dsMeP probe916252 bp dsMeP probe618241 bp dsMeP probe33437All MeP data was gathered under 5 pN of opposing force and [ATP] = 3 mM*All MeP probe segments carry a 4 bp dsMeP modification upstream of the probe

## SpoIIIE tracks the 5’→3’ strand in the direction of translocation

To determine whether SpoIIIE tracks the phosphate backbone of one or both DNA strands, we repeated the above experiment with 30-base inserts where phosphates on either strand were selectively neutralized. 23 out of 24 SpoIIIE molecules traversed the insert containing MeP on the 3'→5' strand in the direction of translocation (

![Figure 3.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig3-v3.jpg)

**Figure 3.:** (a) Sample traces of SpoIIIE translocating on DNA with 30 bp of neutral DNA on either the 3’-5’ strand (orange traces) or the 5’-3’ strand (magenta traces) in the direction of translocation. (b) Cartoon illustrating a hypothetical sequential model in which the DNA backbone is handed off between adjacent subunits within a hexameric ring. For clarity only one strand of dsDNA is shown. A highlighted backbone phosphate (yellow) is in contact with a motor subunit (magenta). In general, the motor step size in such a model can be anything less than 10 bp. Here we illustrate the model using a 2-bp step size. After one motor subunit (magenta) executes its power-stroke, the helical backbone of the dsDNA’s will be shifted, positioning the phosphate backbone in close proximity to the next subunit poised to fire. (c) Cartoon illustrating a hypothetical model in which a 10-bp burst enables a hexameric ring ATPase to maintain phosphate contacts on the same DNA strand. Initially, a single subunit (magenta) is contacting the phosphate backbone (yellow). After a 10 bp burst, the motor has traversed nearly a full helical turn on dsDNA, bringing the phosphate backbone back in register with the same ATPase subunit.DOI: http://dx.doi.org/10.7554/eLife.09224.007

## Strand tracking favors a sequential ATP hydrolysis model for SpoIIIE

The observation that SpoIIIE tracks only one of the DNA strands imposes geometric constraints on how the DNA is handed off from subunit to subunit during translocation. Strand-tracking is inconsistent with a stochastic coordination mechanism in which the six ATPase subunits execute their power-strokes at random. In such a mechanism, the subunit poised to fire is unlikely to be aligned with the tracked strand and will therefore not engage the DNA substrate. Since the DNA is held under constant tension in our experiments, a stochastically coordinated ATPase ring is expected to slip frequently, contrary to our observations.

Two possible scenarios are consistent with strand–tracking: (i) Subunits hydrolyze ATP and execute their power-strokes sequentially around the ring, such that after every power-stroke the subunit scheduled to fire next is properly aligned to interact with the phosphate backbone of the tracked strand (Figure 3b). In this scenario, the SpoIIIE subunits would fire consecutively (subunit 1 fires, followed by subunit 2, followed by subunit 3, etc). After subunit 1 executes its power-stroke, the helical geometry of the DNA will position the phosphate backbone of the tracked strand in close proximity to subunit 2, depending on the step size of the motor (Massey et al., 2006; Strick and Quessada-Vial, 2006). Thus, motor-DNA contacts would proceed from one subunit to the next in an ordinal fashion. (ii) The motor translocates DNA in increments of 10–11 bp, which closely matches the helical periodicity of dsDNA (10.4–10.5 bp/pitch). This mechanism would ensure that after each translocation event, the motor contacts the same strand after traversing one full helical turn along the DNA (Figure 3c). Such a mechanism is employed by the φ29 ring ATPase, which translocates DNA in 10-bp bursts and contacts the DNA backbone on the same strand every 10 base pairs (Aathavan et al., 2009).

The data presented above indicate that SpoIIIE makes periodic contacts with the same DNA strand every five base pairs or less and are consistent only with the sequential ATP hydrolysis mechanism outlined in scenario (i).

## MeP stepping stone constructs suggest that SpoIIIE has a step size of 2 bp

In order to rationalize how SpoIIIE easily traverses 4 bp of neutral DNA, but has difficulty crossing 5 bp of neutral DNA (

![Figure 4.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig4-v3.jpg)

**Figure 4.:** (a) Cartoon illustrating the sequential firing of subunits A–F of SpoIIIE as it approaches a 4 bp insert of dsMeP. (b) Possible translocation models (i–v) depicting the interaction between SpoIIIE subunits (A–F) and DNA; in all models subunits fire in a sequential order (A→B→C→D→E→F→A etc). For clarity, we show only the backbone the DNA strand tracked by SpoIIIE. Phosphate and MeP groups are shown in blue and red, respectively. A solid line connecting a SpoIIIE subunit to the backbone represents a stable electrostatic interaction; a dashed line represents a disrupted interaction.DOI: http://dx.doi.org/10.7554/eLife.09224.008

Five models (Figure 4b i–v ) are consistent with the results of the dsMeP experiments (Figure 2) and satisfy the conditions listed above: (i) At any time, only one subunit contacts one phosphate on DNA (Figure 4b i); this model requires a 5-bp step size to cross a 4-bp MeP insert. (ii) Only one subunit contacts two adjacent DNA phosphates at any time (Figure 4b ii); this model requires a 4-bp step size to clear a 4-bp MeP insert. (iii) At any time, two neighboring subunits each contact one DNA phosphate; this model requires a 3-bp step size to clear a 4-bp MeP insert (Figure 4b iii). (iv) At any time, two neighboring subunits each contact two adjacent DNA phosphates; this model requires a 2-bp step size to cross a 4-bp MeP insert (Figure 4b iv). We disfavor models where SpoIIIE subunit simultaneously contact more than two consecutive phosphate groups on the DNA backbone, and models where three or more consecutive subunits contact the DNA backbone because such models would require large motor/DNA distortions. Finally, we also considered a translocation model similar to the mechanisms proposed for the E1 and Rho helicases (Enemark and Joshua-Tor, 2006; Thomsen and Berger, 2009), (v) at any time five subunits contact five consecutive DNA phosphates; this model requires a 1-bp step size to cross a 4-bp insert (Figure 4b v). Although this E1/Rho-like model requires significant motor/DNA distortions (5 SpoIIIE subunits span an arc of 300° while five consecutive phosphates in dsDNA span an arc of ∼170°), it is in principle consistent with the data from Figure 2.

While we cannot rule out more complex models that may involve non-consecutive subunits simultaneously contacting the DNA, or stochastic bursts consisting of multiple, rapid consecutive steps (Cordova et al., 2014; Sen et al., 2013), we favor the more parsimonious models presented here.

To distinguish among the models proposed above and to determine SpoIIIE’s step size, we challenged the motor with inserts containing a 4-bp MeP segment ('register'), followed by 1 bp of regular DNA ('stepping-stone') that is in turn followed by a variable-length MeP segment ('probe') of 1–4 bp (

![Figure 5.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig5-v3.jpg)

**Figure 5.:** (a) The design of 'stepping-stone' constructs. Each insert consists of a register segment with 4 bp of neutral DNA, followed by one regular DNA base ('stepping-stone'), and a probe segment with x bp of neutral DNA. For clarity, only the DNA strand tracked by SpoIIIE is shown. (b) Diagrams illustrating the longest probe segment that can be traversed by the models depicted in Figure 4b. Model (i) should traverse a probe segment of at most 4 bp, whereas model (v) cannot traverse even a probe of 1 bp. (c) Sample traces of SpoIIIE translocating on DNA with 'stepping-stone' inserts containing a 1-bp probe (orange) or a 2-bp probe (magenta). (d) Traversal probability for stepping-stone constructs with various probe lengths. Error-bars show the 68% CI estimated via bootstrapping. p values were calculated using a two-tailed Fisher exact test. (e) Diagram illustrating how model (iv) can successfully traverse a 'stepping-stone' insert with a probe of 1 bp. The star marks the subunit executing the power-stroke. Once a subunit fires, it cannot fire again (gray shading) and must eventually disengage from the DNA (subunit shown as making no interactions with DNA). (f) Diagram showing why model (iv) fails to cross a 'stepping-stone' insert with a probe of 2 bp.DOI: http://dx.doi.org/10.7554/eLife.09224.009

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** Diagram illustrating two different scenarios of how the E1/Rho-like translocation model would cope with a MeP stepping stone insert. In this model subunits fire in a well-defined sequential order (firing subunit denoted by the yellow star) and move by 1 bp on DNA, whereas the remaining subunits escort the DNA during the translocation process. If the ATPase subunits have to fire in a strictly sequential order, a subunit cannot fire multiple consecutive times, or fire out of order, and is grayed out after firing. A motor operating via a strictly sequential E1/Rho-like translocation mechanism is not capable of crossing a MeP stepping stone insert with a 1-bp probe (frame 8), contrary to our observations (Figure 5c–d). If the same ATPase subunit could fire out of order several times in a row, the motor should traverse a MeP stepping stone insert with a 4-bp probe (inset), again inconsistent with our findings (Figure 5c–d).DOI: http://dx.doi.org/10.7554/eLife.09224.010

Figure 5e illustrates how model iv enables SpoIIIE to cross the insert with a 1-bp probe. The first three frames illustrate the sequential firing of subunits A, B, and C, all of which maintain at least one anchoring contact with the phosphate backbone. Because subunit D cannot make electrostatic contacts with the backbone, it fails to propel the DNA upon firing (Figure 5e, frame 5). As a result, no other subunit can establish new contacts with the DNA backbone. After subunit E translocates the DNA by 2 bp, subunit F can now latch onto a negatively charged phosphate and continue to translocate DNA. Figure 5f illustrates how this model copes with a 2-bp MeP probe: subunit F cannot anchor itself onto the DNA, causing the motor to pause and eventually slip (as shown in Figure 5c, magenta traces). This two-subunit DNA escort model requires one subunit to execute the power stroke while an adjacent subunit maintains its phosphate contacts during this power-stroke, escorting the DNA through the ring. In this model, the ATPase subunits translocate the DNA sequentially around the ring in a highly coordinated fashion that enables SpoIIIE to track one DNA strand. There is increasing structural evidence for this type of motor mechanism involving 'translocating' subunits and 'escorting' subunits; examples include the E.coli’s Rho helicase (Thomsen and Berger, 2009) and the papillomavirus E1 helicase (Enemark and Joshua-Tor, 2006). However, unlike the E1/Rho mechanisms, which employ four escorting subunits, the SpoIIIE translocation model proposed here requires only one escorting subunit.

## Nucleotides stabilize the SpoIIIE-DNA interactions

To quantify the strength of the motor–DNA interaction, we measured the force at which SpoIIIE loses its grip on DNA. In a buffer lacking nucleotides, SpoIIIE could bind to DNA and form tethers between the trapped bead and the micropipette-held bead. Manual pulling experiments revealed that these tethers rupture at ∼3 pN (Figure 7—figure supplement 1, apo), suggesting that apo-SpoIIIE does not interact strongly with DNA. In buffers containing only ADP or ATPγS, SpoIIIE could bind to DNA, forming tethers that rupture at ∼15 and ∼25 pN, respectively (Figure 7—figure supplement 1). These results indicate that nucleotides stabilize motor–DNA interactions and suggest that only nucleotide-bound subunits are capable of forming stable electrostatic contacts with the DNA phosphate backbone.

## The SpoIIIE ring can operate with non-consecutive inactive subunits

To further investigate how individual SpoIIIE subunits coordinate their ATP hydrolysis activity, we monitored DNA translocation in a saturating [ATP] buffer that contained ATPγS – a nucleotide analog that is hydrolyzed very slowly. Structural studies of FtsK indicate that ATPγS binds to the same catalytic pocket as ATP (

![Figure 6.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig6-v3.jpg)

**Figure 6.:** (a) Sample SpoIIIE traces acquired at different [ATPγS] and 3mM ATP. Pauses are highlighted in red. (b) Mean duration of the ATPγS-induced pauses extracted from fitting the pause duration distribution to an exponential. Error-bars represent the 95% CI of the fit. Insert: histogram of pause durations at 750 μM ATPγS and 3 mM ATP and the exponential fit to this distribution. (c) The density of ATPγS-induced pauses at various [ATPγS] and 3mM ATP. Error-bars represent the SEM. (d) Pause density versus [ATPγS] corrected to account for missed pauses (black symbols). Error-bars represent the SEM. The shaded regions illustrate the predictions for a sequential hydrolysis model where SpoIIIE pauses when n consecutive subunits are bound to ATPγS.DOI: http://dx.doi.org/10.7554/eLife.09224.011

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** (a) Pause-free velocity versus opposing force for various [ATPγS] and 3mM ATP. Error-bars represent the SEM. (b) Degree of pause-free velocity inhibition i = 1-v ([ATPγS])/v versus [ATPγS] at 3 mM [ATP] and 5 pN of opposing force. The dashed curve represents the fit to the competitive inhibition model (inset) with maxK µM. (i = 124 ± 20c) Pause-free velocity versus opposing force at 3 mM [ATP] in the absence of any nucleotide analogs (black), in the presence 500 µM [ATPγS] (green), or in the presence of 500 µM [AMP-PNP] (pink). Error bars represent the SEM. (d) Pause density measured at 3 mM [ATP] and various [ATPγS] (blue symbols). Experiments were also performed with 3 mM [ATP] and 0.5 mM [AMP-PNP] (red symbol). Error bars represent the SEM. (e) Pause density versus opposing force at 3 mM [ATP] and 1 mM [ATPγS]. (f) Mean lifetime of ATPγS-induced pauses calculated from single-exponential fits to the pause duration distribution at 3 mM [ATP] and 1 mM [ATPγS]. Error bars represent the 95% CI of the fits.DOI: http://dx.doi.org/10.7554/eLife.09224.012

To determine how many analog-bound subunits are required to arrest DNA translocation, we measured the density and duration of ATPγS-induced pauses as a function of [ATPγS]. The density and duration of analog-induced pauses does not depend on external force (Figure 6—figure supplement 1e–f), consequently pauses detected at all forces were pooled together. Given the spatio-temporal resolution of our experiments, we could reliably detect pauses longer than 30 ms at 125 –250 μM ATPγS, 50 ms at 375–500 μM ATPγS, and 75 ms at 750–1000 μM ATPγS. However, regardless of the shortest detectable pause duration and the ATPγS concentration, the distribution of measured pause durations was well described by a single exponential decay (Figure 6b, inset) with the same characteristic life-time of ∼35 ms (Figure 6b). The fact that the characteristic life-time does not depend on ATPγS concentration suggests that all analog-induced pauses are drawn from the same distribution. Furthermore, the single-exponential dependence of the pause duration distribution indicates that the exit from the paused state is governed by a single rate-limiting event—presumably the exchange of an ATPγS molecule with one ATP which is present in saturating concentrations, as proposed for other ring ATPases (Chistol et al., 2012; Sen et al., 2013). Despite the fact that we cannot detect analog-induced pauses shorter than a certain cutoff (30–75 ms), we can estimate the number of missed pauses—and therefore the true pause density—from the measured pause density (Figure 6c) and the characteristic life-time derived from the pause distribution (Figure 6b), assuming that the single-exponential distribution holds for pauses shorter than the cutoff (Hodges et al., 2009) (see 'Materials and methods').

The MeP experiments support a sequential nucleotide hydrolysis model. Therefore, to explain the density of ATPγS-induced pauses, we considered a sequentially coordinated hexameric ATPase ring that pauses whenever n consecutive subunits are bound to ATPγS (1 ≤ n ≤6). The pause density (PD) can be analytically expressed in terms of the motor’s pause-free velocity (vpf), the ATPγS dissociation rate (koff), and the probability that the motor is paused (Ppause)—which is proportional to the concentrations and dissociation constants of ATP and ATPγS (Materials and methods), as follows:

PD = koffvpf·Ppause(1- PPause)

Figure 6d shows the expected pause density predicted for different n values. For example, n=1 (green shaded region) corresponds to a sequentially coordinated ring that pauses whenever a single subunit is bound to ATPγS; n=2 (blue shaded region) corresponds to a sequentially coordinated ring that pauses when two consecutive subunits are both bound to ATPγS, and so on. The ATPγS pause-density data corrected to account for missed pauses (Figure 6d black symbols) are best described by the model in which two (n=2) consecutive analog-bound subunits are required to induce a pause in the motor (Figure 6d, blue-shaded region). In other words, analysis of the pause density indicates that the motor can operate processively with non-consecutive inactive subunits but not with two or more consecutive subunits. This conclusion is further supported by the observation that FtsK hexamers readily bypass individual catalytically inactive ATPase subunits (Crozat et al., 2010).

## Discussion

## Secondary motor-DNA interactions

We have shown that SpoIIIE translocates DNA by making crucial anchoring contacts with the negatively charged phosphate groups on one DNA strand. Although electrostatic interactions with the backbone of the 5’→3’ strand in the direction of translocation are the principal mode of motor-substrate contact, we surmise that other types of interactions (e.g. steric) play a secondary role in maintaining SpoIIIE’s grip on DNA. This inference explains why we observe small but non-zero traversal probabilities for neutral inserts of 10–30 bp, much longer than the expected motor step size (Figure 2b). Interestingly, SpoIIIE is more likely to traverse 30-bp inserts with a neutral backbone only on the 5’→3’ strand (6 out of 28 molecules) than 30-bp inserts with a neutral backbone on both strands (1 out of 32 molecules) (Table 1). To explain this discrepancy, we speculate that during translocation, in addition to the essential electrostatic interactions with the 5’→3’ strand, the SpoIIIE ring may also interact very weakly with charges on the 3'→5' strand. These secondary interactions could be mediated by parts of the motor other than the pore loops which execute the power – stroke.

## MeP is not expected to cause significant DNA distortions

Prior experiments on MeP DNA have established that certain patterns of neutral and charged bases can introduce large DNA distortions. An asymmetric neutralization of the phosphate backbone whereby one 'face' of the dsDNA helix had its charges removed (e.g. neutralizing bases 1-3 on one strand and bases 3-6 on the other strand) results in DNA bending toward the direction of the neutralized region (Strauss and Maher, 1994). However, a symmetric neutralization of the phosphate backbone, whereby the phosphates on both strands were uniformly neutralized, resulted in no significant DNA distortions (Strauss and Maher, 1994).

We do not expect the MeP DNA constructs used in this study to introduce significant distortions on the double helix for two reasons: (1) Magnesium ions were present in the experimental buffer at a sufficiently high concentration (10 mM), which had been demonstrated to mitigate the effect of DNA distortions due to asymmetric phosphate neutralization (Strauss and Maher, 1994). (2) In designing the MeP inserts used in this study, care was taken to avoid an asymmetric neutralization of the phosphate backbone. The majority of the experiments with MeP inserts tested in this study utilized dsMeP modifications. Thus, the backbone neutralization was symmetrically distributed and therefore not expected to cause significant DNA distortions. We tested only two single-stranded MeP/DNA hybrid constructs, with 30 consecutive neutralized bases on either strand, covering nearly three full helical turns of the DNA. Because the backbone neutralization was distributed evenly in all directions around the DNA helix, the charge neutralization should be symmetrical, and therefore, it is not expected to introduce significant DNA distortions.

## DNA translocation model

To rationalize the results of the MeP experiments, we propose a minimal translocation model in which SpoIIIE subunits fire sequentially around the ring, each subunit translocates 2 bp of DNA per power-stroke, at least two consecutive ATPase subunits contact the backbone of one DNA strand, and each subunit contacts two consecutive backbone phosphates. To be consistent with the results of the stepping-stone insert experiments (Figure 5c–d), our two-subunit translocation-escort model requires that subunits fire in a well- defined sequential fashion (A, B, C, D, E, F, A, B, C etc) and a subunit cannot fire multiple times in a row or out of order.

## SpoIIIE does not employ the E1/Rho-like translocation model

The structures of homo-hexameric helicases E1 and Rho co-crystallized with their single-stranded nucleic acid substrates strongly support a translocation mechanism where five motor subunits contact five consecutive phosphates on the ssDNA/ssRNA backbone (Enemark and Joshua-Tor, 2006; Thomsen and Berger, 2009), and the hydrolysis of one ATP is coupled to the translocation of one nucleotide. Although an E1/Rho-like mechanism could potentially rationalize how SpoIIIE easily traverses a dsMeP insert of 4 bp but not 5 bp (Figure 2), such a model predicts that the motor would fail to traverse a stepping-stone construct with a 1-bp MeP probe (Figure 5b v). Even if the E1/Rho-like model did allow a subunit to fire several times in a row, such a model would still be inconsistent with the stepping stone data (Figure 5—figure supplement 1).

## Strand-tracking in a dsDNA translocase

It was previously reported that SpoIIIE supercoils plasmid DNA in vitro, and strand/groove-tracking was proposed to explain this observation (Bath et al., 2000). Magnetic tweezers measurements of DNA supercoiling during translocation ruled out a groove-tracking mechanism for FtsK (Saleh et al., 2005). Here, we show that SpoIIIE does indeed track one DNA strand by making specific electrostatic contacts with backbone phosphates on the 5'→3' strand in the direction of translocation, a feature reported for other RecA-like NTPases: the φ29 packaging motor, DnaB, and Rho (Aathavan et al., 2009; Itsathitphaisarn et al., 2012; Thomsen and Berger, 2009). Unlike the φ29 ATPase, which translocates dsDNA, DnaB, and Rho are single-stranded nucleic acid translocases, and therefore track one strand by default. Interestingly, both SpoIIIE and the φ29 ATPase encircle dsDNA, positioning multiple subunits in close proximity to the dsDNA helix, while they still possess the ability to discriminate one strand from the other. How these dsDNA translocases achieve strand discrimination remains unclear.

Several studies have demonstrated that certain skewed sequences (i.e. sequences whose presence is biased on the leading vs. the lagging strand) impart directionality to FtsK/SpoIIIE translocation (Besprozvannaya et al., 2013; Cattoni et al., 2013; Lee et al., 2012; Levy et al., 2005; Löwe et al., 2008). It is tempting to imagine that the strand tracking mechanism presented here could be used by SpoIIIE to read these skewed sequences (i.e. the SpoIIIE Recognition Sequences, SRS). However, the γ domains of SpoIIIE have been shown to be required for reading the SRS (Ptacin et al., 2008) and co-crystal structures of dsDNA with the domain γ reveals it interacting with both DNA strands at the backbone, the major and minor grooves, and individual bases (Löwe et al., 2008). We consider it unlikely therefore, that SpoIIIE enlists the strand-tracking mechanism described here for SRS sequence recognition.

## The motor-DNA symmetry mismatch should give rise to DNA supercoiling

The electrostatic interactions between SpoIIIE and the DNA backbone are likely to have two main purposes

![Figure 7.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig7-v3.jpg)

**Figure 7.:** (a) Diagram illustrating how SpoIIIE supercoils DNA while tracking the phosphate backbone of one DNA strand. Neighboring subunits in the SpoIIIE hexamer are spaced by 60°; consecutive DNA phosphates are spaced by ∼34°; and the backbone contacts of two adjacent subunits are separated by ∼69°. After a 2-bp translocation step, a 9-degree counter-clockwise rotation of the DNA relative to the motor is needed to align the next translocating subunit and the nearest pair of backbone phosphates. (b) Diagram of the SpoIIIE hexamer illustrating how the two-subunit DNA escort model enables the motor to bypass an ATPγS-bound subunit (red). For simplicity, only one DNA strand is shown (orange). DNA is translocated out of the page, and each subunit interacts with two neighboring phosphates. The star marks the subunit slated to execute the power-stroke.DOI: http://dx.doi.org/10.7554/eLife.09224.013

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/09224/elife-09224-fig7-figsupp1-v3.jpg)

**Figure 7—figure supplement 1.:** To probe the strength of the motor-DNA interaction in the presence of different nucleotides, we pulled on single SpoIIIE-DNA complexes in a nucleotide-free buffer (Apo state, green), 1mM [ATPγS] (cyan), and 1mM [ADP] (orange) and measured the mean pull force, that is, the average force at which the tether ruptured. Error bars represent the SEM.DOI: http://dx.doi.org/10.7554/eLife.09224.014

In vivo measurements indicate that, during B. subtilis sporulation, the DNA is negatively supercoiled by 1 turn per 97 ± 6 bp in the forespore and 1 turn per 140 ± 10 bp in the mother cell (Nicholson and Setlow, 1990). Since SpoIIIE is anchored at the septum during sporulation and the B. subtilis DNA is circular, the two-subunit escort model predicts that SpoIIIE translocation should introduce one negative supercoil in the forespore and one positive supercoil in the mother cell for every ∼80 bp translocated. We surmise that the SpoIIIE mechanism is fine tuned to deliver DNA to the forespore in the appropriate negative supercoiled state, similar to what has been proposed for FtsK (Saleh et al., 2005). This mechanism may help to conserve cellular resources by minimizing the amount of maintenance performed by topoisomerases/gyrases, a strategy that may provide a significant advantage in the harsh conditions that prompt sporulation (i.e., starvation).

## SpoIIIE/FtsK rings can tolerate non-consecutive inactive subunits

The results of ATPγS experiments suggest that SpoIIIE can processively translocate DNA with non-consecutive inactive subunits. This conclusion can be rationalized by the two-subunit DNA escort model proposed above: having two adjacent ATPase subunits simultaneously contact the DNA enables the motor to continue translocating if either of the two subunits is inactive, but not when both are disabled. Figure 7b illustrates how the two-subunit DNA escort model can bypass the ATPγS-bound subunit B: (i) subunit A fires and translocates DNA while subunit B escorts the DNA, (ii) the analog-bound subunit B fails to fire while subunit C was poised to escort the DNA (iii) subunit C then fires and translocates the DNA, handing it over to subunit D. During this step, subunit B, which remains bound to ATPγS, escorts the DNA for subunit C.

Our conclusions agree with the results of a single-molecule study by Crozat et al., which found that FtsK hexamers with two diametrically opposed inactive subunits translocated DNA as fast as wildtype hexamers (Crozat et al., 2010). The authors of that study proposed a sequential DNA escort mechanism in which at least three motor subunits contact the DNA at any given time. The ATPγS experiments presented here provide additional evidence that SpoIIIE/FtsK motors can bypass individual inactive subunits. Moreover, the strand-tracking behavior reported here for SpoIIIE strongly favors a model in which ring subunits fire sequentially, a key aspect of the DNA escort mechanism proposed here and in the Crozat et al study.

This study presents evidence for a type of inter-subunit coordination in ASCE ring NTPases where subunit firing is highly coordinated around the ring, yet the motor possesses sufficient flexibility to bypass non-consecutive inactive subunits. How is this mechanism optimized for the specific biological task of SpoIIIE? In vivo, SpoIIIE is present in low copy numbers during sporulation, with only two motors responsible for the vital task of chromosome translocation at any given time (Burton et al., 2007; Yen Shin et al., 2015). As a result, each SpoIIIE ring functions as a single-molecule bottleneck for this process, where the failure of either motor is likely to be lethal for the cell. The coordination mechanism proposed here can potentially explain how B. subtilis safeguards against the failure of individual motor subunits during sporulation. We speculate that other ASCE motors that also represent single-points of failure may have evolved into similar flexible operations.

## Materials and methods

## Sample preparation

Biotinylated SpoIIIE constructs were generated by ligating the biotin tag sequence from plasmid Pinpoint Xa-1 (Promega, Madison, WI) to the N terminus of SpoIIIE from plasmid pJB103 (Bath et al., 2000). Protein purification was conducted as described previously with the addition of 2 µM biotin in the liquid cultures (Ptacin et al., 2008). DNA tethers were generated using a 5' biotinylated primer (IDT) to PCR amplify a 21 kb region of lambda phage DNA (NEB) and gel extracted. DNA oligos containing MeP inserts (Gene Link or TriLink BioTechnologies) were ligated to gel-purified DNA fragments: a 9167-bp fragment with the ACT 3'-overhang (amplified from λ DNA and digested with AlwNI), and a biotinylated 3976-bp fragment with the GAA 3'-overhang (amplified from φ29 DNA and digested with BglI). The final ligation product was gel-purified using the QIAEX II kit (Qiagen).

## Optical tweezers experiments

In this study, 2.1 µm streptavidin beads (Spherotech) were blocked for 30 min in 50 mM Tris–HCl pH 7.5, 10 mM MgCl2, 4% bovine serum albumin (BSA), w/v and 0.1% Tween-20. Then ∼1 pmol of biotinylated SpoIIIE and ∼1 ng of biotinylated DNA were incubated separately onto streptavidin beads and spatially separated in the fluidics chamber. DNA-bound beads and SpoIIIE-bound beads were brought in close proximity to allow SpoIIIE to engage the DNA. DNA translocation was conducted in a reaction buffer containing 50 mM Tris–HCl pH 7.5, 10 mM MgCl2, and 3 mM ATP.

## Data analysis

Pauses were detected using a modified Schwartz Information Criterion (mSIC) method (Chistol et al., 2012). The number and duration of pauses missed by this algorithm were inferred by fitting the pause durations to a single exponential with a maximum likelihood estimator. After removing the detected pauses, the translocation velocity was computed by fitting the data to a straight line. Force-velocity data (Figure 6—figure supplement 1a) was gathered in 'passive-mode' (Smith et al., 2001), where the optical trap position is fixed. Single-molecule trajectories were partitioned into segments spanning 2–3 pN, and the velocity was computed for each segment. Tether tension and extension were converted to contour length using the Worm-Like-Chain approximation with persistence length p=30 nm, and stretch modulus S = 1200 pN·nm (Baumann et al., 1997).

## Estimating the number and duration of missed pauses

The pause-detection algorithm can detect only pauses longer than tc, but it is possible to account for the duration and number of pauses missed by the algorithm. We observe that pauses are drawn from a single-exponential distribution P(t) with a mean pause-duration t.

(1)P(t)=A·e−tτ

The number of all pauses (Nall), the number of detected pauses (Ndet), and the number of missed pauses (Nmiss) are given below.

(2)Nall=∫0∞ P(t)· dt=∫0∞A· e−tτ· dt

(3)Ndet=∫tc∞ A· e−tτ· dt

(4)Nmiss=∫0tc A· e−tτ· dt

The duration of all pauses (Tall)

(5)Tall=∫0∞ t· P(t)· dt=∫0∞ t· A· e−tτ· dt

The duration of detected pauses is Tdet:

(6)Tdet=∫tc∞t· A· e−tτ· dt

The duration of missed pauses:

(7)Tmiss=∫0tct· A· e−tτ· dt

Given the number of detected pauses and the mean pause duration calculated by fitting the pause distribution to a single-exponential, it is possible to infer the number of total pauses and the number of missed pauses as follows:

(8)Nall=Ndet· etcτ

(9)Nmiss=Ndet· (etcτ−1)

If the pause-detection algorithm identifies and removes only pauses longer than tc, then the measured pause-free velocity (Vmeas) is given by the following expression:

(10)Vmeas = DTpf Tmiss

Here D is the total distance translocated by the motor, Tpf is the 'pause-free' time (i.e. only the time spent translocating DNA), and Tmiss is the total duration of missed pauses. The true pause-free velocity (Vpf) is given by the following expression:

(11)Vpf=DTpf=DDVmeas−∫0tct·A·e−tτ·dt

## Predicting the density of ATPγS-induced pauses

The probability of finding the ring in a pause state Ppause (i.e. the fraction of the time spent in the paused state) is:

(12)Ppause=τpτp  τx

where tp is the total time the motor spends in a pause state and tx is the total time the motor spends translocating DNA. The total pause time tp and the total translocation time tx can be expressed as

(13)τp=<T>·η=(1/koff)·η

(14)τx = x(t)vPF

where <T> is the average pause duration, η is the number of pauses, koff is a first-order dissociation rate of ATPγS from the ring, x (t) is distance translocated over time and vPF is the pause-free velocity expressed as:

(15)vPF = ∑i = 06pivi

where pi is the probability of the ring being bound to i ATPγS molecules and vi is the pause-free velocity of the ring bound to i ATPγS molecules. Substituting Equation 14 into Equation 12, we can express the pausing probability as:

(16)Ppause=η/x(t)η/x(t) + koff/vPF=PDPD +  koff/vPF

We define the pause density (the number of pauses per distance translocated) as PD =η / x (t). Thus, the PD can be expressed in terms of the pausing probability (Ppause), the ATPγS dissociation rate (koff), and the pause-free translocation velocity (vPF):

(17)PD=koffvPF·Ppause(1−Ppause)

The pausing probability (Ppause) can be expressed in terms of the probability that a single subunit is bound to ATPγS (p). p depends on the concentrations of ATP and ATPγS, as well as the dissociation constants (koff/kon) of ATP and ATPγS (KATP and KγS) for individual ATPase subunits (Sen et al., 2013):

(18)p=KATP[ATPγS]KγSKATP KγS[ATP] + KATP[ATPγS]

To calculate the expected pause probability, we used the measured Ki of ATPγS (124 ± 20 µM) for KγS (Figure 6—figure supplement 1b). For KATP, we used the measured Km of ATP (505 ± 50 µM) as an upper-bound estimate. For a sequential ordinal ATP binding/hydrolysis inter-subunit coordination model (i.e. subunit 1 binds ATP, hydrolyzes ATP, releases Pi and ADP, and executes the power-stroke, followed by subunit 2, then subunit 3, etc), the pausing probability is given by Ppause = pn, were n is the number of ATPγS molecules required to induce a pause.

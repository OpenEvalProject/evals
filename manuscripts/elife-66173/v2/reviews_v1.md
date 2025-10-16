# Peer review - Round 1

Editors:
- Denise Cai, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66173.sa1](https://doi.org/10.7554/eLife.66173.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Thank you for submitting your work on FED3, a new and improved open-source option for a home cage pellet dispensing device, to eLife. The reviewers agreed that this open-source tool would be of wide-interest to neuroscience laboratories, that the manuscript was well-written and clear, and that the cross-lab validation was informative. They also appreciated that this Tools and Resource manuscript documents all necessary open-source hardware, firmware, visualization code, and Arduino and Python libraries for user customization of experiments and analysis.

Decision letter after peer review:

Thank you for submitting your article "Feeding Experimentation Device version 3 (FED3): An open-source device for measuring food intake and operant behavior" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Daniel Aharoni (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1. Describe in more detail the current commercial and open-source methods there are for monitoring food intake and operant behavior in rodent home cages. How does FED3 compare to those designs?

2. With the exception of panel 2D, little is shown to quantify jam-rate, which is one if the biggest issues with any pellet dispenser. Do the authors have any other data to this end? The authors mention in Figure 5D there is a retrieval time metric. Do you also have a time between pellet dispense onset and when the pellet dispenser detects that the pellet has arrived onto the pedestal?

3. In relation to the point "FED3 also has a programmable output that can control other equipment, for example to trigger optogenetic stimulation after a nose-poke or pellet removal, or to synchronize feeding behavior with electrophysiological or fiber photometry recordings." Do the requirements of this function impede one of the major strengths of this technology: large scale testing in laboratory vivariums? I would suspect tethers / wires in the home cage would be a major limitation to this feature for around the clock testing. Upon closer readings in the methods section, the mice were removed from the home cage for this part of the experiment. Perhaps the authors could make that clearer earlier on and separate describing this feature from the home-cage functionality of the device in its description.

4. For combining with optogenetic stimulation in Figure 7, is the FED3 output a single pulse trigger that is driving a pre-programmed train driven by another high-fidelity stimulation device or is the voltage train of 20hz being driven by FED3 directly turning on the LED? On a related note, how is the precision of timestamp recording for the external device? How is time stamp fidelity maintained across the session? It would be helpful to better understand how your system was set up to relate the time stamps of the data being written to the SD card and how well-registered they were after the fact.

5. Is FED3 water resistant? If a cage were to flood as sometimes happens with displaced water bottle tops, how well does the FED3 housing protect the electronics of the device and the animal?

6. Clarification or corrections needed for analysis/methods/statistics:

• Figure 3 shows an N of 10 but the manuscript text mentions you used 11 mice. This seems like a discrepancy in the paper.

• In the multi-site study of learning rates with FED3 section, you say "This highlights how FED3 enables high throughput studies of operant behavior and also demonstrates the potential for false positive effects when comparing between groups with small sample sizes (Figure 5B)". I feel like your claim that this data shows the potential for false positive effects is unsupported as I don't think you show that the individual groups must be pulled from the same distribution.

• For Figure 4E, please describe how the poke efficiency metric was calculated.

• In Figure 5 c – f, it is unclear if the error bars are across mice or across groups.

• In Figure 5 e and f, the vertical axis units are labeled as (%) but the vertical axis numbers look to be off by 100 times.

• In Figure 7 c, I think this is a plot of the cumulative poke count and not a temporally binned poke count. It would be nice to clarify this in the text or vertical axis label.

• Figure 7D shows data across 3 mice but, unlike most of your other figures, does not show the individual data points for each mouse. It would be nice to add those to the plot. It might be also worth considering showing the data from all 3 mice in figure 7C.

# Peer review - Round 1

Editors:
- Louis J Ptáček, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62073.sa1](https://doi.org/10.7554/eLife.62073.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "A Sub-Minute Resolution Prediction of Brain Temperature Based on Sleep-Wake State in the Mouse" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Catherine Dulac as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Brain temperature is of neurobiological and clinical importance. The authors previously used a statistical approach to demonstrate that hourly brain-temperature values strongly co-varied with time-spent-awake, separate from locomotion. they now have developed a mathematical tool to simulate and predict mice cortical temperature based on the 4-second sleep-wake sequence. The model estimated temperature precisely with 91% of its variance based on three main factors: sleep-wake sequence, time-of-day (“circadian”), and a novel “prior wake prevalence”. With similar accuracy the model predicted temperature in a second, independent cohort using the parameters optimized for the first.

This manuscript tackles an important question of wake-sleep-dependent changes in brain temperature. The conventional view is that body temperature in mice is regulated by the circadian clock and it still often comes as a surprise to many that in fact the observed differences between day and night are primarily driven by the state of vigilance. The relationship between wakefulness and increased body temperature (or perhaps more correctly the relationship between sleep and hypothermia) has been established before, but the study of Sela et al. goes to great length to quantitatively describe the temperature dynamics. The authors conclude that model "can help differentiate thermoregulatory from sleep-wake driven effects".

Essential revisions:

1) First, how vigilance state and sleep-wake history affect the relationship between the brain and body temperature remains unclear. Very few laboratories monitor brain temperature routinely, and the circadian field relies almost entirely on skin or core body temperature recording. Clearly, the authors do not have access to such data in the data set they used, but it is essential to be discussed. Are they independent? If the time constants were different, it could provide important insights into the underlying mechanisms and also functional significance.

2) To this end, while the effects of vigilance states on temperature dynamics are nicely documented, the underlying causes or biological significance of the effects observed remain unclear. The authors mention that "Brain temperature affects many properties of neuronal functioning", but discussing some specific examples, illustrating which properties are actually influenced by changes within the temperature range investigated here, may help. Conversely, I am still not entirely clear what are the factors that actually drive the changes in brain temperature observed.

3) The observations made by the authors clearly apply to artificial laboratory conditions at a specific ambient temperature only, but it remains unclear how the vigilance state affects body/brain temperature at different ambient temperatures. Would you still observe vigilance-state specific changes in brain temperature if mice were kept at thermoneutrality? The authors optimise some specific parameters, such as "window length", "window shift" or "scaling factor", which helps to obtain a better fit, but then the question remains whether these would also work at different ambient temperatures, and what is their biological meaning.

4) Arguably, the actual temperature in the nest is higher than ambient temperature. Is the drop in temperature during sleep smaller when the animal sleeps in the nest?

5) Finally, what is the relationship between locomotor activity and brain temperature? Does it matter if the animal is involved in an intense exploratory or running behaviour vs. relatively quiet wakefulness? Would the model work just as well in both cases?

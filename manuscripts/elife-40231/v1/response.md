# Author response - Round 1

Authors:
- Byounghoon Kim ([ORCID: 0000-0001-7159-5134](https://orcid.org/0000-0001-7159-5134))
- Shobha Channabasappa Kenchappa
- Adhira Sunkara
- Ting-Yu Chang ([ORCID: 0000-0003-3964-0905](https://orcid.org/0000-0003-3964-0905))
- Lowell Thompson
- Raymond Doudlah
- Ari Rosenberg ([ORCID: 0000-0002-8606-2987](https://orcid.org/0000-0002-8606-2987))

## Response text

DOI: [10.7554/eLife.40231.019](https://doi.org/10.7554/eLife.40231.019)

Major concerns:

As you can see in the reviews below, the reviewers largely agree on these central recommendations:

1) Maximize the generality of the described tool/resource by demonstrating application to multiple diverse experimental settings and by providing information on how to customize the software for any of a range of applications. This could be achieved, for example, by briefly describing the application to the psychophysics experiments alluded to, and by collaborating with another lab to tailor the system to their acquisition/control needs in a very different (ideally non-vision) setting.

Based on the reviewers’ comments and a follow-up discussion with the editor, our revisions focus on demonstrating the generality of the REC-GUI framework using three distinct applications with humans, non-human primates, and rodents. The non-human primate application confirms the ability of the framework to accurately and precisely control external hardware under computationally demanding scenarios while achieving millisecond level precision. We added details of a human psychophysics application to show that the framework can coordinate experimental control based on multiple external device inputs. This application further shows that measurements made by multiple external devices can be saved and precisely aligned without external data acquisition systems. We added a passive avoidance task with mice to show how the framework can be used to automate behavioral training and assessment by transforming input device signals into control signals for external devices. Together, these three applications show generality across animal models, as well as experimental modalities (e.g., neural recordings during behavior, human psychophysics, and animal behavioral training and assessment).

We greatly expanded the user manual and supporting code. These provide detailed examples of coding structures used by the REC-GUI framework, including three ready-to-use scripts for implementing specific protocols: (i) a gaze fixation task (fixation.m), (ii) an eye calibration routine (calibration.m), and (iii) a receptive field mapping routine (receptive_field_mapping.m). The examples implement vision-related tasks, but the structures are applicable to a broad range of experiments, regardless of the sensory or motor modality investigated. For example, the eye calibration routine can be modified into a motor reach calibration routine with minimal effort. A main point of these examples is to illustrate how the GUI communicates with hardware and other software to implement tasks. We also include a basic template for implementing new protocols (start_coding.m), and code implementing a simple closed-loop task (start_coding_closedloop.m). In particular, the closed-loop task is a useful starting point for learning to use and customize the REC-GUI framework since it does not require specialized hardware or software (beyond Python and MATLAB).

We believe that these additions provide sufficient information to guide a wide range of customizations of the REC-GUI framework. We further emphasized that support will be provided through the REC-GUI forum (https://recgui2018.wixsite.com/rec-gui/forum) to cover any questions that may arise, and that the REC-GUI framework is an open-source project that will continue to evolve. We will routinely update the user manual based on developments and forum discussions. The user manual can be downloaded from the REC-GUI GitHub (https://github.com/rec-gui).

2) Describe the performance in more general terms (e.g. as is done in Figure 5), rather than in terms specific to the major use case for which it was developed. This also applies to the discussion, which is now very focused on software for monkey vision experiments.

We expanded the analyses quantifying system performance (Figure 5). Specifically, we characterize upper and lower bound estimates of performance when relying entirely on high-level programming environments to implement an experiment. We also provide specific test results from three applications using different system configurations to support studies with humans, non-human primates, and rodents.

To ensure that the testing results are relevant to experimentalists and readily interpretable, they were performed using specific applications. To increase the generality of the tests, we framed the motivations for them and the interpretation of the results in terms of broader experimental needs.

Within the Discussion, we expanded text regarding how the REC-GUI framework can be applied to a broad range of neuroscience questions ranging from in vitro experiments to closed-loop multisensory studies. In addition to other control systems previously discussed, we now discuss the Spike2 (CED, Inc.) system which is used in a wide range of applications.

3) Think through and describe the resources needed to support application of the software to other use cases. This includes a plan for maintenance of the software (e.g. via GitHub) as well as much more detailed supplementary instructions for modification and use.

The REC-GUI webpage (https://recgui2018.wixsite.com/rec-gui) hosts a discussion forum and contains links to essential downloads. In addition to the user manual, we indicate in the text that the forum is an important resource for customization. The added GitHub stores the user manual, software, and tracks versioning (https://github.com/rec-gui). Throughout the text, we provide examples of what would be needed for the framework to support applications that were not tested. These additions largely occur in the Materials and methods and Discussion sections. As discussed above, we expanded the user manual and included additional example code to further clarify modification and use.

4) Clearly state existing limitations to the generality. State what has and has not been tested and what is and is not possible with the existing software.

We have clarified limitations to the generality of the REC-GUI framework throughout the manuscript as they relate to hardware, software, and the types of experimental paradigms. For example, we emphasize that customization does require programming, but highlight that the necessary coding abilities are of the level expected of graduate students. We also reiterate that network interfacing is a requirement to integrate hardware or software with the framework. In the Discussion, we mention applications and extensions that have not been tested, and what would be required to implement them. We additionally discuss performance limitations, and how future developments can reduce those limitations (though in some cases, doing so would require more advanced programming abilities). We encourage contributions from the scientific community to further develop the generality and functionality of the framework.

5) Although the issue of novelty of the approach was raised by one of the reviewers, and this view is shared, it will likely not be helpful to try to rewrite the manuscript to stress the novelty. Taking steps to ensure the usefulness and then highlighting them will probably be more fruitful in terms of improving the manuscript.

Network-based parallel processing in and of itself is, of course, not novel. But the application of such a framework to provide experimental flexibility and high temporal precision while minimizing coding demands is unique. The unmet need for a system that jointly meets these competing goals is evident since there have been multiple previous attempts to develop such a system. However, existing alternatives have had limited success compared to the REC-GUI framework. We have further clarified this point and highlighted the usefulness of the framework in the Discussion.

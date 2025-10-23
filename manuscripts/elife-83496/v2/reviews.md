# Peer review - Round 1

Editors:
- Mathieu Wolff, https://ror.org/057qpr032 CNRS, University of Bordeaux France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83496.sa0](https://doi.org/10.7554/eLife.83496.sa0)

This paper provides the field with a new and important Python-based tool to assist neurosurgery both before and after a wide range of interventions. In its present form, the software comes as a convincing toolbox that may be helpful for researchers relying on neurosurgery in rodents (both mice and rats).


---

# Peer review - Round 1

Editors:
- Mathieu Wolff, https://ror.org/057qpr032 CNRS, University of Bordeaux France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83496.sa1](https://doi.org/10.7554/eLife.83496.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "TRACER: A toolkit to register and visualize anatomical coordinates in the rat brain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Mathieu Wolff as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by a Senior Editor.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

In short, all reviewers found the tool described of this study with a clear value but it really needs further polishing to be widely used within the neuroscience community. At present the installation process is by itself an obstacle for any user with only moderate familiarity with Python-based environment. So this would need to be considerably enhanced to consider a new examination of this tool. In addition a more thorough description of its specific value versus other tools already available including for rats is warranted to understand the added value that TRACER brings.

Reviewer #1 (Recommendations for the authors):

General comments:

It seems like a lot of work to go through all sections and match to the digital atlas. Incorporating matching between pre-processed images and reference sections seems crucial for widespread use of the tool. If this is something that cannot be done in short order, a widespread use of the tool may be limited.

More extensive comments should be made about Brainrender, which was published in eLife in March 2021. This tool is only mentioned and no extensive comparison with TRACER is made.

Software issues:

In evaluating the package (on a machine with Linux Mint 20 Cinnamon, version 4.6.7. Linux Kernel, 5.4.0-89-generic), there were issues with getting the atlas to load. It was an issue with an xcf library, so perhaps this is very specific to this setup, but perhaps is worth noting that some Linux users may have a similar issue.

More generally, there were issues with getting the latest atlas (v4) to work. An error was received that the process was "Killed" and then a message stating that the atlas v3 couldn't be found. Downloading atlas v3 resolved the issue.

It would be useful to know if this software allow for localization of microelectrode arrays? The paper states that TRACER can place trajectory of 6 probes for prediction or reconstruction, so does this mean it can only be used for single point trajectories (such as those from single shank electrodes, fiber optic cannula, or a drug infusion cannula)? A statement should be included about the utility of TRACER for array probes. (If it is not capable of mapping arrays, perhaps this is a modification to consider for the future).

The text in Figure 5 as a bit small and maybe the axis labels could also be shortened and bounding boxes removed.

Potential issue with tissue processing:

How was shrinkage dealt with in processing the brain tissue? Was any estimate done? This might matter for the specific experiment reported in the manuscript, which involved staining with several antibodies. This could also be a major issue for users, especially in cases where histochemical or immunohistochemical stains might be combined in a study.

Reviewer #2 (Recommendations for the authors):

Strengths

– The tool and user manual both appear excellent. The authors have put a lot of effort into making this tool.

– Prior tools were focused on mice, while this one is optimized for rat histology.

– The "surgery planning" aspects were interesting and very useful, particularly for deciding how many recording sites would end up in various brain regions with different insertion angles, etc.

Weaknesses

– There were files from the Waxholm Space rat brain atlas that needed to be downloaded. I clicked on the provided link but it wasn't clear how to find the relevant files, they appear to come from multiple different releases. Unless it violates licensing, can these be automatically included in TRACER? Extra steps like this can confuse and trip up new users (like me!), and potentially create obsolete instructions if the external links change their organization or content.

– The authors correctly note that installing and running TRACER requires some knowledge of Python and the command line. I see this as the biggest weakness of the package. They say they are working on a stand-alone GUI to run it, but in the meantime I suggest they develop instructional videos to talk a new user through a standard installation and example case.

– Both myself and a grad student in our lab tried to install the tool but ultimately failed to do so. We are moderately experienced with Python and we worked through some errors and felt like we were getting closer, but after ~3 hours we finally gave up. While I'm sure the fault is on our end to some degree, we were motivated to test the tool out and we are experienced in Python but we could not get it installed on our system. I suggest the author's β test the tool with novice users with no instruction other than what is on the Github, and see if they can discover any pain points in the installation process. I believe this is addressable, but is a critical weakness of the tool as it currently stands.

Suggestions for improving the user experience

– Strongly encourage the authors to upload the package to Pypi or conda package repository. This will make the installation of the dependencies and the package itself much easier.

– At the bare minimum, instructions should be expanded and clarified starting from the creation of the environment. If the terminal will be used anyway for installing the dependencies, it is much easier to create the environment using the Anaconda prompt from scratch.

– Downloading packages from Github can be confusing for people who are not experienced with this. Where the instructions say they need "TRACER package downloaded on your local computer…" I think the user manual should explicitly walk them through each step – What does a user do when they're looking at the Github page? Click download as Zip? Does it matter where this is saved? Should this be unzipped? Getting tripped up on these early steps can be deal breakers for new users.

– In the user manual, some screenshots would be helpful to orient the user, instead of things like "open the terminal by clicking the arrow near the name of your environment".

– After downloading the zip file from Github and extracting the package, the name of the folder is TRACER_main (or TRACER_master) and not just TRACER. So when trying to run it on Spyder (or wherever), it doesn't find the module.

– To run the package, the working directory has to be inside the first TRACER_main folder, since there is another TRACER_main folder inside the first. This tripped us up for a while.

Reviewer #3 (Recommendations for the authors):

The authors propose here a new open-source, python-based toolkit to reconstruct the trajectories of recording electrodes in the rat brain. Other possible applications include to visualize virus spread or to provide candidates stereotaxic coordinates before starting a surgery. At first glance, the tool is promising and may effectively fill a gap as many existing tools have been designed for mice primarily although rats continue to be highly relevant for behavioral studies. Installing and using the tool is not trivial for users with no Python experience though and the added value by comparison with other tools recently developed is unclear as detailed below.

Installing/running TRACER

The authors acknowledge in the short discussion that using TRACER may be challenging for users with no experience in Python-based environments. I can concur with that comment. I have asked a few trainees in the lab (with no coding experience) to try to install it and none of them was able to go through the entire process alone. So I think getting a GUI as stand-alone is really needed to impact on the field. Otherwise it is hard to appreciate why this could be more useful than any other tools. I would really encourage the authors to develop this GUI early on rather than only suggesting it's a possible future direction.

Added value versus other existing tools

Earlier this year, another paper was published at eLife documenting Brainrender, which is potentially suitable across species, including rats (Claudi et al., 2021). There are multiple other resources that are also available. I think a greater effort to explain how the present tool is positioned by respect with these other options is needed. This is very important for the field; while we can appreciate the value of having diverse tools to rely on, there is also some merit in adopting standards and splitting the community around multiple tools may not be beneficial in the long run. I think a much more thorough discussion is needed to present the PROs and CONs of TRACER versus Brainrender and other tools.

To address my general comments, I think the authors should really answer the following question: Considering that Brainrender is available in multiple species, what is the added value of TRACER?

I do not intend at all to minimize the work produced by the authors, I just want to make my point clearer from the end-user viewpoint: as many potentially equivalent tools exist, why choosing a specific one over the others?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "HERBS: Histological E-data Registration in rodent Brain Spaces" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

All reviewers recognized the value of HERB to process brain histology data and think it could be particularly useful for people working with rats, for which very little tools are currently available. The reviewers also identified a number of points that, if adequately addressed, may considerably improve the impact of HERB for the field. The authors are encouraged to implement these points or at least to provide a thorough discussion on their will and ability to carry further developments of the software in the future.

1) There is a need for clearer plans for long term sustainability of the software following future releases of Python. The authors should indicate with more details if they have the manpower necessary to ensure the maintenance of all packages in the long run, and possibly to implement further features (see other points below)

2) Being able to incorporate other brain atlases and other packages (e.g. CellFinder) would enhance its value and the potential for HERB to be widely adopted.

3) Viral reconstruction could benefit from a more quantitative assessment: since the user is provided with a list of brain structures affected by the viral spread, it would be incredibly helpful to provide the volume estimates (or %) affected for each of these brain regions.

4) Automatic registration of sections is not available, and therefore requires extensive manual work to use the software. Perhaps the authors have plans to improve on this front.

Reviewer #2 (Recommendations for the authors):

We gave HERBS some testing in the team and we found that it could really be very helpful for many researchers.

One potential caveat will be to ensure that maintenance of the main packages is being covered as new versions of Python are being developed. Recommending older Python versions for HERB may not be a realistic option in the long run as this is currently suggested in the Cooking book (which currently do not point on the right page for Python 3.9.9 – p.10, section 3.4.2).

We do have a major suggestion for viral spread reconstruction as we think this particular option may be particularly useful. Since the user is provided with a list of brain structures affected by the viral spread, it would be incredibly helpful to provide the volume estimates (or %) affected for each of these brain regions. This would thus open the way for relatively unbiased quantitative analyses (specificity of viral spread, but also lesions, or any infusion). This is much needed in the field to encourage researchers to better report histology data and I strongly believe it will really make HERB reaching another level.

Reviewer #3 (Recommendations for the authors):

It would be useful to specify whether this toolkit covers the following features, and if so, how?

– Designing multi-area implants: does the first section (generating surgical coordinates) include the possibility to design multi-probe implants that could target different brain areas? this can be a great value to those who'd like prototype headstages for targeting multiple areas.

– Adaptable to other atlases: is it possible to upload brain atlas for similar animals (e.g. naked mole rats or tree shrews)? How about other available rat brain atlases?

– Integrating other available packages: it would be great if one could easily integrate e.g. CellFinder with HERBS.

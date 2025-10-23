# Author response - Round 1

Authors:
- Salvador Dura-Bernal ([ORCID: 0000-0002-8561-5324](https://orcid.org/0000-0002-8561-5324))
- Benjamin A Suter ([ORCID: 0000-0002-9885-6936](https://orcid.org/0000-0002-9885-6936))
- Padraig Gleeson ([ORCID: 0000-0001-5963-8576](https://orcid.org/0000-0001-5963-8576))
- Matteo Cantarelli ([ORCID: 0000-0002-0054-226X](https://orcid.org/0000-0002-0054-226X))
- Adrian Quintana
- Facundo Rodriguez
- David J Kedziora ([ORCID: 0000-0002-0673-182X](https://orcid.org/0000-0002-0673-182X))
- George L Chadderdon
- Cliff C Kerr
- Samuel A Neymotin ([ORCID: 0000-0003-3646-5195](https://orcid.org/0000-0003-3646-5195))
- Robert A McDougal ([ORCID: 0000-0001-6394-3127](https://orcid.org/0000-0001-6394-3127))
- Michael Hines
- Gordon MG Shepherd ([ORCID: 0000-0002-1455-8262](https://orcid.org/0000-0002-1455-8262))
- William W Lytton ([ORCID: 0000-0002-3727-2849](https://orcid.org/0000-0002-3727-2849))

## Response text

DOI: [10.7554/eLife.44494.016](https://doi.org/10.7554/eLife.44494.016)

Essential revisions:

1) The installation process is not always straightforward. Some environmentsdon't seem to work right out of the box, and the instructions are not ascomplete as one would like.

We have rewritten and reorganized the installation instructions to clarify the steps involved, and have fixed several issues identified by the reviewers. Further details are provided in the answers below.

2) There is some confusion about support for Python 2 vs Python 3. It is notalways clear which works best. The reviewers would be quite happy if it is just

Python 3, but in any event the Python version support for each of the reportedfeatures should be clearly stated.

We have now clarified in the installation instructions that all NetPyNE features support both Python 2 and 3, except for the NetPyNE GUI, which only supports Python 3.

3) Rainbow color maps (used in Figures 3 and 6) are not ideal. The authors shouldrevisit this, and the reviewers make several suggestions.

We are thankful to the reviewers for bringing to our attention this issue, which we were not aware of. We have replaced the rainbow colormap in Figures 1, 3, 5, 6 and 7 with the Viridis colormap suggested by one of the reviewers. This colormap marks strength by intensity (equivalent to grayscale) and is colorblind friendly.

Reviewer #1:

[…] I have only a few small critiques of the paper, particularly with regard tois rather sparse coverage of the RxD capabilities. RxD is mentioned severaltimes but other than some calcium dynamics its use is not well illustrated.

It isn't clear if there is currently a capability to read/write SBML, thoughthe NeuroML capability is well stated. In contrast, the network capabilitiesare very well fleshed out. Similarly, it isn't clear how ion channel kineticsmay be defined within this framework, or if they rely on pre-existing channeldefinitions.

We agree with the reviewer that RxD was not adequately covered. We have created a separate subsection "Reaction-diffusion parameters" under the "High-level specifications", added two paragraphs describing the RxD components and how they are defined within NetPyNE. This includes a simple example to implement calcium buffering, which is also included in Figure 2A, and the description of a more detailed example involving IP3 and calcium signaling within the cytosol and endoplasmic reticulum, in a small cortical network.

To clarify kinetics definition we added the following: "RxD is now being extended to also permit definition of voltage-dependent or voltage- and ligand-dependent ion channels, and can also respond to synaptic events or interact with NMODL-defined mechanisms so as to affect membrane currents and membrane voltages."Experimental support for voltage-dependent ion channel kinetics has been added in a branch, and is expected to be available in NEURON 7.7, pending satisfactory completion of tests. See: https://github.com/adamjhn/nrn/commit/c87ea34c848f47f3b6a1c90e95b3119e8117e170

We added the following on SBML to the Discussion: "Work is also in progress to extend NEURON's RxD partial support for reading and writing Systems Biology Markup Language (SBML), a standardized declarative format for computer models of biological processes (Bulanova et al., 2014). We also aim to provide direct translation of SBML to NetPyNE's RxD declarative specifications."

Reviewer #2:

[…] I have tried using and downloading the software, confirming that the first tutorial example (http://www.netpyne.org/tutorial.html) works. I found that on my system (Scientific Linux 7) things did not quite work out of the box when I tried installing from source, but I would expect this from software that has not yet been tested widely in the field. From my previous experience of the NEURON maintainers, I expect that bug reports like mine (see below) will be dealt with quickly.

We thank the reviewer for taking the time to install and try the software, and for identifying several issues. We have now fixed these issues and have provided more clear installation instructions. More details can be found in the responses below.

There are some limitations to the connectivity structures possible to create, but this is a consequence of a declarative design, which does offer advantages over a programmatic generation of connectivity.

We agree that the declarative approach has some limitations in terms of expressing connectivity. We have now clarified the text to better convey that connectivity patterns can also be defined via custom connectivity matrices; and that several parameters (e.g. probability, weight, delay, etc.) can be defined using arbitrarily-defined mathematical expressions that can include cell properties (e.g. location).

The paper is well-written, though I do have a small gripe with the rainbow colormap used in Figures 3 and 6, which I think could be designed to be more colorblind friendly. If viewed through Color Oracle (http://colororacle.org/index.html) with the grayscale option, it can be seen that the maximum intensity appears about halfway up the scale. Compare with a colorblind-friendly palette, such as Viridis: https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html

We have replaced all the colormaps in Figure 1, 3, 5, 6 and 7 with the Viridis colormap suggested by the reviewer.

Reviewer #3:

[…] Main concernhttp://netpyne.org/install.html declares that Python 2 or 3 are supported. https://github.com/MetaCell/NetPyNE-UI/wiki/Installing-NEURON-crxd-Version declares Python3 is in development. Which is the case? As this software is geared also towards less advanced users the installation instructions should be clear. I have a feeling they have not been tested by naive users.

What I expect is a clear information of how to install all tools relevant for the users of NetPyNE to use its all potential: multithreaded computation, RxD, GUI, etc. If the instructions are the same in Python 2 and 3 this should be made clear in the docs. If they differ, it should be clear. If only certain features work in one version of Python or Neuron, this should be acknowledged. I think this is much more important for the users than the information that it is possible to install NetPyNE without Neuron to translate models. This is an advanced feature which would not be used by many users, I suppose. The clear steps to installation should lead the user to an instance which at a minimum will allow him or her to run the tutorials, multithreaded computation, RxD, GUI. Assume no Neuron installed and recommend installation. Current instructions indicate --without-paranrn installation. Is this required for RxD? It is not clear.

We are thankful to the reviewer for taking the time to install and test the tool, and provide helpful feedback. We have updated the text and reorganized the installation instructions (http://www.netpyne.org/install.html) to make them more clear and to provide information on how to install the different required tools. We have also clarified that the basic NetPyNE package (without GUI) supports both Python 2 and Python 3, but the NetPyNE GUI only supports Python 3, and have provided instructions for each case. We made the installation with parallel support (--with-paranrn) the default option, and clarified that installing support for parallelization is optional, and that both options are compatible with RxD and the GUI. We have also removed comments about using NetPyNE without NEURON, and other unnecessary information.

We would also like to note that we have a working online version of NetPyNE (including the GUI, RxD and parallelization) which we plan to make permanently available this year as part of a collaboration with Open Source Brain. This will enable users to run the full tool online in a web browser without the need for any installation.

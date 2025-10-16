# Peer review - Round 1

Editors:
- Caleb Kemere, https://ror.org/008zs3103 Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70661.sa0](https://doi.org/10.7554/eLife.70661.sa0)

An increasing number of systems neuroscience experiments involve imaging neural activity using head-mounted epifluorescent microscopes, or "miniscopes". A growing community has been using the Minian software package to process the imaging data into a useful form for subsequent analysis. The Minian team has done an excellent job of exposing the various parameters involved to be easily accessible to users while maintaining a performant robust tool. This work presents Minian and is in many ways an exemplar of how open source software can be presented in journal form.


---

# Peer review - Round 1

Editors:
- Caleb Kemere, https://ror.org/008zs3103 Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70661.sa1](https://doi.org/10.7554/eLife.70661.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your work entitled "Minian: An Open-source Miniscope Analysis Pipeline" for further consideration by eLife. Your revised article has been reviewed by three peer reviewers, including Caleb Kemere as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers were unanimous in concluding that there was considerable value in presenting Minian to the field. In particular they appreciated (as you have described) the insight into parameter selection that the Minian codebase allows. However, there was concern that the manuscript does not adequately compare Minian with existing tools (e.g., CaImAn) in terms of batch run time (i.e., after the parameters have been selected and one wants to churn through data) and final performance/accuracy (i.e., are the ROIs "as good"?). Given that memory needs are a claimed advantage, a comparison here would also be valuable. Reviewer 3 has used simulated data for the ROI comparison and includes code in their review.

Reviewer #1 (Recommendations for the authors):

The advent of open source miniscopes has significantly expanded the population of experimenters who are excited to record activity-dependent fluorescence in freely moving animals. Unfortunately, they often find that once they have solved the challenges that arise in acquiring the data, a new challenge awaits – extracting the neural activity for analysis. While there are existing open source tools for extracting activity-dependent fluorescence traces from video data, these packages are not particularly accessible for investigators with significant experience in computational code. For novices, they can be impenetrable. The Minian toolbox aims to solve the problem of data analysis while also bringing along novices, illuminating different parameter choices, and making each step of the process more understandable. We found that, to a great extent, it achieves this aim, and thus we think that it rises to the level of significant interest to a broad audience. We did have some concerns with the current manuscript. In particular, limited evidence is provided to allow comparison of results, performance and efficiency between Minian and other established packages (e.g., how in terms of processing time, or in terms of the results).

If Minian's major contribution is usability and accessibility (lines 134-135) it is not clear why a new package had to be created rather than extending CaImAn or MIN1PIPE. The former does have out-of-core support, where memory usage can be reduced by limiting the number of parallel processes. A table detailing the methods/algorithms used by each of these packages may be useful for comparison purposes.

Lines 113-115: The text indicates that data may still be split into patches of pixels, so it is unclear how merging based on overlapping parts can be avoided. Aren't the overlaps necessary because putative neurons may span patch boundaries? Perhaps the authors could also compare performance of temporal splitting and non-splitting data processing. Will temporal splitting lead to comparable performance?

Lines 117-119. Had to look at documentation website to figure out how to limit memory usage--put this in paper. Include some graphs to show the tradeoff between memory usage and computational time.

Please comment on motion correction when there is a rotation in the FOV?

For motion correction, provide additional information about how the template is generated (e.g. how many frames used) and any user-defined parameters.

Lines 205-206: Will the same mask be applied to all frames before motion correction? Or the mask will be applied to this certain frame and then be applied to all frames after motion correction?

Line 499: write the function used for optimization.

Paragraph starting at line 576 would benefit from some equations for clarity's sake.

Implement manual merging as in original CNMF-E paper?

Line 699: define preprocessed with respect to Figure 1--this is post motion-correction presumably?

Line 725, For Figure 14, what is the fps for the data taken? Only frame number was shown in the right side column, if the fps is 20, then 150 frames correspond to about 10 sec of calcium transient, which is on the long side for a healthy neuron.

Line 826-828: Is dimension here referring to x and y dimensions of the frame? Please elaborate how each slice on one dimension can be processed independently.

Discuss robustness to long data (where CaImAn seems to fail). Using Minian, was CNMF performed on each msCam video individually? If so, what happens when a calcium event occurs near the video boundaries?

Line 879: What would be an example number that you would consider as "significantly high (see below) stability"? It is not clear what "see below" was referring to in terms of high stability. Example provided for place field size criterion only.

Reviewer #2 (Recommendations for the authors):

Dong et al. presents "Minian" (Miniscope Analysis), a novel, open-source analysis pipeline for single photon in vivo calcium imaging studies. Minian aims to allow for users with relatively little computational experience to extract cell location and corresponding calcium traces in order to process and analyze neural activity from imaging experiments. It does so by enhancing the visualization of changes to free parameters during each step of data processing and analysis. Importantly, Minian operates with a relatively small memory demand, making it feasible for use on a laptop. In this manuscript, the authors validate Minian's ability to reliably extract calcium events across different brain regions and from different cell types. The manuscript is well-organized, clear, and easy to follow. Importantly, this manuscript describes a resource which complements previous open-sourced tools built by the authors (e.g. the UCLA Miniscope), as well as other, similar systems. Collectively, these tools comprise an affordable, open-source, easy to use system for single photon calcium imaging and analysis in freely-behaving mice. This project will impact the field by providing open-source, user-friendly, customizable, intuitive software for the analysis of single photon in vivo calcium imaging experiments across a variety of imaging systems.

1) Page 5, line 100. In regards to visualization of parameter changes and resulting outcomes using Minian, the authors state that "This feature provides users with knowledge about which parameter values should be used to achieve the best outcomes and whether the results appear accurate." What do the authors mean by "best outcomes" and "appear accurate"? Is there a way the authors can suggest to rigorously test for data accuracy rather than looking to see if data "appear accurate"? Do the authors plan to provide any guidance for standard parameters/variables to use for brain regions and/or cell types? These issues are somewhat highlighted in the limitations section at the end, but I think there could be some more effort put into providing more objectivity to this approach.

2) Page 9, line 240. As part of their "denoising" step, the authors pass their frames through a median filter. A number of filters can be used for denoising (e.g. Gaussian). The authors should justify why this filter is used and potentially compare it to other filters.

3) Page 9 describes setting the window size to avoid "salt and pepper" noise on the one end, and "over-smoothing" on the other. Minian allows for the visualization of distinct settings of the window size, however, it is left up to the user to select the "best" window. This allows for user bias in selection of an optimal window. One thing that would be useful is if the window size selected could be compared to the expected cell diameter, which could then be reported alongside final results.

4) Page 23, line 671. For registering cells across multiple recording sessions, the authors "discard all matches that result in conflict". Are users notified of number of discarded matches and is there a way to discard one match (eg cell A to B) but not another (Cell B to C)?

5) Page 26, like 750. The authors use Minian to process and analyze calcium imaging data and ezTrack to extract animal location. The two are time-locked using timestamps and further analyses are performed to correlate imaging and behavioral data. Do the authors synchronize their imaging and behavioral data using additional software? If so, can they provide information onto how best to synchronize and analyze such data?

Reviewer #3 (Recommendations for the authors):

Context:

Brain imaging techniques using miniaturized microscopes have enabled deep brain imaging in freely behaving animals. However, very large background fluctuations and high spatial overlaps intrinsic to this recording modality complicate the goal of efficiently extracting accurate estimates of single-neuronal activity. The CNMF-E algorithm uses a refined background model to address this challenge and has been implemented in the CaImAn analysis pipeline. It yields accurate results, but is demanding both in terms of computing and memory requirements. Later an online adaptation of the CNMF-E algorithm, OnACID-E, has been presented which dramatically reduces its memory and computation requirements.

Strengths:

Here the authors use a simpler background model that has been suggested by the authors of the MIN1PIPE pipeline. After the background has been (approximately) removed the data can be processed using the standard CNMF algorithm. The latter requires some user specified parameters and the interactive visualizations provided by Minian greatly simplify the setting of these parameters. Thus Minian's learning curve is less steep than that of other pipelines. Using a less refined background model and libraries that support parallel and out-of-core computation, Minian requires less memory than the batch CNMF-E algorithm.

Weakness:

While Minian's memory requirements are low compared to the batch CNMF-E algorithm, its online adaptation OnACID-E is even less demanding. The authors base their insights mainly on visual inspection, and fail to thoroughly validate the accuracy of their extracted temporal traces using simulated ground truth data as well as various real datasets as was done in the original CNMF-E (as well as the MIN1PIPE) paper. Own analysis of simulated ground truth data indicates that Minian uses less memory but also performs less well than CaImAn's CNMF-E implementation with regard to computational processing time and accuracy of extracted deconvolved calcium traces.

Upshot:

Minian is a user-friendly single-photon calcium imaging analysis pipeline. It's interactive visualizations facilitate accessibility and provide an easy means to set key parameters. In practice, Minian's slower computational processing time compared to other pipelines is likely offset by less user time spent on parameter specification. I expect other pipelines will take up the idea put forward by Minian to use interactive visualizations for the latter.

You primarily focus on interactive visualizations. I had no trouble installing Minian and thoroughly enjoyed the visualizations afforded by xarray, dask, bokeh and holoviews.

Basing your pipeline on established algorithms makes one hopeful to get accurate results, but since you are not just providing a GUI for a well validated pipeline but taking inspiration from CaImAn, MIN1PIPE and your own previous work, that's not guaranteed. In light of this, I don't find the Results section convincing.

Showing only averaged results and comparing to a null distribution leaves the reader with the impression that the pipeline performs better than random, which is not that impressive. Your pipeline actually does quite well and deserves better promotion.

You need to rework the Results section and follow along the lines of the CNMF-E and MIN1PIPE paper:

* compare to simulated ground truth data

- false positives/false negatives

- most importantly, how accurate are the extracted deconvolved traces that would be used in the downstream analysis?

* compare to multiple real datasets

- false positives/ false negatives using manual annotation as (imperfect) 'ground truth'

- show individual traces

Because one of your sale pitches is Minian's low memory demand, you need to include a figure illustrating the scaling of processing time and memory with dataset size (FOV, #frames, #neurons), cf. Figure 8 of the CaImAn paper.

A good starting point would be the simulated data of the CNMF-E paper. I used that data to gain some experience with Minian as a potential future user, and to compare it to CaImAn, with which I already have some familiarity.

After parameter tweaking both yielded a perfect F1 score of 1. However, the denoised/deconvolved traces obtained with CaImAn had an average correlation of 0.9970/0.9896 with ground truth, whereas Minian only yielded average correlations of 0.9669/0.9304.

The processing time on my Desktop/MacBookPro was 46.6s/169.1s for CaImAn and 140.9s/359.8s for Minian (using 12/4 workers, 2 threads). The peak memory was 31.698GB/4.508GB for CaImAn and 11.382GB/5.534GB for Minian.

Thus, at least in my hands, CaImAn outperforms Minian, presumably due to the more refined background model, and I'll likely stick with the former. Though I grant you that parameter selection is easier in Minian. I wished there was a pipeline with the best of both.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Minian An Open-source Miniscope Analysis Pipeline" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Please address the comments of the reviewers below. In particular, the issue of reproducibility (i.e., missing data source files) is important, as is the concern of reproducing Figure 18.

Reviewer #1 (Recommendations for the authors):

Most concerns were addressed, but a couple of clarifications are still needed. First, with regard to boundary conditions for chunks, based on our understanding of your response, the text should be updated to clarify that neither spatial nor temporal chunking can be used for the core CNMF computation (as it computes across both space and time). How does this limitation constrain performance?

Second, with regard to chunking, there is a long description of motion correction. It seems that the initial chunk has a minimum size of 3, which will be aligned, then 9 frames will be aligned, and so on in powers of three (27, 243, etc). Is this correct? Perhaps some numerical example would be helpful for this text description.

Reviewer #2 (Recommendations for the authors):

The revisions adequately addressed all of my concerns.

Reviewer #3 (Recommendations for the authors):

The authors did a good job addressing the vast majority of my concerns and improving the paper.

My main concern is lacking reproducibility, contrary to the claims in the "Transparent Reporting File":

While the repo for figure 1-14 and figure 20 can be found at

https://github.com/denisecailab/Minian_paper_data, the data source files that are supposed to be hosted as zip files on a google drive are missing.

The repo for figure 15-19 https://github.com/denisecailab/Minian-validation does not exist, or is not public.

I have not been able to reproduce Figure 18.

I repeated (6x) and concatenated the 2000frames of your demo pipeline, and processed them using 4 parallel processes. (The only parameters in Caiman's demo pipeline adjusted were gSig=(5,5); gSiz=(21,21); min_corr=.75; min_pnr=7; yielding ~280 cells). The results should thus be in the same ballpark as Figure 18, 300 cells, 12k frames.

However, the runtime was similarly about 25 min whether using Minian or Caiman, and whether running on a Linux Desktop or MacBookPro.

The reported memory seems about right for my Desktop, however, my MacBookPro processed the data using Caiman and merely 10GB of RAM, the same amount of memory as Minian.

Your demo pipeline doesn't run on my MacBookPro (with M1 chip), it fails in update_background step, and I had to increase the memory limit for each worker from 2 to 2.5GB.

I have the following remaining issues:

line 542: You need to subtract the neural activity AC before projecting, f = b'(Y-AC).

line 635: Is the 'input movie data' the data after subtracting the contributions of all the other neurons and background bf? Otherwise projecting the input data on the cell doesn't properly demix them if other components overlap. The least squares solution of min_c ||y-Ac|| is (A'A)^{-1}A'y, not A'y.

Figure 15: Why not put error bars for the correlations like you do in Figure 16? If the error bars are smaller than the symbols, say so in the paper. (E.g. standard error of the median via bootstrap)

Figure 16: Why does the correlation saturate at ~0.8? Shouldn't it approach ->1 for noise->0?

line 851: Is the data described in a previous publication you missed to cite? Frames, FOV, rate?

line 895: "despite the fact…". Why despite? This is expected behavior when the number of parallel processes is set to be constant, without putting a limit on memory.

line 933: Is the data described in [35]? I.e. 320x320@20Hz.

# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68837.sa1](https://doi.org/10.7554/eLife.68837.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper presents and evaluates a machine learning method for segmenting and annotating animal acoustic communication signals. The paper presents results from applying the method to signals from Drosophila, mice, marmosets, and songbirds, but the method should be useful for a broad range of researchers who record animal vocalizations. The method appears to be easily generalizable and has high throughput and modest training times.

Decision letter after peer review:

Thank you for submitting your article "Fast and accurate annotation of acoustic signals with deep neural networks" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Ronald Calabrese as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Roian Egnor (Reviewer #1); Todd Troyer (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

There are two main concerns with this paper that all three reviewers shared in their own way. The reviews offer details of how to address these concerns.

1. The authors claim that the method compares favorably to other machine learning methods, but they only provide head-to-head performance comparisons for Drosophila songs. There are no direct comparisons against other methods for mouse ultrasonic or songbird vocalizations, nor is there a readable summary of performance numbers from the literature. This makes it difficult for the reader to assess the authors' claim that DeepSS is a significant advance over the state of the art.

2. The authors provide little discussion about optimizing network parameters for a given data set. If the software is to be useful for the non-expert, a broader discussion of considerations for setting parameters would be useful. How should one choose the stack number, or the size or number of kernels? Moreover, early in the paper DeepSS is claimed as a method that learns directly from the raw audio data, in contrast to methods that rely on Fourier or Wavelet transforms. Yet in the Methods section it is revealed that a short-term Fourier front-end was used for both the mouse and songbird data.

Reviewer #1 (Recommendations for the authors):

General comments:

This is a reasonable piece of software. Not super polished, but pretty straightforward. Once I got it installed (which was a little involved) it worked out of the box on raw mouse vocalizations. There could be a little more background on other methods/approaches and their strengths and weaknesses. In addition, I think more explanation about tuning parameters is necessary if the goal is for users without machine learning expertise to be able to use this.

I. Results

A. How good is it?

1. How fast is it?

a. How long to train?

Train time depends on the amount of data, but the ranges quotes (10 minutes to 5 hours) are quite reasonable. It works on reasonable hardware (I tested on a laptop with a GPU).

b. How long to classify?

Latency to classification is between 7-15ms, which is a little long for triggered optogenetics, but not bad, and certainly reasonable for acoustic feedback.

2. How accurate is it?

a. Accuracy is improved relative to Fly Song Segmenter, particularly in recall (Arthur et al., 2013; Coen et al., 2014).

Pulse song:

DeepSS precision: 97%, recall: 96%

FlySongSegmenter: precision: 99%, recall 87%.

Sine song:

DeepSS precision: 92%, recall: 98%

FlySongSegmenter: precision: 91%, recall: 91%.

b. One main concern I have is that all the signals described, with the exception of pulse song, are relatively simple tonally. Bengalese finch song is much less noisy than zebra finch song. Mouse vocalizations are quite tonal. How would this method work on acoustic signals with noise components, like zebra finches or some non-human primate signals? Some signals can have variable spectrotemporal structure based on the distortion due to increased intensity of the signal (see, for example, Fitch, Neubauer, and Hertzel, 2002).

W.Tecumseh Fitch, Jürgen Neubauer and Hanspeter Herzel (2002) "Calls out of chaos: the adaptive significance of nonlinear phenomena in mammalian vocal production" Animal Behaviour, 63: 407-418. doi:10.1006/anbe.2001.1912

B. How easy to use?

0. "our method can be optimized for new species without requiring expert knowledge and with little manual annotation work." There isn't a lot of explanation, either in the paper or in the associated documentation, of how to select network parameters for a new vocalization type. However, it does appear that small amounts of annotation are sufficient to train a reasonable classifier.

1. How much pre-processing of signals is necessary?

All the claims of the paper are based on pre-processed audio data, although they state, in the Methods section that preprocessing is not necessary. It's not clear how important this pre-processing is for achieving the kinds of accuracy observed. Certainly I would expect the speed to drop if high frequency signals like mouse vocalizations aren't downsampled. However, I tried it on raw, un-preprocessed mouse vocalizations, without downsampling and using very few training examples, and it worked quite well, only missing low signal-to-noise vocalizations.

C. How different from other things out there?

It would strengthen the paper to include some numbers on other mouse and birdsong methods, rather than simple and vague assertions "These performance values compare favorably to that of methods specialized to annotate USVs (Coffey et al., 2019; Tachibana et al., 2020; Van Segbroeck et al., 2017)." "Thus, DeepSS performs as well as or better than specialized deep learning-based methods for annotating bird song (Cohen et al., 2020; Koumura and Okanoya, 2016).

D. Miscellaneous comments

1. Interestingly, the song types don't appear to be mutually exclusive. One can have pulse song in the middle of sine song. That might be useful to be able to toggle…I can imagine cases where it would be nice to be able to label things that overlap, but in general if something is sine song, it can't be pulse song. And my assumption certainly was that song types would be mutually exclusive. Adding some explanation of that to the text/user's manual would be useful.

2. How information is combined across channels is aluded to several times but not described well in the body of the manuscript, though it is mentioned in the methods in vague terms:

"several channel convolutions, 𝑘𝛾(1, 𝛾), combine information across channels."

II. Usability

A. Getting it installed

Installing on Windows 10, was a bit involved if you were not already using python: Anaconda, python, tensorflow, CUDA libraries, create an account to download cuDNN, and update NVIDIA drivers.

However, it went OK until I hit this:

error:

File "…\miniconda3\envs\dss\lib\ctypes\__init__.py", line 373, in __init__

self._handle = _dlopen(self._name, mode)

FileNotFoundError: Could not find module '…\miniconda3\envs\dss\lib\site-packages\scipy\.libs\libbanded5x.3OIBJ6VWWPY6GDLEMSTXSIPCHHWASXGT.gfortran-win_amd64.dll' (or one of its dependencies). Try using the full path with constructor syntax.

rummaging around in Stackoverflow I found this (answer #4):

https://stackoverflow.com/questions/59330863/cant-import-dll-module-in-python

which was to edit ~\Miniconda3\envs\dss\lib\ctypes\ _init_.py to change winmode=None to winmode=0.

This worked, but did slow me down a fair bit. I'm not sure who the target audience is for this software, but it may be a bit much for the average biologist.

B. Using it

It wasn't clear to me what " complete annotation" meant: "Once you have completely annotated the song in the first 18 seconds of the tutorial recording…". Does this mean that all instances of pulse and sine song must be labeled? What are the consequences if this is not true?

I also wasn't clear how to know when it finished training and I could try predicting.

I was a bit confused by there being 2 menu headings called "DeepSS", one of which (the rightmost) has a Predict option and one of which doesn't. The first time through I used the leftmost DeepSS menu heading for Make dataset and Train, and it didn't work, the second time through I used the rightmost one and it did work (but this might have been user error).

III. General usability:

1. It would be nice if the oscillogram vertical axis didn't autoscale, it made it hard to recognize sine song when there were no pulses.

2. It would be nice to be able to change the playback rate, or the size of the jumps in the navigation bar at the bottom.

3. It was not very clear in the instructions how to fix errors and use those annotations to train again, although in the body of the text this is explicitly stated as important.

"We find that DeepSS can be efficiently trained using an iterative protocol (Pereira et al., 2018) (Figure 4C, S8): Annotate a small set of recordings and train the network for a few epochs; then generate annotations on a larger set of recordings and correct these annotations."

"Correct any prediction errors-add missing annotations, remove false positive annotations, adjust the timing of annotations."

4. The instructions for correcting could be more clear. It took a little fiddling to figure out I needed to switch to "add pulse_proposals" in order to remove a pulse proposal.

Reviewer #2 (Recommendations for the authors):

In general, I recommend publication after major revision.

Apart from my comments above, my excitement for this toolbox is a little bit hampered by a few aspects:

Regarding the comparisons to other tools, it would be great to compare (or at least discuss the performance of other recent tools on the bird and mouse dataset). Existing models are described as slow (Line 50), but no quantitative comparisons are given.

What are the human recall/precision for Figure 1 (compare to MARS, where a nice classifier vs. human comparison is given: https://www.biorxiv.org/content/10.1101/2020.07.26.222299v1). Is FSS a tunable algorithm and how was it tuned?

While the authors emphasize that the architecture does not require any pre-processing, they end up using the "optional" Short-time Fourier transform frontend for all, but the sine wave detection for flies (i.e. mice and bird). So I think this emphasis is ill advised.

In the end, the authors use different network parameters for all datasets (see Table S1A; with/without STFT, # stacks, kernel size…). This begs the question is this necessary. What happens if one trains the same architectures on the different datasets, does the performance suffer? -- I would suppose that is not the case, and with respect to the usability of this toolbox this seems to be an important question. I.e. how should users pick the architecture and hyperparameters?

Reviewer #3 (Recommendations for the authors):

The most important issue I had with the paper is that it provided the reader with little sense of DeepSS's performance relative to other software. The paper would be much better if other approaches were implemented on publicly available data sets and compared head-to-head.

The methods should state very clearly where the data sets used are available for download. While the authors may believe in DeepSS, other challengers will inevitably arise. These authors should be given the opportunity to report head-to-head performance against DeepSS on the same data.

The text references in the mouse section are to figure 3, but the relevant figure is now figure 2.

There are several places where the color scale used is useless, namely in the confusion matrices (Figure 1D, 1I, 2E, 2H, 3C and some supplemental figs). At these performance levels, color just indicates the correct vs. incorrect parts of the graph – relative shades of the heat map are not perceptible.

The birdsong confusion matrices are similarly uninformative, since all that is seen is a bunch of boxes along the diagonal. Worse yet, the discretization of the figure makes it appear that boxes along the diagonal have different sizes/offsets, suggesting structure where there is none. Showing marginals of the matrix like Figure S4E can be useful.

In Figure S4C, precision and recall are plotted whereas in S4E false positive and false negatives are plotted. Are both plots needed?

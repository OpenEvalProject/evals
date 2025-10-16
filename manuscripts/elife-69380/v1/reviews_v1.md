# Peer review - Round 1

Editors:
- Mackenzie W Mathis, EPFL Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69380.sa1](https://doi.org/10.7554/eLife.69380.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Tracking cell lineages in 3D by incremental deep learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Asim Iqbal (Reviewer #1); Christian Tischer (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please address the usability of the code (i.e., please see all three reviewers comments and try to address them).

2) Please address reviewer comments regarding if a 3DUNet is sufficient, and truly state of the art; please provide results comparing to other architectures (such as StarDist, as reviewer 2 points out, or other architectures, see reviewer 1). Also, please consider adding limitations around network options to the discussion.

3) Multiple reviewers have questions around the ellipse tracker – could you show this is best / alternatives for cells with other shapes, and please consider a limitation regarding this (i.e., I assume a neuron with a long axon would not be well fit by an ellipse).

Reviewer #1 (Recommendations for the authors):

– Consider moving figure 1 in supplementary and make figure 2 as figure 1.

– Add a block diagram to show how to use ELEPHANT step by step through an example.

– It would be nice to show training, validation curves of 3D U-Nets in the supplementary figures to confirm if there is no over-fitting in the models.

– Demonstrate the usage and performance of the framework on diverse examples in the main figures (e.g. Figure 2).

– Expand the Result section in the study.

Reviewer #2 (Recommendations for the authors):

More details about running the code: The specific link to the documentation was broken on github. I tried to go through the instructions in the readme, discovered that Mastodon installation requires java sdk (these instructions should be included for linux, windows and mac). Once java was installed the user needs to convert tiffs, like those from celltrackingchallenge.net, into bigdataviewer format. This procedure should be documented at least for the format provided on celltrackingchallenge. For instance, I opened a folder of tiffs in imageJ, converted to a stack, then saved as an xml. If there is a way to do this for instance from the command line it would be great for it to be documented. Next I opened the xml from inside mastodon (the window that pops up from "java -jar elephant-0.1.0-client.jar"). I was able to open bdv but when I tried to do anything in the elephant plugin it said connection refused. I was running the code on Ubuntu 18.04.

It would be helpful to include more discussion about the amount of data needed, and the amount of manual input. This tool has increased practical value if ~1 month of interactive tracking (as described in the paper) is not needed for each dataset. It is excellent that the networks in the paper are provided as pth files. Can you have the networks as options in the mastodon plugin so that users can easily access them?

Can you comment on the use of ellipses to approximate nuclei instead of more complex shapes? Is the advantage of this representation that it is easy to use in the case of sparse labels? Or do you see it as advantageous to allow overlapping masks? Similarly, for the optical flow model, the output of the detection model is used to compute optical flow, so ellipses instead of precise cell boundaries. Have you considered how having precise cell boundaries might help the optical flow model perform better?

Reviewer #3 (Recommendations for the authors):

Overall I think this is fantastic work and I would be very happy to review a revised version of the software.

30: I would just write "..for 3D cell tracking.."

37: "in a crustacean (1 week)" It is not clear to me what the "1 week" refers to. Maybe the number of time points and cells would be more informative in this technical context?

63: It is not really "based on Fiji", maybe write "deployed in Fiji"?

194: "To reduce the amount of…" Does one also need to duplicate the data when running client and server on the same computer? For big image data it would be very nice to avoid this.

214: Insert space between "without "

215: "showed non-negligible variations in intensity" Is this a problem for the deep learning detection model? If so, this should be elaborated on and a section "Image data preparation" where this is explained should be added to the documentation.

224: "On the server, images, annotation labels and outputs were stored in the Zarr format," I am curious: Why is it necessary to store the image in Zarr format rather than HDF5?

226: "these data were prepared using a custom Python script" Running a python script within a Docker container could be quite a hurdle for non-computational end-users. Any chance that could be simplified?

247: "Lprioris" There is a space missing.

ELEPHANT/Mastodon software and documentation

Mastodon

The author's software should be compatible with the latest version of Mastodon, which includes a few bug fixes that avoid hanging of the software during the annotation process.

Example demo data set

To get started, the authors provide an example data set, which is great. However, for me training the detection and linkage on the current example data set takes too much time to be done during a review of the publication. I would appreciate if the authors provided a much simpler demo dataset where everything (detection + linkage) could be done within maximally 30 minutes of work. I think for reviewing the software and also for beginner users such a toy data set would be extremly useful.

Server connection

I think adding something to the user interface that makes the connection to the server more explicit would be very nice.

For example: Plugins > ELEPHANT > Connect to Server

Then one could put functionality there that would, e.g., allow the user to check whether the connection is working and maybe some feedback about which server one is connecting to.

In fact, for connecting to the Google Colab sever one should explore whether it is possible to create a UI in Mastodon where the user could just copy and paste these two lines:

SSH command: ssh -p10739 root@8.tcp.ngrok.io

Root password: qXzK8cOwvkWxdAcGZwM0

And then the Java code would parse those two lines create system calls to establish the server connection via the two SSH commands. This would be much more convenient than the current workflow where one needs to open a terminal and modify tedious SSH command line calls (also, many less IT savvy users could be put off by the command line calls).

Maybe for the other server modes similar ideas could be explored (personally I only looked into the Colab based solution).

It would be great if there was more feedback within the client on what is happening right now on the server side. I added specific suggestions in few places (see below). One could even consider mirroring all the text output that is generated server side in the Elephant client log window.

Training of detection

While I think I get the point now, it is a bit though to understand all the different tags (TP,FP,…).

What I understood now is that probably it is OK to simply add spots manually and they would be used as training data (being tagged as TP by default). If that is true I would suggest to split the annotation workflow in the documentation in a basic and advanced version, where in the basic version one maybe does not need to explicitly provide manual tags at all?!

https://elephant-track.github.io/#/v0.1/?id=_2-shortcuts

Current text: If you cannot find the ~/.mastodon/keymaps/ directory, please run [File > Preferences…] first to create it with the ~/.mastodon/keymaps/keymaps.yaml.

Suggested text: If you cannot find the ~/.mastodon/keymaps/ directory, please run [File > Preferences…] and click [OK] to create it. Please restart Mastodon for the Elephant keymap to become active.

In addition, it would really be great if setting up the keymap.yaml file was easier.

One could for example provide the already edited keymap.yaml file for download and tell the user to replace the current one. Since you are shipping a stand-alone version of Mastodon anyway, even better would be if that was somehow included in (or taken care of by) the elephant.jar. Could you somehow ship this information inside the jar?

https://elephant-track.github.io/#/v0.1/?id=detection-workflow

I would recommend adding a sentence here that first the connection to the server needs to be established.

https://elephant-track.github.io/#/v0.1/?id=_5-establish-connections-from-your-computer-to-the-server-on-colab

It would be nice to add an explanation why one needs to establish two connections (rather than only one).

https://elephant-track.github.io/#/v0.1/?id=_2-initialize-a-model

It would be very good if there was more feedback within the Mastodon UI about whether and when the model initialization has finished successfully.

Also feedback about the training progress, e.g. the decrease of the loss, the current cycle, a progress bar, would be great such that one can judge how well the training worked and whether the current number of training cycles is adequat.

Typo in Mastodon: "Detection > Reset *a* Seg Model". I suggest removing the "a".

"Predicted spots and manually added spots are tagged by default as unlabeled and fn, respectively."

I wonder whether manually added spots should be tagged as tp by default? At least I often forgot clicking "4" to mark them as tp. In fact, I am confused now, because maybe the manually added spots are tagged as tp by default?

https://elephant-track.github.io/#/v0.1/?id=_6-importing-and-extending-a-pretrained-model

Importing a pretrained model is simple. Just specify the model parameter file located at the workspace/models in the settings.

I could not figure out where to specify the model parameter file. On the client or on the server? And how to do it exactly?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Tracking cell lineages in 3D by incremental deep learning" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Please be sure to not use the term "state of the art" (SOTA) unless you demonstrate truly best performance (which you do not) – it is not a requirement to be SOTA to be published. Moreover, please address reviewer #2's request, and consider reviewer #3, i.e., providing local GPU instructions (vs only COLAB).

Reviewer #1 (Recommendations for the authors):

Thanks to the authors for submitting the revised manuscript and providing the response to the reviewers' comments. The manuscript, as well as the codebase, are significantly updated after taking the feedback from the reviewers into account, in particular, figure 3 is a useful addition in the manuscript and it showcases the performance of ELEPHANT on diverse datasets. A systematic comparison between ELEPHANT and StarDist 3D is also useful to evaluate the performance comparison.

However, the limited performance of ELEPHANT on segmentation tasks is expected since the method is limited to detect ellipsoid shape-based objects but since the method is focused on only detection and tracking so it would be useful to state it clearly in the abstract and manuscript. This will help the users to get a better idea about the strengths and limitations of the toolbox in advance. Overall the study seems to be in much better shape now.

Reviewer #2 (Recommendations for the authors):

Thank you for the really great improvements to usability. I was able to easily install Elephant and Mastodon through Fiji. The google colab server setup took around 30 minutes to get started – I'm not sure if there's any way to make it faster, but wanted to point it out. After that I tried to "add port forward" and received a "Connection refused" error, there was no pop up to input my password. Is there another step with rabbitMQ permissions perhaps that I'm missing?

Thanks for also running StarDist on one of the frames. Can you please add quantitative metrics to Supplementary Figure 8? Maybe they are somewhere but I missed them and apologies if I did. Given StarDist does not have temporal information, it is likely that Elephant outperforms StarDist, but it would be good to include the quantitative results for the reader to be able to decide whether to use StarDist or Elephant. Thanks for the information about how stardist+trackmate are only in 2D.

Reviewer #3 (Recommendations for the authors):

First of all we would like to congratulate the authors for doing a great job in addressing the issues that we have raised in the previous review. As a result the software is in our view now much more user friendly; for example connecting from the Fiji user interface to the deep learning server is a great improvement as compared to the previous command line based way.

However, in practice we still struggled to reliably work with the Google Colab server and we feel that this might be a source of frustration for the potential users of the software. In the previous version of the software the authors also presented another solution (i.e. a local server), given that the users would have a computer with an appropriate GPU. Maybe one could reconsider those ideas?

We are also wondering, given the advances in running deep learning models in Java (DeepImageJ and CSDBDeep) whether a fully Java based (i.e. one Fiji plugin) solution would be feasible to make this great tool more user friendly and stable? We know that this would not solve the issue of providing the GPU resources, but maybe users would then simply need to have a computer with a GPU (which we think could be "fair enough").

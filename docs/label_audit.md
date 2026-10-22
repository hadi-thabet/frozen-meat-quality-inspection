\# Label audit



Manual check of images that have no labelled boxes, done by looking at each image.

Categories: defect-free, defect visible (label probably missing), unclear.



\## Training set (30 random unlabelled images, seed 0)

\- Defect-free: 25

\- Defect visible: 2

&#x20; - frame\_with\_red\_4222 (unsealed)

&#x20; - frame\_with\_red\_8326 (packaging-error)

\- Unclear: 3 (all on the border between defect-free and packaging-error)



Note: unsealed vs sealed was always clear. The packaging-error class looks

more subjective, since there is no sharp threshold for "meat too close to

the edge".



\## Validation set (all 14 unlabelled images)

\- Defect-free: 12

\- Defect visible: 2 (file names: frame\_with\_red\_4704\_jpg.rf.80cecf14c626b6a221d917bfb6f405c2, frame\_with\_red\_6496\_jpg.rf.87e72288446b3dd379425dfe570336d9  )

\- Unclear: 0



\## Test set (all 12 unlabelled images)

\- Defect-free: 11

\- Defect visible: 1 (file name: frame\_with\_red\_7471\_jpg.rf.d9733c9a3c8e75ec75d4c6c9f744a199)

\- Unclear: 0



\## What this means

The labels are quite reliable but not perfect. In the audit, 2 out of the 30 sampled unlabelled training images and 2 out of the 14 validation images and 1 out of the 12 test images showed a clear unsealed defect or a subjective packaging error defect. These all had no labels. This meant that some defective trays would've been recorded as defect- free. Every miss that I found myself manually was an unsealed or packaging error defect. The ambiguous images sat on the border between defect-free and packaging-error, which suggests that class is the most subjective to label. These errors will likely underestimate the precision of the algorithm., because a correct detection on a missed defect counts as a false positive, and they will make some tray level fail predictions look wrong when they are actually correct. I will keep the original labels as the official benchmark and also report results with the three affected validation and test images excluded, so the effect of label noise can be seen directly.




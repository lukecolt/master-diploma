# master-diploma

The main objective of this study was
to conduct comparative research on deep learning algorithms used in cytological diagnostics
for the classification of tumor changes and to develop an image registration system (using IoT
devices) that can be mounted on any optical microscope. Four deep learning methods were
proposed: a custom CNN, VGG-16, ResNet-50, and Vision Transformer, which were trained
and verified on a diverse dataset authored by Prof. Md. Maria Chosia from the Department of
Pathomorphology at Pomeranian Medical University in Szczecin. These methods were adapted
for the task through data augmentation, the addition of layers, and the use of transfer learning
(for ResNet-50 and VGG-16). The results of the experiments showed that the VGG-16 model
performed best, achieving an average accuracy of 86.3% on the test set. The VGG-16 network
also achieved the best results for other metrics: average F1 score, average sensitivity, and
average precision, with values of 84%, 83.7%, and 85.7% respectively. Additionally, the Vision
Transformer model had the fastest training time, while the custom CNN-based model had
the fewest parameters. Considering the small number of images in the dataset, the results
are satisfactory. For future work, the methods should be tested on a larger dataset and
using more advanced image augmentation techniques. It is also worth exploring other model
architectures. The algorithms were also tested on images captured by the developed image
registration system on an optical microscope. This system enables manual data collection for
future research purposes.


# Workshop Abstract
Our understanding of modern neural networks lags behind their practical successes.
As this understanding gap grows, it poses a serious challenge to the future pace of progress because fewer pillars of knowledge will be available to designers of models and algorithms.
This workshop aims to close this understanding gap in deep learning.
It solicits contributions that view the behavior of deep nets as a natural phenomenon to investigate with methods inspired from the natural sciences, like physics, astronomy, and biology.
We solicit empirical work that isolates phenomena in deep nets, describes them quantitatively, and then replicates or falsifies them.

As a starting point for this effort, we focus on the interplay between data, network architecture, and training algorithms. We are looking for contributions that identify precise, reproducible phenomena, as well as systematic studies and evaluations of current beliefs such as “sharp local minima do not generalize well” or “SGD navigates out of local minima”. Through the workshop, we hope to catalogue quantifiable versions of such statements, as well as demonstrate whether or not they occur reproducibly.



# Confirmed Speakers
- [Konrad Kording](http://koerding.com/) (University of Pennsylvania)
- [Aude Oliva](http://cvcl.mit.edu/) (MIT)
- [Benjamin Recht](https://people.eecs.berkeley.edu/~brecht/) (UC Berkeley)
- [Olga Russakovsky](http://www.cs.princeton.edu/~olgarus/) (Princeton University)
- [Andrew Saxe](http://decisions.psy.ox.ac.uk/people/saxe_site/) (University of Oxford)
- [Nati Srebro](https://ttic.uchicago.edu/~nati/) (TTI Chicago)
- [Christian Szegedy](https://ai.google/research/people/ChristianSzegedy) (Google Brain)


# Schedule

TBD


# Call for Papers and Submission Instructions

We hope to elicit experimental work of the following character as part of this workshop:

- **Interesting and unusual behaviour observed on deep nets:** Data, architecture, and optimization can give rise to any number of curious behaviours in deep learning. We hope to collate and characterize observations about such behaviours. “Interesting” and “unusual” are subjective, but any result that is carefully studied -- whether it violates or supports intuition and folklore -- is welcome. The phenomenon should be defined in a (mathematically) unambiguous way. For example, if the phenomenon is about “internal covariate shift” or “sharpness of a local minimum”, the submission should present quantifiable candidate definitions of these quantities.


- **Using sufficiently large and well-known models and datasets:** A common but fair criticism of new research is that results are reported on only MNIST. We request experiments to be run on the largest model and dataset that are appropriate for the phenomenon of interest (e.g., well-known published models such as Resnet-50, Inception V3, etc). More concretely, we prefer large, standard datasets such as ImageNet or LibriSpeech. CIFAR-10 is appropriate for phenomena with heavy computational demands, or in a study of the scaling behavior of deep nets as the size of the dataset varies, when it is paired with at least one other large dataset. We discourage the reporting of results which have been demonstrated only on MNIST. Toy models (1-hidden layer MLP) on synthetic datasets are appropriate for isolating a phenomenon once it has been observed in a realistic setting. 


- **Reproducible:** The phenomena should be easy to reproduce by the community. We are looking for phenomena that occur when the  experiment is run many times, across diverse models and datasets. We encourage the use of standard statistical tools (hypothesis testing, confidence intervals, etc) to demonstrate the extent and significance of phenomena. We also encourage submissions to release code, and statistical analysis in Jupyter notebook format.


- **Isolated and analyzed:**  We prefer small and easy to describe phenomena over complex ones for which only vague descriptions are offered. Phenomena should be stated precisely and in a quantifiable way. E.g., “using residual connections reduces the sensitivity of training procedure to parameter initialization”, “reduces”, “sensitivity”, and “residual connections” should be made precise, e.g., the percentage of runs that successfully train after random gaussian initialization.


We specifically **do not** require the phenomenon to be novel. We value instead a formalization of the phenomenon, followed by reliable evidence in support for it, or a thorough refutation of it.
We especially welcome work that carefully characterizes the limits of the phenomenon observed, and show that it only occurs under specific conditions and settings.
We do not require an explanation of _why_ a phenomenon might occur, only demonstrations that it does so reliably (or refutations).
We hope that the catalogue of phenomena we accumulate will be embraced as a starting point for a better understanding of deep learning.



# Important Dates
- Submission Deadline: TBD
- Notification: TBD
- Workshop: June 14th or 15th, 2019

# Organizers
- [Samy Bengio](https://bengio.abracadoudou.com/) (Google Brain)
- [Kenji Hata]() (Google)
- [Aleksander Mądry](https://people.csail.mit.edu/madry/) (MIT)
- [Ari Morcos](http://www.arimorcos.com/) (Facebook AI Research)
- [Behnam Neyshabur](https://www.neyshabur.net/) (NYU)
- [Maithra Raghu](http://maithraraghu.com/) (Cornell University and Google Brain)
- [Ali Rahimi]() (Google)
- [Ludwig Schmidt](http://people.csail.mit.edu/ludwigs/) (UC Berkeley)
- [Hanie Sedghi]() (Google Brain)
- [Ying Xiao](https://ai.google/research/people/YingXiao) (Google)

Please email icml2019phenomena@gmail.com with any questions.

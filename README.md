# Workshop Abstract
Our understanding of modern neural networks lags behind their practical successes.
This growing gap poses a challenge to the pace of progress in machine learning because fewer pillars of knowledge are available to designers of models and algorithms.
This workshop aims to close this understanding gap.
We solicit contributions that view the behavior of deep nets as natural phenomena, to be investigated with methods inspired from the natural sciences like physics, astronomy, and biology.
We call for empirical work that isolates phenomena in deep nets, describes them quantitatively, and then replicates or falsifies them.

As a starting point for this effort, we focus on the interplay between data, network architecture, and training algorithms. We seek contributions that identify precise, reproducible phenomena, and studies of current beliefs such as “sharp local minima do not generalize well” or “SGD navigates out of local minima”.
Through the workshop, we hope to catalogue quantifiable versions of such statements, and demonstrate whether they occur reliably.



# Confirmed Speakers
- [Konrad Kording](http://koerding.com/) (University of Pennsylvania)
- [Aude Oliva](http://cvcl.mit.edu/) (MIT)
- [Benjamin Recht](https://people.eecs.berkeley.edu/~brecht/) (UC Berkeley)
- [Olga Russakovsky](http://www.cs.princeton.edu/~olgarus/) (Princeton University)
- [Andrew Saxe](http://decisions.psy.ox.ac.uk/people/saxe_site/) (University of Oxford)
- [Nati Srebro](https://ttic.uchicago.edu/~nati/) (TTI Chicago)
- [Christian Szegedy](https://ai.google/research/people/ChristianSzegedy) (Google)


# Schedule

_To be announced_


# Call for Papers

We solicit the following kind of experimental work:

- **Interesting and unusual behaviour observed in deep nets:**
Interactions between datasets, architecture, and optimization procedures can give rise to curious behaviors in deep learning.
“Interesting” and “unusual” are subjective, but any result that is carefully studied - whether it violates or supports intuition and folklore - is welcome.
The phenomenon should be defined in a (mathematically) unambiguous way.
For example, if the phenomenon is about “internal covariate shift” or “sharpness of a local minimum”, the submission should present quantifiable candidate definitions of these quantities.


- **Using sufficiently large and well-known models and datasets:**
We request that experiments to be run on the largest model and dataset that are appropriate for the phenomenon of interest. 
We prefer well-known published models such as Resnet-50 or Inception V3 and large, standard datasets such as ImageNet or LibriSpeech.
CIFAR-10 is appropriate for phenomena with heavy computational demands, or in a study of the scaling behavior of deep nets as the size of the dataset varies, when CIFAR-10 is paired with at least one other large dataset.
We discourage results that have been demonstrated only on MNIST.
Toy models (1-hidden layer MLP and the like) on synthetic datasets are appropriate for isolating a phenomenon once it has been observed in a realistic setting. 


- **Reproducible:** The phenomenon should be easy to reproduce by the community.
We seek phenomena that occur when the  experiment is run many times, across diverse models and datasets.
We encourage a thorough statistical analysis of the experiments to demonstrate the extent and significance of a phenomenon.
We also encourage submissions to release code, and statistical analysis in Jupyter notebook format.


- **Isolated and analyzed:**  We prefer small and precisely described phenomena over complex ones with imprecise descriptions.
Phenomena should be stated in a quantifiable way.
For example, when stating that “residual connections reduce the sensitivity of training procedures to parameter initialization”, the terms “reduce”, “sensitivity”, and “residual connections” should be defined explicitly.


We specifically **do not** require the phenomenon to be novel. We value instead a formalization of the phenomenon, followed by reliable evidence to support it or a thorough refutation of it.
We especially welcome work that carefully characterizes the limits of the phenomenon observed, and show that it only occurs under specific conditions and settings.
We do not require an explanation of _why_ a phenomenon might occur, only demonstrations that it does so reliably (or refutations).
We hope that the catalogue of phenomena we accumulate will serve as a starting point for a better understanding of deep learning.

## Submission Instructions

Please submit your paper through OpenReview: [https://openreview.net/group?id=ICML.cc/2019/Workshop/Deep_Phenomena](https://openreview.net/group?id=ICML.cc/2019/Workshop/Deep_Phenomena).

The main part of a submission should be at most **4 pages** long. These first four pages should contain a definition of the phenomena of interest and the main experimental results. There is no space limit for references, acknowledgements, and details included in appendices.

Papers should be formatted with at least a 10 pt font, standard line spacing, and a 1 inch margin.
We do not require a specific formatting style beyond these constraints.

We welcome all unpublished results and also papers that were published in 2018 or later.
Submission must be anonymized.


# Important Dates
- Submission Deadline: May 5, 2019 (11:59 pm PST)
- Notification: May 30, 2019 (early notification available upon request)
- Workshop: June 15th, 2019

# Organizers
- [Samy Bengio](https://bengio.abracadoudou.com/) (Google)
- [Kenji Hata]() (Google)
- [Aleksander Mądry](https://people.csail.mit.edu/madry/) (MIT)
- [Ari Morcos](http://www.arimorcos.com/) (Facebook)
- [Behnam Neyshabur](https://www.neyshabur.net/) (NYU)
- [Maithra Raghu](http://maithraraghu.com/) (Cornell University and Google)
- [Ali Rahimi]() (Google)
- [Ludwig Schmidt](http://people.csail.mit.edu/ludwigs/) (UC Berkeley)
- [Hanie Sedghi](https://ai.google/research/people/HanieSedghi) (Google)
- [Ying Xiao](https://ai.google/research/people/YingXiao) (Google)

Please email [icml2019phenomena@gmail.com](mailto:icml2019phenomena@gmail.com) with any questions.

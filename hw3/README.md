## Problem Set 3

### Question 1

The CIFAR-10 dataset analysis can be found in the following jupyter notebook: ```CIFAR10_Analysis.ipynb```:  
- dataset read in using two methods
  - dictionary with data array (I performed a manual transformation to view the image). 
  - keras pre-loaded package
- training/testing split is approximately 80-20 (50,000 / 60,000). 
- scale the data from 0 to 1 (divide by maximum 255 for RGB scale). 
- perform dimension reduction
  - PCA  
  - SVD  
  - NMF  

**Bonus 1 and 2**

Here is a visualization on how these three methods are different. Note that only two components are used for a 2D comparison.  

PCA extracts important components from a large set of variables by calculating and ranking the importance of features/dimensions by using SVD. Therefore, since SVD is also a method used on covariance matrix to calculate and rank the importance of the features, PCA is the truncated SVD method on centered data, hence why the visuals appear similar. In comparison to PCA which captures components by variance explained, the NMF method essentially selects metafeatures that represent the main characteristics of the whole dataset.  

![] (images/question1.png?raw=true "PCAvSVDvNMF")

Finally, when it comes to extracting better features, there are a multitude of other methods such as:  
- ICA (independent component method) which assumes each sample of data is a mixture of independent features and aims to find independent components  
- LDA (linear discriminant analysis) which reduces the number of input variables through a supervised method  
- LLE (locally linear embedding) which reduces dimensions while preserving geometric features of the original non-linear feature structure  
- AE (autoencoders) which uses a speical neural network which is trained to copy input to the output

In addition to some of these specific methods, my main recommendation would be to explore supervised dimension reduction techniques since we are given the labels for each image in the CIFAR-10 dataset. This might allow us to narrow in on some patterns that the unspervised methods cannot pick up on.  

### Question 2

Below is a dataframe containing the averaged precision, recall, f1-score, and accuracy of all four classifiers:  
- Linear SVC
- Logistic Regression Classifier
- K-nearest Neighbors Classifier
- Perceptron  
In general, it appears that the linear support vector classification performs the best with over 50% for all metrics. 

![](images/question2.png?raw=true "VariousMetrics")

*Note*: The prediction arrays of all four classification methods can be found in the ```results``` directory under their respective model names.  

### Question 3

Due to limited computing, I was unable to perform a large grid search for all possible dimensionality reduction and model selection hyper-parameters. Therefore, in the ```CIFAR10_Analysis.ipynb``` notebook, you will find the code to run smaller grid searches such as:   
- optimal PCA/SVM components with Linear SVC hyper-parameter search   
- optimal hyper-parameters for Linear SVC only   
- optimal PCA/SVM components with Logistic Regression hyper-parameter search   
- optimal hyper-parameters for K-nearest neighbors   
- optimal hyper-parameters (eta0- 0.0001, 0.001, 0.01, 0.1, 1.0) for perceptron   

Unfortunately, my computer does not have the computational power to run the above grid searches. I left the first grid search running for nearly 8 hours over night but my computer crashed and did not reboot until 13 hours later. Out of caution, I did not proceed to run any following code and was not able to fine tune the hyper-parameters for both dimension reduction and classification models.

**The best pipeline would result in significantly lower averaged precision, recall, f1-score, and accuracy for the test data because the tuned hyper-parameters would result in an overfit model. So while a grid search would improve these various metrics for the training data, if the goal is to build a more consistent model for new data, then a grid search is not going to be the most effective method.**

### Extra Credit 1

In the ```ExtraCredit.ipynb``` file, the OpenCv library is utilized to perform various transformations on images in the CIFAR-10 test dataset. The following images can be found in the **images/opencv** directory:  

**Original Image**  
![](images/opencv/original.png?raw=true "Original")
**Vertical Shift**  
![] (images/opencv/vertical.png?raw=true "Vertical")
**Horizontal Shift**  
![] (images/opencv/horizontal.png?raw=true "Horizontal")
**90 Degree Rotation**   
![] (images/opencv/90.png?raw=true "90 degree rotation")
**180 Degree Rotation**   
![] (images/opencv/180.png?raw=true "180 degree rotation")
**270 Degree Rotation**   
![] (images/opencv/270.png?raw=true "270 degree rotation")
**Diagonal Shift**   
![] (images/opencv/diag.png?raw=true "Diagonal Shift")

### Extra Credit 2

Also located in the ```ExtraCredit.ipynb``` file, you will find a text mining example using the *nltk* package and a training subset of the *newsgroup* dataset, saved as *20_newsgroup.csv* in the **hw3** directory. Before cleaning the tokens in this corpus, we have a total of 3,056,183 unique words. Once we remove punctuation, stop words, infrequent words (in less than 5 documents), and perform stemming, we have 445,000 terms remaining. Finally, we report the top 10 words with the highest TF-IDF values averaged over all documents belonging to each class. Here is one example:

![] (images/ec.png?raw=true "Extra Credit Example")
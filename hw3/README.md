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

![](images/question1.png?raw=true "PCAvSVDvNMF")

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

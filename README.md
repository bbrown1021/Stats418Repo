# UCLA Masters of Applied Statistics - Stats 418

Britney Brown (505-119-082)

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

![](hw3/images/question1.png?raw=true "PCAvSVDvNMF")

Finally, when it comes to extracting better features, there are a multitude of other methods such as:  
- ICA (independent component method) which assumes each sample of data is a mixture of independent features and aims to find independent components  
- LDA (linear discriminant analysis) which reduces the number of input variables through a supervised method  
- LLE (locally linear embedding) which reduces dimensions while preserving geometric features of the original non-linear feature structure  
- AE (autoencoders) which uses a speical neural network which is trained to copy input to the output

In addition to some of these specific methods, my main recommendation would be to explore supervised dimension reduction techniques since we are given the labels for each image in the CIFAR-10 dataset. This might allow us to narrow in on some patterns that the unspervised methods cannot pick up on.  

## Problem Set 1

### Segment 1

A screenshot of this repository's gitignore can be found in the q1 directory. 

**Bonus question:** In theory, branching off the ```hw1``` branch for each individual segment q1, q2, etc. would allow for the commits of each branch and corresponding question to appear in order when merged back onto the hw1 branch.  

### Segment 2

The 'Hello World' Flask project is deployed here: http://stats418hello505119082world.azurewebsites.net/. The app code can be found in q2 along with the submodule used to deploy to Azure. 

### Segment 3

After installing VirtualBox 6.1 on my Mac OS, I then setup a Linux environment using the latest LTS version of Ubuntu. 

![](hw1/q3/VirtualBox_screenshot.png?raw=true "VirtualBox_setup")
![](hw1/q3/screenshot.png?raw=true "Linux_environment"). 

In the Linux command line, ```./setup.sh``` will install all necessary packages. A copy of this script can be found in q3 directory. 

### Segment 4

Inside q4 directory, **Command Line:**  
``` python3 main.py```

**Output:**
- successful connection to SQL database  
- successful transformation into pandas dataframe  
- **Answers:**  
4.1 - Store 2  
4.2 - 2017-11-07  
4.3 - 2019  
4.4 - Store 2  
4.5 - Store 7   
- successful creation of new csv file in q4 directory
- successful creation of plot in q4 directory

### Segment 5

***Section 5.1***  
``` df_reshape.py``` reshapes the original ```TV-Sales.csv``` file  into ``` clean_TV_sales.csv``` to match the sales schema defined in ```create.sql```

Inside q5 directory, **Command Line:**  
``` python3 df_reshape.py```  
``` sqlite3 < create.sql```

**Output:**
- db.sqlite3 database in the hw1 directory

***Section 5.2-5***  
Inside q5 directory, **Command Line:**
``` sqlite3 < queries.sql```

**Output:**
- schema for stores table
- schema for sales table
- **Answers:**  
5.2 - Store 2   
5.3 Stores 8, 9, and 10   
5.4 -  Store 2  
5.5 - 37th week of the year   

### Segment 6  

```main.py``` utilizes the example input 2D arrays found in ```data.py``` which can be opened and customized by user

Inside q6 directory, **Command Line:**  
``` python3 main.py```

**Output:**  
- all numpy arrays for the main assignment
- all numpy arrays for the ***bonus assignments*** including
  - a new file ```input_array.npy``` of the current example array in q6 directory

## Extra Credit

### Segment 7

Due to my music background, I chose the following Kaggle dataset (https://www.kaggle.com/vageeshabudanur/songdetails) which contains songs from the 1990-2010 top 10 of the Billboard Hot 100 as well as songs that did not make the list (for comparison). Some variables include artist, time signature, loudness, key, pitch, tempo, and timbre. In the q7 directory, you will find the data under ```songs.csv``` and an extensive EDA in the notebook ```musicEDA.ipynb```.

### Segment 8

Navigate to the q8 directory for the TV sales analysis performed in R which includes all questions/queries from segments 4 and 5, as well as the bonus plot from segment 4. The notebook can be viewed at ```R_extra_credit.Rmd``` and the rendered document is viewable at ```R_extra_credit.pdf```. Note that a dataset with imputed missing values was generated under the name ```repaired.csv``` and the extra credit plot is saved at ```extra_plot.jpeg``` as well.

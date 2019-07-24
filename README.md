# COE125-E02-Group03-DoE-ObjectClassifier
The group would like to create a program that will be able to determine a card's rank and suit from the cards in a standard deck as shown in Figure 1. Accordingly, the group would also like to create a program that will use a web camera to serve as the input device where the information coming from this device will be processed in order to achieve the first objective of the program.  

The creators of this project would like to attain the following goals: 

To determine the value of cards detecting instances of objects from a particular class in an image 
To be able to know and construct a system model for an object class from a set of training examples. 

## Scopes: 

The program will be able to detect the card's rank. 
The program can only detect cards from a live preview from a web camera. 

 

## Delimitations:  

The program does not allow images as inputs. 
The program cannot detect the colors in a card. 
The program cannot detect the suit of the card. 

The following are the basic fundamental requirements needed in the project which is divided into two kinds of requirements, those being the interface requirements and regulatory requirements, respectively: 

  

## Interface Requirements 

1. Accepts images as an entry. 
2. Can detect the name of the deck of cards. 
3. Label the deck of cards with its accurate name. 

  

## Regulatory Requirements 

1. The card detector will limit the image used to a readable quality. 
2. The text file will contain labels for detection. 

### The following are the basic non-fundamental requirements that are needed to be satisfied for the said program: 

 

## Web camera requirements: 

The clarity which the camera will be able to detect the given image. 
Stable and non-moving/blurred image will be required. 
Specific resolution of the camera enables higher performance in image detection 

In installing the tensorflow 
The following are the basic non-fundamental requirements that are needed to be satisfied for the said program: 


Install a anaconda prompt then check the version using  
> python –version 

## In our python version could be Python 3.5.6 :: Anaconda 4.2.0 (64-bit) 

### Step 1:


Install CUDA and CUDNN. Cude is a parallel computing platform and programming model developed by Nvidia for general computing on its own GPUs (graphics processing units). CUDA enables developers to speed up compute-intensive applications by harnessing the power of GPUs for the parallelizable part of the computation.


### Step 2: 

Download the package of Tensorflow using the command prompt or directly download the package from the site using these commands
>pip3 install -U pip virtualenv
>pip3 install --user --upgrade tensorflow  

then after installing, check the version of your packages.
>python3 --version
>pip3 --version
>virtualenv --version

Activate the environment
> activate tensorflow1

(tensorflow) C:\>python -m pip install --upgrade pip

### Step 3: 

Download the following packages in your command prompt windows or ubuntu.

> conda install -c anaconda protobuf
> pip install pillow
> pip install lxml
> pip install Cython
> pip install contextlib2
> pip install jupyter
> pip install matplotlib
> pip install pandas
> pip install opencv-python

Pandas and opencv-python are used for the feed of the webcam real-time.

### Step 4:

After downloading the packages, follow these instruction for setting up the path for the tensorflow.


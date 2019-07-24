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

### CUDA

![GetImage (3)](https://user-images.githubusercontent.com/50915438/61794995-06243480-ae55-11e9-92df-e6288a46f727.jpg)

### CUDNN

![GetImage (4)](https://user-images.githubusercontent.com/50915438/61794994-06243480-ae55-11e9-8776-baab4643a206.jpg)




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

![GetImage](https://user-images.githubusercontent.com/50915438/61794912-d117e200-ae54-11e9-9907-0ff73ede1e9d.jpg)


CLICK THE ENVIRONMENT VARIABLES

![GetImage (1)](https://user-images.githubusercontent.com/50915438/61794997-06bccb00-ae55-11e9-9b23-67e2a04b0cd0.jpg)


Then, go to pythonpath 

![GetImage (2)](https://user-images.githubusercontent.com/50915438/61794996-06bccb00-ae55-11e9-93e7-51191b0fe56f.jpg)

Follow the format

![GetImage (5)](https://user-images.githubusercontent.com/50915438/61795134-4b486680-ae55-11e9-9208-c9c6752cf1c9.jpg)



### Step 5 

After setting up the requirements, type in the directory

>python setup.py build 
>python setup.py install

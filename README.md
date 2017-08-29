[![Datmo Project](https://datmo.io/shabazp/iris-classification/badge.svg)](https://datmo.io/shabazp/iris-classification)

# iris-classification

This is an example of a Datmo Project which uses iris dataset to classify between different flower types. This project tries nearest neighbor and naive bayes algorithms.

The Iris dataset was used in R.A. Fisher's classic 1936 paper and can also be found on the [UCI Machine Learning Repository][1].

It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.

The columns in this dataset are:

 - Id
 - SepalLengthCm
 - SepalWidthCm
 - PetalLengthCm
 - PetalWidthCm
 - Species

  [1]: http://archive.ics.uci.edu/ml/

Check out the Snapshots tab above for information on snapshots that were taken with various parameters. Search and filter them to find the best ones.

Clone this model on your local machine with the Datmo CLI

$ datmo clone https://datmo.io/shabazp/iris-classification

Now you can run the set of commands below to better understand the advantages of converting a repository to a Datmo Project. First you can check out all of the snapshots that have already been created by the user.

$ datmo snapshot ls 

Once you have viewed all of the existing snapshots, you can create your own by simply running the code below which runs the classification training which saves a few key files (the weights file, metrics for this file) in the output directory which creates a new snapshot.

$ datmo task run "python3 classifier.py"

For reference, here are few more quick details about what you can find in the repository.

Dockerfile: this is meant to keep track of your environment. For example, this Dockerfile ensures that our environment has all of the requirements needed to run our model. You can manage, edit, and create new enviroments with the datmo env command. Each session you create with datmo will have a default environment associated with it.

_datmo: visible datmo folder where the input information (data, snapshots, misc files) will go.

_datmo/data: we store any data that you might use for the model. In this case, we are pulling data from a remote server and will populate this directory automatically while training. For other models, you will want to use the datmo dataset command to create, manage, or pull datasets from the remote server

_datmo/snapshots: contains weights, statistics and files(visualizations) that are pulled in to be inputs for processing
The commands and quick reference above is by no means meant to be comprehensive. Please refer to the CLI documentation for more details on the various Datmo commands to use and file structures present in Datmo.

Happy Building :)

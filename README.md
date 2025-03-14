# LMNOP

LMNOP (LLM-based Microbial Metadata Notebook Processing) is a tool presented in the form of a jupyter notebook that allows users to easily clean and summarize metadata fields with support for attributes commonly relevant to microbiome studies, such as summary statistics and visualizations. Users can directly query an LLM within a jupyter notebook in ways that automatically provide context to queries based on the loaded metadata file. With automated improved prompt engineering, obtaining and running code suggestions from ChatGPT is simplified. The notebook also provides functions for anomaly detection and column name correction. Voice recognition is also supported through OpenAI's extremely accurate whisper voice transcription library. Using LMNOP to process metadata is a potential first step in a microbiome data analysis pipeline.

Metadata associated with microbiome samples contains the information necessary for mapping samples and their microbial profiles to characteristics like the environment from which a sample came, time of collection, numerous clinical parameters that describe a patient from which a sample came in human studies, or geographic information in ecology studies. They are thus one of the most important data layers in microbiome data analysis. Metadata is frequently collected by hand and is thus prone to human errors such as misspellings or the addition of trailing white spaces, all of which would lead to erroneous conclusions from metagenomic data. Despite the importance of integral metadata, proper attention to data cleaning is frequently overlooked for two key reasons. First, metadata contains many fields for many samples, making it impossible to inspect by hand, especially with the growing scale of metagenomic studies. Second, comprehensive tools do not exist to thoroughly inspect metadata in the same way that they do for the sequencing data itself. Recent advancements in AI have enabled Large Language Models to perform tasks like parsing and analyzing large bodies of text, however to the best of our knowledge, this technology has not been applied in the space of microbiome metadata validation. Here we present **LMNOP (LLLM-based Microbiome metadata NOtebook Processing)**, a tool for inspecting and correcting common human errors found in microbiome metadata. **LMNOP** integrates calls to ChatGPT into a Jupyter Notebook for streamlined generation of code to clean and manipulate metadata files. It also provides functionality to summarize and visualize all fields in a manner that makes constructing clinical attribute tables in human microbiome studies much simpler by providing summary statistics. Measures in the notebook are taken to ensure the reproducibility of stochastic calls to an LLM. Voice recognition is also supported using whisper, OpenAI’s extremely accurate speech transcription function.

## Inputs

Two things are necessary to have before using the LMNOP notebook:
1) **Metadata file:** Either tab-separated (.tsv) or comma-separated (.csv) file
2) **An OpenAI API Key:** This will allow you to make calls to the LLM. See below.
   
## Installation

To use this notebook, clone the repository and create a new conda environment.
The environment file will set the name of your env to `lmnop`:

```bash
git clone https://github.com/dpear/LMNOP.git
cd LMNOP
conda env create -f environment.yml
```

Then, activate the environment to add a jupyter notebook kernel:
```bash
conda activate lmnop
python -m ipykernel install --user --name lmnop --display-name "Python (lmnop jupyter kernel)"
```

## Using the Notebook with Uncleaned Metadata

First activate the environment, then actiate the jupyter notebook server (please note that you must activate the environment before starting the jupyter notebook server):
```bash
conda activate lmnop
jupyter notebook
```
Navigate to the `tutorial.ipynb` notebook and run to see an example of the different supported summarization and cleaning functions. After interactively making changes to a metadata file, simply save the file as a csv or tsv using `pandas` to use the metadata file in downstream analyses.

## Cells that make a call to the LLM automatically disable themselves
Cells that make a call to the LLM will automatically disable themselves by switching from `code` cell type to `raw` cell type. This is because each call to the LLM may produce different results based on a probabilistic response generating scheme, which is re-trained each time a call is made (imagine asking ChatGPT the same question twice in a row; you would expect to get two similar but different results). Normal jupyter notebook behavior–code behavior in general–maintains that running the same code or cells from top to bottom produces the same result, which would not be the case for calls to the LLM. Unlike `np.random` or similar libraries that rely on stochasticity, there is no way of setting a seed when making calls to the LLM. Thus the notebook saves both the call and the response to the LLM but disables the cells, which is helpful behavior so that **an informative response from the LLM does not get deleted.**

## Re-Enabling cells that make a call to an LLM
If you wish to rerun a cell to re-ask a quesion, cells need only be switched back from `raw` cell type to `code` cell type.  More information can be found at the following resources:
- https://www.geeksforgeeks.org/markdown-cell-in-jupyter-notebook/

## Voice recognition
To enable or disable audio transcription, set `g_use_speech=True` variable in the `tutorial.ipynb` notebook. This will add the speech recognition / Record button to the list of buttons in the notebook and allow you to record speech that will be transcribed and sent as a call to the LLM.


## How to Obtain an API Key from OpenAI

To use OpenAI's API with this project, you will need an API key.
Navigate to OpenAI's Developer Quickstart page for instructions on how to create and export an API key:
https://platform.openai.com/docs/quickstart

#### Troubleshooting:
- If you encounter problems with your API key, it may require setting up an account that has a paid subscription plan. 
- Please see the [OpenAI website](https://platform.openai.com/) for more details.

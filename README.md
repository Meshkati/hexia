# Visual Question Answering with Stacked Attention Networks

<div align="center">

<a href="https://www.python.org/downloads/release/python-360/"> <img src="https://img.shields.io/badge/python-3.6-blue.svg" alt="Python 3.6"/> </a>
<a href="https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=aligholami/Visual-Question-Answering-with-Stacked-Attention-Networks&amp;utm_campaign=Badge_Grade"> <img src="https://api.codacy.com/project/badge/Grade/62aaec49f9294a46a74c65dacf599a37" alt="Codacy Badge"/> </a>

</div>

In this project, we will analyze different methods for building a VQA systems. Our goal is to first produce promising results with basic archtiectures and then develop the model to a degree in which **reasoning** is being done at its best possible state.

## Baseline 1

In this section, we initially implement a VQA model with the following characteristics:

1. Extraction of image feature maps with a VGG-16 convolutional architecture.
2. Averaging embedding scores of words in a question.
3. Concatenating image feature maps and averaged embedding scores.
4. Classifying the obtained inputs from step 3 with answers as labels using a multi-layer perceptron.
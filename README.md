# Plant-Seedlings-Classification
Plant Seedlings Classification competition

The images were resized to 224x224. Then, employing trasfer learning, and then finetuning the network. 

<p align="center">
<img src="https://github.com/camilo1704/Plant-Seedlings-Classification/blob/master/xcep1_.png" alt="alt text" width="640" >
</p>
Training 2 blocks and freezing the others generalize better than just training the last block. Values of the L2 constant bigger than 0.1 destabilize the learning process.

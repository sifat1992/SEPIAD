
#Attention Enhanced Perceptual Image Anomaly Detection for Ultrasound Imagery

# Key features
> Perceptual Autoencoders
> Semi-supervised learning
> Anomaly detection
> Ultrasound Imagery

#Abstract
This paper proposes a novel model, SEPIAD, with an integration of the Squeeze and Excitation attention block into the architecture of the Perceptual Image Anomaly Detection model, PIAD. The dataset used in this work consisted of 2813 images, with 2014 normal and 799 abnormal images of abdominal organs, curated from 242 patients at MH Samorita Hospital and Medical College in Dhaka, Bangladesh. Perceptual Image anomaly
Detection (PIAD) leverages adversarial losses and perceptual losses trained solely on normal images. To enhancethis framework, we have proposed a lightweight architecture, SEPIAD, using the Squeeze and Excitation (SE) blocks to focus more on the important feature channels, enhancing anomaly detection on ultrasound images without raising the model complexity. After training, the proposed model, SEPIAD, calculates the abnormality
of the input image as the perceptual dissimilarity between it and the closest generated image of the modeled data distribution. SEPIAD outperformed the baseline model, PIAD, achieving a Receiver Operating Characteristic Area Under the Curve (ROC AUC) of 0.95, outperforming the baseline model by at least 8%, proving the
model’s effectiveness in Ultrasound image analysis, which has an inherently noisy structure, low contrast, and subtle organ boundaries.

# Dataset
> Custom curated Ultrasound dataset.
> Not publicly available due to sensitivity and privacy constraints.
> Contact for access if needed for research colloboration. 

### Dataset Breakdown

<p align="center">
  <img src="Results/git1.png" alt="Comparison Table" width="600"/>
</p>

# Project sturcture
```
├── assets/                         # Folder containing sample dataset images
│   ├── healthy_example1.png
│   ├── abnormal_example1.png
├── Results                         # Folder containing images of results
│   ├── git1.png
│   
├── pg_decoders.py                      # Training and evaluation using AlexNet
├── pg_encoders.py                    # Training and evaluation using DenseNet121
├── evaluate.py           # Training and evaluation using ResNet50
├── latent_dis.py             # Training and evaluation using VGG16
├── latent_model.py         # Training and evaluation of custom CNN
├── optimizer.py                  # Custom CNN with Learnable 2D Gaussian layer
├── train.py    # Script defining the learnable 2D Gaussian layer
├── utils.py               # Dataset loading and preprocessing
├── Attn_models.py               # Dataset loading and preprocessing
├── layers.py               # Dataset loading and preprocessing
├── pg_networks.py               # Dataset loading and preprocessing
└── .gitignore                      # Specifies files and folders to be ignored by Git
├── README.md                       # Reading this!
```
#References
1. Nina Tuluptceva, Bart Bakker, Irina Fedulova1, Anton Konushin
   “PERCEPTUAL IMAGE ANOMALY DETECTION.” [arXiv:1909.05904](https://arxiv.org/pdf/1909.05904) 


# Author
- **Sifat Z. Karim** — Graduate Student, Mississippi State University  
  📧 [sifatzinakarim1992@gmail.com](mailto:sifatzinakarim1992@gmail.com)  
  🧑‍💻 GitHub: [@sifat1992](https://github.com/sifat1992)

## Contact

For questions, suggestions, or collaboration opportunities, feel free to reach out!  
I’m happy to receive feedback and open to connecting with fellow researchers.


---


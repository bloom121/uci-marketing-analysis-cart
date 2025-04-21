<table align="center">
    <tr>
    <th align="center"> Toretsk (Ukraine, April 2025)</th>
    </tr>
    <tr>
    <td>
    <img src="./images/Toretsk-2025.jpg"  alt="What remains of Toretsk, Ukraine, April 2025" width="100%" >
    </td>
    </tr>
</table>

[...](https://www.reddit.com/r/UkraineRussiaReport/comments/1k2d20a/ua_pov_birdseye_view_of_what_remains_of_toretsk/)

## The UCI Bank Marketing Campaign Decision Tree Analysis

This project analyzes [the UCI Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing) using CART to predict customer subscription (a binary variable). A conversion rate is the average of the subscription value for a chosen data subset (market segment).

## Python3 and miniconda (Ubuntu 22.04)

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

The last step of miniconda (155MB) install: "Do you wish to update your shell profile to automatically initialize conda?" I have chosen "No", and simply initialize it manually:

```bash
source /home/tokyo/miniconda3/etc/profile.d/conda.sh
```

## Dependencies

Environment: 

```bash
conda create -n banktree
conda info --envs

# conda environments:
#
base                   /home/tokyo/miniconda3
banktree               /home/tokyo/miniconda3/envs/banktree

conda activate banktree
```

Dependencies:

```bash
conda install python=3.13
conda install pandas scikit-learn
conda install -c conda-forge ucimlrepo certifi 
conda install requests tabulate
```

Exit and removal:

```bash
conda deactivate
conda env remove --name banktree
rm -rf /home/tokyo/miniconda3/envs/banktree
conda clean --all
```

## Grok

"Give me the script which loads the UCI Bank Marketing Dataset, splits 20% into testing, builds CART, outputs training set sample number, accuracy, conversion rate, same for testing. Also, output top ten groups based on job and education with highest conversion rates and show sample numbers, nothing else."

```bash
python main_grok.py
Training set:
  Sample number: 36168
  Accuracy: 1.0000
  Conversion rate: 0.1161

Testing set:
  Sample number: 9043
  Accuracy: 0.8734
  Conversion rate: 0.1206

Top 10 groups based on job and education with highest conversion rates:
          Job Education  Conversion Rate  Sample Number
      student   primary         0.363636             44
      student secondary         0.297244            508
      retired  tertiary         0.275956            366
      student  tertiary         0.264574            223
      retired   primary         0.223899            795
      retired secondary         0.210366            984
   unemployed  tertiary         0.193772            289
       admin.  tertiary         0.173077            572
  blue-collar  tertiary         0.161074            149
self-employed  tertiary         0.160864            833

```

## deepseek

"Give me the script which loads the UCI Bank Marketing Dataset, splits 20% into testing, builds CART, outputs training set sample number, accuracy, conversion rate, same for testing. Also, output top ten groups based on job and education with highest conversion rates and show sample numbers, nothing else."

"The link is https://archive.ics.uci.edu/static/public/222/bank+marketing.zip, and it's a zip file, not csv! Inside bank+marketing.zip there are bank.zip and bank-additional.zip. Inside bank.zip there is bank.csv (around 460 KB), bank-full.csv (around 4.6MB) and bank-names.txt 3.9 KB. Inside bank-additional.zip there is bank-additional folder inside it bank-additional.csv (around 584KB), bank-additional-full.csv (~5.8MB), and bank-additional-names.txt (~5.5KB)."

```bash
python main_deepseek.py
Training Set
Samples: 32,950
Accuracy: 100.00%
Conversion Rate: 11.24%

Testing Set
Samples: 8,238
Accuracy: 88.69%
Conversion Rate: 11.35%

Conversion Rate Ranges:
Max: 35.35%
Min: 18.64%

Top 10 Job/Education Groups:
|                                      |   Conversion_Rate |   Samples |
|:-------------------------------------|------------------:|----------:|
| ('student', 'basic.9y')              |          0.353535 |        99 |
| ('student', 'unknown')               |          0.353293 |       167 |
| ('retired', 'unknown')               |          0.336735 |        98 |
| ('student', 'high.school')           |          0.319328 |       357 |
| ('retired', 'basic.4y')              |          0.309883 |       597 |
| ('retired', 'professional.course')   |          0.236515 |       241 |
| ('retired', 'university.degree')     |          0.231579 |       285 |
| ('retired', 'high.school')           |          0.224638 |       276 |
| ('student', 'university.degree')     |          0.205882 |       170 |
| ('housemaid', 'professional.course') |          0.186441 |        59 |

```

## Notes

* As Leo Breiman has noted himself in 2001, CART is not the most accurate method.

* CART is great in that it handles any data (missing, mixing continuous with nominal), and is automatic. It is also fast: no inverses, no learning, no GPUs needed. Ideal for rough estimates.

* I would not spend too much time on the generated trees, clusters/rules, variable importance.

* pip is horrible, but conda solves the problem. Jupyter Notebook is not that useful.

* ChatGPT, deepseek, and Grok are great for such scripts, but one needs to debug/iterate.

* [Artiom Kovnatsky](https://www.artiomkovnatsky.com/) uses CART in real-world commercial projects.
   
## References 

[A Conversation with Leo Breiman (2001)](https://projecteuclid.org/journals/statistical-science/volume-16/issue-2/A-Conversaton-with-Leo-Breiman/10.1214/ss/1009213290.full)        
   

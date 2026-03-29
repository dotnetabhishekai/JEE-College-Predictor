# 🎓 JEE College Predictor

A Streamlit app that predicts your best-fit engineering colleges based on your JEE Advanced or JEE Mains rank, preferred streams, and reservation category.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red)
![Plotly](https://img.shields.io/badge/Plotly-5.18%2B-purple)

---

## Features

### Exam Support
- JEE Advanced — predicts IIT admissions
- JEE Mains — predicts NIT, IIIT, and GFTI admissions

### College Database
| Type | Count | Examples |
|------|-------|---------|
| IIT | 10 IITs, 50+ streams | Bombay, Delhi, Madras, Kanpur, Kharagpur, Roorkee, Guwahati, Hyderabad, BHU, Indore, Dhanbad |
| NIT | 7 NITs, 30+ streams | Trichy, Surathkal, Warangal, Calicut, Rourkela, VNIT Nagpur, MNNIT Allahabad |
| IIIT | 7 IIITs | Hyderabad, Allahabad, Delhi, Bangalore, Lucknow, Gwalior, Jabalpur |
| GFTI | 6 institutes | BITS Pilani, DTU Delhi, NSUT Delhi, IIIT Sri City, IIIT Kottayam |

100+ college-stream combinations total.

### Streams Covered
Computer Science, Electrical Engineering, Mechanical Engineering, Chemical Engineering, Civil Engineering, Aerospace Engineering, Mining Engineering, Textile Engineering, Ceramic Engineering

### Category-Based Rank Adjustment
| Category | Rank Multiplier |
|----------|----------------|
| General | 1.0x (no adjustment) |
| EWS | 1.2x |
| OBC-NCL | 1.3x |
| SC | 2.0x |
| ST | 2.5x |
| PwD | 2.0x |

Your actual rank is divided by the multiplier to compute an effective rank for comparison against General cutoffs.

### Admission Chance Levels
| Chance | Meaning |
|--------|---------|
| 🟢 High | Rank is within opening cutoff |
| 🟡 Moderate | Rank is in the upper half of the cutoff range |
| 🟠 Low-Moderate | Rank is in the lower half of the cutoff range |
| 🔴 Slim | Rank is within 15% beyond closing cutoff |

### Visualizations
- Donut chart — admission chance distribution
- Bar chart — colleges grouped by type (IIT/NIT/IIIT/GFTI)

### Other Features
- Tabbed results view (All / High / Moderate / Slim)
- NIRF ranking displayed per college
- City information for each college
- Opening and closing rank ranges shown
- CSV download of all predicted colleges

---

## Getting Started

### Prerequisites
- Python 3.8+

### Installation

```bash
cd st_JEE
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```



---

## How to Use

1. Open the sidebar
2. Select exam type (JEE Advanced or JEE Mains)
3. Enter your All India Rank (AIR)
4. Choose your reservation category
5. Select preferred streams (multi-select)
6. For JEE Mains, optionally filter by college type (NIT/IIIT/GFTI)
7. Click "Predict Colleges"
8. Browse results by chance level using tabs
9. Download results as CSV if needed

---



---

## Disclaimer

⚠️ Cutoff ranks are approximate and based on previous years' trends. Actual cutoffs vary each year based on difficulty, number of candidates, and seat availability. This tool is for guidance only — always verify with official JoSAA/CSAB counselling data.

---

Made with ❤️ by dotnetabhishekai

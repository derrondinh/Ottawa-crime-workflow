Project Description:
Ottawa Crime Workflow is a data pipeline that automates the retrieval, cleaning, transformation, analysis, and visualization of bike theft incidents in Ottawa.
The workflow is implemented using Snakemake to ensure reproducibility and efficiency.

Setup Instructions

1. Install Dependencies

Ensure you have the required dependencies installed. You can set up a virtual environment using conda:
conda create -n crime-workflow python=3.9 -y
conda activate crime-workflow
pip install pandas matplotlib snakemake

Alternatively, install dependencies from requirements.txt:
pip install -r requirements.txt

2. Clone the Repository
git clone https://github.com/YOUR_USERNAME/Ottawa-crime-workflow.git
cd Ottawa-crime-workflow

3. Organize the Directory Structure
Ensure that your directory follows this structure:
Ottawa-crime-workflow/
│── data/
│   ├── raw/              # Raw dataset
│   ├── clean/            # Cleaned dataset
│   ├── transformed/      # Aggregated & processed data
│── results/
│   ├── plots/            # Visualizations
│   ├── reports/          # Summary reports
│── scripts/
│   ├── download_data.py
│   ├── clean_data.py
│   ├── transform_data.py
│   ├── analyze_data.py
│── Snakefile
│── README.md
│── requirements.txt

4. Workflow Execution Instructions
snakemake --cores 1


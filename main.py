import pandas as pd
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))

if not file_path:
    print("No file selected. Exiting.")
    exit()

def classify_job_role(row):
    job_title = str(row['JOBTITLE']).lower()
    prior_positions = str(row['PRIOR_POSITIONS']).lower() if pd.notna(row['PRIOR_POSITIONS']) else ''

    keywords = {
        'sales': ['sales', 'lead generation', 'customer management', 'sales operations'],
        'it': ['enterprise architecture', 'technical support', 'cyber security', 'data management', 'business intelligence'],
        'engineer': ['data pipelines', 'software products', 'cloud systems', 'qa', 'data scientist', 'machine learning'],
        'product': ['product owner', 'product manager', 'product marketing', 'ux/ui', 'product analyst'],
        'marketing': ['marketing', 'digital marketing', 'social media', 'brand manager'],
        'admin': ['legal', 'human resources', 'recruiting', 'executive assistant', 'contract management'],
        'operations': ['supply chain', 'quality assurance', 'manufacturing', 'project management', 'strategy associate'],
        'scientist': ['researcher', 'ai researcher', 'ai scientist', 'chemistry', 'biology'],
        'finance': ['accounting', 'finance', 'm&a', 'financial reporting', 'investor relations']
    }

    for category, category_keywords in keywords.items():
        if any(keyword in job_title or keyword in prior_positions for keyword in category_keywords):
            return category

    return 'Neither'

df = pd.read_csv(file_path)

df['Classification'] = df.apply(classify_job_role, axis=1)

output_file_path = file_path.replace('.csv', '_classified.csv')
df.to_csv(output_file_path, index=False)

print(f"Classification complete. Results saved to: {output_file_path}")

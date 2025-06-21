import csv

input_file = 'C:/Users/techin/Amharic-NER-Data-Collector_week4/notebooks/labeling_template.csv'  # Replace with your CSV filename
output_file = 'output_conll.txt'

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    reader = csv.reader(f_in)
    current_id = None
    
    for row in reader:
        sent_id, token, tag = row
        
        if sent_id != current_id:
            # New sentence
            if current_id is not None:
                f_out.write('\n')  # blank line between sentences
            current_id = sent_id
        
        f_out.write(f"{token} {tag}\n")
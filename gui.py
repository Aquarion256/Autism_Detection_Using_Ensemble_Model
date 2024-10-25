import tkinter as tk
from tkinter import ttk
import pickle
import pandas as pd
import csv
from collections import OrderedDict


user_input = {
    'Social_Responsiveness_Scale': 6.0,
    'Age_Years': 3,
    'Speech Delay/Language Disorder': 'Yes',
    'Learning disorder': 'Yes',
    'Genetic_Disorders': 'Yes',
    'Depression': 'Yes',
    'Global developmental delay/intellectual disability': 'Yes',
    'Social/Behavioural Issues': 'Yes',
    'Childhood Autism Rating Scale': 2,
    'Anxiety_disorder': 'Yes',
    'Sex': 'M',
    'Ethnicity': 'White European',
    'Jaundice': 'Yes',
    'Family_mem_with_ASD': 'No',
    'Who_completed_the_test': 'Family Member'
}
all_columns=['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
       'A10_Autism_Spectrum_Quotient', 'Social_Responsiveness_Scale',
       'Age_Years', 'Childhood Autism Rating Scale',
       'Speech Delay/Language Disorder_No',
       'Speech Delay/Language Disorder_Yes', 'Learning disorder_No',
       'Learning disorder_Yes', 'Genetic_Disorders_No',
       'Genetic_Disorders_Yes', 'Depression_No', 'Depression_Yes',
       'Global developmental delay/intellectual disability_No',
       'Global developmental delay/intellectual disability_Yes',
       'Social/Behavioural Issues_No', 'Social/Behavioural Issues_Yes',
       'Anxiety_disorder_No', 'Anxiety_disorder_Yes', 'Sex_F', 'Sex_M',
       'Ethnicity_Asian', 'Ethnicity_Black', 'Ethnicity_Hispanic',
       'Ethnicity_Latino', 'Ethnicity_Middle Eastern', 'Ethnicity_Mixed',
       'Ethnicity_Native Indian', 'Ethnicity_Others', 'Ethnicity_PaciFica',
       'Ethnicity_South Asian', 'Ethnicity_White European', 'Ethnicity_asian',
       'Ethnicity_black', 'Ethnicity_middle eastern', 'Ethnicity_mixed',
       'Ethnicity_south asian', 'Jaundice_No', 'Jaundice_Yes',
       'Family_mem_with_ASD_No', 'Family_mem_with_ASD_Yes',
       'Who_completed_the_test_Family Member',
       'Who_completed_the_test_Family member',
       'Who_completed_the_test_Health Care Professional',
       'Who_completed_the_test_Others',
       'Who_completed_the_test_School and NGO', 'Who_completed_the_test_Self']

input_dict={'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': 0, 'A8': 0, 'A9': 0,'A10_Autism_Spectrum_Quotient': 0, 
            'Social_Responsiveness_Scale': 0.0, 
            'Age_Years': 0,
            'Speech Delay/Language Disorder': '', 
            'Learning disorder': '', 
            'Genetic_Disorders': '', 
            'Depression': '', 
            'Global developmental delay/intellectual disability': '', 
            'Social/Behavioural Issues': '',
            'Childhood Autism Rating Scale': 0, 
            'Anxiety_disorder': '', 
            'Sex': '', 
            'Ethnicity': 'White European', 
            'Jaundice': '', 
            'Family_mem_with_ASD': '', 
            'Who_completed_the_test': ''}


def show_initial_form():
    # Clear current screen
    for widget in root.winfo_children():
        widget.destroy()

    # Create the basic input form
    ttk.Label(root, text="Age:").grid(row=0, column=0)
    ttk.Combobox(root, textvariable=age_var, values=[i for i in range(1, 19)]).grid(row=0, column=1)

    ttk.Label(root, text="Sex:").grid(row=1, column=0)
    ttk.Combobox(root, textvariable=sex_var, values=["Male", "Female"]).grid(row=1, column=1)

    ttk.Label(root, text="Social Responsiveness Scale:").grid(row=2, column=0)
    ttk.Combobox(root, textvariable=srs_var, values=[i for i in range(11)]).grid(row=2, column=1)

    ttk.Label(root, text="Childhood Autism Rating Scale:").grid(row=3, column=0)
    ttk.Combobox(root, textvariable=cars_var, values=[i for i in range(5)]).grid(row=3, column=1)

    ttk.Label(root, text="Ethnicity:").grid(row=4, column=0)
    ttk.Combobox(root, textvariable=ethnicity_var, values=['middle eastern',
 'White European',
 'Middle Eastern',
 'Hispanic',
 'Black',
 'Asian',
 'South Asian',
 'Native Indian',
 'Others',
 'black',
 'asian',
 'Latino',
 'Mixed',
 'south asian',
 'mixed',
 'PaciFica']).grid(row=4, column=1)

    ttk.Label(root, text="Who completed the test:").grid(row=5, column=0)
    ttk.Combobox(root, textvariable=who_completed_var, values=['Family Member',
 'Health Care Professional',
 'Self',
 'Family member',
 'Others',
 'School and NGO']).grid(row=5, column=1)

    # Radio buttons for other attributes
    ttk.Label(root, text="Speech Delay/Language Disorder:").grid(row=6, column=0)
    tk.Radiobutton(root, text="Yes", variable=sdld_var, value="Yes").grid(row=6, column=1)
    tk.Radiobutton(root, text="No", variable=sdld_var, value="No").grid(row=6, column=2)

    ttk.Label(root, text="Learning Disorder:").grid(row=7, column=0)
    tk.Radiobutton(root, text="Yes", variable=ld_var, value="Yes").grid(row=7, column=1)
    tk.Radiobutton(root, text="No", variable=ld_var, value="No").grid(row=7, column=2)

    ttk.Label(root, text="Genetic Disorders:").grid(row=8, column=0)
    tk.Radiobutton(root, text="Yes", variable=gd_var, value="Yes").grid(row=8, column=1)
    tk.Radiobutton(root, text="No", variable=gd_var, value="No").grid(row=8, column=2)

    ttk.Label(root, text="Depression:").grid(row=9, column=0)
    tk.Radiobutton(root, text="Yes", variable=depression_var, value="Yes").grid(row=9, column=1)
    tk.Radiobutton(root, text="No", variable=depression_var, value="No").grid(row=9, column=2)

    ttk.Label(root, text="Global Developmental Delay/Intellectual Disability:").grid(row=10, column=0)
    tk.Radiobutton(root, text="Yes", variable=delay_var, value="Yes").grid(row=10, column=1)
    tk.Radiobutton(root, text="No", variable=delay_var, value="No").grid(row=10, column=2)

    ttk.Label(root, text="Social/Behavioural Issues:").grid(row=11, column=0)
    tk.Radiobutton(root, text="Yes", variable=behavioral_var, value="Yes").grid(row=11, column=1)
    tk.Radiobutton(root, text="No", variable=behavioral_var, value="No").grid(row=11, column=2)

    ttk.Label(root, text="Anxiety Disorder:").grid(row=12, column=0)
    tk.Radiobutton(root, text="Yes", variable=anxiety_var, value="Yes").grid(row=12, column=1)
    tk.Radiobutton(root, text="No", variable=anxiety_var, value="No").grid(row=12, column=2)

    ttk.Label(root, text="Jaundice:").grid(row=13, column=0)
    tk.Radiobutton(root, text="Yes", variable=jaundice_var, value="Yes").grid(row=13, column=1)
    tk.Radiobutton(root, text="No", variable=jaundice_var, value="No").grid(row=13, column=2)

    ttk.Label(root, text="Family Member with ASD:").grid(row=14, column=0)
    tk.Radiobutton(root, text="Yes", variable=family_asd_var, value="Yes").grid(row=14, column=1)
    tk.Radiobutton(root, text="No", variable=family_asd_var, value="No").grid(row=14, column=2)

    ttk.Button(root, text="Next", command=next_screen).grid(row=15, column=1)

def show_screen(screen_num):
    # Clear current screen
    for widget in root.winfo_children():
        widget.destroy()

    # Show the appropriate screen based on the screen_num
    questions = []
    if screen_num == 1:
        questions = screen_1_questions
    elif screen_num == 2:
        questions = screen_2_questions
    elif screen_num == 3:
        questions = screen_3_questions
    elif screen_num == 4:
        questions = screen_4_questions

    ttk.Label(root, text=f"Screen {screen_num}").grid(row=0, column=0, columnspan=2)

    # Display the questions with radio buttons
    for i, question in enumerate(questions):
        ttk.Label(root, text=question).grid(row=i + 1, column=0, sticky=tk.W)
        tk.Radiobutton(root, text="Yes", variable=question_vars[i], value="Yes").grid(row=i + 1, column=1)
        tk.Radiobutton(root, text="No", variable=question_vars[i], value="No").grid(row=i + 1, column=2)

    # Back and Submit buttons
    ttk.Button(root, text="Back", command=show_initial_form).grid(row=11, column=0)
    ttk.Button(root, text="Submit", command=submit_form).grid(row=11, column=2)

def next_screen():
    # Capture values from dropdowns and radio buttons
    input_dict['Age_Years'] = age_var.get()
    age=age_var.get()
    sex = sex_var.get()
    if sex.lower() == "male":
        input_dict['Sex'] = 'M'
    else:
        input_dict['Sex'] = 'F'
    input_dict['Social_Responsiveness_Scale'] = srs_var.get()
    input_dict['Childhood Autism Rating Scale'] = cars_var.get()
    input_dict['Ethnicity'] = ethnicity_var.get()
    input_dict['Who_completed_the_test'] = who_completed_var.get()
    input_dict['Speech Delay/Language Disorder'] = sdld_var.get()
    input_dict['Learning disorder'] = ld_var.get()
    input_dict['Genetic_Disorders'] = gd_var.get()
    input_dict['Depression'] = depression_var.get()
    input_dict['Global developmental delay/intellectual disability'] = delay_var.get()
    input_dict['Social/Behavioural Issues'] = behavioral_var.get()
    input_dict['Anxiety_disorder'] = anxiety_var.get()
    input_dict['Jaundice'] = jaundice_var.get()
    input_dict['Family_mem_with_ASD'] = family_asd_var.get()

    # Determine which screen to show based on age
    if 0 <= age <= 3:
        show_screen(1)
    elif 4 <= age <= 11:
        show_screen(2)
    elif 12 <= age <= 15:
        show_screen(3)
    elif age >= 16:
        show_screen(4)


def add_data_to_dataset(input_dict, prediction):
    # Calculate the ASD traits based on the prediction
    asd_traits = 'Yes' if prediction[0] == 'Yes' else 'No'
    
    # Open the CSV to find the last serial number
    try:
        with open('global_dataset.csv', mode='r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if rows:
                last_serial_number = int(rows[-1]["CASE_NO_PATIENT'S"])  # Get the last serial number
            else:
                last_serial_number = 0  # If the file is empty, start with 0
    except FileNotFoundError:
        last_serial_number = 0  # If the file doesn't exist yet, start with 0

    # Increment the serial number for the new entry
    new_serial_number = last_serial_number + 1

    # Prepare the ordered dictionary with CASE_NO_PATIENT'S as the first column
    ordered_data = OrderedDict()
    ordered_data["CASE_NO_PATIENT'S"] = new_serial_number
    ordered_data.update(input_dict)  # Add the main input dictionary data
    ordered_data['ASD_traits'] = asd_traits  # Add the ASD traits as the last column

    # Open the CSV file in append mode
    with open('global_dataset.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=ordered_data.keys())
        
        # Write header if the file is new
        if file.tell() == 0:
            writer.writeheader()
        
        # Write the new data row
        writer.writerow(ordered_data)
        
    # Notify user of successful addition
    ttk.Label(root, text="Data added successfully!", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=10)


def show_results_screen(prediction):
    # Clear current screen
    for widget in root.winfo_children():
        widget.destroy()

    # Set window size (width x height)
    root.geometry("500x400")  # You can adjust this if needed

    # Configure rows and columns to expand dynamically
    root.grid_rowconfigure(0, weight=1)  # First row (Label) will expand
    root.grid_rowconfigure(1, weight=1)  # Second row (Result Text) will expand
    root.grid_rowconfigure(2, weight=1)  # Third row (Buttons) will expand
    root.grid_rowconfigure(3, weight=1)  #Fourth row (Buttons) will expand
    root.grid_columnconfigure(0, weight=1)  # First column will expand
    root.grid_columnconfigure(1, weight=1)  # Second column (for buttons) will expand

    # Display the results based on the prediction
    if prediction[0] == 'Yes':
        result_text = "You are likely to have Autism."
    else:
        result_text = "You are unlikely to have Autism."

    # Main label
    ttk.Label(root, text="Results of Autism Detection Test: ", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="nsew")

    # Result text (resizes dynamically)
    ttk.Label(root, text=result_text, font=("Helvetica", 16)).grid(row=1, column=0, columnspan=2, pady=20, padx=10, sticky="nsew")

    ttk.Button(root, text="Get More Help" ).grid(row=2, column=0, pady=20, padx=10, sticky="nsew")
    ttk.Button(root, text="Add data to our dataset", command=lambda: add_data_to_dataset(input_dict, prediction)).grid(row=2, column=1, pady=20, padx=10, sticky="nsew")

    # Button to go back to the initial form or exit (they will also expand)
    ttk.Button(root, text="Back", command=show_initial_form).grid(row=3, column=0, pady=20, padx=10, sticky="nsew")
    ttk.Button(root, text="Exit", command=root.quit).grid(row=3, column=1, pady=20, padx=10, sticky="nsew")



def submit_form():
    # Handle form submission logic for each screen
    for i, var in enumerate(question_vars):
        if(var.get() == "Yes"):
            temp = 1
        else:
            temp = 0
        if i + 1 != 10:
            input_dict[f"A{i + 1}"] = temp
        else:
            input_dict["A10_Autism_Spectrum_Quotient"] = temp

    print(input_dict)
    with open('ensemble_model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    input_df = pd.DataFrame([input_dict])
    input_df_encoded = pd.get_dummies(input_df)

    # Assuming input_df_encoded is your DataFrame
    missing_cols = set(all_columns) - set(input_df_encoded.columns)

    for col in missing_cols:
        input_df_encoded[col] = 0

    input_df_encoded = input_df_encoded[all_columns]

    prediction = loaded_model.predict(input_df_encoded)

    # Show results screen with the prediction
    show_results_screen(prediction)


root = tk.Tk()
root.title("Autism Detection Form")

# Sample questions for each screen (placeholders and will be replaced later)
screen_1_questions = ["Does the child look at you when you call his/her name?", 
                      "Is it easy for you to get eye contact with your child?", 
                      "Does your child point to indicate that s/he wants something?", 
                      "Does your child point to share interest with you?", 
                      "Does your child pretend?",
                      "Does your child follow where you're looking?", 
                      "If you or someone else in your family is visibly upset, does your child show signs of wanting to comfort them?", 
                      "Would you describe your child's first words as typical?", 
                      "Does your child use simple gestures?", 
                      "Does your child stare at nothing with no apparent purpose?"]
screen_2_questions = ["Does S/he often notices small sounds when others do not?", 
                      "Does S/he usually concentrates more on the whole picture rather than the small details?", 
                      "In a social group, can S/he easily keep track of several different people's conversation?", 
                      "Does S/he find it easy to go back and forth between different activities?", 
                      "Does S/he know how to keep a conversation going with his/her peers?",
                      "Is S/he good at social chit-chat?", 
                      "When S/he is reading a story, S/he finds it difficult to work out the character's intentions or feelings?", 
                      "When S/he was in preschool S/he would enjoy playing pretending games with other children?", 
                      "S/he finds it easy to work out what someone id feeling or thinking, just by looking at their face?", 
                      "Does S/he finds it hard to make new friends?"]
screen_3_questions = ["Is the child able to understand humor?", 
                      "Do they follow simple instructions?", 
                      "Question 23?", 
                      "Question 24?", 
                      "Question 25?",
                      "Question 26?", 
                      "Question 27?", 
                      "Question 28?", 
                      "Question 29?", 
                      "Question 30?"]
screen_4_questions = ["I often notice small sounds when others do not.", 
                      "I usually concentrate more on the whole picture, rather than the small details.", 
                      "I find it easy to do more than one thing at once.", 
                      "If there is an interruption, I can switch back to what I was doing very quickly", 
                      "I find it easy to 'read between the lines' when someone is talking to me",
                      "I know how to tell if someone listening to me is getting bored", 
                      "When I'm reading a story I find it difficult to work out the characters' intentions", 
                      "I like to collect information about categories of things (e.g. types of car, bird, train, plant etc.)", 
                      "I find it easy to work out what someone is thinking or feeling just by looking at their face", 
                      "I find it difficult to work out people's intentions."]

age_var = tk.IntVar(value=user_input['Age_Years'])
sex_var = tk.StringVar(value='Male' if user_input['Sex'] == 'M' else 'Female')
srs_var = tk.DoubleVar(value=float(user_input['Social_Responsiveness_Scale']))
cars_var = tk.IntVar(value=user_input['Childhood Autism Rating Scale'])
ethnicity_var = tk.StringVar(value=user_input['Ethnicity'])
who_completed_var = tk.StringVar(value=user_input['Who_completed_the_test'])

sdld_var = tk.StringVar(value=user_input['Speech Delay/Language Disorder'])
ld_var = tk.StringVar(value=user_input['Learning disorder'])
gd_var = tk.StringVar(value=user_input['Genetic_Disorders'])
depression_var = tk.StringVar(value=user_input['Depression'])
delay_var = tk.StringVar(value=user_input['Global developmental delay/intellectual disability'])
behavioral_var = tk.StringVar(value=user_input['Social/Behavioural Issues'])
anxiety_var = tk.StringVar(value=user_input['Anxiety_disorder'])
jaundice_var = tk.StringVar(value=user_input['Jaundice'])
family_asd_var = tk.StringVar(value=user_input['Family_mem_with_ASD'])

default_answers = ["Yes", "Yes", "No", "No", "No", "Yes", "Yes", "No", "No", "No"]
question_vars = [tk.StringVar(value=default_answer) for default_answer in default_answers]

show_initial_form()
root.mainloop()

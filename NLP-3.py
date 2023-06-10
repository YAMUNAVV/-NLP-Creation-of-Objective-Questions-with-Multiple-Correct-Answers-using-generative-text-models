# -*- coding: utf-8 -*-

import PyPDF2
import random
import os
def get_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
    
def get_mca_questions(context):
    # Split the context into sentences
    sentences = context.strip().split('. ')

    # Generate multiple-choice questions
    mca_questions = []
    for sentence in sentences:
        question = "Which of the following is true about " + sentence + "?"
        choices = random.sample(sentences, k=3)  # Randomly select 3 choices
        choices.append(sentence)  # Add the correct answer to the choices
        random.shuffle(choices)  # Shuffle the choices

        mca_question = question + "\n"
        for i, choice in enumerate(choices):
            mca_question += chr(ord('a') + i) + ") " + choice + "\n"

        mca_questions.append(mca_question)

    return mca_questions 

# Example usage
#file_path = 'path/to/your/pdf/file.pdf'
#file_path = C:/Users/ELCOT/Desktop/chapter-2.pdf

file_path = 'chapter-2.pdf'
context = get_text_from_pdf(file_path)

questions = get_mca_questions(context)
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question}")
    
    
    
    
# Example usage
#file_path = 'path/to/your/pdf/file.pdf'
#file_path = C:/Users/ELCOT/Desktop/chapter-3.pdf

file_path = 'chapter-3.pdf'
context = get_text_from_pdf(file_path)

questions = get_mca_questions(context)
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question}")
    
    
    
# Example usage
#file_path = 'path/to/your/pdf/file.pdf'
#file_path = C:/Users/ELCOT/Desktop/chapter-4.pdf

file_path = 'chapter-4.pdf'
context = get_text_from_pdf(file_path)

questions = get_mca_questions(context)
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question}")
def create_html_paragraphs(input_string):
    # Split the input string into paragraphs based on line breaks
    paragraphs = input_string.split('\n')

    # Create HTML <p> elements for each paragraph
    html_paragraphs = ['<p class="spacing-after-paragraph">{}</p>'.format(p.strip()) for p in paragraphs if p.strip()]

    # Join the HTML paragraphs into a single string
    html_output = '\n'.join(html_paragraphs)

    return html_output

# Example usage:
input_text = """
Dominic has over 40 years’ experience in implementing training and employment strategies, particularly relating to the needs of ICT industry and employer organisations.
Dominic is the National Executive Officer of CITT, a ‘not for profit’ national Industry based Company that works extensively with industry and governments to implement VET (Vocational Education & Training) ICT (Information & Communications Technology) programs and strategies. 
Dominic is also the Secretary of the Australian Digital and Telecommunications Industry Association, a ‘not for profit’ National Industry Association that deals extensively with the Digital, Internet of Things (IoT), ICT and Telecommunications areas of the ICT and integrated industries to develop and support the ICT workforce skills. 
He has been instrumental in raising Cyber Security and Internet of Things (IoT) within VET and was the Deputy Chair of the committee developing the Certificate IV and Associate Diploma in Cyber Security within the VET system with over 3,000 leaners enrolled throughout Australia.
Dominic has relevant qualifications in B. Bus. (Admin), Grad Cert. Management, Grad Dip. in Vocational Counselling. 
"""

html_output = create_html_paragraphs(input_text)
print(html_output)
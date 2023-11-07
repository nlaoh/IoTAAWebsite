def convert_newlines_to_br(input_string):
    # Replace newline characters with <br> tags
    output_string = input_string.replace('\n', '<br style="margin-bottom: 8px;">')
    return output_string

# Input text
input_text = """Sean is the Head of Smart Metering for Suez Water Australia, working to add intelligence to the infrastructure that supports our communities.
As an engineer, he strongly believes that IoT should meet the levels of performance and reliability that we’ve come to expect from *all* our infrastructure. Whether it’s a bridge or a battery, it should be built to last.
Sean has built a career on technology development and deployment, across electricity, water & wastewater treatment, communications systems, and medical devices. 
Sean has also been instrumental in working with the WIZE Alliance to make the WIZE open standard available for digital metering and utility IoT applications in Australia.
Sean is also a massive nerd (his daughter had a soldering party for her birthday).
"""

# Call the function to replace newlines with <br> tags
output_text = convert_newlines_to_br(input_text)

# Print the result
print(output_text)
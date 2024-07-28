import base64

def data_url_to_file(data_url, output_file_path):
    """
    Converts a data URL to an image file.

    Parameters:
    data_url (str): The data URL to convert.
    output_file_path (str): The path where the output file should be saved.
    """
    # Split the Data URL to get the base64 encoded data part
    header, encoded = data_url.split(",", 1)

    # Decode the base64 data
    data = base64.b64decode(encoded)

    # Write the decoded data to a file
    with open(output_file_path, "wb") as output_file:
        output_file.write(data)

if __name__ == "__main__":
    # Example data URL (Replace this with your own data URL)
    data_url = "data:font/woff2;base64,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"

    # Example output file path
    output_file_path = "output_image.woff2"

    # Convert the data URL to an image file
    data_url_to_file(data_url, output_file_path)

    print(f"Image file saved as {output_file_path}")

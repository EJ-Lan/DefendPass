import requests
import hashlib
import sys


def request_api_data(query_char):
    # Construct the URL with the given query character
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    # Send a GET request to the API and retrieve the response
    res = requests.get(url)
    # Check if the response was successful (status code 200)
    if res.status_code != 200:
        # Raise an error if the response was not successful
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    # Return the response data
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # Split the response into lines and split each line into hash and count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # Iterate over each hash and count
    for h, count in hashes:
        # Check if the hash matches the hash to check
        if h == hash_to_check:
            # Return the count if the hash is found
            return count
    # Return 0 if the hash is not found
    return 0


def pwned_api_check(password):
    # Hash the password using SHA-1 algorithm and convert to uppercase
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Split the hashed password into first 5 characters and the remaining characters
    first5_char, tail = sha1password[:5], sha1password[5:]
    # Request the API data for the first 5 characters of the hashed password
    response = request_api_data(first5_char)
    # Get the count of password leaks for the remaining characters of the hashed password
    return get_password_leaks_count(response, tail)


def main(args):
    # Define the output file for writing the results
    output_file = 'password_check_results.txt'
    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Iterate over each password provided as arguments
        for password in args:
            # Check if the password has been compromised
            count = pwned_api_check(password)
            # Write the result to the output file
            if count:
                file.write(f'{password} was found {count} time... you should probably change your password!\n')
            else:
                file.write(f'{password} was NOT found. Carry on!\n')
    # Return a completion message
    return 'Done!'


if __name__ == '__main__':
    # Call the main function with the command-line arguments (excluding the script name)
    sys.exit(main(sys.argv[1:]))

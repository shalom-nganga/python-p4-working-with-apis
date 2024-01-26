import requests
import json

class GetPrograms:
    def program_school(self):
        programs_list = []
        programs = self.get_programs()
        
        for program in programs:
            # Check if "agency" key exists in the program dictionary
            if "agency" in program:
                programs_list.append(program["agency"])

        return programs_list

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)

        if response.status_code == 200:
            # Parse the response content as JSON
            return response.json()
        else:
            # Print the error if the request was unsuccessful
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return []

# Create an instance of GetPrograms
programs = GetPrograms()

# Call program_school method to get a list of programs
programs_schools = programs.program_school()

# Print the unique schools
for school in set(programs_schools):
    print(school)

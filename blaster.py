import requests
from bs4 import BeautifulSoup
import phonenumbers

custom_header_thatsthem = r'''

██████╗  █████╗ ███████╗██╗ ██████╗    ██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██║██╔════╝    ██║████╗  ██║██╔════╝██╔═══██╗
██████╔╝███████║███████╗██║██║         ██║██╔██╗ ██║█████╗  ██║   ██║
██╔══██╗██╔══██║╚════██║██║██║         ██║██║╚██╗██║██╔══╝  ██║   ██║
██████╔╝██║  ██║███████║██║╚██████╗    ██║██║ ╚████║██║     ╚██████╔╝
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
'''

country_code = input("Input the country code country code (example: +1): ")
phone_number_without_country = input("Input the phone number without the country code (example: 1111111111) country code: ")
phone_number_with_hyphens = input("Input the phone number with dashes (example: 111-111-1111):  ")
full_phone_number = f"{country_code}{phone_number_without_country}"

print(custom_header_thatsthem)

api_key = "5e32e0970f00059ad0a63dec2b4b686a"
numverify_url = f"http://apilayer.net/api/validate?access_key={api_key}&number={full_phone_number}"

numverify_response = requests.get(numverify_url)
numverify_data = numverify_response.json()

if "valid" in numverify_data and numverify_data["valid"]:
    country = numverify_data.get('country_name', 'N/A')
    location = numverify_data.get('location', 'N/A')
    line_type = numverify_data.get('line_type', 'N/A')
    carrier_info = numverify_data.get('carrier', 'N/A')
    
    print("\nStarting Researches:")
    print(f"Country: {country}")
    print(f"Location: {location}")
    print(f"Type: {line_type}")
    print(f"Operator: {carrier_info}")
else:
    print("Invalid phone number for 'Numverify'.")

thatsthem_url = f'https://thatsthem.com/phone/{phone_number_with_hyphens}'

thatsthem_headers = {
    "put your headers here"
}

thatsthem_response = requests.get(thatsthem_url, headers=thatsthem_headers)

if thatsthem_response.status_code == 200:
    thatsthem_soup = BeautifulSoup(thatsthem_response.text, 'html.parser')
    
    found = False
    processed_results = set()
    
    web_links = thatsthem_soup.find_all('a', class_='web')
    
    for link in web_links:
        href = link.get('href')
        label = None
        
        if href.startswith('https://thatsthem.com/name/'):
            label = "Possible Names"
        elif href.startswith('https://thatsthem.com/address/'):
            label = "Address"
        elif href.startswith('https://thatsthem.com/email/'):
            label = "Email"
        elif href.startswith('https://thatsthem.com/ip/'):
            label = "IP"
        
        if label and label not in processed_results:
            processed_results.add(label)
            print(f"{label}: {href.split('/')[-1]} - {link.text.strip()}")
            
            found = True
    
    if not found:
        print("No advanced info found or captcha issue try seeing solve_issues.txt'.")
else:
    print(f"Errore nella richiesta HTTP a 'thatsthem.com'. Codice di stato: {thatsthem_response.status_code}")
    print(f"Testo di risposta: {thatsthem_response.text}")

whatsapp_link_without_country = f"https://api.whatsapp.com/send?phone={phone_number_without_country}"
whatsapp_response = requests.get(whatsapp_link_without_country)

if whatsapp_response.status_code == 200:
    if 'https://web.whatsapp.com/send/?phone=' in whatsapp_response.text and '<a href="https://web.whatsapp.com/send/?phone=' in whatsapp_response.text:
        print("WhatsApp Found")
    else:
        print("WhatsApp Not Found")
else:
    print("Errore nella richiesta HTTP per WhatsApp.")

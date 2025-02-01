import random
import json
from flask import Flask, jsonify
from faker import Faker

app = Flask(__name__)
fake = Faker('en_IN')  # भारत के एड्रेस और नाम जनरेट करने के लिए

# भारत के सभी 28 राज्य और 8 केंद्र शासित प्रदेश के शहर
state_cities = {
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Kurnool"],
    "Arunachal Pradesh": ["Itanagar", "Naharlagun", "Pasighat", "Ziro"],
    "Assam": ["Guwahati", "Dibrugarh", "Jorhat", "Silchar", "Tezpur"],
    "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Purnia", "Darbhanga"],
    "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur", "Korba", "Durg"],
    "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar"],
    "Haryana": ["Gurgaon", "Faridabad", "Panipat", "Ambala", "Hisar"],
    "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Solan", "Kullu"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh"],
    "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Hubli", "Belagavi"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Alappuzha"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur", "Gwalior", "Ujjain"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
    "Manipur": ["Imphal", "Thoubal", "Bishnupur"],
    "Meghalaya": ["Shillong", "Tura", "Jowai"],
    "Mizoram": ["Aizawl", "Lunglei", "Champhai"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Puri"],
    "Punjab": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner"],
    "Sikkim": ["Gangtok", "Namchi"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad"],
    "Tripura": ["Agartala", "Dharmanagar"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Prayagraj"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Haldwani", "Roorkee"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Asansol"],
    
    # केंद्र शासित प्रदेश (Union Territories)
    "Andaman and Nicobar Islands": ["Port Blair"],
    "Chandigarh": ["Chandigarh"],
    "Dadra and Nagar Haveli and Daman and Diu": ["Silvassa", "Daman", "Diu"],
    "Lakshadweep": ["Kavaratti"],
    "Delhi": ["New Delhi"],
    "Puducherry": ["Puducherry"],
    "Ladakh": ["Leh", "Kargil"],
    "Jammu and Kashmir": ["Srinagar", "Jammu"]
}

def generate_data():
    state = random.choice(list(state_cities.keys()))  # कोई भी राज्य चुनें
    city = random.choice(state_cities[state])  # उस राज्य का कोई भी शहर चुनें

    record = {
        "Zip/Postal Code": fake.postcode(),
        "Street": fake.street_address(),
        "City/Town": city,
        "Gender": random.choice(["Male", "Female"]),
        "Birthday": fake.date_of_birth(minimum_age=18, maximum_age=40).strftime("%Y-%m-%d"),
        "Full Name": fake.name(),
        "Email": fake.email(),
        "Mobile Number": fake.phone_number(),
        "City": city,
        "State": state,
        "Post Office": f"{city} Post Office",
        "Mobile Flag": random.choice([True]),
        "Email Flag": random.choice([True]),
        "Verified": random.choice([True]),
        "Enable": random.choice([True]),
        "Registration Flag": random.choice([True]),
        "RDS Flag": random.choice([False])
    }
    return record

@app.route('/data', methods=['GET'])
def get_random_data():
    return jsonify(generate_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

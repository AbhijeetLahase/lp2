def expert_system():
    print("Expert System: Welcome! How can I assist you today?")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hi":
            print("Expert System: Hello there! What can I help you with today?")

        elif user_input in ["thanks", "thankyou"]:
            print("Expert System: You're most welcome! Take care.")

        elif user_input == "sorry":
            print("Expert System: No worries at all. How can I help further?")

        elif "no" in user_input or "don't" in user_input or "do not admit" in user_input:
            print("Expert System: Alright, feel free to reach out if you need assistance.")

        elif user_input == "bye":
            print("Expert System: Goodbye! Wishing you good health.")
            break

        elif ("admission" in user_input or "admit" in user_input) and "hospital" in user_input:
            location = input("Expert System: Could you please tell me your city? ").strip().lower()
            hospitals = {
                "pune": ["Ruby Hall Clinic", "Jehangir Hospital"],
                "mumbai": ["Lilavati Hospital", "Nanavati Hospital"],
                "delhi": ["AIIMS", "Apollo Hospital"]
            }
            print(f"Expert System: Based on your location, recommended hospitals in {location.title()} are: {', '.join(hospitals.get(location, ['No hospital data available for this city.']))}")

        elif any(word in user_input for word in ["cough", "cold", "fever", "vomit", "pain", "headache", "stomach", "rash", "itch", "tired", "chest", "breathing"]):
            print("Expert System: Let's analyze your symptoms further.")

            try:
                temp = input("Expert System: Do you have a fever? (yes/no): ").strip().lower()
                if temp == "yes":
                    temperature = float(input("Expert System: What is your body temperature in °F? ").strip())
                else:
                    temperature = 98.6

                vomit = input("Expert System: Do you experience vomiting? (yes/no): ").strip().lower()
                if vomit == "yes":
                    vomit_count = int(input("Expert System: How many times did you vomit today? ").strip())
                else:
                    vomit_count = 0

                stomach_pain = input("Expert System: Do you have stomach pain? (yes/no): ").strip().lower()
                headache = input("Expert System: Are you experiencing headache? (yes/no): ").strip().lower()
                chest_pain = input("Expert System: Do you have chest pain or tightness? (yes/no): ").strip().lower()
                breathing = input("Expert System: Do you have difficulty breathing? (yes/no): ").strip().lower()
                fatigue = input("Expert System: Do you feel unusually tired or weak? (yes/no): ").strip().lower()
                sore_throat = input("Expert System: Do you have a sore throat? (yes/no): ").strip().lower()
                rash = input("Expert System: Do you have a skin rash or itching? (yes/no): ").strip().lower()

                print("\nExpert System: Summary of your symptoms:")
                if temperature >= 102:
                    print("- High-grade fever")
                elif 99 < temperature < 102:
                    print("- Low-grade fever")

                if vomit == "yes":
                    print(f"- Vomiting ({vomit_count} times)")

                if stomach_pain == "yes":
                    print("- Stomach pain")
                if headache == "yes":
                    print("- Headache")
                if chest_pain == "yes":
                    print("- Chest pain")
                if breathing == "yes":
                    print("- Difficulty breathing")
                if fatigue == "yes":
                    print("- Fatigue or weakness")
                if sore_throat == "yes":
                    print("- Sore throat")
                if rash == "yes":
                    print("- Skin rash or itching")

                # Determine specialist
                if breathing == "yes" or chest_pain == "yes":
                    specialist = "Pulmonologist"
                elif rash == "yes":
                    specialist = "Dermatologist"
                elif stomach_pain == "yes" and vomit_count >= 2:
                    specialist = "Gastroenterologist"
                elif headache == "yes" and temperature >= 102:
                    specialist = "Neurologist"
                elif sore_throat == "yes":
                    specialist = "ENT Specialist"
                elif fatigue == "yes":
                    specialist = "General Physician"
                else:
                    specialist = "Family Doctor"

                print(f"\nExpert System: You should consider visiting a **{specialist}**.")

                print("\nExpert System: Meanwhile, you can:")
                print("- Stay hydrated and rest.")
                print("- Avoid oily/spicy food.")
                if temperature >= 99:
                    print("- Take paracetamol for fever.")
                if sore_throat == "yes":
                    print("- Gargle with warm salt water.")
                if rash == "yes":
                    print("- Apply calamine lotion and avoid scratching.")

            except ValueError:
                print("Expert System: Please enter valid numbers where asked.")

        elif "doctor" in user_input or "specialist" in user_input:
            doctor_specialties = {
                "knee": "Orthopedist", "elbow": "Orthopedist", "hand": "Orthopedist", "bone": "Orthopedist",
                "eye": "Ophthalmologist", "eyes": "Ophthalmologist",
                "brain": "Neurologist", "head": "Neurologist",
                "heart": "Cardiologist", "pulse": "Cardiologist", "fast beats": "Cardiologist",
                "itching": "Dermatologist", "rash": "Dermatologist", "skin": "Dermatologist",
                "cancer": "Oncologist"
            }

            specialist_found = None
            for keyword, specialist in doctor_specialties.items():
                if keyword in user_input:
                    specialist_found = specialist
                    break

            if specialist_found:
                print(f"Expert System: You may consider visiting a {specialist_found}.")
            else:
                print("Expert System: It's best to consult a general physician first.")

        elif "insurance" in user_input or "claim" in user_input:
            try:
                income = int(input("Expert System: Kindly enter your annual income (in numbers): ").strip())
                if income < 500000:
                    print("Expert System: Based on your income, a 'Basic Health Plan' is suggested.")
                elif 500000 <= income <= 1000000:
                    print("Expert System: You may go for a 'Premium Health Cover'.")
                else:
                    print("Expert System: You are eligible for an Elite Family Insurance Plan.")
            except ValueError:
                print("Expert System: Invalid input. Please enter your income as a number (e.g., 750000).")

        else:
            print("Expert System: I'm not sure how to help with that. For more help, please call our medical helpline: 1800-220-220")

# Run the system
expert_system()

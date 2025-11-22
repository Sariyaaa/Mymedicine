import streamlit as st

# ================================
# MOCK DRUG DATABASE (India-focused + Side Effects)
# ================================
def get_drug_info(drug_name):
    mock_data = {
        # === Pain & Fever ===
        "paracetamol": {
            "brand_name": "Crocin, Dolo",
            "indications": "Fever, headache, mild to moderate pain.",
            "side_effects": "Rare: liver damage (if overdosed), skin rash.",
            "warnings": "Do not exceed 4g/day. Avoid alcohol."
        },
        "ibuprofen": {
            "brand_name": "Brufen, Ibugesic",
            "indications": "Pain, inflammation, fever.",
            "side_effects": "Stomach pain, heartburn, nausea, dizziness.",
            "warnings": "Take with food. Avoid if you have ulcers."
        },
        "aspirin": {
            "brand_name": "Ecosprin",
            "indications": "Pain, fever, heart attack prevention (low dose).",
            "side_effects": "Stomach irritation, bleeding, tinnitus (ringing in ears).",
            "warnings": "Do not give to children. May cause bleeding."
        },
        "diclofenac": {
            "brand_name": "Voveran",
            "indications": "Arthritis, muscle pain, inflammation.",
            "side_effects": "Stomach ulcers, nausea, headache, dizziness.",
            "warnings": "Risk of stomach bleeding. Use lowest dose."
        },
        "aceclofenac": {
            "brand_name": "Aceproxyvon",
            "indications": "Osteoarthritis, rheumatoid arthritis.",
            "side_effects": "Dyspepsia, abdominal pain, dizziness.",
            "warnings": "Avoid in kidney disease."
        },
        "mefenamic acid": {
            "brand_name": "Ponstan",
            "indications": "Menstrual pain, dental pain.",
            "side_effects": "Nausea, diarrhea, headache, rash.",
            "warnings": "Short-term use only."
        },
        "nimesulide": {
            "brand_name": "Nicip, Nimulid",
            "indications": "Acute pain, osteoarthritis.",
            "side_effects": "Stomach upset, dizziness, liver enzyme elevation.",
            "warnings": "Not for children <12 years. Liver risk."
        },
        "tramadol": {
            "brand_name": "Ultracet",
            "indications": "Moderate to severe pain.",
            "side_effects": "Nausea, dizziness, constipation, drowsiness.",
            "warnings": "Habit-forming. Do not mix with alcohol."
        },

        # === Antibiotics ===
        "amoxicillin": {
            "brand_name": "Novamox, Moxikind",
            "indications": "Bacterial infections (throat, ear, skin).",
            "side_effects": "Diarrhea, rash, nausea, yeast infection.",
            "warnings": "Complete full course. May cause diarrhea."
        },
        "azithromycin": {
            "brand_name": "Azee, Zithromax",
            "indications": "Respiratory, skin, ear infections.",
            "side_effects": "Nausea, abdominal pain, diarrhea, temporary hearing changes.",
            "warnings": "Take on empty stomach. Avoid antacids."
        },
        "cefixime": {
            "brand_name": "Monocef, Zifi",
            "indications": "Typhoid, urinary tract infections.",
            "side_effects": "Diarrhea, nausea, headache, vaginal itching.",
            "warnings": "Not for viral infections."
        },
        "levofloxacin": {
            "brand_name": "Levoflox, Tavanic",
            "indications": "Pneumonia, sinusitis, UTI.",
            "side_effects": "Nausea, headache, dizziness, tendon pain.",
            "warnings": "Avoid sun exposure. Tendon risk."
        },
        "ofloxacin": {
            "brand_name": "Oflomac, Flox",
            "indications": "Eye/ear infections, UTI, diarrhea.",
            "side_effects": "Nausea, insomnia, dizziness, photosensitivity.",
            "warnings": "Do not use in pregnancy."
        },
        "doxycycline": {
            "brand_name": "Doxy, Mysim",
            "indications": "Acne, malaria prevention, Lyme disease.",
            "side_effects": "Sun sensitivity, nausea, esophageal irritation.",
            "warnings": "Avoid sun. Take with full glass of water."
        },
        "metronidazole": {
            "brand_name": "Metrogyl, Flagyl",
            "indications": "Dental infections, amoebiasis, bacterial vaginosis.",
            "side_effects": "Metallic taste, nausea, dark urine, dizziness.",
            "warnings": "Do NOT consume alcohol."
        },
        "ciprofloxacin": {
            "brand_name": "Ciplox, Cifran",
            "indications": "UTI, diarrhea, eye/ear infections.",
            "side_effects": "Nausea, diarrhea, tendon pain, restlessness.",
            "warnings": "Not for children <18."
        },
        "amoxicillin+clavulanic acid": {
            "brand_name": "Augmentin, Moxikind-CV",
            "indications": "Sinus, dental, skin infections.",
            "side_effects": "Diarrhea, rash, nausea, yeast infection.",
            "warnings": "May cause diarrhea."
        },
        "cefpodoxime": {
            "brand_name": "Cefoprox, Simplicef",
            "indications": "Respiratory and urinary infections.",
            "side_effects": "Diarrhea, nausea, headache, dizziness.",
            "warnings": "Complete full course."
        },

        # === Antacids & GI ===
        "pantoprazole": {
            "brand_name": "Pantocid, Pantodac",
            "indications": "Acid reflux, ulcers, GERD.",
            "side_effects": "Headache, nausea, constipation, vitamin B12 deficiency (long-term).",
            "warnings": "Long-term use may cause bone loss."
        },
        "omeprazole": {
            "brand_name": "Omez, Ocid",
            "indications": "Heartburn, ulcers, acid-related disorders.",
            "side_effects": "Headache, abdominal pain, diarrhea, dizziness.",
            "warnings": "Take before meals."
        },
        "rabeprazole": {
            "brand_name": "Rabekind, Rablet",
            "indications": "GERD, peptic ulcers.",
            "side_effects": "Nausea, headache, dizziness, flatulence.",
            "warnings": "Do not crush tablet."
        },
        "esomeprazole": {
            "brand_name": "Nexium",
            "indications": "Severe acid reflux, erosive esophagitis.",
            "side_effects": "Headache, nausea, abdominal pain, diarrhea.",
            "warnings": "May interact with clopidogrel."
        },
        "domperidone": {
            "brand_name": "Domstal, Perinorm",
            "indications": "Nausea, vomiting, bloating.",
            "side_effects": "Dry mouth, headache, irregular heartbeat (rare).",
            "warnings": "Avoid in heart conditions."
        },
        "ondansetron": {
            "brand_name": "Emeset, Ondem",
            "indications": "Nausea from chemo, surgery, or pregnancy.",
            "side_effects": "Headache, constipation, dizziness.",
            "warnings": "Use with caution in liver disease."
        },
        "ranitidine": {
            "brand_name": "Rantac",
            "indications": "Heartburn, ulcers (less used now).",
            "side_effects": "Headache, constipation, fatigue.",
            "warnings": "Withdrawn in some countries due to impurity risk."
        },
        "sucralfate": {
            "brand_name": "Sucrafil",
            "indications": "Stomach ulcers.",
            "side_effects": "Constipation, dry mouth, nausea.",
            "warnings": "Take on empty stomach."
        },

        # === Diabetes ===
        "metformin": {
            "brand_name": "Glycomet, Gluformin",
            "indications": "Type 2 diabetes.",
            "side_effects": "Nausea, diarrhea, stomach upset, metallic taste.",
            "warnings": "Avoid in kidney disease. Lactic acidosis risk."
        },
        "glimepiride": {
            "brand_name": "Amaryl, Glimy",
            "indications": "Type 2 diabetes.",
            "side_effects": "Low blood sugar, weight gain, dizziness.",
            "warnings": "Risk of low blood sugar."
        },
        "sitagliptin": {
            "brand_name": "Januvia, Ziten",
            "indications": "Type 2 diabetes.",
            "side_effects": "Headache, upper respiratory infection, nausea.",
            "warnings": "Monitor for pancreatitis."
        },
        "empagliflozin": {
            "brand_name": "Jardiance, Glyxambi",
            "indications": "Type 2 diabetes, heart/kidney protection.",
            "side_effects": "Urinary tract infection, yeast infection, dehydration.",
            "warnings": "May cause genital yeast infections."
        },
        "insulin": {
            "brand_name": "Humalog, Lantus",
            "indications": "Type 1 and Type 2 diabetes.",
            "side_effects": "Low blood sugar, weight gain, injection site reactions.",
            "warnings": "Risk of hypoglycemia. Store properly."
        },

        # === Hypertension & Heart ===
        "amlodipine": {
            "brand_name": "Amlogard, Amlodac",
            "indications": "High blood pressure, angina.",
            "side_effects": "Ankle swelling, headache, dizziness, flushing.",
            "warnings": "May cause ankle swelling."
        },
        "telmisartan": {
            "brand_name": "Telma, Telmikind",
            "indications": "Hypertension, diabetic kidney protection.",
            "side_effects": "Dizziness, fatigue, back pain.",
            "warnings": "Avoid in pregnancy."
        },
        "losartan": {
            "brand_name": "Losar, Arbiflow",
            "indications": "High blood pressure, heart failure.",
            "side_effects": "Dizziness, fatigue, cough (less than ACE inhibitors).",
            "warnings": "Monitor kidney function."
        },
        "atenolol": {
            "brand_name": "Aten, Tenormin",
            "indications": "Hypertension, angina, post-heart attack.",
            "side_effects": "Fatigue, cold hands/feet, slow heartbeat.",
            "warnings": "Do not stop suddenly."
        },
        "metoprolol": {
            "brand_name": "Metolar, Betaloc",
            "indications": "Hypertension, arrhythmia, heart failure.",
            "side_effects": "Tiredness, dizziness, slow pulse.",
            "warnings": "Avoid abrupt withdrawal."
        },
        "enalapril": {
            "brand_name": "Enam, Envas",
            "indications": "Hypertension, heart failure.",
            "side_effects": "Dry cough, dizziness, high potassium.",
            "warnings": "May cause dry cough."
        },
        "ramipril": {
            "brand_name": "Cardace, Ramistar",
            "indications": "Hypertension, post-heart attack.",
            "side_effects": "Dry cough, dizziness, fatigue.",
            "warnings": "Avoid in pregnancy."
        },
        "hydrochlorothiazide": {
            "brand_name": "Hytel, Dyzide",
            "indications": "Hypertension, edema.",
            "side_effects": "Low potassium, dizziness, increased urination.",
            "warnings": "May lower potassium."
        },
        "furosemide": {
            "brand_name": "Lasix, Frusemide",
            "indications": "Edema, heart failure.",
            "side_effects": "Dehydration, low potassium, dizziness.",
            "warnings": "Causes frequent urination."
        },
        "atorvastatin": {
            "brand_name": "Atorva, Storvas",
            "indications": "High cholesterol, heart attack prevention.",
            "side_effects": "Muscle pain, liver enzyme rise, headache.",
            "warnings": "Monitor liver enzymes."
        },
        "rosuvastatin": {
            "brand_name": "Crestor, Rosuvas",
            "indications": "High cholesterol.",
            "side_effects": "Headache, muscle pain, nausea.",
            "warnings": "Avoid grapefruit juice."
        },

        # === Respiratory ===
        "salbutamol": {
            "brand_name": "Asthalin, Ventolin",
            "indications": "Asthma, bronchospasm.",
            "side_effects": "Tremor, headache, fast heartbeat.",
            "warnings": "Overuse may worsen symptoms."
        },
        "levosalbutamol": {
            "brand_name": "Levolin",
            "indications": "Asthma, COPD.",
            "side_effects": "Mild tremor, headache, nervousness.",
            "warnings": "Use as directed."
        },
        "montelukast": {
            "brand_name": "Montair, Romilast",
            "indications": "Asthma, allergic rhinitis.",
            "side_effects": "Headache, abdominal pain, mood changes (rare).",
            "warnings": "May cause mood changes."
        },
        "budesonide": {
            "brand_name": "Pulmicort",
            "indications": "Asthma prevention.",
            "side_effects": "Hoarseness, oral thrush, cough.",
            "warnings": "Rinse mouth after use."
        },
        "fluticasone": {
            "brand_name": "Flohale, Flonase",
            "indications": "Asthma, nasal allergies.",
            "side_effects": "Nasal irritation, headache, nosebleed (nasal form).",
            "warnings": "Not for acute attacks."
        },

        # === Cough & Cold ===
        "chlorpheniramine": {
            "brand_name": "Coricidin, Allercet",
            "indications": "Allergic rhinitis, cold symptoms.",
            "side_effects": "Drowsiness, dry mouth, blurred vision.",
            "warnings": "Causes drowsiness."
        },
        "phenylephrine": {
            "brand_name": "Sudafed PE",
            "indications": "Nasal congestion.",
            "side_effects": "Increased blood pressure, restlessness, insomnia.",
            "warnings": "Avoid in high BP."
        },
        "dextromethorphan": {
            "brand_name": "D'Cold, Zedex",
            "indications": "Dry cough suppression.",
            "side_effects": "Dizziness, drowsiness, nausea.",
            "warnings": "Do not exceed dose."
        },
        "guaifenesin": {
            "brand_name": "Mucinac, Grilinctus",
            "indications": "Loosens mucus in chesty cough.",
            "side_effects": "Nausea, vomiting, dizziness.",
            "warnings": "Drink plenty of water."
        },

        # === Vitamins & Supplements ===
        "vitamin c": {
            "brand_name": "Celin, Limcee",
            "indications": "Immunity, scurvy prevention.",
            "side_effects": "Diarrhea (in high doses), stomach cramps.",
            "warnings": "High doses may cause diarrhea."
        },
        "vitamin d3": {
            "brand_name": "D Rise, Calcirol",
            "indications": "Bone health, calcium absorption.",
            "side_effects": "Nausea, constipation (if overdosed).",
            "warnings": "Take with calcium if deficient."
        },
        "calcium carbonate": {
            "brand_name": "Shelcal, Calbo",
            "indications": "Calcium deficiency, osteoporosis.",
            "side_effects": "Constipation, gas, bloating.",
            "warnings": "Take after meals."
        },
        "folic acid": {
            "brand_name": "Folvite, Fol5",
            "indications": "Pregnancy, anemia prevention.",
            "side_effects": "Rare: allergic reactions, nausea.",
            "warnings": "Essential before and during pregnancy."
        },
        "iron": {
            "brand_name": "Fefol, Livogen",
            "indications": "Iron-deficiency anemia.",
            "side_effects": "Constipation, black stools, nausea.",
            "warnings": "Take on empty stomach. Causes black stools."
        },
        "zinc": {
            "brand_name": "Zincovit, Becozinc",
            "indications": "Immunity, wound healing.",
            "side_effects": "Nausea, metallic taste, stomach upset.",
            "warnings": "Do not exceed 40mg/day."
        },

        # === Skin & Allergy ===
        "cetirizine": {
            "brand_name": "Cetzine, Alerid",
            "indications": "Allergies, hives, itching.",
            "side_effects": "Mild drowsiness, dry mouth, fatigue.",
            "warnings": "May cause mild drowsiness."
        },
        "levocetirizine": {
            "brand_name": "Xyzal, Levokast",
            "indications": "Allergic rhinitis, chronic urticaria.",
            "side_effects": "Mild drowsiness, dry mouth, headache.",
            "warnings": "Less drowsy than cetirizine."
        },
        "fexofenadine": {
            "brand_name": "Allegra, Telfast",
            "indications": "Seasonal allergies.",
            "side_effects": "Headache, dizziness, nausea.",
            "warnings": "Non-drowsy."
        },
        "hydrocortisone cream": {
            "brand_name": "Efcort, Cortisol",
            "indications": "Skin inflammation, itching.",
            "side_effects": "Skin thinning, irritation (with long-term use).",
            "warnings": "Avoid on face/long-term use."
        },
        "clotrimazole": {
            "brand_name": "Candid, Clotrin",
            "indications": "Fungal skin infections (ringworm, athlete’s foot).",
            "side_effects": "Mild burning, redness, itching at application site.",
            "warnings": "Use full course."
        },
        "miconazole": {
            "brand_name": "Daktarin",
            "indications": "Fungal infections.",
            "side_effects": "Skin irritation, burning sensation.",
            "warnings": "Avoid in pregnancy unless advised."
        },
        "ketoconazole": {
            "brand_name": "Keto",
            "indications": "Severe fungal infections, dandruff.",
            "side_effects": "Skin irritation, redness, itching.",
            "warnings": "Oral form has liver risk."
        },
        "calamine": {
            "brand_name": "Calapure, Lacto Calamine",
            "indications": "Itching, sunburn, chickenpox.",
            "side_effects": "Rare: skin dryness, irritation.",
            "warnings": "For external use only."
        },

        # === Eye & Ear ===
        "moxifloxacin eye drops": {
            "brand_name": "Moxicip, Vigamox",
            "indications": "Bacterial conjunctivitis.",
            "side_effects": "Eye irritation, dryness, blurred vision.",
            "warnings": "Do not touch dropper to eye."
        },
        "tobramycin eye drops": {
            "brand_name": "Tobrex",
            "indications": "Eye infections.",
            "side_effects": "Eye stinging, redness, eyelid swelling.",
            "warnings": "Complete full course."
        },
        "sodium chloride": {
            "brand_name": "Normal Saline",
            "indications": "Nasal/eye irrigation, dry eyes.",
            "side_effects": "Mild stinging (rare).",
            "warnings": "Sterile use only."
        },
        "ciprofloxacin ear drops": {
            "brand_name": "Ciplox",
            "indications": "Outer ear infection (swimmer’s ear).",
            "side_effects": "Ear discomfort, itching, temporary hearing changes.",
            "warnings": "Do not use if eardrum is perforated."
        },

        # === Common Brand Aliases (India) ===
        "crocin": { 
            "brand_name": "Crocin", 
            "indications": "Fever, pain.", 
            "side_effects": "Rare: liver damage (if overdosed), skin rash.",
            "warnings": "Contains paracetamol." 
        },
        "dolo": { 
            "brand_name": "Dolo", 
            "indications": "Headache, fever.", 
            "side_effects": "Rare: liver damage, rash.",
            "warnings": "Contains paracetamol." 
        },
        "nicip": { 
            "brand_name": "Nicip", 
            "indications": "Pain, inflammation.", 
            "side_effects": "Stomach upset, dizziness, liver enzyme changes.",
            "warnings": "Contains nimesulide." 
        },
        "flexon": { 
            "brand_name": "Flexon", 
            "indications": "Pain, fever.", 
            "side_effects": "Stomach pain, nausea, dizziness.",
            "warnings": "Contains ibuprofen + paracetamol." 
        },
        "enzoflam": { 
            "brand_name": "Enzoflam", 
            "indications": "Muscle pain, swelling.", 
            "side_effects": "Stomach upset, dizziness, rash.",
            "warnings": "Contains diclofenac + serratiopeptidase." 
        },
        "rabekind": { 
            "brand_name": "Rabekind", 
            "indications": "Acidity, heartburn.", 
            "side_effects": "Nausea, headache, dizziness.",
            "warnings": "Contains rabeprazole." 
        },
        "pantocid": { 
            "brand_name": "Pantocid", 
            "indications": "GERD, ulcers.", 
            "side_effects": "Headache, nausea, constipation.",
            "warnings": "Contains pantoprazole." 
        },
        "azee": { 
            "brand_name": "Azee", 
            "indications": "Bacterial infections.", 
            "side_effects": "Nausea, abdominal pain, diarrhea.",
            "warnings": "Contains azithromycin." 
        },
        "monocef": { 
            "brand_name": "Monocef", 
            "indications": "Typhoid, UTI.", 
            "side_effects": "Diarrhea, nausea, headache.",
            "warnings": "Contains cefixime." 
        },
        "telma": { 
            "brand_name": "Telma", 
            "indications": "High blood pressure.", 
            "side_effects": "Dizziness, fatigue, back pain.",
            "warnings": "Contains telmisartan." 
        },
        "amlogard": { 
            "brand_name": "Amlogard", 
            "indications": "Hypertension, chest pain.", 
            "side_effects": "Ankle swelling, headache, flushing.",
            "warnings": "Contains amlodipine." 
        },

        # === Others ===
        "serratiopeptidase": { 
            "brand_name": "Serrapeptase", 
            "indications": "Reduces swelling, post-surgery pain.", 
            "side_effects": "Nausea, diarrhea, muscle pain.",
            "warnings": "Use with anti-inflammatory." 
        },
        "ambroxol": { 
            "brand_name": "Mucosolvan, Ambrodil", 
            "indications": "Cough with mucus.", 
            "side_effects": "Nausea, vomiting, stomach upset.",
            "warnings": "Drink water after dose." 
        },
        "albendazole": { 
            "brand_name": "Albenza, Zentel", 
            "indications": "Worm infections.", 
            "side_effects": "Abdominal pain, headache, dizziness.",
            "warnings": "Take with fatty meal." 
        },
        "levothyroxine": { 
            "brand_name": "Thyronorm", 
            "indications": "Hypothyroidism.", 
            "side_effects": "Nervousness, headache, sweating, weight loss.",
            "warnings": "Take on empty stomach." 
        },
        "clopidogrel": { 
            "brand_name": "Clopilet", 
            "indications": "Prevents blood clots (post-stent).", 
            "side_effects": "Bleeding, bruising, stomach pain.",
            "warnings": "Bleeding risk." 
        },
        "warfarin": { 
            "brand_name": "Warf", 
            "indications": "Blood thinner.", 
            "side_effects": "Bleeding, bruising, hair loss.",
            "warnings": "Regular INR monitoring needed." 
        }
    }

    return mock_data.get(drug_name.lower(), None)


# ================================
# STREAMLIT APP
# ================================
st.set_page_config(page_title="My Medicine Helper", layout="centered")
st.title("💊 My Medicine Helper")
st.write("Enter a **generic drug name** or **common brand name** (e.g., *paracetamol*, *crocin*, *azee*) and click **Search**.")

drug_input = st.text_input("Enter drug name:", placeholder="e.g., paracetamol, rabekind, azee")

if st.button("Search"):
    if drug_input.strip() == "":
        st.warning("Please enter a drug name.")
    else:
        result = get_drug_info(drug_input.strip())
        if result:
            st.success(f"**Brand Name(s):** {result['brand_name']}")
            st.info(f"**Indications:** {result['indications']}")
            st.error(f"**Common Side Effects:** {result['side_effects']}")
            st.warning(f"**Warnings:** {result['warnings']}")
        else:
            st.error("Sorry, I don't have information for this drug yet.")
            st.info("Try common drugs like: **paracetamol, azithromycin, pantoprazole, crocin, or enzoflam**.")

st.markdown("---")
st.warning("⚠️ **DISCLAIMER**: This is a learning project with simplified, mock data. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always consult a doctor before taking any medicine.")
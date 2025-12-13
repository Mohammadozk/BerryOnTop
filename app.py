import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Berry On Top 🍓",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# CSS Styling
st.markdown("""
<style>
.mobile-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: white;
    border-top: 1px solid #ddd;
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 70px;
    z-index: 9999;
}

.nav-btn {
    background: none;
    border: none;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
}

.floating-order {
    position: fixed;
    bottom: 35px;
    left: 50%;
    transform: translateX(-50%);
    background: #c8102e;
    color: white;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    border: none;
    font-size: 26px;
    box-shadow: 0px 6px 12px rgba(0,0,0,0.3);
    cursor: pointer;
    z-index: 10000;
}

.floating-order:hover {
    background: #ff3c4e;
}

.contact-float {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #ff1744;
    color: white;
    padding: 15px 25px;
    border-radius: 50px;
    font-weight: bold;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    z-index: 999;
}

@media (min-width: 900px) {
    .mobile-nav, .floating-order {
        display: none;
    }
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

[data-testid="stAppViewContainer"] {
    background-image: url("https://i.pinimg.com/1200x/76/18/fe/7618fe761344a9ba3d40386ba48ccf5d.jpg");
}

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-color: rgba(0,0,0,0.4);
    z-index: 0;
}

html, body, [class*="css"] {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000000;
    font-family: 'Cursive', 'Brush Script MT', sans-serif;
}

h1, h2, h3, h4, h5, h6, label, .stTextInput label, .stSelectbox label, .handwriting, .packages-title, .packages-subtitle, .package-name, .package-details {
    color: #ffffff !important;
    text-shadow: 2px 2px 4px #000 !important;
    font-family: 'Cursive', 'Brush Script MT', sans-serif;
}

.stButton>button {
    background-color: #c8102e;
    color: #fff; 
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 25px;
    box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
}

.stButton>button:hover {
    background-color: #ff3c4e;
}

.stTextInput>div>div>input, 
.stTextArea>div>div>textarea, 
.stSelectbox>div>div>div {
    background-color: rgba(255,255,255,0.9) !important;
    color: #000 !important;
    border: 2px solid #fff;
    border-radius: 5px;
}

.stSelectbox>div>div>div>div {
    color: #000 !important;
    text-shadow: none !important;
}

[data-baseweb="select"] div {
    color: #000 !important;
}

[data-baseweb="select"] option {
    color: #000 !important;
    background-color: #fff !important;
}

::placeholder {
    color: rgba(0,0,0,0.5);
}

.stButton>button {
    width: 100%;
    max-width: 200px;
    height: 60px;
    font-size: 18px;
    background-color: #c8102e;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
    margin: 5px auto;
    display: block;
}

.stButton>button:hover {
    background-color: #ff3c4e;
}

@media only screen and (max-width: 600px) {
    .stButton>button {
        font-size: 12px;
        height: 40px;
        width: 70%;
        padding: 5px 15px !important;
        margin: 8px auto;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="mobile-nav">
    <button class="nav-btn" onclick="window.location.href='?page=Home'">🏠 Home</button>
    <button class="nav-btn" onclick="window.location.href='?page=Gallery'">📸 Gallery</button>
    <button class="nav-btn" onclick="window.location.href='?page=Contact'">📞 Contact</button>
</div>

<button class="floating-order" onclick="window.location.href='?page=Order'">
    🛒
</button>

<div class="contact-float">
    📞 Contact: +961 71 184 268
</div>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "page" in st.query_params:
    st.session_state.page = st.query_params["page"][0]

for key in ["name", "phone", "delivery", "notes"]:
    if key not in st.session_state:
        st.session_state[key] = ""

if "gallery_page" not in st.session_state:
    st.session_state.gallery_page = 1

# Navigation Function
def go_to_page(page_name):
    st.session_state.page = page_name
    st.query_params["page"] = page_name

# ==================== HOME PAGE ====================
if st.session_state.page == "Home":
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-size: 70px; margin:0; letter-spacing:2px;'>Berry on Top</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-size: 32px; color:#FFB6C1; margin:10px 0; font-weight:bold;'>Delicious Desserts</h3>", unsafe_allow_html=True)
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1,1,1,1], gap="small")
    with col1:
        if st.button("🎂 Order Cakes & Desserts"):
            go_to_page("Order")
    with col2:
        if st.button("🎁 View Packages"):
            go_to_page("Packages")
    with col3:
        if st.button("📸 Gallery"):
            go_to_page("Gallery")
    with col4:
        if st.button("📞 Contact Us"):
            go_to_page("Contact")

# ==================== ORDER PAGE ====================
elif st.session_state.page == "Order":
    st.markdown("<h1>Place Your Orders</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Cakes Section
    st.markdown("<h2>🎂 Cakes</h2>", unsafe_allow_html=True)
    option = st.multiselect("Options Available:", ["Cake"])

    if "Cake" in option:
        real_fake = st.selectbox("Real or Fake Cake", ["Real Cake", "Fake Cake"])
        cake_qty = st.number_input("Cake Quantity", min_value=1, value=1, key="cake_qty")

        if real_fake == "Real Cake":
            shape = st.selectbox("Shapes", ["Round", "Oval","Heart"])
            flavors = st.selectbox("Flavors Available", ["Nutella", "Ferrero Rocher", "Vanilla", "Vanilla & Hazelnut", "Lotus"])
            size = st.selectbox("Sizes Available", ["3 people", "5 people", "10 people", "15 people", "20 people","25 people","30 people","40 people","50 people"])
            cake_design = st.selectbox("Design", ["Simple", "Custom Design"])
            if cake_design == "Custom Design":
                custom_details = st.text_area("Describe your custom design")
            else:
                custom_details = ""
        else:
            shape = st.selectbox("Fake Cake Shape", ["Round", "Oval", "Heart", "Square", "Custom Design"])
            color = st.selectbox("Color Available", ["Blue", "Baby Blue", "Red", "Black", "White", "Pink", "Purple", "Burgundy", "Gold", "Silver", "Rose Gold", "Mint", "Peach", "Grey", "Navy Blue", "Baby Pink", "Pastel Purple", "Pastel Yellow", "(Custom Theme)"])
            layers = st.selectbox("Layers", ["1 Layer", "2 Layers", "3 Layers", "4 Layers"])

    st.markdown("---")
    
    # Desserts Section
    st.markdown("<h2>🍰 Desserts</h2>", unsafe_allow_html=True)
    option1 = st.multiselect("Options Available:", ["Cookies", "Brownies", "Donuts", "Cheesecakes", "Cake cups", "Eclairs", "Popsicles"])

    popsicle_type = ""
    eclair_type = ""
    cakecups_type = ""
    cheesecake_type = ""
    donuts_type = ""
    cookies_type = ""
    brownies_type = ""

    if "Popsicles" in option1:
        popsicle_type = st.selectbox("Popsicles", ["Simple – $2.5", "3D Design – $3"])
        popsicle_qty = st.number_input("Popsicles Quantity", min_value=1, value=1, key="popsicle_qty")
    else:
        popsicle_qty = 0

    if "Eclairs" in option1:
        eclair_type = st.selectbox("Éclairs", ["Simple – $2", "3D Design – $2.5"])
        eclair_qty = st.number_input("Éclairs Quantity", min_value=1, value=1, key="eclair_qty")
    else:
        eclair_qty = 0

    if "Cake cups" in option1:
        cakecups_type = st.selectbox("Cake Cups (per dozen)", ["Nutella - $30", "Ferrero – $30", "Fraisier – $30", "Red Velvet – $36"])
        cakecups_qty = st.number_input("Cake Cups Quantity (dozen)", min_value=1, value=1, key="cakecups_qty")
    else:
        cakecups_qty = 0

    if "Cheesecakes" in option1:
        cheesecake_type = st.selectbox("Cheesecakes (per piece)", ["Simple – $2.5", "3D Design – $3.0"])
        cheesecake_qty = st.number_input("Cheesecakes Quantity", min_value=1, value=1, key="cheesecake_qty")
    else:
        cheesecake_qty = 0

    if "Donuts" in option1:
        donuts_type = st.selectbox("Donuts (per piece)", ["Simple – $2"])
        donuts_qty = st.number_input("Donuts Quantity", min_value=1, value=1, key="donuts_qty")
    else:
        donuts_qty = 0

    if "Cookies" in option1:
        cookies_type = st.selectbox("Cookies (per piece)", ["Simple – $2.5", "Decorated - $3.0"])
        cookies_qty = st.number_input("Cookies Quantity", min_value=1, value=1, key="cookies_qty")
    else:
        cookies_qty = 0

    if "Brownies" in option1:
        brownies_type = st.selectbox("Brownies (per piece)", ["Simple – $2", "3D Flower – $2.5"])
        brownies_qty = st.number_input("Brownies Quantity", min_value=1, value=1, key="brownies_qty")
    else:
        brownies_qty = 0

    st.markdown("---")
    
    # Customer Information Section
    st.markdown("<h2>📝 Your Information</h2>", unsafe_allow_html=True)
    st.session_state.name = st.text_input("Full Name*", value=st.session_state.name)
    st.session_state.phone = st.text_input("Phone Number*", value=st.session_state.phone)
    st.session_state.delivery = st.text_area("Delivery Address", value=st.session_state.delivery)
    st.session_state.notes = st.text_area("Special Instructions (optional)", value=st.session_state.notes)

    # Order Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📩 Send Order via WhatsApp"):
            if st.session_state.name.strip() != "" and st.session_state.phone.strip() != "":
                message = f"Hello Berry On Top! 🍓\n\nMy Order:\n"

                if "Cake" in option:
                    message += f"- {real_fake} Cake (Quantity: {cake_qty})\n"
                    if real_fake == "Real Cake":
                        message += f"  Shape: {shape}\n  Flavor: {flavors}\n  Size: {size}\n  Design: {cake_design}\n"
                        if cake_design == "Custom Design":
                            message += f"  Custom Details: {custom_details}\n"
                    if real_fake == "Fake Cake":
                        message += f"  Layers: {layers}\n  Color: {color}\n"

                for dessert, value, qty in [("Popsicles", popsicle_type, popsicle_qty), ("Éclairs", eclair_type, eclair_qty), ("Cake cups", cakecups_type, cakecups_qty),
                                       ("Cheesecakes", cheesecake_type, cheesecake_qty), ("Donuts", donuts_type, donuts_qty), ("Cookies", cookies_type, cookies_qty), ("Brownies", brownies_type, brownies_qty)]:
                    if value:
                        message += f"- {dessert}: {value} x{qty}\n"

                message += f"\n📝 Name: {st.session_state.name}\n📞 Phone: {st.session_state.phone}\nDelivery: {st.session_state.delivery}"
                if st.session_state.notes:
                    message += f"\n💬 Notes: {st.session_state.notes}"

                whatsapp_link = f"https://wa.me/96171184268?text={urllib.parse.quote(message)}"
                st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:#25D366;color:white;padding:15px 30px;border:none;border-radius:10px;font-size:18px;">💬 Send Order via WhatsApp</button></a>', unsafe_allow_html=True)
            else:
                st.error("❌ Please fill in your name and phone number!")
    
    with col2:
        if st.button("⬅️ Back to Home"):
            go_to_page("Home")

# ==================== PACKAGES PAGE ====================
elif st.session_state.page == "Packages":
    st.markdown('<h1 class="packages-title" style="font-size: 80px; text-align:center;">Party Packages</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="packages-subtitle" style="font-size: 50px; text-align:center; font-style:italic;">Delicious Desserts</h2>', unsafe_allow_html=True)
    
    packages = {
        "Small Party ($120)": "1 Custom Cake (7 people), 12 Cookies, 12 Brownies, 12 Donuts",
        "Medium Party ($170)": "1 Custom Cake (15 people), 24 Cookies, 12 Brownies, 1 Donuts Tower, 12 Eclairs",
        "Large Party ($350)": "1 Custom Cake (30 people), 24 Cookies, 24 Brownies, 1 Donuts Tower, 1 Eclair Tower, 24 Popsicles"
    }

    for name, details in packages.items():
        st.markdown(f'''
            <div style="
                background-color: rgba(0, 0, 0, 0.5); 
                padding: 30px; 
                border-radius: 20px; 
                margin: 20px auto; 
                max-width: 900px;
            ">
                <h2 style="font-size: 60px; color:#ffffff; text-align:center; text-shadow: 2px 2px 6px #000;">{name}</h2>
                <p style="font-size: 45px; color:#ffffff; text-align:center; text-shadow: 2px 2px 6px #000;">{details}</p>
            </div>
        ''', unsafe_allow_html=True)
        if st.button(f"📩 Order

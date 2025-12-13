import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Berry On Top 🍓",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&family=Dancing+Script:wght@400;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.mobile-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: white;
    border-top: 2px solid #FFB6C1;
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 70px;
    z-index: 9999;
}

.nav-btn {
    background: none;
    border: none;
    font-size: 12px;
    font-weight: bold;
    cursor: pointer;
    transition: transform 0.2s;
}

.nav-btn:hover {
    transform: scale(1.1);
}

.floating-order {
    position: fixed;
    bottom: 35px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, #c8102e, #ff3c4e);
    color: white;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    border: none;
    font-size: 28px;
    box-shadow: 0px 8px 16px rgba(200, 16, 46, 0.4);
    cursor: pointer;
    z-index: 10000;
    animation: pulse 2s infinite;
}

.floating-order:hover {
    transform: translateX(-50%) scale(1.1);
}

@keyframes pulse {
    0%, 100% { transform: translateX(-50%) scale(1); }
    50% { transform: translateX(-50%) scale(1.05); }
}

.contact-float {
    position: fixed;
    bottom: 90px;
    right: 20px;
    background-color: #ff1744;
    color: white;
    padding: 12px 20px;
    border-radius: 50px;
    font-size: 12px;
    font-weight: bold;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
    z-index: 999;
    text-align: center;
}

@media (min-width: 900px) {
    .mobile-nav, .floating-order, .contact-float { display: none; }
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

[data-testid="stAppViewContainer"] {
    background-image: url("https://i.pinimg.com/1200x/76/18/fe/7618fe761344a9ba3d40386ba48ccf5d.jpg");
    background-attachment: fixed;
}

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-color: rgba(0,0,0,0.45);
    z-index: 0;
}

html, body, [class*="css"] {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000000;
    font-family: 'Caveat', 'Dancing Script', cursive;
}

h1, h2, h3, h4, h5, h6, label {
    color: #ffffff !important;
    text-shadow: 2px 2px 4px #000 !important;
    font-family: 'Caveat', 'Dancing Script', cursive;
    font-weight: 700;
}

.packages-title {
    color: #ffffff !important;
    text-shadow: 3px 3px 8px #000 !important;
    font-family: 'Dancing Script', cursive !important;
    font-weight: 700 !important;
    letter-spacing: 3px;
}

.packages-subtitle {
    color: #FFB6C1 !important;
    text-shadow: 2px 2px 6px #000 !important;
    font-family: 'Caveat', cursive !important;
    font-weight: 400 !important;
}

.package-card {
    background: linear-gradient(135deg, rgba(0, 0, 0, 0.7), rgba(200, 16, 46, 0.2));
    padding: 25px;
    border-radius: 20px;
    margin: 20px 0;
    border: 3px solid #FFB6C1;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.6);
    backdrop-filter: blur(10px);
    transition: transform 0.3s, box-shadow 0.3s;
}

.package-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 15px 35px rgba(200, 16, 46, 0.4);
}

.package-name {
    color: #ffffff !important;
    text-shadow: 2px 2px 6px #000 !important;
    font-family: 'Dancing Script', cursive !important;
    font-weight: 700 !important;
    font-size: 26px !important;
    text-align: center;
    margin: 0 0 15px 0;
}

.package-details {
    color: #ffffff !important;
    text-shadow: 1px 1px 3px #000 !important;
    font-family: 'Caveat', cursive !important;
    font-size: 18px !important;
    text-align: center;
    line-height: 1.8;
}

.stButton>button {
    background: linear-gradient(135deg, #c8102e, #ff3c4e);
    color: #fff !important; 
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 28px !important;
    box-shadow: 0px 6px 12px rgba(200, 16, 46, 0.4);
    font-family: 'Caveat', cursive !important;
    font-size: 16px !important;
    border: none !important;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: none;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #ff3c4e, #ff6b7a);
    transform: translateY(-3px);
    box-shadow: 0px 10px 20px rgba(200, 16, 46, 0.5);
}

.stButton>button:active {
    transform: translateY(-1px);
}

.stTextInput>div>div>input, 
.stTextArea>div>div>textarea, 
.stSelectbox>div>div>div {
    background-color: rgba(255,255,255,0.98) !important;
    color: #333 !important;
    border: 2px solid #FFB6C1 !important;
    border-radius: 10px !important;
    font-family: 'Caveat', cursive !important;
    font-size: 16px !important;
}

.stSelectbox>div>div>div>div {
    color: #333 !important;
    text-shadow: none !important;
}

[data-baseweb="select"] {
    color: #333 !important;
}

::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

.stMarkdown {
    padding: 0 10px;
}

@media only screen and (max-width: 480px) {
    .packages-title { font-size: 42px !important; }
    .packages-subtitle { font-size: 26px !important; }
    .package-card { padding: 18px; margin: 15px 8px; border: 2px solid #FFB6C1; }
    .package-name { font-size: 20px !important; margin-bottom: 10px; }
    .package-details { font-size: 15px !important; }
    
    .stButton>button {
        width: 85%;
        max-width: 280px;
        height: 48px;
        font-size: 13px;
        padding: 10px 18px !important;
        margin: 8px auto !important;
        display: block;
    }
    
    .mobile-nav { height: 75px; }
    .contact-float { font-size: 10px; padding: 10px 15px; }
    
    [data-testid="stAppViewContainer"] { padding-bottom: 95px; }
    
    h1 { font-size: 40px !important; }
    h2 { font-size: 24px !important; }
    h3 { font-size: 18px !important; }
}

@media only screen and (max-width: 640px) {
    h1 { font-size: 44px !important; }
    h2 { font-size: 26px !important; }
    
    .stTextInput>div>div>input { font-size: 14px !important; }
}

@media only screen and (min-width: 481px) and (max-width: 768px) {
    .stButton>button { width: 90%; max-width: 320px; height: 50px; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="mobile-nav">
    <button class="nav-btn" onclick="window.location.href='?page=Home'">🏠</button>
    <button class="nav-btn" onclick="window.location.href='?page=Gallery'">📸</button>
    <button class="nav-btn" onclick="window.location.href='?page=Contact'">📞</button>
</div>
<button class="floating-order" onclick="window.location.href='?page=Order'">🛒</button>
<div class="contact-float">📞<br>+961 71 184 268</div>
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

def go_to_page(page_name):
    st.session_state.page = page_name
    st.query_params["page"] = page_name

DESSERT_OPTIONS = {
    "Popsicles": ["Simple – $2.5", "3D Design – $3"],
    "Éclairs": ["Simple – $2", "3D Design – $2.5"],
    "Cake cups": ["Nutella - $30", "Ferrero – $30", "Fraisier – $30", "Red Velvet – $36"],
    "Cheesecakes": ["Simple – $2.5", "3D Design – $3.0"],
    "Donuts": ["Simple – $2"],
    "Cookies": ["Simple – $2.5", "Decorated - $3.0"],
    "Brownies": ["Simple – $2", "3D Flower – $2.5"]
}

PACKAGES = {
    "Small ($120)": "1 Custom Cake (7), 12 Cookies, 12 Brownies, 12 Donuts",
    "Medium ($170)": "1 Custom Cake (15), 24 Cookies, 12 Brownies, 1 Tower, 12 Eclairs",
    "Large ($350)": "1 Custom Cake (30), 24 Cookies, 24 Brownies, 1 Tower, 1 Tower, 24 Popsicles"
}

if st.session_state.page == "Home":
    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-size: 72px; letter-spacing: 3px;'>Berry on Top</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-size: 32px; color:#FFB6C1; margin-bottom: 10px;'>Delicious Desserts</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size: 18px; color: #FFB6C1;'>Handmade with Love & Fresh Ingredients</p>", unsafe_allow_html=True)
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4, gap="small")
    with col1:
        if st.button("🎂 Order Now"):
            go_to_page("Order")
    with col2:
        if st.button("🎁 View Packages"):
            go_to_page("Packages")
    with col3:
        if st.button("📸 See Gallery"):
            go_to_page("Gallery")
    with col4:
        if st.button("📞 Get in Touch"):
            go_to_page("Contact")
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 2px solid #FFB6C1;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Why Choose Berry On Top?</h3>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("<h4 style='text-align:center;'>✨ Premium Quality</h4><p style='text-align:center;'>Best ingredients sourced locally</p>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<h4 style='text-align:center;'>🎨 Custom Designs</h4><p style='text-align:center;'>Personalized for your special day</p>", unsafe_allow_html=True)
    with col_c:
        st.markdown("<h4 style='text-align:center;'>⚡ Quick Delivery</h4><p style='text-align:center;'>Fresh & on time, always</p>", unsafe_allow_html=True)

elif st.session_state.page == "Order":
    st.markdown("<h1>🎂 Place Your Order</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<h2>Real or Fake Cake?</h2>", unsafe_allow_html=True)
    option = st.radio("Select:", ["Cake"], horizontal=True)
    
    if option == "Cake":
        real_fake = st.selectbox("Type", ["Real Cake", "Fake Cake"])
        cake_qty = st.number_input("Quantity", min_value=1, value=1, key="cake_qty")

        if real_fake == "Real Cake":
            shape = st.selectbox("Shape", ["Round", "Oval", "Heart"])
            flavors = st.selectbox("Flavor", ["Nutella", "Ferrero Rocher", "Vanilla", "Vanilla & Hazelnut", "Lotus"])
            size = st.selectbox("Size (Servings)", ["3 people", "5 people", "10 people", "15 people", "20 people", "25 people", "30 people", "40 people", "50 people"])
            cake_design = st.selectbox("Design", ["Simple", "Custom Design"])
            custom_details = st.text_area("Custom Design Details", value="", placeholder="Describe your dream cake...") if cake_design == "Custom Design" else ""
        else:
            shape = st.selectbox("Shape", ["Round", "Oval", "Heart", "Square", "Custom"])
            color = st.selectbox("Color", ["Blue", "Baby Blue", "Red", "Black", "White", "Pink", "Purple", "Burgundy", "Gold", "Silver", "Rose Gold", "Mint", "Peach", "Grey", "Navy Blue", "Baby Pink", "Pastel Purple", "Pastel Yellow", "Custom"])
            layers = st.selectbox("Number of Layers", ["1", "2", "3", "4"])

    st.markdown("---")
    st.markdown("<h2>🍰 Add Extra Desserts</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Make your celebration even sweeter!</p>", unsafe_allow_html=True)
    option1 = st.multiselect("Select Desserts:", list(DESSERT_OPTIONS.keys()))

    dessert_orders = {}
    if option1:
        for dessert in option1:
            dessert_type = st.selectbox(f"{dessert} Type", DESSERT_OPTIONS[dessert], key=f"type_{dessert}")
            qty = st.number_input(f"{dessert} Quantity", min_value=1, value=1, key=f"qty_{dessert}")
            dessert_orders[dessert] = (dessert_type, qty)

    st.markdown("---")
    st.markdown("<h2>📝 Your Contact Information</h2>", unsafe_allow_html=True)
    st.session_state.name = st.text_input("Full Name*", value=st.session_state.name, placeholder="Enter your name")
    st.session_state.phone = st.text_input("Phone Number*", value=st.session_state.phone, placeholder="Enter your phone")
    st.session_state.delivery = st.text_area("Delivery Address", value=st.session_state.delivery, height=80, placeholder="Where should we deliver?")
    st.session_state.notes = st.text_area("Special Requests & Notes", value=st.session_state.notes, height=80, placeholder="Any special instructions?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Send Order via WhatsApp"):
            if st.session_state.name.strip() and st.session_state.phone.strip():
                message = "Hello Berry On Top! 🍓\n\n*My Order:*\n"
                message += f"- {real_fake} Cake x{cake_qty}\n"
                for dessert, (dtype, qty) in dessert_orders.items():
                    message += f"- {dessert}: {dtype} x{qty}\n"
                message += f"\n*Customer Details:*\n📝 Name: {st.session_state.name}\n📞 Phone: {st.session_state.phone}\n📍 Delivery: {st.session_state.delivery}"
                if st.session_state.notes:
                    message += f"\n💬 Notes: {st.session_state.notes}"
                
                link = f"https://wa.me/96171184268?text={urllib.parse.quote(message)}"
                st.markdown(f'<a href="{link}" target="_blank"><button style="background:linear-gradient(135deg,#25D366,#31a952);color:white;padding:12px 24px;border:none;border-radius:10px;font-size:16px;cursor:pointer;width:100%;">✅ Confirm Order</button></a>', unsafe_allow_html=True)
            else:
                st.error("❌ Please fill in your name and phone number!")
    with col2:
        if st.button("Back to Home"):
            go_to_page("Home")

elif st.session_state.page == "Packages":
    st.markdown('<h1 class="packages-title" style="text-align:center;">🎉 Party Packages</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="packages-subtitle" style="text-align:center;">Perfect for Every Celebration</h2>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size: 16px;'>Choose the perfect package for your special occasion</p>", unsafe_allow_html=True)
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    for name, details in PACKAGES.items():
        st.markdown(f'<div class="package-card"><h2 class="package-name">{name}</h2><p class="package-details">{details}</p></div>', unsafe_allow_html=True)
        if st.button(f"📦 Order Package {name}", key=f"pkg_{name}"):
            msg = f"Hello Berry On Top! 🍓\n\nI'm interested in the {name} Package:\n\n{details}\n\nPlease confirm availability and delivery options."
            link = f"https://wa.me/96171184268?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank"><button style="background:#25D366;color:white;padding:10px 20px;border:none;border-radius:8px;width:100%;cursor:pointer;font-weight:bold;">💬 Order via WhatsApp</button></a>', unsafe_allow_html=True)
        st.markdown("")

    st.markdown("---")
    if st.button("⬅️ Back to Home"):
        go_to_page("Home")

elif st.session_state.page == "Gallery":
    st.markdown("<h1>📸 Gallery</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Explore our amazing creations and get inspired!</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 2px solid #FFB6C1;'>", unsafe_allow_html=True)
    
    images = [["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop"] * 20,
              [f"https://via.placeholder.com/300x300?text=Dessert+{i}" for i in range(21, 41)],
              [f"https://via.placeholder.com/300x300?text=Dessert+{i}" for i in range(41, 61)],
              [f"https://via.placeholder.com/300x300?text=Dessert+{i}" for i in range(61, 81)]]
    
    current = images[st.session_state.gallery_page - 1]
    st.markdown(f"<h3 style='text-align:center;'>Page {st.session_state.gallery_page} of 4</h3>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, img in enumerate(current):
        with cols[i % 4]:
            st.image(img, use_column_width=True)
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.session_state.gallery_page > 1 and st.button("⬅️ Previous"):
            st.session_state.gallery_page -= 1
            st.rerun()
    with c4:
        if st.session_state.gallery_page < 4 and st.button("Next ➡️"):
            st.session_state.gallery_page += 1
            st.rerun()
    
    st.markdown("---")
    if st.button("⬅️ Back to Home"):
        go_to_page("Home")

elif st.session_state.page == "Contact":
    st.markdown("<h1>📞 Contact Us</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 2px solid #FFB6C1;'>", unsafe_allow_html=True)
    
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.markdown("<h3>📱 Phone</h3>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#FFB6C1;'>+961 71 184 268</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 14px;'>Call or WhatsApp us for quick inquiries</p>", unsafe_allow_html=True)
    
    with col_info2:
        st.markdown("<h3>📧 Email</h3>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#FFB6C1;'>berryontop@gmail.com</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 14px;'>Email us for bulk orders</p>", unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #FFB6C1;'>", unsafe_allow_html=True)
    st.markdown("<h3>📍 Location</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#FFB6C1;'>South Lebanon</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px;'>Available for local delivery and custom orders</p>", unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #FFB6C1;'>", unsafe_allow_html=True)
    st.markdown("<h2>💌 Get in Touch!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 16px; line-height: 1.8;'>We'd absolutely love to hear from you! Whether you have a special request, custom cake idea, or just want to know more about our amazing desserts, don't hesitate to reach out. Our team is ready to make your celebration unforgettable!</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    if st.button("⬅️ Back to Home"):
        go_to_page("Home")


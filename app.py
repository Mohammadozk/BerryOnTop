import streamlit as st
import urllib.parse

# -------------------------------
# PAGE CONFIG (only once, top)
# -------------------------------
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

# -------------------------------
# SESSION STATE INIT
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

for key in ["name", "phone", "delivery", "notes"]:
    if key not in st.session_state:
        st.session_state[key] = ""
if "gallery_page" not in st.session_state:
    st.session_state.gallery_page = 1

# -------------------------------
# QUERY PARAM HANDLING
# -------------------------------
if "page" in st.query_params:
    st.session_state.page = st.query_params["page"][0]

# -------------------------------
# PAGE NAVIGATION FUNCTION
# -------------------------------
def go_to_page(page_name):
    st.session_state.page = page_name
    st.experimental_set_query_params(page=page_name)

# -------------------------------
# GLOBAL CSS / MOBILE NAV / FLOATING ORDER
# -------------------------------
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

@media (min-width: 900px) {
    .mobile-nav, .floating-order {
        display: none;
    }
}

/* Hide default Streamlit menu and footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# MOBILE NAV HTML
# -------------------------------
st.markdown("""
<div class="mobile-nav">
    <button class="nav-btn" onclick="window.location.href='?page=Home'">🏠 Home</button>
    <button class="nav-btn" onclick="window.location.href='?page=Gallery'">📸 Gallery</button>
    <button class="nav-btn" onclick="window.location.href='?page=Contact'">📞 Contact</button>
</div>

<button class="floating-order" onclick="window.location.href='?page=Order'">
    🛒
</button>
""", unsafe_allow_html=True)

# -------------------------------
# PAGE: HOME (skipped here, optional)
# -------------------------------

# -------------------------------
# PAGE: ORDER
# -------------------------------
if st.session_state.page == "Order":
    st.markdown("<h1>Place Your Orders</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h2>🎂 Cakes</h2>", unsafe_allow_html=True)

    option = st.multiselect("Options Available:", ["Cake"])

    if "Cake" in option:
        real_fake = st.selectbox("Real or Fake Cake", ["Real Cake", "Fake Cake"])
        cake_qty = st.number_input("Cake Quantity", min_value=1, value=1, key="cake_qty")

        if real_fake == "Real Cake":
            shape = st.selectbox("Shapes", ["Round", "Oval", "Heart"])
            flavors = st.selectbox("Flavors Available", ["Nutella", "Ferrero Rocher", "Vanilla", "Vanilla & Hazelnut", "Lotus"])
            size = st.selectbox("Sizes Available", ["3 people", "5 people", "10 people", "15 people", "20 people","25 people","30 people","40 people","50 people"])
            cake_design = st.selectbox("Design", ["Simple", "Custom Design"])
            custom_details = st.text_area("Describe your custom design") if cake_design == "Custom Design" else ""
        else:
            shape = st.selectbox("Fake Cake Shape", ["Round", "Oval", "Heart", "Square", "Custom Design"])
            color = st.selectbox("Color Available", [
                "Blue", "Baby Blue", "Red", "Black", "White", "Pink", "Purple",
                "Burgundy", "Gold", "Silver", "Rose Gold", "Mint", "Peach",
                "Grey", "Navy Blue", "Baby Pink", "Pastel Purple", "Pastel Yellow", "(Custom Theme)"])
            layers = st.selectbox("Layers", ["1 Layer", "2 Layers", "3 Layers", "4 Layers"])

    st.markdown("---")
    st.markdown("<h2>🍰 Desserts</h2>", unsafe_allow_html=True)
    option1 = st.multiselect("Options Available:", ["Cookies", "Brownies", "Donuts", "Cheesecakes", "Cake cups", "Eclairs", "Popsicles"])

    # Initialize dessert types and quantities
    popsicle_type = eclair_type = cakecups_type = cheesecake_type = donuts_type = cookies_type = brownies_type = ""
    popsicle_qty = eclair_qty = cakecups_qty = cheesecake_qty = donuts_qty = cookies_qty = brownies_qty = 0

    if "Popsicles" in option1:
        popsicle_type = st.selectbox("Popsicles", ["Simple – $2.5", "3D Design – $3"])
        popsicle_qty = st.number_input("Popsicles Quantity", min_value=1, value=1, key="popsicle_qty")

    if "Eclairs" in option1:
        eclair_type = st.selectbox("Éclairs", ["Simple – $2", "3D Design – $2.5"])
        eclair_qty = st.number_input("Éclairs Quantity", min_value=1, value=1, key="eclair_qty")

    if "Cake cups" in option1:
        cakecups_type = st.selectbox("Cake Cups (per dozen)", ["Nutella - $30", "Ferrero – $30", "Fraisier – $30", "Red Velvet – $36"])
        cakecups_qty = st.number_input("Cake Cups Quantity (dozen)", min_value=1, value=1, key="cakecups_qty")

    if "Cheesecakes" in option1:
        cheesecake_type = st.selectbox("Cheesecakes (per piece)", ["Simple – $2.5", "3D Design – $3.0"])
        cheesecake_qty = st.number_input("Cheesecakes Quantity", min_value=1, value=1, key="cheesecake_qty")

    if "Donuts" in option1:
        donuts_type = st.selectbox("Donuts (per piece)", ["Simple – $2"])
        donuts_qty = st.number_input("Donuts Quantity", min_value=1, value=1, key="donuts_qty")

    if "Cookies" in option1:
        cookies_type = st.selectbox("Cookies (per piece)", ["Simple – $2.5", "Decorated - $3.0"])
        cookies_qty = st.number_input("Cookies Quantity", min_value=1, value=1, key="cookies_qty")

    if "Brownies" in option1:
        brownies_type = st.selectbox("Brownies (per piece)", ["Simple – $2", "3D Flower – $2.5"])
        brownies_qty = st.number_input("Brownies Quantity", min_value=1, value=1, key="brownies_qty")

    st.markdown("---")
    st.markdown("<h2>📝 Your Information</h2>", unsafe_allow_html=True)
    st.session_state.name = st.text_input("Full Name*", value=st.session_state.name)
    st.session_state.phone = st.text_input("Phone Number*", value=st.session_state.phone)
    st.session_state.delivery = st.text_area("Delivery Address", value=st.session_state.delivery)
    st.session_state.notes = st.text_area("Special Instructions (optional)", value=st.session_state.notes)


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
        if st.button(f"📩 Order {name} via WhatsApp"):
            import urllib.parse
            message = f"Hello Berry On Top! 🍓\n\nI want to order the {name}:\n{details}"
            whatsapp_link = f"https://wa.me/96171184268?text={urllib.parse.quote(message)}"
            st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:#25D366;color:white;padding:20px 40px;border:none;border-radius:15px;font-size:30px;">💬 Send WhatsApp Order</button></a>', unsafe_allow_html=True)

    if st.button("⬅️ Back to Home"):
        go_to_page("Home")

elif st.session_state.page == "Gallery":
    st.markdown("<h1>Gallery</h1>", unsafe_allow_html=True)
    st.write("Check out our delicious creations!")
    gallery_images_page1 = [
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop",
    ]
    
    gallery_images_page2 = [
        "https://via.placeholder.com/300x300?text=Dessert+21",
        "https://via.placeholder.com/300x300?text=Dessert+22",
        "https://via.placeholder.com/300x300?text=Dessert+23",
        "https://via.placeholder.com/300x300?text=Dessert+24",
        "https://via.placeholder.com/300x300?text=Dessert+25",
        "https://via.placeholder.com/300x300?text=Dessert+26",
        "https://via.placeholder.com/300x300?text=Dessert+27",
        "https://via.placeholder.com/300x300?text=Dessert+28",
        "https://via.placeholder.com/300x300?text=Dessert+29",
        "https://via.placeholder.com/300x300?text=Dessert+30",
        "https://via.placeholder.com/300x300?text=Dessert+31",
        "https://via.placeholder.com/300x300?text=Dessert+32",
        "https://via.placeholder.com/300x300?text=Dessert+33",
        "https://via.placeholder.com/300x300?text=Dessert+34",
        "https://via.placeholder.com/300x300?text=Dessert+35",
        "https://via.placeholder.com/300x300?text=Dessert+36",
        "https://via.placeholder.com/300x300?text=Dessert+37",
        "https://via.placeholder.com/300x300?text=Dessert+38",
        "https://via.placeholder.com/300x300?text=Dessert+39",
        "https://via.placeholder.com/300x300?text=Dessert+40",
    ]
    
    gallery_images_page3 = [
        "https://via.placeholder.com/300x300?text=Dessert+41",
        "https://via.placeholder.com/300x300?text=Dessert+42",
        "https://via.placeholder.com/300x300?text=Dessert+43",
        "https://via.placeholder.com/300x300?text=Dessert+44",
        "https://via.placeholder.com/300x300?text=Dessert+45",
        "https://via.placeholder.com/300x300?text=Dessert+46",
        "https://via.placeholder.com/300x300?text=Dessert+47",
        "https://via.placeholder.com/300x300?text=Dessert+48",
        "https://via.placeholder.com/300x300?text=Dessert+49",
        "https://via.placeholder.com/300x300?text=Dessert+50",
        "https://via.placeholder.com/300x300?text=Dessert+51",
        "https://via.placeholder.com/300x300?text=Dessert+52",
        "https://via.placeholder.com/300x300?text=Dessert+53",
        "https://via.placeholder.com/300x300?text=Dessert+54",
        "https://via.placeholder.com/300x300?text=Dessert+55",
        "https://via.placeholder.com/300x300?text=Dessert+56",
        "https://via.placeholder.com/300x300?text=Dessert+57",
        "https://via.placeholder.com/300x300?text=Dessert+58",
        "https://via.placeholder.com/300x300?text=Dessert+59",
        "https://via.placeholder.com/300x300?text=Dessert+60",
    ]
    
    gallery_images_page4 = [
        "https://via.placeholder.com/300x300?text=Dessert+61",
        "https://via.placeholder.com/300x300?text=Dessert+62",
        "https://via.placeholder.com/300x300?text=Dessert+63",
        "https://via.placeholder.com/300x300?text=Dessert+64",
        "https://via.placeholder.com/300x300?text=Dessert+65",
        "https://via.placeholder.com/300x300?text=Dessert+66",
        "https://via.placeholder.com/300x300?text=Dessert+67",
        "https://via.placeholder.com/300x300?text=Dessert+68",
        "https://via.placeholder.com/300x300?text=Dessert+69",
        "https://via.placeholder.com/300x300?text=Dessert+70",
        "https://via.placeholder.com/300x300?text=Dessert+71",
        "https://via.placeholder.com/300x300?text=Dessert+72",
        "https://via.placeholder.com/300x300?text=Dessert+73",
        "https://via.placeholder.com/300x300?text=Dessert+74",
        "https://via.placeholder.com/300x300?text=Dessert+75",
        "https://via.placeholder.com/300x300?text=Dessert+76",
        "https://via.placeholder.com/300x300?text=Dessert+77",
        "https://via.placeholder.com/300x300?text=Dessert+78",
        "https://via.placeholder.com/300x300?text=Dessert+79",
        "https://via.placeholder.com/300x300?text=Dessert+80",
    ]
    
    all_pages = [gallery_images_page1, gallery_images_page2, gallery_images_page3, gallery_images_page4]
    current_images = all_pages[st.session_state.gallery_page - 1]
    
    st.markdown(f"<h3>Page {st.session_state.gallery_page} of 4</h3>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    for idx, img in enumerate(current_images):
        with cols[idx % 4]:
            st.image(img, use_column_width=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.session_state.gallery_page > 1:
            if st.button("⬅️ Previous"):
                st.session_state.gallery_page -= 1
                st.rerun()
    
    with col4:
        if st.session_state.gallery_page < 4:
            if st.button("Next ➡️"):
                st.session_state.gallery_page += 1
                st.rerun()
    
    if st.button("⬅️ Back to Home"):
        go_to_page("Home")

elif st.session_state.page == "Contact":
    st.markdown("<h1>Contact Us</h1>", unsafe_allow_html=True)
    st.write("📞 Phone: +961 71 184 268")
    st.write("📧 Email: berryontop@gmail.com")
    st.write("🏠 Address: south lebanon")

    if st.button("⬅️ Back to Home"):
        go_to_page("Home")


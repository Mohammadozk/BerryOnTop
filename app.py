import streamlit as st
import urllib.parse

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
  background-image: url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWm5ybnJ2eoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlbaWmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD/2Q==");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
html, body, [class*="css"] {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000000;
}

h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000000;
}

label, .stTextInput label, .stSelectbox label {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000000;
}

.handwriting {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000000;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
html, body, [class*="css"] {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000000;
}

h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
    text-shadow: 2px 2px 4px #000000;
}

label, .stTextInput label, .stSelectbox label {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000000;
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
.stTextArea>div>div>textarea {
    background-color: rgba(255,255,255,0.9) !important;
    color: #000 !important;
    border: 2px solid #fff;
    border-radius: 5px;
}

.stSelectbox>div>div>div {
    background-color: rgba(255,255,255,0.9) !important;
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

.handwriting {
    color: #fff;
    text-shadow: 2px 2px 4px #000;
    font-family: 'Cursive', 'Brush Script MT', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.sidebar-nav {
    position: fixed;
    left: 0;
    top: 0;
    width: 250px;
    height: 100vh;
    background: rgba(200, 16, 46, 0.95);
    padding: 20px;
    overflow-y: auto;
    z-index: 100;
}

.sidebar-nav h2 {
    color: #fff;
    text-align: center;
    margin-bottom: 30px;
    font-size: 24px;
    text-shadow: 2px 2px 4px #000;
}

.sidebar-nav button {
    width: 100%;
    background-color: #fff;
    color: #c8102e;
    border: none;
    padding: 12px;
    margin: 10px 0;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.3s;
}

.sidebar-nav button:hover {
    background-color: #FFB6C1;
    transform: translateX(5px);
}

main {
    margin-left: 250px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"

for key in ["name", "phone", "delivery", "notes"]:
    if key not in st.session_state:
        st.session_state[key] = ""
if "gallery_page" not in st.session_state:
    st.session_state.gallery_page = 1

st.markdown("""
<div class="sidebar-nav">
    <h2>🍓 Berry on Top</h2>
</div>
<main>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
with col2:
    if st.button("🎂 Order"):
        st.session_state.page = "Order"
with col3:
    if st.button("🎁 Packages"):
        st.session_state.page = "Packages"
with col4:
    if st.button("📸 Gallery"):
        st.session_state.page = "Gallery"
with col5:
    if st.button("📞 Contact"):
        st.session_state.page = "Contact"

prices = {
    "Cake": 0,
    "Cake cups": {"Nutella": 30, "Ferrero": 30, "Fresir": 30, "Red Velvet": 36},
    "Cookies": {"Chocolate Chip": 2.5, "Nutella Stuffed": 3},
    "Brownies": {"Classic": 2, "Nutella": 2.5, "Lotus": 2.5},
    "Donuts": {"Glazed": 2, "Chocolate": 2.5},
    "Cheesecakes": {"Classic": 2.5, "3D": 3},
    "Eclairs": {"Simple": 2, "3D": 2.5},
    "Popsicles": {"Simple": 2.5, "3D": 3}
}

st.header("📝 Your Information")
name = st.text_input("Full Name*")
phone = st.text_input("Phone Number*")
delivery = st.text_input("Delivery Address")
notes = st.text_area("Special Instructions (optional)")

st.header("🛒 Your Order")
option = st.multiselect(
    "What would you like to order?",
    ["Cake", "Cake cups", "Cookies", "Brownies", "Donuts", "Cheesecakes", "Eclairs", "Popsicles"]
)

total = 0
order_details = ""

if "Cake" in option:
    real_fake = st.selectbox("Real or Fake Cake", ["Real Cake", "Fake Cake"])
    if real_fake == "Real Cake":
        shape = st.selectbox("Shape", ["Round", "Square", "Heart"])
        flavors = st.selectbox("Flavor", ["Nutella", "Ferrero Rocher", "Vanilla", "Lotus"])
        size = st.selectbox("Size", ["3 people", "5 people", "10 people", "15 people", "20 people"])
        cake_price = st.number_input("Cake Price ($)", min_value=0.0, step=1.0)
        total += cake_price
        order_details += f"- Cake ({real_fake}) | {shape}, {flavors}, {size} — ${cake_price}\n"

if "Cake cups" in option:
    cakecups = st.selectbox("Cake Cups (Dozen)", list(prices["Cake cups"].keys()))
    price = prices["Cake cups"][cakecups]
    total += price
    order_details += f"- Cake Cups ({cakecups}) — ${price}\n"

if "Cookies" in option:
    cookies = st.selectbox("Cookies Type", list(prices["Cookies"].keys()))
    qty = st.number_input("Cookies Quantity", 1, 100)
    price = prices["Cookies"][cookies] * qty
    total += price
    order_details += f"- Cookies ({cookies}) x{qty} — ${price}\n"

if "Brownies" in option:
    brownies = st.selectbox("Brownies Type", list(prices["Brownies"].keys()))
    qty = st.number_input("Brownies Quantity", 1, 100)
    price = prices["Brownies"][brownies] * qty
    total += price
    order_details += f"- Brownies ({brownies}) x{qty} — ${price}\n"

if "Donuts" in option:
    donuts = st.selectbox("Donuts Type", list(prices["Donuts"].keys()))
    qty = st.number_input("Donuts Quantity", 1, 100)
    price = prices["Donuts"][donuts] * qty
    total += price
    order_details += f"- Donuts ({donuts}) x{qty} — ${price}\n"

if "Cheesecakes" in option:
    cheesecake = st.selectbox("Cheesecake Type", list(prices["Cheesecakes"].keys()))
    qty = st.number_input("Cheesecakes Quantity", 1, 100)
    price = prices["Cheesecakes"][cheesecake] * qty
    total += price
    order_details += f"- Cheesecakes ({cheesecake}) x{qty} — ${price}\n"

if "Eclairs" in option:
    eclair = st.selectbox("Éclairs Type", list(prices["Eclairs"].keys()))
    qty = st.number_input("Éclairs Quantity", 1, 100)
    price = prices["Eclairs"][eclair] * qty
    total += price
    order_details += f"- Éclairs ({eclair}) x{qty} — ${price}\n"

if "Popsicles" in option:
    popsicle = st.selectbox("Popsicles Type", list(prices["Popsicles"].keys()))
    qty = st.number_input("Popsicles Quantity", 1, 100)
    price = prices["Popsicles"][popsicle] * qty
    total += price
    order_details += f"- Popsicles ({popsicle}) x{qty} — ${price}\n"

st.subheader(f"💰 Total: ${total}")

if st.button("Submit Order via WhatsApp"):
    if name.strip() and phone.strip():
        message = f"""
Hello Berry On Top! 🍓

Name: {name}
Phone: {phone}
Delivery: {delivery}

Order:
{order_details}

Total: ${total}
"""
        if notes:
            message += f"\nNotes: {notes}"

        link = f"https://wa.me/96171184268?text={urllib.parse.quote(message)}"

        st.markdown(f"""
        <a href="{link}" target="_blank">
            <button style="background:#25D366;color:white;padding:15px 30px;border:none;border-radius:10px;font-size:18px;font-weight:bold;">
                💬 Send Order on WhatsApp
            </button>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ Name and phone are required")

elif st.session_state.page == "Packages":
    st.markdown("<h1>Party Packages</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-size: 36px; color:#FFB6C1; text-shadow: 2px 2px 4px #000; margin:10px 0 0 0; font-style:italic;'>Delicious Desserts</h3>", unsafe_allow_html=True)

    packages = {
        "Small Party ($120)": "1 Custom Cake (7 people), 12 Cookies, 12 Brownies, 12 Donuts",
        "Medium Party ($170)": "1 Custom Cake (15 people), 24 Cookies, 12 Brownies, 1 Donuts Tower, 12 Eclairs",
        "Large Party ($350)": "1 Custom Cake (30 people), 24 Cookies, 24 Brownies, 1 Donuts Tower, 1 Eclair Tower, 24 Popsicles"
    }

    for name, details in packages.items():
        st.markdown(f"<h3 style='color:#fff !important; text-shadow: 2px 2px 4px #000;'>{name}</h3>", unsafe_allow_html=True)
        st.markdown(f"<div style='color:#fff !important; text-shadow: 1px 1px 3px #000; font-size:16px; font-weight:bold;'>{details}</div>", unsafe_allow_html=True)
        if st.button(f"📩 Order {name} via WhatsApp"):
            message = f"Hello Berry On Top! 🍓\n\nI want to order the {name}:\n{details}"
            whatsapp_link = f"https://wa.me/96171184268?text={urllib.parse.quote(message)}"
            st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:#25D366;color:white;padding:15px 30px;border:none;border-radius:10px;font-size:18px;">💬 Send WhatsApp Order</button></a>', unsafe_allow_html=True)

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


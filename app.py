import streamlit as st
import urllib.parse

st.set_page_config(layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
  background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbbRx3u9QvaCigoDufC2sysUKR-gfifIMsnA&s");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

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

.summary-box {
    background-color: rgba(200, 16, 46, 0.3);
    border: 2px solid #FFB6C1;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
}

.total-box {
    background-color: rgba(255, 182, 193, 0.2);
    border: 3px solid #FFB6C1;
    border-radius: 10px;
    padding: 20px;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "gallery_page" not in st.session_state:
    st.session_state.gallery_page = 1

for key in ["name", "phone", "delivery", "notes"]:
    if key not in st.session_state:
        st.session_state[key] = ""

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

st.markdown("---")

if st.session_state.page == "Home":
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-size: 70px; color:#fff; text-shadow: 4px 4px 8px #000;'>Berry on Top</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-size: 32px; color:#FFB6C1; text-shadow: 2px 2px 4px #000;'>Delicious Desserts</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-size: 24px; color:#fff; text-shadow: 2px 2px 4px #000;'>📞 +961 71 184 268</h3>", unsafe_allow_html=True)

elif st.session_state.page == "Order":
    st.markdown("<h1>🎂 Place Your Order</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.session_state.name = st.text_input("👤 Full Name*", value=st.session_state.name)
    st.session_state.phone = st.text_input("📞 Phone Number*", value=st.session_state.phone)
    st.session_state.delivery = st.text_area("🏠 Delivery Address", value=st.session_state.delivery, height=80)
    st.session_state.notes = st.text_area("💬 Special Instructions (optional)", value=st.session_state.notes, height=80)

    st.markdown("---")
    st.markdown("<h2>🎂 Select Your Items</h2>", unsafe_allow_html=True)

    cake_total = 0
    dessert_total = 0
    order_items = []

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3>🍰 Real Cakes</h3>", unsafe_allow_html=True)
        add_real_cake = st.checkbox("Add Real Cake")
        if add_real_cake:
            cake_shape = st.selectbox("Shape", ["Round", "Oval", "Heart"], key="cake_shape")
            cake_flavor = st.selectbox("Flavor", ["Nutella", "Ferrero Rocher", "Vanilla", "Vanilla & Hazelnut", "Lotus"], key="cake_flavor")
            cake_size = st.selectbox("Size", 
                ["3 people - $35", "5 people - $50", "10 people - $80", "15 people - $120", "20 people - $150"],
                key="cake_size")
            cake_price = float(cake_size.split("- $")[1])
            cake_qty = st.number_input("Quantity", min_value=1, value=1, key="cake_qty")
            custom_design = st.checkbox("Add Custom Design (+$15)")
            if custom_design:
                cake_price += 15
                custom_details = st.text_area("Describe your design")
            else:
                custom_details = ""
            
            cake_total = cake_price * cake_qty
            order_items.append({
                "name": "Real Cake",
                "details": f"{cake_shape}, {cake_flavor}, {cake_size.split(' - ')[0]}",
                "qty": cake_qty,
                "unit_price": cake_price,
                "total": cake_total
            })

        st.markdown("<h3>🎨 Fake Cakes</h3>", unsafe_allow_html=True)
        add_fake_cake = st.checkbox("Add Fake Cake")
        if add_fake_cake:
            fake_shape = st.selectbox("Shape", ["Round", "Oval", "Heart", "Square", "Custom"], key="fake_shape")
            fake_color = st.selectbox("Color", 
                ["Blue", "Baby Blue", "Red", "Black", "White", "Pink", "Purple", "Burgundy", "Gold", 
                 "Silver", "Rose Gold", "Mint", "Peach", "Grey", "Navy Blue", "Baby Pink", "Pastel Purple", "Pastel Yellow"],
                key="fake_color")
            fake_layers = st.selectbox("Layers",
                ["1 Layer - $25", "2 Layers - $40", "3 Layers - $60", "4 Layers - $80"],
                key="fake_layers")
            fake_price = float(fake_layers.split("- $")[1])
            fake_qty = st.number_input("Quantity", min_value=1, value=1, key="fake_qty")
            fake_total = fake_price * fake_qty
            order_items.append({
                "name": "Fake Cake",
                "details": f"{fake_shape}, {fake_color}, {fake_layers.split(' - ')[0]}",
                "qty": fake_qty,
                "unit_price": fake_price,
                "total": fake_total
            })

    with col2:
        st.markdown("<h3>🍪 Desserts</h3>", unsafe_allow_html=True)

        desserts_options = {
            "Popsicles": {"Simple": 2.5, "3D Design": 3},
            "Eclairs": {"Simple": 2, "3D Design": 2.5},
            "Cake Cups": {"Nutella": 30, "Ferrero": 30, "Fraisier": 30, "Red Velvet": 36},
            "Cheesecakes": {"Simple": 2.5, "3D Design": 3},
            "Donuts": {"Simple": 2},
            "Cookies": {"Simple": 2.5, "Decorated": 3},
            "Brownies": {"Simple": 2, "3D Flower": 2.5}
        }

        for dessert_type, options in desserts_options.items():
            add_dessert = st.checkbox(f"Add {dessert_type}")
            if add_dessert:
                if len(options) > 1:
                    dessert_variant = st.selectbox(f"{dessert_type} Type", list(options.keys()), key=f"{dessert_type}_type")
                    dessert_price = options[dessert_variant]
                else:
                    dessert_variant = list(options.keys())[0]
                    dessert_price = options[dessert_variant]

                dessert_qty = st.number_input(f"{dessert_type} Qty", min_value=1, value=1, key=f"{dessert_type}_qty")
                dessert_item_total = dessert_price * dessert_qty
                order_items.append({
                    "name": dessert_type,
                    "details": dessert_variant,
                    "qty": dessert_qty,
                    "unit_price": dessert_price,
                    "total": dessert_item_total
                })

    st.markdown("---")
    st.markdown("<h2>📋 Order Summary</h2>", unsafe_allow_html=True)

    total_price = 0
    if order_items:
        st.markdown("<div class='summary-box'>", unsafe_allow_html=True)
        for item in order_items:
            st.markdown(f"<p style='color:#fff; font-size:16px;'>• <b>{item['qty']}x {item['name']}</b> ({item['details']}) - <b>${item['total']:.2f}</b></p>", unsafe_allow_html=True)
            total_price += item['total']
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(f"<div class='total-box'><h3 style='text-align:center; color:#FFB6C1;'>💰 Total: ${total_price:.2f}</h3></div>", unsafe_allow_html=True)

        if st.button("📩 Send Order via WhatsApp"):
            if st.session_state.name.strip() and st.session_state.phone.strip():
                message = f"Hello Berry On Top! 🍓\n\n"
                message += f"👤 Name: {st.session_state.name}\n"
                message += f"📞 Phone: {st.session_state.phone}\n"
                message += f"🏠 Delivery: {st.session_state.delivery}\n\n"
                message += "📋 ORDER DETAILS:\n"
                message += "=" * 40 + "\n"

                for item in order_items:
                    message += f"🍰 {item['qty']}x {item['name']} ({item['details']})\n"
                    message += f"   ${item['unit_price']:.2f} × {item['qty']} = ${item['total']:.2f}\n"

                message += "=" * 40 + "\n"
                message += f"💰 TOTAL: ${total_price:.2f}\n\n"

                if st.session_state.notes:
                    message += f"💬 Special Instructions: {st.session_state.notes}\n"

                whatsapp_link = f"https://wa.me/96171184268?text={urllib.parse.quote(message)}"
                st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:#25D366;color:white;padding:15px 30px;border:none;border-radius:10px;font-size:18px;font-weight:bold;">💬 Send Order via WhatsApp</button></a>', unsafe_allow_html=True)
            else:
                st.error("❌ Please fill in your name and phone number!")
    else:
        st.markdown("<p style='color:#FFB6C1; font-size:18px;'>No items selected yet. Please add items to your order.</p>", unsafe_allow_html=True)

elif st.session_state.page == "Packages":
    st.markdown("<h1>🎉 Party Packages</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FFB6C1;'>Perfect for Your Celebrations!</h3>", unsafe_allow_html=True)
    st.markdown("---")

    packages = {
        "Small Party ($120)": "1 Custom Cake (7 people), 12 Cookies, 12 Brownies, 12 Donuts",
        "Medium Party ($170)": "1 Custom Cake (15 people), 24 Cookies, 12 Brownies, 1 Donuts Tower, 12 Eclairs",
        "Large Party ($350)": "1 Custom Cake (30 people), 24 Cookies, 24 Brownies, 1 Donuts Tower, 1 Eclair Tower, 24 Popsicles"
    }

    for pkg_name, details in packages.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"<h3 style='color:#fff !important;'>{pkg_name}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#fff !important; font-size:16px;'>{details}</p>", unsafe_allow_html=True)
        with col2:
            if st.button(f"Order", key=f"pkg_{pkg_name}"):
                price = pkg_name.split("($")[1].split(")")[0]
                message = f"Hello Berry On Top! 🍓\n\nI want to order: {pkg_name}\n\n{details}\n\nTotal: ${price}"
                whatsapp_link = f"https://wa.me/96171184268?text={urllib.parse.quote(message)}"
                st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:#25D366;color:white;padding:10px 20px;border:none;border-radius:8px;">WhatsApp</button></a>', unsafe_allow_html=True)

elif st.session_state.page == "Gallery":
    st.markdown("<h1>📸 Gallery</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#fff;'>Check out our delicious creations!</p>", unsafe_allow_html=True)
    st.markdown("---")

    gallery_images_page1 = ["https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=400&fit=crop"] * 20
    gallery_images_page2 = ["https://via.placeholder.com/300x300?text=Dessert"] * 20
    gallery_images_page3 = ["https://via.placeholder.com/300x300?text=Dessert"] * 20
    gallery_images_page4 = ["https://via.placeholder.com/300x300?text=Dessert"] * 20

    all_pages = [gallery_images_page1, gallery_images_page2, gallery_images_page3, gallery_images_page4]
    current_images = all_pages[st.session_state.gallery_page - 1]

    st.markdown(f"<h3 style='text-align:center;'>Page {st.session_state.gallery_page} of 4</h3>", unsafe_allow_html=True)

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

elif st.session_state.page == "Contact":
    st.markdown("<h1>📞 Contact Us</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h3 style='color:#FFB6C1;'>Get in Touch!</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>📞 <b>Phone:</b> +961 71 184 268</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>📧 <b>Email:</b> berryontop@gmail.com</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>🏠 <b>Address:</b> South Lebanon</p>", unsafe_allow_html=True)

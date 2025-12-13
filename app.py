import streamlit as st
import urllib.parse

st.set_page_config(page_title="Berry on Top 🍓", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

def go(page):
    st.session_state.page = page
    st.rerun()

st.markdown("""
<style>
.contact {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #ff1744;
    color: white;
    padding: 14px 22px;
    border-radius: 40px;
    font-weight: bold;
    z-index: 999;
}
</style>
<div class="contact">📞 +961 71 184 268</div>
""", unsafe_allow_html=True)

if st.session_state.page == "Home":
    st.markdown("<h1>🍓 Berry on Top</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Homemade desserts for every occasion</h3>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("🎂 Order Now", on_click=lambda: go("Order"))
    with c2:
        st.button("🎁 Packages", on_click=lambda: go("Packages"))
    with c3:
        st.button("📞 Contact", on_click=lambda: go("Contact"))

elif st.session_state.page == "Order":
    st.markdown("<h1>🛒 Place Your Order</h1>", unsafe_allow_html=True)

    order_items = []

    st.subheader("🎂 Cake")
    if st.checkbox("Add Cake"):
        cake_type = st.selectbox("Cake Type", ["Real Cake", "Fake Cake"])
        if cake_type == "Real Cake":
            shape = st.selectbox("Shape", ["Round", "Oval", "Heart"])
            flavor = st.selectbox("Flavor", ["Nutella", "Ferrero", "Vanilla", "Vanilla & Hazelnut", "Lotus"])
            size = st.selectbox("Serves", ["3", "5", "10", "15", "20", "25", "30", "35", "40", "50"])
            order_items.append(f"Real Cake – {shape}, {flavor}, {size} people")
        else:
            layers = st.selectbox("Layers", ["1", "2", "3", "4"])
            color = st.selectbox("Color", ["White", "Pink", "Blue", "Black", "Red"])
            order_items.append(f"Fake Cake – {layers} layers, {color}")

    st.subheader("🍰 Desserts")

    if st.checkbox("Popsicles"):
        pops = st.selectbox("Popsicles Type", ["Simple – $2.5", "3D – $3"])
        order_items.append(f"Popsicles: {pops}")

    if st.checkbox("Eclairs"):
        eclair = st.selectbox("Eclairs Type", ["Simple – $2", "3D – $2.5"])
        order_items.append(f"Eclairs: {eclair}")

    if st.checkbox("Cake Cups (Dozen)"):
        cup = st.selectbox("Cake Cups", ["Nutella – $30", "Ferrero – $30", "Fraisier – $30", "Red Velvet – $36"])
        order_items.append(f"Cake Cups (Dozen): {cup}")

    if st.checkbox("Cheesecakes"):
        cheesecake = st.selectbox("Cheesecakes", ["Simple – $2.5", "3D – $3"])
        order_items.append(f"Cheesecakes: {cheesecake}")

    if st.checkbox("Donuts"):
        donut = st.selectbox("Donuts", ["Simple – $2"])
        order_items.append(f"Donuts: {donut}")

    if st.checkbox("Cookies"):
        cookie = st.selectbox("Cookies", ["Simple – $2.5", "Decorated – $3"])
        order_items.append(f"Cookies: {cookie}")

    if st.checkbox("Brownies"):
        brownie = st.selectbox("Brownies", ["Simple – $2", "3D Flower – $2.5"])
        order_items.append(f"Brownies: {brownie}")

    st.markdown("---")
    st.subheader("📝 Your Information")

    name = st.text_input("Full Name*")
    phone = st.text_input("Phone Number*")
    address = st.text_input("Delivery Address")
    notes = st.text_area("Special Instructions")

    if st.button("Submit Order via WhatsApp"):
        if name.strip() and phone.strip() and order_items:
            message = f"""Hello Berry on Top 🍓

Name: {name}
Phone: {phone}
Address: {address}

Order:
"""
            for item in order_items:
                message += f"- {item}\n"

            if notes:
                message += f"\nNotes: {notes}"

            link = f"https://wa.me/96171184268?text={urllib.parse.quote(message)}"

            st.success("Order ready")
            st.markdown(f"""
            <a href="{link}" target="_blank">
            <button style="background:#25D366;color:white;padding:14px 30px;border:none;border-radius:10px;font-size:16px;">
            💬 Send via WhatsApp
            </button>
            </a>
            """, unsafe_allow_html=True)
        else:
            st.error("Name, phone, and at least one item are required")

    st.button("⬅ Back", on_click=lambda: go("Home"))

elif st.session_state.page == "Packages":
    st.markdown("<h1>🎁 Party Packages</h1>", unsafe_allow_html=True)

    packages = {
        "Small Party – $120": "Cake (7 people), 12 Cookies, 12 Brownies, 12 Donuts",
        "Medium Party – $170": "Cake (15 people), 24 Cookies, 12 Brownies, Donut Tower, 12 Eclairs",
        "Large Party – $350": "Cake (30 people), 24 Cookies, 24 Brownies, Donut Tower, Eclair Tower, 24 Popsicles"
    }

    for title, details in packages.items():
        st.markdown(f"### {title}")
        st.write(details)
        if st.button(f"Order {title}"):
            msg = f"Hello Berry on Top 🍓\n\nI want to order:\n{title}\n{details}"
            link = f"https://wa.me/96171184268?text={urllib.parse.quote(msg)}"
            st.markdown(f"""
            <a href="{link}" target="_blank">
            <button style="background:#25D366;color:white;padding:12px 26px;border:none;border-radius:10px;">
            💬 Send Package Order
            </button>
            </a>
            """, unsafe_allow_html=True)

    st.button("⬅ Back", on_click=lambda: go("Home"))

elif st.session_state.page == "Contact":
    st.markdown("<h1>📞 Contact</h1>", unsafe_allow_html=True)
    st.write("Phone: +961 71 184 268")
    st.write("Location: Lebanon")
    st.button("⬅ Back", on_click=lambda: go("Home"))

    st.markdown(f"<p style='font-size:18px;'>📞 <b>Phone:</b> +961 71 184 268</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>📧 <b>Email:</b> berryontop@gmail.com</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>🏠 <b>Address:</b> South Lebanon</p>", unsafe_allow_html=True)


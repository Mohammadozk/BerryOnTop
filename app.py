if st.session_state.page == "Home":
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-size: 70px; margin:0; letter-spacing:2px;'>Berry on Top</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; font-size: 32px; color:#FFB6C1; margin:10px 0; font-weight:bold;'>Delicious Desserts</h3>", unsafe_allow_html=True)
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    <style>
    .stButton>button {
        min-width: 150px;
        max-width: 220px;
        height: 60px;
        font-size: 18px;
        background-color: #c8102e;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
        margin: 5px;
        white-space: nowrap;
    }
    .stButton>button:hover {
        background-color: #ff3c4e;
    }
    .button-container {
        display: flex;
        overflow-x: auto;
        gap: 10px;
        padding: 0 10px;
    }
    .button-container::-webkit-scrollbar {
        display: none;
    }
    @media only screen and (max-width: 600px) {
        .stButton>button {
            font-size: 16px;
            height: 50px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="button-container">', unsafe_allow_html=True)

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

    st.markdown('</div>', unsafe_allow_html=True)






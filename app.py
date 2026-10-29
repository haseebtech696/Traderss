import streamlit as st
import os
import base64

# Configure Page
st.set_page_config(
    page_title="Malik Traders | Crop Protection",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Streamlit
st.markdown("""
<style>
    .main-title {
        font-size: 2.3rem;
        font-weight: 700;
        color: #1b5e20;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4b5563;
        margin-bottom: 1.5rem;
    }
    .badge-insecticide {
        background-color: #e8f5e9;
        color: #1b5e20;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
    }
    .badge-herbicide {
        background-color: #fef3c7;
        color: #b45309;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
    }
    .badge-fungicide {
        background-color: #e0f2fe;
        color: #0369a1;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
    }
    .stButton>button {
        background-color: #25d366 !important;
        color: white !important;
        font-weight: 600;
        border-radius: 8px;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to load images safely
def get_image_path(filename):
    path = os.path.join(os.path.dirname(__file__), "images", filename)
    if os.path.exists(path):
        return path
    return None

# Sidebar Navigation
st.sidebar.image("images/founder.jpg" if os.path.exists("images/founder.jpg") else None, width=120)
st.sidebar.title("Malik Traders")
st.sidebar.caption("Sui Wala, Adda Nawa Wasti, District Lodhran")
st.sidebar.markdown("**Phone / WhatsApp:** [0300-8682363](tel:+923008682363)")

page = st.sidebar.radio("Navigation", ["Home", "Products Catalog", "Meet the Founder", "Contact Us"])

# Safety Banner
st.sidebar.info("⚠️ **Safety Notice:** Use pesticides strictly as per label instructions and safety guidelines.")

# ----------------- HOME PAGE -----------------
if page == "Home":
    st.markdown('<div class="main-title">Protect Your Crops, Grow Your Harvest</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Reliable, field-tested crop protection chemistry tailored for healthy fields and high yields.</div>', unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        st.link_button("Chat on WhatsApp", "https://wa.me/923008682363?text=Hello%20Malik%20Traders,%20I%20would%20like%20to%20inquire%20about%20pesticides.")
    
    st.divider()

    # 3 Highlights
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🛡️ Quality Formulations")
        st.write("100% authentic, certified insecticides, herbicides, and fungicides tested for maximum biological efficacy.")
    with col2:
        st.subheader("🤝 Trusted Supplier")
        st.write("Serving growers and retailers with transparent pricing and prompt stock availability in Lodhran and beyond.")
    with col3:
        st.subheader("🌾 Farmer Advisory")
        st.write("Straightforward recommendations on dosage, spray timing, and safety for every crop season.")

    st.divider()
    st.subheader("Featured Solutions")
    feat_cols = st.columns(3)
    with feat_cols[0]:
        st.image("images/product-1.jpg", caption="CropGuard Pro (Insecticide)")
    with feat_cols[1]:
        st.image("images/product-2.jpg", caption="WeedShield Ultra (Herbicide)")
    with feat_cols[2]:
        st.image("images/product-3.jpg", caption="FungiStop Max (Fungicide)")

# ----------------- PRODUCTS PAGE -----------------
elif page == "Products Catalog":
    st.markdown('<div class="main-title">Our Crop Protection Products</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Browse certified products. Click any button to place an instant WhatsApp order.</div>', unsafe_allow_html=True)

    products = [
        {"id": 1, "name": "CropGuard Pro", "cat": "Insecticides", "img": "product-1.jpg", "desc": "Fast-acting systemic insecticide designed for stem borers, aphids, and bollworms in cotton and paddy."},
        {"id": 2, "name": "WeedShield Ultra", "cat": "Herbicides", "img": "product-2.jpg", "desc": "Broad-spectrum selective post-emergence herbicide targeting broadleaf weeds and wild grasses in wheat."},
        {"id": 3, "name": "FungiStop Max", "cat": "Fungicides", "img": "product-3.jpg", "desc": "Protective and curative systemic fungicide preventing yellow rust, powdery mildew, and blight."},
        {"id": 4, "name": "AgroSect 50 EC", "cat": "Insecticides", "img": "product-4.jpg", "desc": "High-efficacy contact insecticide offering rapid knock-down action against severe sucking pests."},
        {"id": 5, "name": "GrassClear Super", "cat": "Herbicides", "img": "product-5.jpg", "desc": "Early post-emergence selective herbicide providing spotless seasonal grass weed control for maize."},
        {"id": 6, "name": "BlightCure 75 WP", "cat": "Fungicides", "img": "product-6.jpg", "desc": "Copper-rich barrier contact fungicide providing long-lasting preventive protection against early/late blight."},
        {"id": 7, "name": "TermiNull Concentrate", "cat": "Insecticides", "img": "product-7.jpg", "desc": "Specialized soil and root trenching insecticide delivering comprehensive subterranean termite eradication."},
        {"id": 8, "name": "CleanField Total", "cat": "Herbicides", "img": "product-8.jpg", "desc": "Non-selective systemic herbicide engineered for pre-planting weed management and orchard floor clearing."},
    ]

    filter_val = st.radio("Filter by Category", ["All", "Insecticides", "Herbicides", "Fungicides"], horizontal=True)

    filtered = [p for p in products if filter_val == "All" or p["cat"] == filter_val]
    st.write(f"Showing {len(filtered)} of {len(products)} products")

    cols = st.columns(3)
    for idx, p in enumerate(filtered):
        with cols[idx % 3]:
            st.image(f"images/{p['img']}")
            st.markdown(f"**{p['name']}**")
            st.caption(f"Category: {p['cat']}")
            st.write(p["desc"])
            wa_url = f"https://wa.me/923008682363?text=Hello%20Malik%20Traders,%20I%20would%20like%20to%20order%20{p['name']}."
            st.link_button(f"Order {p['name']} on WhatsApp", wa_url)
            st.markdown("---")

# ----------------- ABOUT PAGE -----------------
elif page == "Meet the Founder":
    st.markdown('<div class="main-title">Meet the Founder</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Malik Muhammad Aslam — Founder & Managing Director</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("images/founder.jpg", caption="Malik Muhammad Aslam (25+ Years Experience)")
    with col2:
        st.write("""
        Founded on the belief that a farmer’s hard work deserves uncompromised crop protection, 
        **Malik Muhammad Aslam** established **Malik Traders** after spending over two decades 
        walking farm fields and working closely with local agricultural communities.

        Witnessing firsthand how counterfeit chemicals and inaccurate dosing ruined entire seasonal yields, 
        he dedicated his career to sourcing strictly authentic, lab-tested insecticides, herbicides, 
        and fungicides from verified national and multinational manufacturers.
        """)
        st.info("“When a farmer buys crop protection from us, he is trusting us with his livelihood and family’s harvest. Our duty is to honor that trust every single day.”")
        st.write("**Mission:** To empower growers with genuine agricultural chemistry, transparent pricing, and practical advisory.")

# ----------------- CONTACT PAGE -----------------
elif page == "Contact Us":
    st.markdown('<div class="main-title">Contact & Order Inquiries</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Business Information")
        st.write("📍 **Address:** Sui Wala, Adda Nawa Wasti, District Lodhran, Punjab, Pakistan")
        st.write("📞 **Phone:** [0300-8682363](tel:+923008682363)")
        st.write("💬 **WhatsApp:** [0300-8682363](https://wa.me/923008682363)")
        st.write("✉️ **Email:** info@maliktraders.pk")
        st.write("⏰ **Hours:** Monday – Saturday: 8:00 AM – 7:00 PM")

    with col2:
        st.subheader("Send an Inquiry")
        with st.form("inquiry_form"):
            name = st.text_input("Full Name")
            phone = st.text_input("Phone Number")
            msg = st.text_area("Your Message / Product Inquired")
            submitted = st.form_submit_button("Submit Inquiry")
            if submitted:
                if name and phone and msg:
                    st.success("Thank you! Your inquiry has been received. Our team will contact you shortly.")
                else:
                    st.error("Please fill in all fields before submitting.")

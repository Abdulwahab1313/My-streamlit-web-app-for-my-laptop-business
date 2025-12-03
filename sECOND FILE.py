import streamlit as st
st.title("Welcome to Aws Gadget")
tab1,tab2,tab3,tabs4= st.tabs(["Hp","Dell","Lenovo","Samsung"])
link = st.markdown("[clikck link to chat me up](http://127.0.0.1:8501)")
with tab1:
    img = st.image("Hp10.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N400000")
    st.markdown("[clikck link to chat me up](http://127.0.0.1:8501)")
    with st.expander("click for more photos and details"):
        lists=["Hp11.jpg","Hp12.jpg"]
        sl1 = st.slider("increase image1 size", 100, 300)
        st.image(lists, width=sl1)
        st.write(sl1)

    img1 = st.image("Hp21.jpg", width=200,caption="hp Elitebook g420 touchscreen.keyboardlight,512ssd,8gbram,N330000")
    st.markdown("[clikck link to chat me up](http://127.0.0.1:8501)")
    with st.expander("click for more photos"):
        lists = ["Hp22.jpg", "Hp23.jpg"]
        sl2= st.slider("increase image2 size",100,300)
        st.image(lists, width=sl2)
        st.write(sl2)


with tab2:
    img2 = st.image("Dell1.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.markdown("[clikck link to chat me up](http://127.0.0.1:8501)")
    with st.expander("click for more photos and details"):
        lists=["Dell2.jpg","Dell3.jpg"]
        sl3 = st.slider("increase image3 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)


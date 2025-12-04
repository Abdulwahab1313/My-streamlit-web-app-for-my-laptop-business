import streamlit as st
st.title("Welcome to Aws Gadget")
tab1,tab2,tab3,tabs4,tab5,tab6= st.tabs(["Hp","Dell","Lenovo","Samsung","acer","Random mini pc" ])
link = st.markdown("[clikck link to chat me up](https:wa.me/+234 806 679 9167)")
with tab1:
    img = st.image("IMG-20251203-WA0009.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N400000")
    st.write(link)
    with st.expander("click for more photos and details"):
        lists=["Hp11.jpg","Hp12.jpg", "Hp13.jpg"]
        sl1 = st.slider("increase image1 size", 100, 300)
        st.image(lists, width=sl1)
        st.write(sl1)

    img1 = st.image("Hp14.jpg", width=200,caption="hp Elitebook g420 touchscreen.keyboardlight,512ssd,8gbram,N330000")
    st.write(link)
    with st.expander("click for more photos"):
        lists = ["Hp15.jpg", "Hp16.jpg","Hp17.jpg","Hp18.jpg"]
        sl2= st.slider("increase image2 size",100,300)
        st.image(lists, width=sl2)
        st.write(sl2)


with tab5:
    img2 = st.image("acer11.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.markdown("[clikck link to chat me up](wa.me/+234 806 679 9167)")
    with st.expander("click for more photos and details"):
        lists=["acer12.jpg","acer13.jpg","acer14"]
        sl3 = st.slider("increase image3 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)

with tab3:
    img2 = st.image("acer11.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.write(link)
    with st.expander("click for more photos and details"):
        lists=["acer12.jpg","acer13.jpg","acer14"]
        sl3 = st.slider("increase image3 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)

with tab5:
    img2 = st.image("acer11.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.write(link)
    with st.expander("click for more photos and details"):
        lists=["acer12.jpg","acer13.jpg","acer14"]
        sl3 = st.slider("increase image3 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)

with tab5:
    img2 = st.image("acer11.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.write(link)
    with st.expander("click for more photos and details"):
        lists=["acer12.jpg","acer13.jpg","acer14"]
        sl3 = st.slider("increase image3 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)

with tab5:
    img2 = st.image("acer11.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.write(link)
    with st.expander("click for more photos and details"):
        lists=["acer12.jpg","acer13.jpg","acer14"]
        sl3 = st.slider("increase image3 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)









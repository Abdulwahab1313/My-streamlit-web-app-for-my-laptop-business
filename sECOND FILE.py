import streamlit as st
st.title("Welcome to Aws Gadget")
tab1,tab2,tab3,tabs4,tab5,tab6= st.tabs(["Hp","Dell","Lenovo","Samsung","acer","Random mini pc" ])
link ="[clikck link to chat me up](https://wa.me/2348066799167)"
with tab1:
    img = st.image("https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Hp10.jpg",width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N400000")
    st.markdown(link)
    with st.expander("click for more photos and details"):
        lists=["https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Hp11.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Hp12.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Hp13.jpg"]
        sl1 = st.slider("increase image1 size", 100, 300)
        st.image(lists, width=sl1)
        st.write(sl1)

    img1 = st.image("https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Hp15.jpg", width=200,caption="hp Elitebook g420 touchscreen.keyboardlight,512ssd,8gbram,N330000")
    st.markdown(link)
    with st.expander("click for more photos"):
        lists = ["https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Hp16.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Hp17.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Hp18.jpg"]
        sl2= st.slider("increase image2 size",100,300)
        st.image(lists, width=sl2)
        st.write(sl2)


with tab5:
    img2 = st.image("https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/acer11.jpg", width=200,caption="acer,500GBhdd,8gbram,N130000")
    st.markdown(link)
    with st.expander("click for more photos and details"):
        lists=["https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/acer12.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/acer13.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/acer14.jpg"]
        sl3 = st.slider("increase image3 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)

with tab3:
    img2 = st.image("https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Dell11.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N180000")
    st.markdown(link)
    with st.expander("click for more photos and details"):
        lists=["https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Dell12.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Dell13.jpg"]
        sl3 = st.slider("increase image4 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)

with tab5:
    img2 = st.image("acer11.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.markdown(link)
    with st.expander("click for more photos and details"):
        lists=["acer12.jpg","acer13.jpg","acer14.jpg"]
        sl3 = st.slider("increase image5 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)

with tab5:
    img2 = st.image("acer11.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.markdown(link)
    with st.expander("click for more photos and details"):
        lists=["acer12.jpg","acer13.jpg","acer14.jpg"]
        sl3 = st.slider("increase image6 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)

with tab6:
    img2 = st.image("https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Random mini lenovo pc 5.jpg", width=200,caption="hp probook touchscreen.keyboardlight,512ssd,8gbram,N40000")
    st.markdown(link)
    with st.expander("click for more photos and details"):
        lists=["https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Random mini lenovo pc1.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Random mini lenovo pc 2.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Random mini lenovo pc 3.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Random mini lenovo pc 4.jpg","https://github.com/Abdulwahab1313/My-streamlit-web-app-for-my-laptop-business/raw/main/Random mini lenovo pc 5.jpg"]
        sl3 = st.slider("increase image7 size", 100, 300)
        st.image(lists, width=sl3)
        st.write(sl3)














import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

url = 'https://lottie.host/4eb1dc2f-a8a5-4a1b-87cd-8883507dea4b/w2xhxe5IxN.json'

# Función para cargar una animación Lottie desde una URL
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
      return None
  return r.json()

lottie = load_lottieurl(url)

def local_css(file_name):
  with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title = 'Mateo App',page_icon = '📈', layout= 'wide')





local_css("style/style.css")

email_address ="emailcontact@gmail.com"

#intro
with st.container():
  st.header('Hola a todos 👋, somos MateoApp')
  st.title('Creamos soluciones para acelerar tu negocio')
  st.write('Somos unos apasionados de la tecnología y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos.')
  st.write('[Cuenta personal](https://www.instagram.com/matteo.angulo/)')

#contenedor con dos partes, texto | animación
with st.container():
  st.write('---') #ver si no tiene problemas con comillas simples
  text_column, animation_column = st.columns(2)
  with text_column:
    st.header("Sobre nosotros")
    st.write(
        """
        Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
        Seguramente te vamos a poder ayudar si:

        - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
        - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
        - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
        - Quieres mejorar la experiencia de tus clientes
        - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

        
        ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
        """
    ) #lo que está entre *** *** es para ponerle negrita
    st.write('[Cuenta personal](https://www.instagram.com/matteo.angulo/)')

  with animation_column:
    st_lottie(lottie, height=400)

  # container de los servicios
  with st.container():
    st.write('---')
    st.header('servicios ✅')
    st.write('##')#espacio
    imagen_column, text_column = st.columns((1,5))
    with imagen_column:
      image = Image.open('imagenes/perfil.jpg')
      st.image(image, use_column_width=True)
    with text_column:
      st.subheader("Diseño de aplicaciones")
      st.write(
          """
          Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.    
          """
      )
      st.write('[Cuenta personal](https://www.instagram.com/matteo.angulo/)')

  # contacto
  with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros!")
    # st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="name" placeholder="Tu nombre" required>
      <input type="email" name="email" placeholder="Tu email" required>
      <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
      <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
      st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
      st.empty()


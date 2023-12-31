#!/bin/python

import pandas as pd
import os

csvfile = pd.read_csv('./films/raws/FOF_Film_Data.csv', sep='\t', delimiter=None, on_bad_lines='skip')
csvfile.fillna('', inplace=True)
row_limit, col_limit = csvfile.shape
cwd = os.getcwd()

year_pivot = csvfile.pivot_table(index = ['FOF'], aggfunc ='size') # 5-6

for i in range(1,row_limit):

  fof_year = str(int(csvfile["FOF"].values[i]))
  directory_path = cwd + '/' + fof_year
  print(directory_path)
  if not os.path.exists(directory_path):
    os.makedirs(directory_path)

  file_name = str(csvfile["MOVIE_NAME"].values[i]).lower().replace(' ', '-')
  img_dir = cwd + '/' + fof_year + '/images/' + file_name
  if not os.path.exists(img_dir):
    os.makedirs(img_dir)
  print(file_name)
  # html_file = open(str(cwd + '/' + fof_year + '/' + file_name + '.html'), 'w+')

  file_contents = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://www.w3schools.com/lib/w3.js"></script>
    <link rel="stylesheet" href="./assets/CSS/style.css" />
    <link rel="icon" type="image/x-icon" href="../assets/Image/favicon.png" />
    <title>Frames of Freedom - ''' + fof_year + '''</title>
  </head>
  <body>
    <nav class="navbar">
      <div class="navbar-container container">
        <input type="checkbox" name="" id="" />
        <div class="hamburger-lines">
          <span class="line line1"></span>
          <span class="line line2"></span>
          <span class="line line3"></span>
        </div>
        <ul class="menu-items">
          <li><a href="./index.html" style="color: red">HOME</a></li>
          <li><a href="">FILMS</a></li>
          <li><a href="./blog.html">BLOGS</a></li>
          <li><a href="./gallery.html">GALLERY</a></li>
          <li><a href="./schedule.html">SCHEDULE</a></li>
        </ul>
        <h1 class="logo">
          <img src="../assets/Image/pfc-logo-wp.png" alt="" />
        </h1>
      </div>
    </nav>
    <br /><br /><br /><br />
    <main>
      <section class="container-img-slider">
        <div class="slider-wrapper">
          <div class="slider">
            <img
              class="nature"
              id="slide-1"
              src="./assets/images/bg_1.webp"
              alt=""
              height="560"
              width="320"
            />
            <img
              class="nature"
              id="slide-2"
              src="./assets/images/bg_2.webp"
              alt=""
              height="560"
              width="320"
            />
            <img
              class="nature"
              id="slide-3"
              src="./assets/images/bg_3.webp"
              alt=""
              height="560"
              width="320"
            />
            <img
              class="nature"
              id="slide-4"
              src="./assets/images/bg_4.webp"
              alt=""
              height="560"
              width="320"
            />
            <img
              class="nature"
              id="slide-5"
              src="./assets/images/bg_5.webp"
              alt=""
              height="560"
              width="320"
            />
          </div>
          <div class="slider-nav">
            <a href="#slide-1"></a>
            <a href="#slide-2"></a>
            <a href="#slide-3"></a>
            <a href="#slide-4"></a>
            <a href="#slide-5"></a>
          </div>
        </div>
      </section>
      <div class="year-about">
        <p style="font-size: xx-large; text-align: center">
          FRAMES OF FREEDOM ''' + fof_year + '''
        </p>
        <br />
        <div class="fof-sub-texts">
          <p>
            In the 5th edition of FRAMES OF FREEDOM Film Festival, we will screen five unforgettable fiction films selected from the last 10 years of KPFF. It promises to be a looking back at socially-committed Indian fiction cinema from the past decade, taking us  on an audiovisual journey through our republic.
          </p>
          <br />
          <p class="text-spacing">
            Alongside the films, we would be hosting Arunabh Saikia, journalist, who has been consistently field-reporting from Manipur and the North East, to speak on what exactly is happening in Manipur.  His talk, titled "Manipur: Notes from ground zero" will be followed by a moderated conversation with the audience.
          </p>
          <br />
          <p>            
            The Kolkata People’s Film Festival (KPFF), organised by the People's Film Collective (PFC), is a people-supported, independent, volunteer-led cinema festival, showcasing politically committed contemporary documentary and fiction cinema from India and Southasia. It brings together a wide cross-section of audience and filmmakers to interact and form friendships and active camaraderie over films and conversations.
          </p>
        </div>
      </div>
      <div>
        <div class="year">
          <a href="" style="text-decoration: none"
            ><p style="color: red" class="year-font"> 
              2023 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span class="pipe">|</span>
            </p></a
          >
          <a href="./2022.html" style="text-decoration: none; color: black"
            ><p style="color: black" class="year-font">
              2022 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span class="pipe">|</span>
            </p></a
          >
          <a href="./2019.html" style="text-decoration: none; color: black"
            ><p style="color: black" class="year-font">
              2019 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span class="pipe">|</span>
            </p></a
          >
          <a href="./2018.html" style="text-decoration: none; color: black"
            ><p style="color: black" class="year-font">
              2018 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <span class="pipe">|</span>
            </p></a
          >
          <a href="./2017.html" style="text-decoration: none; color: black"
            ><p style="color: black" class="year-font">
              2017
            </p></a
          >
        </div>
      </div>
      <div class="fof-films">
        <div class="flex-row">
          <div>
            <a href="./films/2023/aise-hee-(just-like-that).html">
              <div class="mobile-thumbnail-web-hidden">
                <img
                  src="./films/2023/images/aise-hee-(just-like-that)/still_1.webp"
                  alt=""
                  width="700px"
                  height="500px"
                />
              </div>
              <div class="mobile-thumbnail">
                <img
                  src="./films/2023/images/aise-hee-(just-like-that)/still_1.webp"
                  alt=""
                  width="350px"
                  height="350px"
                  style="border-radius: 3%"
                />
                <div class="mobile-thumbnail-text">
                  <p style="font-size: 10px; margin-bottom: 5%">
                    KISLAY
                  </p>
                  <p style="font-size: 24px; font-weight: 600">AISE HEE</p>
                  <p style="font-size: 24px; font-weight: 600">Just Like That</p>
                </div>
              </div>
            </a>
          </div>

          <div>
            <a href="./films/2023/court.html">
              <div class="mobile-thumbnail-web-hidden">
                <img
                  src="./films/2023/images/court/poster.webp"
                  alt=""
                  width="480px"
                  height="500px"
                />
              </div>
              <div class="mobile-thumbnail">
                <img
                  src="./films/2023/images/court/poster.webp"
                  alt=""
                  width="350px"
                  height="350px"
                  style="border-radius: 3%"
                />
                <div class="mobile-thumbnail-text">
                  <p style="font-size: 10px; margin-bottom: 5%">
                    CHAITANYA TAMHANE
                  </p>
                  <p style="font-size: 24px; font-weight: 600">COURT</p>
                  <p style="font-size: 24px; font-weight: 600"></p>
                </div>
              </div>
            </a>
          </div>
        </div>

        <div class="flex-row">
          <div>
            <a href="./films/2023/fandry-(pig).html">
              <div class="mobile-thumbnail-web-hidden">
                <img
                  src="./films/2023/images/fandry-(pig)/still_1.webp"
                  alt=""
                  width="700px"
                  height="300px"
                />
              </div>
            </a>
            <div class="mobile-thumbnail">
              <img
                src="./films/2023/images/fandry-(pig)/still_1.webp"
                alt=""
                width="350px"
                height="350px"
                style="border-radius: 3%"
              />
              <div class="mobile-thumbnail-text">
                <p style="font-size: 10px; margin-bottom: 5%">NAGRAJ MANJULE</p>
                <p style="font-size: 24px; font-weight: 600">FANDRY</p>
                <p style="font-size: 24px; font-weight: 600">Pig</p>
              </div>
            </div>
          </div>
          <div>
            <a href="./films/2023/ghode-ko-jalebi-khilane-le-ja-riya-hoon-(taking-the-horse-to-eat-jalebis).html">
              <div class="mobile-thumbnail-web-hidden">
                <img
                  src="./films/2023/images/ghode-ko-jalebi-khilane-le-ja-riya-hoon-(taking-the-horse-to-eat-jalebis)/still_1.webp"
                  alt=""
                  width="480px"
                  height="300px"
                />
              </div>
              <div class="mobile-thumbnail">
                <img
                  src="./films/2023/images/ghode-ko-jalebi-khilane-le-ja-riya-hoon-(taking-the-horse-to-eat-jalebis)/still_1.webp"
                  alt=""
                  width="350px"
                  height="350px"
                  style="border-radius: 3%"
                />
                <div class="mobile-thumbnail-text">
                  <p style="font-size: 10px; margin-bottom: 5%">
                    ANAMIKA HAKSAR
                  </p>
                  <p style="font-size: 24px; font-weight: 600">GHODE KO JALEBI KHILANE LE JA RIYA HOON
</p>
                  <p style="font-size: 24px; font-weight: 600">Taking the Horse to Eat Jalebis</p>
                </div>
              </div>
            </a>
          </div>
        </div>

        <!-- <div class="flex-row">
          <div>
            <a href="">
              <div class="mobile-thumbnail-web-hidden">
              <img
                src="./assets/images/stock1.jpg"
                alt=""
                width="500px"
                height="500px"
              />
            </div>
            <div class="mobile-thumbnail">
              <img
                src="./assets/images/stock1.jpg"
                alt=""
                width="350px"
                height="350px"
                class="mobile-thumbnail"
              />
            </div>
            </a>
          </div>
          <div>
            <a href="">
              <div class="mobile-thumbnail-web-hidden">
              <img
                src="./assets/images/stock1.jpg"
                alt=""
                width="680px"
                height="500px"
              />
            </div>
            <div class="mobile-thumbnail">
              <img
                src="./assets/images/stock1.jpg"
                alt=""
                width="350px"
                height="350px"
                class="mobile-thumbnail"
              />
            </div>
            </a>
          </div>
        </div> -->

        <div class="last-img">
          <a href="./films/2023/jhini-bini-chadariya-(the-brittle-thread).html">
            <div class="mobile-thumbnail-web-hidden">
              <img
                src="./films/2023/images/jhini-bini-chadariya-(the-brittle-thread)/still_1.webp"
                alt=""
                width="1200px"
                height="400px"
              />
            </div>
            <div class="mobile-thumbnail">
              <img
                src="./films/2023/images/jhini-bini-chadariya-(the-brittle-thread)/still_1.webp"
                alt=""
                width="350px"
                height="350px"
                style="border-radius: 3%"
              />
              <div class="mobile-thumbnail-text">
                <p style="font-size: 10px; margin-bottom: 5%">DIRECTOR NAME</p>
                <p style="font-size: 24px; font-weight: 600">THE ROARRING</p>
                <p style="font-size: 24px; font-weight: 600">WAVES</p>
              </div>
            </div>
          </a>
        </div>
      </div>
    </main>
    <div class="main-location">
      <div>
        <div>
          <p style="font-size: 40px">GET IN TOUCH</p>
          <div style="line-height: 2" >
            <label for="">NAME</label> <br />
            <input type="text" class="input-class" />
            <br />
            <label for="">EMAIL</label> <br />
            <input type="email" class="input-class" />
            <br />
            <label for="">SUBJECT</label> <br />
            <input type="text" class="input-class" />
            <br />
            <label for="">MESSAGE</label> <br />
            <textarea class="form-input-message"> </textarea>
            <br />
            <br />
            <input type="submit" class="submit-button" />
          </div>
        </div>
      </div>
      <div>
        <p class="festival-location-text">FESTIVAL LOCATION</p>
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14742.064866442734!2d88.3487472!3d22.5223274!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a027731576b6be7%3A0x96a67c9579d27e65!2sMahanayak%20Uttam%20Manch!5e0!3m2!1sen!2sin!4v1691133754500!5m2!1sen!2sin"
          width="500"
          height="425"
          class="map"
          style="border: 0"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
        ></iframe>
      </div>
    </div>
    <footer>
      <div style="line-height: 1.6">
        <div class="footer-subtext footer-one">
          <div>
            <p class="sub-header">CONTACT US</p>
            <p class="sub-header-text">EMAIL - <a href='mailto:peoplesfilmcollective@gmail.com'>peoplesfilmcollective@gmail.com</a></p>
            <p class="sub-header-text">PHONE - <a href='tel:+919163736863'>+91 91637 36863</a></p>
          </div>
        </div>
      </div>

      <div class="footer-subtext footer-two">
        <div style="line-height: 1.6">
          <p>CONTACT WITH US</p>
          <div>icons</div>
        </div>
        <div style="line-height: 1.6">
          <div>
            <a href="./2023.html" style="text-decoration: none; color: white"
              >HOME &nbsp;|&nbsp;
            </a>
            <a href="" style="text-decoration: none; color: white"
              >FILMS &nbsp;|&nbsp;
            </a>
            <a
              href="./in-the-news.html"
              style="text-decoration: none; color: white"
              >BLOGS
            </a>
          </div>
          <div>
            <a href="./gallery.html" style="text-decoration: none; color: white"
              >GALLERY &nbsp;|&nbsp;
            </a>
            <a href="" style="text-decoration: none; color: white"
              >SCHEDULE &nbsp;|&nbsp;
            </a>
            <a
              href="../location.html"
              style="text-decoration: none; color: white"
              >LOCATION</a
            >
          </div>
        </div>
      </div>
    </footer>
    <p class="copyright">© Copyright - People's Film Collective</p>
    <script>
      w3.slideshow(".nature", 3000);
    </script>
    <script src="./assets/JS/script.js"></script>
  </body>
</html>
  
  '''

  html_file.write(file_contents)
  html_file.close()

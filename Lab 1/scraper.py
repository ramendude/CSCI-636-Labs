# Lab Report 1
# Rex Ocampo
# to do - include name of prof in bios and courses to identify who is who
import requests
from bs4 import BeautifulSoup
# data
bio_url = []
course_taught = []
bios = []
dumb = "https://www.cms.caltech.edu"
url = "https://www.cms.caltech.edu/cms-people/faculty"
# make a request here
r = requests.get(url)
doc = BeautifulSoup(r.text,'html.parser')

# put request here for soup time
if r.status_code == 200:
    # write to txt
    def w2t(list, filename):
        with open(filename, mode ='w') as file:
            for item in list:
                file.write(str(item) + '\n')


    def getCourses(soup, list):
        course_tag = soup.find('div',class_ = "courses-block")
        if course_tag is not None:
            for tag in course_tag:
                string = tag.text.strip()
                if(string != 'Related Courses' and string != '2021-22' and string != ''):
                    list.append(string)
                elif(string == '2021-22'):
                    break
        else:
            list.append('No courses found!')


    def getBio(soup,list):
        bio_tag = soup.find('div', class_ = 'rich-text')
        if bio_tag is not None:
            list.append(bio_tag.text)
        else:
            return list.append('No biography found!')


    # getting the faculty links
    links = doc.find_all('a', class_="person-teaser__link")
    for i, link in enumerate(links):
        href = link.get('href')
        bio_url.append(href)

    # to make the actual link
    bio_url = [dumb + url for url in bio_url]

    # requesting the links
    for i, links in enumerate(bio_url):
        response = requests.get(bio_url[i])
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            getCourses(soup,course_taught)
            getBio(soup,bios)
        else:
            print('Failed to fetch {link}')

    # writing text
    w2t(bio_url,'bio_url.txt')
    w2t(course_taught,'course.txt')
    w2t(bios,'bios.txt')
    print('Finished')

else:
    print('Failed to fetch {url}')
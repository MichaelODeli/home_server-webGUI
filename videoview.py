#!/bin/python3
#!C:/Users/MichaelODeli/AppData/Local/Programs/Python/Python38/python.exe

from templates import html_templates
import cgi, cgitb
import traceback
import configparser
import sys
if sys.platform == "linux" or sys.platform == "linux2":
    lm=("/home/michael/server-side/storage/")
elif sys.platform == "win32":
    lm=("C:/Users/MichaelODeli/OneDrive/DEVELOP/work/home-server/server-side/storage/")
from storage import fileSearch as fs
def id_check(id):
    return True
try:
    cgitb.enable()
    form = cgi.FieldStorage()
    if form.getvalue('videoid', 'none'):
        if id_check(form.getvalue('videoid'))==True:
            videoid = form.getvalue('videoid', 'none')
            vidinfo=fs.searchById(videoid, fman=True)
        else: pass
    print("Content-type: text/html")
    print('')
    print(html_templates.title_header('Home server - Videoview', header_active='video', dark=True, from_video=True))
    # print(vidinfo)
    if vidinfo==[['Not found']]:
        print('<center><div style="color: #343a40; margin: 10px;"><p>Not found</p></div></center>')
    elif vidinfo==None:
        print('<center><div style="color: #343a40; margin: 10px;"><p>Not found</p></div></center>')
    else:
        cfg = configparser.ConfigParser()
        with open(lm+'settings.ini', 'r', encoding='utf-8') as fp:
            cfg.read_file(fp)
        urlf=cfg.get('links', 'webdir')+cfg.get('settings', 'storageFolder')+'/'+vidinfo[0][0]+'/'+vidinfo[0][2]+'/'+vidinfo[0][3]
        print('''
<body style="height: 100%;width: 100%;">
    <style type="text/css">   @import url("../assets/css/ml-video-1.css"); </style>
    <style type="text/css">   @import url("../assets/css/ml-video.css"); </style>
    <style type="text/css">   @import url("../assets/css/Video-Responsive.css"); </style>
    <div class="col" style="padding-top: 10px;padding-right: 10%;padding-bottom: 10px;padding-left: 10%;">
        <div>
            <div class="vplayer" data-v="{video_url}">
                <div class="plybtn"></div>
            </div>
        </div>
        <h4>{video_name}</h4>
        <h6>{channel}</h6>
    </div>
    <div class="container">
        <div class="row d-lg-flex">
            <div class="col-md-6">
                <h4 style="text-align: center;">Related videos</h4>
                <div class="card"><img class="card-img w-100 d-block" src="../assets/img/27_5516_L.jpg" style="height: 120px;">
                    <div class="card-img-overlay">
                        <h4 style="color: var(--bs-gray-200);">Relaed video name</h4>
                        <p style="color: var(--bs-gray-100);">Related video channel</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <h4 style="text-align: center;">Recommended videos</h4>
                <div class="card"><img class="card-img w-100 d-block" src="../assets/img/27_5516_L.jpg" style="height: 120px;">
                    <div class="card-img-overlay">
                        <h4 style="color: var(--bs-gray-200);">Recommended video name</h4>
                        <p style="color: var(--bs-gray-100);">Related video channel</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="../assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="../assets/js/ml-video.js"></script>
</body>

</html>
    '''.format(video_url=urlf, channel=vidinfo[0][2].replace('-', ' '), video_name=vidinfo[0][3].replace('-', ' ').replace('.mp4', '')))
except Exception as e:
    print("Content-type: text/html")
    print('')
    print(traceback.format_exc())
import os
os.system('')
print("""\033[0;31m
  ██████  ▄████▄    ▄████     ██▓███   ▄▄▄        ▄████ ▓█████      ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██    ▒ ▒██▀ ▀█   ██▒ ▀█▒   ▓██░  ██▒▒████▄     ██▒ ▀█▒▓█   ▀     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▒██░▄▄▄░   ▓██░ ██▓▒▒██  ▀█▄  ▒██░▄▄▄░▒███      ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒░▓█  ██▓   ▒██▄█▓▒ ▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒██████▒▒▒ ▓███▀ ░░▒▓███▀▒   ▒██▒ ░  ░ ▓█   ▓██▒░▒▓███▀▒░▒████▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ░▒   ▒    ▒▓▒░ ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ░   ░    ░▒ ░       ▒   ▒▒ ░  ░   ░  ░ ░  ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░  ░  ░  ░        ░ ░   ░    ░░         ░   ▒   ░ ░   ░    ░      ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
      ░  ░ ░            ░                   ░  ░      ░    ░  ░         ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
         ░                                                                                                                                      \033[0m
         
         """)

bcctags = [
    {"tag":"b","html":"b"},
    {"tag":"u","html":"u"},
    {"tag":"i","html":"i"}
]

# test = 'a'
# test.replace('a','b')
# print(test)

page = {}

page["title"] = input('Please enter game title: ')
page["desc"]  = input('Please enter game description: ')
page["dname"]  = input('Please enter game download name: ')
page["dins"]  = input('Please enter game download instructions: ')
for i in bcctags:
    page["desc"]  = page["desc"].replace(("["+i["tag"]+"]"),("<"+i["html"]+">"))
    page["desc"]  = page["desc"].replace(("[/"+i["tag"]+"]"),("</"+i["html"]+">"))
    page["dins"]  = page["dins"].replace(("["+i["tag"]+"]"),("<"+i["html"]+">"))
    page["dins"]  = page["dins"].replace(("[/"+i["tag"]+"]"),("</"+i["html"]+">"))
    pass
print(page)

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu%3A400%2C400italic%2C700%2C700italic" type="text/css" rel="stylesheet">
    <title>Supra games - cool games by cool people</title>
</head>
<body>
    <header align="center">
            <img alt="logo" src="../icon.png">
            <div style="width: calc(100% - (30px + (7.5px * 2)))">
                <a title="NOT FUNCTIONAL!">Games</a>
            </div>
    </header>

    <div class="main">
        <div class="collum-middle">
            <div class="game-header">
                <h2>[NAME]</h2>
                <!-- <img class="thumbnail" alt="thumbnail"  src="https://placekitten.com/500/175"> -->
            </div>
            <div class="game-content">
                <div class="game-iframe">
                    <iframe src="https://v6p9d9t4.ssl.hwcdn.net/html/7552717/index.html" allow="autoplay; fullscreen *; geolocation; microphone; camera; midi; monetization; xr-spatial-tracking; gamepad; gyroscope; accelerometer; xr; cross-origin-isolated" allowtransparency="true" allowfullscreen="true" mozallowfullscreen="true" msallowfullscreen="true" scrolling="no" id="game_drop" webkitallowfullscreen="true" frameborder="0" width="100%"></iframe>
                </div>
                <p>[DESC]</p>

                <div class="uploads">
                    <h2 id="download">Download</h2>
                    <div id="upload_list_2743036" class="upload_list_widget base_widget">
                        <div class="upload"><a href="javascript:void(0);" data-upload_id="7552750" class="button download_btn">Download</a>
                            <div class="info_column">
                                <div class="upload_name">
                                    <strong title="Supra cow 2_ Day One_assets.zip" class="name">[DNAME]</strong> 
                                    <span class="file_size"><span>38 MB</span></span> <span class="download_platforms"></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="download_instructions "><h2 id="instructions">Install instructions</h2>
                    <div class="formatted_description user_formatted">
                    <p>[DINS]</p>
                    </div>
                </div>

                
            </div>
        </div>
    </div>
        <center>
            <div class="bottom-links">
                <a href="..">Home</a>
            </div>
        </center>
</body>
</html>'''

template=template.replace('[NAME]',page["title"])

input("")
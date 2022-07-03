def title_header(pagename, header_active=False, dark=False, search_text='', selectedmobile='', from_video=''):
    g = ''
    darkstyle = '''
<style>
body {
    background-color:#2e2d2d
}
</style>
        '''
    if header_active=='home': activehome='active'
    else: activehome = ''
    if header_active=='video': activevideo='active'
    else: activevideo = ''
    if selectedmobile !='': selectedmobile='checked'
    if from_video==True: from_video='<input type="checkbox" name="fromvideo" value="True" checked style="display:none">'
    page = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>{page_name}</title>
    <link rel="stylesheet" href="../assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../assets/fonts/fontawesome-all.min.css">
    <link rel="stylesheet" href="../assets/css/header_styles.css">
</head>

<body>
    <header style="text-align: right;border-style: none;">
        <nav class="navbar navbar-light navbar-expand-md py-3" style="box-shadow: 2px 0px 6px;background: var(--bs-gray-dark);border-style: none;height: 67px;">
            <div class="container"><a class="navbar-brand d-flex align-items-center" href="http://192.168.3.33"><span class="bs-icon-sm bs-icon-rounded bs-icon-primary d-flex justify-content-center align-items-center me-2 bs-icon" style="background: #f38021;"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none">
                            <path d="M9 6C8.44772 6 8 6.44772 8 7C8 7.55228 8.44772 8 9 8H15C15.5523 8 16 7.55228 16 7C16 6.44772 15.5523 6 15 6H9Z" fill="currentColor"></path>
                            <path d="M9 10C8.44772 10 8 10.4477 8 11C8 11.5523 8.44772 12 9 12H15C15.5523 12 16 11.5523 16 11C16 10.4477 15.5523 10 15 10H9Z" fill="currentColor"></path>
                            <path d="M13 17C13 17.5523 12.5523 18 12 18C11.4477 18 11 17.5523 11 17C11 16.4477 11.4477 16 12 16C12.5523 16 13 16.4477 13 17Z" fill="currentColor"></path>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M4 5C4 3.34315 5.34315 2 7 2H17C18.6569 2 20 3.34315 20 5V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V5ZM7 4H17C17.5523 4 18 4.44772 18 5V19C18 19.5523 17.5523 20 17 20H7C6.44772 20 6 19.5523 6 19V5C6 4.44772 6.44771 4 7 4Z" fill="currentColor"></path>
                        </svg></span><span style="padding: 0px;padding-top: 0px;padding-bottom: 2px;font-size: 23px;">Home server</span></a><button data-bs-toggle="collapse" class="navbar-toggler" data-bs-target="#navcol-1"><span class="visually-hidden">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse text-center" id="navcol-1" style="text-align: center;background: #343a40;">
                    <ul class="navbar-nav me-auto">
                        <li class="nav-item"><a class="nav-link {active_home}" href="http://192.168.3.33" style="font-size: 18px;text-align: center;">Home</a></li>
                        <li class="nav-item dropdown"><a class="dropdown-toggle nav-link d-xl-flex align-items-xl-center" aria-expanded="false" data-bs-toggle="dropdown" href="#" style="height: 43px;text-align: center;font-size: 18px;">Useful tools</a>
                            <div class="dropdown-menu"><a class="dropdown-item" href="https://192.168.3.33:10000">Webmin</a><a class="dropdown-item" href="http://192.168.3.33:12345">Transmission</a><a class="dropdown-item" href="http://192.168.3.33:789">Wiki</a></div>
                        </li>
                        <li class="nav-item" style="font-size: 18px;text-align: center;"><a class="nav-link {active_video}" href="http://192.168.3.33/videoview.py" style="font-size: 18px;text-align: center;">Videoview</a></li>
                    </ul>
                    <form class="d-flex align-items-xl-center" action="../cgi-bin/search.py">
                        <div class="container" style="width: 186px;text-align: left;margin-left: 0px;margin-right: 0px;">
                            <div class="row">
                                <div class="col-md-12" style="max-height: 26px;">
                                    <p style="color: var(--bs-light);font-weight: bold;font-size: 15px;">Search options</p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="form-check"><input class="form-check-input" type="checkbox" id="formCheck-4" name="searchtype" value="channel"><label class="form-check-label" for="formCheck-4" style="color: var(--bs-light);">Search by category</label></div>
                                </div>
                            </div>
                        </div>
                        <div class="container" style="width: 153px;text-align: left;margin-right: 0px;margin-left: 0px;">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="form-check" style="width: 100px;"><input class="form-check-input" type="checkbox" id="formCheck-1" name="device" value="mobile" {selected_mobile}><label class="form-check-label" for="formCheck-1" style="color: var(--bs-light);">Mobile</label></div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="form-check"><input class="form-check-input" type="checkbox" id="formCheck-2" name="searchtype" value="type"><label class="form-check-label" for="formCheck-2" style="color: var(--bs-light);">By type</label></div>
                                </div>
                            </div>
                        </div><input class="form-control" type="search" style="height: 36px;color: rgb(255,255,255);background: rgb(66,74,82);border-style: solid;border-color: rgb(37,41,45);border-top-width: 1px;border-right-style: none;border-bottom-width: 1px;border-left-width: 1px;text-align: center;padding-bottom: 4px;width: 184.062px;" required value="{search_value}" placeholder="Search..." name="filename"><button class="btn btn-primary" type="submit" style="border-radius: 0;background: #f38021;width: 38.0156px;border-style: solid;border-color: rgb(37,41,45);border-top-style: none;padding: 0px;min-height: 36px;text-align: center;"><i class="fas fa-search" style="font-size: 22px;"></i></button>
                        {fromvideo}
                    </form>
                </div>
            </div>
        </nav>
    </header>
    <script src="../assets/bootstrap/js/bootstrap.min.js"></script>
    '''
    return g + page.format(page_name=pagename, active_home=activehome, active_video=activevideo, search_value=search_text, selected_mobile=selectedmobile, fromvideo=from_video, dark_style=darkstyle)

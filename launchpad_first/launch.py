import webview, os, configparser, webbrowser

# 1) Read config
cfg = configparser.ConfigParser()
cfg.read('config.ini')
c = cfg['DEFAULT']

# 2) Template path
TEMPLATE = os.path.join(os.path.dirname(__file__), 'splash.html')

# 3) Render-splash replaces placeholders in splash.html
def render_splash():
    tpl = open(TEMPLATE, 'r', encoding='utf-8').read()
    return tpl.format(
        project_name    = c.get('project_name', fallback='LaunchPad'),
        logo_main       = c.get('logo_main', fallback='logo.png'),
        logo_partner    = c.get('logo_partner', fallback='partner-logo.png'),
        author          = 'Kasim Janci',
        website_url     = c.get('website_url', fallback='#'),
        splash_duration = c.get('splash_duration', fallback='3000')
    )

# 4) JS↔Python bridge
class Api:
    def open_github(self):
        webbrowser.open(c.get('github_url', fallback='#'))
    def open_website(self):
        webbrowser.open(c.get('website_url', fallback='#'))
    def close_splash(self):
        webview.windows[0].destroy()

# 5) Launch the splash window
def show_splash():
    html = render_splash()
    webview.create_window(
        title='',
        html=html,
        width=800,
        height=450,
        frameless=True,
        resizable=False,
        easy_drag=True,
        confirm_close=False,
        js_api=Api()
    )
    webview.start(gui='cef')

if __name__ == '__main__':
    show_splash()
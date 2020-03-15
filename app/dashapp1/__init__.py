import dash
from .build_layout import layout
from .callbacks import register_callbacks
from .controls import assets_folder


def create_app(server):
    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
    }

    # CSS
    external_stylesheets = ['/static/bootstrap.css',
                            '/static/style.css',
                            '/static/navbar.css']

    # dash app
    dashapp = dash.Dash(__name__,
                        server=server,
                        url_base_pathname='/apps/dummy_app/',
                        assets_folder=assets_folder,
                        assets_ignore="bootstrap.css",
                        external_stylesheets=external_stylesheets,
                        meta_tags=[meta_viewport]
                        )

    with server.app_context():
        dashapp.title = 'Dummy App'
        dashapp.layout = layout()
        register_callbacks(dashapp)

    return dashapp

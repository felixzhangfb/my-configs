c = get_config()  # type: ignore

# ------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
# ------------------------------------------------------------------------------
c.Application.log_level = 40

# ------------------------------------------------------------------------------
# LabApp(LabServerApp) configuration
# ------------------------------------------------------------------------------
c.LabApp.extension_manager = False
c.LabApp.open_browser = False

# ------------------------------------------------------------------------------
# ServerApp(JupyterApp) configuration
# ------------------------------------------------------------------------------
c.ServerApp.allow_remote_access = False
c.ServerApp.autoreload = True
c.ServerApp.ip = 'localhost'
c.ServerApp.port = 8888
c.ServerApp.root_dir = ''
